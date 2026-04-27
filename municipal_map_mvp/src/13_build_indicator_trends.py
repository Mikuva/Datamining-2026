#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
13_build_indicator_trends.py

Vytvoří trendové hodnoty indikátorů za roky 2020–2024.

Smysl:
- aktuální skóre za jeden rok je jen "fotka",
- trend 2020–2024 ukazuje, jestli se obec zlepšuje, zhoršuje nebo má výkyv,
- u malých obcí pomáhá odlišit strukturální problém od jednorázové události.

Důležité k interpretaci:
- "Meziroční změna" = hodnota 2024 minus hodnota 2023.
- "Změna za 5 let" = hodnota 2024 minus hodnota 2020.
- U procentních ukazatelů jde o změnu v procentních bodech, ne o procentní růst.
- U ukazatelů na 1000 obyvatel jde o rozdíl hodnoty v dané jednotce.

Vstupy:
    data/raw/csu_mos_data_2020.csv
    data/raw/csu_mos_data_2021.csv
    data/raw/csu_mos_data_2022.csv
    data/raw/csu_mos_data_2023.csv
    data/raw/csu_mos_data_2024.csv
    data/processed/geo_master.csv
    config/indicator_catalog.csv

Výstupy:
    data/processed/municipality_indicators_timeseries.csv
    data/processed/municipality_indicators_trends_wide.csv
    outputs/trend_profile_<kod_obce>.md

Spuštění:
    python municipal_map_mvp/src/13_build_indicator_trends.py

Volitelně pro konkrétní obec:
    python municipal_map_mvp/src/13_build_indicator_trends.py --kod-obce 540480
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


# =============================================================================
# CESTY
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
CONFIG_DIR = PROJECT_ROOT / "config"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

GEO_MASTER_PATH = PROCESSED_DIR / "geo_master.csv"
CONFIG_PATH = CONFIG_DIR / "indicator_catalog.csv"

TIMESERIES_OUT = PROCESSED_DIR / "municipality_indicators_timeseries.csv"
TRENDS_WIDE_OUT = PROCESSED_DIR / "municipality_indicators_trends_wide.csv"


# =============================================================================
# NASTAVENÍ
# =============================================================================

YEARS = [2020, 2021, 2022, 2023, 2024]
BASE_YEAR = 2020
PREVIOUS_YEAR = 2023
CURRENT_YEAR = 2024

# Ukazatele, které chceme sledovat v čase.
# source_key bereme z config/indicator_catalog.csv.
TREND_INDICATORS = [
    "population",
    "migration_balance_per_1000",
    "natural_increase",
    "unemployment_rate",
    "completed_flats_per_1000",
    "ecological_stability_coef",
    "average_age",
]

INDICATOR_LABELS = {
    "population": "Počet obyvatel",
    "migration_balance_per_1000": "Migrační saldo / 1000 obyvatel",
    "natural_increase": "Přirozený přírůstek / úbytek",
    "unemployment_rate": "Podíl nezaměstnaných osob",
    "completed_flats_per_1000": "Dokončené byty / 1000 obyvatel",
    "completed_flats_estimated": "Odhad dokončených bytů celkem",
    "ecological_stability_coef": "Koeficient ekologické stability",
    "average_age": "Průměrný věk obyvatel",
}

# Směr se používá pro jednoduché vyhodnocení trendu.
# UP = vyšší hodnota je příznivější.
# DOWN = nižší hodnota je příznivější.
DIRECTION = {
    "population": "UP",
    "migration_balance_per_1000": "UP",
    "natural_increase": "UP",
    "unemployment_rate": "DOWN",
    "completed_flats_per_1000": "UP",
    "completed_flats_estimated": "UP",
    "ecological_stability_coef": "UP",
    "average_age": "DOWN",
}


# =============================================================================
# POMOCNÉ FUNKCE
# =============================================================================

def clean_code(value) -> str:
    """Vyčistí kód obce do textové podoby bez .0."""
    if pd.isna(value):
        return ""
    return str(value).strip().replace(".0", "")


def read_csv_smart(path: Path, **kwargs) -> pd.DataFrame:
    """Načte CSV s tolerancí na české kódování."""
    last_error = None

    for enc in ["utf-8-sig", "utf-8", "cp1250", "windows-1250", "latin-1"]:
        try:
            return pd.read_csv(path, encoding=enc, **kwargs)
        except Exception as exc:
            last_error = exc

    raise RuntimeError(f"Nepodařilo se načíst {path}: {last_error}")


