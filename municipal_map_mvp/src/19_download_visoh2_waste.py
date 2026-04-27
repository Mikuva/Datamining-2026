#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
19_download_visoh2_waste.py

Zpracování exportu VISOH2:
- plnění cíle třídění,
- produkce komunálního odpadu,
- produkce směsného komunálního odpadu,
- produkce objemného odpadu,
- separované recyklovatelné složky,
- separace plastu,
- účinnost separace plastu.

Vstup:
    ručně stažený export z VISOH2 ve formátu XLSX / CSV

Výstupy:
    data/processed/waste_indicators_raw.csv
    data/processed/waste_indicators_trends_wide.csv
    doplněný data/processed/municipality_indicators_raw.csv

Spuštění:
    python municipal_map_mvp/src/19_download_visoh2_waste.py --input municipal_map_mvp/data/raw/visoh2/NAZEV_SOUBORU.xlsx

Nebo pokud je ve složce data/raw/visoh2 jen jeden export:
    python municipal_map_mvp/src/19_download_visoh2_waste.py
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

VISOH_RAW_DIR = RAW_DIR / "visoh2"

MUNICIPALITY_RAW_PATH = PROCESSED_DIR / "municipality_indicators_raw.csv"

WASTE_RAW_OUT = PROCESSED_DIR / "waste_indicators_raw.csv"
WASTE_TRENDS_OUT = PROCESSED_DIR / "waste_indicators_trends_wide.csv"


BASE_COLUMNS = {
    "year": ["Rok", "rok", "Year"],
    "kraj": ["Kraj", "kraj"],
    "obec": ["Obec", "obec"],
    "kod_obce": ["Obec - kód", "Obec-kód", "Kód obce", "kod_obce", "KOD_OBCE"],
}

SOURCE_COLUMNS = {
    "waste_sorting_target_share": [
        "Cíl pro třídění",
        "Cil pro trideni",
    ],
    "municipal_waste_tonnes": [
        "Sum of I.O.1KO",
        "I.O.1KO",
    ],
    "mixed_municipal_waste_tonnes": [
        "Sum of I.O.2SKO",
        "I.O.2SKO",
    ],
    "bulky_waste_tonnes": [
        "Sum of I.O.3Obj",
        "I.O.3Obj",
    ],
    "separated_recyclables_tonnes": [
        "Sum of I.O.5SEPppsk",
        "I.O.5SEPppsk",
    ],
    "paper_separation_tonnes": [
        "Sum of I.O.5SEPpap",
        "I.O.5SEPpap",
    ],
    "plastic_separation_tonnes": [
        "Sum of I.O.5SEPpl",
        "I.O.5SEPpl",
    ],
    "glass_separation_tonnes": [
        "Sum of I.O.5SEPs",
        "I.O.5SEPs",
    ],
    "metal_separation_tonnes": [
        "Sum of I.O.5SEPk",
        "I.O.5SEPk",
    ],
    "plastic_separation_efficiency": [
        "I.O.6USEPpl",
        "Sum of I.O.6USEPpl",
    ],
    "bio_waste_tonnes": [
        "Sum of I.O.7.SEPBio",
        "I.O.7.SEPBio",
    ],
    "textile_waste_tonnes": [
        "Sum of I.O.8.SEPTex",
        "I.O.8.SEPTex",
    ],
    "hazardous_waste_tonnes": [
        "Sum of I.O.9SEPN",
        "I.O.9SEPN",
    ],
}

DERIVED_PER_CAPITA = {
    "municipal_waste_kg_per_capita": "municipal_waste_tonnes",
    "mixed_municipal_waste_kg_per_capita": "mixed_municipal_waste_tonnes",
    "bulky_waste_kg_per_capita": "bulky_waste_tonnes",
    "separated_recyclables_kg_per_capita": "separated_recyclables_tonnes",
    "paper_separation_kg_per_capita": "paper_separation_tonnes",
    "plastic_separation_kg_per_capita": "plastic_separation_tonnes",
    "glass_separation_kg_per_capita": "glass_separation_tonnes",
    "metal_separation_kg_per_capita": "metal_separation_tonnes",
    "bio_waste_kg_per_capita": "bio_waste_tonnes",
    "textile_waste_kg_per_capita": "textile_waste_tonnes",
    "hazardous_waste_kg_per_capita": "hazardous_waste_tonnes",
}

PUBLIC_INDICATORS = [
    "waste_sorting_target_share",
    "municipal_waste_kg_per_capita",
    "mixed_municipal_waste_kg_per_capita",
    "bulky_waste_kg_per_capita",
    "separated_recyclables_kg_per_capita",
    "plastic_separation_kg_per_capita",
    "plastic_separation_efficiency",
    "bio_waste_kg_per_capita",
]

