#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
15_add_age_structure.py

Přidá věkovou strukturu obcí do projektu.

Cíl:
- načíst CSV se základní věkovou strukturou obcí,
- vytvořit standardizované ukazatele:
    children_share       = podíl obyvatel 0–14 let
    working_age_share    = podíl obyvatel 15–64 let
    senior_share         = podíl obyvatel 65+ let
    ageing_index         = senioři 65+ / děti 0–14 × 100
- vytvořit časovou řadu 2020–2024,
- vytvořit wide trendovou tabulku,
- připojit poslední rok 2024 do municipality_indicators_raw.csv,
- připravit výstup pro business dashboard.

Očekávaný vstup:
    data/raw/csu_age_structure_basic.csv

Soubor může být export z ČSÚ/DataStat nebo ručně připravený CSV.
Skript se snaží automaticky najít sloupce pro:
- rok,
- kód obce,
- věkovou skupinu,
- hodnotu,
- pohlaví.

Výstupy:
    data/processed/age_structure_timeseries.csv
    data/processed/age_structure_trends_wide.csv
    data/processed/municipality_indicators_raw.csv  doplněný o věkové ukazatele 2024

Spuštění:
    python municipal_map_mvp/src/15_add_age_structure.py

Volitelně:
    python municipal_map_mvp/src/15_add_age_structure.py --input data/raw/csu_age_structure_basic.csv
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

DEFAULT_INPUT_PATH = RAW_DIR / "csu_age_structure_basic.csv"

INDICATORS_RAW_PATH = PROCESSED_DIR / "municipality_indicators_raw.csv"

AGE_TIMESERIES_OUT = PROCESSED_DIR / "age_structure_timeseries.csv"
AGE_TRENDS_WIDE_OUT = PROCESSED_DIR / "age_structure_trends_wide.csv"

YEARS = [2020, 2021, 2022, 2023, 2024]
BASE_YEAR = 2020
PREVIOUS_YEAR = 2023
CURRENT_YEAR = 2024


# =============================================================================
# POMOCNÉ FUNKCE
# =============================================================================

def normalize_text(value) -> str:
    """Normalizuje text pro robustní hledání názvů sloupců a kategorií."""
    if pd.isna(value):
        return ""

    text = str(value)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return text.strip()


def clean_code(value) -> str:
    """Vyčistí kód obce / ZÚJ."""
    if pd.isna(value):
        return ""

    text = str(value).strip().replace(".0", "")

    # Pokud by kód měl leading zeros, zachováme textovou podobu.
    return text


def read_csv_smart(path: Path) -> pd.DataFrame:
    """Načte CSV s tolerancí na české kódování a oddělovače."""
    last_error = None

    for enc in ["utf-8-sig", "utf-8", "cp1250", "windows-1250", "latin-1"]:
        for sep in [",", ";", "\t"]:
            try:
                df = pd.read_csv(path, encoding=enc, sep=sep, dtype=str)
                if df.shape[1] > 1:
                    return df
            except Exception as exc:
                last_error = exc

    raise RuntimeError(f"Nepodařilo se načíst {path}: {last_error}")


def find_column(df: pd.DataFrame, candidates: list[str], required: bool = True) -> str | None:
    """Najde sloupec podle normalizovaných názvů."""
    normalized_cols = {normalize_text(c): c for c in df.columns}

    for cand in candidates:
        cand_norm = normalize_text(cand)

        # Přesná shoda
        if cand_norm in normalized_cols:
            return normalized_cols[cand_norm]

    # Částečná shoda
    for cand in candidates:
        cand_norm = normalize_text(cand)

        for norm_col, original_col in normalized_cols.items():
            if cand_norm in norm_col or norm_col in cand_norm:
                return original_col

    if required:
        raise ValueError(
            f"Nepodařilo se najít sloupec pro kandidáty {candidates}.\n"
            f"Dostupné sloupce: {list(df.columns)}"
        )

    return None