def fmt(value, digits: int = 2, suffix: str = "") -> str:
    """Bezpečné formátování hodnot pro markdown."""
    if pd.isna(value):
        return "bez dat"

    try:
        value = float(value)
    except Exception:
        return str(value)

    if digits == 0:
        return f"{value:.0f}{suffix}"

    return f"{value:.{digits}f}{suffix}"


def load_config() -> pd.DataFrame:
    """Načte katalog indikátorů a vrátí jen indikátory určené pro trend."""
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Chybí config: {CONFIG_PATH}")

    cfg = read_csv_smart(CONFIG_PATH, dtype=str)
    cfg.columns = [c.strip() for c in cfg.columns]

    if "indicator_id" not in cfg.columns:
        raise ValueError("V indicator_catalog.csv chybí sloupec indicator_id.")

    if "source_key" not in cfg.columns:
        raise ValueError("V indicator_catalog.csv chybí sloupec source_key.")

    cfg = cfg[cfg["indicator_id"].astype(str).isin(TREND_INDICATORS)].copy()

    cfg["indicator_id"] = cfg["indicator_id"].astype(str).str.strip()
    cfg["source_key"] = (
        cfg["source_key"]
        .astype(str)
        .str.strip()
        .str.replace(".0", "", regex=False)
    )

    if "transform" not in cfg.columns:
        cfg["transform"] = "none"

    if "direction" not in cfg.columns:
        cfg["direction"] = cfg["indicator_id"].map(DIRECTION).fillna("UP")

    return cfg


def load_geo_master() -> pd.DataFrame:
    """Načte základní tabulku obcí."""
    if not GEO_MASTER_PATH.exists():
        raise FileNotFoundError(
            f"Chybí {GEO_MASTER_PATH}. Nejdřív spusť geo krok pipeline."
        )

    geo = read_csv_smart(GEO_MASTER_PATH, dtype=str)
    geo.columns = [c.strip() for c in geo.columns]

    if "kod_obce" not in geo.columns:
        raise ValueError("V geo_master.csv chybí sloupec kod_obce.")

    geo["kod_obce"] = geo["kod_obce"].map(clean_code)

    keep_cols = [
        "kod_obce",
        "obec",
        "okres",
        "orp",
        "kraj",
        "population",
        "size_category",
    ]

    return geo[[c for c in keep_cols if c in geo.columns]].copy()