DIRECTION = {
    "waste_sorting_target_share": "UP",
    "municipal_waste_kg_per_capita": "DOWN",
    "mixed_municipal_waste_kg_per_capita": "DOWN",
    "bulky_waste_kg_per_capita": "DOWN",
    "separated_recyclables_kg_per_capita": "CONTEXT",
    "plastic_separation_kg_per_capita": "CONTEXT",
    "plastic_separation_efficiency": "UP",
    "bio_waste_kg_per_capita": "CONTEXT",
}


def clean_code(value) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip().replace(".0", "")
    digits = re.sub(r"\D", "", text)
    return digits.zfill(6) if digits else ""


def normalize_col(value) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip()
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text


def norm_key(value) -> str:
    text = normalize_col(value).lower()
    text = text.replace("á", "a").replace("č", "c").replace("ď", "d")
    text = text.replace("é", "e").replace("ě", "e").replace("í", "i")
    text = text.replace("ň", "n").replace("ó", "o").replace("ř", "r")
    text = text.replace("š", "s").replace("ť", "t").replace("ú", "u")
    text = text.replace("ů", "u").replace("ý", "y").replace("ž", "z")
    text = re.sub(r"[^a-z0-9]+", "", text)
    return text


def to_number(series: pd.Series) -> pd.Series:
    """
    Bezpečný převod českých/evropských číselných hodnot na float.

    Podporuje:
    - desetinnou čárku,
    - pevné mezery,
    - běžné mezery,
    - procenta typu "54.3 %" nebo "54,3 %",
    - prázdné hodnoty a pomlčky.
    """
    cleaned = (
        series.astype(str)
        .str.strip()
        .str.replace("\u00a0", "", regex=False)
        .str.replace(" ", "", regex=False)
        .str.replace("%", "", regex=False)
        .str.replace(",", ".", regex=False)
    )

    cleaned = cleaned.replace(
        {
            "": None,
            "nan": None,
            "NaN": None,
            "None": None,
            "none": None,
            "-": None,
            "–": None,
            "—": None,
        }
    )

    return pd.to_numeric(cleaned, errors="coerce")


def find_input_file(input_path: str | None) -> Path:
    if input_path:
        path = Path(input_path)
        if not path.exists():
            raise FileNotFoundError(f"Soubor neexistuje: {path}")
        return path

    VISOH_RAW_DIR.mkdir(parents=True, exist_ok=True)
    candidates = []
    for pattern in ["*.xlsx", "*.xls", "*.csv"]:
        candidates.extend(VISOH_RAW_DIR.glob(pattern))

    candidates = sorted(candidates, key=lambda p: p.stat().st_mtime, reverse=True)

    if not candidates:
        raise FileNotFoundError(
            "Nenašel jsem žádný VISOH2 export.\n"
            f"Ulož XLSX/CSV do: {VISOH_RAW_DIR}\n"
            "nebo spusť skript s parametrem --input."
        )

    if len(candidates) > 1:
        print("[INFO] Nalezeno více kandidátů, používám nejnovější:")
        for p in candidates[:10]:
            print(" ", p.name, f"{p.stat().st_size / 1024 / 1024:.2f} MB")

    return candidates[0]


def read_visoh_export(path: Path) -> pd.DataFrame:
    print(f"[INFO] Načítám VISOH2 export: {path}")

    suffix = path.suffix.lower()

    if suffix in [".xlsx", ".xls"]:
        raw = pd.read_excel(path, sheet_name=0, header=None, dtype=object)
    elif suffix == ".csv":
        try:
            raw = pd.read_csv(path, header=None, dtype=object, sep=None, engine="python")
        except UnicodeDecodeError:
            raw = pd.read_csv(path, header=None, dtype=object, sep=None, engine="python", encoding="cp1250")
    else:
        raise ValueError(f"Nepodporovaný formát: {suffix}")

    header_idx = None

    for idx in range(min(30, len(raw))):
        values = [normalize_col(x) for x in raw.iloc[idx].tolist()]
        joined = " | ".join(values)
        if "Rok" in values and "Obec" in values and ("Obec - kód" in values or "Obec-kód" in values or "Kód obce" in values):
            header_idx = idx
            break
        if "Rok" in joined and "Obec" in joined and "kód" in joined:
            header_idx = idx
            break

    if header_idx is None:
        raise RuntimeError(
            "Nepodařilo se najít hlavičku. Očekávám řádek se sloupci Rok, Obec, Obec - kód."
        )

    columns = [normalize_col(x) for x in raw.iloc[header_idx].tolist()]
    df = raw.iloc[header_idx + 1 :].copy()
    df.columns = columns
    df = df.dropna(how="all").copy()

    unnamed = [c for c in df.columns if c == ""]
    if unnamed:
        df = df.drop(columns=unnamed)

    print(f"[INFO] Hlavička nalezena na řádku: {header_idx + 1}")
    print(f"[INFO] Řádků v exportu: {len(df):,}")
    print("[INFO] Sloupce:")
    for c in df.columns:
        print(" ", c)

    return df


