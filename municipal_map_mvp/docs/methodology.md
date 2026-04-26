# Metodika projektu

## Cíl projektu

Cílem projektu je vytvořit datovou mapu obcí ČR, která ukazuje vybrané dimenze rozvoje obcí na škále 0–100.

Projekt není koncipován jako jeden definitivní index kvality života. Hlavním výstupem jsou samostatné dimenze, které pomáhají interpretovat silné a slabé stránky obcí.

## Datový zdroj

Základním zdrojem jsou otevřená data ČSÚ MOS, tedy Městská a obecní statistika.

Použité soubory:

- číselník území
- číselník ukazatelů
- roční datový soubor MOS

V aktuálním běhu byl použit rok 2024.

## Použité indikátory

| Indikátor | Dimenze | Směr |
|---|---|---|
| Migrační saldo na 1000 obyvatel | Demografie | vyšší = lepší |
| Přirozený přírůstek / úbytek | Demografie | vyšší = lepší |
| Podíl nezaměstnaných osob | Trh práce | nižší = lepší |
| Dokončené byty na 1000 obyvatel | Bydlení a rozvoj | vyšší = lepší |
| Koeficient ekologické stability | Životní prostředí | vyšší = lepší |

## Výpočet skóre 0–100

Každý skórovaný indikátor je převeden na škálu 0–100.

Postup:

1. převod indikátorů na srovnatelnou jednotku,
2. ořez extrémních hodnot na 5. a 95. percentilu,
3. min-max standardizace,
4. otočení směru u ukazatelů, kde nižší hodnota znamená lepší výsledek,
5. výpočet průměru indikátorů v rámci dimenze.

## Interpretace skóre

Skóre 0 neznamená absolutně špatný stav a skóre 100 neznamená dokonalý stav. Skóre vyjadřuje relativní pozici obce vůči ostatním obcím v datech.

Výsledky je nutné číst společně se surovými hodnotami, velikostní kategorií obce a metodickými limity.

## Limity

- Výsledky závisí na dostupnosti veřejných dat.
- Výběr indikátorů ovlivňuje výsledné skóre.
- U menších obcí může malý absolutní počet událostí výrazně ovlivnit přepočet na 1000 obyvatel.
- Projekt zatím neobsahuje finanční data obcí ani širší vybavenost službami.
- Výstup není žebříček obcí, ale analytický nástroj pro srovnání dílčích dimenzí.
