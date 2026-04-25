from __future__ import annotations

"""Post-processing patch for CZSO IKZ v5 outputs.

This module reorders already generated IKZ outputs by territorial scope without
re-downloading datasets or regenerating head/tail previews.

Typical use:
    manifest_df, results = load_existing_output(OUTPUT_DIR)
    manifest_df, results, summary = resort_outputs_by_territory(
        manifest_df=manifest_df,
        results=results,
        output_dir=OUTPUT_DIR,
        persist=True,
    )
"""

from dataclasses import fields
from datetime import datetime
from pathlib import Path
import json
from typing import Any, Iterable, Sequence

import pandas as pd

import czso_ikz_a_to_z_v5 as pipeline

base = pipeline.base
DatasetAssessment = pipeline.DatasetAssessment
Markdown = pipeline.Markdown
_display = pipeline.display

CATEGORY_ORDER = dict(base.CATEGORY_ORDER)

TERRITORIAL_SCOPE_ORDER = {
    "obec": 0,
    "orp": 10,
    "okres": 20,
    "kraj": 30,
    "region_soudrznosti": 40,
    "cr_stat": 50,
    "jiny_nadobecni_celek": 60,
    "vice_urovni": 70,
    "podobecni": 80,
    "nezname": 99,
}

TERRITORIAL_SCOPE_LABELS = {
    "obec": "obec",
    "orp": "správní obvod ORP",
    "okres": "okres",
    "kraj": "kraj",
    "region_soudrznosti": "region soudržnosti",
    "cr_stat": "ČR / stát",
    "jiny_nadobecni_celek": "jiný nadobecní celek",
    "vice_urovni": "více úrovní / smíšené",
    "podobecni": "podobecní úroveň",
    "nezname": "neurčeno",
}

TERRITORIAL_CIS_MAP = {
    42: "podobecni",  # cast obce
    43: "obec",
    65: "orp",
    72: "jiny_nadobecni_celek",  # spravni obvody Prahy / specialni celky
    97: "cr_stat",
    100: "kraj",
    101: "okres",
    427: "jiny_nadobecni_celek",
    428: "jiny_nadobecni_celek",
}

MUNICIPALITY_PK_NAMES = {
    "obeckod",
    "obec_kod",
    "kodobce",
    "kod_obce",
    "kodobcezuj",
    "kod_obce_zuj",
    "idobce",
    "id_obce",
    "obecid",
    "obec_id",
    "opobeckod",
    "op_obec_kod",
    "dojobeckod",
    "doj_obec_kod",
    "zujkod",
    "zuj_kod",
    "kodzuj",
    "kod_zuj",
}

SUBMUNICIPAL_TOKENS = {
    "podobecni",
    "castobce",
    "castobcedil",
    "zsj",
    "zsjd",
    "zdj",
    "dil",
}

MUNICIPAL_TOKENS = {
    "obec",
    "obce",
    "obcich",
    "mestskeobvody",
    "mestskeobvodyacasti",
    "zuj",
}

ORP_TOKENS = {"orp", "soorp", "spravniobvodobcesrozsirenoupusobnosti"}
OKRES_TOKENS = {"okres", "okresy"}
KRAJ_TOKENS = {"kraj", "kraje"}
REGION_TOKENS = {"regionsoudrznosti", "regionysoudrznosti"}
CR_TOKENS = {"cr", "ceskarepublika", "stat"}
MULTI_LEVEL_TOKENS = {"viceurovni", "census", "vicerovni"}

TEXT_SCOPE_HINTS = [
    ("podobecni", SUBMUNICIPAL_TOKENS),
    ("obec", MUNICIPAL_TOKENS),
    ("orp", ORP_TOKENS),
    ("okres", OKRES_TOKENS),
    ("kraj", KRAJ_TOKENS),
    ("region_soudrznosti", REGION_TOKENS),
    ("cr_stat", CR_TOKENS),
    ("vice_urovni", MULTI_LEVEL_TOKENS),
]

