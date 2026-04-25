#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pipeline_core_scripts_02_06.py

Společný MVP skript pro kroky:
- config      vytvoří indicator_catalog.csv
- geo         vytvoří geo_master.csv
- indicators  vytvoří municipality_indicators_raw.csv
- score       vytvoří municipality_scores.csv a dimension_scores.csv
- map         vytvoří HTML mapu, pokud existuje GeoJSON
- case        vytvoří případovou studii Moravičany

Spuštění z rootu repozitáře:

    python municipal_map_mvp/src/pipeline_core_scripts_02_06.py config
    python municipal_map_mvp/src/pipeline_core_scripts_02_06.py geo
    python municipal_map_mvp/src/pipeline_core_scripts_02_06.py indicators
    python municipal_map_mvp/src/pipeline_core_scripts_02_06.py score
    python municipal_map_mvp/src/pipeline_core_scripts_02_06.py case
    python municipal_map_mvp/src/pipeline_core_scripts_02_06.py map

Poznámka:
- Pro první MVP je vše v jednom souboru, aby se to lépe kopírovalo a spouštělo.
- Později lze rozdělit do souborů utils.py, 02_prepare_geo_master.py atd.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


# =============================================================================
# CESTY
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
GEO_DIR = DATA_DIR / "geo"
CONFIG_DIR = PROJECT_ROOT / "config"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"


# =============================================================================
# SPOLEČNÉ POMOCNÉ FUNKCE
# =============================================================================