def detect_columns(df: pd.DataFrame) -> dict[str, str | None]:
    """Detekuje relevantní sloupce ve vstupním CSV."""
    year_col = find_column(
        df,
        [
            "rok",
            "year",
            "obdobi",
            "ref_period",
            "time",
        ],
    )

    code_col = find_column(
        df,
        [
            "kod_obce",
            "kod obce",
            "zuj",
            "koduzemi",
            "kod uzemi",
            "uzemi kod",
            "vuzemi kod",
            "ref_area",
            "uzemi",
        ],
    )

    age_col = find_column(
        df,
        [
            "vekova skupina",
            "věková skupina",
            "vek",
            "age",
            "age group",
            "v vek",
            "vekovaskupina",
            "vekova_kategorie",
        ],
    )

    value_col = find_column(
        df,
        [
            "hodnota",
            "value",
            "obs_value",
            "pocet",
            "počet",
            "obyvatel",
            "obyvatele",
        ],
    )

    sex_col = find_column(
        df,
        [
            "pohlavi",
            "pohlaví",
            "sex",
        ],
        required=False,
    )

    return {
        "year": year_col,
        "code": code_col,
        "age_group": age_col,
        "value": value_col,
        "sex": sex_col,
    }


def classify_age_group(value) -> str | None:
    """
    Převede různé texty věkových skupin na:
    - children
    - working_age
    - seniors

    Podporuje běžné zápisy:
    0-14, 0–14, 0 až 14, 15-64, 65+, 65 a více apod.
    """
    text = normalize_text(value)

    if not text:
        return None

    # Často se v datech používá "celkem" nebo total, to nechceme jako věkovou skupinu.
    if text in ["celkem", "total", "obyvatelstvo celkem", "celkem obyvatel"]:
        return None

    # Děti 0–14
    children_patterns = [
        "0 14",
        "0 az 14",
        "0 do 14",
        "0 15",
        "0 az 15",
        "do 14",
        "mladsi 15",
        "predproduktivni",
        "0 14 let",
    ]

    for pattern in children_patterns:
        if pattern in text:
            return "children"

    # Produktivní věk 15–64
    working_patterns = [
        "15 64",
        "15 az 64",
        "15 do 64",
        "15 65",
        "15 az 65",
        "produktivni",
        "15 64 let",
    ]

    for pattern in working_patterns:
        if pattern in text:
            return "working_age"

    # Senioři 65+
    senior_patterns = [
        "65",
        "65 a vice",
        "65 vice",
        "65 let a vice",
        "65 plus",
        "poproduktivni",
        "seniori",
        "senior",
    ]

    # Pozor: text "15 64" obsahuje čísla, ale ne 65.
    # Senior zachytíme až po working_age.
    for pattern in senior_patterns:
        if pattern in text:
            return "seniors"

    return None


def is_total_sex(value) -> bool:
    """
    Vrátí True pro celkem obě pohlaví.
    Pokud sloupec pohlaví neexistuje, nefiltrujeme.
    """
    if value is None or pd.isna(value):
        return True

    text = normalize_text(value)

    total_values = [
        "celkem",
        "total",
        "obe pohlavi",
        "obě pohlaví",
        "muzi zeny",
        "muzi a zeny",
        "m z",
        "all",
    ]

    if text in [normalize_text(x) for x in total_values]:
        return True

    # Některé datové exporty mohou používat kód T.
    if text in ["t", "tot", "total"]:
        return True

    return False


def prepare_long_age_structure(input_path: Path) -> pd.DataFrame:
    """Načte vstupní CSV a vytvoří long tabulku věkové struktury."""
    if not input_path.exists():
        raise FileNotFoundError(
            f"Chybí vstupní soubor: {input_path}\n\n"
            "Ulož CSV export věkové struktury do:\n"
            "municipal_map_mvp/data/raw/csu_age_structure_basic.csv\n\n"
            "Potřebné sloupce: rok, kód obce, věková skupina, hodnota."
        )

    print(f"[INFO] Načítám věkovou strukturu: {input_path}")

    df = read_csv_smart(input_path)
    df.columns = [c.strip() for c in df.columns]

    cols = detect_columns(df)

    print("[INFO] Detekované sloupce:")
    for key, col in cols.items():
        print(f"  {key}: {col}")

    year_col = cols["year"]
    code_col = cols["code"]
    age_col = cols["age_group"]
    value_col = cols["value"]
    sex_col = cols["sex"]

    work = df.copy()

    if sex_col is not None:
        work = work[work[sex_col].map(is_total_sex)].copy()

    work["year"] = pd.to_numeric(work[year_col], errors="coerce").astype("Int64")
    work["kod_obce"] = work[code_col].map(clean_code)
    work["age_group_std"] = work[age_col].map(classify_age_group)
    work["value"] = pd.to_numeric(work[value_col], errors="coerce")

    work = work[
        work["year"].isin(YEARS)
        & work["kod_obce"].ne("")
        & work["age_group_std"].notna()
        & work["value"].notna()
    ].copy()

    if work.empty:
        raise ValueError(
            "Po načtení a klasifikaci věkových skupin nezbyl žádný řádek.\n"
            "Zkontroluj, jak jsou ve vstupním CSV pojmenované věkové skupiny."
        )

    grouped = (
        work.groupby(["kod_obce", "year", "age_group_std"], as_index=False)["value"]
        .sum()
    )

    print("[OK] Long věková struktura připravena.")
    print(grouped.head(10).to_string(index=False))

    return grouped