TYPE_SCOPE_HINTS = [
    ("podobecni", {"castobce", "zsj", "zsjd", "zdj", "castobcedil"}),
    ("obec", {"obec"}),
    ("orp", {"orp", "spravniobvodobcesrozsirenoupusobnosti"}),
    ("okres", {"okres"}),
    ("kraj", {"kraj"}),
    ("region_soudrznosti", {"regionsoudrznosti", "regionysoudrznosti"}),
    ("cr_stat", {"cr", "ceskarepublika", "stat"}),
]


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
    out = base.clean_string(value)
    return out or ""


def _normalize(value: Any) -> str:
    return base.normalize_name(_text(value))


def _tokens(value: Any) -> set[str]:
    return set(base._split_name_tokens(_text(value)))


def _safe_read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, encoding="utf-8-sig")


def _safe_read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _collect_preview_frames(row: pd.Series, output_dir: Path) -> tuple[pd.DataFrame | None, pd.DataFrame | None, dict[str, Any] | None]:
    head_df: pd.DataFrame | None = None
    tail_df: pd.DataFrame | None = None
    meta: dict[str, Any] | None = None

    head_rel = _text(row.get("head_csv"))
    tail_rel = _text(row.get("tail_csv"))
    meta_rel = _text(row.get("metadata_json"))

    if head_rel:
        head_path = output_dir / Path(head_rel)
        if head_path.exists():
            try:
                head_df = _safe_read_csv(head_path)
            except Exception:
                head_df = None
    if tail_rel:
        tail_path = output_dir / Path(tail_rel)
        if tail_path.exists():
            try:
                tail_df = _safe_read_csv(tail_path)
            except Exception:
                tail_df = None
    if meta_rel:
        meta_path = output_dir / Path(meta_rel)
        if meta_path.exists():
            try:
                meta = _safe_read_json(meta_path)
            except Exception:
                meta = None
    return head_df, tail_df, meta


def _combine_sample_frames(head_df: pd.DataFrame | None, tail_df: pd.DataFrame | None) -> pd.DataFrame | None:
    frames = [df for df in [head_df, tail_df] if df is not None and not df.empty]
    if not frames:
        return None
    try:
        return pd.concat(frames, ignore_index=True)
    except Exception:
        return frames[0].copy()


def _sample_column_values(df: pd.DataFrame | None, candidates: Sequence[str], limit: int = 100) -> list[Any]:
    if df is None or df.empty:
        return []
    norm_map = {_normalize(c): str(c) for c in df.columns}
    values: list[Any] = []
    for candidate in candidates:
        col = norm_map.get(_normalize(candidate))
        if col:
            series = df[col].dropna().head(limit)
            values.extend(series.tolist())
    return values


def _scope_from_text_hints(*values: Any) -> tuple[str | None, str | None]:
    for raw in values:
        norm = _normalize(raw)
        toks = _tokens(raw)
        if not norm and not toks:
            continue
        for scope, hints in TEXT_SCOPE_HINTS:
            if any(h in norm for h in hints) or (toks & hints):
                return scope, f"text hint: {raw}"
    return None, None


def _scope_from_type_values(values: Sequence[Any]) -> tuple[str | None, str | None]:
    normalized = [_normalize(v) for v in values if _text(v)]
    if not normalized:
        return None, None
    unique_values = sorted(set(normalized))
    for scope, hints in TYPE_SCOPE_HINTS:
        if all(any(h in value for h in hints) for value in unique_values):
            return scope, f"uzemi_typ/vuzemi_typ: {', '.join(unique_values[:5])}"
    if any("obec" == value or "obec" in value for value in unique_values):
        return "obec", f"uzemi_typ/vuzemi_typ contains obec: {', '.join(unique_values[:5])}"
    return None, None


