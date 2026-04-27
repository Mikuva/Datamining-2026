#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
17_apply_methodology_updates.py

Metodicky stabilní přepočet kategorií, ošetření extrémů a skóre 0–100.

Co skript dělá:
1. přidá finální velikostní kategorie obcí,
2. přidá typ sídla,
3. přidá varování pro malé obce,
4. počítá robustní skóre indikátorů s ořezem na 5.–95. percentil,
5. agreguje indikátorová skóre do dimenzí,
6. ukládá statistiky skóre pro metodickou obhajobu.

Vstupy:
    municipal_map_mvp/config/indicator_catalog.csv
    municipal_map_mvp/data/processed/geo_master.csv
    municipal_map_mvp/data/processed/municipality_indicators_raw.csv

Výstupy:
    municipal_map_mvp/data/processed/municipality_indicators_raw.csv
    municipal_map_mvp/data/processed/municipality_scores.csv
    municipal_map_mvp/data/processed/dimension_scores.csv
    municipal_map_mvp/data/processed/indicator_scoring_stats.csv
    municipal_map_mvp/outputs/methodology_update_summary.md

Spuštění:
    python municipal_map_mvp/src/17_apply_methodology_updates.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

CONFIG_PATH = PROJECT_ROOT / "config" / "indicator_catalog.csv"

PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

GEO_MASTER_PATH = PROCESSED_DIR / "geo_master.csv"
RAW_INDICATORS_PATH = PROCESSED_DIR / "municipality_indicators_raw.csv"

MUNICIPALITY_SCORES_OUT = PROCESSED_DIR / "municipality_scores.csv"
DIMENSION_SCORES_OUT = PROCESSED_DIR / "dimension_scores.csv"
SCORING_STATS_OUT = PROCESSED_DIR / "indicator_scoring_stats.csv"

SUMMARY_OUT = OUTPUTS_DIR / "methodology_update_summary.md"


SIZE_BINS = [
    0,
    499,
    999,
    1999,
    4999,
    14999,
    29999,
    49999,
    99999,
    float("inf"),
]

SIZE_LABELS = [
    "0-499",
    "500-999",
    "1000-1999",
    "2000-4999",
    "5000-14999",
    "15000-29999",
    "30000-49999",
    "50000-99999",
    "100000+",
]


DIMENSION_ALIASES = {
    "ageing": "demography",
    "aging": "demography",
}


DIMENSION_OUTPUT_ORDER = [
    "demography",
    "labour",
    "housing",
    "environment",
    "economy",
    "services",
    "social",
]


def clean_code(value) -> str:
    """Vyčistí kód obce do textové podoby bez .0."""
    if pd.isna(value):
        return ""

    return str(value).strip().replace(".0", "")


def read_csv_smart(path: Path) -> pd.DataFrame:
    """Načte CSV s tolerancí na běžná česká kódování."""
    last_error = None

    for enc in ["utf-8-sig", "utf-8", "cp1250", "windows-1250", "latin-1"]:
        try:
            return pd.read_csv(path, encoding=enc)
        except Exception as exc:
            last_error = exc

    raise RuntimeError(f"Nepodařilo se načíst {path}: {last_error}")


def assign_size_category_final(population) -> str:
    """Přiřadí finální velikostní kategorii."""
    if pd.isna(population):
        return "bez dat"

    pop = float(population)

    for upper, label in zip(SIZE_BINS[1:], SIZE_LABELS):
        if pop <= upper:
            return label

    return "100000+"


def assign_settlement_type(population) -> str:
    """Přiřadí uživatelsky srozumitelný typ sídla."""
    if pd.isna(population):
        return "bez dat"

    pop = float(population)

    if pop <= 499:
        return "mikroobec"
    if pop <= 999:
        return "malá obec I"
    if pop <= 1999:
        return "malá obec II"
    if pop <= 4999:
        return "větší obec / městys"
    if pop <= 14999:
        return "malé město"
    if pop <= 29999:
        return "menší střední město"
    if pop <= 49999:
        return "střední město"
    if pop <= 99999:
        return "velké město"

    return "metropole / největší město"


