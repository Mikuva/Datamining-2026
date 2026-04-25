from __future__ import annotations

"""CZSO IKZ patch v7.

Goals:
- keep the v5 year-detection fixes,
- exclude datasets whose latest available year is older than 2020,
- for one-year snapshot datasets from 2020-2023, build HEAD/TAIL from the
  full dataset instead of an empty target-year filtered subset,
- preserve territorial ordering (municipality first) while grouping yearly
  variants of the same dataset family together.

This module supports both:
1) a fresh end-to-end run over the catalogue;
2) patching / resorting an already generated output directory without
   re-running the entire several-hour pipeline.
"""

import argparse
import json
import os
import re
import shutil
import sys
import time
from dataclasses import asdict, fields
from pathlib import Path
from typing import Any, Iterable, Sequence

import pandas as pd

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

import czso_ikz_a_to_z_v5 as pipeline  # noqa: E402
import czso_ikz_territory_patch as territory  # noqa: E402
import _czso_ikz_a_to_z_v4_base as base  # noqa: E402
import pyczso  # noqa: E402
from pyczso_lkod_bridge import LKODBridge, detect_encoding  # noqa: E402


# Re-export notebook-friendly helpers.
TablePreview = pipeline.TablePreview
DatasetAssessment = pipeline.DatasetAssessment
TARGET_YEARS_DEFAULT = list(pipeline.TARGET_YEARS_DEFAULT)
PROBE_ROWS_DEFAULT = pipeline.PROBE_ROWS_DEFAULT
read_catalogue = pipeline.read_catalogue
ORIGINAL_SELECT_RELEVANT_DATASETS = pipeline.select_relevant_datasets
build_summary_tables = pipeline.build_summary_tables
assessment_display_series = pipeline.assessment_display_series
format_years_sample = pipeline.format_years_sample
sanitize_filename = pipeline.sanitize_filename
Markdown = pipeline.Markdown
_display = pipeline.display

HISTORICAL_CUTOFF_YEAR = 2020
SNAPSHOT_FULL_PREVIEW_MIN_YEAR = 2020
SNAPSHOT_FULL_PREVIEW_MAX_YEAR = 2023

CATEGORY_ORDER = dict(base.CATEGORY_ORDER)

YEAR_ONLY_RE = re.compile(r"\b(18|19|20)\d{2}\b")


def _clean(value: Any) -> Any:
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except Exception:
        pass
    return value


def _text(value: Any) -> str:
    return base.clean_string(value) or ""


def _normalize(value: Any) -> str:
    return base.normalize_name(_text(value))


def _parse_years_from_any(*values: Any) -> list[int]:
    years: set[int] = set()
    for value in values:
        years.update(base.extract_years_from_value(value))
    return sorted(years)


def infer_latest_year_from_row(row: pd.Series | dict[str, Any]) -> int | None:
    getter = row.get if hasattr(row, "get") else lambda k, d=None: d

    years: set[int] = set()

    # Most reliable: already profiled years.
    for key in ["years_min", "years_max"]:
        years.update(base.extract_years_from_value(getter(key)))

    # Catalog range.
    years.update(base.parse_catalog_years(getter("start_catalog"), getter("end_catalog")))
    years.update(base.parse_catalog_years(getter("start"), getter("end")))

    # Title / family / id fallbacks.
    years.update(_parse_years_from_any(
        getter("dataset_title"),
        getter("title"),
        getter("rodina_datasetu"),
        getter("dataset_id"),
    ))

    if not years:
        return None
    return max(int(y) for y in years)


def infer_all_years_from_row(row: pd.Series | dict[str, Any]) -> list[int]:
    getter = row.get if hasattr(row, "get") else lambda k, d=None: d
    years: set[int] = set()

    # Profiled years if available.
    y_min = _clean(getter("years_min"))
    y_max = _clean(getter("years_max"))
    y_count = _clean(getter("years_count"))
    try:
        if y_min is not None and y_max is not None:
            ymin = int(float(y_min))
            ymax = int(float(y_max))
            if ymin == ymax:
                years.add(ymin)
            elif y_count is not None and int(float(y_count)) <= 12 and ymin <= ymax and ymax - ymin <= 15:
                years.update(range(ymin, ymax + 1))
            else:
                years.update({ymin, ymax})
    except Exception:
        pass

    years.update(base.parse_catalog_years(getter("start_catalog"), getter("end_catalog")))
    years.update(base.parse_catalog_years(getter("start"), getter("end")))
    years.update(_parse_years_from_any(getter("dataset_title"), getter("title"), getter("rodina_datasetu"), getter("dataset_id")))

    return sorted(years)


def should_exclude_historical_row(row: pd.Series | dict[str, Any], *, cutoff_year: int = HISTORICAL_CUTOFF_YEAR) -> bool:
    latest = infer_latest_year_from_row(row)
    return latest is not None and latest < int(cutoff_year)


def select_relevant_datasets(catalogue: pd.DataFrame, *, cutoff_year: int = HISTORICAL_CUTOFF_YEAR) -> pd.DataFrame:
    df = ORIGINAL_SELECT_RELEVANT_DATASETS(catalogue).copy()
    latest_years = []
    exclude_flags = []
    for _, row in df.iterrows():
        latest = infer_latest_year_from_row(row)
        latest_years.append(latest)
        exclude_flags.append(latest is not None and latest < int(cutoff_year))
    df["latest_year_hint"] = latest_years
    df["excluded_historical"] = exclude_flags
    df = df.loc[~pd.Series(exclude_flags, index=df.index)].copy()
    df = df.reset_index(drop=True)
    return df


