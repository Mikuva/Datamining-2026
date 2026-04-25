#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
01_download_data.py

Účel skriptu
------------
Tento skript připravuje vstupní datovou vrstvu projektu
"Datová mapa kvality a rozvoje obcí ČR".

Co skript dělá:
1. vytvoří potřebné složky v data/raw/, data/processed/ a data/geo/,
2. stáhne veřejně dostupné datové soubory ČSÚ MOS, pokud jsou dostupné přes URL,
3. uloží je beze změny do data/raw/,
4. pokusí se stáhnout katalog ČSÚ DataStat přes lokální pyczso.py, pokud je dostupný,
5. ověří dostupnost LKOD/VDB bridge, pokud je dostupný,
6. vytvoří jednoduchý log zdrojů v data/raw/source_links.md.

Důležité:
- Raw data ručně neupravujeme.
- Veškeré čištění a transformace se budou dělat až v dalších skriptech.
- Pokud některý zdroj nejde stáhnout automaticky, skript to zapíše do logu
  a projekt může pokračovat s ručně staženým souborem.

Spuštění z rootu repozitáře:
    python municipal_map_mvp/src/01_download_data.py

Volitelně:
    python municipal_map_mvp/src/01_download_data.py --force
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

import requests


# =============================================================================
# CESTY
# =============================================================================

# Soubor je v municipal_map_mvp/src/, proto parents[1] = municipal_map_mvp/
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
GEO_DIR = DATA_DIR / "geo"

OUTPUTS_DIR = PROJECT_ROOT / "outputs"
DOCS_DIR = PROJECT_ROOT / "docs"
CONFIG_DIR = PROJECT_ROOT / "config"
PRESENTATION_DIR = PROJECT_ROOT / "presentation"

SOURCE_LOG_PATH = RAW_DIR / "source_links.md"

DATASTAT_CATALOGUE_PATH = RAW_DIR / "czso_datastat_catalogue.csv"
DATASTAT_CATALOGUE_LATEST_PATH = RAW_DIR / "czso_datastat_catalogue_latest.csv"


# =============================================================================
# VOLITELNÉ IMPORTY ZE STARŠÍHO CZSO BALÍKU
# =============================================================================

# V repozitáři už existují pyczso.py a pyczso_lkod_bridge.py ve starších složkách.
# Tento skript zkusí najít:
# 1. municipal_map_mvp/src/vendor/
# 2. root repozitáře Datamining-2026/
# 3. starý bundle czso_ikz_v10_display_fixed_clean_bundle/

REPO_ROOT = PROJECT_ROOT.parent
VENDOR_DIR = PROJECT_ROOT / "src" / "vendor"
OLD_BUNDLE_DIR = REPO_ROOT / "czso_ikz_v10_display_fixed_clean_bundle"

for candidate_dir in [VENDOR_DIR, REPO_ROOT, OLD_BUNDLE_DIR]:
    if candidate_dir.exists() and str(candidate_dir) not in sys.path:
        sys.path.insert(0, str(candidate_dir))

try:
    import pyczso  # type: ignore
except Exception:
    pyczso = None  # type: ignore

try:
    from pyczso_lkod_bridge import LKODBridge  # type: ignore
except Exception:
    LKODBridge = None  # type: ignore


# =============================================================================
# DATOVÉ ZDROJE
# =============================================================================

@dataclass
class DataSource:
    """Jednoduchý popis jednoho datového zdroje."""

    name: str
    url: Optional[str]
    output_filename: str
    description: str
    required: bool = False
    note: str = ""


# Poznámka:
# ČSÚ může měnit konkrétní URL. Pokud download selže, soubory lze stáhnout ručně
# ze stránky ČSÚ MOS a uložit do data/raw/ pod názvy níže.
#
# Stránka ČSÚ MOS:
# https://csu.gov.cz/produkty/databaze-mos-otevrena-data

