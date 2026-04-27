#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
14_generate_interactive_map_business_dashboard.py

Interaktivní datová mapa obcí ČR s rozvojovým dashboardem.

Hlavní logika:
- mapa zobrazuje konkrétní ukazatel, ne kompozitní index,
- výchozí oblast je Odpadové hospodářství,
- ukazatele jsou seskupené do oblastí,
- trendová tabulka ukazuje jen vybranou oblast,
- grafy ukazují jen vybranou oblast,
- u odpadů se používá období 2021–2023,
- u ČSÚ ukazatelů období 2020–2024,
- u krajiny se jako trend ukazuje hlavně koeficient ekologické stability,
- katastrální / land-use ukazatele se zobrazují jako statický profil území,
- věková struktura se zobrazuje jen pro oblast Demografie a věková struktura,
- priority pro starostu se neduplikují s hlavními rozvojovými souvislostmi,
- KES je interpretován podle prahů používaných v Mozaice UR,
- pro živou ukázku lze zrychlit mapu přes FAST_DEMO_MODE,
- zoom mapy je ovládaný přes + / - nebo Command/Ctrl/Alt + kolečko.

Vstupy:
    data/geo/municipalities.geojson
    data/processed/dimension_scores.csv
    data/processed/municipality_indicators_raw.csv
    data/processed/municipality_indicators_trends_wide.csv
    data/processed/age_structure_trends_wide.csv
    data/processed/waste_indicators_trends_wide.csv

Výstup:
    outputs/interactive_map_business_dashboard.html

Spuštění:
    python municipal_map_mvp/src/14_generate_interactive_map_business_dashboard.py
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

try:
    import geopandas as gpd
except ImportError as exc:
    raise ImportError(
        "Chybí geopandas. Nainstaluj například:\n"
        "conda install geopandas\n"
        "nebo:\n"
        "pip install geopandas"
    ) from exc


# =============================================================================
# CESTY
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
GEO_DIR = DATA_DIR / "geo"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

GEOJSON_PATH = GEO_DIR / "municipalities.geojson"

SCORES_PATH = PROCESSED_DIR / "dimension_scores.csv"
RAW_INDICATORS_PATH = PROCESSED_DIR / "municipality_indicators_raw.csv"
TRENDS_PATH = PROCESSED_DIR / "municipality_indicators_trends_wide.csv"
AGE_TRENDS_PATH = PROCESSED_DIR / "age_structure_trends_wide.csv"
WASTE_TRENDS_PATH = PROCESSED_DIR / "waste_indicators_trends_wide.csv"

OUTPUT_PATH = OUTPUTS_DIR / "interactive_map_business_dashboard.html"


# =============================================================================
# REŽIM PRO ŽIVOU UKÁZKU
# =============================================================================

# True = menší a rychlejší HTML pro prezentaci.
# False = plná přesnost hranic obcí.
FAST_DEMO_MODE = True

# Zjednodušení hranic v metrech.
# Doporučení:
# - 60 m = přesnější, stále rychlé
# - 100 m = dobrý kompromis pro živou ukázku
# - 150 m = nejrychlejší, hrubší hranice
GEOMETRY_SIMPLIFY_TOLERANCE_METERS = 100


# =============================================================================
# DEFINICE UKAZATELŮ
# =============================================================================

MAP_INDICATORS = {
    "population": {
        "label": "Počet obyvatel",
        "unit": "obyvatel",
        "digits": 0,
        "direction": "CONTEXT",
        "description": "Velikost obce podle počtu obyvatel.",
        "requires_population": False,
    },
    "migration_balance_per_1000": {
        "label": "Migrační saldo / 1000 obyvatel",
        "unit": "",
        "digits": 2,
        "direction": "UP",
        "description": "Kladná hodnota znamená, že se do obce více lidí přistěhovalo, než se odstěhovalo.",
        "requires_population": True,
    },
    "natural_increase": {
        "label": "Přirozený přírůstek / úbytek",
        "unit": "osob",
        "digits": 0,
        "direction": "UP",
        "description": "Rozdíl mezi počtem narozených a zemřelých.",
        "requires_population": True,
    },
    "unemployment_rate": {
        "label": "Podíl nezaměstnaných osob",
        "unit": "%",
        "digits": 2,
        "direction": "DOWN",
        "description": "Nižší hodnota obvykle znamená příznivější situaci na trhu práce.",
        "requires_population": True,
    },
    "completed_flats_per_1000": {
        "label": "Dokončené byty / 1000 obyvatel",
        "unit": "",
        "digits": 2,
        "direction": "UP",
        "description": "Intenzita bytové výstavby v přepočtu na velikost obce.",
        "requires_population": True,
    },
    "children_share": {
        "label": "Podíl dětí 0–14",
        "unit": "%",
        "digits": 2,
        "direction": "CONTEXT",
        "description": "Podíl dětské složky populace.",
        "requires_population": True,
    },
    "working_age_share": {
        "label": "Podíl obyvatel 15–64",
        "unit": "%",
        "digits": 2,
        "direction": "CONTEXT",
        "description": "Podíl obyvatel v produktivním věku.",
        "requires_population": True,
    },
    "senior_share": {
        "label": "Podíl seniorů 65+",
        "unit": "%",
        "digits": 2,
        "direction": "CONTEXT",
        "description": "Podíl seniorské složky populace.",
        "requires_population": True,
    },
    "ageing_index": {
        "label": "Index stáří",
        "unit": "",
        "digits": 2,
        "direction": "DOWN",
        "description": "Počet seniorů 65+ na 100 dětí 0–14.",
        "requires_population": True,
    },
    "average_age": {
        "label": "Průměrný věk",
        "unit": "roku",
        "digits": 1,
        "direction": "DOWN",
        "description": "Průměrný věk obyvatel obce.",
        "requires_population": True,
    },
    "waste_sorting_target_share": {
        "label": "Plnění cíle třídění",
        "unit": "%",
        "digits": 2,
        "direction": "UP",
        "description": "Vyšší hodnota znamená lepší plnění cíle třídění komunálních odpadů.",
        "requires_population": False,
    },
    "municipal_waste_kg_per_capita": {
        "label": "Komunální odpad / obyv.",
        "unit": "kg/obyv.",
        "digits": 1,
        "direction": "DOWN",
        "description": "Produkce komunálního odpadu v kg na obyvatele. Nižší hodnota je obecně příznivější, ale musí se kontrolovat skladba odpadu.",
        "requires_population": True,
    },
    "mixed_municipal_waste_kg_per_capita": {
        "label": "Směsný komunální odpad / obyv.",
        "unit": "kg/obyv.",
        "digits": 1,
        "direction": "DOWN",
        "description": "Produkce směsného komunálního odpadu v kg na obyvatele. Nižší hodnota je příznivější.",
        "requires_population": True,
    },
    "bulky_waste_kg_per_capita": {
        "label": "Objemný odpad / obyv.",
        "unit": "kg/obyv.",
        "digits": 1,
        "direction": "DOWN",
        "description": "Produkce objemného odpadu v kg na obyvatele.",
        "requires_population": True,
    },
    "separated_recyclables_kg_per_capita": {
        "label": "Separované recyklovatelné složky / obyv.",
        "unit": "kg/obyv.",
        "digits": 1,
        "direction": "CONTEXT",
        "description": "Množství separovaných recyklovatelných složek v kg na obyvatele.",
        "requires_population": True,
    },
    "plastic_separation_kg_per_capita": {
        "label": "Separace plastu / obyv.",
        "unit": "kg/obyv.",
        "digits": 1,
        "direction": "CONTEXT",
        "description": "Množství vytříděného plastu v kg na obyvatele.",
        "requires_population": True,
    },
    "plastic_separation_efficiency": {
        "label": "Účinnost separace plastu",
        "unit": "%",
        "digits": 2,
        "direction": "UP",
        "description": "Vyšší hodnota znamená lepší účinnost separace plastu.",
        "requires_population": False,
    },
    "bio_waste_kg_per_capita": {
        "label": "Bioodpad / obyv.",
        "unit": "kg/obyv.",
        "digits": 1,
        "direction": "CONTEXT",
        "description": "Množství bioodpadu v kg na obyvatele.",
        "requires_population": True,
    },
    "ecological_stability_coef": {
        "label": "Koeficient ekologické stability",
        "unit": "",
        "digits": 4,
        "direction": "UP",
        "description": "Poměr ekologicky příznivých ploch vůči plochám zatěžujícím životní prostředí.",
        "requires_population": False,
    },
    "municipality_area_km2": {
        "label": "Výměra obce",
        "unit": "km²",
        "digits": 2,
        "direction": "CONTEXT",
        "description": "Celková výměra území obce.",
        "requires_population": False,
    },
    "population_density_per_km2": {
        "label": "Hustota obyvatel",
        "unit": "obyv./km²",
        "digits": 1,
        "direction": "CONTEXT",
        "description": "Počet obyvatel na km² území obce.",
        "requires_population": True,
    },
    "built_up_area_share": {
        "label": "Podíl zastavěných ploch",
        "unit": "%",
        "digits": 2,
        "direction": "DOWN",
        "description": "Podíl zastavěných ploch na výměře obce.",
        "requires_population": False,
    },
    "arable_land_share": {
        "label": "Podíl orné půdy",
        "unit": "%",
        "digits": 2,
        "direction": "CONTEXT",
        "description": "Podíl orné půdy na výměře obce.",
        "requires_population": False,
    },
    "forest_land_share": {
        "label": "Podíl lesní půdy",
        "unit": "%",
        "digits": 2,
        "direction": "UP",
        "description": "Podíl lesní půdy na výměře obce.",
        "requires_population": False,
    },
    "permanent_grassland_share": {
        "label": "Podíl trvalých travních porostů",
        "unit": "%",
        "digits": 2,
        "direction": "UP",
        "description": "Podíl trvalých travních porostů na výměře obce.",
        "requires_population": False,
    },
    "water_area_share": {
        "label": "Podíl vodních ploch",
        "unit": "%",
        "digits": 2,
        "direction": "UP",
        "description": "Podíl vodních ploch na výměře obce.",
        "requires_population": False,
    },
    "agricultural_land_share": {
        "label": "Podíl zemědělské půdy",
        "unit": "%",
        "digits": 2,
        "direction": "CONTEXT",
        "description": "Podíl zemědělské půdy na výměře obce.",
        "requires_population": False,
    },
    "natural_stable_area_share": {
        "label": "Přírodně stabilnější plochy",
        "unit": "%",
        "digits": 2,
        "direction": "UP",
        "description": "Součet lesní půdy, trvalých travních porostů a vodních ploch na výměře obce.",
        "requires_population": False,
    },
    "intensive_land_use_share": {
        "label": "Intenzivně využívané plochy",
        "unit": "%",
        "digits": 2,
        "direction": "DOWN",
        "description": "Součet orné půdy a zastavěných ploch na výměře obce.",
        "requires_population": False,
    },
}

RAW_INDICATORS = [
    "migration_balance_per_1000",
    "natural_increase",
    "unemployment_rate",
    "completed_flats_per_1000",
    "completed_flats_estimated",
    "average_age",
    "children_count",
    "working_age_count",
    "senior_count",
    "children_share",
    "working_age_share",
    "senior_share",
    "ageing_index",
    "children_share_change_2024_2020",
    "working_age_share_change_2024_2020",
    "senior_share_change_2024_2020",
    "ageing_index_change_2024_2020",
    "waste_sorting_target_share",
    "municipal_waste_kg_per_capita",
    "mixed_municipal_waste_kg_per_capita",
    "bulky_waste_kg_per_capita",
    "separated_recyclables_kg_per_capita",
    "plastic_separation_kg_per_capita",
    "plastic_separation_efficiency",
    "bio_waste_kg_per_capita",
    "ecological_stability_coef",
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
]

TREND_INDICATORS = [
    "population",
    "migration_balance_per_1000",
    "natural_increase",
    "unemployment_rate",
    "completed_flats_per_1000",
    "completed_flats_estimated",
    "ecological_stability_coef",
    "average_age",
    "children_share",
    "working_age_share",
    "senior_share",
    "ageing_index",
]

WASTE_INDICATORS = [
    "waste_sorting_target_share",
    "municipal_waste_kg_per_capita",
    "mixed_municipal_waste_kg_per_capita",
    "bulky_waste_kg_per_capita",
    "separated_recyclables_kg_per_capita",
    "plastic_separation_kg_per_capita",
    "plastic_separation_efficiency",
    "bio_waste_kg_per_capita",
]

LAND_USE_INDICATORS = [
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
]

AGE_TREND_PREFIXES = [
    "children",
    "working_age",
    "seniors",
    "children_share",
    "working_age_share",
    "senior_share",
    "ageing_index",
]

POSSIBLE_GEO_CODE_COLUMNS = [
    "kod_obce",
    "KOD_OBCE",
    "kod_obec",
    "KOD_OBEC",
    "kod_obec_p",
    "KOD_OBEC_P",
    "koduzemi",
    "KODUZEMI",
    "kod_uzemi",
    "KOD_UZEMI",
    "zuj",
    "ZUJ",
]


# =============================================================================
# POMOCNÉ FUNKCE
# =============================================================================