def find_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    col_map = {norm_key(c): c for c in df.columns}

    for candidate in candidates:
        key = norm_key(candidate)
        if key in col_map:
            return col_map[key]

    for col in df.columns:
        col_key = norm_key(col)
        for candidate in candidates:
            candidate_key = norm_key(candidate)
            if candidate_key and candidate_key in col_key:
                return col

    return None


def load_population() -> pd.DataFrame:
    if not MUNICIPALITY_RAW_PATH.exists():
        raise FileNotFoundError(
            f"Chybí {MUNICIPALITY_RAW_PATH}. Nejdřív spusť základní pipeline."
        )

    df = pd.read_csv(MUNICIPALITY_RAW_PATH, dtype={"kod_obce": str})
    if "kod_obce" not in df.columns or "population" not in df.columns:
        raise ValueError("municipality_indicators_raw.csv musí obsahovat kod_obce a population.")

    out_cols = ["kod_obce", "population"]
    for col in ["obec", "okres", "orp", "kraj", "size_category", "size_category_final", "settlement_type"]:
        if col in df.columns:
            out_cols.append(col)

    out = df[out_cols].copy()
    out["kod_obce"] = out["kod_obce"].map(clean_code)
    out["population"] = pd.to_numeric(out["population"], errors="coerce")

    return out.drop_duplicates("kod_obce")


def normalize_percent(series: pd.Series) -> pd.Series:
    values = to_number(series)
    valid = values.dropna()

    if valid.empty:
        return values

    if valid.quantile(0.95) <= 1.5:
        return values * 100

    return values