def ensure_dirs() -> None:
    """Vytvoří potřebné složky, pokud neexistují."""
    for path in [RAW_DIR, PROCESSED_DIR, GEO_DIR, CONFIG_DIR, OUTPUTS_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def normalize_text(value: Any) -> str:
    """Normalizuje text pro porovnávání názvů sloupců a ukazatelů."""
    text = "" if value is None else str(value)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def compact(value: Any) -> str:
    """Normalizuje text a odstraní mezery."""
    return re.sub(r"[^a-z0-9]+", "", normalize_text(value))


def guess_col(df: pd.DataFrame, candidates: list[str], required: bool = False) -> str | None:
    """
    Najde sloupec podle možných názvů.

    Funguje tolerantně vůči diakritice, velikosti písmen a podtržítkům.
    """
    if df is None:
        if required:
            raise ValueError("DataFrame je None, nelze hledat sloupec.")
        return None

    normalized = {compact(col): col for col in df.columns}

    for candidate in candidates:
        key = compact(candidate)
        if key in normalized:
            return normalized[key]

    for col in df.columns:
        col_key = compact(col)
        for candidate in candidates:
            key = compact(candidate)
            if key and key in col_key:
                return col

    if required:
        raise ValueError(
            f"Nenalezen povinný sloupec. Kandidáti: {candidates}. "
            f"Dostupné sloupce: {list(df.columns)}"
        )

    return None


def read_csv_smart(path: str | Path) -> pd.DataFrame:
    """
    Načte CSV s tolerantní detekcí oddělovače a kódování.

    ČSÚ uvádí MOS CSV jako UTF-8, ale pro jistotu zkoušíme více kódování.
    """
    path = Path(path)
    last_error: Exception | None = None

    for enc in ["utf-8-sig", "utf-8", "cp1250", "windows-1250", "latin-1"]:
        try:
            return pd.read_csv(path, sep=None, engine="python", encoding=enc)
        except Exception as exc:
            last_error = exc

    raise RuntimeError(f"Nepodařilo se načíst CSV {path}: {last_error}")


def clean_municipality_code(value: Any) -> str | None:
    """
    Vrátí kód obce / ZÚJ jako šestimístný text.

    Nepoužíváme zfill(6). Chybný pětimístný kód nesmí být tiše změněn
    na zdánlivě validní šestimístný kód.
    """
    if value is None:
        return None

    try:
        if pd.isna(value):
            return None
    except Exception:
        pass

    text = str(value).strip().replace(" ", "")
    text = re.sub(r"\.0$", "", text)
    digits = re.sub(r"\D", "", text)

    if not digits or len(digits) != 6:
        return None

    return digits


def is_valid_zuj(value: Any) -> bool:
    """Vrátí True, pokud hodnota vypadá jako šestimístný kód obce."""
    code = clean_municipality_code(value)
    return bool(code and re.fullmatch(r"\d{6}", code))


def filter_valid_for_year(
    df: pd.DataFrame,
    year: int,
    start_candidates: list[str],
    end_candidates: list[str],
) -> pd.DataFrame:
    """
    Vybere řádky platné pro daný rok podle sloupců typu PLATIOD/PLATIDO.

    Pokud sloupce platnosti nejsou dostupné, vrátí data beze změny.
    """
    start_col = guess_col(df, start_candidates)
    end_col = guess_col(df, end_candidates)

    if not start_col and not end_col:
        return df.copy()

    out = df.copy()
    mask = pd.Series(True, index=out.index)

    if start_col:
        start = pd.to_numeric(out[start_col], errors="coerce")
        mask &= start.isna() | (start <= int(year))

    if end_col:
        end = pd.to_numeric(out[end_col], errors="coerce")
        mask &= end.isna() | (end >= int(year))

    return out.loc[mask].copy()


def size_category(population: Any) -> str | None:
    """Vrátí velikostní kategorii obce podle počtu obyvatel."""
    pop = pd.to_numeric(population, errors="coerce")

    if pd.isna(pop):
        return None

    pop = int(pop)

    if pop <= 750:
        return "0–750"
    if pop <= 1999:
        return "751–1999"
    if pop <= 4999:
        return "2000–4999"
    if pop <= 14999:
        return "5000–14999"
    if pop <= 39999:
        return "15000–39999"
    if pop <= 99999:
        return "40000–99999"

    return "100000+"


def score_0_100(series: pd.Series, direction: str = "UP") -> pd.Series:
    """
    Převede číselnou řadu na skóre 0–100 s ořezem p05/p95.

    direction:
    - UP: vyšší hodnota je lepší
    - DOWN: nižší hodnota je lepší
    """
    x = pd.to_numeric(series, errors="coerce")
    valid = x.dropna()

    if valid.empty:
        return pd.Series(np.nan, index=series.index)

    p05 = valid.quantile(0.05)
    p95 = valid.quantile(0.95)

    if pd.isna(p05) or pd.isna(p95) or p05 == p95:
        return pd.Series(np.nan, index=series.index)

    clipped = x.clip(lower=p05, upper=p95)
    score = 100 * (clipped - p05) / (p95 - p05)

    if str(direction).upper() == "DOWN":
        score = 100 - score

    return score.clip(lower=0, upper=100).round(2)


# =============================================================================
# AUTODETEKCE MOS UKAZATELŮ
# =============================================================================

MOS_AUTODETECT_PATTERNS: dict[str, dict[str, list[str]]] = {
    "population": {
        "patterns": ["počet obyvatel", "pocet obyvatel", "stav obyvatel"],
        "exclude": ["hustota", "index", "podíl", "podil"],
    },
    "migration_balance_per_1000": {
        "patterns": [
            "migrační saldo",
            "migracni saldo",
            "saldo migrace",
            "přírůstek stěhováním",
            "prirustek stehovanim",
        ],
        "exclude": ["index"],
    },
    "natural_increase": {
        "patterns": [
            "přirozený přírůstek",
            "prirozeny prirustek",
            "přirozený úbytek",
            "prirozeny ubytek",
        ],
        "exclude": ["index"],
    },
    "unemployment_rate": {
        "patterns": [
            "podíl nezaměstnaných osob",
            "podil nezamestnanych osob",
            "míra nezaměstnanosti",
            "mira nezamestnanosti",
        ],
        "exclude": [],
    },
    "completed_flats_per_1000": {
        "patterns": ["dokončené byty", "dokoncene byty"],
        "exclude": ["zahájené", "zahajene"],
    },
    "ecological_stability_coef": {
        "patterns": [
            "koeficient ekologické stability",
            "koeficient ekologicke stability",
        ],
        "exclude": [],
    },
}


def suggest_mos_indicator_code(
    ukazatele: pd.DataFrame,
    patterns: list[str],
    exclude_patterns: list[str] | None = None,
) -> str | None:
    """
    Najde pravděpodobný KODUKAZ v MOS_UKAZ podle textových vzorů.

    Výsledek je potřeba po prvním běhu zkontrolovat a ideálně zapsat napevno
    do config/indicator_catalog.csv.
    """
    code_col = guess_col(
        ukazatele,
        ["kodukaz", "kod_ukaz", "kod ukazatele", "kod", "ukazatel_kod"],
        required=True,
    )
    name_col = guess_col(
        ukazatele,
        ["nazev", "název", "nazev_ukazatele", "ukazatel", "popis"],
        required=True,
    )

    text = ukazatele[name_col].astype(str).map(normalize_text)
    mask = pd.Series(False, index=ukazatele.index)

    for pattern in patterns:
        mask |= text.str.contains(normalize_text(pattern), regex=False, na=False)

    if exclude_patterns:
        for pattern in exclude_patterns:
            mask &= ~text.str.contains(normalize_text(pattern), regex=False, na=False)

    candidates = ukazatele.loc[mask].copy()

    if candidates.empty:
        return None

    # Kratší název často znamená obecnější ukazatel, ne detailní odvozeninu.
    candidates["_name_len"] = candidates[name_col].astype(str).str.len()
    best = candidates.sort_values("_name_len").iloc[0]

    return str(best[code_col]).replace(".0", "").strip()


# =============================================================================
# config
# =============================================================================

def create_default_indicator_catalog(
    path: str | Path = CONFIG_DIR / "indicator_catalog.csv",
) -> pd.DataFrame:
    """
    Vytvoří základní indicator_catalog.csv, pokud ještě neexistuje.

    Sloupec source_key může být ze začátku prázdný.
    build_indicators() se potom pokusí KODUKAZ autodetekovat z MOS_UKAZ.
    """
    ensure_dirs()
    path = Path(path)

    if path.exists():
        print(f"[INFO] indicator_catalog.csv už existuje: {path}")
        return read_csv_smart(path)

    catalog = pd.DataFrame(
        [
            {
                "indicator_id": "population",
                "name": "Počet obyvatel",
                "dimension": "context",
                "source": "CSU_MOS",
                "source_key": "",
                "year": 2024,
                "unit": "obyv.",
                "direction": "UP",
                "role": "context",
                "influence_level": "low",
                "transform": "none",
                "selected_for_mvp": 1,
                "notes": "Kontextový ukazatel.",
            },
            {
                "indicator_id": "migration_balance_per_1000",
                "name": "Migrační saldo na 1000 obyvatel",
                "dimension": "demography",
                "source": "CSU_MOS",
                "source_key": "",
                "year": 2024,
                "unit": "na 1000 obyv.",
                "direction": "UP",
                "role": "context",
                "influence_level": "low",
                "transform": "per_1000",
                "selected_for_mvp": 1,
                "notes": "Kontextový ukazatel.",
            },
            {
                "indicator_id": "natural_increase",
                "name": "Přirozený přírůstek / úbytek",
                "dimension": "demography",
                "source": "CSU_MOS",
                "source_key": "",
                "year": 2024,
                "unit": "osoby",
                "direction": "UP",
                "role": "context",
                "influence_level": "low",
                "transform": "none",
                "selected_for_mvp": 1,
                "notes": "Kontextový ukazatel.",
            },
            {
                "indicator_id": "unemployment_rate",
                "name": "Podíl nezaměstnaných osob",
                "dimension": "labour",
                "source": "CSU_MOS",
                "source_key": "",
                "year": 2024,
                "unit": "%",
                "direction": "DOWN",
                "role": "score",
                "influence_level": "low",
                "transform": "none",
                "selected_for_mvp": 1,
                "notes": "Nižší hodnota = lepší skóre.",
            },
            {
                "indicator_id": "completed_flats_per_1000",
                "name": "Dokončené byty na 1000 obyvatel",
                "dimension": "housing",
                "source": "CSU_MOS",
                "source_key": "",
                "year": 2024,
                "unit": "byty / 1000 obyv.",
                "direction": "UP",
                "role": "score",
                "influence_level": "medium",
                "transform": "per_1000",
                "selected_for_mvp": 1,
                "notes": "Skórovaný indikátor.",
            },
            {
                "indicator_id": "ecological_stability_coef",
                "name": "Koeficient ekologické stability",
                "dimension": "environment",
                "source": "CSU_MOS",
                "source_key": "",
                "year": 2024,
                "unit": "koeficient",
                "direction": "UP",
                "role": "score",
                "influence_level": "low",
                "transform": "none",
                "selected_for_mvp": 1,
                "notes": "Skórovaný / spíše kontextový environmentální ukazatel.",
            },
        ]
    )

    catalog.to_csv(path, index=False, encoding="utf-8-sig")
    print(f"[OK] Vytvořen výchozí indicator_catalog.csv: {path}")

    return catalog


# =============================================================================
# geo
# =============================================================================

def extract_population_from_mos(
    mos_data_path: str | Path,
    mos_ukazatele_path: str | Path,
) -> pd.DataFrame:
    """
    Najde v MOS ukazatel počtu obyvatel a vrátí population podle obce.
    """
    data = read_csv_smart(mos_data_path)
    ukaz = read_csv_smart(mos_ukazatele_path)

    data_code_col = guess_col(
        data,
        ["koduzemi", "kod_uzemi", "kód území", "kod obce", "kod_obce", "zuj"],
        required=True,
    )
    data_ind_col = guess_col(
        data,
        ["kodukaz", "kod_ukaz", "kod ukazatele", "ukazatel_kod"],
        required=True,
    )
    data_val_col = guess_col(data, ["hodnota", "value", "data"], required=True)

    ukaz_code_col = guess_col(
        ukaz,
        ["kodukaz", "kod_ukaz", "kod ukazatele", "kod", "ukazatel_kod"],
        required=True,
    )
    ukaz_name_col = guess_col(
        ukaz,
        ["nazev", "název", "nazev_ukazatele", "ukazatel", "popis"],
        required=True,
    )

    autodetect = MOS_AUTODETECT_PATTERNS["population"]
    pop_indicator_code = suggest_mos_indicator_code(
        ukaz,
        patterns=autodetect["patterns"],
        exclude_patterns=autodetect["exclude"],
    )

    if not pop_indicator_code:
        raise ValueError("V číselníku ukazatelů nebyl nalezen kandidát na počet obyvatel.")

    candidates = ukaz[
        ukaz[ukaz_code_col]
        .astype(str)
        .str.replace(r"\.0$", "", regex=True)
        .str.strip()
        .eq(pop_indicator_code)
    ].copy()

    if not candidates.empty:
        print(
            f"[INFO] Populační ukazatel MOS detekován jako "
            f"{pop_indicator_code}: {candidates.iloc[0][ukaz_name_col]}"
        )
    else:
        print(f"[INFO] Populační ukazatel MOS detekován jako {pop_indicator_code}")

    data_ind = (
        data[data_ind_col]
        .astype(str)
        .str.replace(r"\.0$", "", regex=True)
        .str.strip()
    )

    pop_rows = data[data_ind.eq(pop_indicator_code)].copy()

    out = pd.DataFrame()
    out["kod_obce"] = pop_rows[data_code_col].map(clean_municipality_code)
    out["population"] = pd.to_numeric(pop_rows[data_val_col], errors="coerce")

    out = out.dropna(subset=["kod_obce"]).drop_duplicates("kod_obce")
    return out[["kod_obce", "population"]]


def prepare_geo_master(
    mos_uzemi_path: str | Path = RAW_DIR / "csu_mos_uzemi.csv",
    mos_data_path: str | Path = RAW_DIR / "csu_mos_data_latest.csv",
    mos_ukazatele_path: str | Path = RAW_DIR / "csu_mos_ukazatele.csv",
    output_path: str | Path = PROCESSED_DIR / "geo_master.csv",
    target_year: int = 2024,
) -> pd.DataFrame:
    """
    Vytvoří referenční seznam obcí.

    Výstupem je geo_master.csv, páteř celého projektu.
    """
    ensure_dirs()

    uzemi = read_csv_smart(mos_uzemi_path)

    uzemi = filter_valid_for_year(
        uzemi,
        target_year,
        start_candidates=["platiod", "platí od", "plati od", "platnost_od"],
        end_candidates=["platido", "platí do", "plati do", "platnost_do"],
    )

    code_col = guess_col(
        uzemi,
        ["koduzemi", "kod_uzemi", "kód území", "kod obce", "kod_obce", "zuj"],
        required=True,
    )
    name_col = guess_col(
        uzemi,
        ["nazev", "název", "obec", "nazev_obce", "název obce"],
        required=True,
    )

    okres_col = guess_col(uzemi, ["okres", "nazev_okres", "okres_nazev"])
    orp_col = guess_col(uzemi, ["orp", "soorp", "so_orp", "spravni_obvod_orp"])
    kraj_col = guess_col(uzemi, ["kraj", "nazev_kraj", "kraj_nazev"])

    geo = pd.DataFrame()
    geo["kod_obce"] = uzemi[code_col].map(clean_municipality_code)
    geo["obec"] = uzemi[name_col].astype(str).str.strip()

    geo["okres"] = uzemi[okres_col] if okres_col else None
    geo["orp"] = uzemi[orp_col] if orp_col else None
    geo["kraj"] = uzemi[kraj_col] if kraj_col else None

    geo = geo[geo["kod_obce"].map(is_valid_zuj)].drop_duplicates("kod_obce").copy()

    try:
        pop = extract_population_from_mos(
            mos_data_path=mos_data_path,
            mos_ukazatele_path=mos_ukazatele_path,
        )
        geo = geo.merge(pop, on="kod_obce", how="left")
        geo["size_category"] = geo["population"].map(size_category)
    except Exception as exc:
        print(f"[WARN] Populaci se nepodařilo doplnit automaticky: {exc}")
        geo["population"] = np.nan
        geo["size_category"] = None

    geo = geo.sort_values(["kraj", "okres", "obec"], na_position="last")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    geo.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"[OK] geo_master uložen: {output_path} ({len(geo)} obcí)")
    return geo