def build_age_indicators(long_df: pd.DataFrame) -> pd.DataFrame:
    """Z long tabulky vytvoří children_share, working_age_share, senior_share, ageing_index."""
    pivot = long_df.pivot_table(
        index=["kod_obce", "year"],
        columns="age_group_std",
        values="value",
        aggfunc="sum",
    ).reset_index()

    for col in ["children", "working_age", "seniors"]:
        if col not in pivot.columns:
            pivot[col] = pd.NA

    pivot["age_total_basic_groups"] = (
        pd.to_numeric(pivot["children"], errors="coerce")
        + pd.to_numeric(pivot["working_age"], errors="coerce")
        + pd.to_numeric(pivot["seniors"], errors="coerce")
    )

    pivot["children_share"] = (
        pd.to_numeric(pivot["children"], errors="coerce")
        / pd.to_numeric(pivot["age_total_basic_groups"], errors="coerce")
        * 100
    )

    pivot["working_age_share"] = (
        pd.to_numeric(pivot["working_age"], errors="coerce")
        / pd.to_numeric(pivot["age_total_basic_groups"], errors="coerce")
        * 100
    )

    pivot["senior_share"] = (
        pd.to_numeric(pivot["seniors"], errors="coerce")
        / pd.to_numeric(pivot["age_total_basic_groups"], errors="coerce")
        * 100
    )

    pivot["ageing_index"] = (
        pd.to_numeric(pivot["seniors"], errors="coerce")
        / pd.to_numeric(pivot["children"], errors="coerce")
        * 100
    )

    # Pokud je počet dětí nulový, index stáří nedává smysl.
    pivot.loc[pd.to_numeric(pivot["children"], errors="coerce").eq(0), "ageing_index"] = pd.NA

    out = pivot[
        [
            "kod_obce",
            "year",
            "children",
            "working_age",
            "seniors",
            "age_total_basic_groups",
            "children_share",
            "working_age_share",
            "senior_share",
            "ageing_index",
        ]
    ].copy()

    for col in out.columns:
        if col not in ["kod_obce", "year"]:
            out[col] = pd.to_numeric(out[col], errors="coerce")

    return out


def make_wide_age_trends(age_ts: pd.DataFrame) -> pd.DataFrame:
    """Vytvoří wide tabulku věkové struktury a změn."""
    indicators = [
        "children",
        "working_age",
        "seniors",
        "children_share",
        "working_age_share",
        "senior_share",
        "ageing_index",
    ]

    pivot = age_ts.pivot_table(
        index="kod_obce",
        columns="year",
        values=indicators,
        aggfunc="first",
    )

    pivot.columns = [
        f"{indicator}_{year}"
        for indicator, year in pivot.columns
    ]

    wide = pivot.reset_index()

    for indicator in indicators:
        c_base = f"{indicator}_{BASE_YEAR}"
        c_prev = f"{indicator}_{CURRENT_YEAR - 1}"
        c_current = f"{indicator}_{CURRENT_YEAR}"

        if c_current in wide.columns and c_prev in wide.columns:
            wide[f"{indicator}_diff_{CURRENT_YEAR}_{CURRENT_YEAR - 1}"] = (
                pd.to_numeric(wide[c_current], errors="coerce")
                - pd.to_numeric(wide[c_prev], errors="coerce")
            )

        if c_current in wide.columns and c_base in wide.columns:
            wide[f"{indicator}_diff_{CURRENT_YEAR}_{BASE_YEAR}"] = (
                pd.to_numeric(wide[c_current], errors="coerce")
                - pd.to_numeric(wide[c_base], errors="coerce")
            )

    return wide