def build_waste_raw(export_df: pd.DataFrame, population_df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {}

    for target, candidates in BASE_COLUMNS.items():
        col = find_column(export_df, candidates)
        if col is None:
            raise ValueError(f"V exportu chybí povinný sloupec pro {target}: {candidates}")
        rename_map[col] = target

    for target, candidates in SOURCE_COLUMNS.items():
        col = find_column(export_df, candidates)
        if col is not None:
            rename_map[col] = target
        else:
            print(f"[WARN] Nenalezen zdrojový sloupec pro {target}: {candidates}")

    df = export_df.rename(columns=rename_map).copy()

    keep_cols = [
        "year",
        "kraj",
        "obec",
        "kod_obce",
        *SOURCE_COLUMNS.keys(),
    ]
    keep_cols = [c for c in keep_cols if c in df.columns]
    df = df[keep_cols].copy()

    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    df["kod_obce"] = df["kod_obce"].map(clean_code)
    df["obec"] = df["obec"].astype(str).str.strip()
    df["kraj"] = df["kraj"].astype(str).str.strip()

    df = df[df["year"].notna()].copy()
    df = df[df["kod_obce"].str.len().eq(6)].copy()

    for col in SOURCE_COLUMNS.keys():
        if col not in df.columns:
            continue
        if col in ["waste_sorting_target_share", "plastic_separation_efficiency"]:
            df[col] = normalize_percent(df[col])
        else:
            df[col] = to_number(df[col])

    df = df.merge(population_df, on="kod_obce", how="left", suffixes=("", "_pipeline"))

    if "obec_pipeline" in df.columns:
        df["obec"] = df["obec"].where(df["obec"].notna() & df["obec"].ne(""), df["obec_pipeline"])
        df = df.drop(columns=["obec_pipeline"])

    for out_col, tonnes_col in DERIVED_PER_CAPITA.items():
        if tonnes_col not in df.columns:
            continue
        df[out_col] = df[tonnes_col] * 1000 / df["population"]
        df.loc[df["population"].isna() | (df["population"] <= 0), out_col] = pd.NA

    ordered = [
        "kod_obce",
        "obec",
        "kraj",
        "year",
        "population",
        "waste_sorting_target_share",
        "municipal_waste_kg_per_capita",
        "mixed_municipal_waste_kg_per_capita",
        "bulky_waste_kg_per_capita",
        "separated_recyclables_kg_per_capita",
        "paper_separation_kg_per_capita",
        "plastic_separation_kg_per_capita",
        "glass_separation_kg_per_capita",
        "metal_separation_kg_per_capita",
        "bio_waste_kg_per_capita",
        "textile_waste_kg_per_capita",
        "hazardous_waste_kg_per_capita",
        "plastic_separation_efficiency",
        "municipal_waste_tonnes",
        "mixed_municipal_waste_tonnes",
        "bulky_waste_tonnes",
        "separated_recyclables_tonnes",
        "plastic_separation_tonnes",
        "bio_waste_tonnes",
    ]

    ordered = [c for c in ordered if c in df.columns]
    rest = [c for c in df.columns if c not in ordered]
    df = df[ordered + rest].copy()

    df = df.sort_values(["kod_obce", "year"]).reset_index(drop=True)

    return df


def classify_trend(v_start, v_end, direction: str) -> str:
    if pd.isna(v_start) or pd.isna(v_end):
        return "bez dat"

    diff = v_end - v_start
    tolerance = max(0.000001, abs(v_start) * 0.001)

    if abs(diff) <= tolerance:
        return "stabilní"

    if direction == "UP":
        return "zlepšení" if diff > 0 else "zhoršení"

    if direction == "DOWN":
        return "zlepšení" if diff < 0 else "zhoršení"

    return "roste" if diff > 0 else "klesá"


def build_wide(waste_raw: pd.DataFrame) -> pd.DataFrame:
    years = sorted(int(y) for y in waste_raw["year"].dropna().unique())
    if not years:
        raise RuntimeError("V datech nejsou žádné roky.")

    first_year = years[0]
    latest_year = years[-1]
    prev_year = years[-2] if len(years) >= 2 else None

    base = waste_raw[["kod_obce", "obec", "kraj", "population"]].drop_duplicates("kod_obce").copy()

    indicators = [c for c in PUBLIC_INDICATORS if c in waste_raw.columns]

    wide = base.copy()

    for indicator in indicators:
        pivot = (
            waste_raw.pivot_table(
                index="kod_obce",
                columns="year",
                values=indicator,
                aggfunc="first",
            )
            .reset_index()
            .copy()
        )

        pivot.columns = [
            "kod_obce" if c == "kod_obce" else f"{indicator}_{int(c)}"
            for c in pivot.columns
        ]

        wide = wide.merge(pivot, on="kod_obce", how="left")

        latest_col = f"{indicator}_{latest_year}"
        first_col = f"{indicator}_{first_year}"

        if latest_col in wide.columns:
            wide[indicator] = wide[latest_col]

        if latest_col in wide.columns and first_col in wide.columns:
            wide[f"{indicator}_diff_{latest_year}_{first_year}"] = wide[latest_col] - wide[first_col]
            wide[f"{indicator}_trend_{first_year}_{latest_year}"] = wide.apply(
                lambda row: classify_trend(
                    row[first_col],
                    row[latest_col],
                    DIRECTION.get(indicator, "CONTEXT"),
                ),
                axis=1,
            )

        if prev_year is not None:
            prev_col = f"{indicator}_{prev_year}"
            if latest_col in wide.columns and prev_col in wide.columns:
                wide[f"{indicator}_diff_{latest_year}_{prev_year}"] = wide[latest_col] - wide[prev_col]

    wide["waste_data_first_year"] = first_year
    wide["waste_data_latest_year"] = latest_year

    return wide.sort_values("kod_obce").reset_index(drop=True)


def merge_into_municipality_raw(wide: pd.DataFrame) -> None:
    print("[INFO] Doplňuji municipality_indicators_raw.csv o nejnovější odpadové ukazatele...")

    muni = pd.read_csv(MUNICIPALITY_RAW_PATH, dtype={"kod_obce": str})
    muni["kod_obce"] = muni["kod_obce"].map(clean_code)

    merge_cols = ["kod_obce", "waste_data_first_year", "waste_data_latest_year"]

    for indicator in PUBLIC_INDICATORS:
        if indicator in wide.columns:
            merge_cols.append(indicator)

    merge_cols = [c for c in merge_cols if c in wide.columns]
    add = wide[merge_cols].copy()

    for col in merge_cols:
        if col == "kod_obce":
            continue
        if col in muni.columns:
            muni = muni.drop(columns=[col])

    muni = muni.merge(add, on="kod_obce", how="left")

    muni.to_csv(MUNICIPALITY_RAW_PATH, index=False, encoding="utf-8-sig")
    print(f"[OK] Doplněno: {MUNICIPALITY_RAW_PATH}")


def write_methodology_summary(waste_raw: pd.DataFrame, wide: pd.DataFrame) -> None:
    out_path = PROJECT_ROOT / "outputs" / "visoh2_waste_summary.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    years = sorted(int(y) for y in waste_raw["year"].dropna().unique())

    lines = []
    lines.append("# VISOH2 odpady — souhrn zpracování")
    lines.append("")
    lines.append(f"Počet řádků v raw datech: {len(waste_raw):,}")
    lines.append(f"Počet obcí ve wide datech: {wide['kod_obce'].nunique():,}")
    lines.append(f"Dostupné roky: {', '.join(map(str, years))}")
    lines.append("")
    lines.append("## Vytvořené veřejné ukazatele")
    lines.append("")

    labels = {
        "waste_sorting_target_share": "Plnění cíle třídění (%)",
        "municipal_waste_kg_per_capita": "Produkce komunálního odpadu (kg/obyv.)",
        "mixed_municipal_waste_kg_per_capita": "Produkce směsného komunálního odpadu (kg/obyv.)",
        "bulky_waste_kg_per_capita": "Produkce objemného odpadu (kg/obyv.)",
        "separated_recyclables_kg_per_capita": "Separované recyklovatelné složky (kg/obyv.)",
        "plastic_separation_kg_per_capita": "Separace plastu (kg/obyv.)",
        "plastic_separation_efficiency": "Účinnost separace plastu (%)",
        "bio_waste_kg_per_capita": "Bioodpad (kg/obyv.)",
    }

    for indicator in PUBLIC_INDICATORS:
        if indicator in wide.columns:
            non_missing = wide[indicator].notna().sum()
            lines.append(f"- `{indicator}` — {labels.get(indicator, indicator)}; vyplněno u {non_missing:,} obcí")

    lines.append("")
    lines.append("## Poznámka")
    lines.append("")
    lines.append("Hodnoty z VISOH2 typu `I.O.1KO`, `I.O.2SKO`, `I.O.3Obj`, `I.O.5...` jsou zpracovány jako tuny za rok a pro dashboard jsou přepočteny na kg/obyvatele pomocí populační hodnoty z `municipality_indicators_raw.csv`.")
    lines.append("Procentní ukazatele z VISOH2 jsou převedeny z podílu 0–1 na procenta 0–100, pokud export obsahuje desetinný podíl.")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] Souhrn metodiky: {out_path}")