# =============================================================================
# indicators
# =============================================================================

def build_indicators(
    geo_master_path: str | Path = PROCESSED_DIR / "geo_master.csv",
    mos_data_path: str | Path = RAW_DIR / "csu_mos_data_latest.csv",
    indicator_catalog_path: str | Path = CONFIG_DIR / "indicator_catalog.csv",
    output_path: str | Path = PROCESSED_DIR / "municipality_indicators_raw.csv",
    mos_ukazatele_path: str | Path = RAW_DIR / "csu_mos_ukazatele.csv",
) -> pd.DataFrame:
    """
    Vytvoří širokou tabulku indikátorů podle CONFIG.

    Každý řádek = jedna obec.
    Každý sloupec = jeden indikátor.
    """
    ensure_dirs()

    geo = read_csv_smart(geo_master_path)
    geo["kod_obce"] = geo["kod_obce"].map(clean_municipality_code)
    geo = geo.dropna(subset=["kod_obce"]).copy()

    if not Path(indicator_catalog_path).exists():
        create_default_indicator_catalog(indicator_catalog_path)

    config = read_csv_smart(indicator_catalog_path)
    mos = read_csv_smart(mos_data_path)
    ukazatele = read_csv_smart(mos_ukazatele_path) if Path(mos_ukazatele_path).exists() else pd.DataFrame()

    mos_code_col = guess_col(
        mos,
        ["koduzemi", "kod_uzemi", "kód území", "kod obce", "kod_obce", "zuj"],
        required=True,
    )
    mos_ind_col = guess_col(
        mos,
        ["kodukaz", "kod_ukaz", "kod ukazatele", "ukazatel_kod"],
        required=True,
    )
    mos_val_col = guess_col(mos, ["hodnota", "value", "data"], required=True)

    mos = mos.copy()
    mos["_kod_obce"] = mos[mos_code_col].map(clean_municipality_code)
    mos["_indicator_code"] = (
        mos[mos_ind_col]
        .astype(str)
        .str.replace(r"\.0$", "", regex=True)
        .str.strip()
    )
    mos["_value"] = pd.to_numeric(mos[mos_val_col], errors="coerce")

    keep_cols = [
        "kod_obce",
        "obec",
        "okres",
        "orp",
        "kraj",
        "population",
        "size_category",
    ]
    keep_cols = [c for c in keep_cols if c in geo.columns]
    out = geo[keep_cols].copy()

    for _, row in config.iterrows():
        if int(row.get("selected_for_mvp", 1)) != 1:
            continue

        if str(row.get("source", "")).upper() != "CSU_MOS":
            continue

        indicator_id = str(row["indicator_id"])
        raw_source_key = row.get("source_key", "")

        if pd.isna(raw_source_key):
            source_key = ""
        else:
            source_key = str(raw_source_key).strip().replace(".0", "")

        if source_key.lower() in ["nan", "none", "null"]:
            source_key = ""
        transform = str(row.get("transform", "none")).lower()

        if not source_key:
            auto = MOS_AUTODETECT_PATTERNS.get(indicator_id)
            if auto and not ukazatele.empty:
                source_key = suggest_mos_indicator_code(
                    ukazatele,
                    patterns=auto["patterns"],
                    exclude_patterns=auto.get("exclude", []),
                ) or ""

                if source_key:
                    print(
                        f"[INFO] {indicator_id}: source_key autodetekován jako {source_key}. "
                        f"Zkontrolujte a zapište do CONFIG."
                    )

        if not source_key:
            print(
                f"[WARN] {indicator_id}: chybí source_key v CONFIG "
                f"a autodetekce selhala, indikátor se přeskočí."
            )
            out[indicator_id] = np.nan
            continue

        selected = mos[mos["_indicator_code"].eq(source_key)][["_kod_obce", "_value"]].copy()
        selected = selected.dropna(subset=["_kod_obce"]).drop_duplicates("_kod_obce")
        selected = selected.rename(
            columns={
                "_kod_obce": "kod_obce",
                "_value": f"_{indicator_id}_raw",
            }
        )

        out = out.merge(selected, on="kod_obce", how="left")

        raw_col = f"_{indicator_id}_raw"

        if transform == "per_1000":
            out[indicator_id] = out[raw_col] / out["population"] * 1000
        elif transform == "per_capita":
            out[indicator_id] = out[raw_col] / out["population"]
        else:
            out[indicator_id] = out[raw_col]

        out = out.drop(columns=[raw_col])

        non_null = int(out[indicator_id].notna().sum())
        print(
            f"[OK] Indikátor {indicator_id} vytvořen ze source_key={source_key}; "
            f"nenulových hodnot: {non_null}"
        )

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"[OK] Indikátorová tabulka uložena: {output_path}")
    return out