def assign_volatility_warning(population) -> str:
    """Vrátí textové varování pro malé obce."""
    if pd.isna(population):
        return "bez dat"

    pop = float(population)

    if pop <= 499:
        return (
            "Vysoká opatrnost: u mikroobcí mohou malé absolutní počty "
            "výrazně ovlivnit přepočet na 1000 obyvatel."
        )

    if pop <= 1999:
        return (
            "Opatrnost: u malých obcí je vhodné kontrolovat i absolutní hodnoty."
        )

    return ""


def normalize_dimension(value) -> str:
    """Normalizuje název dimenze a aplikuje aliasy."""
    if pd.isna(value):
        return ""

    dim = str(value).strip()
    return DIMENSION_ALIASES.get(dim, dim)


def get_config_column(
    config: pd.DataFrame,
    candidates: list[str],
    required: bool = True,
) -> str | None:
    """Najde sloupec v configu podle více možných názvů."""
    lower_map = {c.lower().strip(): c for c in config.columns}

    for cand in candidates:
        key = cand.lower().strip()

        if key in lower_map:
            return lower_map[key]

    if required:
        raise ValueError(
            f"V configu chybí některý ze sloupců: {candidates}. "
            f"Dostupné sloupce: {list(config.columns)}"
        )

    return None


def load_inputs() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Načte config, geo_master a raw indikátory."""
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Chybí config: {CONFIG_PATH}")

    if not GEO_MASTER_PATH.exists():
        raise FileNotFoundError(f"Chybí geo_master: {GEO_MASTER_PATH}")

    if not RAW_INDICATORS_PATH.exists():
        raise FileNotFoundError(f"Chybí raw indikátory: {RAW_INDICATORS_PATH}")

    config = read_csv_smart(CONFIG_PATH)
    geo = read_csv_smart(GEO_MASTER_PATH)
    raw = read_csv_smart(RAW_INDICATORS_PATH)

    for df in [geo, raw]:
        if "kod_obce" not in df.columns:
            raise ValueError("Vstupní CSV musí obsahovat sloupec kod_obce.")

        df["kod_obce"] = df["kod_obce"].map(clean_code)

    if "population" not in raw.columns:
        if "population" in geo.columns:
            raw = raw.merge(
                geo[["kod_obce", "population"]],
                on="kod_obce",
                how="left",
                suffixes=("", "_geo"),
            )
        else:
            raise ValueError("Chybí population v raw i geo_master.")

    raw["population"] = pd.to_numeric(raw["population"], errors="coerce")

    return config, geo, raw


def add_size_categories(
    raw: pd.DataFrame,
    geo: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Přidá finální velikostní kategorie do raw i geo_master."""
    raw = raw.copy()
    geo = geo.copy()

    for df in [raw, geo]:
        if "population" in df.columns:
            df["population"] = pd.to_numeric(df["population"], errors="coerce")
            df["size_category_final"] = df["population"].map(assign_size_category_final)
            df["settlement_type"] = df["population"].map(assign_settlement_type)
            df["volatility_warning"] = df["population"].map(assign_volatility_warning)

    return raw, geo


