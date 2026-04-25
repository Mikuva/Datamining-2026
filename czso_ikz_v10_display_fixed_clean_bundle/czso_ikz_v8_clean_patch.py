from __future__ import annotations

"""CZSO IKZ patch v8.

Goals:
- keep year-detection and territorial sorting fixes from v5-v7,
- drop datasets whose latest relevant year is older than 2020,
- keep one-year 2020-2023 snapshots with full-dataset previews,
- drop datasets that still do not have a non-empty HEAD and TAIL preview,
- keep municipality-first territorial ordering,
- keep yearly variants of the same dataset family adjacent,
- clean downloaded source files after preview generation.

This patch is designed to be usable in two ways:
1) a fresh end-to-end run over the catalogue,
2) repair/post-process an already generated output directory without a full rerun.
"""

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Any, Iterable, Sequence

import pandas as pd

import czso_ikz_v7_patch as prev

# Re-export notebook-friendly symbols.
TablePreview = prev.TablePreview
DatasetAssessment = prev.DatasetAssessment
TARGET_YEARS_DEFAULT = list(prev.TARGET_YEARS_DEFAULT)
read_catalogue = prev.read_catalogue
select_relevant_datasets = prev.select_relevant_datasets
build_summary_tables = prev.build_summary_tables
assessment_display_series = prev.assessment_display_series
Markdown = prev.Markdown
_display = prev._display
sanitize_filename = prev.sanitize_filename
HISTORICAL_CUTOFF_YEAR = prev.HISTORICAL_CUTOFF_YEAR
SNAPSHOT_FULL_PREVIEW_MIN_YEAR = prev.SNAPSHOT_FULL_PREVIEW_MIN_YEAR
SNAPSHOT_FULL_PREVIEW_MAX_YEAR = prev.SNAPSHOT_FULL_PREVIEW_MAX_YEAR
CATEGORY_ORDER = dict(prev.CATEGORY_ORDER)
territory = prev.territory
base = prev.base
pipeline = prev.pipeline

# Also strip years and common trailing release suffixes when grouping families.
YEAR_TOKEN_RE = re.compile(r"\b(?:18|19|20)\d{2}\b")
TRAILING_RELEASE_SUFFIX_RE = re.compile(r"([_-]?)(?:r|q|m|y|p)(\d{2})(?:\b|$)", re.IGNORECASE)
MULTISPACE_RE = re.compile(r"\s+")


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

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


def _family_key_from_row_strip_years(row: pd.Series | dict[str, Any]) -> str:
    getter = row.get if hasattr(row, "get") else lambda k, d=None: d
    family = _text(getter("rodina_datasetu")) or _text(getter("dataset_title")) or _text(getter("dataset_id"))
    if not family:
        return "dataset"

    txt = family
    txt = YEAR_TOKEN_RE.sub(" ", txt)
    txt = TRAILING_RELEASE_SUFFIX_RE.sub(" ", txt)
    txt = MULTISPACE_RE.sub(" ", txt).strip(" _-.,;/")
    normalized = _normalize(txt)
    return normalized or _normalize(family) or "dataset"


def _variant_year_from_row(row: pd.Series | dict[str, Any]) -> int:
    getter = row.get if hasattr(row, "get") else lambda k, d=None: d

    for key in ["years_max", "years_min"]:
        value = _clean(getter(key))
        if value is not None:
            try:
                return int(float(value))
            except Exception:
                pass

    years = prev.infer_all_years_from_row(row)
    if years:
        return max(int(y) for y in years)

    # Fallback for ids like 250169r24, 140133q25, 250169m23 ...
    for raw in [getter("dataset_id"), getter("dataset_title"), getter("rodina_datasetu")]:
        text = _text(raw)
        if not text:
            continue
        # Common CZSO release suffixes: 250169r24, 140133q25, ...
        m = re.search(r"(?:[rqmyp])(\d{2})$", text, flags=re.IGNORECASE)
        if not m:
            m = re.search(r"(?:^|[_-]|\b)(?:r|q|m|y|p)(\d{2})(?:$|[_-]|\b)", text, flags=re.IGNORECASE)
        if m:
            yy = int(m.group(1))
            return 2000 + yy if yy <= 79 else 1900 + yy

    return 9999


def _collect_preview_frames(row: pd.Series | dict[str, Any], output_dir: Path) -> tuple[pd.DataFrame | None, pd.DataFrame | None, dict[str, Any] | None]:
    row_series = row if isinstance(row, pd.Series) else pd.Series(row)
    return territory._collect_preview_frames(row_series, output_dir)  # type: ignore[attr-defined]


def _preview_nonempty(df: pd.DataFrame | None) -> bool:
    return df is not None and not df.empty and len(df.columns) > 0


