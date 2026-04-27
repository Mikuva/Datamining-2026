#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
download_age_structure_oby02e.py

Stáhne nebo načte dataset ČSÚ/DataStat OBY02E:
"Obyvatelstvo podle pohlaví a základních věkových skupin".

Cíl:
- použít data za obce,
- vybrat roky 2020–2024,
- vybrat pohlaví celkem,
- vybrat základní věkové skupiny:
    0–14
    15–64
    65+
- uložit jednotný vstup pro další krok:
    data/raw/csu_age_structure_basic.csv

Výstupní soubor:
    rok,kod_obce,vekova_skupina,vekova_skupina_std,hodnota

Spuštění:
    python municipal_map_mvp/src/download_age_structure_oby02e.py

Volitelně z lokálního souboru:
    python municipal_map_mvp/src/download_age_structure_oby02e.py --input municipal_map_mvp/data/raw/OD_DEM05_vse_2025051511393673.CSV

Potom:
    python municipal_map_mvp/src/15_add_age_structure.py
"""

from __future__ import annotations

import argparse
import re
import unicodedata
import zipfile
from pathlib import Path

import pandas as pd
import requests


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"

OUTPUT_PATH = RAW_DIR / "csu_age_structure_basic.csv"
DOWNLOAD_ZIP_PATH = RAW_DIR / "oby02e_data.zip"
EXTRACT_DIR = RAW_DIR / "oby02e_extracted"

# DataStat OBY02E data ZIP. Pokud ČSÚ změní verzi souboru,
# použij --input s ručně staženým CSV z dashboardu DataStat.
DEFAULT_ZIP_URL = "https://data.csu.gov.cz/opendata/sady/OBY02E/130149-25data052025.zip"

YEARS = [2020, 2021, 2022, 2023, 2024]

# ČSÚ číselník území:
# 43 = obce
MUNICIPALITY_AREA_CODE = "43"

# Kódy věkových skupin podle dokumentace OBY02E.
AGE_CODE_TO_STD = {
    "400000610015000": "0-14",
    "410015610065000": "15-64",
    "410065799999000": "65+",
}

AGE_STD_ORDER = {
    "0-14": 1,
    "15-64": 2,
    "65+": 3,
}


def normalize_text(value) -> str:
    """Normalizace textu pro porovnávání bez diakritiky."""
    if pd.isna(value):
        return ""

    text = str(value)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return text.strip()


def clean_code(value) -> str:
    """Vrátí šestimístný kód obce jako text."""
    if pd.isna(value):
        return ""

    text = str(value).strip().replace(".0", "")
    digits = re.sub(r"\D", "", text)

    if len(digits) == 6:
        return digits

    return ""


def detect_separator(path: Path) -> str:
    """Jednoduchá detekce oddělovače CSV."""
    sample = path.read_text(encoding="utf-8-sig", errors="ignore")[:20000]

    if sample.count(";") > sample.count(","):
        return ";"

    return ","


def read_header(path: Path) -> list[str]:
    """Načte pouze hlavičku CSV."""
    sep = detect_separator(path)
    header = pd.read_csv(path, sep=sep, nrows=0, encoding="utf-8-sig")
    return list(header.columns)


def find_column(columns: list[str], candidates: list[str], required: bool = True) -> str | None:
    """Najde sloupec podle možných názvů."""
    normalized = {normalize_text(col): col for col in columns}

    for candidate in candidates:
        key = normalize_text(candidate)
        if key in normalized:
            return normalized[key]

    for candidate in candidates:
        key = normalize_text(candidate)
        for norm_col, original_col in normalized.items():
            if key and (key in norm_col or norm_col in key):
                return original_col

    if required:
        raise ValueError(
            "Nenalezen sloupec pro kandidáty: "
            + str(candidates)
            + "\nDostupné sloupce: "
            + str(columns)
        )

    return None


def classify_age_group_from_code(value) -> str | None:
    """Klasifikace věkové skupiny podle kódu."""
    if pd.isna(value):
        return None

    code = str(value).strip().replace(".0", "")
    return AGE_CODE_TO_STD.get(code)


def classify_age_group_from_text(value) -> str | None:
    """Klasifikace věkové skupiny podle textu."""
    text = normalize_text(value)

    if not text:
        return None

    if text in {"celkem", "total", "obyvatelstvo celkem"}:
        return None

    # 0 až 14
    if (
        "0 az 14" in text
        or "0 14" in text
        or "0 do 14" in text
        or "do 14" in text
        or "mladsi 15" in text
    ):
        return "0-14"

    # 15 až 64
    if (
        "15 az 64" in text
        or "15 64" in text
        or "15 do 64" in text
    ):
        return "15-64"

    # 65 a více
    if (
        "65 a vice" in text
        or "65 vice" in text
        or "65 plus" in text
        or text == "65"
    ):
        return "65+"

    return None


def is_total_sex(row: pd.Series, sex_code_col: str | None, sex_text_col: str | None) -> bool:
    """
    Vrátí True pro pohlaví celkem.

    V dokumentaci OBY02E je uvedeno, že pokud pohlaví_kod není vyplněn,
    jedná se o osoby celkem. Některé exporty mohou mít i text "celkem".
    """
    if sex_code_col is not None:
        code = row.get(sex_code_col)

        if pd.isna(code) or str(code).strip() == "":
            return True

        norm_code = normalize_text(code)
        if norm_code in {"celkem", "total", "t", "all"}:
            return True

    if sex_text_col is not None:
        text = normalize_text(row.get(sex_text_col))
        if text in {"celkem", "total", "obe pohlavi", "muzi a zeny", "all"}:
            return True

    return False


def extract_year(value) -> int | None:
    """Získá rok z hodnoty typu 2024 nebo 2024-12-31."""
    if pd.isna(value):
        return None

    match = re.search(r"(20\d{2})", str(value))
    if not match:
        return None

    return int(match.group(1))


def download_zip(force: bool = False) -> Path:
    """Stáhne ZIP s daty OBY02E, pokud není lokálně."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if DOWNLOAD_ZIP_PATH.exists() and not force:
        print(f"[OK] ZIP už existuje, stahování přeskočeno: {DOWNLOAD_ZIP_PATH}")
        return DOWNLOAD_ZIP_PATH

    print("[INFO] Stahuji OBY02E ZIP:")
    print(DEFAULT_ZIP_URL)

    response = requests.get(DEFAULT_ZIP_URL, timeout=300)
    response.raise_for_status()

    DOWNLOAD_ZIP_PATH.write_bytes(response.content)

    size_mb = DOWNLOAD_ZIP_PATH.stat().st_size / 1024 / 1024
    print(f"[OK] Staženo: {DOWNLOAD_ZIP_PATH} ({size_mb:.2f} MB)")

    return DOWNLOAD_ZIP_PATH