def _should_use_full_preview_for_single_snapshot(years: Sequence[int] | None) -> bool:
    if not years:
        return False
    uniq = sorted({int(y) for y in years})
    return len(uniq) == 1 and SNAPSHOT_FULL_PREVIEW_MIN_YEAR <= uniq[0] <= SNAPSHOT_FULL_PREVIEW_MAX_YEAR


def _time_columns_and_years_from_probe(df: pd.DataFrame) -> tuple[str | None, list[str], set[int], list[str]]:
    column_names = [str(c) for c in df.columns]
    best_time_col, _, time_columns = pipeline.detect_year_column(df)
    header_years = base.years_from_strings(column_names)
    years: set[int] = set(header_years)
    return best_time_col, time_columns, years, column_names


def load_csv_preview(
    path: Path,
    *,
    head_rows: int,
    tail_rows: int,
    chunksize: int = 50000,
    probe_rows: int = PROBE_ROWS_DEFAULT,
    target_years: Sequence[int] | None = None,
    filter_preview_to_target_years: bool = False,
) -> TablePreview:
    probe_nrows = max(head_rows, probe_rows)
    probe_df = base.csv_read_attempts(path, nrows=probe_nrows)
    best_time_col, time_columns, years, column_names = _time_columns_and_years_from_probe(probe_df)
    column_count = len(column_names)
    header_years = base.years_from_strings(column_names)
    years_source: str | None = "header_columns" if header_years else None

    total_rows = 0
    matched_rows = 0
    raw = base.read_bytes_head(path)
    last_exc: Exception | None = None

    full_head_df = probe_df.head(head_rows).copy()
    full_tail_df: pd.DataFrame | None = None

    filtered_head_df: pd.DataFrame | None = None
    filtered_tail_df: pd.DataFrame | None = None
    if not (filter_preview_to_target_years and target_years and best_time_col):
        filtered_head_df = full_head_df.copy()

    for enc in detect_encoding(raw):
        try:
            for chunk in pd.read_csv(path, encoding=enc, sep=None, engine="python", chunksize=chunksize):
                total_rows += len(chunk)
                if full_tail_df is None:
                    full_tail_df = chunk.tail(tail_rows).copy()
                else:
                    full_tail_df = pd.concat([full_tail_df, chunk], ignore_index=True).tail(tail_rows).copy()

                for col in time_columns:
                    if col in chunk.columns:
                        years.update(base.series_years(chunk[col]))

                if filter_preview_to_target_years and target_years and best_time_col and best_time_col in chunk.columns:
                    filtered_chunk, matched = pipeline.filter_dataframe_to_target_years(chunk, best_time_col, target_years)
                    matched_rows += matched
                    if filtered_head_df is None:
                        filtered_head_df = filtered_chunk.head(head_rows).copy()
                    elif len(filtered_head_df) < head_rows and not filtered_chunk.empty:
                        filtered_head_df = pd.concat([filtered_head_df, filtered_chunk], ignore_index=True).head(head_rows).copy()
                    if filtered_tail_df is None:
                        filtered_tail_df = filtered_chunk.tail(tail_rows).copy()
                    else:
                        filtered_tail_df = pd.concat([filtered_tail_df, filtered_chunk], ignore_index=True).tail(tail_rows).copy()
                else:
                    if filtered_tail_df is None:
                        filtered_tail_df = chunk.tail(tail_rows).copy()
                    else:
                        filtered_tail_df = pd.concat([filtered_tail_df, chunk], ignore_index=True).tail(tail_rows).copy()

            last_exc = None
            break
        except Exception as exc:
            total_rows = 0
            matched_rows = 0
            full_tail_df = None
            filtered_tail_df = None
            filtered_head_df = None if (filter_preview_to_target_years and target_years and best_time_col) else full_head_df.copy()
            years = set(header_years)
            last_exc = exc
            continue

    if last_exc is not None:
        raise RuntimeError(f"CSV streaming failed for {path.name}: {last_exc}")

    years_sorted = sorted(years)
    if years_sorted and time_columns:
        years_source = "data_columns"

    notes: list[str] = ["roky načteny z celého souboru po chunkách"]

    use_full_snapshot_preview = _should_use_full_preview_for_single_snapshot(years_sorted)
    if use_full_snapshot_preview:
        head_df = full_head_df.copy()
        tail_df = (full_tail_df if full_tail_df is not None else probe_df.tail(tail_rows).copy())
        notes.append(
            f"dataset obsahuje jediný rok {years_sorted[0]} v intervalu {SNAPSHOT_FULL_PREVIEW_MIN_YEAR}-{SNAPSHOT_FULL_PREVIEW_MAX_YEAR}; head/tail jsou z celého datasetu"
        )
    elif filter_preview_to_target_years and target_years:
        if best_time_col:
            notes.append(f"head/tail filtrovány na target years {list(target_years)} přes sloupec `{best_time_col}`; matching_rows={matched_rows}")
            head_df = filtered_head_df if filtered_head_df is not None else probe_df.head(0).copy()
            tail_df = filtered_tail_df if filtered_tail_df is not None else probe_df.head(0).copy()
        else:
            notes.append("head/tail zůstaly nefiltrované: nebyl nalezen spolehlivý řádkový časový sloupec")
            head_df = full_head_df.copy()
            tail_df = (full_tail_df if full_tail_df is not None else probe_df.tail(tail_rows).copy())
    else:
        head_df = full_head_df.copy()
        tail_df = (filtered_tail_df if filtered_tail_df is not None else full_tail_df if full_tail_df is not None else probe_df.tail(tail_rows).copy())

    return TablePreview(
        head_df=head_df,
        tail_df=tail_df,
        row_count=int(total_rows),
        column_count=int(column_count),
        column_names=column_names,
        time_columns=time_columns,
        years=years_sorted,
        years_source=years_source,
        selected_file=path.name,
        selected_sheet=None,
        selected_format="csv",
        notes=" | ".join(notes),
    )