def load_mos_year(year: int) -> pd.DataFrame | None:
    """Načte roční MOS data, pokud existují."""
    path = RAW_DIR / f"csu_mos_data_{year}.csv"

    if not path.exists():
        print(f"[WARN] Chybí soubor pro rok {year}: {path}")
        return None

    print(f"[INFO] Načítám MOS data {year}: {path.name}")

    df = read_csv_smart(path, dtype=str)
    df.columns = [c.strip().lower() for c in df.columns]

    required = {"rok", "kodukaz", "koduzemi", "hodnota"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(
            f"V {path.name} chybí sloupce {missing}. "
            f"Dostupné sloupce: {list(df.columns)}"
        )

    df["rok"] = pd.to_numeric(df["rok"], errors="coerce").astype("Int64")
    df["kodukaz"] = (
        df["kodukaz"]
        .astype(str)
        .str.strip()
        .str.replace(".0", "", regex=False)
    )
    df["kod_obce"] = df["koduzemi"].map(clean_code)
    df["hodnota"] = pd.to_numeric(df["hodnota"], errors="coerce")

    return df[["rok", "kodukaz", "kod_obce", "hodnota"]].copy()


def extract_indicator_for_year(
    mos: pd.DataFrame,
    indicator_id: str,
    source_key: str,
    year: int,
) -> pd.DataFrame:
    """Vybere jednu hodnotu indikátoru z MOS dat pro daný rok."""
    subset = mos[
        mos["kodukaz"].astype(str).str.strip().eq(str(source_key).strip())
    ].copy()

    subset = subset[["kod_obce", "hodnota"]].rename(columns={"hodnota": "value"})
    subset["indicator_id"] = indicator_id
    subset["year"] = year

    return subset[["kod_obce", "indicator_id", "year", "value"]]


# =============================================================================
# TVORBA ČASOVÉ ŘADY
# =============================================================================

def build_raw_timeseries(cfg: pd.DataFrame) -> pd.DataFrame:
    """Vytvoří long timeseries tabulku indikátorů."""
    frames: list[pd.DataFrame] = []

    for year in YEARS:
        mos = load_mos_year(year)

        if mos is None:
            continue

        for _, row in cfg.iterrows():
            indicator_id = str(row["indicator_id"]).strip()
            source_key = str(row["source_key"]).strip()

            if not source_key or source_key.lower() in ["nan", "none", "null"]:
                print(f"[WARN] {indicator_id}: chybí source_key, přeskočeno.")
                continue

            extracted = extract_indicator_for_year(
                mos=mos,
                indicator_id=indicator_id,
                source_key=source_key,
                year=year,
            )

            non_null = extracted["value"].notna().sum()
            print(f"[OK] {year} {indicator_id}: {non_null} hodnot")

            frames.append(extracted)

    if not frames:
        raise RuntimeError("Nepodařilo se vytvořit žádné časové řady.")

    return pd.concat(frames, ignore_index=True)


def attach_population_and_transforms(ts: pd.DataFrame) -> pd.DataFrame:
    """
    Dopočítá per_1000 transformace a odhad absolutního počtu dokončených bytů.

    Některé MOS ukazatele jsou absolutní počty.
    V configu máme například:
    - migration_balance_per_1000: zdroj je saldo migrace celkem, transform=per_1000
    - completed_flats_per_1000: zdroj je počet dokončených bytů, transform=per_1000

    Proto potřebujeme pro každý rok populaci.
    """
    cfg = load_config()

    pop = ts[ts["indicator_id"].eq("population")][
        ["kod_obce", "year", "value"]
    ].rename(columns={"value": "population_for_year"})

    ts = ts.merge(pop, on=["kod_obce", "year"], how="left")

    transform_map = dict(zip(cfg["indicator_id"], cfg["transform"].fillna("none")))

    transformed_values = []

    for _, row in ts.iterrows():
        indicator_id = row["indicator_id"]
        value = row["value"]
        population = row["population_for_year"]
        transform = str(transform_map.get(indicator_id, "none")).strip().lower()

        if transform == "per_1000":
            if pd.notna(value) and pd.notna(population) and float(population) != 0:
                transformed_values.append(float(value) / float(population) * 1000)
            else:
                transformed_values.append(pd.NA)
        else:
            transformed_values.append(value)

    ts["value"] = pd.to_numeric(transformed_values, errors="coerce")

    # Přidáme pomocný indikátor: odhad dokončených bytů celkem.
    # Ten se hodí v interpretaci, protože per_1000 může u malých obcí hodně kolísat.
    flats_source = ts[ts["indicator_id"].eq("completed_flats_per_1000")].copy()

    if not flats_source.empty:
        flats_total = flats_source.copy()
        flats_total["indicator_id"] = "completed_flats_estimated"

        flats_total["value"] = (
            pd.to_numeric(flats_total["value"], errors="coerce")
            * pd.to_numeric(flats_total["population_for_year"], errors="coerce")
            / 1000
        )

        ts = pd.concat([ts, flats_total], ignore_index=True)

    ts = ts.drop(columns=["population_for_year"], errors="ignore")

    return ts


def make_wide_trends(ts: pd.DataFrame, geo: pd.DataFrame) -> pd.DataFrame:
    """Převede long timeseries na wide tabulku s trendy."""
    pivot = ts.pivot_table(
        index="kod_obce",
        columns=["indicator_id", "year"],
        values="value",
        aggfunc="first",
    )

    pivot.columns = [
        f"{indicator}_{year}"
        for indicator, year in pivot.columns
    ]

    wide = pivot.reset_index()

    indicators = sorted(set(ts["indicator_id"].dropna().astype(str)))

    for indicator in indicators:
        c_base = f"{indicator}_{BASE_YEAR}"
        c_prev = f"{indicator}_{PREVIOUS_YEAR}"
        c_current = f"{indicator}_{CURRENT_YEAR}"

        if c_current in wide.columns and c_prev in wide.columns:
            wide[f"{indicator}_diff_{CURRENT_YEAR}_{PREVIOUS_YEAR}"] = (
                pd.to_numeric(wide[c_current], errors="coerce")
                - pd.to_numeric(wide[c_prev], errors="coerce")
            )

        if c_current in wide.columns and c_base in wide.columns:
            wide[f"{indicator}_diff_{CURRENT_YEAR}_{BASE_YEAR}"] = (
                pd.to_numeric(wide[c_current], errors="coerce")
                - pd.to_numeric(wide[c_base], errors="coerce")
            )

    # Zpětná kompatibilita se staršími názvy sloupců, pokud na ně naváže jiný skript.
    for indicator in indicators:
        new_prev = f"{indicator}_diff_{CURRENT_YEAR}_{PREVIOUS_YEAR}"
        new_base = f"{indicator}_diff_{CURRENT_YEAR}_{BASE_YEAR}"

        legacy_prev = f"{indicator}_change_24_23"
        legacy_base = f"{indicator}_change_24_20"

        if new_prev in wide.columns:
            wide[legacy_prev] = wide[new_prev]

        if new_base in wide.columns:
            wide[legacy_base] = wide[new_base]

    # Přidáme jednoduchý trend label za celé období.
    for indicator in indicators:
        diff_col = f"{indicator}_diff_{CURRENT_YEAR}_{BASE_YEAR}"
        label_col = f"{indicator}_trend_{BASE_YEAR}_{CURRENT_YEAR}"
        legacy_label_col = f"{indicator}_trend_20_24"

        if diff_col not in wide.columns:
            continue

        direction = DIRECTION.get(indicator, "UP")

        def trend_label(diff):
            if pd.isna(diff):
                return "bez dat"

            diff = float(diff)

            # Malé změny označíme jako stabilní.
            if abs(diff) < 0.01:
                return "stabilní"

            if direction == "DOWN":
                return "zlepšení" if diff < 0 else "zhoršení"

            return "zlepšení" if diff > 0 else "zhoršení"

        wide[label_col] = wide[diff_col].map(trend_label)

        # Zpětná kompatibilita.
        wide[legacy_label_col] = wide[label_col]

    geo = geo.copy()
    geo["kod_obce"] = geo["kod_obce"].map(clean_code)
    wide["kod_obce"] = wide["kod_obce"].map(clean_code)

    return geo.merge(wide, on="kod_obce", how="left")


# =============================================================================
# TRENDOVÝ PROFIL OBCE
# =============================================================================

def render_indicator_trend(row: pd.Series, indicator: str) -> str:
    """Vyrenderuje jeden řádek trendové markdown tabulky."""
    label = INDICATOR_LABELS.get(indicator, indicator)

    v20 = row.get(f"{indicator}_2020", pd.NA)
    v21 = row.get(f"{indicator}_2021", pd.NA)
    v22 = row.get(f"{indicator}_2022", pd.NA)
    v23 = row.get(f"{indicator}_2023", pd.NA)
    v24 = row.get(f"{indicator}_2024", pd.NA)

    diff_prev = row.get(f"{indicator}_diff_{CURRENT_YEAR}_{PREVIOUS_YEAR}", pd.NA)
    diff_base = row.get(f"{indicator}_diff_{CURRENT_YEAR}_{BASE_YEAR}", pd.NA)
    trend = row.get(f"{indicator}_trend_{BASE_YEAR}_{CURRENT_YEAR}", "bez dat")

    if indicator in ["population", "natural_increase", "completed_flats_estimated"]:
        digits = 0
    elif indicator == "ecological_stability_coef":
        digits = 4
    elif indicator == "average_age":
        digits = 1
    else:
        digits = 2

    suffix = " %" if indicator == "unemployment_rate" else ""

    return (
        f"| {label} | "
        f"{fmt(v20, digits, suffix)} | "
        f"{fmt(v21, digits, suffix)} | "
        f"{fmt(v22, digits, suffix)} | "
        f"{fmt(v23, digits, suffix)} | "
        f"{fmt(v24, digits, suffix)} | "
        f"{fmt(diff_prev, digits, suffix)} | "
        f"{fmt(diff_base, digits, suffix)} | "
        f"{trend} |"
    )


def create_trend_profile(wide: pd.DataFrame, kod_obce: str) -> Path:
    """Vytvoří markdown profil trendu pro konkrétní obec."""
    kod_obce = clean_code(kod_obce)

    row_df = wide[wide["kod_obce"].map(clean_code).eq(kod_obce)]

    if row_df.empty:
        raise ValueError(f"Obec s kódem {kod_obce} nebyla nalezena v trendové tabulce.")

    row = row_df.iloc[0]

    obec = row.get("obec", "obec")
    okres = row.get("okres", "neuvedeno")
    orp = row.get("orp", "neuvedeno")
    size_category = row.get("size_category", "neuvedeno")

    indicators_to_show = [
        "population",
        "migration_balance_per_1000",
        "natural_increase",
        "unemployment_rate",
        "completed_flats_per_1000",
        "completed_flats_estimated",
        "ecological_stability_coef",
        "average_age",
    ]

    lines: list[str] = []

    lines.append(f"# Trendový profil obce: {obec}\n")
    lines.append("## Základní informace\n")
    lines.append("| Položka | Hodnota |")
    lines.append("|---|---:|")
    lines.append(f"| Kód obce / ZÚJ | `{kod_obce}` |")
    lines.append(f"| Okres | {okres} |")
    lines.append(f"| ORP | {orp} |")
    lines.append(f"| Velikostní kategorie | {size_category} |")

    lines.append(f"\n## Trend vybraných indikátorů {BASE_YEAR}–{CURRENT_YEAR}\n")
    lines.append(
        "| Ukazatel | 2020 | 2021 | 2022 | 2023 | 2024 | "
        "Meziroční změna | Změna za 5 let | Trend 2020–2024 |"
    )
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---|")

    for indicator in indicators_to_show:
        if f"{indicator}_{CURRENT_YEAR}" in wide.columns:
            lines.append(render_indicator_trend(row, indicator))

    lines.append("\n## Jak trend interpretovat\n")
    lines.append(
        "Trend pomáhá odlišit dlouhodobější vývoj od jednorázového výkyvu. "
        "To je důležité zejména u menších obcí, kde například několik dokončených bytů "
        "může výrazně změnit přepočet na 1000 obyvatel."
    )

    lines.append("\n## Význam sloupců\n")
    lines.append(f"- `Meziroční změna` znamená rozdíl hodnoty {CURRENT_YEAR} minus {PREVIOUS_YEAR}.")
    lines.append(f"- `Změna za 5 let` znamená rozdíl hodnoty {CURRENT_YEAR} minus {BASE_YEAR}.")
    lines.append("- U procentních ukazatelů jde o změnu v procentních bodech, ne o procentní růst.")
    lines.append("- U přepočtů na 1000 obyvatel jde o změnu hodnoty indikátoru v dané jednotce.")

    lines.append("\n## Interpretační poznámky\n")
    lines.append("- `Zlepšení` a `zhoršení` se určuje podle směru indikátoru.")
    lines.append("- U nezaměstnanosti a průměrného věku znamená nižší hodnota lepší směr.")
    lines.append("- U migrace, bydlení, populace a ekologické stability znamená vyšší hodnota lepší směr.")
    lines.append("- Trend není kauzální vysvětlení, ale signál pro další analýzu.")

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    out = OUTPUTS_DIR / f"trend_profile_{kod_obce}.md"
    out.write_text("\n".join(lines), encoding="utf-8")

    return out


# =============================================================================
# HLAVNÍ BĚH
# =============================================================================

def run(kod_obce: str = "540480") -> None:
    """Hlavní běh."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    cfg = load_config()
    geo = load_geo_master()

    print("[INFO] Vytvářím long timeseries tabulku...")
    ts = build_raw_timeseries(cfg)
    ts = attach_population_and_transforms(ts)

    ts = ts.sort_values(["kod_obce", "indicator_id", "year"])
    ts.to_csv(TIMESERIES_OUT, index=False, encoding="utf-8-sig")
    print("[OK] Timeseries uložena:", TIMESERIES_OUT)

    print("[INFO] Vytvářím wide trendovou tabulku...")
    wide = make_wide_trends(ts, geo)
    wide.to_csv(TRENDS_WIDE_OUT, index=False, encoding="utf-8-sig")
    print("[OK] Trendová wide tabulka uložena:", TRENDS_WIDE_OUT)

    profile_path = create_trend_profile(wide, kod_obce=kod_obce)
    print("[OK] Trendový profil uložen:", profile_path)

    selected = wide[wide["kod_obce"].map(clean_code).eq(clean_code(kod_obce))]

    if not selected.empty:
        row = selected.iloc[0]
        print("")
        print(f"Kontrola obce {row.get('obec', kod_obce)}:")

        for indicator in [
            "population",
            "migration_balance_per_1000",
            "unemployment_rate",
            "completed_flats_per_1000",
            "completed_flats_estimated",
            "average_age",
        ]:
            c_current = f"{indicator}_{CURRENT_YEAR}"
            trend = f"{indicator}_trend_{BASE_YEAR}_{CURRENT_YEAR}"

            if c_current in wide.columns:
                print(
                    f"  {indicator}: "
                    f"{CURRENT_YEAR}={row.get(c_current)}; "
                    f"trend={row.get(trend, 'bez dat')}"
                )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Vytvoří trendové indikátory obcí za roky 2020–2024."
    )
    parser.add_argument(
        "--kod-obce",
        default="540480",
        help="Šestimístný kód obce pro trendový profil. Výchozí je 540480 Moravičany.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run(kod_obce=args.kod_obce)