def _scope_from_cis_values(values: Sequence[Any]) -> tuple[str | None, str | None]:
    ints: list[int] = []
    for value in values:
        value = _clean(value)
        if value is None:
            continue
        try:
            ints.append(int(float(value)))
        except Exception:
            continue
    if not ints:
        return None, None
    unique_codes = sorted(set(ints))
    mapped = [TERRITORIAL_CIS_MAP.get(code) for code in unique_codes if code in TERRITORIAL_CIS_MAP]
    mapped = [m for m in mapped if m]
    if not mapped:
        return None, None
    best = sorted(mapped, key=lambda scope: TERRITORIAL_SCOPE_ORDER.get(scope, 99))[0]
    return best, f"uzemi_cis/vuzemi_cis={','.join(str(c) for c in unique_codes[:6])}"


def infer_territorial_scope(
    row: pd.Series,
    head_df: pd.DataFrame | None = None,
    tail_df: pd.DataFrame | None = None,
    meta: dict[str, Any] | None = None,
) -> tuple[str, int, str]:
    sample_df = _combine_sample_frames(head_df, tail_df)

    level_text = _text(row.get("uzemni_uroven"))
    title_text = _text(row.get("dataset_title"))
    detail_text = _text(row.get("detailni_skupina"))
    pk_col = _text(row.get("primary_key_column"))
    pk_kind = _text(row.get("primary_key_kind"))

    # 1) Hard sub-municipal guardrails.
    scope, evidence = _scope_from_text_hints(level_text)
    if scope == "podobecni":
        return scope, TERRITORIAL_SCOPE_ORDER[scope], evidence or "uzemni_uroven indicates submunicipal"

    if sample_df is not None:
        norm_cols = {_normalize(c): str(c) for c in sample_df.columns}
        if any(col in norm_cols for col in ["zsjd_kod", "zsj_kod", "zsj", "cast_obce_kod", "cast_obce"]):
            return "podobecni", TERRITORIAL_SCOPE_ORDER["podobecni"], "preview columns indicate part-of-municipality / ZSJ"

        type_values = _sample_column_values(sample_df, ["uzemi_typ", "vuzemi_typ"])
        type_scope, type_evidence = _scope_from_type_values(type_values)
        if type_scope == "podobecni":
            return type_scope, TERRITORIAL_SCOPE_ORDER[type_scope], type_evidence or "preview uzemi_typ indicates submunicipal"

        cis_values = _sample_column_values(sample_df, ["uzemi_cis", "vuzemi_cis"])
        cis_scope, cis_evidence = _scope_from_cis_values(cis_values)
        if cis_scope == "podobecni":
            return cis_scope, TERRITORIAL_SCOPE_ORDER[cis_scope], cis_evidence or "preview uzemi_cis indicates submunicipal"

    # 2) Explicit municipality evidence.
    if _normalize(pk_col) in MUNICIPALITY_PK_NAMES:
        return "obec", TERRITORIAL_SCOPE_ORDER["obec"], f"primary_key_column={pk_col}"

    if sample_df is not None:
        type_values = _sample_column_values(sample_df, ["uzemi_typ", "vuzemi_typ"])
        type_scope, type_evidence = _scope_from_type_values(type_values)
        if type_scope == "obec":
            return "obec", TERRITORIAL_SCOPE_ORDER["obec"], type_evidence or "preview uzemi_typ indicates municipality"

        cis_values = _sample_column_values(sample_df, ["uzemi_cis", "vuzemi_cis"])
        cis_scope, cis_evidence = _scope_from_cis_values(cis_values)
        if cis_scope == "obec":
            return "obec", TERRITORIAL_SCOPE_ORDER["obec"], cis_evidence or "preview uzemi_cis=43"

    if any(tok in _normalize(level_text) for tok in MUNICIPAL_TOKENS) and not any(tok in _normalize(level_text) for tok in SUBMUNICIPAL_TOKENS | MULTI_LEVEL_TOKENS):
        return "obec", TERRITORIAL_SCOPE_ORDER["obec"], f"uzemni_uroven={level_text}"

    # 3) Larger territorial units.
    larger_text_scope, larger_text_evidence = _scope_from_text_hints(level_text, detail_text, title_text)
    if larger_text_scope in {"orp", "okres", "kraj", "region_soudrznosti", "cr_stat", "vice_urovni"}:
        # Allow sample evidence to refine ambiguous multi-level cases.
        if sample_df is not None:
            type_values = _sample_column_values(sample_df, ["uzemi_typ", "vuzemi_typ"])
            type_scope, type_evidence = _scope_from_type_values(type_values)
            if type_scope in {"orp", "okres", "kraj", "region_soudrznosti", "cr_stat"}:
                return type_scope, TERRITORIAL_SCOPE_ORDER[type_scope], type_evidence or larger_text_evidence or "preview type values"
            cis_values = _sample_column_values(sample_df, ["uzemi_cis", "vuzemi_cis"])
            cis_scope, cis_evidence = _scope_from_cis_values(cis_values)
            if cis_scope in {"orp", "okres", "kraj", "region_soudrznosti", "cr_stat"}:
                return cis_scope, TERRITORIAL_SCOPE_ORDER[cis_scope], cis_evidence or larger_text_evidence or "preview cis values"
            if larger_text_scope == "vice_urovni" and type_scope == "obec":
                return "obec", TERRITORIAL_SCOPE_ORDER["obec"], f"metadata says multi-level, preview sample shows municipality ({type_evidence})"
        return larger_text_scope, TERRITORIAL_SCOPE_ORDER[larger_text_scope], larger_text_evidence or f"metadata hint: {level_text or title_text}"

    if sample_df is not None:
        type_values = _sample_column_values(sample_df, ["uzemi_typ", "vuzemi_typ"])
        type_scope, type_evidence = _scope_from_type_values(type_values)
        if type_scope in {"orp", "okres", "kraj", "region_soudrznosti", "cr_stat"}:
            return type_scope, TERRITORIAL_SCOPE_ORDER[type_scope], type_evidence or "preview type values"
        cis_values = _sample_column_values(sample_df, ["uzemi_cis", "vuzemi_cis"])
        cis_scope, cis_evidence = _scope_from_cis_values(cis_values)
        if cis_scope in {"orp", "okres", "kraj", "region_soudrznosti", "cr_stat", "jiny_nadobecni_celek"}:
            return cis_scope, TERRITORIAL_SCOPE_ORDER[cis_scope], cis_evidence or "preview cis values"

        norm_cols = {_normalize(c): str(c) for c in sample_df.columns}
        if any(key in norm_cols for key in ["so_orp", "soorp", "prislorp_kod", "prislorp"]):
            return "orp", TERRITORIAL_SCOPE_ORDER["orp"], "preview contains ORP columns"
        if any(key in norm_cols for key in ["okres", "okres_kod", "okreskod"]):
            return "okres", TERRITORIAL_SCOPE_ORDER["okres"], "preview contains district columns"
        if any(key in norm_cols for key in ["kraj", "kraj_kod", "krajkod"]):
            return "kraj", TERRITORIAL_SCOPE_ORDER["kraj"], "preview contains region columns"

    if pk_kind == "territorial_non_municipal":
        return "jiny_nadobecni_celek", TERRITORIAL_SCOPE_ORDER["jiny_nadobecni_celek"], f"primary_key_kind={pk_kind} ({pk_col})"

    if "viceurovni" in _normalize(level_text):
        return "vice_urovni", TERRITORIAL_SCOPE_ORDER["vice_urovni"], f"uzemni_uroven={level_text}"

    return "nezname", TERRITORIAL_SCOPE_ORDER["nezname"], "nepodařilo se spolehlivě určit územní úroveň"