def run(input_path: str | None = None) -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    VISOH_RAW_DIR.mkdir(parents=True, exist_ok=True)

    path = find_input_file(input_path)
    export_df = read_visoh_export(path)
    population_df = load_population()

    waste_raw = build_waste_raw(export_df, population_df)
    waste_wide = build_wide(waste_raw)

    waste_raw.to_csv(WASTE_RAW_OUT, index=False, encoding="utf-8-sig")
    waste_wide.to_csv(WASTE_TRENDS_OUT, index=False, encoding="utf-8-sig")

    print(f"[OK] Uloženo: {WASTE_RAW_OUT}")
    print(f"[OK] Uloženo: {WASTE_TRENDS_OUT}")

    merge_into_municipality_raw(waste_wide)
    write_methodology_summary(waste_raw, waste_wide)

    print("")
    print("[INFO] Ukázka Moravičany 540480:")
    mor = waste_wide[waste_wide["kod_obce"].eq("540480")]
    if mor.empty:
        print("Moravičany v exportu nenalezeny.")
    else:
        cols = [
            "kod_obce",
            "obec",
            "waste_data_first_year",
            "waste_data_latest_year",
            "waste_sorting_target_share",
            "municipal_waste_kg_per_capita",
            "mixed_municipal_waste_kg_per_capita",
            "plastic_separation_efficiency",
        ]
        cols = [c for c in cols if c in mor.columns]
        print(mor[cols].to_string(index=False))

    print("")
    print("[OK] Hotovo.")
    print("")
    print("Další krok:")
    print("1) Zkontroluj výstupy:")
    print(f"   head -n 5 {WASTE_RAW_OUT}")
    print(f"   head -n 5 {WASTE_TRENDS_OUT}")
    print("")
    print("2) Potom upravíme dashboard 14_generate_interactive_map_business_dashboard.py,")
    print("   aby nové odpadové ukazatele nabízel v mapě.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default=None,
        help="Cesta k ručně staženému exportu VISOH2 XLSX/CSV.",
    )
    args = parser.parse_args()

    run(args.input)


if __name__ == "__main__":
    main()