def robust_score(series: pd.Series, direction: str) -> tuple[pd.Series, dict]:
    """
    Spočítá robustní skóre 0–100:
    1. ořez 5.–95. percentil,
    2. min-max standardizace,
    3. směr UP / DOWN.
    """
    values = pd.to_numeric(series, errors="coerce")
    valid = values.dropna()

    direction_clean = str(direction).strip().upper()

    if valid.empty:
        score = pd.Series(pd.NA, index=series.index, dtype="Float64")
        stats = {
            "q05": None,
            "q95": None,
            "n_valid": 0,
            "n_below_q05": 0,
            "n_above_q95": 0,
            "direction": direction_clean,
        }
        return score, stats

    q05 = valid.quantile(0.05)
    q95 = valid.quantile(0.95)

    n_below = int((valid < q05).sum())
    n_above = int((valid > q95).sum())

    if q95 == q05:
        score = pd.Series(pd.NA, index=series.index, dtype="Float64")
        score.loc[values.notna()] = 50.0
    else:
        clipped = values.clip(lower=q05, upper=q95)

        if direction_clean == "DOWN":
            score = (q95 - clipped) / (q95 - q05) * 100
        else:
            score = (clipped - q05) / (q95 - q05) * 100

        score = score.clip(lower=0, upper=100)

    stats = {
        "q05": q05,
        "q95": q95,
        "n_valid": int(valid.shape[0]),
        "n_below_q05": n_below,
        "n_above_q95": n_above,
        "direction": direction_clean,
    }

    return score.round(2), stats