def _coerce_bool(value: Any) -> bool | None:
    value = _clean(value)
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"true", "1", "ano", "yes"}:
        return True
    if text in {"false", "0", "ne", "no"}:
        return False
    return None


def _row_to_assessment(row: pd.Series) -> DatasetAssessment:
    data: dict[str, Any] = {}
    for field in fields(DatasetAssessment):
        value = _clean(row.get(field.name))
        if field.name in {"has_target_years", "has_primary_key"}:
            value = _coerce_bool(value)
        data[field.name] = value
    return DatasetAssessment(**data)


def load_existing_output(output_dir: Path) -> tuple[pd.DataFrame, list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]]]:
    out_dir = Path(output_dir)
    manifest_path = out_dir / "ikz_a_to_z_manifest.csv"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest nenalezen: {manifest_path}")
    manifest_df = pd.read_csv(manifest_path, encoding="utf-8-sig")
    results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]] = []
    for _, row in manifest_df.iterrows():
        assessment = _row_to_assessment(row)
        head_df, tail_df, _ = _collect_preview_frames(row, out_dir)
        results.append((assessment, head_df, tail_df))
    return manifest_df, results


def _write_manifest_xlsx_with_territory(output_dir: Path, manifest_df: pd.DataFrame) -> None:
    workbook_path = output_dir / "ikz_a_to_z_manifest.xlsx"
    summary_tables = dict(pipeline.build_summary_tables(manifest_df))
    summary_tables["datasets_by_territorial_scope"] = (
        manifest_df.groupby(["territorial_scope_label", "category"], dropna=False)
        .size()
        .reset_index(name="dataset_count")
        .sort_values(["territorial_scope_label", "category"], na_position="last")
        .reset_index(drop=True)
    )
    with pd.ExcelWriter(workbook_path, engine="openpyxl") as writer:
        manifest_df.to_excel(writer, sheet_name="manifest", index=False)
        for name, table in summary_tables.items():
            sheet = pipeline.sanitize_filename(name, max_len=31)[:31] or name[:31]
            table.to_excel(writer, sheet_name=sheet, index=False)