def load_excel_preview(
    path: Path,
    *,
    head_rows: int,
    tail_rows: int,
    probe_rows: int = PROBE_ROWS_DEFAULT,
    target_years: Sequence[int] | None = None,
    filter_preview_to_target_years: bool = False,
) -> TablePreview:
    full = pd.read_excel(path)
    probe_df = full.head(max(head_rows, probe_rows)).copy()
    column_names = [str(c) for c in full.columns]
    best_time_col, _, time_columns = pipeline.detect_year_column(probe_df)
    years, years_source = pipeline._years_from_dataframe(full, time_columns, column_names)

    notes: list[str] = ["roky načteny z celého sešitu"]
    if _should_use_full_preview_for_single_snapshot(years):
        preview_df = full
        notes.append(
            f"dataset obsahuje jediný rok {years[0]} v intervalu {SNAPSHOT_FULL_PREVIEW_MIN_YEAR}-{SNAPSHOT_FULL_PREVIEW_MAX_YEAR}; head/tail jsou z celého datasetu"
        )
    elif filter_preview_to_target_years and target_years:
        if best_time_col and best_time_col in full.columns:
            preview_df, matched_rows = pipeline.filter_dataframe_to_target_years(full, best_time_col, target_years)
            notes.append(f"head/tail filtrovány na target years {list(target_years)} přes sloupec `{best_time_col}`; matching_rows={matched_rows}")
        else:
            preview_df = full
            notes.append("head/tail zůstaly nefiltrované: nebyl nalezen spolehlivý řádkový časový sloupec")
    else:
        preview_df = full

    return TablePreview(
        head_df=preview_df.head(head_rows).copy(),
        tail_df=preview_df.tail(tail_rows).copy(),
        row_count=int(len(full)),
        column_count=int(len(full.columns)),
        column_names=column_names,
        time_columns=time_columns,
        years=years,
        years_source=years_source,
        selected_file=path.name,
        selected_sheet=None,
        selected_format=path.suffix.lower().lstrip("."),
        notes=" | ".join(notes),
    )


def load_dataframe_preview(
    df: pd.DataFrame,
    *,
    head_rows: int,
    tail_rows: int,
    selected_file: str | None = None,
    probe_rows: int = PROBE_ROWS_DEFAULT,
    target_years: Sequence[int] | None = None,
    filter_preview_to_target_years: bool = False,
) -> TablePreview:
    probe_df = df.head(max(head_rows, probe_rows)).copy()
    column_names = [str(c) for c in df.columns]
    best_time_col, _, time_columns = pipeline.detect_year_column(probe_df)
    years, years_source = pipeline._years_from_dataframe(df, time_columns, column_names)

    notes: list[str] = ["roky načteny z celého DataFrame"]
    if _should_use_full_preview_for_single_snapshot(years):
        preview_df = df
        notes.append(
            f"dataset obsahuje jediný rok {years[0]} v intervalu {SNAPSHOT_FULL_PREVIEW_MIN_YEAR}-{SNAPSHOT_FULL_PREVIEW_MAX_YEAR}; head/tail jsou z celého datasetu"
        )
    elif filter_preview_to_target_years and target_years:
        if best_time_col and best_time_col in df.columns:
            preview_df, matched_rows = pipeline.filter_dataframe_to_target_years(df, best_time_col, target_years)
            notes.append(f"head/tail filtrovány na target years {list(target_years)} přes sloupec `{best_time_col}`; matching_rows={matched_rows}")
        else:
            preview_df = df
            notes.append("head/tail zůstaly nefiltrované: nebyl nalezen spolehlivý řádkový časový sloupec")
    else:
        preview_df = df

    return TablePreview(
        head_df=preview_df.head(head_rows).copy(),
        tail_df=preview_df.tail(tail_rows).copy(),
        row_count=int(len(df)),
        column_count=int(len(df.columns)),
        column_names=column_names,
        time_columns=time_columns,
        years=years,
        years_source=years_source,
        selected_file=selected_file,
        selected_sheet=None,
        selected_format="datastat_csv",
        notes=" | ".join(notes),
    )


def load_zip_preview(
    path: Path,
    *,
    head_rows: int,
    tail_rows: int,
    target_years: Sequence[int] | None = None,
    filter_preview_to_target_years: bool = False,
) -> TablePreview:
    temp_prefix = f"extract_{base.sanitize_filename(path.stem, max_len=40)}_"
    with base.tempfile.TemporaryDirectory(dir=path.parent, prefix=temp_prefix) as tmpdir:
        extract_dir = Path(tmpdir)
        with base.zipfile.ZipFile(path, "r") as zf:
            zf.extractall(extract_dir)
        candidates = [p for p in extract_dir.rglob("*") if p.is_file() and p.suffix.lower() in {".csv", ".xlsx", ".xls", ".xlsm"}]
        if not candidates:
            return TablePreview(
                head_df=None,
                tail_df=None,
                row_count=None,
                column_count=None,
                column_names=[],
                time_columns=[],
                years=[],
                years_source=None,
                selected_file=None,
                selected_sheet=None,
                selected_format="zip",
                notes="Archiv neobsahuje CSV/XLSX soubor, který by šel automaticky profilovat.",
            )
        chosen = base.choose_archive_table_file(candidates)
        if chosen.suffix.lower() == ".csv":
            preview = load_csv_preview(
                chosen,
                head_rows=head_rows,
                tail_rows=tail_rows,
                target_years=target_years,
                filter_preview_to_target_years=filter_preview_to_target_years,
            )
        else:
            preview = load_excel_preview(
                chosen,
                head_rows=head_rows,
                tail_rows=tail_rows,
                target_years=target_years,
                filter_preview_to_target_years=filter_preview_to_target_years,
            )
        note = f"Archiv obsahuje {len(candidates)} čitelných souborů; použit byl vybraný soubor `{chosen.name}`."
        preview.notes = note if not preview.notes else f"{preview.notes} | {note}"
        preview.selected_format = f"zip->{preview.selected_format}"
        preview.selected_file = chosen.name
        return preview


