# Metodika projektu

## Cíl projektu

Cílem projektu je vytvořit datovou mapu obcí ČR, která pomáhá analyzovat vybrané aspekty kvality a rozvoje obcí.

Projekt není definitivní žebříček obcí ani absolutní index kvality života.

Hlavní výstupy projektu jsou:

1. samostatné surové ukazatele,
2. skóre vybraných dimenzí na škále 0–100,
3. trendové grafy,
4. velikostní benchmark obce,
5. interaktivní HTML dashboard.

Finální dashboard zobrazuje konkrétní ukazatele, nikoli pouze kompozitní skóre.

---

## Hlavní princip interpretace

Dashboard rozlišuje dvě roviny:

1. **surová hodnota ukazatele** — například kg odpadu na obyvatele, podíl seniorů v %, počet obyvatel nebo koeficient ekologické stability.
2. **relativní pozice v benchmarku** — hodnota je srovnána s podobně velkými obcemi a převedena na škálu 0–100.

Surová hodnota je vždy uvedena v tooltipu nebo dashboardu. Barva mapy vyjadřuje relativní pozici v benchmarku.

---

## Datové zdroje

### ČSÚ MOS

Základním zdrojem jsou otevřená data ČSÚ MOS, tedy Městská a obecní statistika.

Používají se číselník území, číselník ukazatelů, roční datové soubory MOS a data za roky 2020–2024.

V aktuálním běhu je jako nejnovější rok použit rok 2024.

### Geometrie obcí

Hranice obcí jsou uloženy v souboru:

```text
municipal_map_mvp/data/geo/municipalities.geojson
```

Geometrie se používají pro vykreslení mapy a propojení s daty přes kód obce.

### Věková struktura

Věková struktura je zpracována ze sady ČSÚ/DataStat OBY02E.

Používané skupiny:

- 0–14 let,
- 15–64 let,
- 65+ let.

Z nich jsou odvozeny podíl dětí, podíl produktivní složky, podíl seniorů a index stáří.

### VISOH2

Odpadová data pocházejí z exportu VISOH2. Export se do projektu vkládá ručně do složky:

```text
municipal_map_mvp/data/raw/visoh2/
```

---

## Oblasti ukazatelů v dashboardu

Dashboard pracuje s těmito oblastmi:

1. Odpadové hospodářství
2. Demografie a věková struktura
3. Práce a sociálně-ekonomická situace
4. Bydlení a výstavba
5. Krajina a životní prostředí

---

## Příklady používaných ukazatelů

### Demografie a věková struktura

| Ukazatel | Interpretace |
|---|---|
| `population` | Počet obyvatel |
| `migration_balance_per_1000` | Migrační saldo na 1000 obyvatel |
| `natural_increase` | Přirozený přírůstek / úbytek |
| `children_share` | Podíl obyvatel 0–14 |
| `working_age_share` | Podíl obyvatel 15–64 |
| `senior_share` | Podíl obyvatel 65+ |
| `ageing_index` | Počet seniorů 65+ na 100 dětí 0–14 |
| `average_age` | Průměrný věk obyvatel |

### Práce a socioekonomická situace

| Ukazatel | Interpretace |
|---|---|
| `unemployment_rate` | Podíl nezaměstnaných osob |

### Bydlení a výstavba

| Ukazatel | Interpretace |
|---|---|
| `completed_flats_per_1000` | Dokončené byty na 1000 obyvatel |

### Odpadové hospodářství

| Ukazatel | Interpretace |
|---|---|
| `waste_sorting_target_share` | Plnění cíle třídění |
| `municipal_waste_kg_per_capita` | Komunální odpad v kg na obyvatele |
| `mixed_municipal_waste_kg_per_capita` | Směsný komunální odpad v kg na obyvatele |
| `bulky_waste_kg_per_capita` | Objemný odpad v kg na obyvatele |
| `separated_recyclables_kg_per_capita` | Separované recyklovatelné složky v kg na obyvatele |
| `plastic_separation_kg_per_capita` | Separace plastu v kg na obyvatele |
| `plastic_separation_efficiency` | Účinnost separace plastu |
| `bio_waste_kg_per_capita` | Bioodpad v kg na obyvatele |

### Krajina a životní prostředí

| Ukazatel | Interpretace |
|---|---|
| `ecological_stability_coef` | Koeficient ekologické stability |
| `municipality_area_km2` | Výměra obce v km² |
| `population_density_per_km2` | Hustota obyvatel na km² |
| `built_up_area_share` | Podíl zastavěných ploch |
| `arable_land_share` | Podíl orné půdy |
| `forest_land_share` | Podíl lesní půdy |
| `permanent_grassland_share` | Podíl trvalých travních porostů |
| `water_area_share` | Podíl vodních ploch |
| `agricultural_land_share` | Podíl zemědělské půdy |
| `natural_stable_area_share` | Podíl přírodně stabilnějších ploch |
| `intensive_land_use_share` | Podíl intenzivně využívaných ploch |