def _write_territorial_markdown_report(
    output_dir: Path,
    manifest_df: pd.DataFrame,
    results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]],
) -> Path:
    report_path = output_dir / "ikz_a_to_z_previews.md"
    lines: list[str] = []
    lines.append("# CZSO IKZ – territorially sorted output")
    lines.append("")
    lines.append(f"Vygenerováno: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    if not manifest_df.empty:
        lines.append("## Souhrn podle územní úrovně")
        lines.append("")
        scope_summary = (
            manifest_df.groupby(["territorial_scope_label", "category"], dropna=False)
            .size()
            .reset_index(name="dataset_count")
        )
        lines.append(scope_summary.to_string(index=False))
        lines.append("")

    current_scope = None
    current_category = None
    for assessment, head_df, tail_df in results:
        scope_label = getattr(assessment, "_territorial_scope_label", None) or "neurčeno"
        if scope_label != current_scope:
            current_scope = scope_label
            current_category = None
            lines.append(f"# Územní úroveň: {scope_label}")
            lines.append("")
        if assessment.category != current_category:
            current_category = assessment.category
            lines.append(f"## Kategorie {current_category}")
            lines.append("")
        title = assessment.dataset_title or assessment.dataset_id or "Dataset"
        lines.append(f"### {assessment.order:03d}. [{assessment.category}] {title}")
        lines.append("")
        lines.append(pipeline.assessment_display_series(assessment).to_string())
        evidence = getattr(assessment, "_territorial_evidence", None)
        if evidence:
            lines.append("")
            lines.append(f"territorial_scope: {scope_label}")
            lines.append(f"territorial_evidence: {evidence}")
        lines.append("")
        lines.append("#### HEAD")
        lines.append("")
        lines.append("```")
        lines.append(pipeline.dataframe_to_pretty_string(head_df))
        lines.append("```")
        lines.append("")
        lines.append("#### TAIL")
        lines.append("")
        lines.append("```")
        lines.append(pipeline.dataframe_to_pretty_string(tail_df))
        lines.append("```")
        lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def _apply_territorial_metadata_to_results(
    manifest_df: pd.DataFrame,
    results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]],
) -> list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]]:
    meta_map = {
        (row["dataset_id"], row["dataset_title"], row["category"], row["status"]): row
        for _, row in manifest_df.iterrows()
    }
    reordered: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]] = []
    for assessment, head_df, tail_df in results:
        key = (assessment.dataset_id, assessment.dataset_title, assessment.category, assessment.status)
        row = meta_map.get(key)
        if row is not None:
            assessment.order = int(row["order"])
            setattr(assessment, "_territorial_scope", row.get("territorial_scope"))
            setattr(assessment, "_territorial_scope_label", row.get("territorial_scope_label"))
            setattr(assessment, "_territorial_rank", row.get("territorial_rank"))
            setattr(assessment, "_territorial_evidence", row.get("territorial_evidence"))
        reordered.append((assessment, head_df, tail_df))
    reordered.sort(key=lambda item: int(getattr(item[0], "order", 999999)))
    return reordered


