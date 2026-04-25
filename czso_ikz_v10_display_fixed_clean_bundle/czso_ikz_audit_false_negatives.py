from __future__ import annotations

"""Audit helper for potential false negatives in the CZSO IKZ pipeline."""

import argparse
import re
from pathlib import Path
from typing import Any

import pandas as pd

YEAR_RE = re.compile(r"(?<!\d)(19\d{2}|20\d{2}|2100)(?!\d)")
KEY_ALIASES = {
    "obec_kod", "kod_obce", "kod_obce_zuj", "zuj_kod", "op_obec_kod", "doj_obec_kod",
    "uzemi_kod", "vuzemi_kod", "idobce", "id_obce", "uzemi", "vuzemi",
}


def parse_years_any(value: Any) -> set[int]:
    if value is None:
        return set()
    try:
        if pd.isna(value):
            return set()
    except Exception:
        pass
    return {int(x) for x in YEAR_RE.findall(str(value)) if 1990 <= int(x) <= 2035}


def extract_years_from_profile_row(row: pd.Series) -> set[int]:
    years: set[int] = set()
    for col in ["years_sample", "years_min", "years_max", "start_catalog", "end_catalog", "source_title", "dataset_title", "selected_file"]:
        if col in row.index:
            years |= parse_years_any(row[col])
    return years


def read_head_columns(base_dir: Path, relpath: Any) -> set[str]:
    if relpath is None:
        return set()
    try:
        if pd.isna(relpath):
            return set()
    except Exception:
        pass
    p = base_dir / str(relpath)
    if not p.exists():
        return set()
    try:
        cols = pd.read_csv(p, nrows=1).columns
        return {str(c).strip().lower().replace('"', '').replace('\ufeff', '') for c in cols}
    except Exception:
        return set()


def run_audit(
    *,
    base_dir: Path,
    shortlist_path: Path,
    final_manifest_path: Path,
    profiles_manifest_path: Path | None = None,
    target_years: tuple[int, int] = (2023, 2024),
) -> dict[str, pd.DataFrame]:
    shortlist = pd.read_csv(shortlist_path, dtype={"dataset_id": "string"})
    final = pd.read_csv(final_manifest_path, dtype={"dataset_id": "string"})

    for df in (shortlist, final):
        if "dataset_id" in df.columns:
            df["dataset_id"] = df["dataset_id"].astype("string").str.strip()

    final_ids = set(final["dataset_id"].dropna()) if "dataset_id" in final.columns else set()

    outputs: dict[str, pd.DataFrame] = {}

    if profiles_manifest_path is None or not profiles_manifest_path.exists():
        missing = shortlist.loc[~shortlist["dataset_id"].isin(final_ids)].copy()
        outputs["missing_from_final_simple"] = missing
        return outputs

    prof = pd.read_csv(profiles_manifest_path, dtype={"dataset_id": "string"})
    prof["dataset_id"] = prof["dataset_id"].astype("string").str.strip()
    prof["profile_years"] = prof.apply(extract_years_from_profile_row, axis=1)
    prof["has_target_years_profile"] = prof["profile_years"].apply(lambda s: all(y in s for y in target_years))
    preview_col = "preview_csv" if "preview_csv" in prof.columns else None
    if preview_col is not None:
        prof["head_columns"] = prof[preview_col].apply(lambda p: read_head_columns(base_dir, p))
    else:
        prof["head_columns"] = [set() for _ in range(len(prof))]
    prof["has_pk_from_head"] = prof["head_columns"].apply(lambda cols: bool(cols & KEY_ALIASES))
    prof["pk_from_head"] = prof["head_columns"].apply(lambda cols: ", ".join(sorted(cols & KEY_ALIASES)) if cols else None)
    prof["profile_ok"] = prof.get("status", pd.Series(index=prof.index, dtype=object)).astype(str).str.startswith("OK")

    keep_cols = [c for c in ["dataset_id", "title", "relevance_pro_IKZ", "relevance_pro_ikz", "uzemni_uroven", "latest_year_hint", "excluded_historical"] if c in shortlist.columns]
    audit = prof.merge(shortlist[keep_cols].drop_duplicates("dataset_id"), on="dataset_id", how="left")
    audit["in_final_manifest"] = audit["dataset_id"].isin(final_ids)

    strong = audit[
        audit["profile_ok"]
        & audit["has_target_years_profile"]
        & audit["has_pk_from_head"]
        & ~audit["in_final_manifest"]
    ].copy()

    soft = audit[
        audit["profile_ok"]
        & audit["has_target_years_profile"]
        & ~audit["in_final_manifest"]
    ].copy()

    technical = audit[
        ~audit["profile_ok"] & ~audit["in_final_manifest"]
    ].copy()

    historical = audit[
        audit["profile_years"].apply(lambda s: len(s) > 0 and max(s) < 2020)
        & ~audit["in_final_manifest"]
    ].copy()

    outputs["false_negative_strong"] = strong
    outputs["false_negative_soft"] = soft
    outputs["technical_failures"] = technical
    outputs["correct_historical_exclusions"] = historical
    return outputs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit potential false negatives in CZSO IKZ outputs.")
    parser.add_argument("--base-dir", default=".")
    parser.add_argument("--shortlist", default="selected_relevant_catalogue.csv")
    parser.add_argument("--final", default="ikz_a_to_z_manifest.csv")
    parser.add_argument("--profiles", default="czso_dataset_profiles/dataset_profiles_manifest.csv")
    parser.add_argument("--out-dir", default="audit_false_negatives")
    args = parser.parse_args(argv)

    base_dir = Path(args.base_dir).resolve()
    outputs = run_audit(
        base_dir=base_dir,
        shortlist_path=(base_dir / args.shortlist),
        final_manifest_path=(base_dir / args.final),
        profiles_manifest_path=(base_dir / args.profiles),
    )
    out_dir = base_dir / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, df in outputs.items():
        df.to_csv(out_dir / f"{name}.csv", index=False, encoding="utf-8-sig")
        print(f"{name}: {len(df)} -> {out_dir / (name + '.csv')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