def build_scores(
    config: pd.DataFrame,
    raw: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Vypočítá indikátorová a dimenzionální skóre podle configu."""
    indicator_col = get_config_column(config, ["indicator_id"])
    dimension_col = get_config_column(config, ["dimension"])
    direction_col = get_config_column(config, ["direction", "smer"])
    role_col = get_config_column(config, ["role", "typ"], required=False)
    selected_col = get_config_column(config, ["selected_for_mvp", "aktivni"], required=False)

    cfg = config.copy()

    if selected_col is not None:
        cfg = cfg[
            cfg[selected_col]
            .astype(str)
            .str.strip()
            .isin(["1", "true", "True", "TRUE"])
        ].copy()

    if role_col is not None:
        cfg = cfg[
            cfg[role_col]
            .astype(str)
            .str.strip()
            .str.lower()
            .isin(["score", "core", "struct"])
        ].copy()

    id_cols = [
        "kod_obce",
        "obec",
        "okres",
        "orp",
        "kraj",
        "population",
        "size_category",
        "size_category_final",
        "settlement_type",
        "volatility_warning",
    ]

    scores = raw[[c for c in id_cols if c in raw.columns]].copy()

    stats_rows = []
    score_columns_by_dimension: dict[str, list[str]] = {}

    for _, row in cfg.iterrows():
        indicator_id = str(row[indicator_col]).strip()

        if not indicator_id:
            continue

        if indicator_id not in raw.columns:
            print(f"[WARN] Indikátor {indicator_id} není v raw datech, přeskakuji.")
            continue

        dimension = normalize_dimension(row[dimension_col])
        direction = str(row[direction_col]).strip().upper()

        score_col = f"{indicator_id}_score"

        score, stats = robust_score(raw[indicator_id], direction=direction)

        scores[score_col] = score
        score_columns_by_dimension.setdefault(dimension, []).append(score_col)

        stats_rows.append(
            {
                "indicator_id": indicator_id,
                "dimension": dimension,
                "direction": direction,
                "score_column": score_col,
                **stats,
            }
        )

        print(
            f"[OK] {indicator_id}: score={score_col}, "
            f"direction={direction}, q05={stats['q05']}, q95={stats['q95']}"
        )

    stats_df = pd.DataFrame(stats_rows)

    dimension_scores = scores[[c for c in id_cols if c in scores.columns]].copy()

    for dimension in DIMENSION_OUTPUT_ORDER:
        cols = score_columns_by_dimension.get(dimension, [])

        if not cols:
            continue

        out_col = f"{dimension}_score"
        dimension_scores[out_col] = scores[cols].mean(axis=1, skipna=True).round(2)

    for dimension, cols in score_columns_by_dimension.items():
        out_col = f"{dimension}_score"

        if out_col in dimension_scores.columns:
            continue

        dimension_scores[out_col] = scores[cols].mean(axis=1, skipna=True).round(2)

    return scores, dimension_scores, stats_df


def write_outputs(
    raw: pd.DataFrame,
    geo: pd.DataFrame,
    scores: pd.DataFrame,
    dimension_scores: pd.DataFrame,
    stats: pd.DataFrame,
) -> None:
    """Zapíše výstupy a metodický souhrn."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    raw.to_csv(RAW_INDICATORS_PATH, index=False, encoding="utf-8-sig")
    geo.to_csv(GEO_MASTER_PATH, index=False, encoding="utf-8-sig")
    scores.to_csv(MUNICIPALITY_SCORES_OUT, index=False, encoding="utf-8-sig")
    dimension_scores.to_csv(DIMENSION_SCORES_OUT, index=False, encoding="utf-8-sig")
    stats.to_csv(SCORING_STATS_OUT, index=False, encoding="utf-8-sig")

    lines = []
    lines.append("# Metodická aktualizace skóre a kategorií\n")

    lines.append("## Velikostní kategorie\n")
    lines.append(
        "Obce jsou rozděleny do finálních velikostních kategorií, které kombinují "
        "datovou logiku a interpretovatelnost. U menších obcí je členění jemnější, "
        "protože ukazatele přepočítané na obyvatele jsou volatilnější. U větších měst "
        "jsou kategorie určeny také podle sídelní funkce."
    )
    lines.append("")
    lines.append("| Kategorie | Interpretace |")
    lines.append("|---|---|")
    lines.append("| 0-499 | mikroobce |")
    lines.append("| 500-999 | malé obce I |")
    lines.append("| 1000-1999 | malé obce II |")
    lines.append("| 2000-4999 | větší obce / městyse |")
    lines.append("| 5000-14999 | malá města |")
    lines.append("| 15000-29999 | menší střední města |")
    lines.append("| 30000-49999 | střední města |")
    lines.append("| 50000-99999 | velká města |")
    lines.append("| 100000+ | metropole / největší města |")

    lines.append("\n## Ošetření extrémních hodnot\n")
    lines.append(
        "Pro výpočet skóre jsou hodnoty indikátorů ořezány na 5. a 95. percentilu. "
        "Následně je provedena min-max standardizace na škále 0-100. Směr indikátoru "
        "je určen v configu hodnotou UP nebo DOWN. Surové hodnoty se nepřepisují a "
        "zůstávají zobrazené v dashboardu."
    )

    lines.append("\n## Varování u malých obcí\n")
    lines.append(
        "U mikroobcí a malých obcí je do dat přidán sloupec volatility_warning. "
        "Dashboard ho může zobrazit jako upozornění, že přepočet na 1000 obyvatel "
        "může být ovlivněn malými absolutními počty."
    )

    lines.append("\n## Výstupy\n")
    lines.append("- municipality_indicators_raw.csv: surové hodnoty + kategorie + varování")
    lines.append("- municipality_scores.csv: skóre jednotlivých indikátorů")
    lines.append("- dimension_scores.csv: agregovaná dimenzionální skóre")
    lines.append("- indicator_scoring_stats.csv: percentily a počty ořezaných hodnot")

    SUMMARY_OUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"[OK] Aktualizován raw indicators: {RAW_INDICATORS_PATH}")
    print(f"[OK] Aktualizován geo_master: {GEO_MASTER_PATH}")
    print(f"[OK] Municipality scores: {MUNICIPALITY_SCORES_OUT}")
    print(f"[OK] Dimension scores: {DIMENSION_SCORES_OUT}")
    print(f"[OK] Scoring stats: {SCORING_STATS_OUT}")
    print(f"[OK] Summary: {SUMMARY_OUT}")


def run() -> None:
    """Hlavní běh skriptu."""
    config, geo, raw = load_inputs()

    raw, geo = add_size_categories(raw, geo)

    scores, dimension_scores, stats = build_scores(config, raw)

    write_outputs(raw, geo, scores, dimension_scores, stats)

    mor = dimension_scores[dimension_scores["kod_obce"].astype(str).eq("540480")]

    if not mor.empty:
        print("")
        print("Kontrola Moravičany:")
        print(mor.to_string(index=False))

    print("")
    print("[OK] Metodická aktualizace dokončena.")


if __name__ == "__main__":
    run()