def fetch_dataset_preview(
    datastat_client: pyczso.CZSOClient,
    lkod_bridge: LKODBridge,
    dataset_id: str,
    *,
    head_rows: int,
    tail_rows: int,
    download_dir: Path,
    force_redownload: bool,
    cleanup_downloaded_files: bool = True,
) -> tuple[TablePreview | None, str | None, str | None, str | None, str, str | None]:
    lkod_error: str | None = None
    local_path: Path | None = None
    try:
        try:
            pointer = lkod_bridge.download_resource(dataset_id, dest_dir=download_dir, force_redownload=force_redownload)
            local_path = Path(pointer["download_path"])
            ext = str(pointer.get("extension") or local_path.suffix.lstrip(".")).lower()
            source_title = base.clean_string(pointer.get("title")) or base.clean_string(pointer.get("format"))
            if ext == "csv":
                preview = load_csv_preview(
                    local_path,
                    head_rows=head_rows,
                    tail_rows=tail_rows,
                    target_years=pipeline._CURRENT_TARGET_YEARS_FOR_PREVIEW,
                    filter_preview_to_target_years=pipeline._FILTER_PREVIEW_TO_TARGET_YEARS,
                )
            elif ext in {"xlsx", "xls", "xlsm"}:
                preview = load_excel_preview(
                    local_path,
                    head_rows=head_rows,
                    tail_rows=tail_rows,
                    target_years=pipeline._CURRENT_TARGET_YEARS_FOR_PREVIEW,
                    filter_preview_to_target_years=pipeline._FILTER_PREVIEW_TO_TARGET_YEARS,
                )
            elif ext == "zip":
                preview = load_zip_preview(
                    local_path,
                    head_rows=head_rows,
                    tail_rows=tail_rows,
                    target_years=pipeline._CURRENT_TARGET_YEARS_FOR_PREVIEW,
                    filter_preview_to_target_years=pipeline._FILTER_PREVIEW_TO_TARGET_YEARS,
                )
            else:
                return None, "LKOD", f"resource#{pointer.get('resource_num')}", source_title, "UNSUPPORTED_FORMAT", f"Stažený formát `{ext}` není podporovaný pro preview head/tail."
            return preview, "LKOD", f"resource#{pointer.get('resource_num')}", source_title, "OK_LKOD", preview.notes
        except Exception as exc:
            lkod_error = str(exc)
    finally:
        if cleanup_downloaded_files:
            base.remove_path_quietly(local_path)

    try:
        selections = datastat_client.get_dataset_selections(dataset_id, as_frame=True)
    except Exception as exc:
        msg = f"LKOD/VDB selhalo: {lkod_error} | DataStat metadata selhala: {exc}" if lkod_error else f"DataStat metadata selhala: {exc}"
        return None, None, None, None, "ERROR_SELECTIONS", msg

    selection_code, selection_title, selection_count = base.choose_selection(selections)
    if not selection_code:
        msg = f"Nebyl nalezen použitelný výběr. Počet nalezených výběrů: {selection_count}"
        if lkod_error:
            msg = f"LKOD/VDB selhalo: {lkod_error} | {msg}"
        return None, "DATASTAT", None, None, "NO_SELECTION", msg

    try:
        df = datastat_client.get_table(selection_code, format="CSV")
    except Exception as exc:
        msg = f"Stažení DataStat výběru selhalo: {exc}"
        if lkod_error:
            msg = f"LKOD/VDB selhalo: {lkod_error} | {msg}"
        return None, "DATASTAT", selection_code, selection_title, "ERROR_TABLE", msg
    if not isinstance(df, pd.DataFrame):
        msg = "DataStat API nevrátilo DataFrame."
        if lkod_error:
            msg = f"LKOD/VDB selhalo: {lkod_error} | {msg}"
        return None, "DATASTAT", selection_code, selection_title, "ERROR_TABLE", msg

    preview = load_dataframe_preview(
        df,
        head_rows=head_rows,
        tail_rows=tail_rows,
        selected_file=f"selection_{selection_code}.csv",
        target_years=pipeline._CURRENT_TARGET_YEARS_FOR_PREVIEW,
        filter_preview_to_target_years=pipeline._FILTER_PREVIEW_TO_TARGET_YEARS,
    )
    return preview, "DATASTAT", selection_code, selection_title, "OK_DATASTAT", lkod_error


def _apply_runtime_monkeypatches() -> dict[str, Any]:
    original = {
        "select_relevant_datasets": base.select_relevant_datasets,
        "fetch_dataset_preview": base.fetch_dataset_preview,
    }
    base.select_relevant_datasets = select_relevant_datasets  # type: ignore[assignment]
    base.fetch_dataset_preview = fetch_dataset_preview  # type: ignore[assignment]
    return original


def _restore_runtime_monkeypatches(original: dict[str, Any]) -> None:
    for name, value in original.items():
        setattr(base, name, value)


def _family_key_from_row(row: pd.Series | dict[str, Any]) -> str:
    getter = row.get if hasattr(row, "get") else lambda k, d=None: d
    family = _text(getter("rodina_datasetu")) or _text(getter("dataset_title")) or _text(getter("dataset_id"))
    if family:
        return _normalize(family)
    return _normalize(getter("dataset_id")) or "dataset"