DATA_SOURCES: list[DataSource] = [
    DataSource(
        name="ČSÚ MOS - číselník ukazatelů",
        url="https://opendata.csu.gov.cz/soubory/od/od_mos01/mos_ukaz.csv",
        output_filename="csu_mos_ukazatele.csv",
        description="Číselník ukazatelů databáze MOS.",
        required=True,
        note="Používá se pro identifikaci KODUKAZ jednotlivých indikátorů.",
    ),
    DataSource(
        name="ČSÚ MOS - číselník území",
        url="https://opendata.csu.gov.cz/soubory/od/od_mos01/mos_uzemi.csv",
        output_filename="csu_mos_uzemi.csv",
        description="Územní číselník databáze MOS.",
        required=True,
        note="Používá se jako základ pro seznam obcí a jejich kódy.",
    ),
    DataSource(
        name="ČSÚ MOS - data 2024",
        url="https://opendata.csu.gov.cz/soubory/od/od_mos01/mos_data_2024.csv",
        output_filename="csu_mos_data_2024.csv",
        description="Roční datový soubor MOS pro rok 2024.",
        required=True,
        note="Hlavní datový soubor pro MVP.",
    ),
    DataSource(
        name="ČSÚ MOS - data 2023",
        url="https://opendata.csu.gov.cz/soubory/od/od_mos01/mos_data_2023.csv",
        output_filename="csu_mos_data_2023.csv",
        description="Roční datový soubor MOS pro rok 2023.",
        required=False,
        note="Záložní rok, pokud některé ukazatele nejsou dostupné za 2024.",
    ),
    DataSource(
        name="MF Monitor - ruční doplnění",
        url=None,
        output_filename="mf_monitor_manual_export.csv",
        description="Rozpočtová data obcí z Monitoru státní pokladny.",
        required=False,
        note=(
            "Tento zdroj zatím nestahujeme automaticky. Pokud bude použit, "
            "uložte ruční CSV/XLSX export do data/raw/."
        ),
    ),
    DataSource(
        name="Geodata obcí - ruční doplnění",
        url=None,
        output_filename="municipalities.geojson",
        description="GeoJSON / hranice obcí pro mapový výstup.",
        required=False,
        note=(
            "Geodata mohou být větší soubor. Pokud je nebudeme verzovat v Gitu, "
            "uložte je do data/geo/ a do README napište zdroj."
        ),
    ),
]


# =============================================================================
# POMOCNÉ FUNKCE
# =============================================================================

def ensure_directories() -> None:
    """Vytvoří základní adresářovou strukturu projektu."""
    for directory in [
        DATA_DIR,
        RAW_DIR,
        PROCESSED_DIR,
        GEO_DIR,
        OUTPUTS_DIR,
        DOCS_DIR,
        CONFIG_DIR,
        PRESENTATION_DIR,
    ]:
        directory.mkdir(parents=True, exist_ok=True)


def download_file(
    url: str,
    output_path: Path,
    force: bool = False,
    timeout: int = 120,
) -> tuple[bool, str]:
    """
    Stáhne soubor z URL.

    Parameters
    ----------
    url:
        URL zdrojového souboru.
    output_path:
        Kam se má soubor uložit.
    force:
        Pokud False a soubor už existuje, znovu se nestahuje.
    timeout:
        Maximální čas čekání na odpověď v sekundách.

    Returns
    -------
    tuple[bool, str]
        První hodnota říká, zda se download povedl.
        Druhá hodnota je stručná zpráva pro log.
    """
    if output_path.exists() and not force:
        return True, f"soubor už existuje, download přeskočen: {output_path.name}"

    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={
                "User-Agent": "datamining-obce-project/1.0",
                "Accept": "text/csv,application/json,application/octet-stream,*/*",
            },
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        return False, f"download selhal: {exc}"

    output_path.write_bytes(response.content)
    size_mb = output_path.stat().st_size / (1024 * 1024)
    return True, f"staženo: {output_path.name} ({size_mb:.2f} MB)"


