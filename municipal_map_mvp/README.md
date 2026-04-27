# Datová mapa kvality a rozvoje obcí ČR — MVP

Tento projekt zpracovává otevřená data ČSÚ MOS na úrovni obcí a vytváří interaktivní HTML dashboard pro analýzu kvality a rozvoje obcí v ČR.

Finální aplikace umožňuje:

- zobrazit obce ČR na interaktivní mapě,
- vybrat konkrétní ukazatel,
- porovnat obec vůči podobně velkým obcím,
- zobrazit trendové grafy,
- zobrazit věkovou strukturu obyvatel,
- zobrazit odpadové ukazatele,
- zobrazit krajinný a environmentální profil obce,
- vyhledat obec podle názvu nebo kódu,
- otevřít výsledný dashboard jako jeden HTML soubor v prohlížeči.

Hlavní výstup projektu:

```text
municipal_map_mvp/outputs/interactive_map_business_dashboard.html
```

HTML dashboard je možné poslat dalším lidem jako samostatný soubor. Pro zobrazení mapového podkladu a načtení knihoven Leaflet / Chart.js je potřeba internetové připojení.

---

## Obsah repozitáře

```text
municipal_map_mvp/
├── src/
│   ├── 00_download_municipality_geometries.py
│   ├── 01_download_data.py
│   ├── pipeline_core_scripts_02_06.py
│   ├── 13_build_indicator_trends.py
│   ├── download_age_structure_oby02e.py
│   ├── 15_add_age_structure.py
│   ├── 17_apply_methodology_updates.py
│   ├── 19_download_visoh2_waste.py
│   ├── 20_add_land_use_environment.py
│   └── 14_generate_interactive_map_business_dashboard.py
├── config/
├── data/
│   ├── raw/
│   ├── processed/
│   └── geo/
└── outputs/
```

---

## Co jednotlivé skripty dělají

### `01_download_data.py`

Připraví základní složky projektu a stáhne základní datové soubory ČSÚ MOS, pokud jsou dostupné přes URL.

Typické výstupy:

```text
municipal_map_mvp/data/raw/csu_mos_ukazatele.csv
municipal_map_mvp/data/raw/csu_mos_uzemi.csv
municipal_map_mvp/data/raw/csu_mos_data_2020.csv
municipal_map_mvp/data/raw/csu_mos_data_2021.csv
municipal_map_mvp/data/raw/csu_mos_data_2022.csv
municipal_map_mvp/data/raw/csu_mos_data_2023.csv
municipal_map_mvp/data/raw/csu_mos_data_2024.csv
municipal_map_mvp/data/raw/csu_mos_data_latest.csv
```

### `00_download_municipality_geometries.py`

Stáhne hranice obcí ČR do lokálního GeoJSON souboru.

Výstup:

```text
municipal_map_mvp/data/geo/municipalities.geojson
```

Tento soubor je nutný pro vykreslení mapy.

### `pipeline_core_scripts_02_06.py`

Základní MVP pipeline. Spouští se po jednotlivých příkazech:

```bash
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py config
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py geo
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py indicators
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py score
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py case
```

Hlavní výstupy:

```text
municipal_map_mvp/config/indicator_catalog.csv
municipal_map_mvp/data/processed/geo_master.csv
municipal_map_mvp/data/processed/municipality_indicators_raw.csv
municipal_map_mvp/data/processed/municipality_scores.csv
municipal_map_mvp/data/processed/dimension_scores.csv
municipal_map_mvp/outputs/case_study_moravicany.md
```

### `13_build_indicator_trends.py`

Vytvoří časové řady a trendy vybraných indikátorů za období 2020–2024.

Výstupy:

```text
municipal_map_mvp/data/processed/municipality_indicators_timeseries.csv
municipal_map_mvp/data/processed/municipality_indicators_trends_wide.csv
```

### `download_age_structure_oby02e.py`

Stáhne nebo připraví dataset věkové struktury obyvatel podle základních věkových skupin.

Výstup:

```text
municipal_map_mvp/data/raw/csu_age_structure_basic.csv
```

Pokud automatické stažení nefunguje, lze použít ručně stažený CSV soubor:

```bash
python municipal_map_mvp/src/download_age_structure_oby02e.py --input municipal_map_mvp/data/raw/NAZEV_SOUBORU.csv
```

### `15_add_age_structure.py`

Zpracuje věkovou strukturu a doplní ukazatele:

- podíl dětí 0–14,
- podíl obyvatel 15–64,
- podíl seniorů 65+,
- index stáří,
- průměrný věk.

Výstupy:

```text
municipal_map_mvp/data/processed/age_structure_timeseries.csv
municipal_map_mvp/data/processed/age_structure_trends_wide.csv
municipal_map_mvp/data/processed/municipality_indicators_raw.csv
```

### `19_download_visoh2_waste.py`

Zpracuje export odpadových dat VISOH2.

Používá se pro ukazatele jako:

- plnění cíle třídění,
- komunální odpad na obyvatele,
- směsný komunální odpad na obyvatele,
- objemný odpad na obyvatele,
- separované recyklovatelné složky,
- separace plastu,
- účinnost separace plastu,
- bioodpad na obyvatele.

Výstupy:

```text
municipal_map_mvp/data/processed/waste_indicators_raw.csv
municipal_map_mvp/data/processed/waste_indicators_trends_wide.csv
municipal_map_mvp/data/processed/municipality_indicators_raw.csv
```

### `20_add_land_use_environment.py`

Doplní územní a environmentální ukazatele z ČSÚ MOS.

Doplňuje například:

- výměru obce,
- ornou půdu,
- zemědělskou půdu,
- lesní půdu,
- trvalé travní porosty,
- vodní plochy,
- zastavěné plochy,
- koeficient ekologické stability,
- podíl přírodně stabilnějších ploch,
- podíl intenzivně využívaných ploch.

Výstupy:

```text
municipal_map_mvp/data/processed/land_use_environment.csv
municipal_map_mvp/data/processed/municipality_indicators_raw.csv
```

### `17_apply_methodology_updates.py`

Provede metodické přepočty, kategorizace a benchmarky.

Dělá zejména:

- finální velikostní kategorie obcí,
- typ sídla,
- varování pro malé obce,
- robustní skóre 0–100,
- agregaci indikátorů do dimenzí,
- výstup pro dashboard.

Výstupy:

```text
municipal_map_mvp/data/processed/municipality_scores.csv
municipal_map_mvp/data/processed/dimension_scores.csv
municipal_map_mvp/data/processed/indicator_scoring_stats.csv
```

### `14_generate_interactive_map_business_dashboard.py`

Vygeneruje finální interaktivní HTML dashboard.

Vstupy:

```text
municipal_map_mvp/data/geo/municipalities.geojson
municipal_map_mvp/data/processed/dimension_scores.csv
municipal_map_mvp/data/processed/municipality_indicators_raw.csv
municipal_map_mvp/data/processed/municipality_indicators_trends_wide.csv
municipal_map_mvp/data/processed/age_structure_trends_wide.csv
municipal_map_mvp/data/processed/waste_indicators_trends_wide.csv
```

Výstup:

```text
municipal_map_mvp/outputs/interactive_map_business_dashboard.html
```

---

## Instalace

Doporučená verze Pythonu:

```text
Python 3.10+
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

### Instalace knihoven

Pokud je v repozitáři soubor `requirements.txt`, spusť:

```bash
pip install -r requirements.txt
```

Pokud `requirements.txt` zatím není, nainstaluj minimální sadu knihoven:

```bash
pip install pandas numpy requests geopandas openpyxl folium
```

Alternativa přes conda, vhodná hlavně kvůli `geopandas`:

```bash
conda create -n municipal-map python=3.10 geopandas pandas numpy requests openpyxl folium
conda activate municipal-map
```

---

## Rychlé spuštění celé pipeline

Skripty se spouští z rootu repozitáře `Datamining-2026`.

```bash
python municipal_map_mvp/src/01_download_data.py
python municipal_map_mvp/src/00_download_municipality_geometries.py

python municipal_map_mvp/src/pipeline_core_scripts_02_06.py config
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py geo
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py indicators
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py score

python municipal_map_mvp/src/13_build_indicator_trends.py

python municipal_map_mvp/src/download_age_structure_oby02e.py
python municipal_map_mvp/src/15_add_age_structure.py

python municipal_map_mvp/src/19_download_visoh2_waste.py

python municipal_map_mvp/src/20_add_land_use_environment.py
python municipal_map_mvp/src/17_apply_methodology_updates.py

python municipal_map_mvp/src/14_generate_interactive_map_business_dashboard.py
```

Po úspěšném doběhnutí vznikne:

```text
municipal_map_mvp/outputs/interactive_map_business_dashboard.html
```

---

## Podrobný postup spuštění mapy

### 1. Naklonování repozitáře

```bash
git clone https://github.com/Mikuva/Datamining-2026.git
cd Datamining-2026
```

### 2. Instalace prostředí

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pandas numpy requests geopandas openpyxl folium
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pandas numpy requests geopandas openpyxl folium
```

### 3. Stažení základních dat