def _variant_year_from_row(row: pd.Series | dict[str, Any]) -> int:
    getter = row.get if hasattr(row, "get") else lambda k, d=None: d

    y_min = _clean(getter("years_min"))
    y_max = _clean(getter("years_max"))
    try:
        if y_min is not None and y_max is not None:
            ymin = int(float(y_min))
            ymax = int(float(y_max))
            if ymin == ymax:
                return ymin
            return ymax
    except Exception:
        pass

    years = base.parse_catalog_years(getter("start_catalog"), getter("end_catalog"))
    if not years:
        years = base.parse_catalog_years(getter("start"), getter("end"))
    if years:
        return max(int(y) for y in years)

    title_years = _parse_years_from_any(getter("dataset_title"), getter("title"), getter("dataset_id"))
    if title_years:
        return max(title_years)
    return 9999


def _sort_manifest_by_territory_and_family(
    manifest_df: pd.DataFrame,
    *,
    output_dir: Path | None = None,
) -> tuple[pd.DataFrame, list[str]]:
    working = manifest_df.copy()
    if working.empty:
        return working, []

    working["original_order"] = pd.to_numeric(working.get("order"), errors="coerce")
    if working["original_order"].isna().all():
        working["original_order"] = range(1, len(working) + 1)
    else:
        missing_mask = working["original_order"].isna()
        if missing_mask.any():
            max_ord = int(pd.to_numeric(working["original_order"], errors="coerce").max() or 0)
            filler = list(range(max_ord + 1, max_ord + 1 + int(missing_mask.sum())))
            working.loc[missing_mask, "original_order"] = filler

    scopes: list[str] = []
    scope_labels: list[str] = []
    scope_ranks: list[int] = []
    scope_evidence: list[str] = []
    preview_cache: dict[tuple[Any, Any, Any, Any], tuple[pd.DataFrame | None, pd.DataFrame | None, dict[str, Any] | None]] = {}
    out_dir = Path(output_dir) if output_dir is not None else None

    for _, row in working.iterrows():
        head_df = tail_df = None
        meta = None
        if out_dir is not None:
            cache_key = (row.get("dataset_id"), row.get("dataset_title"), row.get("head_csv"), row.get("tail_csv"))
            if cache_key not in preview_cache:
                preview_cache[cache_key] = territory._collect_preview_frames(row, out_dir)  # type: ignore[attr-defined]
            head_df, tail_df, meta = preview_cache[cache_key]
        scope, rank, evidence = territory.infer_territorial_scope(row, head_df=head_df, tail_df=tail_df, meta=meta)
        scopes.append(scope)
        scope_labels.append(territory.TERRITORIAL_SCOPE_LABELS.get(scope, scope))
        scope_ranks.append(rank)
        scope_evidence.append(evidence)

    working["territorial_scope"] = scopes
    working["territorial_scope_label"] = scope_labels
    working["territorial_rank"] = scope_ranks
    working["territorial_evidence"] = scope_evidence

    working["family_sort_key"] = working.apply(_family_key_from_row, axis=1)
    working["variant_year"] = working.apply(_variant_year_from_row, axis=1)

    working["_category_rank"] = working["category"].map(CATEGORY_ORDER).fillna(99).astype(int)
    working["_relevance_rank"] = pd.to_numeric(working.get("relevance_rank"), errors="coerce").fillna(99).astype(int)
    working["_has_years_sort"] = working.get("has_target_years", pd.Series(False, index=working.index)).fillna(False).astype(int) * -1
    working["_has_pk_sort"] = working.get("has_primary_key", pd.Series(False, index=working.index)).fillna(False).astype(int) * -1
    working["_years_max_sort"] = pd.to_numeric(working.get("years_max"), errors="coerce").fillna(-1)

    working["family_bucket_order"] = (
        working.groupby(["territorial_rank", "_category_rank", "family_sort_key"], dropna=False)["original_order"]
        .transform("min")
        .fillna(999999)
    )

    working = working.sort_values(
        [
            "territorial_rank",
            "_category_rank",
            "family_bucket_order",
            "variant_year",
            "_relevance_rank",
            "_has_years_sort",
            "_has_pk_sort",
            "_years_max_sort",
            "dataset_title",
            "dataset_id",
        ],
        ascending=[True, True, True, True, True, True, True, False, True, True],
        na_position="last",
    ).reset_index(drop=True)

    working["order"] = range(1, len(working) + 1)

    helper_cols = [
        "_category_rank",
        "_relevance_rank",
        "_has_years_sort",
        "_has_pk_sort",
        "_years_max_sort",
        "original_order",
        "family_bucket_order",
    ]
    working = working.drop(columns=[c for c in helper_cols if c in working.columns])

    removed_notes: list[str] = []
    return working, removed_notes


def _results_from_manifest_and_output(manifest_df: pd.DataFrame, output_dir: Path) -> list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]]:
    results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]] = []
    for _, row in manifest_df.iterrows():
        assessment = territory._row_to_assessment(row)  # type: ignore[attr-defined]
        head_df, tail_df, _ = territory._collect_preview_frames(row, output_dir)  # type: ignore[attr-defined]
        results.append((assessment, head_df, tail_df))
    results.sort(key=lambda item: int(getattr(item[0], "order", 999999)))
    return results