def find_csv_in_zip(zip_path: Path) -> Path:
    """Rozbalí ZIP a najde hlavní CSV soubor."""
    EXTRACT_DIR.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(EXTRACT_DIR)

    csv_files = sorted(EXTRACT_DIR.glob("*.csv")) + sorted(EXTRACT_DIR.glob("*.CSV"))

    if not csv_files:
        raise FileNotFoundError(f"V ZIPu nebyl nalezen CSV soubor: {zip_path}")

    # Preferujeme datový soubor, ne případnou dokumentaci.
    csv_files = sorted(csv_files, key=lambda p: p.stat().st_size, reverse=True)

    selected = csv_files[0]
    print(f"[OK] Nalezen CSV soubor v ZIPu: {selected}")

    return selected


def choose_input_file(input_path: str | None, force_download: bool = False) -> Path:
    """Vybere vstupní CSV: explicitní soubor, lokální OD_DEM05, nebo stažený ZIP."""
    if input_path:
        path = Path(input_path)
        if not path.exists():
            raise FileNotFoundError(f"Zadaný vstupní soubor neexistuje: {path}")
        return path

    # Pokud už máš ručně stažený DataStat CSV v raw složce, použije se.
    candidates = sorted(RAW_DIR.glob("OD_DEM05*.CSV")) + sorted(RAW_DIR.glob("OD_DEM05*.csv"))

    if candidates:
        selected = candidates[0]
        print(f"[OK] Používám lokální DataStat CSV: {selected}")
        return selected

    zip_path = download_zip(force=force_download)
    return find_csv_in_zip(zip_path)


