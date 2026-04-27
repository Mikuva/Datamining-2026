#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
20_add_land_use_environment.py

Doplnění územních a environmentálních ukazatelů z ČSÚ/MOS.

Zdrojová struktura MOS dat:
    rok, kodukaz, koduzemi, hodnota

Použité kódy ukazatelů:
    140100 Celková výměra
    140200 Orná půda
    140700 Trvalé travní porosty
    140900 Zemědělská půda
    141000 Lesní půda
    141200 Vodní plochy
    141300 Zastavěné plochy
    141400 Ostatní plochy
    142000 Koeficient ekologické stability

Výstupy:
    data/processed/land_use_environment.csv
    data/processed/municipality_indicators_raw.csv
    outputs/land_use_environment_summary.md

Spuštění:
    python municipal_map_mvp/src/20_add_land_use_environment.py
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


# =============================================================================
# CESTY
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

MOS_DATA_FILES = [
    RAW_DIR / "csu_mos_data_latest.csv",
    RAW_DIR / "csu_mos_data_2024.csv",
    RAW_DIR / "csu_mos_data_2023.csv",
    RAW_DIR / "csu_mos_data_2022.csv",
    RAW_DIR / "csu_mos_data_2021.csv",
    RAW_DIR / "csu_mos_data_2020.csv",
]

TRENDS_PATH = PROCESSED_DIR / "municipality_indicators_trends_wide.csv"
SCORES_PATH = PROCESSED_DIR / "dimension_scores.csv"
RAW_INDICATORS_PATH = PROCESSED_DIR / "municipality_indicators_raw.csv"

LAND_USE_OUTPUT_PATH = PROCESSED_DIR / "land_use_environment.csv"
SUMMARY_PATH = OUTPUTS_DIR / "land_use_environment_summary.md"


# =============================================================================
# MAPOVÁNÍ UKAZATELŮ
# =============================================================================

LAND_USE_CODES = {
    "140100": "municipality_area_ha",
    "140200": "arable_land_ha",
    "140700": "permanent_grassland_ha",
    "140900": "agricultural_land_ha",
    "141000": "forest_land_ha",
    "141200": "water_area_ha",
    "141300": "built_up_area_ha",
    "141400": "other_area_ha",
    "142000": "ecological_stability_coef",
}

LAND_USE_LABELS = {
    "municipality_area_ha": "Celková výměra obce",
    "arable_land_ha": "Orná půda",
    "permanent_grassland_ha": "Trvalé travní porosty",
    "agricultural_land_ha": "Zemědělská půda",
    "forest_land_ha": "Lesní půda",
    "water_area_ha": "Vodní plochy",
    "built_up_area_ha": "Zastavěné plochy",
    "other_area_ha": "Ostatní plochy",
    "ecological_stability_coef": "Koeficient ekologické stability",
}


# =============================================================================
# POMOCNÉ FUNKCE
# =============================================================================

def clean_code(value: Any) -> str:
    if value is None or pd.isna(value):
        return ""

    text = str(value).strip()

    if text.endswith(".0"):
        text = text[:-2]

    return text


def parse_number(value: Any) -> float | None:
    if value is None or pd.isna(value):
        return None

    if isinstance(value, (int, float)):
        return float(value)

    text = str(value).strip()

    if text == "":
        return None

    text = text.replace("\u00a0", "")
    text = text.replace(" ", "")
    text = text.replace(",", ".")

    try:
        return float(text)
    except ValueError:
        return None


def read_csv_smart(path: Path) -> pd.DataFrame:
    last_error = None

    for enc in ["utf-8-sig", "utf-8", "cp1250", "windows-1250", "latin-1"]:
        try:
            return pd.read_csv(path, encoding=enc, dtype=str, low_memory=False)
        except Exception as exc:
            last_error = exc

    raise RuntimeError(f"Nepodařilo se načíst {path}: {last_error}")


def existing_mos_files() -> list[Path]:
    return [p for p in MOS_DATA_FILES if p.exists()]


# =============================================================================
# EXTRAKCE LAND USE DAT
# =============================================================================