def row_has_nonempty_head_and_tail(row: pd.Series | dict[str, Any], output_dir: Path) -> bool:
    head_df, tail_df, _ = _collect_preview_frames(row, output_dir)
    return _preview_nonempty(head_df) and _preview_nonempty(tail_df)


def _should_drop_row_without_preview(row: pd.Series | dict[str, Any], output_dir: Path) -> bool:
    return not row_has_nonempty_head_and_tail(row, output_dir)


def _archive_orphan_preview_files(output_dir: Path, rows: Iterable[pd.Series], *, archive_dir_name: str) -> None:
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


def _sort_manifest_by_territory_and_family(
    manifest_df: pd.DataFrame,
    *,
    output_dir: Path | None = None,
) -> pd.DataFrame:
    working = manifest_df.copy()
    if working.empty:
        return working

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
                preview_cache[cache_key] = _collect_preview_frames(row, out_dir)
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
    working["family_sort_key"] = working.apply(_family_key_from_row_strip_years, axis=1)
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
            "family_sort_key",
            "variant_year",
            "_relevance_rank",
            "_has_years_sort",
            "_has_pk_sort",
            "_years_max_sort",
            "dataset_title",
            "dataset_id",
        ],
        ascending=[True, True, True, True, True, True, True, True, False, True, True],
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
    return working


def _results_from_manifest_and_output(manifest_df: pd.DataFrame, output_dir: Path) -> list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]]:
    results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]] = []
    for _, row in manifest_df.iterrows():
        assessment = territory._row_to_assessment(row)  # type: ignore[attr-defined]
        head_df, tail_df, _ = _collect_preview_frames(row, output_dir)
        if not (_preview_nonempty(head_df) and _preview_nonempty(tail_df)):
            continue
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


def _refresh_problematic_recent_snapshots(
    manifest_df: pd.DataFrame,
    *,
    output_dir: Path,
    target_years: Sequence[int] = TARGET_YEARS_DEFAULT,
    force_redownload: bool = False,
    pause_seconds: float = 0.0,
    cleanup_downloaded_files: bool = True,
) -> tuple[pd.DataFrame, list[str]]:
    """Re-download one-year datasets from 2020-2023, especially when preview is missing/empty."""
    working = manifest_df.copy()
    logs: list[str] = []
    if working.empty:
        return working, logs

    # Reuse v7 implementation: it refreshes all one-year 2020-2023 datasets.
    working, refresh_logs = prev.refresh_recent_single_year_datasets(
        working,
        output_dir=output_dir,
        target_years=target_years,
        force_redownload=force_redownload,
        pause_seconds=pause_seconds,
        cleanup_downloaded_files=cleanup_downloaded_files,
    )
    logs.extend(refresh_logs)
    return working, logs


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
    drop_rows_without_preview: bool = True,
) -> tuple[pd.DataFrame, list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]], dict[str, Any]]:
    working = manifest_df.copy()
    notes: list[str] = []

    if refresh_recent_single_year:
        working, refresh_logs = _refresh_problematic_recent_snapshots(
            working,
            output_dir=output_dir,
            target_years=target_years,
            force_redownload=force_redownload,
            pause_seconds=pause_seconds,
            cleanup_downloaded_files=cleanup_downloaded_files,
        )
        notes.extend(refresh_logs)

    # 1) Drop historical datasets older than the cutoff year.
    historical_mask = working.apply(lambda r: prev.should_exclude_historical_row(r), axis=1)
    removed_historical_rows = [row for _, row in working.loc[historical_mask].iterrows()]
    removed_historical = int(historical_mask.sum())
    if removed_historical:
        _archive_orphan_preview_files(output_dir, removed_historical_rows, archive_dir_name="_excluded_historical")
        notes.append(f"vyřazeno historických datasetů starších než {HISTORICAL_CUTOFF_YEAR}: {removed_historical}")
    working = working.loc[~historical_mask].copy().reset_index(drop=True)

    # 2) Drop datasets that still do not have a usable HEAD and TAIL preview.
    removed_no_preview = 0
    if drop_rows_without_preview and not working.empty:
        no_preview_mask = working.apply(lambda r: _should_drop_row_without_preview(r, output_dir), axis=1)
        removed_no_preview_rows = [row for _, row in working.loc[no_preview_mask].iterrows()]
        removed_no_preview = int(no_preview_mask.sum())
        if removed_no_preview:
            _archive_orphan_preview_files(output_dir, removed_no_preview_rows, archive_dir_name="_excluded_no_preview")
            notes.append(f"vyřazeno datasetů bez ne-prázdného HEAD a TAIL preview: {removed_no_preview}")
        working = working.loc[~no_preview_mask].copy().reset_index(drop=True)

    # 3) Municipality-first territorial ordering, yearly variants of one family together.
    working = _sort_manifest_by_territory_and_family(working, output_dir=output_dir)
    results_new = _results_from_manifest_and_output(working, output_dir)

    if persist:
        _persist_manifest_and_results(output_dir, working, results_new)
        try:
            selected_path = output_dir / "selected_relevant_catalogue.csv"
            if selected_path.exists():
                selected = pd.read_csv(selected_path, encoding="utf-8-sig")
                selected = selected.merge(
                    working[["dataset_id", "dataset_title", "category", "order", "territorial_scope_label"]],
                    on=["dataset_id", "dataset_title"],
                    how="inner",
                )
                selected = selected.sort_values("order", na_position="last")
                selected.to_csv(selected_path, index=False, encoding="utf-8-sig")
        except Exception:
            pass

    summary = {
        "removed_historical": removed_historical,
        "removed_no_preview": removed_no_preview,
        "remaining": int(len(working)),
        "notes": notes,
    }
    return working, results_new, summary


