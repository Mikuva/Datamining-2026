from __future__ import annotations

"""CZSO IKZ A-to-Z workflow – v5.

This wrapper keeps the end-to-end workflow from the v4 pipeline, but fixes two
important methodological issues:

1. false positives in target-year detection caused by numeric value columns
   (e.g. ``hodnota`` containing values 2023 or 2024);
2. preview rows are filtered to target years *before* ``head()``/``tail()`` are
   generated, so the previews are relevant for the requested analysis window.

Implementation strategy:
- import the stable v4 workflow as a base module;
- monkey-patch the dataset preview loaders and time-column detection;
- reuse the rest of the workflow (catalogue selection, classification,
  manifest/report generation, notebook display helpers).
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Sequence

import pandas as pd

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

import _czso_ikz_a_to_z_v4_base as base  # noqa: E402
import pyczso  # noqa: E402
from pyczso_lkod_bridge import LKODBridge, detect_encoding  # noqa: E402


# Re-export notebook-friendly helpers and data structures.
TablePreview = base.TablePreview
DatasetAssessment = base.DatasetAssessment
TARGET_YEARS_DEFAULT = [2023, 2024]
PROBE_ROWS_DEFAULT = base.PROBE_ROWS_DEFAULT
read_catalogue = base.read_catalogue
select_relevant_datasets = base.select_relevant_datasets
build_summary_tables = base.build_summary_tables
write_markdown_report = base.write_markdown_report
display_category_results = base.display_category_results
display_assessment_in_notebook = base.display_assessment_in_notebook
assessment_display_series = base.assessment_display_series
dataframe_to_pretty_string = base.dataframe_to_pretty_string
sanitize_filename = base.sanitize_filename
clean_string = base.clean_string
format_years_sample = base.format_years_sample
Markdown = base.Markdown
display = base.display


# Internal runtime config injected by the wrapper ``process_relevant_catalogue``.
_CURRENT_TARGET_YEARS_FOR_PREVIEW: list[int] | None = None
_FILTER_PREVIEW_TO_TARGET_YEARS: bool = True


STRICT_TASK_YEAR_MIN = 1990
STRICT_TASK_YEAR_MAX = 2030
STRICT_YEAR_RE = re.compile(r"(?<!\d)(19\d{2}|20\d{2}|2100)(?!\d)")
STRICT_YYYYMM_RE = re.compile(r"^(19\d{2}|20\d{2}|2100)(0[1-9]|1[0-2])$")
STRICT_YYYYMMDD_RE = re.compile(r"^(19\d{2}|20\d{2}|2100)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])$")

# Strong preference for explicit time-like names. We intentionally avoid
# guessing time columns from arbitrary numeric content because that created
# false positives in columns such as ``hodnota``, various IDs, and code fields.
EXACT_TIME_NAME_PRIORITY = {
    "rok": 300,
    "year": 300,
    "sldbrok": 295,
    "datum": 290,
    "date": 290,
    "sldbdatum": 285,
    "casref": 280,
    "casrefod": 278,
    "casrefdo": 278,
    "obdobi": 275,
    "period": 275,
    "mesic": 260,
    "month": 260,
    "ctvrtleti": 255,
    "quarter": 255,
    "tyden": 250,
    "week": 250,
}
TIME_HINT_TOKENS = {
    "rok", "year", "datum", "date", "casref", "obdobi", "period",
    "mesic", "month", "ctvrtleti", "quarter", "tyden", "week",
}
NON_TIME_EXACT_NAMES = {
    "hodnota",
    "value",
    "count",
    "idhod",
    "id",
    "staprokod",
    "ukazkod",
    "ukazid",
    "vuk",
    "vukid",
    "vukkod",
    "metricid",
    "resourceid",
}
NON_TIME_TOKENS = {
    "hodnota", "value", "count", "pocet", "sum", "avg", "prumer",
    "id", "kod", "cis", "cislo", "ukaz", "vuk", "metric", "measure",
    "indicator", "indikator", "stapro", "resource", "identifikator",
    "txt", "text", "label", "desc", "description", "nazev", "popis",
}
NON_TIME_SUFFIXES = ("kod", "cis", "id", "txt", "text")


def _normalize(value: Any) -> str:
    return base.normalize_name(value)


def _tokens(value: Any) -> list[str]:
    return base._split_name_tokens(value)



def extract_years_from_value_strict(
    value: Any,
    *,
    year_min: int = STRICT_TASK_YEAR_MIN,
    year_max: int = STRICT_TASK_YEAR_MAX,
) -> list[int]:
    """Extract plausible years for *target-year* logic.

    This is intentionally stricter than the generic extractor in the v4 base:
    - the detected year must be a standalone year or the leading year of
      YYYYMM / YYYYMMDD-like values;
    - purely numeric values outside the configured logical range are ignored;
    - years embedded in longer identifiers are ignored.
    """
    years: set[int] = set()
    if value is None:
        return []
    try:
        if pd.isna(value):
            return []
    except Exception:
        pass

    if hasattr(value, 'year') and not isinstance(value, str):
        try:
            year = int(value.year)
            if year_min <= year <= year_max:
                years.add(year)
                return sorted(years)
        except Exception:
            pass

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        try:
            if float(value).is_integer():
                digits = str(int(value))
                if len(digits) == 4:
                    year = int(digits)
                    if year_min <= year <= year_max:
                        years.add(year)
                elif len(digits) == 6 and STRICT_YYYYMM_RE.fullmatch(digits):
                    year = int(digits[:4])
                    if year_min <= year <= year_max:
                        years.add(year)
                elif len(digits) == 8 and STRICT_YYYYMMDD_RE.fullmatch(digits):
                    year = int(digits[:4])
                    if year_min <= year <= year_max:
                        years.add(year)
        except Exception:
            pass
        return sorted(years)

    text = str(value).strip()
    if not text:
        return []

    compact = re.sub(r"\s+", "", text)
    if STRICT_YYYYMM_RE.fullmatch(compact):
        year = int(compact[:4])
        if year_min <= year <= year_max:
            years.add(year)
    if STRICT_YYYYMMDD_RE.fullmatch(compact):
        year = int(compact[:4])
        if year_min <= year <= year_max:
            years.add(year)

    for match in STRICT_YEAR_RE.findall(text):
        year = int(match)
        if year_min <= year <= year_max:
            years.add(year)
    return sorted(years)



def years_from_strings_strict(
    values: Sequence[Any],
    *,
    year_min: int = STRICT_TASK_YEAR_MIN,
    year_max: int = STRICT_TASK_YEAR_MAX,
) -> list[int]:
    years: set[int] = set()
    for value in values:
        years.update(extract_years_from_value_strict(value, year_min=year_min, year_max=year_max))
    return sorted(years)



def series_years_strict(
    series: pd.Series,
    *,
    limit: int | None = None,
    year_min: int = STRICT_TASK_YEAR_MIN,
    year_max: int = STRICT_TASK_YEAR_MAX,
) -> list[int]:
    values = series.dropna()
    if limit is not None:
        values = values.head(limit)
    return years_from_strings_strict(values.tolist(), year_min=year_min, year_max=year_max)



def parse_year_series(series: pd.Series, *, limit: int | None = None) -> pd.Series:
    """Return a Series of lists of extracted years for target-year logic.

    Text forms such as ``1. čtvrtletí 2024``, ``Rok 2024`` and ``20240430``
    are preserved, but years are limited to the logical task window 1990-2030.
    """
    if series is None:
        return pd.Series(dtype=object)
    values = series
    if limit is not None:
        values = values.head(limit)
    return values.map(extract_years_from_value_strict)



def _time_name_priority(column_name: Any) -> int:
    norm = _normalize(column_name)
    toks = set(_tokens(column_name))

    if norm in EXACT_TIME_NAME_PRIORITY:
        return EXACT_TIME_NAME_PRIORITY[norm]

    # Suffixes like `_kod`, `_cis`, `_id`, `_txt` almost always indicate codes,
    # codelists or labels, not a row-level time dimension.
    if norm.endswith(NON_TIME_SUFFIXES):
        return 0
    if toks & {"hodnota", "value", "count", "id", "kod", "cis", "cislo", "ukaz", "vuk", "stapro", "txt", "text"}:
        return 0

    if toks & {"rok", "year"}:
        return 220
    if toks & {"datum", "date", "casref", "obdobi", "period"}:
        return 210
    if toks & {"mesic", "month", "ctvrtleti", "quarter", "tyden", "week"}:
        return 200
    return 0



def is_time_like_column_name(column_name: Any) -> bool:
    return _time_name_priority(column_name) > 0



def _is_obvious_non_time_column(column_name: Any) -> bool:
    norm = _normalize(column_name)
    toks = set(_tokens(column_name))
    if _time_name_priority(column_name) > 0:
        return False
    if norm in NON_TIME_EXACT_NAMES:
        return True
    if norm.endswith(NON_TIME_SUFFIXES):
        return True
    if toks & NON_TIME_TOKENS:
        return True
    if any(tok.endswith(("id", "kod", "cis", "txt")) for tok in toks):
        return True
    return False



def _analyse_year_signal(series: pd.Series, *, sample_limit: int = 400) -> dict[str, Any]:
    sample = series.dropna().head(sample_limit)
    if sample.empty:
        return {
            "sample_size": 0,
            "hit_count": 0,
            "hit_ratio": 0.0,
            "unique_years": [],
            "unique_year_count": 0,
            "value_unique_count": 0,
        }

    extracted = parse_year_series(sample)
    hit_count = int(extracted.map(bool).sum())
    unique_years = sorted({year for years in extracted.tolist() for year in years})
    value_unique_count = int(sample.astype(str).nunique(dropna=True))
    return {
        "sample_size": int(len(sample)),
        "hit_count": hit_count,
        "hit_ratio": hit_count / max(len(sample), 1),
        "unique_years": unique_years,
        "unique_year_count": len(unique_years),
        "value_unique_count": value_unique_count,
    }



def _time_candidates_from_probe(df: pd.DataFrame) -> list[tuple[float, str, dict[str, Any]]]:
    if df is None or df.empty:
        return []

    candidates: list[tuple[float, str, dict[str, Any]]] = []
    for col in df.columns:
        priority = _time_name_priority(col)
        if priority <= 0:
            continue
        if _is_obvious_non_time_column(col):
            continue

        info = _analyse_year_signal(df[col])
        if info["hit_count"] <= 0:
            continue

        unique_year_count = int(info["unique_year_count"])
        hit_ratio = float(info["hit_ratio"])
        value_unique_count = int(info["value_unique_count"])
        sample_size = int(info["sample_size"])

        # Explicit time-name whitelist > content sniffing. Still require the
        # column to behave like time: high year hit ratio and a plausible count
        # of distinct years. Date columns may have many distinct values, but not
        # many distinct *years*.
        if unique_year_count > 30:
            continue
        if hit_ratio < 0.90:
            continue

        norm = _normalize(col)
        if norm in {"rok", "year", "sldbrok"} and value_unique_count > max(30, int(sample_size * 0.50)):
            continue

        score = 1000.0 + float(priority) + (hit_ratio * 100.0) - (unique_year_count * 0.25)
        candidates.append((score, str(col), info))

    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates



def detect_time_columns_from_probe(df: pd.DataFrame) -> list[str]:
    return [col for _, col, _ in _time_candidates_from_probe(df)]



def detect_year_column(df: pd.DataFrame) -> tuple[str | None, list[int], list[str]]:
    # Absolute priority for canonical year column names.
    for col in df.columns:
        norm = _normalize(col)
        if norm in {"rok", "year", "sldbrok"}:
            info = _analyse_year_signal(df[col])
            if info["hit_count"] > 0 and info["hit_ratio"] >= 0.90 and 1 <= int(info["unique_year_count"]) <= 30:
                time_columns = [str(col)] + [c for c in detect_time_columns_from_probe(df) if str(c) != str(col)]
                return str(col), list(info.get("unique_years") or []), time_columns

    candidates = _time_candidates_from_probe(df)
    if not candidates:
        return None, [], []
    best_score, best_col, best_info = candidates[0]
    _ = best_score
    time_columns = [col for _, col, _ in candidates]
    return best_col, list(best_info.get("unique_years") or []), time_columns



def mask_series_for_target_years(series: pd.Series, target_years: Sequence[int]) -> pd.Series:
    target = {int(y) for y in target_years}
    if not target:
        return pd.Series([True] * len(series), index=series.index)
    if pd.api.types.is_datetime64_any_dtype(series):
        parsed = pd.to_datetime(series, errors="coerce")
        return parsed.dt.year.isin(target).fillna(False)
    return series.map(lambda value: bool(target.intersection(extract_years_from_value_strict(value))))



def filter_dataframe_to_target_years(df: pd.DataFrame, year_column: str, target_years: Sequence[int]) -> tuple[pd.DataFrame, int]:
    if year_column not in df.columns:
        return df.head(0).copy(), 0
    mask = mask_series_for_target_years(df[year_column], target_years)
    filtered = df.loc[mask].copy()
    return filtered, int(mask.sum())



def _years_from_dataframe(df: pd.DataFrame, time_columns: Sequence[str], column_names: Sequence[str]) -> tuple[list[int], str | None]:
    header_years = years_from_strings_strict(column_names)
    years: set[int] = set(header_years)
    years_source: str | None = "header_columns" if header_years else None
    if time_columns:
        extracted: set[int] = set(years)
        for col in time_columns:
            if col in df.columns:
                extracted.update(series_years_strict(df[col]))
        years = sorted(extracted)
        if extracted:
            years_source = "data_columns"
    return sorted(dict.fromkeys(years)), years_source


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
    column_names = [str(c) for c in probe_df.columns]
    column_count = len(column_names)
    best_time_col, _, time_columns = detect_year_column(probe_df)
    header_years = years_from_strings_strict(column_names)
    years: set[int] = set(header_years)
    years_source: str | None = "header_columns" if header_years else None

    total_rows = 0
    matched_rows = 0
    last_exc: Exception | None = None
    raw = base.read_bytes_head(path)

    if filter_preview_to_target_years and target_years and best_time_col:
        head_df: pd.DataFrame | None = None
        tail_df: pd.DataFrame | None = None
    else:
        head_df = probe_df.head(head_rows).copy()
        tail_df = None

    for enc in detect_encoding(raw):
        try:
            for chunk in pd.read_csv(path, encoding=enc, sep=None, engine="python", chunksize=chunksize):
                total_rows += len(chunk)
                for col in time_columns:
                    if col in chunk.columns:
                        years.update(series_years_strict(chunk[col]))

                if filter_preview_to_target_years and target_years and best_time_col and best_time_col in chunk.columns:
                    filtered_chunk, matched = filter_dataframe_to_target_years(chunk, best_time_col, target_years)
                    matched_rows += matched
                    if head_df is None:
                        head_df = filtered_chunk.head(head_rows).copy()
                    elif len(head_df) < head_rows and not filtered_chunk.empty:
                        head_df = pd.concat([head_df, filtered_chunk], ignore_index=True).head(head_rows).copy()
                    if tail_df is None:
                        tail_df = filtered_chunk.tail(tail_rows).copy()
                    else:
                        tail_df = pd.concat([tail_df, filtered_chunk], ignore_index=True).tail(tail_rows).copy()
                else:
                    if tail_df is None:
                        tail_df = chunk.tail(tail_rows).copy()
                    else:
                        tail_df = pd.concat([tail_df, chunk], ignore_index=True).tail(tail_rows).copy()
            last_exc = None
            break
        except Exception as exc:
            total_rows = 0
            matched_rows = 0
            tail_df = None
            head_df = None if (filter_preview_to_target_years and target_years and best_time_col) else probe_df.head(head_rows).copy()
            years = set(header_years)
            last_exc = exc
            continue

    if last_exc is not None:
        raise RuntimeError(f"CSV streaming failed for {path.name}: {last_exc}")

    if years and time_columns:
        years_source = "data_columns"

    notes: list[str] = ["roky načteny z celého souboru po chunkách"]
    if filter_preview_to_target_years and target_years:
        if best_time_col:
            notes.append(f"head/tail filtrovány na target years {list(target_years)} přes sloupec `{best_time_col}`; matching_rows={matched_rows}")
            if head_df is None:
                head_df = probe_df.head(0).copy()
            if tail_df is None:
                tail_df = probe_df.head(0).copy()
        else:
            notes.append("head/tail zůstaly nefiltrované: nebyl nalezen spolehlivý řádkový časový sloupec")
            if head_df is None:
                head_df = probe_df.head(head_rows).copy()
            if tail_df is None:
                tail_df = probe_df.tail(tail_rows).copy()
    else:
        if tail_df is None:
            tail_df = probe_df.tail(tail_rows).copy()

    return TablePreview(
        head_df=head_df,
        tail_df=tail_df,
        row_count=int(total_rows),
        column_count=int(column_count),
        column_names=column_names,
        time_columns=time_columns,
        years=sorted(years),
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
    best_time_col, _, time_columns = detect_year_column(probe_df)
    years, years_source = _years_from_dataframe(full, time_columns, column_names)

    preview_df = full
    notes: list[str] = ["roky načteny z celého sešitu"]
    if filter_preview_to_target_years and target_years:
        if best_time_col and best_time_col in full.columns:
            preview_df, matched_rows = filter_dataframe_to_target_years(full, best_time_col, target_years)
            notes.append(f"head/tail filtrovány na target years {list(target_years)} přes sloupec `{best_time_col}`; matching_rows={matched_rows}")
        else:
            notes.append("head/tail zůstaly nefiltrované: nebyl nalezen spolehlivý řádkový časový sloupec")

    head_df = preview_df.head(head_rows).copy()
    tail_df = preview_df.tail(tail_rows).copy()
    return TablePreview(
        head_df=head_df,
        tail_df=tail_df,
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
    best_time_col, _, time_columns = detect_year_column(probe_df)
    years, years_source = _years_from_dataframe(df, time_columns, column_names)

    preview_df = df
    notes: list[str] = ["roky načteny z celého DataFrame"]
    if filter_preview_to_target_years and target_years:
        if best_time_col and best_time_col in df.columns:
            preview_df, matched_rows = filter_dataframe_to_target_years(df, best_time_col, target_years)
            notes.append(f"head/tail filtrovány na target years {list(target_years)} přes sloupec `{best_time_col}`; matching_rows={matched_rows}")
        else:
            notes.append("head/tail zůstaly nefiltrované: nebyl nalezen spolehlivý řádkový časový sloupec")

    head_df = preview_df.head(head_rows).copy()
    tail_df = preview_df.tail(tail_rows).copy()
    return TablePreview(
        head_df=head_df,
        tail_df=tail_df,
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
            source_title = clean_string(pointer.get("title")) or clean_string(pointer.get("format"))
            if ext == "csv":
                preview = load_csv_preview(
                    local_path,
                    head_rows=head_rows,
                    tail_rows=tail_rows,
                    target_years=_CURRENT_TARGET_YEARS_FOR_PREVIEW,
                    filter_preview_to_target_years=_FILTER_PREVIEW_TO_TARGET_YEARS,
                )
            elif ext in {"xlsx", "xls", "xlsm"}:
                preview = load_excel_preview(
                    local_path,
                    head_rows=head_rows,
                    tail_rows=tail_rows,
                    target_years=_CURRENT_TARGET_YEARS_FOR_PREVIEW,
                    filter_preview_to_target_years=_FILTER_PREVIEW_TO_TARGET_YEARS,
                )
            elif ext == "zip":
                preview = load_zip_preview(
                    local_path,
                    head_rows=head_rows,
                    tail_rows=tail_rows,
                    target_years=_CURRENT_TARGET_YEARS_FOR_PREVIEW,
                    filter_preview_to_target_years=_FILTER_PREVIEW_TO_TARGET_YEARS,
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
        target_years=_CURRENT_TARGET_YEARS_FOR_PREVIEW,
        filter_preview_to_target_years=_FILTER_PREVIEW_TO_TARGET_YEARS,
    )
    return preview, "DATASTAT", selection_code, selection_title, "OK_DATASTAT", lkod_error


# Inject fixes into the base module so notebook helpers use the improved logic.
base.is_time_like_column_name = is_time_like_column_name
base.detect_time_columns_from_probe = detect_time_columns_from_probe
base.fetch_dataset_preview = fetch_dataset_preview


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
) -> tuple[pd.DataFrame, list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]]]:
    global _CURRENT_TARGET_YEARS_FOR_PREVIEW, _FILTER_PREVIEW_TO_TARGET_YEARS
    old_years = _CURRENT_TARGET_YEARS_FOR_PREVIEW
    old_filter_flag = _FILTER_PREVIEW_TO_TARGET_YEARS
    _CURRENT_TARGET_YEARS_FOR_PREVIEW = [int(y) for y in target_years]
    _FILTER_PREVIEW_TO_TARGET_YEARS = bool(filter_preview_to_target_years)
    try:
        return base.process_relevant_catalogue(
            catalog_xlsx,
            output_dir=output_dir,
            target_years=target_years,
            require_all_target_years=require_all_target_years,
            head_rows=head_rows,
            tail_rows=tail_rows,
            max_datasets=max_datasets,
            force_redownload=force_redownload,
            cleanup_downloaded_files=cleanup_downloaded_files,
            pause_seconds=pause_seconds,
            display_in_notebook=display_in_notebook,
        )
    finally:
        _CURRENT_TARGET_YEARS_FOR_PREVIEW = old_years
        _FILTER_PREVIEW_TO_TARGET_YEARS = old_filter_flag


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CZSO IKZ A-to-Z workflow v5: fixed year detection + target-year-filtered previews.")
    parser.add_argument("--catalog-xlsx", required=True, help="Path to czso_katalog_trideny.xlsx")
    parser.add_argument("--output-dir", required=True, help="Directory for manifest, previews, and temporary downloads")
    parser.add_argument("--target-years", nargs="+", type=int, default=TARGET_YEARS_DEFAULT, help="Target years for category A/B logic. Default: 2023 2024")
    parser.set_defaults(require_all_target_years=True)
    parser.add_argument("--require-all-target-years", dest="require_all_target_years", action="store_true", help="Require all target years to be present (default).")
    parser.add_argument("--allow-any-target-year", dest="require_all_target_years", action="store_false", help="Relax classification: any overlap with target years is enough.")
    parser.set_defaults(filter_preview_to_target_years=True)
    parser.add_argument("--no-filter-preview-target-years", dest="filter_preview_to_target_years", action="store_false", help="Do not filter preview rows to target years before head()/tail().")
    parser.add_argument("--head-rows", type=int, default=5, help="Number of rows for head() preview")
    parser.add_argument("--tail-rows", type=int, default=5, help="Number of rows for tail() preview")
    parser.add_argument("--max-datasets", type=int, default=None, help="Optional limit for quick testing")
    parser.add_argument("--force-redownload", action="store_true", help="Re-download datasets even if cached files exist")
    parser.add_argument("--keep-downloads", action="store_true", help="Keep downloaded source files in _downloads after previews are created")
    parser.add_argument("--pause-seconds", type=float, default=0.0, help="Optional sleep between datasets")
    parser.add_argument("--print-previews", action="store_true", help="Print head/tail previews to console after processing")
    return parser



def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    manifest_df, results = process_relevant_catalogue(
        Path(args.catalog_xlsx),
        output_dir=Path(args.output_dir),
        target_years=args.target_years,
        require_all_target_years=bool(args.require_all_target_years),
        head_rows=int(args.head_rows),
        tail_rows=int(args.tail_rows),
        max_datasets=args.max_datasets,
        force_redownload=bool(args.force_redownload),
        cleanup_downloaded_files=not bool(args.keep_downloads),
        pause_seconds=float(args.pause_seconds),
        display_in_notebook=False,
        filter_preview_to_target_years=bool(args.filter_preview_to_target_years),
    )

    print("\nHotovo.")
    print(f"- manifest  : {Path(args.output_dir) / 'ikz_a_to_z_manifest.csv'}")
    print(f"- previews  : {Path(args.output_dir) / 'previews'}")
    print(f"- report    : {Path(args.output_dir) / 'ikz_a_to_z_previews.md'}")
    print(f"- downloads : {Path(args.output_dir) / '_downloads'}")
    if not args.keep_downloads:
        print("  (stažené zdrojové soubory se po vytvoření preview průběžně mažou)")
    if args.filter_preview_to_target_years:
        print(f"  (head/tail jsou filtrované jen na target years: {list(args.target_years)})")
    print("\nPočty podle kategorií:")
    if manifest_df.empty:
        print("<prázdné>")
    else:
        print(manifest_df.groupby("category").size().to_string())

    if args.print_previews:
        for assessment, head_df, tail_df in results:
            print("=" * 100)
            print(f"{assessment.order:03d}. [{assessment.category}] {assessment.dataset_title or assessment.dataset_id}")
            print(assessment_display_series(assessment).to_string())
            print("\nHEAD:\n")
            print(dataframe_to_pretty_string(head_df))
            print("\nTAIL:\n")
            print(dataframe_to_pretty_string(tail_df))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