def save_datastat_catalogue(force: bool = False) -> tuple[bool, str]:
    """
    Stáhne katalog sad ČSÚ DataStat přes lokální pyczso.py, pokud je dostupný.

    Tento katalog není hlavní datový zdroj pro MVP, ale hodí se pro screening
    obecních datasetů a pozdější rozšíření projektu.
    """
    if pyczso is None:
        return False, "pyczso.py není dostupný, DataStat katalog nebyl stažen"

    if (
        DATASTAT_CATALOGUE_PATH.exists()
        and DATASTAT_CATALOGUE_LATEST_PATH.exists()
        and not force
    ):
        return True, "DataStat katalog už existuje, stažení přeskočeno"

    try:
        client = pyczso.CZSOClient()
        try:
            catalogue = client.get_catalogue(as_frame=True)
        finally:
            client.close()

        catalogue.to_csv(DATASTAT_CATALOGUE_PATH, index=False, encoding="utf-8-sig")

        try:
            normalized = pyczso.czso_normalize_catalogue(catalogue)
            latest = pyczso.czso_keep_latest_versions(normalized)
            latest.to_csv(
                DATASTAT_CATALOGUE_LATEST_PATH,
                index=False,
                encoding="utf-8-sig",
            )
            return True, (
                f"DataStat katalog stažen: {len(catalogue)} řádků, "
                f"latest verze: {len(latest)} řádků"
            )
        except Exception as exc:
            return True, (
                f"DataStat katalog stažen: {len(catalogue)} řádků; "
                f"normalizace/latest výběr selhal: {exc}"
            )

    except Exception as exc:
        return False, f"stažení DataStat katalogu přes pyczso selhalo: {exc}"


def save_lkod_capability_note() -> tuple[bool, str]:
    """
    Zkontroluje, zda je dostupný LKODBridge.

    LKODBridge zatím v tomto skriptu nestahuje konkrétní datasety.
    Použije se až ve screeningu nebo při cíleném stažení datasetů podle dataset_id.
    """
    if LKODBridge is None:
        return False, (
            "pyczso_lkod_bridge.py není dostupný, "
            "LKOD/VDB cesta zatím nebude použita"
        )

    return True, "LKODBridge je dostupný pro pozdější stahování LKOD/VDB datasetů"


def create_placeholder_files() -> None:
    """
    Vytvoří placeholder soubory, aby bylo jasné, kam patří ručně doplněná data.
    """
    geo_readme = GEO_DIR / "README.md"
    if not geo_readme.exists():
        geo_readme.write_text(
            "# Geodata\n\n"
            "Sem patří GeoJSON nebo jiný mapový podklad s hranicemi obcí.\n\n"
            "Doporučený soubor:\n"
            "- municipalities.geojson\n\n"
            "Soubor musí obsahovat klíč, který půjde spojit s kódem obce / ZÚJ.\n",
            encoding="utf-8",
        )

    raw_readme = RAW_DIR / "README.md"
    if not raw_readme.exists():
        raw_readme.write_text(
            "# Raw data\n\n"
            "Sem ukládáme původní stažené soubory.\n\n"
            "Pravidlo: raw data se ručně neupravují. Pokud je potřeba data čistit, "
            "výsledek patří do `data/processed/`.\n",
            encoding="utf-8",
        )