```bash
python municipal_map_mvp/src/01_download_data.py
```

Tento krok připraví složky:

```text
municipal_map_mvp/data/raw/
municipal_map_mvp/data/processed/
municipal_map_mvp/data/geo/
municipal_map_mvp/outputs/
```

a pokusí se stáhnout základní soubory ČSÚ MOS.

### 4. Stažení geometrií obcí

```bash
python municipal_map_mvp/src/00_download_municipality_geometries.py
```

Po doběhnutí musí existovat:

```text
municipal_map_mvp/data/geo/municipalities.geojson
```

Bez tohoto souboru se mapa nevygeneruje.

### 5. Vytvoření konfigurace indikátorů

```bash
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py config
```

Po doběhnutí musí existovat:

```text
municipal_map_mvp/config/indicator_catalog.csv
```

### 6. Vytvoření územního master souboru

```bash
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py geo
```

Po doběhnutí musí existovat:

```text
municipal_map_mvp/data/processed/geo_master.csv
```

### 7. Vytvoření základních indikátorů

```bash
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py indicators
```

Po doběhnutí musí existovat:

```text
municipal_map_mvp/data/processed/municipality_indicators_raw.csv
```

### 8. Vytvoření základního skóre

```bash
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py score
```

Po doběhnutí musí existovat:

```text
municipal_map_mvp/data/processed/municipality_scores.csv
municipal_map_mvp/data/processed/dimension_scores.csv
```

### 9. Vytvoření trendů indikátorů

```bash
python municipal_map_mvp/src/13_build_indicator_trends.py
```

Po doběhnutí musí existovat:

```text
municipal_map_mvp/data/processed/municipality_indicators_trends_wide.csv
```

### 10. Věková struktura

Nejdříve připrav vstupní data:

```bash
python municipal_map_mvp/src/download_age_structure_oby02e.py
```

Po doběhnutí musí existovat:

```text
municipal_map_mvp/data/raw/csu_age_structure_basic.csv
```

Potom doplň věkové ukazatele:

```bash
python municipal_map_mvp/src/15_add_age_structure.py
```

Po doběhnutí musí existovat:

```text
municipal_map_mvp/data/processed/age_structure_trends_wide.csv
```

### 11. Odpadová data VISOH2

Odpadová data nemusí jít stáhnout automaticky. Je potřeba mít export VISOH2 ve složce:

```text
municipal_map_mvp/data/raw/visoh2/
```

Pokud je ve složce právě jeden soubor, spusť:

```bash
python municipal_map_mvp/src/19_download_visoh2_waste.py
```

Pokud je souborů více nebo chceš použít konkrétní export:

```bash
python municipal_map_mvp/src/19_download_visoh2_waste.py --input municipal_map_mvp/data/raw/visoh2/NAZEV_SOUBORU.xlsx
```

Po doběhnutí musí existovat:

```text
municipal_map_mvp/data/processed/waste_indicators_trends_wide.csv
```

### 12. Krajina a životní prostředí

```bash
python municipal_map_mvp/src/20_add_land_use_environment.py
```

Po doběhnutí by měl existovat:

```text
municipal_map_mvp/data/processed/land_use_environment.csv
```

a zároveň budou doplněné environmentální ukazatele do:

```text
municipal_map_mvp/data/processed/municipality_indicators_raw.csv
```

### 13. Metodické přepočty a benchmarky

```bash
python municipal_map_mvp/src/17_apply_methodology_updates.py
```

Tento krok je důležitý pro finální dashboard, protože vytváří finální benchmarky a soubor:

```text
municipal_map_mvp/data/processed/dimension_scores.csv
```

### 14. Vygenerování finální mapy

```bash
python municipal_map_mvp/src/14_generate_interactive_map_business_dashboard.py
```

Po úspěšném doběhnutí vznikne:

```text
municipal_map_mvp/outputs/interactive_map_business_dashboard.html
```

### 15. Otevření mapy

macOS:

```bash
open municipal_map_mvp/outputs/interactive_map_business_dashboard.html
```

Windows:

```powershell
start municipal_map_mvp/outputs/interactive_map_business_dashboard.html
```

Linux:

```bash
xdg-open municipal_map_mvp/outputs/interactive_map_business_dashboard.html
```

Soubor lze otevřít také ručně dvojklikem v prohlížeči.

---

## Kontrola, že pipeline doběhla správně

Po kompletním běhu by měly existovat minimálně tyto soubory:

```text
municipal_map_mvp/data/geo/municipalities.geojson
municipal_map_mvp/data/processed/geo_master.csv
municipal_map_mvp/data/processed/municipality_indicators_raw.csv
municipal_map_mvp/data/processed/municipality_indicators_trends_wide.csv
municipal_map_mvp/data/processed/age_structure_trends_wide.csv
municipal_map_mvp/data/processed/waste_indicators_trends_wide.csv
municipal_map_mvp/data/processed/dimension_scores.csv
municipal_map_mvp/outputs/interactive_map_business_dashboard.html
```

Rychlá kontrola v terminálu:

```bash
ls -lh municipal_map_mvp/data/geo/municipalities.geojson
ls -lh municipal_map_mvp/data/processed/geo_master.csv
ls -lh municipal_map_mvp/data/processed/municipality_indicators_raw.csv
ls -lh municipal_map_mvp/data/processed/municipality_indicators_trends_wide.csv
ls -lh municipal_map_mvp/data/processed/age_structure_trends_wide.csv
ls -lh municipal_map_mvp/data/processed/waste_indicators_trends_wide.csv
ls -lh municipal_map_mvp/data/processed/dimension_scores.csv
ls -lh municipal_map_mvp/outputs/interactive_map_business_dashboard.html
```

---

## Použitý rok dat

Aktuální běh používá data ČSÚ MOS za rok 2024.

Soubor:

```text
municipal_map_mvp/data/raw/csu_mos_data_latest.csv
```

slouží jako alias na nejnovější dostupný roční soubor MOS.

Použitý rok je uložen v:

```text
municipal_map_mvp/data/raw/latest_mos_year.txt
```

Do budoucna je možné skript `01_download_data.py` upravit tak, aby nový rok detekoval automaticky.

---

## Práce s VISOH2 daty

Export VISOH2 není standardně součástí repozitáře.

Postup:

1. stáhnout export z VISOH2,
2. uložit ho do:

```text
municipal_map_mvp/data/raw/visoh2/
```

3. spustit:

```bash
python municipal_map_mvp/src/19_download_visoh2_waste.py
```

nebo s konkrétním souborem:

```bash
python municipal_map_mvp/src/19_download_visoh2_waste.py --input municipal_map_mvp/data/raw/visoh2/NAZEV_SOUBORU.xlsx
```

---

## Co se necommitujeme do gitu

Repozitář standardně neobsahuje velké raw/processed datové soubory ani vygenerované HTML výstupy.

Necommitují se hlavně:

```text
municipal_map_mvp/data/raw/
municipal_map_mvp/data/processed/
municipal_map_mvp/data/geo/
municipal_map_mvp/outputs/
```

V těchto složkách zůstávají jen `.gitkeep` soubory, aby byla zachovaná struktura projektu.

Důvod:

- menší velikost repozitáře,
- jednodušší verzování,
- reprodukovatelná pipeline,
- oddělení kódu od generovaných dat.

---

## Troubleshooting

### Chyba: chybí `geopandas`

Doporučené řešení přes conda:

```bash
conda create -n municipal-map python=3.10 geopandas pandas numpy requests openpyxl folium
conda activate municipal-map
```

Alternativně přes pip:

```bash
pip install geopandas
```

Na některých systémech může být `geopandas` jednodušší instalovat přes conda.

### Chyba: chybí vstupní soubor

Pokud skript hlásí, že chybí soubor v `data/raw/`, `data/processed/` nebo `data/geo/`, zkontroluj:

1. že jsi ve správné složce projektu,
2. že spouštíš skripty z rootu repozitáře,
3. že jsi spustil předchozí kroky pipeline ve správném pořadí.

Správná pracovní složka:

```bash
pwd
```

má končit například:

```text
Datamining-2026
```

### Chyba při zpracování VISOH2

Zkontroluj, že export je uložený v:

```text
municipal_map_mvp/data/raw/visoh2/
```

a že jde o podporovaný formát, typicky:

```text
.xlsx
.csv
```

Pokud je ve složce více exportů, použij parametr `--input`.

### HTML se otevře, ale mapa nemá podklad

Zkontroluj internetové připojení. HTML používá online:

- Leaflet,
- Chart.js,
- mapové dlaždice CARTO / OpenStreetMap.

Bez internetu se může zobrazit dashboard, ale nemusí se načíst mapový podklad.

---

## Git workflow pro členy týmu

Před začátkem práce:

```bash
git pull --rebase origin master
```

Po změnách:

```bash
git status
git add <konkrétní soubory>
git commit -m "Popis změny"
git pull --rebase origin master
git push
```

Před commitem zkontroluj, že nepřidáváš generated data:

```bash
git diff --staged --stat
```

Ve staged by neměly být velké CSV/XLSX/HTML výstupy, pokud to není výslovně záměr.