def _persist_manifest_and_results(output_dir: Path, manifest_df: pd.DataFrame, results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_df.to_csv(output_dir / "ikz_a_to_z_manifest.csv", index=False, encoding="utf-8-sig")
    try:
        territory._write_manifest_xlsx_with_territory(output_dir, manifest_df)  # type: ignore[attr-defined]
    except Exception:
        pass
    try:
        territory._write_territorial_markdown_report(output_dir, manifest_df, results)  # type: ignore[attr-defined]
    except Exception:
        pass
    if manifest_df.empty or not {"territorial_scope_label", "category"}.issubset(set(manifest_df.columns)):
        summary = pd.DataFrame(columns=["territorial_scope_label", "category", "dataset_count"])
    else:
        summary = (
            manifest_df.groupby(["territorial_scope_label", "category"], dropna=False)
            .size()
            .reset_index(name="dataset_count")
            .sort_values(["territorial_scope_label", "category"], na_position="last")
            .reset_index(drop=True)
        )
    summary.to_csv(output_dir / "datasets_by_territorial_scope.csv", index=False, encoding="utf-8-sig")


def _archive_orphan_preview_files(output_dir: Path, rows: Iterable[pd.Series], *, archive_dir_name: str = "_excluded_historical") -> None:
    archive_dir = output_dir / archive_dir_name
    archive_dir.mkdir(parents=True, exist_ok=True)
    for row in rows:
        for key in ["head_csv", "tail_csv", "metadata_json"]:
            rel = _text(row.get(key))
            if not rel:
                continue
            src = output_dir / Path(rel)
            if src.exists():
                dest = archive_dir / src.name
                try:
                    if dest.exists():
                        dest.unlink()
                    shutil.move(str(src), str(dest))
                except Exception:
                    pass


def _refresh_manifest_row_with_preview(
    row: pd.Series,
    preview: TablePreview,
    *,
    source_kind: str | None,
    source_code: str | None,
    source_title: str | None,
    status: str,
    error: str | None,
    output_dir: Path,
    head_rows: int,
    tail_rows: int,
) -> pd.Series:
    updated = row.copy()

    # Overwrite existing preview artifacts if paths exist, otherwise create them.
    head_rel = _text(updated.get("head_csv"))
    tail_rel = _text(updated.get("tail_csv"))
    meta_rel = _text(updated.get("metadata_json"))

    previews_dir = output_dir / "previews"
    previews_dir.mkdir(parents=True, exist_ok=True)

    if not head_rel or not tail_rel or not meta_rel:
        prefix = f"{sanitize_filename(_text(updated.get('category')) or 'X')}_{sanitize_filename(_text(updated.get('dataset_id')) or 'none')}_{sanitize_filename(_text(updated.get('dataset_title')) or _text(updated.get('rodina_datasetu')) or 'dataset', max_len=60)}"
        head_rel, tail_rel, meta_rel = base.write_preview_files(prefix, preview, previews_dir)
    else:
        if preview.head_df is not None:
            preview.head_df.to_csv(output_dir / Path(head_rel), index=False, encoding="utf-8-sig")
        if preview.tail_df is not None:
            preview.tail_df.to_csv(output_dir / Path(tail_rel), index=False, encoding="utf-8-sig")
        metadata = {
            "row_count": preview.row_count,
            "column_count": preview.column_count,
            "column_names": preview.column_names,
            "time_columns": preview.time_columns,
            "years": preview.years,
            "years_source": preview.years_source,
            "selected_file": preview.selected_file,
            "selected_sheet": preview.selected_sheet,
            "selected_format": preview.selected_format,
            "notes": preview.notes,
        }
        (output_dir / Path(meta_rel)).write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    years = preview.years or []
    updated["status"] = status
    updated["source_kind"] = source_kind
    updated["source_code"] = source_code
    updated["source_title"] = source_title
    updated["selected_file"] = preview.selected_file
    updated["selected_sheet"] = preview.selected_sheet
    updated["selected_format"] = preview.selected_format
    updated["row_count"] = preview.row_count
    updated["column_count"] = preview.column_count
    updated["time_columns"] = ", ".join(preview.time_columns) if preview.time_columns else None
    updated["years_min"] = min(years) if years else None
    updated["years_max"] = max(years) if years else None
    updated["years_count"] = len(years) if years else 0
    updated["years_sample"] = format_years_sample(years)
    updated["years_source"] = preview.years_source
    updated["head_csv"] = head_rel
    updated["tail_csv"] = tail_rel
    updated["metadata_json"] = meta_rel
    updated["error"] = error

    # Reclassify A-D with the updated preview.
    temp_preview = preview
    category, reason, has_target_years, present_years, missing_years, has_pk, pk_col, pk_kind, pk_note = base.classify_dataset(
        updated,
        temp_preview,
        status=status,
        target_years=pipeline._CURRENT_TARGET_YEARS_FOR_PREVIEW or TARGET_YEARS_DEFAULT,
        require_all_target_years=True,
    )
    updated["category"] = category
    updated["category_reason"] = reason
    updated["has_target_years"] = has_target_years
    updated["target_years_present"] = ", ".join(str(y) for y in present_years) if present_years else None
    updated["target_years_missing"] = ", ".join(str(y) for y in missing_years) if missing_years else None
    updated["has_primary_key"] = has_pk
    updated["primary_key_column"] = pk_col
    updated["primary_key_kind"] = pk_kind
    updated["primary_key_note"] = pk_note
    return updated


def refresh_recent_single_year_datasets(
    manifest_df: pd.DataFrame,
    *,
    output_dir: Path,
    target_years: Sequence[int] = TARGET_YEARS_DEFAULT,
    force_redownload: bool = False,
    pause_seconds: float = 0.0,
    cleanup_downloaded_files: bool = True,
) -> tuple[pd.DataFrame, list[str]]:
    working = manifest_df.copy()
    if working.empty:
        return working, []

    # Candidates: datasets whose only available year is 2020-2023.
    refresh_indices: list[int] = []
    refresh_logs: list[str] = []
    for idx, row in working.iterrows():
        years = infer_all_years_from_row(row)
        if len(set(years)) == 1 and years and SNAPSHOT_FULL_PREVIEW_MIN_YEAR <= years[0] <= SNAPSHOT_FULL_PREVIEW_MAX_YEAR:
            refresh_indices.append(idx)

    if not refresh_indices:
        return working, refresh_logs

    old_years = pipeline._CURRENT_TARGET_YEARS_FOR_PREVIEW
    old_filter = pipeline._FILTER_PREVIEW_TO_TARGET_YEARS
    pipeline._CURRENT_TARGET_YEARS_FOR_PREVIEW = [int(y) for y in target_years]
    pipeline._FILTER_PREVIEW_TO_TARGET_YEARS = True

    datastat_client = pyczso.CZSOClient()
    lkod_bridge = LKODBridge()
    downloads_dir = Path(output_dir) / "_downloads"
    downloads_dir.mkdir(parents=True, exist_ok=True)

    try:
        for idx in refresh_indices:
            row = working.loc[idx]
            dataset_id = _text(row.get("dataset_id"))
            if not dataset_id:
                continue
            try:
                preview, source_kind, source_code, source_title, status, error = fetch_dataset_preview(
                    datastat_client,
                    lkod_bridge,
                    dataset_id,
                    head_rows=5,
                    tail_rows=5,
                    download_dir=downloads_dir,
                    force_redownload=force_redownload,
                    cleanup_downloaded_files=cleanup_downloaded_files,
                )
                if preview is None:
                    refresh_logs.append(f"{dataset_id}: preview se nepodařilo obnovit ({status})")
                    continue
                updated_row = _refresh_manifest_row_with_preview(
                    row,
                    preview,
                    source_kind=source_kind,
                    source_code=source_code,
                    source_title=source_title,
                    status=status,
                    error=error,
                    output_dir=output_dir,
                    head_rows=5,
                    tail_rows=5,
                )
                working.loc[idx] = updated_row
                refresh_logs.append(f"{dataset_id}: obnoveno full preview pro jednoletý dataset {infer_all_years_from_row(updated_row)}")
            except Exception as exc:
                refresh_logs.append(f"{dataset_id}: chyba při obnově preview ({exc})")
            if pause_seconds > 0:
                time.sleep(pause_seconds)
    finally:
        try:
            datastat_client.session.close()  # type: ignore[attr-defined]
        except Exception:
            pass
        try:
            lkod_bridge.close()
        except Exception:
            pass
        if cleanup_downloaded_files:
            base.clear_directory_contents(downloads_dir)
        pipeline._CURRENT_TARGET_YEARS_FOR_PREVIEW = old_years
        pipeline._FILTER_PREVIEW_TO_TARGET_YEARS = old_filter

    return working, refresh_logs


def apply_output_postprocessing(
    manifest_df: pd.DataFrame,
    results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]] | None = None,
    *,
    output_dir: Path,
    refresh_recent_single_year: bool = False,
    target_years: Sequence[int] = TARGET_YEARS_DEFAULT,
    force_redownload: bool = False,
    pause_seconds: float = 0.0,
    cleanup_downloaded_files: bool = True,
    persist: bool = True,
) -> tuple[pd.DataFrame, list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]], dict[str, Any]]:
    working = manifest_df.copy()
    notes: list[str] = []

    if refresh_recent_single_year:
        working, refresh_logs = refresh_recent_single_year_datasets(
            working,
            output_dir=output_dir,
            target_years=target_years,
            force_redownload=force_redownload,
            pause_seconds=pause_seconds,
            cleanup_downloaded_files=cleanup_downloaded_files,
        )
        notes.extend(refresh_logs)

    historical_mask = working.apply(lambda r: should_exclude_historical_row(r), axis=1)
    removed_rows = [row for _, row in working.loc[historical_mask].iterrows()]
    removed_count = int(historical_mask.sum())
    if removed_count:
        _archive_orphan_preview_files(output_dir, removed_rows)
        notes.append(f"vyřazeno historických datasetů starších než {HISTORICAL_CUTOFF_YEAR}: {removed_count}")
    working = working.loc[~historical_mask].copy().reset_index(drop=True)

    working, sort_notes = _sort_manifest_by_territory_and_family(working, output_dir=output_dir)
    notes.extend(sort_notes)
    results_new = _results_from_manifest_and_output(working, output_dir)

    if persist:
        _persist_manifest_and_results(output_dir, working, results_new)
        # Also refresh selected relevant catalogue if present.
        try:
            selected_path = output_dir / "selected_relevant_catalogue.csv"
            if selected_path.exists():
                selected = pd.read_csv(selected_path, encoding="utf-8-sig")
                selected = selected.merge(
                    working[["dataset_id", "dataset_title", "category", "order", "territorial_scope_label"]],
                    on=["dataset_id", "dataset_title"], how="inner"
                )
                selected = selected.sort_values("order", na_position="last")
                selected.to_csv(selected_path, index=False, encoding="utf-8-sig")
        except Exception:
            pass

    summary = {
        "removed_historical": removed_count,
        "remaining": int(len(working)),
        "notes": notes,
    }
    return working, results_new, summary