def build_filtered_file(input_csv: Path) -> None:
    """Z CSV OBY02E vytvoří zjednodušený soubor pro projekt."""
    sep = detect_separator(input_csv)
    columns = read_header(input_csv)

    print(f"[INFO] Vstupní CSV: {input_csv}")
    print(f"[INFO] Oddělovač: {repr(sep)}")
    print("[INFO] Sloupce:")
    print(columns)

    value_col = find_column(columns, ["hodnota", "value", "obs_value"])
    area_codebook_col = find_column(columns, ["uzemi_cis", "vuzemi_cis"], required=False)
    area_code_col = find_column(columns, ["uzemi_kod", "vuzemi_kod", "kod_obce", "zuj", "koduzemi"])
    period_col = find_column(columns, ["rok", "obdobi", "casref_do", "referencni obdobi"])
    sex_code_col = find_column(columns, ["pohlavi_kod"], required=False)
    sex_text_col = find_column(columns, ["pohlavi_txt", "pohlavi"], required=False)
    age_code_col = find_column(columns, ["vek_kod"], required=False)
    age_text_col = find_column(columns, ["vek_txt", "vek", "vekova skupina", "vekove skupiny"], required=False)

    if age_code_col is None and age_text_col is None:
        raise ValueError(
            "Nenalezen sloupec vek_kod ani vek_txt. "
            "Tento CSV zřejmě není obecní dataset OBY02E se základními věkovými skupinami."
        )

    print("[INFO] Použité sloupce:")
    print(f"  hodnota: {value_col}")
    print(f"  uzemi_cis/vuzemi_cis: {area_codebook_col}")
    print(f"  uzemi_kod/vuzemi_kod: {area_code_col}")
    print(f"  rok/obdobi: {period_col}")
    print(f"  pohlavi_kod: {sex_code_col}")
    print(f"  pohlavi_txt: {sex_text_col}")
    print(f"  vek_kod: {age_code_col}")
    print(f"  vek_txt: {age_text_col}")

    frames: list[pd.DataFrame] = []
    chunksize = 250_000

    usecols = [
        c for c in [
            value_col,
            area_codebook_col,
            area_code_col,
            period_col,
            sex_code_col,
            sex_text_col,
            age_code_col,
            age_text_col,
        ]
        if c is not None
    ]

    for chunk in pd.read_csv(
        input_csv,
        sep=sep,
        dtype=str,
        encoding="utf-8-sig",
        chunksize=chunksize,
        usecols=usecols,
    ):
        part = chunk.copy()

        # Filtr: obce. Pokud sloupec s číselníkem území není v exportu, bereme pouze řádky s 6místným kódem.
        if area_codebook_col is not None:
            part = part[part[area_codebook_col].astype(str).str.strip().eq(MUNICIPALITY_AREA_CODE)].copy()

        part["kod_obce"] = part[area_code_col].map(clean_code)
        part = part[part["kod_obce"].ne("")].copy()

        part["rok"] = part[period_col].map(extract_year)
        part = part[part["rok"].isin(YEARS)].copy()

        if part.empty:
            continue

        part["_is_total_sex"] = part.apply(
            lambda row: is_total_sex(row, sex_code_col, sex_text_col),
            axis=1,
        )
        part = part[part["_is_total_sex"]].copy()

        if part.empty:
            continue

        if age_code_col is not None:
            part["vekova_skupina_std"] = part[age_code_col].map(classify_age_group_from_code)
        else:
            part["vekova_skupina_std"] = None

        if age_text_col is not None:
            missing_age = part["vekova_skupina_std"].isna()
            part.loc[missing_age, "vekova_skupina_std"] = part.loc[missing_age, age_text_col].map(
                classify_age_group_from_text
            )
            part["vekova_skupina"] = part[age_text_col].astype(str)
        else:
            part["vekova_skupina"] = part[age_code_col].astype(str)

        part = part[part["vekova_skupina_std"].notna()].copy()

        if part.empty:
            continue

        part["hodnota"] = pd.to_numeric(part[value_col], errors="coerce")
        part = part[part["hodnota"].notna()].copy()

        part = part[
            [
                "rok",
                "kod_obce",
                "vekova_skupina",
                "vekova_skupina_std",
                "hodnota",
            ]
        ]

        frames.append(part)

    if not frames:
        raise RuntimeError(
            "Po filtrování nezbyla žádná data. "
            "Zkontroluj, že vstup je opravdu OBY02E s obcemi, pohlavím celkem a věkovými skupinami."
        )

    out = pd.concat(frames, ignore_index=True)

    # Pokud je v datech více řádků pro stejnou kombinaci, sečteme je.
    out = (
        out.groupby(["rok", "kod_obce", "vekova_skupina_std"], as_index=False)["hodnota"]
        .sum()
    )

    labels = {
        "0-14": "0 až 14",
        "15-64": "15 až 64",
        "65+": "65 a více",
    }

    out["vekova_skupina"] = out["vekova_skupina_std"].map(labels)
    out["_order"] = out["vekova_skupina_std"].map(AGE_STD_ORDER)

    out = out.sort_values(["kod_obce", "rok", "_order"])
    out = out.drop(columns=["_order"])

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

    print(f"[OK] Vytvořen soubor: {OUTPUT_PATH}")
    print(f"[INFO] Řádků: {len(out):,}")

    print("\n[INFO] Ukázka:")
    print(out.head(20).to_string(index=False))

    print("\n[INFO] Kontrola Moravičany 540480:")
    mor = out[out["kod_obce"].eq("540480")]
    print(mor.to_string(index=False))

    expected_rows_per_municipality = len(YEARS) * 3
    mor_count = len(mor)
    if mor_count != expected_rows_per_municipality:
        print(
            f"[WARN] Moravičany mají {mor_count} řádků, očekáváno {expected_rows_per_municipality}. "
            "Zkontroluj vstupní data."
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Stáhne nebo načte OBY02E a vytvoří csu_age_structure_basic.csv."
    )
    parser.add_argument(
        "--input",
        default=None,
        help="Volitelná cesta k ručně staženému CSV DataStat OBY02E.",
    )
    parser.add_argument(
        "--force-download",
        action="store_true",
        help="Znovu stáhne ZIP z ČSÚ i pokud už existuje.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_csv = choose_input_file(args.input, force_download=args.force_download)
    build_filtered_file(input_csv)


if __name__ == "__main__":
    main()