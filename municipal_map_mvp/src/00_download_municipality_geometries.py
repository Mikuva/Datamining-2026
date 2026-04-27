#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
00_download_municipality_geometries.py

Jednorázové stažení hranic obcí ČR do lokálního GeoJSON souboru.

Výstup:
    municipal_map_mvp/data/geo/municipalities.geojson

Tento soubor potom používá:
    09_generate_interactive_map.py

Smysl:
- hranice obcí nestahujeme při každém generování mapy,
- stáhneme je jednou,
- potom už mapy vznikají rychle z lokálního souboru.
"""

from pathlib import Path
import requests
import geopandas as gpd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GEO_DIR = PROJECT_ROOT / "data" / "geo"
OUTPUT_PATH = GEO_DIR / "municipalities.geojson"


BASE_URL = "https://gis.izscr.cz/arcgis/rest/services/terinos_sluzby/cez_test/MapServer/3/query"


def download_municipality_geometries(force: bool = False) -> Path:
    GEO_DIR.mkdir(parents=True, exist_ok=True)

    if OUTPUT_PATH.exists() and not force:
        print(f"[OK] GeoJSON už existuje, stahování přeskočeno: {OUTPUT_PATH}")
        return OUTPUT_PATH

    all_features = []
    offset = 0
    chunk_size = 1000

    print("[INFO] Stahuji hranice obcí ČR...")

    while True:
        params = {
            "where": "1=1",
            "outFields": "kod_obec_p,naz_obec_p",
            "resultOffset": offset,
            "resultRecordCount": chunk_size,
            "f": "geojson",
            "outSR": "4326",
        }

        response = requests.get(BASE_URL, params=params, timeout=90)
        response.raise_for_status()

        data = response.json()
        features = data.get("features", [])

        if not features:
            break

        all_features.extend(features)
        print(f"[INFO] Staženo geometrií: {len(all_features)}")

        offset += chunk_size

    if not all_features:
        raise RuntimeError("Nepodařilo se stáhnout žádné geometrie obcí.")

    print("[INFO] Převádím na GeoDataFrame...")

    gdf = gpd.GeoDataFrame.from_features(all_features, crs="EPSG:4326")

    if "kod_obec_p" not in gdf.columns:
        raise RuntimeError(f"Ve stažených datech chybí kod_obec_p. Sloupce: {list(gdf.columns)}")

    gdf["kod_obce"] = gdf["kod_obec_p"].astype(str).str.strip()

    if "naz_obec_p" in gdf.columns:
        gdf["obec_geo"] = gdf["naz_obec_p"].astype(str)

    print(f"[INFO] Ukládám GeoJSON: {OUTPUT_PATH}")
    gdf.to_file(OUTPUT_PATH, driver="GeoJSON")

    print(f"[OK] Hotovo. Uloženo {len(gdf)} obcí.")
    return OUTPUT_PATH


if __name__ == "__main__":
    download_municipality_geometries(force=False)