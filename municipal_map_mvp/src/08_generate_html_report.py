 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
OUTPUTS = ROOT / "outputs"


def read_csv_smart(path):
    for enc in ["utf-8-sig", "utf-8", "cp1250", "windows-1250", "latin-1"]:
        try:
            return pd.read_csv(path, encoding=enc)
        except Exception:
            pass
    raise RuntimeError(f"Nepodařilo se načíst soubor: {path}")


def main():
    scores = read_csv_smart(PROCESSED / "dimension_scores.csv")
    raw = read_csv_smart(PROCESSED / "municipality_indicators_raw.csv")

    raw_cols = [
        "kod_obce",
        "migration_balance_per_1000",
        "natural_increase",
        "unemployment_rate",
        "completed_flats_per_1000",
        "ecological_stability_coef",
    ]

    df = scores.merge(raw[raw_cols], on="kod_obce", how="left")

    cols = [
        "kod_obce",
        "obec",
        "okres",
        "orp",
        "population",
        "size_category",
        "demography_score",
        "labour_score",
        "housing_score",
        "environment_score",
        "migration_balance_per_1000",
        "natural_increase",
        "unemployment_rate",
        "completed_flats_per_1000",
        "ecological_stability_coef",
    ]

    df = df[[c for c in cols if c in df.columns]].copy()

    for col in df.columns:
        if col not in ["kod_obce", "obec", "okres", "orp", "size_category"]:
            df[col] = pd.to_numeric(df[col], errors="coerce").round(2)

    moravicany = df[
        df["kod_obce"].astype(str).str.replace(".0", "", regex=False).eq("540480")
    ]

    html_parts = [
        "<!doctype html>",
        "<html lang='cs'>",
        "<head>",
        "<meta charset='utf-8'>",
        "<title>Datová mapa obcí ČR - MVP report</title>",
        "</head>",
        "<body>",
        "<h1>Datová mapa kvality a rozvoje obcí ČR - MVP report</h1>",
        "<p>Záložní nemapový výstup: skóre dimenzí 0-100 a surové indikátory obcí.</p>",
        "<h2>Případová obec: Moravičany</h2>",
        moravicany.to_html(index=False),
        "<h2>Všechny obce</h2>",
        df.to_html(index=False),
        "</body>",
        "</html>",
    ]

    html = "\n".join(html_parts)

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    out = OUTPUTS / "municipality_report.html"
    out.write_text(html, encoding="utf-8")

    print(f"[OK] HTML report uložen: {out}")


if __name__ == "__main__":
    main()