# Datový slovník

Tento dokument popisuje hlavní datové soubory používané v projektu `municipal_map_mvp`.

Projekt pracuje se čtyřmi typy dat:

1. vstupní raw data,
2. zpracované processed tabulky,
3. geodata,
4. finální HTML dashboard.

Generovaná data nejsou standardně commitována do gitu. Vznikají lokálně spuštěním pipeline.

---

## Hlavní výstup

### `outputs/interactive_map_business_dashboard.html`

Finální interaktivní HTML dashboard.

Obsahuje mapu obcí ČR, výběr oblasti ukazatelů, výběr konkrétního ukazatele, vyhledávání obce, tooltip se surovou hodnotou a benchmarkem, dashboard vybrané obce, trendové grafy, věkovou strukturu, odpadové ukazatele a krajinný/environmentální profil.

Soubor je možné otevřít v prohlížeči. Pro mapový podklad a knihovny Leaflet / Chart.js je potřeba internetové připojení.

---

## Raw data

### `data/raw/csu_mos_ukazatele.csv`

Číselník ukazatelů ČSÚ MOS. Slouží k identifikaci kódů ukazatelů a výběru relevantních indikátorů.

### `data/raw/csu_mos_uzemi.csv`

Číselník území ČSÚ MOS. Obsahuje obce, jejich názvy, kódy a vazby na vyšší územní celky.

### `data/raw/csu_mos_data_2020.csv` až `data/raw/csu_mos_data_2024.csv`

Roční datové soubory ČSÚ MOS.

Typická struktura:

| Sloupec | Popis |
|---|---|
| `rok` | Rok hodnoty |
| `kodukaz` | Kód ukazatele |
| `koduzemi` | Kód území |
| `hodnota` | Hodnota ukazatele |

Používají se pro výpočet indikátorů, časové řady, trendy a environmentální ukazatele.

### `data/raw/csu_mos_data_latest.csv`

Alias na nejnovější dostupný roční soubor MOS. V aktuálním běhu odpovídá roku 2024.

### `data/raw/latest_mos_year.txt`

Textový soubor s informací o použitém nejnovějším roku MOS.

### `data/raw/csu_age_structure_basic.csv`

Připravený vstup pro věkovou strukturu obyvatel. Vzniká skriptem:

```bash
python municipal_map_mvp/src/download_age_structure_oby02e.py
```

Typická struktura:

| Sloupec | Popis |
|---|---|
| `rok` | Rok |
| `kod_obce` | Kód obce |
| `vekova_skupina` | Původní věková skupina |
| `vekova_skupina_std` | Standardizovaná skupina: `0-14`, `15-64`, `65+` |
| `hodnota` | Počet obyvatel v dané skupině |

### `data/raw/visoh2/`

Složka pro ručně stažený export odpadových dat VISOH2. Podporované formáty jsou `.xlsx` a `.csv`. Export VISOH2 není standardně součástí repozitáře.

---

## Geo data

### `data/geo/municipalities.geojson`

GeoJSON s hranicemi obcí ČR. Vzniká skriptem:

```bash
python municipal_map_mvp/src/00_download_municipality_geometries.py
```

Důležité sloupce:

| Sloupec | Popis |
|---|---|
| `kod_obce` | Šestimístný kód obce / ZÚJ |
| `obec_geo` | Název obce podle geodat |
| `geometry` | Geometrie obce |

Používá se pro vykreslení polygonů obcí a propojení s datovými tabulkami přes `kod_obce`.

---

## Processed data

### `data/processed/geo_master.csv`

Základní master tabulka obcí. Vzniká skriptem:

```bash
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py geo
```

Důležité sloupce:

| Sloupec | Popis |
|---|---|
| `kod_obce` | Šestimístný kód obce / ZÚJ |
| `obec` | Název obce |
| `okres` | Okres |
| `orp` | Obec s rozšířenou působností |
| `kraj` | Kraj |
| `population` | Počet obyvatel |
| `size_category` | Původní velikostní kategorie |

### `data/processed/municipality_indicators_raw.csv`

Hlavní tabulka surových indikátorů obcí. Vzniká a doplňuje se skripty:

```bash
python municipal_map_mvp/src/pipeline_core_scripts_02_06.py indicators
python municipal_map_mvp/src/15_add_age_structure.py
python municipal_map_mvp/src/19_download_visoh2_waste.py
python municipal_map_mvp/src/20_add_land_use_environment.py
```

Vybrané sloupce:

| Sloupec | Popis |
|---|---|
| `kod_obce` | Kód obce |
| `obec` | Název obce |
| `population` | Počet obyvatel |
| `migration_balance_per_1000` | Migrační saldo na 1000 obyvatel |
| `natural_increase` | Přirozený přírůstek / úbytek |
| `unemployment_rate` | Podíl nezaměstnaných osob v % |
| `completed_flats_per_1000` | Dokončené byty na 1000 obyvatel |
| `average_age` | Průměrný věk |
| `children_share` | Podíl obyvatel 0–14 |
| `working_age_share` | Podíl obyvatel 15–64 |
| `senior_share` | Podíl obyvatel 65+ |
| `ageing_index` | Index stáří |
| `waste_sorting_target_share` | Plnění cíle třídění |
| `municipal_waste_kg_per_capita` | Komunální odpad kg/obyv. |
| `mixed_municipal_waste_kg_per_capita` | Směsný komunální odpad kg/obyv. |
| `plastic_separation_kg_per_capita` | Separace plastu kg/obyv. |
| `plastic_separation_efficiency` | Účinnost separace plastu |
| `bio_waste_kg_per_capita` | Bioodpad kg/obyv. |
| `ecological_stability_coef` | Koeficient ekologické stability |
| `municipality_area_km2` | Výměra obce v km² |
| `population_density_per_km2` | Hustota obyvatel |
| `built_up_area_share` | Podíl zastavěných ploch |
| `arable_land_share` | Podíl orné půdy |
| `forest_land_share` | Podíl lesní půdy |
| `water_area_share` | Podíl vodních ploch |
| `natural_stable_area_share` | Podíl přírodně stabilnějších ploch |
| `intensive_land_use_share` | Podíl intenzivně využívaných ploch |

### `data/processed/municipality_scores.csv`

Tabulka skóre jednotlivých indikátorů na škále 0–100. Skóre je relativní vůči obcím v datech.

### `data/processed/dimension_scores.csv`

Finální tabulka používaná dashboardem. Vzniká skriptem:

```bash
python municipal_map_mvp/src/17_apply_methodology_updates.py
```

Důležité sloupce:

| Sloupec | Popis |
|---|---|
| `kod_obce` | Kód obce |
| `obec` | Název obce |
| `okres` | Okres |
| `orp` | ORP |
| `population` | Počet obyvatel |
| `size_category_final` | Finální velikostní benchmark |
| `settlement_type` | Typ sídla |
| `volatility_warning` | Varování pro malé obce |
| `demography_score` | Skóre demografie |
| `labour_score` | Skóre trhu práce |
| `housing_score` | Skóre bydlení |
| `environment_score` | Skóre životního prostředí |

### `data/processed/municipality_indicators_trends_wide.csv`

Wide tabulka trendů indikátorů za roky 2020–2024. Používá ji finální dashboard pro trendové grafy.

### `data/processed/age_structure_trends_wide.csv`

Wide tabulka věkových ukazatelů za roky 2020–2024. Používá ji dashboard pro věkovou strukturu a demografické grafy.

### `data/processed/waste_indicators_trends_wide.csv`

Wide tabulka odpadových ukazatelů. Typické roky jsou 2021, 2022 a 2023. Používá ji dashboard pro oblast Odpadové hospodářství.

### `data/processed/land_use_environment.csv`

Tabulka krajinných a environmentálních ukazatelů z ČSÚ MOS. Obsahuje výměru obce, ornou půdu, zemědělskou půdu, lesní půdu, vodní plochy, zastavěné plochy a koeficient ekologické stability.

### `data/processed/indicator_scoring_stats.csv`

Pomocný metodický výstup. Obsahuje statistiky použité při skórování: počet validních hodnot, 5. percentil, 95. percentil, směr indikátoru a dimenzi.

---

## Klíčové identifikátory

### `kod_obce`

Šestimístný kód obce / ZÚJ. Používá se pro spojování všech datových vrstev.

### `size_category_final`

Finální velikostní benchmark obce.

Kategorie:

```text
0-499
500-999
1000-1999
2000-4999
5000-14999
15000-29999
30000-49999
50000-99999
100000+
```

### `settlement_type`

Uživatelsky srozumitelný typ sídla odvozený z počtu obyvatel.

Příklady: mikroobec, malá obec, větší obec / městys, malé město, střední město, velké město, metropole.

### `volatility_warning`

Textové upozornění pro malé obce. U malých obcí mohou malé absolutní počty výrazně ovlivnit přepočty na 1000 obyvatel.

---

## Poznámka k verzování dat

Soubory v `data/raw/`, `data/processed/`, `data/geo/` a `outputs/` jsou generované a standardně se necommitují.

V repozitáři zůstávají pouze `.gitkeep` soubory.