# ---------------------------------------------------------------------------
# Public workflow wrappers
# ---------------------------------------------------------------------------

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
    refresh_recent_single_year: bool = True,
    drop_rows_without_preview: bool = True,
) -> tuple[pd.DataFrame, list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]], dict[str, Any]]:
    manifest_df, results, _summary_prev = prev.process_relevant_catalogue(
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
        refresh_recent_single_year=refresh_recent_single_year,
    )

    manifest_df, results, summary = apply_output_postprocessing(
        manifest_df,
        results,
        output_dir=Path(output_dir),
        refresh_recent_single_year=False,  # already handled above
        target_years=target_years,
        force_redownload=force_redownload,
        pause_seconds=pause_seconds,
        cleanup_downloaded_files=cleanup_downloaded_files,
        persist=True,
        drop_rows_without_preview=drop_rows_without_preview,
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
    drop_rows_without_preview: bool = True,
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
        drop_rows_without_preview=drop_rows_without_preview,
    )


def display_results_by_territory(
    results: Sequence[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]],
    *,
    scopes: Sequence[str] | None = None,
    max_items: int | None = None,
) -> None:
    if _display is None or Markdown is None:
        return
    wanted = {s.lower() for s in scopes} if scopes else None
    current_scope = None
    shown = 0
    for assessment, head_df, tail_df in results:
        if not (_preview_nonempty(head_df) and _preview_nonempty(tail_df)):
            continue
        scope = getattr(assessment, "_territorial_scope", None) or "nezname"
        label = getattr(assessment, "_territorial_scope_label", None) or territory.TERRITORIAL_SCOPE_LABELS.get(scope, scope)
        if wanted and scope.lower() not in wanted and label.lower() not in wanted:
            continue
        if label != current_scope:
            current_scope = label
            _display(Markdown(f"# Územní úroveň: {label}"))
        pipeline.display_assessment_in_notebook(assessment, head_df, tail_df)
        shown += 1
        if max_items is not None and shown >= max_items:
            break


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="CZSO IKZ v8 patch: municipality-first territory sorting, family-year adjacency, drop historical datasets and datasets without usable previews."
    )
    parser.add_argument("--catalog-xlsx", required=False, help="Path to czso_katalog_trideny.xlsx")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    parser.add_argument("--target-years", nargs="+", type=int, default=TARGET_YEARS_DEFAULT)
    parser.add_argument("--max-datasets", type=int, default=None)
    parser.add_argument("--head-rows", type=int, default=5)
    parser.add_argument("--tail-rows", type=int, default=5)
    parser.add_argument("--force-redownload", action="store_true")
    parser.add_argument("--keep-downloads", action="store_true")
    parser.add_argument("--pause-seconds", type=float, default=0.0)
    parser.add_argument("--no-filter-preview-target-years", dest="filter_preview_to_target_years", action="store_false")
    parser.add_argument("--no-refresh-recent-single-year", dest="refresh_recent_single_year", action="store_false")
    parser.add_argument("--keep-rows-without-preview", dest="drop_rows_without_preview", action="store_false")
    parser.add_argument("--repair-existing-output", action="store_true", help="Patch an existing output dir in place instead of running from the catalogue again.")
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
            drop_rows_without_preview=bool(args.drop_rows_without_preview),
        )
    else:
        if not args.catalog_xlsx:
            parser.error("--catalog-xlsx je povinný, pokud nepoužíváš --repair-existing-output")
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
            drop_rows_without_preview=bool(args.drop_rows_without_preview),
        )

    print("\nHotovo.")
    print(f"- manifest: {Path(args.output_dir) / 'ikz_a_to_z_manifest.csv'}")
    print(f"- previews: {Path(args.output_dir) / 'previews'}")
    print(f"- report  : {Path(args.output_dir) / 'ikz_a_to_z_previews.md'}")
    print(f"- removed historical: {summary.get('removed_historical')}")
    print(f"- removed no preview: {summary.get('removed_no_preview')}")
    print(f"- remaining         : {summary.get('remaining')}")
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