---

## Směr indikátorů

Každý ukazatel má přiřazený interpretační směr.

### `UP`

Vyšší hodnota je považována za příznivější.

Příklady: plnění cíle třídění, účinnost separace plastu, koeficient ekologické stability, podíl lesní půdy, podíl vodních ploch.

### `DOWN`

Nižší hodnota je považována za příznivější.

Příklady: podíl nezaměstnaných osob, směsný komunální odpad na obyvatele, komunální odpad na obyvatele, index stáří, průměrný věk, podíl zastavěných ploch, intenzivně využívané plochy.

### `CONTEXT`

Ukazatel nemá jednoznačně pozitivní nebo negativní směr.

Příklady: počet obyvatel, podíl dětí, podíl produktivní složky, podíl seniorů, výměra obce, hustota obyvatel, separované recyklovatelné složky, bioodpad na obyvatele.

U těchto ukazatelů se barva interpretuje jako relativní výše hodnoty v benchmarku, ne jako definitivní kvalita.

---

## Výpočet skóre 0–100

Skóre je relativní pozice ukazatele vůči srovnávací skupině.

Postup:

1. vybere se relevantní ukazatel,
2. vyberou se obce v příslušném benchmarku,
3. hodnoty se očistí o extrémy pomocí 5. a 95. percentilu,
4. hodnota se převede na škálu 0–100,
5. u ukazatelů se směrem `DOWN` se škála otočí,
6. výsledné skóre se použije pro barvu mapy nebo dimenzionální skóre.

Skóre 100 neznamená absolutně dokonalý stav a skóre 0 neznamená absolutně špatný stav. Vyjadřuje pouze relativní pozici v datech.

---

## Velikostní benchmark

Obce nejsou v dashboardu primárně porovnávány se všemi obcemi najednou, ale s podobně velkými obcemi.

Použité velikostní kategorie:

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

Důvodem je, že malé obce mají jiné hodnoty a výkyvy než velká města. Přepočty na 1000 obyvatel jsou u malých obcí citlivé na malé absolutní počty.

---

## Ošetření extrémů

Pro mapové skóre a metodické skórování se používá ořez na 5. a 95. percentilu.

Důvod:

- snížení vlivu extrémních hodnot,
- stabilnější barevná škála,
- lepší čitelnost mapy,
- omezení zkreslení u malých obcí.

Hodnoty pod 5. percentilem jsou pro účely škálování brány jako 5. percentil. Hodnoty nad 95. percentilem jsou brány jako 95. percentil.

---

## Barevná interpretace mapy

Mapa používá jednotnou škálu:

| Barva | Význam |
|---|---|
| tmavě zelená | příznivá / vysoká hodnota |
| zelená | spíše příznivá / vyšší hodnota |
| světle zelená | střední hodnota |
| oranžová | méně příznivá / nižší hodnota |
| červená | riziková / nízká hodnota |
| šedá | bez dat / mimo filtr |

U ukazatelů se směrem `DOWN` je škála otočena. Nižší surová hodnota tedy vede k zelenější barvě.

U kontextových ukazatelů zelená značí vyšší hodnotu v benchmarku a červená nižší hodnotu. Neznamená to automaticky lepší nebo horší kvalitu.

---

## Trendy

Trendové grafy pracují s dostupnými roky:

- u většiny ČSÚ ukazatelů 2020–2024,
- u odpadových ukazatelů typicky 2021–2023.

Trend má ukázat vývoj v čase, ne pouze aktuální stav.

U procentních ukazatelů se rozdíl interpretuje jako změna v procentních bodech.

---

## Koeficient ekologické stability

Koeficient ekologické stability je poměr ekologicky příznivých ploch vůči plochám zatěžujícím životní prostředí.

V dashboardu je použit pro environmentální profil a interpretaci krajinné stability.

---

## Limity

- Výsledky závisí na dostupnosti veřejných dat.
- Výběr indikátorů ovlivňuje interpretaci.
- U malých obcí mohou malé absolutní počty výrazně ovlivnit přepočty na 1000 obyvatel.
- Kontextové ukazatele nemají automaticky hodnoticí význam.
- Výstup není žebříček obcí, ale analytický nástroj.
- HTML dashboard potřebuje internet pro mapové podklady a online knihovny.

---

## Doporučená interpretace

Výsledky je vhodné číst společně:

1. surová hodnota,
2. trend v čase,
3. velikostní benchmark,
4. typ sídla,
5. varování pro malé obce,
6. lokální znalost konkrétní obce.