# =============================================================================
# score
# =============================================================================

def score_indicators(
    indicators_path: str | Path = PROCESSED_DIR / "municipality_indicators_raw.csv",
    indicator_catalog_path: str | Path = CONFIG_DIR / "indicator_catalog.csv",
    scores_output_path: str | Path = PROCESSED_DIR / "municipality_scores.csv",
    dimension_output_path: str | Path = PROCESSED_DIR / "dimension_scores.csv",
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Spočítá skóre indikátorů a skóre dimenzí.
    """
    ensure_dirs()

    df = read_csv_smart(indicators_path)
    config = read_csv_smart(indicator_catalog_path)

    if "kod_obce" in df.columns:
        df["kod_obce"] = df["kod_obce"].map(clean_municipality_code)
        df = df.dropna(subset=["kod_obce"]).copy()

    id_cols = [
        c for c in [
            "kod_obce",
            "obec",
            "okres",
            "orp",
            "kraj",
            "population",
            "size_category",
        ]
        if c in df.columns
    ]

    scores = df[id_cols].copy()
    score_columns_by_dimension: dict[str, list[str]] = {}

    for _, row in config.iterrows():
        if int(row.get("selected_for_mvp", 1)) != 1:
            continue

        if str(row.get("role", "score")).lower() != "score":
            continue

        indicator_id = str(row["indicator_id"])

        if indicator_id not in df.columns:
            print(f"[WARN] {indicator_id}: není v datech, skóre se nepočítá.")
            continue

        direction = str(row.get("direction", "UP")).upper()
        dimension = str(row.get("dimension", "other"))
        score_col = f"{indicator_id}_score"

        scores[score_col] = score_0_100(df[indicator_id], direction=direction)
        score_columns_by_dimension.setdefault(dimension, []).append(score_col)

        print(f"[OK] Skóre {score_col} spočítáno, direction={direction}")

    dimensions = scores[id_cols].copy()

    for dimension, cols in score_columns_by_dimension.items():
        dimensions[f"{dimension}_score"] = scores[cols].mean(axis=1, skipna=True).round(2)

    scores_output_path = Path(scores_output_path)
    dimension_output_path = Path(dimension_output_path)

    scores.to_csv(scores_output_path, index=False, encoding="utf-8-sig")
    dimensions.to_csv(dimension_output_path, index=False, encoding="utf-8-sig")

    print(f"[OK] Indikátorová skóre uložena: {scores_output_path}")
    print(f"[OK] Dimenzionální skóre uloženo: {dimension_output_path}")

    return scores, dimensions


# =============================================================================
# case
# =============================================================================

def build_case_study(
    municipality_code: str = "540480",
    municipality_name: str = "Moravičany",
    dimension_scores_path: str | Path = PROCESSED_DIR / "dimension_scores.csv",
    raw_indicators_path: str | Path = PROCESSED_DIR / "municipality_indicators_raw.csv",
    output_csv: str | Path = OUTPUTS_DIR / "moravicany_profile.csv",
    output_md: str | Path = OUTPUTS_DIR / "case_study_moravicany.md",
) -> pd.DataFrame:
    """
    Vytvoří krátký profil obce a porovnání s podobně velkými obcemi.
    """
    ensure_dirs()

    code = clean_municipality_code(municipality_code)

    dims = read_csv_smart(dimension_scores_path)
    raw = read_csv_smart(raw_indicators_path)

    dims["kod_obce"] = dims["kod_obce"].map(clean_municipality_code)
    raw["kod_obce"] = raw["kod_obce"].map(clean_municipality_code)

    dims = dims.dropna(subset=["kod_obce"]).copy()
    raw = raw.dropna(subset=["kod_obce"]).copy()

    row_dims = dims[dims["kod_obce"].eq(code)].copy()
    row_raw = raw[raw["kod_obce"].eq(code)].copy()

    if row_dims.empty:
        raise ValueError(f"Obec {municipality_name} / {code} není v dimension_scores.csv.")

    profile = row_dims.merge(
        row_raw,
        on=["kod_obce", "obec"],
        how="left",
        suffixes=("", "_raw"),
    )

    size_cat = profile.iloc[0].get("size_category")

    if "size_category" in dims.columns:
        benchmark = dims[dims["size_category"].eq(size_cat)].copy()
    else:
        benchmark = pd.DataFrame()

    score_cols = [c for c in dims.columns if c.endswith("_score")]

    rows = []
    for col in score_cols:
        value = pd.to_numeric(profile.iloc[0].get(col), errors="coerce")

        if not benchmark.empty:
            median_similar = pd.to_numeric(benchmark[col], errors="coerce").median()
        else:
            median_similar = np.nan

        rows.append(
            {
                "dimension": col,
                "municipality_score": round(value, 2) if pd.notna(value) else np.nan,
                "median_similar_size": round(median_similar, 2) if pd.notna(median_similar) else np.nan,
                "difference": round(value - median_similar, 2)
                if pd.notna(value) and pd.notna(median_similar)
                else np.nan,
            }
        )

    out = pd.DataFrame(rows)

    output_csv = Path(output_csv)
    output_md = Path(output_md)
    output_csv.parent.mkdir(parents=True, exist_ok=True)

    out.to_csv(output_csv, index=False, encoding="utf-8-sig")

    md = []
    md.append(f"# Případová studie: {municipality_name}\n")
    md.append(f"Kód obce / ZÚJ: `{code}`\n")
    md.append(f"Velikostní kategorie: `{size_cat}`\n")
    md.append("## Skóre dimenzí\n")
    md.append(out.to_markdown(index=False))
    md.append("\n## Interpretace\n")
    md.append(
        "Tabulka ukazuje skóre obce v jednotlivých dimenzích a srovnání s mediánem "
        "obcí ve stejné velikostní kategorii. Kladný rozdíl znamená, že obec je "
        "nad mediánem podobně velkých obcí.\n"
    )

    output_md.write_text("\n".join(md), encoding="utf-8")

    print(f"[OK] Profil obce uložen: {output_csv}")
    print(f"[OK] Markdown případová studie uložena: {output_md}")

    return out


# =============================================================================
# map
# =============================================================================

def build_map(
    geojson_path: str | Path = GEO_DIR / "municipalities.geojson",
    dimension_scores_path: str | Path = PROCESSED_DIR / "dimension_scores.csv",
    output_html: str | Path = OUTPUTS_DIR / "interactive_map.html",
    dimension_column: str | None = None,
) -> None:
    """
    Vytvoří jednoduchou HTML mapu pomocí folium.

    Vyžaduje GeoJSON obcí v data/geo/municipalities.geojson.
    """
    ensure_dirs()

    try:
        import geopandas as gpd
        import folium
    except ImportError as exc:
        raise ImportError("Pro mapu je potřeba nainstalovat geopandas a folium.") from exc

    geojson_path = Path(geojson_path)

    if not geojson_path.exists():
        raise FileNotFoundError(
            f"Chybí geodata: {geojson_path}. "
            f"Uložte GeoJSON obcí do data/geo/municipalities.geojson."
        )

    gdf = gpd.read_file(geojson_path)
    scores = read_csv_smart(dimension_scores_path)

    geo_code_col = guess_col(
        gdf,
        ["kod_obce", "koduzemi", "kod_uzemi", "zuj", "KOD_OBCE"],
        required=True,
    )

    gdf["kod_obce"] = gdf[geo_code_col].map(clean_municipality_code)
    scores["kod_obce"] = scores["kod_obce"].map(clean_municipality_code)

    gdf = gdf.dropna(subset=["kod_obce"]).copy()
    scores = scores.dropna(subset=["kod_obce"]).copy()

    score_cols = [c for c in scores.columns if c.endswith("_score")]

    if not score_cols:
        raise ValueError(f"V {dimension_scores_path} nejsou žádné sloupce *_score.")

    if dimension_column is None:
        dimension_column = score_cols[0]

    if dimension_column not in scores.columns:
        raise ValueError(
            f"Sloupec {dimension_column} není v datech. "
            f"Dostupné score sloupce: {score_cols}"
        )

    merged = gdf.merge(scores, on="kod_obce", how="left")

    try:
        merged["geometry"] = merged["geometry"].simplify(0.001, preserve_topology=True)
    except Exception:
        pass

    try:
        center = merged.geometry.union_all().centroid
    except Exception:
        center = merged.geometry.unary_union.centroid

    m = folium.Map(location=[center.y, center.x], zoom_start=7, tiles="cartodbpositron")

    tooltip_fields = [
        c for c in ["obec", "kod_obce", dimension_column, "population", "size_category"]
        if c in merged.columns
    ]

    folium.Choropleth(
        geo_data=merged,
        data=merged,
        columns=["kod_obce", dimension_column],
        key_on="feature.properties.kod_obce",
        fill_opacity=0.75,
        line_opacity=0.1,
        legend_name=f"{dimension_column} (0–100)",
    ).add_to(m)

    folium.GeoJson(
        merged,
        name="Obce",
        tooltip=folium.GeoJsonTooltip(fields=tooltip_fields, aliases=tooltip_fields),
        style_function=lambda feature: {
            "fillOpacity": 0,
            "color": "#333333",
            "weight": 0.2,
        },
    ).add_to(m)

    output_html = Path(output_html)
    output_html.parent.mkdir(parents=True, exist_ok=True)
    m.save(output_html)

    print(f"[OK] Mapa uložena: {output_html}")


# =============================================================================
# CLI
# =============================================================================

def main() -> None:
    parser = argparse.ArgumentParser(description="MVP pipeline pro datovou mapu obcí.")
    parser.add_argument(
        "step",
        choices=["config", "geo", "indicators", "score", "map", "case"],
        help="Který krok pipeline spustit.",
    )
    parser.add_argument(
        "--dimension",
        default=None,
        help="Sloupec dimenze pro mapu, např. housing_score.",
    )
    parser.add_argument(
        "--year",
        type=int,
        default=2024,
        help="Rok pro filtrování platnosti území v MOS_UZEMI.",
    )

    args = parser.parse_args()

    if args.step == "config":
        create_default_indicator_catalog()

    elif args.step == "geo":
        prepare_geo_master(target_year=args.year)

    elif args.step == "indicators":
        build_indicators()

    elif args.step == "score":
        score_indicators()

    elif args.step == "map":
        build_map(dimension_column=args.dimension)

    elif args.step == "case":
        build_case_study()


if __name__ == "__main__":
    main()