def write_source_log(results: list[dict]) -> None:
    """Zapíše přehled zdrojů a výsledků stahování do Markdown souboru."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines: list[str] = []
    lines.append("# Přehled zdrojových dat\n")
    lines.append(f"Vygenerováno: {now}\n")
    lines.append(
        "Tento soubor popisuje vstupní zdroje používané v projektu. "
        "Raw data se ručně neupravují; transformace probíhají až v dalších skriptech.\n"
    )

    for result in results:
        source: DataSource = result["source"]

        lines.append(f"## {source.name}\n")
        lines.append(f"- Popis: {source.description}")
        lines.append(f"- Povinný zdroj: {'ano' if source.required else 'ne'}")
        lines.append(f"- Výstupní soubor: `{result['output_path']}`")

        if source.url:
            lines.append(f"- URL: {source.url}")
        else:
            lines.append("- URL: není nastaveno, zdroj se doplňuje ručně")

        lines.append(f"- Stav: {result['status']}")

        if source.note:
            lines.append(f"- Poznámka: {source.note}")

        lines.append("")

    SOURCE_LOG_PATH.write_text("\n".join(lines), encoding="utf-8")


# =============================================================================
# HLAVNÍ BĚH
# =============================================================================

def run(force: bool = False) -> None:
    """Hlavní funkce skriptu."""
    ensure_directories()
    create_placeholder_files()

    results: list[dict] = []

    print("=" * 80)
    print("01_download_data.py")
    print("Příprava vstupních dat")
    print("=" * 80)
    print(f"PROJECT_ROOT: {PROJECT_ROOT}")
    print("")

    # 1) Pokus o stažení katalogu ČSÚ DataStat přes pyczso.
    ok, message = save_datastat_catalogue(force=force)
    print(f"[{'OK' if ok else 'INFO'}] ČSÚ DataStat katalog: {message}")

    results.append(
        {
            "source": DataSource(
                name="ČSÚ DataStat katalog sad",
                url="https://data.csu.gov.cz/api/katalog/v1/sady",
                output_filename=DATASTAT_CATALOGUE_PATH.name,
                description="Katalog datasetů ČSÚ DataStat získaný přes lokální pyczso.py.",
                required=False,
                note="Použije se pro screening dostupných obecních datasetů.",
            ),
            "output_path": str(DATASTAT_CATALOGUE_PATH.relative_to(PROJECT_ROOT)),
            "status": message,
        }
    )

    # 2) Informace o LKOD/VDB bridge.
    ok, message = save_lkod_capability_note()
    print(f"[{'OK' if ok else 'INFO'}] LKOD/VDB bridge: {message}")

    results.append(
        {
            "source": DataSource(
                name="LKOD/VDB bridge dostupnost",
                url="https://vdb.czso.cz/pll/eweb/lkod_ld.datova_sada?id=<dataset_id>",
                output_filename="neni_soubor_v_kroku_01.txt",
                description="Informace, zda lze použít pyczso_lkod_bridge.py pro LKOD/VDB distribuce.",
                required=False,
                note=(
                    "Konkrétní LKOD datasety se budou stahovat až cíleně "
                    "podle shortlistu nebo screeningu."
                ),
            ),
            "output_path": "data/raw/source_links.md",
            "status": message,
        }
    )

    # 3) Stažení hlavních raw zdrojů.
    for source in DATA_SOURCES:
        if source.output_filename.endswith(".geojson"):
            output_path = GEO_DIR / source.output_filename
        else:
            output_path = RAW_DIR / source.output_filename

        if source.url is None:
            status = "ruční zdroj - automatické stažení přeskočeno"
            print(f"[SKIP] {source.name}: {status}")

            results.append(
                {
                    "source": source,
                    "output_path": str(output_path.relative_to(PROJECT_ROOT)),
                    "status": status,
                }
            )
            continue

        ok, message = download_file(source.url, output_path, force=force)
        status_prefix = "OK" if ok else "ERROR"
        print(f"[{status_prefix}] {source.name}: {message}")

        results.append(
            {
                "source": source,
                "output_path": str(output_path.relative_to(PROJECT_ROOT)),
                "status": message,
            }
        )

    write_source_log(results)

    print("=" * 80)
    print("Hotovo.")
    print(f"Log zdrojů: {SOURCE_LOG_PATH.relative_to(PROJECT_ROOT)}")
    print("")
    print("Další krok:")
    print("python municipal_map_mvp/src/pipeline_core_scripts_02_06.py config")
    print("=" * 80)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Stáhne nebo připraví vstupní data projektu."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Znovu stáhne soubory, i pokud už existují.",
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    args = parse_args()
    try:
        run(force=args.force)
    except KeyboardInterrupt:
        print("\nPřerušeno uživatelem.")
        sys.exit(130)