def update_municipality_indicators_raw(age_wide: pd.DataFrame) -> None:
    """Doplní ukazatele věkové struktury za rok 2024 do municipality_indicators_raw.csv."""
    if not INDICATORS_RAW_PATH.exists():
        print(f"[WARN] Chybí {INDICATORS_RAW_PATH}, přeskočeno doplnění raw indikátorů.")
        return

    raw = read_csv_smart(INDICATORS_RAW_PATH)
    raw.columns = [c.strip() for c in raw.columns]
    raw["kod_obce"] = raw["kod_obce"].map(clean_code)

    age = age_wide.copy()
    age["kod_obce"] = age["kod_obce"].map(clean_code)

    cols_2024 = [
        "kod_obce",
        "children_2024",
        "working_age_2024",
        "seniors_2024",
        "children_share_2024",
        "working_age_share_2024",
        "senior_share_2024",
        "ageing_index_2024",
        "children_share_diff_2024_2020",
        "working_age_share_diff_2024_2020",
        "senior_share_diff_2024_2020",
        "ageing_index_diff_2024_2020",
    ]

    age = age[[c for c in cols_2024 if c in age.columns]].copy()

    rename = {
        "children_2024": "children_count",
        "working_age_2024": "working_age_count",
        "seniors_2024": "senior_count",
        "children_share_2024": "children_share",
        "working_age_share_2024": "working_age_share",
        "senior_share_2024": "senior_share",
        "ageing_index_2024": "ageing_index",
        "children_share_diff_2024_2020": "children_share_change_2024_2020",
        "working_age_share_diff_2024_2020": "working_age_share_change_2024_2020",
        "senior_share_diff_2024_2020": "senior_share_change_2024_2020",
        "ageing_index_diff_2024_2020": "ageing_index_change_2024_2020",
    }

    age = age.rename(columns=rename)

    # Odstraníme staré věkové sloupce, pokud už existují.
    for col in age.columns:
        if col != "kod_obce" and col in raw.columns:
            raw = raw.drop(columns=[col])

    out = raw.merge(age, on="kod_obce", how="left")

    out.to_csv(INDICATORS_RAW_PATH, index=False, encoding="utf-8-sig")

    print(f"[OK] municipality_indicators_raw.csv doplněn o věkovou strukturu: {INDICATORS_RAW_PATH}")


def run(input_path: Path) -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    long_age = prepare_long_age_structure(input_path)
    age_ts = build_age_indicators(long_age)
    age_wide = make_wide_age_trends(age_ts)

    age_ts.to_csv(AGE_TIMESERIES_OUT, index=False, encoding="utf-8-sig")
    age_wide.to_csv(AGE_TRENDS_WIDE_OUT, index=False, encoding="utf-8-sig")

    print(f"[OK] Uloženo: {AGE_TIMESERIES_OUT}")
    print(f"[OK] Uloženo: {AGE_TRENDS_WIDE_OUT}")

    update_municipality_indicators_raw(age_wide)

    # Kontrola Moravičan
    mor = age_wide[age_wide["kod_obce"].astype(str).eq("540480")]
    if not mor.empty:
        cols = [
            "kod_obce",
            "children_share_2024",
            "working_age_share_2024",
            "senior_share_2024",
            "ageing_index_2024",
            "children_share_diff_2024_2020",
            "senior_share_diff_2024_2020",
            "ageing_index_diff_2024_2020",
        ]
        print("\nKontrola Moravičany:")
        print(mor[[c for c in cols if c in mor.columns]].to_string(index=False))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Přidá věkovou strukturu obcí a její změnu 2020–2024."
    )
    parser.add_argument(
        "--input",
        default=str(DEFAULT_INPUT_PATH),
        help=(
            "Cesta k CSV se základní věkovou strukturou obcí. "
            "Výchozí: data/raw/csu_age_structure_basic.csv"
        ),
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run(Path(args.input))