def process_relevant_catalogue(
    catalog_xlsx: Path,
    *,
    output_dir: Path,
    target_years: Sequence[int] = TARGET_YEARS_DEFAULT,
    require_all_target_years: bool = True,
    head_rows: int = 5,
    tail_rows: int = 5,
    max_datasets: int | None = None,
    force_redownload: bool = False,
    cleanup_downloaded_files: bool = True,
    pause_seconds: float = 0.0,
    display_in_notebook: bool = False,
    filter_preview_to_target_years: bool = True,
    refresh_recent_single_year: bool = False,
) -> tuple[pd.DataFrame, list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]], dict[str, Any]]:
    original = _apply_runtime_monkeypatches()
    try:
        manifest_df, results = pipeline.process_relevant_catalogue(
            Path(catalog_xlsx),
            output_dir=Path(output_dir),
            target_years=target_years,
            require_all_target_years=require_all_target_years,
            head_rows=head_rows,
            tail_rows=tail_rows,
            max_datasets=max_datasets,
            force_redownload=force_redownload,
            cleanup_downloaded_files=cleanup_downloaded_files,
            pause_seconds=pause_seconds,
            display_in_notebook=False,
            filter_preview_to_target_years=filter_preview_to_target_years,
        )
    finally:
        _restore_runtime_monkeypatches(original)

    manifest_df, results, summary = apply_output_postprocessing(
        manifest_df,
        results,
        output_dir=Path(output_dir),
        refresh_recent_single_year=refresh_recent_single_year,
        target_years=target_years,
        force_redownload=force_redownload,
        pause_seconds=pause_seconds,
        cleanup_downloaded_files=cleanup_downloaded_files,
        persist=True,
    )

    if display_in_notebook:
        display_results_by_territory(results)
    return manifest_df, results, summary