def extract_land_use_from_file(path: Path) -> pd.DataFrame:
    print(f"[INFO] Načítám zdroj: {path}")

    df = read_csv_smart(path)

    required_cols = {"rok", "kodukaz", "koduzemi"}
    missing = required_cols - set(df.columns)

    if missing:
        raise ValueError(
            f"Soubor {path} nemá očekávané sloupce: {missing}. "
            f"Dostupné sloupce: {list(df.columns)}"
        )

    value_col = None
    for col in df.columns:
        if col.strip().lower() == "hodnota":
            value_col = col
            break

    if value_col is None:
        raise ValueError(
            f"Soubor {path} nemá sloupec hodnota. Dostupné sloupce: {list(df.columns)}"
        )

    work = df[["rok", "kodukaz", "koduzemi", value_col]].copy()

    work["year"] = pd.to_numeric(work["rok"], errors="coerce").astype("Int64")
    work["kodukaz"] = work["kodukaz"].map(clean_code)
    work["kod_obce"] = work["koduzemi"].map(clean_code)
    work["value"] = work[value_col].map(parse_number)

    work = work[work["kodukaz"].isin(LAND_USE_CODES.keys())].copy()
    work = work[work["kod_obce"].str.match(r"^\d{6}$", na=False)].copy()

    if work.empty:
        print(f"[WARN] V souboru nebyly nalezeny cílové kódy: {path.name}")
        return pd.DataFrame()

    work["indicator"] = work["kodukaz"].map(LAND_USE_CODES)

    pivot = (
        work
        .pivot_table(
            index=["kod_obce", "year"],
            columns="indicator",
            values="value",
            aggfunc="first",
        )
        .reset_index()
    )

    pivot.columns.name = None

    found = [c for c in LAND_USE_CODES.values() if c in pivot.columns]
    print(f"[OK] Nalezené ukazatele: {', '.join(found)}")
    print(f"[INFO] Počet obcí/roků: {len(pivot):,}")

    return pivot


def load_land_use_data() -> pd.DataFrame:
    files = existing_mos_files()

    if not files:
        raise FileNotFoundError("Nenalezeny žádné soubory csu_mos_data_*.csv v data/raw.")

    frames = []

    for path in files:
        part = extract_land_use_from_file(path)

        if not part.empty:
            frames.append(part)

    if not frames:
        raise RuntimeError("Nepodařilo se vytěžit žádná land-use data.")

    all_data = pd.concat(frames, ignore_index=True)

    value_cols = [c for c in LAND_USE_CODES.values() if c in all_data.columns]

    all_data = (
        all_data
        .groupby(["kod_obce", "year"], as_index=False)[value_cols]
        .mean()
    )

    return all_data


# =============================================================================
# ODVOZENÉ UKAZATELE
# =============================================================================

def add_derived_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    if "municipality_area_ha" in out.columns:
        out["municipality_area_km2"] = out["municipality_area_ha"] / 100.0

    def share(source_col: str, target_col: str) -> None:
        if source_col in out.columns and "municipality_area_ha" in out.columns:
            out[target_col] = (
                pd.to_numeric(out[source_col], errors="coerce")
                / pd.to_numeric(out["municipality_area_ha"], errors="coerce")
                * 100.0
            )

    share("built_up_area_ha", "built_up_area_share")
    share("arable_land_ha", "arable_land_share")
    share("forest_land_ha", "forest_land_share")
    share("permanent_grassland_ha", "permanent_grassland_share")
    share("water_area_ha", "water_area_share")
    share("agricultural_land_ha", "agricultural_land_share")
    share("other_area_ha", "other_area_share")

    stable_cols = [
        "forest_land_ha",
        "permanent_grassland_ha",
        "water_area_ha",
    ]

    if all(c in out.columns for c in stable_cols) and "municipality_area_ha" in out.columns:
        out["natural_stable_area_share"] = (
            out[stable_cols].sum(axis=1, min_count=1)
            / out["municipality_area_ha"]
            * 100.0
        )

    intensive_cols = [
        "arable_land_ha",
        "built_up_area_ha",
    ]

    if all(c in out.columns for c in intensive_cols) and "municipality_area_ha" in out.columns:
        out["intensive_land_use_share"] = (
            out[intensive_cols].sum(axis=1, min_count=1)
            / out["municipality_area_ha"]
            * 100.0
        )

    return out