def clean_code(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip().replace(".0", "")


def read_csv_smart(path: Path) -> pd.DataFrame:
    last_error = None

    for enc in ["utf-8-sig", "utf-8", "cp1250", "windows-1250", "latin-1"]:
        try:
            return pd.read_csv(path, encoding=enc, low_memory=False)
        except Exception as exc:
            last_error = exc

    raise RuntimeError(f"Nepodařilo se načíst {path}: {last_error}")


def find_geo_code_column(gdf: gpd.GeoDataFrame) -> str:
    for col in POSSIBLE_GEO_CODE_COLUMNS:
        if col in gdf.columns:
            return col

    raise ValueError(
        "V geodatech se nepodařilo najít sloupec s kódem obce.\n"
        f"Dostupné sloupce: {list(gdf.columns)}"
    )


def require_input_files() -> None:
    required = [
        GEOJSON_PATH,
        SCORES_PATH,
        RAW_INDICATORS_PATH,
        TRENDS_PATH,
        AGE_TRENDS_PATH,
    ]

    missing = [path for path in required if not path.exists()]

    if missing:
        msg = "\n".join(str(p) for p in missing)
        raise FileNotFoundError(
            "Chybí vstupní soubory:\n"
            f"{msg}\n\n"
            "Nejdřív spusť hlavní kroky:\n"
            "python municipal_map_mvp/src/pipeline_core_scripts_02_06.py indicators\n"
            "python municipal_map_mvp/src/13_build_indicator_trends.py\n"
            "python municipal_map_mvp/src/15_add_age_structure.py\n"
            "python municipal_map_mvp/src/17_apply_methodology_updates.py\n"
            "python municipal_map_mvp/src/19_download_visoh2_waste.py\n"
            "python municipal_map_mvp/src/20_add_land_use_environment.py"
        )


def safe_numeric_columns(df: pd.DataFrame, skip_cols: set[str]) -> pd.DataFrame:
    out = df.copy()

    for col in out.columns:
        if col in skip_cols:
            continue

        out[col] = pd.to_numeric(out[col], errors="ignore")

    return out


# =============================================================================
# PŘÍPRAVA DAT
# =============================================================================

def prepare_data() -> gpd.GeoDataFrame:
    require_input_files()

    print("[INFO] Načítám geodata...")
    gdf = gpd.read_file(GEOJSON_PATH)

    if gdf.crs is None:
        print("[WARN] GeoJSON nemá CRS. Nastavuji EPSG:4326.")
        gdf = gdf.set_crs("EPSG:4326")
    elif str(gdf.crs).lower() not in ["epsg:4326", "wgs84"]:
        gdf = gdf.to_crs("EPSG:4326")

    code_col = find_geo_code_column(gdf)
    gdf["kod_obce"] = gdf[code_col].map(clean_code)

    print("[INFO] Načítám identitu obcí a benchmarky...")
    scores = read_csv_smart(SCORES_PATH)
    scores["kod_obce"] = scores["kod_obce"].map(clean_code)

    score_keep_cols = [
        "kod_obce",
        "obec",
        "okres",
        "orp",
        "population",
        "size_category",
        "size_category_final",
        "settlement_type",
        "volatility_warning",
    ]
    scores = scores[[c for c in score_keep_cols if c in scores.columns]].copy()
    scores = safe_numeric_columns(
        scores,
        skip_cols={
            "kod_obce",
            "obec",
            "okres",
            "orp",
            "size_category",
            "size_category_final",
            "settlement_type",
            "volatility_warning",
        },
    )

    print("[INFO] Načítám surové indikátory...")
    raw = read_csv_smart(RAW_INDICATORS_PATH)
    raw["kod_obce"] = raw["kod_obce"].map(clean_code)

    raw_keep_cols = ["kod_obce", *RAW_INDICATORS]
    raw = raw[[c for c in raw_keep_cols if c in raw.columns]].copy()
    raw = safe_numeric_columns(raw, skip_cols={"kod_obce"})

    if "completed_flats_estimated" not in raw.columns:
        if "completed_flats_per_1000" in raw.columns and "population" in scores.columns:
            tmp = scores[["kod_obce", "population"]].merge(raw, on="kod_obce", how="left")
            tmp["completed_flats_estimated"] = (
                pd.to_numeric(tmp["completed_flats_per_1000"], errors="coerce")
                * pd.to_numeric(tmp["population"], errors="coerce")
                / 1000
            )
            raw = raw.merge(
                tmp[["kod_obce", "completed_flats_estimated"]],
                on="kod_obce",
                how="left",
            )

    print("[INFO] Načítám trendovou tabulku indikátorů...")
    trends = read_csv_smart(TRENDS_PATH)
    trends["kod_obce"] = trends["kod_obce"].map(clean_code)

    trend_cols = [
        c for c in trends.columns
        if c == "kod_obce"
        or any(c.startswith(f"{ind}_") for ind in TREND_INDICATORS)
    ]
    trends = trends[trend_cols].copy()
    trends = safe_numeric_columns(
        trends,
        skip_cols={
            "kod_obce",
            *[
                c for c in trends.columns
                if c.endswith("_trend_2020_2024") or c.endswith("_trend_20_24")
            ],
        },
    )

    print("[INFO] Načítám věkovou strukturu 2020–2024...")
    age = read_csv_smart(AGE_TRENDS_PATH)
    age["kod_obce"] = age["kod_obce"].map(clean_code)

    age_cols = [
        c for c in age.columns
        if c == "kod_obce"
        or any(c.startswith(f"{prefix}_") for prefix in AGE_TREND_PREFIXES)
    ]
    age = age[age_cols].copy()
    age = safe_numeric_columns(age, skip_cols={"kod_obce"})

    print("[INFO] Načítám odpadové ukazatele VISOH2...")
    waste = pd.DataFrame({"kod_obce": []})

    if WASTE_TRENDS_PATH.exists():
        waste = read_csv_smart(WASTE_TRENDS_PATH)
        waste["kod_obce"] = waste["kod_obce"].map(clean_code)

        waste_cols = [
            c for c in waste.columns
            if c == "kod_obce"
            or c in ["waste_data_first_year", "waste_data_latest_year"]
            or c in WASTE_INDICATORS
            or any(c.startswith(f"{ind}_") for ind in WASTE_INDICATORS)
        ]
        waste = waste[waste_cols].copy()
        waste = safe_numeric_columns(
            waste,
            skip_cols={
                "kod_obce",
                *[c for c in waste.columns if "_trend_" in c],
            },
        )
    else:
        print(f"[WARN] Chybí {WASTE_TRENDS_PATH}, odpadové trendy přeskočeny.")

    print("[INFO] Spojuji identitu, surové hodnoty, trendy, věkovou strukturu a odpady...")
    data = scores.merge(raw, on="kod_obce", how="left")
    data = data.merge(trends, on="kod_obce", how="left")
    data = data.merge(age, on="kod_obce", how="left")

    if not waste.empty:
        overlapping = [c for c in waste.columns if c != "kod_obce" and c in data.columns]
        if overlapping:
            data = data.drop(columns=overlapping)

        data = data.merge(waste, on="kod_obce", how="left")

    for indicator in MAP_INDICATORS:
        if indicator not in data.columns and f"{indicator}_2024" in data.columns:
            data[indicator] = data[f"{indicator}_2024"]

    print("[INFO] Spojuji geometrii s daty...")
    merged = gdf.merge(data, on="kod_obce", how="left")

    matched = merged["population"].notna().sum() if "population" in merged.columns else 0
    total = len(merged)
    print(f"[INFO] Spojeno: {matched}/{total} obcí má základní data.")

    base_cols = [
        "kod_obce",
        "obec",
        "okres",
        "orp",
        "population",
        "size_category",
        "size_category_final",
        "settlement_type",
        "volatility_warning",
        *MAP_INDICATORS.keys(),
        *RAW_INDICATORS,
    ]

    dynamic_trend_cols = [
        c for c in merged.columns
        if any(c.startswith(f"{ind}_") for ind in TREND_INDICATORS)
        or any(c.startswith(f"{prefix}_") for prefix in AGE_TREND_PREFIXES)
        or any(c.startswith(f"{ind}_") for ind in WASTE_INDICATORS)
        or c in ["waste_data_first_year", "waste_data_latest_year"]
    ]

    output_cols = []
    for col in [*base_cols, *dynamic_trend_cols, "geometry"]:
        if col in merged.columns and col not in output_cols:
            output_cols.append(col)

    merged = merged[output_cols].copy()

    if FAST_DEMO_MODE:
        print(
            "[INFO] FAST_DEMO_MODE=True: zjednodušuji geometrii pro rychlejší živou ukázku "
            f"({GEOMETRY_SIMPLIFY_TOLERANCE_METERS} m)."
        )

        original_crs = merged.crs

        merged_projected = merged.to_crs("EPSG:3857")
        merged_projected["geometry"] = merged_projected.geometry.simplify(
            tolerance=GEOMETRY_SIMPLIFY_TOLERANCE_METERS,
            preserve_topology=True,
        )

        merged = merged_projected.to_crs(original_crs)

    return merged


# =============================================================================
# HTML
# =============================================================================

def generate_html(gdf: gpd.GeoDataFrame) -> str:
    print("[INFO] Převádím data do GeoJSON pro HTML...")

    gdf = gdf.copy()
    gdf = gdf.to_crs("EPSG:4326")
    gdf = gdf.where(pd.notnull(gdf), None)

    geojson_data = json.loads(gdf.to_json())

    geojson_json = json.dumps(
        geojson_data,
        ensure_ascii=False,
        separators=(",", ":"),
    )

    indicator_meta_json = json.dumps(
        MAP_INDICATORS,
        ensure_ascii=False,
        separators=(",", ":"),
    )

    html_template = """<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<title>Datová mapa obcí ČR — rozvojový dashboard</title>

<link
  rel="stylesheet"
  href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
/>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
html, body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f5f5f5;
    color: #222;
}

#map {
    height: 68vh;
    width: 100%;
}

.leaflet-control-zoom {
    border: 1px solid #999 !important;
    box-shadow: 0 2px 10px rgba(0,0,0,0.25) !important;
}

.leaflet-control-zoom a {
    width: 34px !important;
    height: 34px !important;
    line-height: 34px !important;
    font-size: 22px !important;
    font-weight: bold !important;
}

.zoom-hint {
    position: absolute;
    right: 16px;
    top: 88px;
    z-index: 9999;
    background: rgba(255,255,255,0.92);
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 6px 9px;
    font-size: 12px;
    color: #444;
    box-shadow: 0 1px 6px rgba(0,0,0,0.15);
}

.control-panel {
    position: absolute;
    top: 16px;
    left: 16px;
    width: 365px;
    max-height: 64vh;
    overflow-y: auto;
    z-index: 9999;
    background: white;
    border: 1px solid #999;
    border-radius: 8px;
    padding: 14px;
    box-shadow: 0 2px 14px rgba(0,0,0,0.25);
    font-size: 14px;
    transition: width 0.2s ease, max-height 0.2s ease, padding 0.2s ease;
}

.control-panel.collapsed {
    width: 58px;
    max-height: 48px;
    overflow: hidden;
    padding: 8px;
}

.panel-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
}

.panel-top h2 {
    font-size: 17px;
    margin: 0;
}

.control-panel.collapsed .panel-content,
.control-panel.collapsed .panel-title {
    display: none;
}

.panel-toggle {
    width: 36px;
    min-width: 36px;
    height: 32px;
    margin: 0;
    padding: 0;
    border: 1px solid #ccc;
    border-radius: 6px;
    background: #eeeeee;
    font-size: 18px;
    cursor: pointer;
}

.control-panel label {
    display: block;
    margin-top: 8px;
    font-weight: bold;
}

.control-panel select,
.control-panel input {
    width: 100%;
    box-sizing: border-box;
    margin-top: 3px;
    padding: 6px;
    border-radius: 7px;
    border: 1px solid #ccc;
}

.small-note {
    font-size: 12px;
    color: #555;
    margin-top: 8px;
    line-height: 1.35;
}

.legend {
    position: absolute;
    right: 16px;
    bottom: calc(32vh + 16px);
    z-index: 9999;
    background: white;
    border: 1px solid #999;
    border-radius: 8px;
    padding: 10px;
    font-size: 13px;
    box-shadow: 0 2px 14px rgba(0,0,0,0.25);
    min-width: 230px;
}

.legend i {
    display: inline-block;
    width: 14px;
    height: 14px;
    margin-right: 6px;
}

.legend.collapsed {
    min-width: auto;
    width: 52px;
    height: 48px;
    overflow: hidden;
    padding: 8px;
}

.legend-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 8px;
}

.legend-toggle {
    width: 32px;
    min-width: 32px;
    height: 30px;
    margin: 0;
    padding: 0;
    border: 1px solid #ccc;
    border-radius: 7px;
    background: #eeeeee;
    font-size: 18px;
    line-height: 1;
    cursor: pointer;
}

.legend.collapsed .legend-content,
.legend.collapsed #legend_indicator_name,
.legend.collapsed .legend-header b {
    display: none;
}

.legend.collapsed .legend-header {
    justify-content: center;
}

button {
    margin-top: 10px;
    width: 100%;
    padding: 7px;
    cursor: pointer;
}

hr {
    border: 0;
    border-top: 1px solid #ddd;
}

.tooltip-note {
    font-size: 12px;
    color: #555;
}

.dashboard {
    padding: 18px 24px 30px 24px;
    background: #f5f5f5;
}

.dashboard-inner {
    max-width: 1550px;
    margin: 0 auto;
}

.dashboard-header {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 14px;
}

.dashboard-title h1 {
    font-size: 23px;
    margin: 0 0 6px 0;
}

.dashboard-title p {
    margin: 0;
    color: #555;
}

.cards {
    display: grid;
    grid-template-columns: repeat(4, minmax(160px, 1fr));
    gap: 12px;
    margin: 12px 0;
}

.card {
    background: white;
    border-radius: 10px;
    padding: 12px;
    box-shadow: 0 1px 6px rgba(0,0,0,0.10);
    border: 1px solid #e0e0e0;
}

.card .label {
    font-size: 12px;
    color: #555;
    margin-bottom: 4px;
}

.card .value {
    font-size: 22px;
    font-weight: bold;
}

.card .sub {
    font-size: 12px;
    color: #666;
    margin-top: 4px;
}

.grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 14px;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(260px, 1fr));
    gap: 14px;
    margin-top: 14px;
}

.panel {
    background: white;
    border-radius: 10px;
    padding: 14px;
    box-shadow: 0 1px 6px rgba(0,0,0,0.10);
    border: 1px solid #e0e0e0;
}

.panel h2 {
    font-size: 17px;
    margin: 0 0 10px 0;
}

.panel p {
    line-height: 1.45;
}

table {
    border-collapse: collapse;
    width: 100%;
    font-size: 13px;
}

th, td {
    border-bottom: 1px solid #eee;
    padding: 6px 5px;
    text-align: right;
}

th:first-child,
td:first-child {
    text-align: left;
}

.badge {
    display: inline-block;
    padding: 3px 8px;
    border-radius: 999px;
    font-size: 12px;
    background: #eee;
    margin-right: 4px;
    white-space: nowrap;
}

.badge-good {
    background: #e5f5e0;
    color: #006d2c;
}

.badge-bad {
    background: #fee0d2;
    color: #a50f15;
}

.badge-neutral {
    background: #eeeeee;
    color: #444;
}

.warning-box {
    background: #fff3cd;
    border: 1px solid #ffe08a;
    border-radius: 8px;
    padding: 10px;
    margin: 10px 0 0 0;
    color: #6b5200;
    font-size: 13px;
}

.age-bar {
    display: flex;
    width: 100%;
    height: 28px;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid #ddd;
    margin: 10px 0;
}

.age-segment {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    color: #111;
    white-space: nowrap;
}

.age-children {
    background: #c7e9c0;
}

.age-working {
    background: #c6dbef;
}

.age-seniors {
    background: #fdd0a2;
}

.chart-card {
    background: white;
    border-radius: 10px;
    padding: 12px;
    box-shadow: 0 1px 6px rgba(0,0,0,0.10);
    border: 1px solid #e0e0e0;
    min-height: 260px;
}

.chart-card h3 {
    font-size: 15px;
    margin: 0 0 8px 0;
}

.chart-wrap {
    height: 210px;
}

.diagnostic-item {
    border-bottom: 1px solid #eee;
    padding: 10px 0;
}

.diagnostic-item:last-child {
    border-bottom: 0;
}

.diagnostic-text {
    margin-top: 6px;
    line-height: 1.45;
}

.land-profile-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
}

.land-profile-bars {
    display: grid;
    gap: 9px;
}

.land-bar-row {
    display: grid;
    grid-template-columns: 190px 1fr 72px;
    gap: 8px;
    align-items: center;
    font-size: 13px;
}

.land-bar-outer {
    background: #eee;
    height: 12px;
    border-radius: 999px;
    overflow: hidden;
}

.land-bar-inner {
    height: 100%;
    background: #74a9cf;
}

.land-summary-box {
    background: #f7f7f7;
    border-radius: 8px;
    padding: 10px;
    border: 1px solid #e0e0e0;
    line-height: 1.45;
}

@media (max-width: 1100px) {
    .cards {
        grid-template-columns: repeat(2, minmax(160px, 1fr));
    }

    .grid-2,
    .grid-3,
    .land-profile-grid {
        grid-template-columns: 1fr;
    }

    .control-panel {
        width: 320px;
    }

    .control-panel.collapsed {
        width: 58px;
    }

    .legend {
        right: 16px;
        bottom: calc(32vh + 16px);
    }
}
</style>
</head>

<body>
<div id="map"></div>
<div class="zoom-hint">Zoom: + / − nebo Command/Ctrl/Alt + kolečko</div>

<div class="control-panel" id="control_panel">
    <div class="panel-top">
        <h2 class="panel-title">Datová mapa obcí ČR</h2>
        <button class="panel-toggle" id="panel_toggle" onclick="toggleControlPanel()" title="Sbalit / rozbalit panel">‹</button>
    </div>

    <div class="panel-content">
        <label for="municipality_search">Najít obec</label>
        <input
            id="municipality_search"
            list="municipality_list"
            placeholder="Zadej název nebo kód obce"
        >
        <datalist id="municipality_list"></datalist>
        <button onclick="zoomToMunicipality()">Najít a přiblížit obec</button>
        <div id="search_status" class="small-note"></div>

        <label for="size_filter">Velikostní benchmark</label>
        <select id="size_filter">
            <option value="ALL">Všechny benchmarky</option>
        </select>

        <div class="small-note">
            Barva mapy je počítána z vybraného ukazatele relativně vůči podobně velkým obcím.
            V tooltipu a dashboardu je vždy zobrazena surová hodnota.
        </div>

        <label for="indicator_group">Oblast ukazatelů</label>
        <select id="indicator_group">
            <option value="waste" selected>Odpadové hospodářství</option>
            <option value="demography">Demografie a věková struktura</option>
            <option value="labour">Práce a sociálně-ekonomická situace</option>
            <option value="housing">Bydlení a výstavba</option>
            <option value="environment">Krajina a životní prostředí</option>
        </select>

        <label for="mode">Zobrazit ukazatel</label>
        <select id="mode"></select>

        <label for="year_select">Rok / období dat</label>
        <select id="year_select">
            <option value="2024">2024</option>
            <option value="2023" selected>2023</option>
            <option value="2022">2022</option>
            <option value="2021">2021</option>
            <option value="2020">2020</option>
        </select>
    </div>
</div>

<div class="legend" id="legend_panel">
    <div class="legend-header">
        <div>
            <b>Barevná škála ukazatele</b><br>
            <span id="legend_indicator_name"></span>
        </div>
        <button
            class="legend-toggle"
            id="legend_toggle"
            onclick="toggleLegendPanel()"
            title="Sbalit / rozbalit legendu"
        >›</button>
    </div>

    <div class="legend-content" id="legend_content">
        <span id="legend_range" class="small-note"></span><br><br>
        <span id="legend_rows"></span>
    </div>
</div>

<div class="dashboard">
    <div class="dashboard-inner">
        <div class="dashboard-header">
            <div class="dashboard-title">
                <h1 id="dash_title">Rozvojový přehled obce</h1>
                <p id="dash_subtitle">Klikni na obec v mapě nebo ji najdi vyhledáváním.</p>
                <div id="dash_warning"></div>
            </div>
            <div>
                <span class="badge">konkrétní ukazatel</span>
                <span class="badge">surová hodnota</span>
                <span class="badge">období podle zdroje dat</span>
                <span class="badge">pořadí v benchmarku</span>
            </div>
        </div>

        <div class="cards" id="score_cards"></div>

        <div class="grid-2">
            <div class="panel">
                <h2>Interpretace vybraného ukazatele</h2>
                <p id="business_summary">
                    Po výběru obce zde bude stručná interpretace vybraného ukazatele.
                </p>
            </div>

            <div class="panel">
                <h2 id="trend_table_title">Trendy vybrané oblasti</h2>
                <div id="trend_table"></div>
            </div>
        </div>

        <div class="panel" id="land_profile_panel" style="margin-top:14px; display:none;">
            <h2>Profil využití území</h2>
            <div id="land_profile_content"></div>
        </div>

        <div class="panel" style="margin-top:14px;">
            <h2>Priority pro starostu</h2>
            <div class="small-note" style="margin-bottom:8px;">
                Akční shortlist nejdůležitějších témat pro vedení obce.
                Položky v této části se již znovu neopakují v širších rozvojových souvislostech níže.
            </div>
            <div id="mayor_priorities"></div>
        </div>

        <div class="panel" style="margin-top:14px;">
            <h2>Hlavní rozvojové souvislosti obce</h2>
            <div class="small-note" style="margin-bottom:8px;">
                Tato část zobrazuje širší analytické souvislosti, které nejsou již uvedené v prioritách pro starostu.
                Automatická diagnostika kombinuje demografii, bydlení, odpady, nezaměstnanost a krajinu.
                Nejde o definitivní závěr, ale o signály, které má obec ověřit v rozhodování.
            </div>
            <div id="cross_domain_diagnostics"></div>
        </div>

        <div class="grid-2">
            <div class="panel" id="age_structure_wrapper" style="display:none;">
                <h2>Věková struktura obce</h2>
                <div id="age_structure_panel"></div>
            </div>

            <div class="panel">
                <h2 id="raw_table_title">Surové hodnoty vybrané oblasti</h2>
                <div id="raw_table"></div>
            </div>
        </div>

        <div class="grid-3" id="charts_grid"></div>
    </div>
</div>

<script>
const geoData = __GEOJSON_DATA__;
const indicatorMeta = __INDICATOR_META__;

const allYears = [2020, 2021, 2022, 2023, 2024];
const wasteYears = [2021, 2022, 2023];

const indicatorGroups = {
    waste: {
        label: "Odpadové hospodářství",
        subtitle: "VISOH2, období 2021–2023",
        defaultYear: "2023",
        indicators: [
            "waste_sorting_target_share",
            "municipal_waste_kg_per_capita",
            "mixed_municipal_waste_kg_per_capita",
            "bulky_waste_kg_per_capita",
            "separated_recyclables_kg_per_capita",
            "plastic_separation_kg_per_capita",
            "plastic_separation_efficiency",
            "bio_waste_kg_per_capita"
        ]
    },
    demography: {
        label: "Demografie a věková struktura",
        subtitle: "ČSÚ, období 2020–2024",
        defaultYear: "2024",
        indicators: [
            "population",
            "migration_balance_per_1000",
            "natural_increase",
            "children_share",
            "working_age_share",
            "senior_share",
            "ageing_index",
            "average_age"
        ]
    },
    labour: {
        label: "Práce a sociálně-ekonomická situace",
        subtitle: "ČSÚ, období 2020–2024",
        defaultYear: "2024",
        indicators: [
            "unemployment_rate"
        ]
    },
    housing: {
        label: "Bydlení a výstavba",
        subtitle: "ČSÚ, období 2020–2024",
        defaultYear: "2024",
        indicators: [
            "completed_flats_per_1000"
        ]
    },
    environment: {
        label: "Krajina a životní prostředí",
        subtitle: "ČSÚ/MOS a ČÚZK, poslední dostupný rok, typicky 2024",
        defaultYear: "2024",
        indicators: [
            "ecological_stability_coef",
            "municipality_area_km2",
            "population_density_per_km2",
            "built_up_area_share",
            "arable_land_share",
            "forest_land_share",
            "permanent_grassland_share",
            "water_area_share",
            "agricultural_land_share",
            "natural_stable_area_share",
            "intensive_land_use_share"
        ],
        trendIndicators: [
            "ecological_stability_coef"
        ],
        profileIndicators: [
            "municipality_area_km2",
            "population_density_per_km2",
            "built_up_area_share",
            "arable_land_share",
            "forest_land_share",
            "permanent_grassland_share",
            "water_area_share",
            "agricultural_land_share",
            "natural_stable_area_share",
            "intensive_land_use_share"
        ]
    }
};

const landUseIndicators = [
    "municipality_area_km2",
    "population_density_per_km2",
    "built_up_area_share",
    "arable_land_share",
    "forest_land_share",
    "permanent_grassland_share",
    "water_area_share",
    "agricultural_land_share",
    "natural_stable_area_share",
    "intensive_land_use_share"
];

let charts = {};
let selectedMunicipalityLayer = null;

function selectedIndicatorGroupId() {
    const el = document.getElementById("indicator_group");
    return el ? el.value : "waste";
}

function selectedIndicatorGroup() {
    return indicatorGroups[selectedIndicatorGroupId()] || indicatorGroups.waste;
}

function isWasteIndicator(indicator) {
    return indicatorGroups.waste.indicators.includes(indicator);
}

function isLandUseIndicator(indicator) {
    return landUseIndicators.includes(indicator);
}

function fillIndicatorSelectForGroup(groupId) {
    const select = document.getElementById("mode");
    const group = indicatorGroups[groupId] || indicatorGroups.waste;

    if (!select) return;

    select.innerHTML = "";

    group.indicators.forEach(function(indicatorId) {
        const meta = indicatorMeta[indicatorId];
        if (!meta) return;

        const option = document.createElement("option");
        option.value = indicatorId;
        option.textContent = meta.label;
        select.appendChild(option);
    });
}

function toggleLegendPanel() {
    const panel = document.getElementById("legend_panel");
    const button = document.getElementById("legend_toggle");

    panel.classList.toggle("collapsed");

    if (panel.classList.contains("collapsed")) {
        button.innerHTML = "‹";
        button.title = "Rozbalit legendu";
    } else {
        button.innerHTML = "›";
        button.title = "Sbalit legendu";
    }
}

function toggleControlPanel() {
    const panel = document.getElementById("control_panel");
    const button = document.getElementById("panel_toggle");

    panel.classList.toggle("collapsed");

    if (panel.classList.contains("collapsed")) {
        button.innerHTML = "›";
        button.title = "Rozbalit panel";
    } else {
        button.innerHTML = "‹";
        button.title = "Sbalit panel";
    }
}

function normalizeText(value) {
    if (value === null || value === undefined) return "";

    return String(value)
        .toLowerCase()
        .normalize("NFD")
        .replace(/[\\u0300-\\u036f]/g, "")
        .trim();
}

function benchmarkCategory(properties) {
    return properties.size_category_final || properties.size_category || "";
}

function settlementType(properties) {
    return properties.settlement_type || "";
}

function hasValidPopulation(properties) {
    const pop = Number(properties.population);
    return !isNaN(pop) && pop > 0;
}

function indicatorRequiresPopulation(indicator) {
    const meta = indicatorMeta[indicator] || {};
    return Boolean(meta.requires_population);
}

function selectedIndicatorId() {
    return document.getElementById("mode").value;
}

function selectedIndicatorMeta() {
    return indicatorMeta[selectedIndicatorId()] || {};
}

function selectedYear() {
    return document.getElementById("year_select").value;
}

function municipalityLabel(properties) {
    const name = properties.obec || "Neznámá obec";
    const code = properties.kod_obce || "";
    const okres = properties.okres || "";
    return `${name} — ${code} — ${okres}`;
}

function formatValue(value, digits = 2) {
    if (value === null || value === undefined || value === "" || isNaN(Number(value))) return "bez dat";
    return Number(value).toLocaleString("cs-CZ", {
        minimumFractionDigits: digits,
        maximumFractionDigits: digits
    });
}

function signedValue(value, digits = 2) {
    if (value === null || value === undefined || value === "" || isNaN(Number(value))) return "bez dat";
    const number = Number(value);
    const sign = number > 0 ? "+" : "";
    return sign + number.toLocaleString("cs-CZ", {
        minimumFractionDigits: digits,
        maximumFractionDigits: digits
    });
}

function formatIndicatorValue(value, meta) {
    if (value === null || value === undefined || value === "" || isNaN(Number(value))) return "bez dat";

    const digits = meta.digits ?? 2;
    let out = Number(value).toLocaleString("cs-CZ", {
        minimumFractionDigits: digits,
        maximumFractionDigits: digits
    });

    if (meta.unit) {
        out += " " + meta.unit;
    }

    return out;
}

function getIndicatorValueForYear(properties, indicator, year) {
    if (indicatorRequiresPopulation(indicator) && !hasValidPopulation(properties)) {
        return null;
    }

    if (isLandUseIndicator(indicator)) {
        const latest = properties[indicator];
        if (latest === null || latest === undefined || latest === "" || isNaN(Number(latest))) {
            return null;
        }
        return Number(latest);
    }

    let value = properties[indicator + "_" + year];

    if (value === null || value === undefined || value === "" || isNaN(Number(value))) {
        if (isWasteIndicator(indicator)) {
            return null;
        }
        value = properties[indicator];
    }

    if (value === null || value === undefined || value === "" || isNaN(Number(value))) {
        if (!isWasteIndicator(indicator)) {
            value = properties[indicator + "_2024"];
        }
    }

    value = Number(value);

    if (isNaN(value)) return null;

    return value;
}

function getRawIndicatorValue(properties) {
    return getIndicatorValueForYear(properties, selectedIndicatorId(), selectedYear());
}

function fillMunicipalitySearch() {
    const datalist = document.getElementById("municipality_list");

    const items = geoData.features
        .map(function(feature) {
            return {
                label: municipalityLabel(feature.properties),
                name: feature.properties.obec || "",
                code: feature.properties.kod_obce || "",
                okres: feature.properties.okres || ""
            };
        })
        .filter(function(item) {
            return item.name !== "";
        })
        .sort(function(a, b) {
            return a.label.localeCompare(b.label, "cs");
        });

    items.forEach(function(item) {
        const option = document.createElement("option");
        option.value = item.label;
        datalist.appendChild(option);
    });
}

function findMunicipalityFeature(query) {
    const q = normalizeText(query);

    if (q === "") return null;

    const codeMatch = String(query).match(/\\b\\d{6}\\b/);
    const searchedCode = codeMatch ? codeMatch[0] : null;

    if (searchedCode) {
        const byCode = geoData.features.find(function(feature) {
            return String(feature.properties.kod_obce) === searchedCode;
        });

        if (byCode) return byCode;
    }

    const exactName = geoData.features.find(function(feature) {
        return normalizeText(feature.properties.obec) === q;
    });

    if (exactName) return exactName;

    const startsWithName = geoData.features.find(function(feature) {
        return normalizeText(feature.properties.obec).startsWith(q);
    });

    if (startsWithName) return startsWithName;

    const containsName = geoData.features.find(function(feature) {
        return normalizeText(feature.properties.obec).includes(q);
    });

    if (containsName) return containsName;

    return null;
}

function uniqueSizeCategories() {
    const values = new Set();

    geoData.features.forEach(function(feature) {
        const cat = benchmarkCategory(feature.properties);
        if (cat !== null && cat !== undefined && cat !== "") {
            values.add(cat);
        }
    });

    return Array.from(values).sort(function(a, b) {
        return String(a).localeCompare(String(b), "cs", { numeric: true });
    });
}

function fillSizeFilter() {
    const select = document.getElementById("size_filter");
    const categories = uniqueSizeCategories();

    categories.forEach(function(cat) {
        const option = document.createElement("option");
        option.value = cat;
        option.textContent = cat;
        select.appendChild(option);
    });
}

function benchmarkFeaturesForProperties(properties) {
    const cat = benchmarkCategory(properties);

    if (!cat) return geoData.features;

    return geoData.features.filter(function(feature) {
        return benchmarkCategory(feature.properties) === cat;
    });
}

function isFeatureInCurrentFilter(feature) {
    const selectedCategory = document.getElementById("size_filter").value;

    if (selectedCategory === "ALL") return true;

    return benchmarkCategory(feature.properties) === selectedCategory;
}

function quantile(sortedValues, q) {
    if (!sortedValues.length) return null;

    const pos = (sortedValues.length - 1) * q;
    const base = Math.floor(pos);
    const rest = pos - base;

    if ((base + 1) < sortedValues.length) {
        return sortedValues[base] + rest * (sortedValues[base + 1] - sortedValues[base]);
    }

    return sortedValues[base];
}

function selectedIndicatorValuesForBenchmark(properties) {
    const indicator = selectedIndicatorId();
    const year = selectedYear();
    const features = benchmarkFeaturesForProperties(properties);

    return features
        .map(function(feature) {
            return getIndicatorValueForYear(feature.properties, indicator, year);
        })
        .filter(function(value) {
            return value !== null && value !== undefined && !isNaN(value);
        })
        .sort(function(a, b) {
            return a - b;
        });
}

function scaleStatsForProperties(properties) {
    const values = selectedIndicatorValuesForBenchmark(properties);

    if (values.length < 2) {
        return {
            values: values,
            p05: null,
            p95: null
        };
    }

    return {
        values: values,
        p05: quantile(values, 0.05),
        p95: quantile(values, 0.95)
    };
}

function valueToColorScale(properties) {
    const value = getRawIndicatorValue(properties);
    if (value === null) return null;

    const stats = scaleStatsForProperties(properties);
    const p05 = stats.p05;
    const p95 = stats.p95;

    if (p05 === null || p95 === null || p05 === p95) return null;

    const meta = selectedIndicatorMeta();

    let clipped = Math.max(p05, Math.min(p95, value));
    let scale = 100 * (clipped - p05) / (p95 - p05);

    if (meta.direction === "DOWN") {
        scale = 100 - scale;
    }

    return scale;
}

function benchmarkSize(properties) {
    return benchmarkFeaturesForProperties(properties).length;
}

function benchmarkWarningText(properties) {
    const n = benchmarkSize(properties);

    if (n < 10) {
        return "Benchmark obsahuje jen " + n + " obcí. Srovnání je pouze orientační.";
    }

    if (n < 30) {
        return "Benchmark obsahuje " + n + " obcí. Srovnání interpretuj opatrně.";
    }

    return "";
}

function benchmarkRankInfo(properties) {
    const indicator = selectedIndicatorId();
    const meta = selectedIndicatorMeta();
    const year = selectedYear();
    const value = getRawIndicatorValue(properties);

    if (value === null || value === undefined || isNaN(value)) {
        return {
            rank: null,
            total: 0,
            text: "bez dat"
        };
    }

    const features = benchmarkFeaturesForProperties(properties);

    let values = features
        .map(function(feature) {
            return getIndicatorValueForYear(feature.properties, indicator, year);
        })
        .filter(function(v) {
            return v !== null && v !== undefined && !isNaN(v);
        });

    const total = values.length;

    if (total === 0) {
        return {
            rank: null,
            total: 0,
            text: "bez dat"
        };
    }

    if (meta.direction === "DOWN") {
        values.sort(function(a, b) { return a - b; });
    } else {
        values.sort(function(a, b) { return b - a; });
    }

    if (meta.direction === "CONTEXT") {
        values.sort(function(a, b) { return b - a; });
    }

    let rank = values.findIndex(function(v) {
        return Math.abs(v - value) < 0.000001;
    });

    if (rank < 0) {
        return {
            rank: null,
            total: total,
            text: "bez dat"
        };
    }

    rank = rank + 1;

    let label = "";
    if (meta.direction === "CONTEXT") {
        label = "pořadí podle výše hodnoty";
    } else {
        label = "pořadí podle příznivosti";
    }

    return {
        rank: rank,
        total: total,
        text: rank + ". z " + total + " — " + label
    };
}

function benchmarkPositionText(properties) {
    const scale = valueToColorScale(properties);
    const meta = selectedIndicatorMeta();

    if (scale === null || scale === undefined || isNaN(scale)) {
        return "bez dat";
    }

    if (meta.direction === "CONTEXT") {
        if (scale >= 80) return "vysoká hodnota";
        if (scale >= 60) return "spíše vyšší hodnota";
        if (scale >= 40) return "střední hodnota";
        if (scale >= 20) return "spíše nižší hodnota";
        return "nízká hodnota";
    }

    if (scale >= 80) return "příznivá hodnota";
    if (scale >= 60) return "spíše příznivá hodnota";
    if (scale >= 40) return "střední hodnota";
    if (scale >= 20) return "spíše méně příznivá hodnota";
    return "riziková hodnota";
}

const canvasRenderer = L.canvas({
    padding: 0.5
});

const map = L.map("map", {
    zoomControl: false,
    preferCanvas: true,
    renderer: canvasRenderer,
    scrollWheelZoom: false,
    wheelDebounceTime: 80,
    wheelPxPerZoomLevel: 90
}).setView([49.8, 15.5], 8);

L.control.zoom({
    position: "topright"
}).addTo(map);

L.control.scale({
    position: "bottomright",
    metric: true,
    imperial: false
}).addTo(map);

let modifierWheelZoomActive = false;
const mapContainer = map.getContainer();

mapContainer.addEventListener("wheel", function(event) {
    const modifierPressed = event.metaKey || event.ctrlKey || event.altKey;

    if (modifierPressed) {
        if (!modifierWheelZoomActive) {
            map.scrollWheelZoom.enable();
            modifierWheelZoomActive = true;
        }
    } else {
        if (modifierWheelZoomActive) {
            map.scrollWheelZoom.disable();
            modifierWheelZoomActive = false;
        }
    }
}, { passive: true });

mapContainer.addEventListener("mouseleave", function() {
    map.scrollWheelZoom.disable();
    modifierWheelZoomActive = false;
});

window.addEventListener("keyup", function() {
    map.scrollWheelZoom.disable();
    modifierWheelZoomActive = false;
});

L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
    attribution: "&copy; OpenStreetMap &copy; CARTO",
    subdomains: "abcd",
    maxZoom: 19,
    updateWhenIdle: true,
    keepBuffer: 2
}).addTo(map);

function getColor(value) {
    // Jednotná barevná škála pro všechny typy ukazatelů:
    // vyšší skóre = lepší / příznivější / vyšší kontextová hodnota = zelená,
    // nižší skóre = horší / méně příznivá / nižší kontextová hodnota = červená.
    if (value === null || value === undefined || isNaN(value)) return "#d9d9d9";
    value = Number(value);

    if (value >= 80) return "#006837";
    if (value >= 60) return "#31a354";
    if (value >= 40) return "#addd8e";
    if (value >= 20) return "#fdae6b";
    return "#de2d26";
}

function styleFeature(feature) {
    if (!isFeatureInCurrentFilter(feature)) {
        return {
            fillColor: "#eeeeee",
            color: "#cccccc",
            weight: 0.1,
            fillOpacity: 0.08
        };
    }

    const colorScale = valueToColorScale(feature.properties);

    return {
        fillColor: getColor(colorScale),
        color: "#333333",
        weight: 0.25,
        fillOpacity: 0.75
    };
}

function tooltipContent(properties) {
    const meta = selectedIndicatorMeta();
    const year = selectedYear();
    const rawValue = getRawIndicatorValue(properties);
    const colorScale = valueToColorScale(properties);
    const warning = benchmarkWarningText(properties);
    const rankInfo = benchmarkRankInfo(properties);

    return `
        <b>${properties.obec || "Neznámá obec"}</b><br>
        Kód obce: ${properties.kod_obce || ""}<br>
        Okres: ${properties.okres || ""}<br>
        ORP: ${properties.orp || ""}<br>
        Počet obyvatel: ${formatValue(properties.population, 0)}<br>
        Velikostní benchmark: ${benchmarkCategory(properties) || ""}<br>
        Typ sídla: ${settlementType(properties) || ""}<br>
        <hr>
        <b>${meta.label} (${year}): ${formatIndicatorValue(rawValue, meta)}</b><br>
        Pořadí v benchmarku: ${rankInfo.text}<br>
        Kontext benchmarku: ${benchmarkPositionText(properties)}<br>
        Barevná škála: ${formatValue(colorScale, 1)} / 100<br>
        ${warning ? "<br><span class='tooltip-note'>" + warning + "</span>" : ""}
        <br><span class="tooltip-note">Barva je relativní vůči podobně velkým obcím. Hodnota výše je surový údaj.</span><br>
    `;
}

let geoLayer = L.geoJSON(geoData, {
    renderer: canvasRenderer,
    style: styleFeature,
    onEachFeature: function(feature, layer) {
        layer.bindTooltip("", {
            sticky: true
        });

        layer.on("tooltipopen", function() {
            layer.setTooltipContent(tooltipContent(layer.feature.properties));
        });

        layer.on("mouseover", function() {
            if (isFeatureInCurrentFilter(feature)) {
                layer.setStyle({
                    weight: 1.5,
                    color: "#000000",
                    fillOpacity: 0.9
                });
            }
        });

        layer.on("mouseout", function() {
            if (selectedMunicipalityLayer !== layer) {
                geoLayer.resetStyle(layer);
            }
        });

        layer.on("click", function() {
            selectMunicipalityLayer(layer, true);
        });
    }
}).addTo(map);

function setFilterToMunicipalityBenchmark(properties) {
    const cat = benchmarkCategory(properties);
    const select = document.getElementById("size_filter");

    if (cat && select.value !== cat) {
        select.value = cat;
    }
}

function selectMunicipalityLayer(layer, setBenchmarkFilter = false) {
    if (selectedMunicipalityLayer) {
        geoLayer.resetStyle(selectedMunicipalityLayer);
    }

    selectedMunicipalityLayer = layer;

    if (setBenchmarkFilter) {
        setFilterToMunicipalityBenchmark(layer.feature.properties);
        updateMap(false);
    }

    layer.setStyle({
        weight: 3,
        color: "#000000",
        fillOpacity: 0.95
    });

    updateDashboard(layer.feature.properties);
}

function zoomToMunicipality() {
    const input = document.getElementById("municipality_search");
    const status = document.getElementById("search_status");
    const query = input.value;

    const feature = findMunicipalityFeature(query);

    if (!feature) {
        status.innerHTML = "Obec nenalezena. Zkus název bez překlepu nebo šestimístný kód obce.";
        return;
    }

    let foundLayer = null;

    geoLayer.eachLayer(function(layer) {
        if (
            layer.feature &&
            layer.feature.properties &&
            String(layer.feature.properties.kod_obce) === String(feature.properties.kod_obce)
        ) {
            foundLayer = layer;
        }
    });

    if (!foundLayer) {
        status.innerHTML = "Obec je v datech, ale nepodařilo se najít její geometrii.";
        return;
    }

    setFilterToMunicipalityBenchmark(feature.properties);
    updateMap(false);

    map.fitBounds(foundLayer.getBounds(), {
        maxZoom: 12
    });

    foundLayer.setTooltipContent(tooltipContent(foundLayer.feature.properties));
    foundLayer.openTooltip();
    selectMunicipalityLayer(foundLayer, false);

    status.innerHTML =
        "Nalezena obec: " +
        (feature.properties.obec || "") +
        " (" +
        (feature.properties.kod_obce || "") +
        "), benchmark: " +
        (benchmarkCategory(feature.properties) || "neuvedeno") +
        ", typ sídla: " +
        (settlementType(feature.properties) || "neuvedeno") +
        ".";
}

function updateLegend() {
    const meta = selectedIndicatorMeta();

    document.getElementById("legend_indicator_name").innerHTML = meta.label || "";

    const rows = document.getElementById("legend_rows");

    rows.innerHTML = `
        <i style="background:#006837"></i>příznivá / vysoká hodnota<br>
        <i style="background:#31a354"></i>spíše příznivá / vyšší<br>
        <i style="background:#addd8e"></i>střední hodnota<br>
        <i style="background:#fdae6b"></i>méně příznivá / nižší<br>
        <i style="background:#de2d26"></i>riziková / nízká hodnota<br>
        <i style="background:#d9d9d9"></i>bez dat / mimo filtr
    `;

    let interpretation = "";
    if (meta.direction === "DOWN") {
        interpretation = " U tohoto ukazatele je nižší surová hodnota považována za příznivější.";
    } else if (meta.direction === "UP") {
        interpretation = " U tohoto ukazatele je vyšší surová hodnota považována za příznivější.";
    } else {
        interpretation = " U kontextových ukazatelů zelená značí vyšší hodnotu v benchmarku, červená nižší hodnotu.";
    }

    document.getElementById("legend_range").innerHTML =
        "Škála je počítána z 5.–95. percentilu v rámci benchmarku pro vybraný rok." + interpretation;
}

function updateMap(refreshDashboard = true) {
    updateLegend();

    geoLayer.eachLayer(function(layer) {
        layer.setStyle(styleFeature(layer.feature));
    });

    if (selectedMunicipalityLayer) {
        selectedMunicipalityLayer.setStyle({
            weight: 3,
            color: "#000000",
            fillOpacity: 0.95
        });

        if (refreshDashboard) {
            updateDashboard(selectedMunicipalityLayer.feature.properties);
        }
    }
}

function getDiffPeriod(props, indicator) {
    return (
        props[indicator + "_diff_2024_2020"] ??
        props[indicator + "_change_2024_2020"] ??
        props[indicator + "_change_24_20"] ??
        props[indicator + "_diff_2023_2021"] ??
        props[indicator + "_change_2023_2021"] ??
        null
    );
}

function getDiffYear(props, indicator) {
    return (
        props[indicator + "_diff_2024_2023"] ??
        props[indicator + "_change_2024_2023"] ??
        props[indicator + "_change_24_23"] ??
        props[indicator + "_diff_2023_2022"] ??
        props[indicator + "_change_2023_2022"] ??
        null
    );
}

function getTrend(props, indicator) {
    if (isLandUseIndicator(indicator)) {
        return "aktuální stav";
    }

    const explicitTrend =
        props[indicator + "_trend_2020_2024"] ||
        props[indicator + "_trend_20_24"] ||
        props[indicator + "_trend_2021_2023"];

    if (explicitTrend && explicitTrend !== "bez dat") {
        return explicitTrend;
    }

    const meta = indicatorMeta[indicator] || {};

    let startValue = null;
    let endValue = null;

    if (isWasteIndicator(indicator)) {
        startValue = Number(props[indicator + "_2021"]);
        endValue = Number(props[indicator + "_2023"]);
    } else {
        startValue = Number(props[indicator + "_2020"]);
        endValue = Number(props[indicator + "_2024"]);
    }

    if (isNaN(startValue) || isNaN(endValue)) {
        return "bez dat";
    }

    const diff = endValue - startValue;
    const tolerance = Math.max(0.000001, Math.abs(startValue) * 0.001);

    if (Math.abs(diff) <= tolerance) {
        return "stabilní";
    }

    if (meta.direction === "CONTEXT") {
        return diff > 0 ? "roste" : "klesá";
    }

    if (meta.direction === "DOWN") {
        return diff < 0 ? "zlepšení" : "zhoršení";
    }

    if (meta.direction === "UP") {
        return diff > 0 ? "zlepšení" : "zhoršení";
    }

    return diff > 0 ? "roste" : "klesá";
}

function trendBadge(trend) {
    if (!trend || trend === "bez dat") {
        return '<span class="badge badge-neutral">bez dat</span>';
    }

    if (trend === "zlepšení") {
        return '<span class="badge badge-good">zlepšení</span>';
    }

    if (trend === "zhoršení") {
        return '<span class="badge badge-bad">zhoršení</span>';
    }

    return '<span class="badge badge-neutral">' + trend + '</span>';
}

function createIndicatorCards(props) {
    const container = document.getElementById("score_cards");
    const indicator = selectedIndicatorId();
    const meta = selectedIndicatorMeta();
    const year = selectedYear();

    const rawValue = getRawIndicatorValue(props);
    const diffPeriod = getDiffPeriod(props, indicator);
    const rankInfo = benchmarkRankInfo(props);
    const benchmarkText = benchmarkPositionText(props);

    const diffText = isLandUseIndicator(indicator)
        ? "statický / aktuální údaj"
        : signedValue(diffPeriod, meta.digits ?? 2);

    container.innerHTML = `
        <div class="card">
            <div class="label">Ukazatel</div>
            <div class="value" style="font-size:18px">${meta.label}</div>
            <div class="sub">${meta.description || ""}</div>
        </div>
        <div class="card">
            <div class="label">Hodnota ${year}</div>
            <div class="value">${formatIndicatorValue(rawValue, meta)}</div>
            <div class="sub">surová hodnota ve vybraném roce nebo poslední dostupný údaj</div>
        </div>
        <div class="card">
            <div class="label">Dlouhodobá změna</div>
            <div class="value" style="font-size:${isLandUseIndicator(indicator) ? "17px" : "22px"}">${diffText}</div>
            <div class="sub">v jednotce ukazatele</div>
        </div>
        <div class="card">
            <div class="label">Pozice mezi podobnými obcemi</div>
            <div class="value" style="font-size:18px">${rankInfo.text}</div>
            <div class="sub">${benchmarkText}, benchmark: ${benchmarkCategory(props) || ""}, rok ${year}</div>
        </div>
    `;
}

function createTrendTable(props) {
    const group = selectedIndicatorGroup();

    const title = document.getElementById("trend_table_title");
    if (title) {
        title.innerHTML = "Trendy: " + group.label;
    }

    function currentValueForTrendTable(props, indicator) {
        if (isWasteIndicator(indicator)) {
            return props[indicator + "_2023"] ?? props[indicator];
        }

        if (isLandUseIndicator(indicator)) {
            return props[indicator];
        }

        return props[indicator + "_2024"] ?? props[indicator];
    }

    function createIndicatorRow(indicator) {
        const meta = indicatorMeta[indicator] || {};
        const label = meta.label || indicator;
        const digits = meta.digits ?? 2;
        const unit = meta.unit || "";

        const current = currentValueForTrendTable(props, indicator);
        const diffYear = isLandUseIndicator(indicator) ? null : getDiffYear(props, indicator);
        const diffPeriod = isLandUseIndicator(indicator) ? null : getDiffPeriod(props, indicator);
        const trend = getTrend(props, indicator);

        let currentText = formatIndicatorValue(current, meta);

        let diffYearText = isLandUseIndicator(indicator) ? "—" : signedValue(diffYear, digits);
        if (diffYearText !== "bez dat" && diffYearText !== "—" && unit) {
            diffYearText += " " + unit;
        }

        let diffPeriodText = isLandUseIndicator(indicator) ? "—" : signedValue(diffPeriod, digits);
        if (diffPeriodText !== "bez dat" && diffPeriodText !== "—" && unit) {
            diffPeriodText += " " + unit;
        }

        return `
            <tr>
                <td>${label}</td>
                <td>${currentText}</td>
                <td>${diffYearText}</td>
                <td>${diffPeriodText}</td>
                <td>${trendBadge(trend)}</td>
            </tr>
        `;
    }

    let periodNote = "";
    let rows = [];

    if (selectedIndicatorGroupId() === "environment") {
        rows = ["ecological_stability_coef"];
        periodNote = `
            <div class="small-note" style="margin-bottom:10px">
                U krajiny dává jako časový trend smysl především koeficient ekologické stability.
                Katastrální ukazatele jako výměra, podíl orné půdy, lesů nebo vodních ploch jsou níže zobrazené jako statický profil území.
            </div>
        `;
    } else if (group === indicatorGroups.waste) {
        rows = group.indicators;
        periodNote = `
            <div class="small-note" style="margin-bottom:10px">
                Odpadové ukazatele jsou z VISOH2. Aktuální hodnota odpovídá poslednímu dostupnému roku,
                typicky 2023. Meziroční změna odpovídá období 2023–2022 a dlouhodobá změna období 2023–2021.
            </div>
        `;
    } else {
        rows = group.indicators;
        periodNote = `
            <div class="small-note" style="margin-bottom:10px">
                Ukazatele v této oblasti jsou zobrazeny pro období 2020–2024.
            </div>
        `;
    }

    let html = `
        <div style="margin-bottom:8px;">
            <div style="font-weight:700; font-size:15px;">${group.label}</div>
            <div class="small-note">${group.subtitle}</div>
        </div>
        ${periodNote}
        <table>
            <thead>
                <tr>
                    <th>Ukazatel</th>
                    <th>Aktuálně</th>
                    <th>Meziročně</th>
                    <th>Dlouhodobě</th>
                    <th>Trend</th>
                </tr>
            </thead>
            <tbody>
    `;

    rows.forEach(function(indicator) {
        if (indicatorMeta[indicator]) {
            html += createIndicatorRow(indicator);
        }
    });

    html += `
            </tbody>
        </table>
    `;

    document.getElementById("trend_table").innerHTML = html;
}

function agePct(value) {
    if (value === null || value === undefined || isNaN(value)) return 0;
    return Math.max(0, Math.min(100, Number(value)));
}

function createAgeStructurePanel(props) {
    const wrapper = document.getElementById("age_structure_wrapper");
    const panel = document.getElementById("age_structure_panel");

    if (selectedIndicatorGroupId() !== "demography") {
        if (wrapper) wrapper.style.display = "none";
        if (panel) panel.innerHTML = "";
        return;
    }

    if (wrapper) wrapper.style.display = "block";

    if (!hasValidPopulation(props)) {
        panel.innerHTML = `
            <div class="warning-box">
                Pro obec nejsou dostupná validní populační data. Věkovou strukturu nelze spolehlivě zobrazit.
            </div>
        `;
        return;
    }

    const childrenCount = props.children_count ?? props.children_2024;
    const workingCount = props.working_age_count ?? props.working_age_2024;
    const seniorCount = props.senior_count ?? props.seniors_2024;

    const childrenShare = props.children_share ?? props.children_share_2024;
    const workingShare = props.working_age_share ?? props.working_age_share_2024;
    const seniorShare = props.senior_share ?? props.senior_share_2024;

    const ageingIndex = props.ageing_index ?? props.ageing_index_2024;

    const childrenChange = props.children_share_change_2024_2020 ?? props.children_share_diff_2024_2020;
    const workingChange = props.working_age_share_change_2024_2020 ?? props.working_age_share_diff_2024_2020;
    const seniorChange = props.senior_share_change_2024_2020 ?? props.senior_share_diff_2024_2020;
    const ageingChange = props.ageing_index_change_2024_2020 ?? props.ageing_index_diff_2024_2020;

    const c = agePct(childrenShare);
    const w = agePct(workingShare);
    const s = agePct(seniorShare);

    const html = `
        <div class="age-bar">
            <div class="age-segment age-children" style="width:${c}%">0–14</div>
            <div class="age-segment age-working" style="width:${w}%">15–64</div>
            <div class="age-segment age-seniors" style="width:${s}%">65+</div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Skupina</th>
                    <th>Počet</th>
                    <th>Podíl 2024</th>
                    <th>Dlouhodobá změna</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Děti 0–14</td>
                    <td>${formatValue(childrenCount, 0)}</td>
                    <td>${formatValue(childrenShare, 2)} %</td>
                    <td>${signedValue(childrenChange, 2)} p. b.</td>
                </tr>
                <tr>
                    <td>Produktivní věk 15–64</td>
                    <td>${formatValue(workingCount, 0)}</td>
                    <td>${formatValue(workingShare, 2)} %</td>
                    <td>${signedValue(workingChange, 2)} p. b.</td>
                </tr>
                <tr>
                    <td>Senioři 65+</td>
                    <td>${formatValue(seniorCount, 0)}</td>
                    <td>${formatValue(seniorShare, 2)} %</td>
                    <td>${signedValue(seniorChange, 2)} p. b.</td>
                </tr>
                <tr>
                    <td><b>Index stáří</b></td>
                    <td colspan="2">${formatValue(ageingIndex, 2)} seniorů na 100 dětí</td>
                    <td>${signedValue(ageingChange, 2)} bodu</td>
                </tr>
            </tbody>
        </table>

        <p class="small-note">
            Index stáří = počet obyvatel 65+ / počet obyvatel 0–14 × 100.
            Změny podílů jsou v procentních bodech.
        </p>
    `;

    panel.innerHTML = html;
}

function createRawTable(props) {
    const group = selectedIndicatorGroup();

    const title = document.getElementById("raw_table_title");
    if (title) {
        title.innerHTML = "Surové hodnoty: " + group.label;
    }

    let html = "<table><tbody>";

    group.indicators.forEach(function(indicator) {
        const meta = indicatorMeta[indicator] || {};

        let value = null;

        if (isWasteIndicator(indicator)) {
            value = props[indicator + "_2023"] ?? props[indicator];
        } else if (isLandUseIndicator(indicator)) {
            value = props[indicator];
        } else {
            value = props[indicator + "_2024"] ?? props[indicator];
        }

        html += `
            <tr>
                <td>${meta.label || indicator}</td>
                <td>${formatIndicatorValue(value, meta)}</td>
            </tr>
        `;
    });

    html += "</tbody></table>";

    document.getElementById("raw_table").innerHTML = html;
}

function numOrNull(value) {
    if (value === null || value === undefined || value === "" || isNaN(Number(value))) {
        return null;
    }
    return Number(value);
}

function propNumber(props, key) {
    return numOrNull(props[key]);
}

function valueForDiagnostic(props, indicator, year) {
    return propNumber(props, indicator + "_" + year) ?? propNumber(props, indicator);
}

function diffForDiagnostic(props, indicator, period) {
    if (period === "2024_2020") {
        return (
            propNumber(props, indicator + "_diff_2024_2020") ??
            propNumber(props, indicator + "_change_2024_2020") ??
            propNumber(props, indicator + "_change_24_20")
        );
    }

    if (period === "2023_2021") {
        return (
            propNumber(props, indicator + "_diff_2023_2021") ??
            propNumber(props, indicator + "_change_2023_2021")
        );
    }

    if (period === "2023_2022") {
        return (
            propNumber(props, indicator + "_diff_2023_2022") ??
            propNumber(props, indicator + "_change_2023_2022")
        );
    }

    return null;
}

function wasteDiffForDiagnostic(props, indicator) {
    return diffForDiagnostic(props, indicator, "2023_2021");
}

function diagnostic(level, title, text, evidence) {
    return {
        level: level,
        title: title,
        text: text,
        evidence: evidence || []
    };
}

function evidenceText(label, valueText) {
    if (valueText === null || valueText === undefined || valueText === "" || valueText === "bez dat") {
        return null;
    }

    return label + ": " + valueText;
}

function buildCrossDomainDiagnostics(props) {
    const out = [];

    const populationDiff = diffForDiagnostic(props, "population", "2024_2020");
    const migration = valueForDiagnostic(props, "migration_balance_per_1000", 2024);

    const childrenShareDiff = diffForDiagnostic(props, "children_share", "2024_2020");
    const seniorShareDiff = diffForDiagnostic(props, "senior_share", "2024_2020");
    const ageingIndexDiff = diffForDiagnostic(props, "ageing_index", "2024_2020");

    const unemploymentDiff = diffForDiagnostic(props, "unemployment_rate", "2024_2020");

    const flats = valueForDiagnostic(props, "completed_flats_per_1000", 2024);
    const flatsDiff = diffForDiagnostic(props, "completed_flats_per_1000", "2024_2020");

    const ecoStability = valueForDiagnostic(props, "ecological_stability_coef", 2024);

    const municipalWasteDiff = wasteDiffForDiagnostic(props, "municipal_waste_kg_per_capita");
    const mixedWasteDiff = wasteDiffForDiagnostic(props, "mixed_municipal_waste_kg_per_capita");
    const separatedDiff = wasteDiffForDiagnostic(props, "separated_recyclables_kg_per_capita");
    const sortingDiff = wasteDiffForDiagnostic(props, "waste_sorting_target_share");
    const plasticEfficiencyDiff = wasteDiffForDiagnostic(props, "plastic_separation_efficiency");

    const density = propNumber(props, "population_density_per_km2");
    const builtUpShare = propNumber(props, "built_up_area_share");
    const arableShare = propNumber(props, "arable_land_share");
    const forestShare = propNumber(props, "forest_land_share");
    const naturalStableShare = propNumber(props, "natural_stable_area_share");
    const intensiveLandUseShare = propNumber(props, "intensive_land_use_share");
    const areaKm2 = propNumber(props, "municipality_area_km2");

    const populationGrowing = populationDiff !== null && populationDiff > 0;
    const populationDeclining = populationDiff !== null && populationDiff < 0;

    const migrationPositive = migration !== null && migration > 0;

    const childrenGrowing = childrenShareDiff !== null && childrenShareDiff > 0;
    const seniorsGrowing = seniorShareDiff !== null && seniorShareDiff > 0;
    const ageingGrowing = ageingIndexDiff !== null && ageingIndexDiff > 0;

    const unemploymentGrowing = unemploymentDiff !== null && unemploymentDiff > 0;

    const flatsGrowing = flatsDiff !== null && flatsDiff > 0;
    const flatsLow = flats !== null && flats < 1;
    const flatsActive = flats !== null && flats >= 1;

    const ecoVeryLow = ecoStability !== null && ecoStability < 0.3;
    const ecoLow = ecoStability !== null && ecoStability < 1.0;

    const municipalWasteGrowing = municipalWasteDiff !== null && municipalWasteDiff > 0;
    const municipalWasteDeclining = municipalWasteDiff !== null && municipalWasteDiff < 0;

    const mixedWasteGrowing = mixedWasteDiff !== null && mixedWasteDiff > 0;
    const mixedWasteDeclining = mixedWasteDiff !== null && mixedWasteDiff < 0;

    const separatedDeclining = separatedDiff !== null && separatedDiff < 0;

    const sortingDeclining = sortingDiff !== null && sortingDiff < 0;
    const sortingStableOrGrowing = sortingDiff !== null && sortingDiff >= -0.1;

    const plasticEfficiencyDeclining = plasticEfficiencyDiff !== null && plasticEfficiencyDiff < 0;

    const densityHigh = density !== null && density >= 500;
    const densityLow = density !== null && density < 30;
    const builtUpHigh = builtUpShare !== null && builtUpShare >= 8;
    const intensiveHigh = intensiveLandUseShare !== null && intensiveLandUseShare >= 70;
    const naturalLow = naturalStableShare !== null && naturalStableShare < 20;
    const forestLow = forestShare !== null && forestShare < 10;
    const arableHigh = arableShare !== null && arableShare >= 60;

    if (migrationPositive && flatsActive && !populationDeclining && !unemploymentGrowing) {
        out.push(diagnostic(
            "good",
            "Rezidenční atraktivita obce",
            "Obec má kladné migrační saldo, neklesá dlouhodobě počtem obyvatel a zároveň vykazuje bytovou výstavbu. To naznačuje rezidenční atraktivitu. Doporučeno sledovat kapacity infrastruktury, dopravu, školství a technické služby.",
            [
                evidenceText("Migrační saldo / 1000 obyv.", formatValue(migration, 2)),
                evidenceText("Dokončené byty / 1000 obyv.", formatValue(flats, 2)),
                evidenceText("Změna počtu obyvatel", signedValue(populationDiff, 0))
            ].filter(Boolean)
        ));
    }

    if (migrationPositive && flatsActive && (populationDeclining || unemploymentGrowing)) {
        out.push(diagnostic(
            "neutral",
            "Krátkodobý pozitivní signál migrace a výstavby",
            "Obec má aktuálně kladné migrační saldo a vykazuje bytovou výstavbu, ale zároveň má dlouhodobý populační pokles nebo zhoršující se nezaměstnanost. Nejde automaticky o stabilní rezidenční atraktivitu, spíše o signál možného obratu.",
            [
                evidenceText("Migrační saldo / 1000 obyv.", formatValue(migration, 2)),
                evidenceText("Dokončené byty / 1000 obyv.", formatValue(flats, 2)),
                evidenceText("Změna počtu obyvatel", signedValue(populationDiff, 0)),
                evidenceText("Změna nezaměstnanosti", signedValue(unemploymentDiff, 2) + " p. b.")
            ].filter(Boolean)
        ));
    }

    if ((populationGrowing || migrationPositive) && flatsLow) {
        out.push(diagnostic(
            "warning",
            "Populační tlak při nízké bytové výstavbě",
            "Obec populačně roste nebo má kladnou migraci, ale aktuální intenzita bytové výstavby je nízká. Může vznikat tlak na dostupnost bydlení nebo na stávající bytový fond.",
            [
                evidenceText("Změna počtu obyvatel", signedValue(populationDiff, 0)),
                evidenceText("Migrační saldo / 1000 obyv.", formatValue(migration, 2)),
                evidenceText("Dokončené byty / 1000 obyv.", formatValue(flats, 2))
            ].filter(Boolean)
        ));
    }

    if (flatsGrowing && populationDeclining) {
        out.push(diagnostic(
            "warning",
            "Výstavba bez zřejmého populačního růstu",
            "Bytová výstavba roste, ale počet obyvatel dlouhodobě klesá. Doporučeno ověřit, zda jde o rekreační bydlení, výměnu bytového fondu nebo opožděný populační efekt.",
            [
                evidenceText("Změna počtu obyvatel", signedValue(populationDiff, 0)),
                evidenceText("Změna dokončených bytů / 1000 obyv.", signedValue(flatsDiff, 2))
            ].filter(Boolean)
        ));
    }

    if (populationGrowing && municipalWasteGrowing) {
        out.push(diagnostic(
            "risk",
            "Růst obce je doprovázen vyšší produkcí odpadu na obyvatele",
            "Obec populačně roste a zároveň roste komunální odpad na obyvatele. Nejde tedy jen o efekt větší populace, ale také o vyšší intenzitu produkce odpadu.",
            [
                evidenceText("Změna počtu obyvatel", signedValue(populationDiff, 0)),
                evidenceText("Změna komunálního odpadu / obyv.", signedValue(municipalWasteDiff, 1) + " kg/obyv.")
            ].filter(Boolean)
        ));
    }

    if (
        populationGrowing &&
        municipalWasteDeclining &&
        sortingStableOrGrowing &&
        !separatedDeclining &&
        !plasticEfficiencyDeclining
    ) {
        out.push(diagnostic(
            "good",
            "Růst obce bez zhoršení odpadového profilu",
            "Obec populačně roste, ale komunální odpad na obyvatele klesá a zároveň neklesají hlavní třídicí ukazatele. To je příznivý signál efektivity odpadového systému.",
            [
                evidenceText("Změna počtu obyvatel", signedValue(populationDiff, 0)),
                evidenceText("Změna komunálního odpadu / obyv.", signedValue(municipalWasteDiff, 1) + " kg/obyv."),
                evidenceText("Změna plnění cíle třídění", signedValue(sortingDiff, 2) + " p. b."),
                evidenceText("Změna separovaných složek / obyv.", signedValue(separatedDiff, 1) + " kg/obyv."),
                evidenceText("Změna účinnosti separace plastu", signedValue(plasticEfficiencyDiff, 2) + " p. b.")
            ].filter(Boolean)
        ));
    }

    if (
        populationGrowing &&
        municipalWasteDeclining &&
        sortingStableOrGrowing &&
        (separatedDeclining || plasticEfficiencyDeclining)
    ) {
        out.push(diagnostic(
            "warning",
            "Růst obce a pokles odpadu vyžaduje kontrolu třídění",
            "Obec populačně roste a komunální odpad na obyvatele klesá, ale zároveň klesá některý z třídicích ukazatelů. Pokles odpadu proto nelze automaticky vyhodnotit jako jednoznačné zlepšení.",
            [
                evidenceText("Změna počtu obyvatel", signedValue(populationDiff, 0)),
                evidenceText("Změna komunálního odpadu / obyv.", signedValue(municipalWasteDiff, 1) + " kg/obyv."),
                evidenceText("Změna plnění cíle třídění", signedValue(sortingDiff, 2) + " p. b."),
                evidenceText("Změna separovaných složek / obyv.", signedValue(separatedDiff, 1) + " kg/obyv."),
                evidenceText("Změna účinnosti separace plastu", signedValue(plasticEfficiencyDiff, 2) + " p. b.")
            ].filter(Boolean)
        ));
    }

    if (flatsGrowing && mixedWasteGrowing) {
        out.push(diagnostic(
            "risk",
            "Výstavba může zvyšovat tlak na směsný odpad",
            "Růst bytové výstavby je doprovázen růstem směsného komunálního odpadu na obyvatele. Doporučeno ověřit zapojení nových domácností do třídění a kapacitu sběrných míst.",
            [
                evidenceText("Změna dokončených bytů / 1000 obyv.", signedValue(flatsDiff, 2)),
                evidenceText("Změna směsného komunálního odpadu / obyv.", signedValue(mixedWasteDiff, 1) + " kg/obyv.")
            ].filter(Boolean)
        ));
    }

    if ((flatsGrowing || flatsActive) && ecoVeryLow) {
        out.push(diagnostic(
            "risk",
            "Rozvoj bydlení v krajině s velmi nízkou ekologickou stabilitou",
            "Bytová výstavba probíhá v území s velmi nízkou ekologickou stabilitou. Doporučeno důsledně hlídat územní plán, zelenou infrastrukturu, retenční opatření a dopady na krajinu.",
            [
                evidenceText("Koeficient ekologické stability", formatValue(ecoStability, 4)),
                evidenceText("Dokončené byty / 1000 obyv.", formatValue(flats, 2))
            ].filter(Boolean)
        ));
    } else if ((flatsGrowing || flatsActive) && ecoLow) {
        out.push(diagnostic(
            "warning",
            "Rozvoj může vytvářet tlak na krajinu",
            "Obec vykazuje bytovou výstavbu a zároveň nižší ekologickou stabilitu. Doporučeno sledovat dopady rozvoje na krajinu, vsakování vody, zeleň a nezastavěné plochy.",
            [
                evidenceText("Koeficient ekologické stability", formatValue(ecoStability, 4)),
                evidenceText("Dokončené byty / 1000 obyv.", formatValue(flats, 2))
            ].filter(Boolean)
        ));
    }

    if ((flatsGrowing || flatsActive) && builtUpHigh) {
        out.push(diagnostic(
            "warning",
            "Výstavba v obci s vyšším podílem zastavěných ploch",
            "Obec vykazuje bytovou výstavbu a zároveň má vyšší podíl zastavěných ploch. Doporučeno hlídat další zábor území, kvalitu veřejných prostranství a kapacity technické infrastruktury.",
            [
                evidenceText("Dokončené byty / 1000 obyv.", formatValue(flats, 2)),
                evidenceText("Podíl zastavěných ploch", formatValue(builtUpShare, 2) + " %")
            ].filter(Boolean)
        ));
    }

    if ((flatsGrowing || flatsActive) && intensiveHigh) {
        out.push(diagnostic(
            "warning",
            "Rozvoj v intenzivně využívaném území",
            "Výstavba probíhá v území s vysokým podílem orné půdy a zastavěných ploch. Doporučeno zvažovat dopady na vsakování vody, zeleň, retenci a krajinnou prostupnost.",
            [
                evidenceText("Intenzivně využívané plochy", formatValue(intensiveLandUseShare, 2) + " %"),
                evidenceText("Podíl orné půdy", formatValue(arableShare, 2) + " %"),
                evidenceText("Podíl zastavěných ploch", formatValue(builtUpShare, 2) + " %")
            ].filter(Boolean)
        ));
    }

    if (ecoLow && naturalLow) {
        out.push(diagnostic(
            "risk",
            "Nízká ekologická stabilita a málo přírodně stabilnějších ploch",
            "Obec má nízkou ekologickou stabilitu a současně nízký podíl lesů, trvalých travních porostů a vodních ploch. Doporučeno prioritně řešit krajinná a retenční opatření.",
            [
                evidenceText("Koeficient ekologické stability", formatValue(ecoStability, 4)),
                evidenceText("Přírodně stabilnější plochy", formatValue(naturalStableShare, 2) + " %")
            ].filter(Boolean)
        ));
    }

    if (arableHigh && forestLow) {
        out.push(diagnostic(
            "warning",
            "Převaha orné půdy při nízkém podílu lesů",
            "Území obce je výrazně zemědělsky využívané a má nízký podíl lesní půdy. Doporučeno sledovat erozi, retenci vody, větrolamy, remízky a zelenou infrastrukturu.",
            [
                evidenceText("Podíl orné půdy", formatValue(arableShare, 2) + " %"),
                evidenceText("Podíl lesní půdy", formatValue(forestShare, 2) + " %")
            ].filter(Boolean)
        ));
    }

    if (densityHigh) {
        out.push(diagnostic(
            "warning",
            "Vyšší hustota obyvatel a tlak na infrastrukturu",
            "Obec má vyšší hustotu obyvatel. Doporučeno sledovat kapacity dopravy, parkování, školství, veřejných prostranství, zeleně a technické infrastruktury.",
            [
                evidenceText("Hustota obyvatel", formatValue(density, 1) + " obyv./km²"),
                evidenceText("Výměra obce", formatValue(areaKm2, 2) + " km²")
            ].filter(Boolean)
        ));
    }

    if (densityLow && areaKm2 !== null && areaKm2 >= 10) {
        out.push(diagnostic(
            "neutral",
            "Nízká hustota obyvatel a nákladnost obsluhy území",
            "Obec má nízkou hustotu obyvatel na relativně rozsáhlém území. To může zvyšovat jednotkové náklady na infrastrukturu, údržbu komunikací, svoz odpadu a dostupnost služeb.",
            [
                evidenceText("Hustota obyvatel", formatValue(density, 1) + " obyv./km²"),
                evidenceText("Výměra obce", formatValue(areaKm2, 2) + " km²")
            ].filter(Boolean)
        ));
    }

    if (populationGrowing && childrenGrowing) {
        out.push(diagnostic(
            "warning",
            "Růst dětské složky populace",
            "Obec roste a zároveň roste podíl dětí. Doporučeno sledovat kapacity mateřské školy, základní školy, volnočasových aktivit, hřišť a bezpečné dopravy.",
            [
                evidenceText("Změna počtu obyvatel", signedValue(populationDiff, 0)),
                evidenceText("Změna podílu dětí", signedValue(childrenShareDiff, 2) + " p. b.")
            ].filter(Boolean)
        ));
    }

    if (seniorsGrowing || ageingGrowing) {
        out.push(diagnostic(
            "warning",
            "Stárnutí populace",
            "Obec vykazuje známky stárnutí populace. Doporučeno plánovat dostupnost zdravotních a sociálních služeb, bezbariérovost, komunitní péči a dopravní obslužnost.",
            [
                evidenceText("Změna podílu seniorů", signedValue(seniorShareDiff, 2) + " p. b."),
                evidenceText("Změna indexu stáří", signedValue(ageingIndexDiff, 2))
            ].filter(Boolean)
        ));
    }

    if (populationGrowing && seniorsGrowing) {
        out.push(diagnostic(
            "warning",
            "Obec roste, ale zároveň stárne",
            "Růst obce nemusí znamenat pouze příliv mladých domácností. Vedle školských kapacit je vhodné plánovat také služby pro seniory.",
            [
                evidenceText("Změna počtu obyvatel", signedValue(populationDiff, 0)),
                evidenceText("Změna podílu seniorů", signedValue(seniorShareDiff, 2) + " p. b.")
            ].filter(Boolean)
        ));
    }

    if (unemploymentGrowing && populationDeclining) {
        out.push(diagnostic(
            "risk",
            "Riziko sociálně-ekonomického oslabování",
            "Obec kombinuje populační úbytek a zhoršující se nezaměstnanost. To může signalizovat slabší atraktivitu obce nebo strukturální problém trhu práce.",
            [
                evidenceText("Změna počtu obyvatel", signedValue(populationDiff, 0)),
                evidenceText("Změna nezaměstnanosti", signedValue(unemploymentDiff, 2) + " p. b.")
            ].filter(Boolean)
        ));
    }

    if (municipalWasteDeclining && mixedWasteDeclining && sortingStableOrGrowing && !separatedDeclining) {
        out.push(diagnostic(
            "good",
            "Kvalitativně příznivý vývoj odpadu",
            "Celkový komunální odpad i směsný komunální odpad klesají a třídění se nezhoršuje. To naznačuje skutečné zlepšení odpadového hospodářství.",
            [
                evidenceText("Změna komunálního odpadu / obyv.", signedValue(municipalWasteDiff, 1) + " kg/obyv."),
                evidenceText("Změna směsného komunálního odpadu / obyv.", signedValue(mixedWasteDiff, 1) + " kg/obyv."),
                evidenceText("Změna plnění cíle třídění", signedValue(sortingDiff, 2) + " p. b.")
            ].filter(Boolean)
        ));
    }

    if (municipalWasteDeclining && (separatedDeclining || sortingDeclining || plasticEfficiencyDeclining)) {
        out.push(diagnostic(
            "warning",
            "Pokles odpadu nemusí být jednoznačně pozitivní",
            "Komunální odpad klesá, ale zároveň klesají tříděné složky, plnění cíle třídění nebo účinnost separace. Doporučeno ověřit skladbu odpadu.",
            [
                evidenceText("Změna komunálního odpadu / obyv.", signedValue(municipalWasteDiff, 1) + " kg/obyv."),
                evidenceText("Změna separovaných složek / obyv.", signedValue(separatedDiff, 1) + " kg/obyv."),
                evidenceText("Změna plnění cíle třídění", signedValue(sortingDiff, 2) + " p. b."),
                evidenceText("Změna účinnosti separace plastu", signedValue(plasticEfficiencyDiff, 2) + " p. b.")
            ].filter(Boolean)
        ));
    }

    if (municipalWasteGrowing && mixedWasteGrowing) {
        out.push(diagnostic(
            "risk",
            "Roste celkový i směsný komunální odpad",
            "Současný růst celkového a směsného komunálního odpadu ukazuje na potřebu řešit prevenci vzniku odpadu, třídění a nastavení svozového systému.",
            [
                evidenceText("Změna komunálního odpadu / obyv.", signedValue(municipalWasteDiff, 1) + " kg/obyv."),
                evidenceText("Změna směsného komunálního odpadu / obyv.", signedValue(mixedWasteDiff, 1) + " kg/obyv.")
            ].filter(Boolean)
        ));
    }

    if (out.length === 0) {
        out.push(diagnostic(
            "neutral",
            "Bez jednoznačného mezioblastního signálu",
            "Z dostupných ukazatelů není patrná silná kombinace rizika ani příležitosti. Doporučeno sledovat jednotlivé oblasti samostatně a postupně doplnit další územní a socioekonomická data.",
            []
        ));
    }

    const priority = {
        risk: 1,
        warning: 2,
        good: 3,
        neutral: 4
    };

    out.sort(function(a, b) {
        return (priority[a.level] || 9) - (priority[b.level] || 9);
    });

    return out;
}

function diagnosticBadgeClass(level) {
    if (level === "good") return "badge-good";
    if (level === "risk") return "badge-bad";
    if (level === "warning") return "badge-bad";
    return "badge-neutral";
}

function diagnosticLabel(level) {
    if (level === "good") return "Příznivý signál";
    if (level === "risk") return "Riziko";
    if (level === "warning") return "Upozornění";
    return "Kontext";
}

function diagnosticKey(item) {
    if (!item || !item.title) return "";
    return String(item.title)
        .toLowerCase()
        .normalize("NFD")
        .replace(/[\\u0300-\\u036f]/g, "")
        .replace(/\\s+/g, " ")
        .trim();
}

function diagnosticSeverityScore(item) {
    const levelScore = {
        risk: 1000,
        warning: 700,
        good: 300,
        neutral: 100
    };

    let score = levelScore[item.level] || 0;

    const title = item.title || "";

    if (title.includes("sociálně-ekonomického oslabování")) score += 250;
    if (title.includes("Nízká ekologická stabilita")) score += 220;
    if (title.includes("Rozvoj bydlení v krajině")) score += 210;
    if (title.includes("Roste celkový i směsný komunální odpad")) score += 210;
    if (title.includes("Pokles odpadu nemusí být jednoznačně pozitivní")) score += 190;
    if (title.includes("Výstavba může zvyšovat tlak na směsný odpad")) score += 180;
    if (title.includes("Výstavba bez zřejmého populačního růstu")) score += 170;
    if (title.includes("Populační tlak při nízké bytové výstavbě")) score += 160;
    if (title.includes("Převaha orné půdy")) score += 140;
    if (title.includes("Stárnutí populace")) score += 130;
    if (title.includes("Růst dětské složky populace")) score += 120;
    if (title.includes("Obec roste, ale zároveň stárne")) score += 110;

    if (item.evidence && item.evidence.length) {
        score += Math.min(60, item.evidence.length * 15);
    }

    return score;
}

function uniqueDiagnostics(items) {
    const seen = new Set();
    const out = [];

    items.forEach(function(item) {
        const key = diagnosticKey(item);

        if (!key || seen.has(key)) return;

        seen.add(key);
        out.push(item);
    });

    return out;
}

function priorityActionForDiagnostic(item) {
    const title = item.title || "";

    if (title.includes("sociálně-ekonomického oslabování")) {
        return "Prověřit příčiny populačního úbytku a růstu nezaměstnanosti; zaměřit se na dostupnost práce, dopravní napojení a atraktivitu obce pro domácnosti.";
    }

    if (title.includes("Výstavba bez zřejmého populačního růstu")) {
        return "Ověřit charakter nové výstavby: trvalé bydlení, rekreační bydlení, výměna bytového fondu nebo opožděný populační efekt.";
    }

    if (title.includes("Stárnutí populace")) {
        return "Plánovat služby pro seniory, bezbariérovost, komunitní péči, dostupnost zdravotních služeb a dopravní obslužnost.";
    }

    if (title.includes("Pokles odpadu nemusí být jednoznačně pozitivní")) {
        return "Zkontrolovat skladbu odpadu: směsný komunální odpad, separované složky, bioodpad, plnění cíle třídění a účinnost separace.";
    }

    if (title.includes("Roste celkový i směsný komunální odpad")) {
        return "Zaměřit se na prevenci vzniku odpadu, třídění, kapacitu sběrných míst a nastavení svozového systému.";
    }

    if (title.includes("Výstavba může zvyšovat tlak na směsný odpad")) {
        return "Ověřit, zda nové domácnosti mají dostatečný přístup ke třídění a zda sběrná infrastruktura odpovídá nové výstavbě.";
    }

    if (title.includes("Populační tlak při nízké bytové výstavbě")) {
        return "Prověřit dostupnost bydlení, územní plán, kapacity infrastruktury a tlak na stávající bytový fond.";
    }

    if (title.includes("Růst dětské složky populace")) {
        return "Zkontrolovat kapacity mateřské školy, základní školy, volnočasových aktivit, hřišť a bezpečné dopravy.";
    }

    if (title.includes("Rozvoj bydlení v krajině") || title.includes("Rozvoj může vytvářet tlak na krajinu")) {
        return "Při rozvoji hlídat územní plán, zelenou infrastrukturu, vsakování vody, retenční opatření a ochranu nezastavěných ploch.";
    }

    if (title.includes("Výstavba v obci s vyšším podílem zastavěných ploch")) {
        return "Ověřit, zda další výstavba nezvyšuje tlak na infrastrukturu, veřejná prostranství, parkování, zeleň a hospodaření s dešťovou vodou.";
    }

    if (title.includes("Rozvoj v intenzivně využívaném území")) {
        return "Při rozvojových plochách posílit zelenou infrastrukturu, vsakování, retenční prvky, krajinnou prostupnost a protierozní opatření.";
    }

    if (title.includes("Nízká ekologická stabilita")) {
        return "Prioritizovat krajinná a retenční opatření: remízky, aleje, travní pásy, mokřady, tůně, zasakovací prvky a ochranu stabilnějších ploch.";
    }

    if (title.includes("Převaha orné půdy")) {
        return "Prověřit erozní ohrožení, odtokové poměry, retenci vody a možnosti doplnění krajinné zeleně.";
    }

    if (title.includes("Vyšší hustota obyvatel")) {
        return "Zkontrolovat kapacity dopravy, parkování, školství, veřejných prostranství, zeleně a technické infrastruktury.";
    }

    if (title.includes("Nízká hustota obyvatel")) {
        return "Vyhodnotit náklady obsluhy území: komunikace, veřejné osvětlení, svoz odpadu, dopravu a dostupnost služeb.";
    }

    if (title.includes("Krátkodobý pozitivní signál migrace a výstavby")) {
        return "Sledovat, zda se kladná migrace a výstavba projeví i ve stabilizaci počtu obyvatel v dalších letech.";
    }

    return item.text || "Ověřit tento signál v detailu a porovnat jej s benchmarkem podobně velkých obcí.";
}

function buildMayorPriorities(props) {
    const diagnostics = uniqueDiagnostics(buildCrossDomainDiagnostics(props));

    const priorities = diagnostics.map(function(item) {
        return {
            level: item.level,
            title: item.title,
            action: priorityActionForDiagnostic(item),
            evidence: item.evidence || [],
            score: diagnosticSeverityScore(item)
        };
    });

    priorities.sort(function(a, b) {
        return b.score - a.score;
    });

    return priorities.slice(0, 5);
}

function createMayorPrioritiesPanel(props) {
    const container = document.getElementById("mayor_priorities");
    if (!container) return;

    const priorities = buildMayorPriorities(props);

    let html = "";

    priorities.forEach(function(item, index) {
        const evidenceHtml = item.evidence && item.evidence.length
            ? `
                <ul style="margin-top:6px; padding-left:18px;">
                    ${item.evidence.slice(0, 3).map(function(e) {
                        return "<li>" + e + "</li>";
                    }).join("")}
                </ul>
            `
            : "";

        html += `
            <div class="diagnostic-item">
                <span class="badge ${diagnosticBadgeClass(item.level)}">
                    ${index + 1}. ${diagnosticLabel(item.level)}
                </span>
                <b>${item.title}</b>
                <div class="diagnostic-text">
                    ${item.action}
                </div>
                ${evidenceHtml}
            </div>
        `;
    });

    container.innerHTML = html;
}

function createCrossDomainDiagnosticsPanel(props) {
    const container = document.getElementById("cross_domain_diagnostics");
    if (!container) return;

    const diagnostics = uniqueDiagnostics(buildCrossDomainDiagnostics(props));
    const priorities = buildMayorPriorities(props);

    const priorityKeys = new Set(
        priorities.map(function(item) {
            return diagnosticKey(item);
        })
    );

    const remainingDiagnostics = diagnostics.filter(function(item) {
        return !priorityKeys.has(diagnosticKey(item));
    });

    let html = "";

    if (remainingDiagnostics.length === 0) {
        html = `
            <div class="diagnostic-item">
                <span class="badge badge-neutral">Shrnutí</span>
                <b>Hlavní signály jsou již uvedeny v prioritách</b>
                <div class="diagnostic-text">
                    Automatická diagnostika nenašla další významné souvislosti mimo prioritní body výše.
                    Detailní interpretaci proto doporučujeme opřít hlavně o sekci „Priority pro starostu“,
                    trendovou tabulku a surové hodnoty vybrané oblasti.
                </div>
            </div>
        `;

        container.innerHTML = html;
        return;
    }

    remainingDiagnostics.slice(0, 8).forEach(function(item) {
        const evidenceHtml = item.evidence && item.evidence.length
            ? `
                <ul style="margin-top:6px; padding-left:18px;">
                    ${item.evidence.map(function(e) {
                        return "<li>" + e + "</li>";
                    }).join("")}
                </ul>
            `
            : "";

        html += `
            <div class="diagnostic-item">
                <span class="badge ${diagnosticBadgeClass(item.level)}">
                    ${diagnosticLabel(item.level)}
                </span>
                <b>${item.title}</b>
                <div class="diagnostic-text">
                    ${item.text}
                </div>
                ${evidenceHtml}
            </div>
        `;
    });

    container.innerHTML = html;
}

function createBusinessSummary(props) {
    const indicator = selectedIndicatorId();
    const meta = selectedIndicatorMeta();
    const year = selectedYear();

    const value = getRawIndicatorValue(props);
    const diffPeriod = getDiffPeriod(props, indicator);
    const trend = getTrend(props, indicator);
    const benchmarkText = benchmarkPositionText(props);
    const benchmarkWarning = benchmarkWarningText(props);
    const rankInfo = benchmarkRankInfo(props);

    let sourceText = "";

    if (isWasteIndicator(indicator)) {
        sourceText = "Odpadové ukazatele jsou z VISOH2 a jsou dostupné za období 2021–2023.";
    } else if (isLandUseIndicator(indicator)) {
        sourceText = "Ukazatel využití území je stavový údaj z ČSÚ/MOS a ČÚZK, typicky za poslední dostupný rok 2024. Nejde o klasický trendový ukazatel.";
    } else {
        sourceText = "Ukazatel je z hlavních obecních dat a je dostupný typicky za období 2020–2024.";
    }

    const diffText = isLandUseIndicator(indicator)
        ? "statický / aktuální údaj"
        : signedValue(diffPeriod, meta.digits ?? 2);

    let text = `
        Obec <b>${props.obec || "vybraná obec"}</b> je zobrazena podle ukazatele
        <b>${meta.label}</b>.
        <br><br>
        Zobrazená hodnota pro rok <b>${year}</b> nebo poslední dostupný rok je
        <b>${formatIndicatorValue(value, meta)}</b>.
        Dlouhodobá změna je <b>${diffText}</b>.
        Trend je ${trendBadge(trend)}.
        <br><br>
        V benchmarku <b>${benchmarkCategory(props) || "neuvedeno"}</b> je obec na pozici:
        <b>${rankInfo.text}</b>.
        Kontextově jde o: <b>${benchmarkText}</b>.
        <br><br>
        ${sourceText}
    `;

    if (benchmarkWarning) {
        text += `
            <br><br>
            <span class="badge badge-neutral">Benchmark</span>
            ${benchmarkWarning}
        `;
    }

    if (props.volatility_warning) {
        text += `
            <br><br>
            <span class="badge badge-neutral">Interpretační upozornění</span>
            ${props.volatility_warning}
        `;
    }

    document.getElementById("business_summary").innerHTML = text;
}

function trendValues(props, indicator) {
    if (indicatorRequiresPopulation(indicator) && !hasValidPopulation(props)) {
        return chartYearsForIndicator(indicator).map(function() {
            return null;
        });
    }

    return chartYearsForIndicator(indicator).map(function(year) {
        const value = props[indicator + "_" + year];
        if (value === null || value === undefined || isNaN(value)) return null;
        return Number(value);
    });
}

function chartYearsForIndicator(indicator) {
    if (isWasteIndicator(indicator)) return wasteYears;
    return allYears;
}

function destroyCharts() {
    Object.keys(charts).forEach(function(key) {
        if (charts[key]) {
            charts[key].destroy();
        }
    });
    charts = {};
}

function makeLineChart(canvasId, label, values, yearsForChart, meta = {}) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return;

    const yAxisTitle = meta.unit ? `${label} (${meta.unit})` : label;

    charts[canvasId] = new Chart(ctx, {
        type: "line",
        data: {
            labels: yearsForChart.map(String),
            datasets: [{
                label: label,
                data: values,
                borderWidth: 2,
                tension: 0.25,
                pointRadius: 4,
                spanGaps: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: false,
            interaction: {
                mode: "index",
                intersect: false
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const value = context.parsed.y;
                            if (value === null || value === undefined || isNaN(value)) {
                                return label + ": bez dat";
                            }
                            return label + ": " + formatIndicatorValue(value, meta);
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: "Rok"
                    }
                },
                y: {
                    beginAtZero: false,
                    title: {
                        display: true,
                        text: yAxisTitle
                    },
                    ticks: {
                        callback: function(value) {
                            return Number(value).toLocaleString("cs-CZ");
                        }
                    }
                }
            }
        }
    });
}

function chartIndicatorListForSelectedGroup() {
    if (selectedIndicatorGroupId() === "environment") {
        return ["ecological_stability_coef"];
    }

    return selectedIndicatorGroup().indicators;
}

function updateCharts(props) {
    destroyCharts();

    const grid = document.getElementById("charts_grid");
    if (!grid) return;

    const indicators = chartIndicatorListForSelectedGroup();

    grid.innerHTML = "";

    indicators.forEach(function(indicator, index) {
        const meta = indicatorMeta[indicator];
        if (!meta) return;

        const canvasId = "chart_dynamic_" + index + "_" + indicator;

        grid.innerHTML += `
            <div class="chart-card">
                <h3>${meta.label}</h3>
                <div class="chart-wrap"><canvas id="${canvasId}"></canvas></div>
            </div>
        `;
    });

    indicators.forEach(function(indicator, index) {
        const meta = indicatorMeta[indicator];
        if (!meta) return;

        const canvasId = "chart_dynamic_" + index + "_" + indicator;
        const yearsForChart = chartYearsForIndicator(indicator);
        const values = trendValues(props, indicator);

        makeLineChart(canvasId, meta.label, values, yearsForChart, meta);
    });
}

function landBar(label, value, digits = 2) {
    const safeValue = value === null || value === undefined || isNaN(Number(value)) ? null : Number(value);
    const width = safeValue === null ? 0 : Math.max(0, Math.min(100, safeValue));

    return `
        <div class="land-bar-row">
            <div>${label}</div>
            <div class="land-bar-outer">
                <div class="land-bar-inner" style="width:${width}%"></div>
            </div>
            <div>${safeValue === null ? "bez dat" : formatValue(safeValue, digits) + " %"}</div>
        </div>
    `;
}

function classifyKES(kes) {
    if (kes === null || kes === undefined || isNaN(Number(kes))) {
        return {
            label: "bez dat",
            text: "Pro koeficient ekologické stability nejsou dostupná data.",
            className: "badge-neutral"
        };
    }

    const value = Number(kes);

    if (value < 0.10) {
        return {
            label: "maximálně narušené území",
            text: "Území má velmi nízký ekostabilizační potenciál. Základní ekologické funkce musí být intenzivně nahrazovány technickými zásahy.",
            className: "badge-bad"
        };
    }

    if (value < 0.30) {
        return {
            label: "nadprůměrně využívané území",
            text: "Území je nadprůměrně využívané se zřetelným narušením přírodních struktur.",
            className: "badge-bad"
        };
    }

    if (value < 1.00) {
        return {
            label: "intenzivně využívané území",
            text: "Území je intenzivně využívané. Ekosystémy jsou ekologicky labilnější a vyžadují vyšší dodatkové vstupy.",
            className: "badge-bad"
        };
    }

    if (value < 3.00) {
        return {
            label: "vcelku vyvážená krajina",
            text: "Krajina je vcelku vyvážená a technické objekty jsou relativně v souladu s dochovanými přírodními strukturami.",
            className: "badge-good"
        };
    }

    return {
        label: "přírodní nebo přírodě blízká krajina",
        text: "Území má výraznou převahu ekologicky stabilních struktur a nízkou intenzitu využívání krajiny člověkem.",
        className: "badge-good"
    };
}

function createLandProfilePanel(props) {
    const panel = document.getElementById("land_profile_panel");
    const content = document.getElementById("land_profile_content");

    if (!panel || !content) return;

    if (selectedIndicatorGroupId() !== "environment") {
        panel.style.display = "none";
        content.innerHTML = "";
        return;
    }

    panel.style.display = "block";

    const area = propNumber(props, "municipality_area_km2");
    const density = propNumber(props, "population_density_per_km2");

    const built = propNumber(props, "built_up_area_share");
    const arable = propNumber(props, "arable_land_share");
    const forest = propNumber(props, "forest_land_share");
    const grass = propNumber(props, "permanent_grassland_share");
    const water = propNumber(props, "water_area_share");
    const agricultural = propNumber(props, "agricultural_land_share");
    const stable = propNumber(props, "natural_stable_area_share");
    const intensive = propNumber(props, "intensive_land_use_share");
    const kes = propNumber(props, "ecological_stability_coef");
    const kesClass = classifyKES(kes);

    let interpretation = "";

    if (kes !== null && kes < 1) {
        interpretation += "Koeficient ekologické stability ukazuje intenzivně využívanou nebo labilnější krajinnou strukturu. ";
    } else if (kes !== null && kes >= 1) {
        interpretation += "Koeficient ekologické stability ukazuje příznivější krajinnou strukturu. ";
    }

    if (arable !== null && arable >= 60) {
        interpretation += "Výrazný podíl orné půdy naznačuje potřebu sledovat erozi, retenci vody a krajinnou zeleň. ";
    }

    if (forest !== null && forest < 10) {
        interpretation += "Nízký podíl lesní půdy omezuje přirozené stabilizační funkce krajiny. ";
    }

    if (stable !== null && stable < 20) {
        interpretation += "Nízký podíl přírodně stabilnějších ploch zvyšuje význam remízků, travních pásů, alejí, mokřadů a dalších retenčních opatření. ";
    }

    if (intensive !== null && intensive >= 70) {
        interpretation += "Vysoký podíl intenzivně využívaných ploch může zvyšovat tlak na vsakování vody, mikroklima a krajinnou prostupnost. ";
    }

    if (!interpretation) {
        interpretation = "Územní profil nevykazuje extrémní hodnoty podle jednoduchých prahů. Přesto je vhodné sledovat vztah výstavby, zeleně, retence vody a zemědělského využití území.";
    }

    content.innerHTML = `
        <div class="land-profile-grid">
            <div>
                <div class="cards" style="grid-template-columns: repeat(2, minmax(140px, 1fr)); margin-top:0;">
                    <div class="card">
                        <div class="label">Výměra obce</div>
                        <div class="value">${formatValue(area, 2)} km²</div>
                        <div class="sub">stavový údaj</div>
                    </div>
                    <div class="card">
                        <div class="label">Hustota obyvatel</div>
                        <div class="value">${formatValue(density, 1)}</div>
                        <div class="sub">obyv./km²</div>
                    </div>
                    <div class="card">
                        <div class="label">Koeficient ekologické stability</div>
                        <div class="value">${formatValue(kes, 4)}</div>
                        <div class="sub">${kesClass.label}</div>
                    </div>
                    <div class="card">
                        <div class="label">Přírodně stabilnější plochy</div>
                        <div class="value">${formatValue(stable, 2)} %</div>
                        <div class="sub">lesy + TTP + vodní plochy</div>
                    </div>
                </div>
            </div>

            <div class="land-profile-bars">
                ${landBar("Zemědělská půda", agricultural)}
                ${landBar("Orná půda", arable)}
                ${landBar("Lesní půda", forest)}
                ${landBar("Trvalé travní porosty", grass)}
                ${landBar("Vodní plochy", water)}
                ${landBar("Zastavěné plochy", built)}
                ${landBar("Intenzivně využívané plochy", intensive)}
                ${landBar("Přírodně stabilnější plochy", stable)}
            </div>
        </div>

        <div class="land-summary-box" style="margin-top:14px;">
            <b>Interpretace územního profilu:</b><br>
            <span class="badge ${kesClass.className}">KES: ${kesClass.label}</span>
            <br><br>
            ${kesClass.text}
            <br><br>
            ${interpretation}
            <br><br>
            <span class="small-note">
                KES je poměr ekologicky příznivých ploch vůči plochám zatěžujícím životní prostředí.
                Jde o orientační indikátor krajinné stability; jeho přesnost závisí na údajích katastru nemovitostí
                a změny využití území jsou obvykle pomalé.
            </span>
        </div>
    `;
}

function updateDashboardWarning(props) {
    const warningBox = document.getElementById("dash_warning");

    if (!hasValidPopulation(props)) {
        warningBox.innerHTML = `
            <div class="warning-box">
                ⚠ Pro obec nejsou dostupná validní populační data. Ukazatele přepočtené na obyvatele,
                věková struktura a některé trendy nejsou spolehlivě interpretovatelné.
            </div>
        `;
        return;
    }

    if (props.volatility_warning) {
        warningBox.innerHTML = `
            <div class="warning-box">
                ⚠ ${props.volatility_warning}
            </div>
        `;
        return;
    }

    warningBox.innerHTML = "";
}

function updateDashboard(props) {
    document.getElementById("dash_title").innerHTML = "Rozvojový přehled: " + (props.obec || "obec");
    document.getElementById("dash_subtitle").innerHTML =
        "Kód obce: " + (props.kod_obce || "") +
        " | Okres: " + (props.okres || "") +
        " | ORP: " + (props.orp || "") +
        " | Benchmark: " + (benchmarkCategory(props) || "") +
        " | Typ sídla: " + (settlementType(props) || "");

    updateDashboardWarning(props);
    createIndicatorCards(props);
    createTrendTable(props);
    createLandProfilePanel(props);
    createMayorPrioritiesPanel(props);
    createCrossDomainDiagnosticsPanel(props);
    createAgeStructurePanel(props);
    createRawTable(props);
    createBusinessSummary(props);
    updateCharts(props);
}

function initializeDashboard() {
    fillSizeFilter();
    fillMunicipalitySearch();

    document.getElementById("indicator_group").value = "waste";
    fillIndicatorSelectForGroup("waste");
    document.getElementById("year_select").value = "2023";

    updateLegend();

    document.getElementById("indicator_group").addEventListener("change", function() {
        const group = indicatorGroups[this.value] || indicatorGroups.waste;
        fillIndicatorSelectForGroup(this.value);
        document.getElementById("year_select").value = group.defaultYear || "2024";
        updateMap(true);
    });

    document.getElementById("mode").addEventListener("change", function() {
        updateMap(true);
    });

    document.getElementById("size_filter").addEventListener("change", function() {
        updateMap(true);
    });

    document.getElementById("year_select").addEventListener("change", function() {
        updateMap(true);
    });

    document.getElementById("municipality_search").addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            zoomToMunicipality();
        }
    });

    const defaultFeature = findMunicipalityFeature("540480");

    if (defaultFeature) {
        let defaultLayer = null;

        geoLayer.eachLayer(function(layer) {
            if (String(layer.feature.properties.kod_obce) === "540480") {
                defaultLayer = layer;
            }
        });

        if (defaultLayer) {
            setFilterToMunicipalityBenchmark(defaultLayer.feature.properties);
            updateMap(false);
            selectMunicipalityLayer(defaultLayer, false);
        } else {
            updateDashboard(defaultFeature.properties);
        }
    }
}

initializeDashboard();
</script>
</body>
</html>
"""

    html = html_template.replace("__GEOJSON_DATA__", geojson_json)
    html = html.replace("__INDICATOR_META__", indicator_meta_json)

    return html


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    gdf = prepare_data()

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    html = generate_html(gdf)
    OUTPUT_PATH.write_text(html, encoding="utf-8")

    size_mb = OUTPUT_PATH.stat().st_size / (1024 * 1024)

    print(f"[OK] Interaktivní mapa s rozvojovým dashboardem uložena: {OUTPUT_PATH}")
    print(f"[INFO] Velikost souboru: {size_mb:.1f} MB")

    if FAST_DEMO_MODE:
        print(
            "[INFO] FAST_DEMO_MODE=True: výstup je optimalizovaný pro živou ukázku "
            f"se zjednodušením geometrie {GEOMETRY_SIMPLIFY_TOLERANCE_METERS} m."
        )
    else:
        print("[INFO] FAST_DEMO_MODE=False: výstup používá plnou geometrii.")

    print("")
    print("Otevření na macOS:")
    print(f"open {OUTPUT_PATH}")


if __name__ == "__main__":
    main()