def repair_existing_output(
    output_dir: Path,
    *,
    refresh_recent_single_year: bool = True,
    target_years: Sequence[int] = TARGET_YEARS_DEFAULT,
    force_redownload: bool = False,
    pause_seconds: float = 0.0,
    cleanup_downloaded_files: bool = True,
    persist: bool = True,
) -> tuple[pd.DataFrame, list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]], dict[str, Any]]:
    out_dir = Path(output_dir)
    manifest_path = out_dir / "ikz_a_to_z_manifest.csv"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest nenalezen: {manifest_path}")
    manifest_df = pd.read_csv(manifest_path, encoding="utf-8-sig")
    return apply_output_postprocessing(
        manifest_df,
        None,
        output_dir=out_dir,
        refresh_recent_single_year=refresh_recent_single_year,
        target_years=target_years,
        force_redownload=force_redownload,
        pause_seconds=pause_seconds,
        cleanup_downloaded_files=cleanup_downloaded_files,
        persist=persist,
    )


def display_results_by_territory(
    results: Sequence[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]],
    *,
    scopes: Sequence[str] | None = None,
    max_items: int | None = None,
) -> None:
    return territory.display_results_by_territory(results, scopes=scopes, max_items=max_items)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CZSO IKZ v7 patch: historical cutoff + full previews for single-year 2020-2023 snapshots + territorial/family sorting.")
    parser.add_argument("--catalog-xlsx", required=True, help="Path to czso_katalog_trideny.xlsx")
    parser.add_argument("--output-dir", required=True, help="Directory for output")
    parser.add_argument("--target-years", nargs="+", type=int, default=TARGET_YEARS_DEFAULT, help="Target years for A/B classification")
    parser.add_argument("--max-datasets", type=int, default=None)
    parser.add_argument("--head-rows", type=int, default=5)
    parser.add_argument("--tail-rows", type=int, default=5)
    parser.add_argument("--force-redownload", action="store_true")
    parser.add_argument("--keep-downloads", action="store_true")
    parser.add_argument("--pause-seconds", type=float, default=0.0)
    parser.add_argument("--no-filter-preview-target-years", dest="filter_preview_to_target_years", action="store_false")
    parser.add_argument("--refresh-recent-single-year", action="store_true", help="After the main run, re-download only one-year 2020-2023 datasets and overwrite their previews with full head/tail.")
    parser.add_argument("--repair-existing-output", action="store_true", help="Do not re-run the full pipeline; patch the already existing output dir in place.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.repair_existing_output:
        manifest_df, results, summary = repair_existing_output(
            Path(args.output_dir),
            refresh_recent_single_year=bool(args.refresh_recent_single_year),
            target_years=args.target_years,
            force_redownload=bool(args.force_redownload),
            pause_seconds=float(args.pause_seconds),
            cleanup_downloaded_files=not bool(args.keep_downloads),
            persist=True,
        )
    else:
        manifest_df, results, summary = process_relevant_catalogue(
            Path(args.catalog_xlsx),
            output_dir=Path(args.output_dir),
            target_years=args.target_years,
            require_all_target_years=True,
            head_rows=int(args.head_rows),
            tail_rows=int(args.tail_rows),
            max_datasets=args.max_datasets,
            force_redownload=bool(args.force_redownload),
            cleanup_downloaded_files=not bool(args.keep_downloads),
            pause_seconds=float(args.pause_seconds),
            display_in_notebook=False,
            filter_preview_to_target_years=bool(args.filter_preview_to_target_years),
            refresh_recent_single_year=bool(args.refresh_recent_single_year),
        )

    print("\nHotovo.")
    print(f"- manifest: {Path(args.output_dir) / 'ikz_a_to_z_manifest.csv'}")
    print(f"- previews: {Path(args.output_dir) / 'previews'}")
    print(f"- report  : {Path(args.output_dir) / 'ikz_a_to_z_previews.md'}")
    print(f"- removed historical datasets: {summary.get('removed_historical')}")
    print(f"- remaining datasets         : {summary.get('remaining')}")
    notes = summary.get("notes") or []
    if notes:
        print("\nPoznámky:")
        for note in notes[:20]:
            print(f"- {note}")
        if len(notes) > 20:
            print(f"... a dalších {len(notes) - 20}")
    if manifest_df is not None and not manifest_df.empty:
        print("\nPočty podle kategorií:")
        print(manifest_df.groupby("category").size().to_string())
    return 0


__all__ = [
    "read_catalogue",
    "select_relevant_datasets",
    "process_relevant_catalogue",
    "repair_existing_output",
    "display_results_by_territory",
    "build_summary_tables",
    "assessment_display_series",
    "TARGET_YEARS_DEFAULT",
    "HISTORICAL_CUTOFF_YEAR",
]


if __name__ == "__main__":
    raise SystemExit(main())