def add_population_density(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    population = None

    if TRENDS_PATH.exists():
        trends = read_csv_smart(TRENDS_PATH)

        if "kod_obce" in trends.columns:
            trends["kod_obce"] = trends["kod_obce"].map(clean_code)

            if "population_2024" in trends.columns:
                population = trends[["kod_obce", "population_2024"]].copy()
                population = population.rename(columns={"population_2024": "population_for_density"})

    if population is None and SCORES_PATH.exists():
        scores = read_csv_smart(SCORES_PATH)

        if "kod_obce" in scores.columns and "population" in scores.columns:
            scores["kod_obce"] = scores["kod_obce"].map(clean_code)
            population = scores[["kod_obce", "population"]].copy()
            population = population.rename(columns={"population": "population_for_density"})

    if population is None:
        print("[WARN] Populace pro výpočet hustoty nebyla nalezena.")
        return out

    population["population_for_density"] = pd.to_numeric(
        population["population_for_density"],
        errors="coerce",
    )

    out = out.merge(population, on="kod_obce", how="left")

    if "municipality_area_km2" in out.columns:
        out["population_density_per_km2"] = (
            out["population_for_density"]
            / pd.to_numeric(out["municipality_area_km2"], errors="coerce")
        )

    return out


def create_latest_table(all_data: pd.DataFrame) -> pd.DataFrame:
    out = all_data.copy()

    out["year"] = pd.to_numeric(out["year"], errors="coerce").astype("Int64")

    latest = (
        out
        .sort_values(["kod_obce", "year"])
        .groupby("kod_obce", as_index=False)
        .tail(1)
        .reset_index(drop=True)
    )

    value_cols = [c for c in LAND_USE_CODES.values() if c in out.columns]

    years = sorted(int(y) for y in out["year"].dropna().unique())

    for year in years:
        part = out[out["year"].eq(year)][["kod_obce", *value_cols]].copy()
        part = part.rename(columns={c: f"{c}_{year}" for c in value_cols})

        latest = latest.merge(part, on="kod_obce", how="left")

    latest = add_derived_columns(latest)
    latest = add_population_density(latest)

    return latest


# =============================================================================
# DOPLNĚNÍ DO municipality_indicators_raw.csv
# =============================================================================

def merge_into_raw_indicators(land: pd.DataFrame) -> None:
    if not RAW_INDICATORS_PATH.exists():
        print(f"[WARN] Nenalezeno {RAW_INDICATORS_PATH}. Přeskakuji doplnění.")
        return

    raw = read_csv_smart(RAW_INDICATORS_PATH)
    raw["kod_obce"] = raw["kod_obce"].map(clean_code)

    add_cols = [
        "kod_obce",
        "municipality_area_ha",
        "municipality_area_km2",
        "population_for_density",
        "population_density_per_km2",
        "agricultural_land_ha",
        "agricultural_land_share",
        "arable_land_ha",
        "arable_land_share",
        "forest_land_ha",
        "forest_land_share",
        "permanent_grassland_ha",
        "permanent_grassland_share",
        "water_area_ha",
        "water_area_share",
        "built_up_area_ha",
        "built_up_area_share",
        "other_area_ha",
        "other_area_share",
        "natural_stable_area_share",
        "intensive_land_use_share",
        "ecological_stability_coef",
    ]

    add = land[[c for c in add_cols if c in land.columns]].copy()

    overlapping = [c for c in add.columns if c != "kod_obce" and c in raw.columns]

    if overlapping:
        raw = raw.drop(columns=overlapping)

    merged = raw.merge(add, on="kod_obce", how="left")

    merged.to_csv(RAW_INDICATORS_PATH, index=False, encoding="utf-8-sig")

    print(f"[OK] Doplněno: {RAW_INDICATORS_PATH}")


# =============================================================================
# SOUHRN
# =============================================================================

def create_summary(land: pd.DataFrame) -> str:
    lines = []

    lines.append("# Souhrn územních a environmentálních ukazatelů")
    lines.append("")
    lines.append("## Použité kódy ČSÚ/MOS")
    lines.append("")

    for code, col in LAND_USE_CODES.items():
        label = LAND_USE_LABELS.get(col, col)
        lines.append(f"- `{code}` → `{col}` — {label}")

    lines.append("")
    lines.append("## Pokrytí")
    lines.append("")
    lines.append(f"- Počet obcí ve výstupu: `{len(land)}`")

    for col in [
        "municipality_area_ha",
        "municipality_area_km2",
        "population_density_per_km2",
        "built_up_area_share",
        "arable_land_share",
        "forest_land_share",
        "permanent_grassland_share",
        "water_area_share",
        "agricultural_land_share",
        "natural_stable_area_share",
        "intensive_land_use_share",
        "ecological_stability_coef",
    ]:
        if col in land.columns:
            lines.append(f"- `{col}`: `{land[col].notna().sum()}` obcí s daty")

    lines.append("")
    lines.append("## Ukázka")
    lines.append("")

    preview_cols = [
        "kod_obce",
        "year",
        "municipality_area_km2",
        "population_density_per_km2",
        "built_up_area_share",
        "arable_land_share",
        "forest_land_share",
        "permanent_grassland_share",
        "water_area_share",
        "natural_stable_area_share",
        "intensive_land_use_share",
        "ecological_stability_coef",
    ]

    preview = land[[c for c in preview_cols if c in land.columns]].head(20)

    try:
        lines.append(preview.to_markdown(index=False))
    except Exception:
        lines.append(preview.to_string(index=False))

    return "\n".join(lines)


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    all_data = load_land_use_data()
    latest = create_latest_table(all_data)

    ordered_cols = [
        "kod_obce",
        "year",
        "municipality_area_ha",
        "municipality_area_km2",
        "population_for_density",
        "population_density_per_km2",
        "agricultural_land_ha",
        "agricultural_land_share",
        "arable_land_ha",
        "arable_land_share",
        "forest_land_ha",
        "forest_land_share",
        "permanent_grassland_ha",
        "permanent_grassland_share",
        "water_area_ha",
        "water_area_share",
        "built_up_area_ha",
        "built_up_area_share",
        "other_area_ha",
        "other_area_share",
        "natural_stable_area_share",
        "intensive_land_use_share",
        "ecological_stability_coef",
    ]

    remaining_cols = [c for c in latest.columns if c not in ordered_cols]
    latest = latest[[c for c in ordered_cols if c in latest.columns] + remaining_cols].copy()

    latest.to_csv(LAND_USE_OUTPUT_PATH, index=False, encoding="utf-8-sig")
    print(f"[OK] Uloženo: {LAND_USE_OUTPUT_PATH}")

    merge_into_raw_indicators(latest)

    summary = create_summary(latest)
    SUMMARY_PATH.write_text(summary, encoding="utf-8")
    print(f"[OK] Souhrn: {SUMMARY_PATH}")

    print("")
    print("[INFO] Ukázka výstupu:")
    preview_cols = [
        "kod_obce",
        "year",
        "municipality_area_km2",
        "population_density_per_km2",
        "built_up_area_share",
        "arable_land_share",
        "forest_land_share",
        "permanent_grassland_share",
        "water_area_share",
        "natural_stable_area_share",
        "intensive_land_use_share",
        "ecological_stability_coef",
    ]
    print(latest[[c for c in preview_cols if c in latest.columns]].head(15).to_string(index=False))

    print("")
    print("[OK] Hotovo.")
    print("")
    print("Další krok:")
    print("python municipal_map_mvp/src/14_generate_interactive_map_business_dashboard.py")
    print("open municipal_map_mvp/outputs/interactive_map_business_dashboard.html")


if __name__ == "__main__":
    main()