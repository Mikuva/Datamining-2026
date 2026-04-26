# Datová mapa kvality a rozvoje obcí ČR — MVP

Tento MVP projekt zpracovává otevřená data ČSÚ MOS na úrovni obcí a vytváří skóre vybraných dimenzí na škále 0–100.

## Aktuální dimenze

- `demography_score` — migrační saldo a přirozený přírůstek
- `labour_score` — podíl nezaměstnaných osob
- `housing_score` — dokončené byty na 1000 obyvatel
- `environment_score` — koeficient ekologické stability

## Hlavní výstupy

- `data/processed/geo_master.csv`
- `data/processed/municipality_indicators_raw.csv`
- `data/processed/municipality_scores.csv`
- `data/processed/dimension_scores.csv`
- `outputs/case_study_moravicany.md`
- `outputs/moravicany_profile.csv`

## Spuštění pipeline

```bash
python municipal_map_mvp/src/01_download_data.py
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py geo
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py indicators
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py score
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py case


Pak ověř:

```bash
ls -lh municipal_map_mvp/README.md
head -n 20 municipal_map_mvp/README.md



ls -lh municipal_map_mvp/README.md
head -n 20 municipal_map_mvp/README.md

## Použitý rok dat

Aktuální běh používá data ČSÚ MOS za rok 2024.

Soubor `data/raw/csu_mos_data_latest.csv` je alias na nejnovější dostupný roční soubor MOS. V současném běhu byl vytvořen ručně ze souboru `csu_mos_data_2024.csv`.

Použitý rok je uložen v:

- `data/raw/latest_mos_year.txt`

Do budoucna je možné skript `01_download_data.py` upravit tak, aby nový rok detekoval automaticky.
