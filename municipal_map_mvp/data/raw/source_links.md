# Přehled zdrojových dat

Vygenerováno: 2026-04-25 22:45:56

Tento soubor popisuje vstupní zdroje používané v projektu. Raw data se ručně neupravují; transformace probíhají až v dalších skriptech.

## ČSÚ DataStat katalog sad

- Popis: Katalog datasetů ČSÚ DataStat získaný přes lokální pyczso.py.
- Povinný zdroj: ne
- Výstupní soubor: `data/raw/czso_datastat_catalogue.csv`
- URL: https://data.csu.gov.cz/api/katalog/v1/sady
- Stav: DataStat katalog stažen: 757 řádků, latest verze: 757 řádků
- Poznámka: Použije se pro screening dostupných obecních datasetů.

## LKOD/VDB bridge dostupnost

- Popis: Informace, zda lze použít pyczso_lkod_bridge.py pro LKOD/VDB distribuce.
- Povinný zdroj: ne
- Výstupní soubor: `data/raw/source_links.md`
- URL: https://vdb.czso.cz/pll/eweb/lkod_ld.datova_sada?id=<dataset_id>
- Stav: LKODBridge je dostupný pro pozdější stahování LKOD/VDB datasetů
- Poznámka: Konkrétní LKOD datasety se budou stahovat až cíleně podle shortlistu nebo screeningu.

## ČSÚ MOS - číselník ukazatelů

- Popis: Číselník ukazatelů databáze MOS.
- Povinný zdroj: ano
- Výstupní soubor: `data/raw/csu_mos_ukazatele.csv`
- URL: https://opendata.csu.gov.cz/soubory/od/od_mos01/mos_ukaz.csv
- Stav: staženo: csu_mos_ukazatele.csv (0.33 MB)
- Poznámka: Používá se pro identifikaci KODUKAZ jednotlivých indikátorů.

## ČSÚ MOS - číselník území

- Popis: Územní číselník databáze MOS.
- Povinný zdroj: ano
- Výstupní soubor: `data/raw/csu_mos_uzemi.csv`
- URL: https://opendata.csu.gov.cz/soubory/od/od_mos01/mos_uzemi.csv
- Stav: staženo: csu_mos_uzemi.csv (0.37 MB)
- Poznámka: Používá se jako základ pro seznam obcí a jejich kódy.

## ČSÚ MOS - data 2024

- Popis: Roční datový soubor MOS pro rok 2024.
- Povinný zdroj: ano
- Výstupní soubor: `data/raw/csu_mos_data_2024.csv`
- URL: https://opendata.csu.gov.cz/soubory/od/od_mos01/mos_data_2024.csv
- Stav: staženo: csu_mos_data_2024.csv (41.83 MB)
- Poznámka: Hlavní datový soubor pro MVP.

## ČSÚ MOS - data 2023

- Popis: Roční datový soubor MOS pro rok 2023.
- Povinný zdroj: ne
- Výstupní soubor: `data/raw/csu_mos_data_2023.csv`
- URL: https://opendata.csu.gov.cz/soubory/od/od_mos01/mos_data_2023.csv
- Stav: staženo: csu_mos_data_2023.csv (41.03 MB)
- Poznámka: Záložní rok, pokud některé ukazatele nejsou dostupné za 2024.

## MF Monitor - ruční doplnění

- Popis: Rozpočtová data obcí z Monitoru státní pokladny.
- Povinný zdroj: ne
- Výstupní soubor: `data/raw/mf_monitor_manual_export.csv`
- URL: není nastaveno, zdroj se doplňuje ručně
- Stav: ruční zdroj - automatické stažení přeskočeno
- Poznámka: Tento zdroj zatím nestahujeme automaticky. Pokud bude použit, uložte ruční CSV/XLSX export do data/raw/.

## Geodata obcí - ruční doplnění

- Popis: GeoJSON / hranice obcí pro mapový výstup.
- Povinný zdroj: ne
- Výstupní soubor: `data/geo/municipalities.geojson`
- URL: není nastaveno, zdroj se doplňuje ručně
- Stav: ruční zdroj - automatické stažení přeskočeno
- Poznámka: Geodata mohou být větší soubor. Pokud je nebudeme verzovat v Gitu, uložte je do data/geo/ a do README napište zdroj.