def resort_outputs_by_territory(
    *,
    manifest_df: pd.DataFrame,
    results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]],
    output_dir: Path | None = None,
    persist: bool = True,
) -> tuple[pd.DataFrame, list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]], pd.DataFrame]:
    if manifest_df is None or manifest_df.empty:
        return manifest_df, results, pd.DataFrame(columns=["territorial_scope_label", "dataset_count"])

    out_dir = Path(output_dir) if output_dir is not None else None
    working = manifest_df.copy()
    working["original_order"] = pd.to_numeric(working.get("order"), errors="coerce")

    scopes: list[str] = []
    scope_labels: list[str] = []
    scope_ranks: list[int] = []
    scope_evidence: list[str] = []

    preview_cache: dict[tuple[Any, Any, Any, Any], tuple[pd.DataFrame | None, pd.DataFrame | None, dict[str, Any] | None]] = {}

    for idx, row in working.iterrows():
        head_df = tail_df = None
        meta = None
        if out_dir is not None:
            cache_key = (row.get("dataset_id"), row.get("dataset_title"), row.get("head_csv"), row.get("tail_csv"))
            if cache_key not in preview_cache:
                preview_cache[cache_key] = _collect_preview_frames(row, out_dir)
            head_df, tail_df, meta = preview_cache[cache_key]
        scope, rank, evidence = infer_territorial_scope(row, head_df=head_df, tail_df=tail_df, meta=meta)
        scopes.append(scope)
        scope_labels.append(TERRITORIAL_SCOPE_LABELS.get(scope, scope))
        scope_ranks.append(rank)
        scope_evidence.append(evidence)

    working["territorial_scope"] = scopes
    working["territorial_scope_label"] = scope_labels
    working["territorial_rank"] = scope_ranks
    working["territorial_evidence"] = scope_evidence

    has_pk_series = working["has_primary_key"] if "has_primary_key" in working.columns else pd.Series(False, index=working.index)
    has_years_series = working["has_target_years"] if "has_target_years" in working.columns else pd.Series(False, index=working.index)
    relevance_series = working["relevance_rank"] if "relevance_rank" in working.columns else pd.Series(99, index=working.index)
    years_max_series = working["years_max"] if "years_max" in working.columns else pd.Series(-1, index=working.index)

    working["_category_rank"] = working["category"].map(CATEGORY_ORDER).fillna(99).astype(int)
    working["_years_max_sort"] = pd.to_numeric(years_max_series, errors="coerce").fillna(-1)
    working["_has_pk_sort"] = has_pk_series.fillna(False).astype(int) * -1
    working["_has_years_sort"] = has_years_series.fillna(False).astype(int) * -1
    working["_relevance_rank"] = pd.to_numeric(relevance_series, errors="coerce").fillna(99).astype(int)

    working = working.sort_values(
        [
            "territorial_rank",
            "_category_rank",
            "_relevance_rank",
            "_has_years_sort",
            "_has_pk_sort",
            "_years_max_sort",
            "dataset_title",
            "dataset_id",
        ],
        ascending=[True, True, True, True, True, False, True, True],
        na_position="last",
    ).reset_index(drop=True)

    working["order"] = range(1, len(working) + 1)

    summary = (
        working.groupby(["territorial_scope_label", "category"], dropna=False)
        .size()
        .reset_index(name="dataset_count")
        .sort_values(["territorial_scope_label", "category"], na_position="last")
        .reset_index(drop=True)
    )

    drop_cols = [
        "_category_rank",
        "_years_max_sort",
        "_has_pk_sort",
        "_has_years_sort",
        "_relevance_rank",
    ]
    working = working.drop(columns=[col for col in drop_cols if col in working.columns])

    reordered_results = _apply_territorial_metadata_to_results(working, results)

    if persist and out_dir is not None:
        working.to_csv(out_dir / "ikz_a_to_z_manifest.csv", index=False, encoding="utf-8-sig")
        try:
            _write_manifest_xlsx_with_territory(out_dir, working)
        except Exception:
            pass
        _write_territorial_markdown_report(out_dir, working, reordered_results)
        try:
            summary.to_csv(out_dir / "datasets_by_territorial_scope.csv", index=False, encoding="utf-8-sig")
        except Exception:
            pass

    return working, reordered_results, summary


def quick_resort_existing_output(
    output_dir: Path,
    *,
    persist: bool = True,
) -> tuple[pd.DataFrame, list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]], pd.DataFrame]:
    manifest_df, results = load_existing_output(output_dir)
    return resort_outputs_by_territory(
        manifest_df=manifest_df,
        results=results,
        output_dir=output_dir,
        persist=persist,
    )


def _preview_nonempty(df: pd.DataFrame | None) -> bool:
    return df is not None and not df.empty and len(df.columns) > 0


def display_results_by_territory(
    results: Sequence[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]],
    *,
    scopes: Sequence[str] | None = None,
    categories: Sequence[str] | None = None,
    max_items: int | None = None,
) -> None:
    """Display already-generated previews grouped by territorial scope.

    Supports both
    - ``categories`` = A/B/C/D filtering
    - ``scopes`` = territorial scope filtering

    It also skips rows without usable HEAD/TAIL previews so that headings are
    never rendered for empty datasets.
    """
    if _display is None or Markdown is None:
        return

    wanted_scopes = {str(s).strip().lower() for s in scopes} if scopes else None
    wanted_categories = {str(c).strip().upper() for c in categories} if categories else None

    current_scope = None
    shown = 0
    for assessment, head_df, tail_df in results:
        if not (_preview_nonempty(head_df) and _preview_nonempty(tail_df)):
            continue
        scope = getattr(assessment, "_territorial_scope", None) or "nezname"
        label = getattr(assessment, "_territorial_scope_label", None) or TERRITORIAL_SCOPE_LABELS.get(scope, scope)
        category = str(getattr(assessment, "category", "") or "").strip().upper()

        if wanted_scopes and scope.lower() not in wanted_scopes and label.lower() not in wanted_scopes:
            continue
        if wanted_categories and category not in wanted_categories:
            continue

        if label != current_scope:
            current_scope = label
            _display(Markdown(f"# Územní úroveň: {label}"))
        pipeline.display_assessment_in_notebook(assessment, head_df, tail_df)
        shown += 1
        if max_items is not None and shown >= max_items:
            break


__all__ = [
    "load_existing_output",
    "resort_outputs_by_territory",
    "quick_resort_existing_output",
    "display_results_by_territory",
    "infer_territorial_scope",
    "TERRITORIAL_SCOPE_ORDER",
    "TERRITORIAL_SCOPE_LABELS",
]
