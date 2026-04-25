from __future__ import annotations

"""End-to-end CZSO pipeline for IKZ dataset selection, ranking, and previewing.

This module does three things in one workflow:
1. selects all relevant datasets from ``Katalog_trideny`` except
   ``referenční / technická``;
2. downloads / profiles each dataset and classifies it into A/B/C/D based on
   target years and presence of a municipality-level primary key;
3. saves and optionally displays head()/tail() previews ordered from A to D.

It is designed for Anaconda + Jupyter and reuses the existing ``pyczso.py``
(DataStat) and ``pyczso_lkod_bridge.py`` (LKOD/VDB) helpers.
"""

import argparse
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
import json
import re
import shutil
import sys
import tempfile
import time
import traceback
import unicodedata
import zipfile
from typing import Any, Iterable, Sequence

import pandas as pd

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

import pyczso  # noqa: E402
from pyczso_lkod_bridge import LKODBridge, detect_encoding, guess_column  # noqa: E402

try:
    from IPython.display import Markdown, display  # type: ignore
except Exception:  # pragma: no cover
    Markdown = None
    display = None


TARGET_YEARS_DEFAULT = [2023, 2024]
PROBE_ROWS_DEFAULT = 250
EXCLUDED_RELEVANCE = {"referenční / technická"}
RELEVANCE_ORDER = {
    "jádrová pro IKŽ": 0,
    "podpůrná / kontextová": 1,
    "volitelná / specializovaná": 2,
    "referenční / technická": 9,
}
CATEGORY_ORDER = {"A": 0, "B": 1, "C": 2, "D": 3}
YEAR_RE = re.compile(r"(?<!\d)(18\d{2}|19\d{2}|20\d{2}|2100)(?!\d)")

# Municipality-level primary key candidates.
PK_EXACT_CANDIDATES = {
    "obeckod",
    "obec_kod",
    "kodobce",
    "kod_obce",
    "kodobcezuj",
    "kod_obce_zuj",
    "obecid",
    "obec_id",
    "idobce",
    "id_obce",
    "obeccode",
    "obec_code",
    "zuj",
    "zujkod",
    "zuj_kod",
    "kodzuj",
    "kod_zuj",
    "kodobceruian",
    "kod_obce_ruian",
}
PK_EQUIV_CANDIDATES = {
    "uzemikod",
    "uzemi_kod",
    "vuzemikod",
    "vuzemi_kod",
    "uzemicode",
    "uzemi_code",
    "vuzemicode",
    "vuzemi_code",
    "uzemicis",
    "uzemi_cis",
    "vuzemicis",
    "vuzemi_cis",
    "uzemiid",
    "uzemi_id",
    "vuzemiid",
    "vuzemi_id",
    "uzemi",
    "vuzemi",
}
PK_HINT_TOKEN_SETS = [
    {"obec", "kod"},
    {"obec", "id"},
    {"obec", "cis"},
    {"obec", "zuj"},
    {"kod", "zuj"},
]
TIME_NAME_KEYWORDS = {
    "rok", "year", "datum", "date", "casref", "obdobi", "period",
    "mesic", "month", "ctvrtleti", "quarter", "tyden", "week",
    "sldbrok", "sldbdatum", "casrefod", "casrefdo",
}
DESCRIPTIVE_NAME_KEYWORDS = {"txt", "text", "nazev", "popis", "label", "desc", "description"}
MUNICIPALITY_POSITIVE_HINTS = [
    "obec",
    "obce",
    "obcich",
    "obci",
    "mestskeobvody",
    "mestskeobvodyacasti",
    "zuj",
]
MUNICIPALITY_NEGATIVE_HINTS = [
    "podobecni",
    "castobce",
    "castobcedil",
    "zsj",
    "zsjd",
    "zdj",
    "orp",
    "okres",
    "kraj",
    "krajesoudrznosti",
]
@dataclass
class TablePreview:
    head_df: pd.DataFrame | None
    tail_df: pd.DataFrame | None
    row_count: int | None
    column_count: int | None
    column_names: list[str]
    time_columns: list[str]
    years: list[int]
    years_source: str | None
    selected_file: str | None
    selected_sheet: str | None
    selected_format: str | None
    notes: str | None = None


@dataclass
class DatasetAssessment:
    order: int
    category: str
    category_reason: str
    relevance_pro_ikz: str | None
    relevance_rank: int
    dataset_id: str | None
    dataset_title: str | None
    rodina_datasetu: str | None
    hlavni_skupina: str | None
    detailni_skupina: str | None
    uzemni_uroven: str | None
    zdroj_typ: str | None
    status: str
    source_kind: str | None
    source_code: str | None
    source_title: str | None
    selected_file: str | None
    selected_sheet: str | None
    selected_format: str | None
    row_count: int | None
    column_count: int | None
    time_columns: str | None
    years_min: int | None
    years_max: int | None
    years_count: int | None
    years_sample: str | None
    years_source: str | None
    has_target_years: bool | None
    target_years_present: str | None
    target_years_missing: str | None
    has_primary_key: bool | None
    primary_key_column: str | None
    primary_key_kind: str | None
    primary_key_note: str | None
    start_catalog: str | None
    end_catalog: str | None
    periodicita_text: str | None
    head_csv: str | None
    tail_csv: str | None
    metadata_json: str | None
    page: str | None
    error: str | None


# ---------------------------------------------------------------------------
# Basic helpers
# ---------------------------------------------------------------------------


def clean_string(value: Any) -> str | None:
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except Exception:
        pass
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    text = str(value).strip()
    return text or None



def normalize_name(value: Any) -> str:
    text = str(value)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    return re.sub(r"[^a-z0-9]+", "", text)



def sanitize_filename(value: str, max_len: int = 100) -> str:
    text = unicodedata.normalize("NFKD", value)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"\s+", "_", text.strip())
    text = re.sub(r"[^0-9A-Za-z_\-]+", "", text)
    text = text.strip("._-")
    if not text:
        text = "dataset"
    if len(text) > max_len:
        text = text[:max_len].rstrip("._-")
    return text or "dataset"



def _split_name_tokens(value: Any) -> list[str]:
    text = str(value)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    tokens = re.split(r"[^a-z0-9]+", text)
    return [token for token in tokens if token]


def extract_years_from_value(value: Any) -> list[int]:
    years: set[int] = set()
    if value is None:
        return []
    try:
        if pd.isna(value):
            return []
    except Exception:
        pass

    if hasattr(value, "year") and not isinstance(value, str):
        try:
            year = int(value.year)
            if 1800 <= year <= 2100:
                years.add(year)
                return sorted(years)
        except Exception:
            pass

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        try:
            if float(value).is_integer():
                digits = str(int(value))
                if len(digits) == 4 and digits.startswith(("18", "19", "20")):
                    years.add(int(digits))
                elif len(digits) in {6, 8} and digits[:4].startswith(("19", "20")):
                    year = int(digits[:4])
                    if 1800 <= year <= 2100:
                        years.add(year)
        except Exception:
            pass

    text = str(value).strip()
    if not text:
        return []

    for match in YEAR_RE.findall(text):
        year = int(match)
        if 1800 <= year <= 2100:
            years.add(year)

    compact = re.sub(r"\s+", "", text)
    if re.fullmatch(r"(18|19|20)\d{2}(0[1-9]|1[0-2])", compact):
        years.add(int(compact[:4]))
    if re.fullmatch(r"(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])", compact):
        years.add(int(compact[:4]))

    return sorted(years)


def years_from_strings(values: Iterable[Any]) -> list[int]:
    years: set[int] = set()
    for value in values:
        years.update(extract_years_from_value(value))
    return sorted(years)


def series_years(series: pd.Series, *, limit: int | None = None) -> list[int]:
    values = series.dropna()
    if limit is not None:
        values = values.head(limit)
    return years_from_strings(values.tolist())


def format_years_sample(years: Sequence[int], max_items: int = 12) -> str | None:
    years = sorted(dict.fromkeys(int(y) for y in years))
    if not years:
        return None
    if len(years) <= max_items:
        return ", ".join(str(y) for y in years)
    front = max_items // 2
    back = max_items - front
    return ", ".join(str(y) for y in years[:front]) + " ... " + ", ".join(str(y) for y in years[-back:])


def dataframe_to_pretty_string(df: pd.DataFrame | None) -> str:
    if df is None or df.empty:
        return "<prázdné>"
    with pd.option_context(
        "display.max_rows", None,
        "display.max_columns", None,
        "display.width", 240,
        "display.max_colwidth", 120,
    ):
        return df.to_string(index=False)


def is_time_like_column_name(column_name: Any) -> bool:
    tokens = _split_name_tokens(column_name)
    compact = normalize_name(column_name)
    token_set = set(tokens)

    if compact in TIME_NAME_KEYWORDS:
        return True
    if token_set & DESCRIPTIVE_NAME_KEYWORDS:
        strong_desc = token_set & {"txt", "text", "label", "desc", "description", "nazev", "popis"}
        if strong_desc and not (token_set & {"datum", "date", "casref", "rok", "year"}):
            return False
    if token_set & TIME_NAME_KEYWORDS:
        return True
    if any(compact.startswith(prefix) for prefix in ["casref", "sldbrok", "sldbdatum"]):
        return True
    return False


def detect_time_columns_from_probe(df: pd.DataFrame) -> list[str]:
    if df is None or df.empty:
        return []

    out: list[str] = []
    for col in df.columns:
        if is_time_like_column_name(col):
            out.append(str(col))
            continue

        series = df[col].dropna().head(100)
        if series.empty:
            continue
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            out.append(str(col))
            continue

        token_set = set(_split_name_tokens(col))
        if token_set & DESCRIPTIVE_NAME_KEYWORDS:
            continue

        parsed = years_from_strings(series.tolist())
        if len(parsed) >= 2:
            out.append(str(col))
            continue

        date_like_hits = 0
        for txt in [str(v).strip() for v in series.tolist()[:100]]:
            compact = re.sub(r"\s+", "", txt)
            if re.fullmatch(r"(18|19|20)\d{2}(0[1-9]|1[0-2])", compact):
                date_like_hits += 1
            elif re.fullmatch(r"(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])", compact):
                date_like_hits += 1
        threshold = max(3, min(10, len(series) // 3 if len(series) else 0))
        if date_like_hits >= threshold:
            out.append(str(col))

    return list(dict.fromkeys(out))
def parse_catalog_years(start_value: Any, end_value: Any) -> list[int]:
    years: set[int] = set()
    for value in [start_value, end_value]:
        if value is None:
            continue
        text = str(value)
        for year in years_from_strings([text]):
            years.add(year)
    if len(years) == 2:
        lo, hi = min(years), max(years)
        if 1800 <= lo <= hi <= 2100 and (hi - lo) <= 50:
            return list(range(lo, hi + 1))
    return sorted(years)


# ---------------------------------------------------------------------------
# Catalogue selection
# ---------------------------------------------------------------------------


def read_catalogue(path: Path, *, sheet_name: str = "Katalog_trideny") -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name=sheet_name)
    if "dataset_id" not in df.columns:
        raise ValueError("List Katalog_trideny musí obsahovat sloupec 'dataset_id'.")
    if "title" not in df.columns and "rodina_datasetu" not in df.columns:
        raise ValueError("List Katalog_trideny musí obsahovat 'title' nebo 'rodina_datasetu'.")
    return df



def select_relevant_datasets(catalogue: pd.DataFrame) -> pd.DataFrame:
    df = catalogue.copy()
    if "relevance_pro_IKZ" in df.columns:
        df["relevance_pro_IKZ"] = df["relevance_pro_IKZ"].map(clean_string)
        df = df[~df["relevance_pro_IKZ"].isin(EXCLUDED_RELEVANCE)].copy()
    else:
        df["relevance_pro_IKZ"] = None
    df["dataset_id"] = df["dataset_id"].map(clean_string)
    df["dataset_title"] = df["title"].map(clean_string) if "title" in df.columns else None
    if "rodina_datasetu" not in df.columns:
        df["rodina_datasetu"] = df["dataset_title"]
    df["rodina_datasetu"] = df["rodina_datasetu"].map(clean_string)
    df["dataset_title"] = df["dataset_title"].fillna(df["rodina_datasetu"])
    df["relevance_rank"] = df["relevance_pro_IKZ"].map(RELEVANCE_ORDER).fillna(99).astype(int)
    df["_input_order"] = range(1, len(df) + 1)
    # Stable pre-sort before actual profiling.
    df = df.sort_values(["relevance_rank", "hlavni_skupina", "detailni_skupina", "dataset_title", "dataset_id"], na_position="last").reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# DataStat selection helper
# ---------------------------------------------------------------------------


def choose_selection(selections: pd.DataFrame) -> tuple[str | None, str | None, int]:
    if selections is None or selections.empty:
        return None, None, 0
    df = selections.copy()
    code_col = guess_column(df, ["kodVyberu", "kod_vyberu", "kod", "selection_code", "vyberKod", "kodvyberu"])
    title_col = guess_column(df, ["nazevVyberu", "nazev_vyberu", "nazev", "title", "selection_title", "nazevvyberu"])
    default_col = guess_column(df, ["vychozi", "jeVychozi", "default", "defaultni"])
    version_col = guess_column(df, ["verzeVyberu", "verze", "version"])
    modified_col = guess_column(df, ["datumAktualizace", "modified", "updated", "zmeneno", "casZmenyDefinice"])
    if code_col is None:
        return None, None, len(df)

    if default_col is not None:
        df["_default_rank"] = (
            df[default_col]
            .fillna(False)
            .astype(str)
            .str.strip()
            .str.lower()
            .isin(["true", "1", "ano", "yes"])  # type: ignore[arg-type]
            .astype(int)
        )
    else:
        df["_default_rank"] = 0

    if version_col is not None:
        df["_version_rank"] = pd.to_numeric(df[version_col], errors="coerce").fillna(-1)
    else:
        df["_version_rank"] = -1

    if modified_col is not None:
        df["_modified_rank"] = pd.to_datetime(df[modified_col], errors="coerce").fillna(pd.Timestamp("1900-01-01"))
    else:
        df["_modified_rank"] = pd.Timestamp("1900-01-01")

    if title_col is not None:
        text = df[title_col].fillna("").astype(str).str.lower()
        df["_title_rank"] = (
            text.str.contains(r"\b(celkem|vse|vsechno|vše|total)\b", regex=True).astype(int) * 3
            + text.str.contains(r"\b(obec|obce|kraj|kraje)\b", regex=True).astype(int)
            - text.str.contains(r"\b(test|archiv|historie)\b", regex=True).astype(int)
        )
    else:
        df["_title_rank"] = 0

    best = df.sort_values(["_default_rank", "_title_rank", "_version_rank", "_modified_rank"], ascending=[False, False, False, False]).iloc[0]
    code = clean_string(best[code_col])
    title = clean_string(best[title_col]) if title_col is not None else None
    return code, title, len(df)


# ---------------------------------------------------------------------------
# File loading / profiling
# ---------------------------------------------------------------------------


def read_bytes_head(path: Path, size: int = 200000) -> bytes:
    with path.open("rb") as f:
        return f.read(size)



def csv_read_attempts(path: Path, **kwargs: Any) -> pd.DataFrame:
    raw = read_bytes_head(path)
    last_exc: Exception | None = None
    for enc in detect_encoding(raw):
        try:
            return pd.read_csv(path, encoding=enc, sep=None, engine="python", **kwargs)
        except Exception as exc:
            last_exc = exc
    raise RuntimeError(f"CSV reading failed for {path.name}: {last_exc}")



def load_csv_preview(
    path: Path,
    *,
    head_rows: int,
    tail_rows: int,
    chunksize: int = 50000,
    probe_rows: int = PROBE_ROWS_DEFAULT,
) -> TablePreview:
    probe_nrows = max(head_rows, probe_rows)
    probe_df = csv_read_attempts(path, nrows=probe_nrows)
    head_df = probe_df.head(head_rows).copy()
    column_names = [str(c) for c in probe_df.columns]
    column_count = len(column_names)
    time_columns = detect_time_columns_from_probe(probe_df)
    header_years = years_from_strings(column_names)
    years: set[int] = set(header_years)
    years_source: str | None = "header_columns" if header_years else None

    total_rows = 0
    tail_df: pd.DataFrame | None = None
    raw = read_bytes_head(path)
    last_exc: Exception | None = None
    for enc in detect_encoding(raw):
        try:
            for chunk in pd.read_csv(path, encoding=enc, sep=None, engine="python", chunksize=chunksize):
                total_rows += len(chunk)
                if tail_df is None:
                    tail_df = chunk.tail(tail_rows).copy()
                else:
                    tail_df = pd.concat([tail_df, chunk], ignore_index=True).tail(tail_rows).copy()
                for col in time_columns:
                    if col in chunk.columns:
                        years.update(series_years(chunk[col]))
            last_exc = None
            break
        except Exception as exc:
            total_rows = 0
            tail_df = None
            years = set(header_years)
            last_exc = exc
            continue
    if last_exc is not None:
        raise RuntimeError(f"CSV streaming failed for {path.name}: {last_exc}")
    if years and time_columns:
        years_source = "data_columns"
    return TablePreview(
        head_df=head_df,
        tail_df=tail_df,
        row_count=int(total_rows),
        column_count=int(column_count),
        column_names=column_names,
        time_columns=time_columns,
        years=sorted(years),
        years_source=years_source,
        selected_file=path.name,
        selected_sheet=None,
        selected_format="csv",
        notes="roky a tail načteny z celého souboru po chunkách",
    )
def load_excel_preview(
    path: Path,
    *,
    head_rows: int,
    tail_rows: int,
    probe_rows: int = PROBE_ROWS_DEFAULT,
) -> TablePreview:
    full = pd.read_excel(path)
    head_df = full.head(head_rows).copy()
    tail_df = full.tail(tail_rows).copy()
    probe_df = full.head(max(head_rows, probe_rows)).copy()
    column_names = [str(c) for c in full.columns]
    time_columns = detect_time_columns_from_probe(probe_df)
    years = years_from_strings(column_names)
    years_source: str | None = "header_columns" if years else None
    if time_columns:
        extracted: set[int] = set(years)
        for col in time_columns:
            if col in full.columns:
                extracted.update(series_years(full[col]))
        years = sorted(extracted)
        if extracted:
            years_source = "data_columns"
    return TablePreview(
        head_df=head_df,
        tail_df=tail_df,
        row_count=int(len(full)),
        column_count=int(len(full.columns)),
        column_names=column_names,
        time_columns=time_columns,
        years=sorted(dict.fromkeys(years)),
        years_source=years_source,
        selected_file=path.name,
        selected_sheet=None,
        selected_format=path.suffix.lower().lstrip("."),
        notes="roky a tail načteny z celého sešitu",
    )
def choose_archive_table_file(files: list[Path]) -> Path:
    def score(path: Path) -> tuple[int, int, int, str]:
        name = normalize_name(path.name)
        ext_score = 100 if path.suffix.lower() == ".csv" else 60 if path.suffix.lower() in {".xlsx", ".xls", ".xlsm"} else 0
        penalty = 0
        for bad in ["readme", "schema", "meta", "ciselnik", "codebook", "documentation", "popis"]:
            if bad in name:
                penalty -= 30
        size_score = int(min(path.stat().st_size / 1_000_000, 200)) if path.exists() else 0
        return (ext_score + penalty + size_score, size_score, -len(path.parts), path.name)

    return sorted(files, key=score, reverse=True)[0]



def remove_path_quietly(path: Path | None) -> None:
    if path is None:
        return
    try:
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
        elif path.exists():
            path.unlink(missing_ok=True)
    except Exception:
        pass


def clear_directory_contents(path: Path) -> None:
    if not path.exists() or not path.is_dir():
        return
    for child in path.iterdir():
        remove_path_quietly(child)


def load_zip_preview(path: Path, *, head_rows: int, tail_rows: int) -> TablePreview:
    temp_prefix = f"extract_{sanitize_filename(path.stem, max_len=40)}_"
    with tempfile.TemporaryDirectory(dir=path.parent, prefix=temp_prefix) as tmpdir:
        extract_dir = Path(tmpdir)
        with zipfile.ZipFile(path, "r") as zf:
            zf.extractall(extract_dir)
        candidates = [p for p in extract_dir.rglob("*") if p.is_file() and p.suffix.lower() in {".csv", ".xlsx", ".xls", ".xlsm"}]
        if not candidates:
            return TablePreview(
                head_df=None,
                tail_df=None,
                row_count=None,
                column_count=None,
                column_names=[],
                time_columns=[],
                years=[],
                years_source=None,
                selected_file=None,
                selected_sheet=None,
                selected_format="zip",
                notes="Archiv neobsahuje CSV/XLSX soubor, který by šel automaticky profilovat.",
            )
        chosen = choose_archive_table_file(candidates)
        if chosen.suffix.lower() == ".csv":
            preview = load_csv_preview(chosen, head_rows=head_rows, tail_rows=tail_rows)
        else:
            preview = load_excel_preview(chosen, head_rows=head_rows, tail_rows=tail_rows)
        note = f"Archiv obsahuje {len(candidates)} čitelných souborů; použit byl vybraný soubor `{chosen.name}`."
        preview.notes = note if not preview.notes else f"{preview.notes} | {note}"
        preview.selected_format = f"zip->{preview.selected_format}"
        preview.selected_file = chosen.name
        return preview


def load_dataframe_preview(
    df: pd.DataFrame,
    *,
    head_rows: int,
    tail_rows: int,
    selected_file: str | None = None,
    probe_rows: int = PROBE_ROWS_DEFAULT,
) -> TablePreview:
    head_df = df.head(head_rows).copy()
    tail_df = df.tail(tail_rows).copy()
    probe_df = df.head(max(head_rows, probe_rows)).copy()
    column_names = [str(c) for c in df.columns]
    time_columns = detect_time_columns_from_probe(probe_df)
    years = years_from_strings(column_names)
    years_source: str | None = "header_columns" if years else None
    if time_columns:
        extracted: set[int] = set(years)
        for col in time_columns:
            if col in df.columns:
                extracted.update(series_years(df[col]))
        years = sorted(extracted)
        if extracted:
            years_source = "data_columns"
    return TablePreview(
        head_df=head_df,
        tail_df=tail_df,
        row_count=int(len(df)),
        column_count=int(len(df.columns)),
        column_names=column_names,
        time_columns=time_columns,
        years=years,
        years_source=years_source,
        selected_file=selected_file,
        selected_sheet=None,
        selected_format="datastat_csv",
        notes="roky a tail načteny z celého DataFrame",
    )

# ---------------------------------------------------------------------------
# Fetch one dataset
# ---------------------------------------------------------------------------


def fetch_dataset_preview(
    datastat_client: pyczso.CZSOClient,
    lkod_bridge: LKODBridge,
    dataset_id: str,
    *,
    head_rows: int,
    tail_rows: int,
    download_dir: Path,
    force_redownload: bool,
    cleanup_downloaded_files: bool = True,
) -> tuple[TablePreview | None, str | None, str | None, str | None, str, str | None]:
    lkod_error: str | None = None
    local_path: Path | None = None
    try:
        try:
            pointer = lkod_bridge.download_resource(dataset_id, dest_dir=download_dir, force_redownload=force_redownload)
            local_path = Path(pointer["download_path"])
            ext = str(pointer.get("extension") or local_path.suffix.lstrip(".")).lower()
            source_title = clean_string(pointer.get("title")) or clean_string(pointer.get("format"))
            if ext == "csv":
                preview = load_csv_preview(local_path, head_rows=head_rows, tail_rows=tail_rows)
            elif ext in {"xlsx", "xls", "xlsm"}:
                preview = load_excel_preview(local_path, head_rows=head_rows, tail_rows=tail_rows)
            elif ext == "zip":
                preview = load_zip_preview(local_path, head_rows=head_rows, tail_rows=tail_rows)
            else:
                return None, "LKOD", f"resource#{pointer.get('resource_num')}", source_title, "UNSUPPORTED_FORMAT", f"Stažený formát `{ext}` není podporovaný pro preview head/tail."
            return preview, "LKOD", f"resource#{pointer.get('resource_num')}", source_title, "OK_LKOD", preview.notes
        except Exception as exc:
            lkod_error = str(exc)
    finally:
        if cleanup_downloaded_files:
            remove_path_quietly(local_path)

    try:
        selections = datastat_client.get_dataset_selections(dataset_id, as_frame=True)
    except Exception as exc:
        msg = f"LKOD/VDB selhalo: {lkod_error} | DataStat metadata selhala: {exc}" if lkod_error else f"DataStat metadata selhala: {exc}"
        return None, None, None, None, "ERROR_SELECTIONS", msg

    selection_code, selection_title, selection_count = choose_selection(selections)
    if not selection_code:
        msg = f"Nebyl nalezen použitelný výběr. Počet nalezených výběrů: {selection_count}"
        if lkod_error:
            msg = f"LKOD/VDB selhalo: {lkod_error} | {msg}"
        return None, "DATASTAT", None, None, "NO_SELECTION", msg

    try:
        df = datastat_client.get_table(selection_code, format="CSV")
    except Exception as exc:
        msg = f"Stažení DataStat výběru selhalo: {exc}"
        if lkod_error:
            msg = f"LKOD/VDB selhalo: {lkod_error} | {msg}"
        return None, "DATASTAT", selection_code, selection_title, "ERROR_TABLE", msg
    if not isinstance(df, pd.DataFrame):
        msg = "DataStat API nevrátilo DataFrame."
        if lkod_error:
            msg = f"LKOD/VDB selhalo: {lkod_error} | {msg}"
        return None, "DATASTAT", selection_code, selection_title, "ERROR_TABLE", msg

    preview = load_dataframe_preview(df, head_rows=head_rows, tail_rows=tail_rows, selected_file=f"selection_{selection_code}.csv")
    return preview, "DATASTAT", selection_code, selection_title, "OK_DATASTAT", lkod_error


# ---------------------------------------------------------------------------
# Primary key and category logic
# ---------------------------------------------------------------------------


def _concat_catalog_text(row: pd.Series) -> str:
    parts = [
        clean_string(row.get("dataset_title")),
        clean_string(row.get("rodina_datasetu")),
        clean_string(row.get("uzemni_uroven")),
        clean_string(row.get("detailni_skupina")),
        clean_string(row.get("description")),
    ]
    return " ".join(part for part in parts if part)



def infer_municipality_context(row: pd.Series, sample_df: pd.DataFrame | None) -> tuple[bool, str | None]:
    score = 0
    reasons: list[str] = []

    text = normalize_name(_concat_catalog_text(row))
    if any(hint in text for hint in [normalize_name(v) for v in MUNICIPALITY_POSITIVE_HINTS]):
        score += 2
        reasons.append("catalog_hints_obec")
    if any(hint in text for hint in [normalize_name(v) for v in MUNICIPALITY_NEGATIVE_HINTS]):
        score -= 2
        reasons.append("catalog_hints_non_obec")

    level = normalize_name(row.get("uzemni_uroven") or "")
    if "obec" in level:
        score += 3
        reasons.append("uzemni_uroven_obec")
    if any(token in level for token in ["podobecni", "castobce", "zsj", "zsjd", "zdj"]):
        score -= 2
        reasons.append("uzemni_uroven_submunicipal")

    if sample_df is not None and not sample_df.empty:
        norm_cols = {normalize_name(c): c for c in sample_df.columns}
        if "obeckod" in norm_cols or "obectxt" in norm_cols or (("uzemikod" in norm_cols or "vuzemikod" in norm_cols) and ("uzemitxt" in norm_cols or "vuzemitxt" in norm_cols)):
            score += 4
            reasons.append("sample_contains_municipality_columns")
        for type_candidate in ["uzemityp", "vuzemityp"]:
            if type_candidate in norm_cols:
                sample_values = sample_df[norm_cols[type_candidate]].dropna().astype(str).head(100).tolist()
                norm_values = [normalize_name(v) for v in sample_values]
                if any("obec" in v for v in norm_values):
                    score += 3
                    reasons.append(f"sample_{type_candidate}_has_obec")
                if norm_values and all(any(tok in v for tok in ["castobce", "zsj", "zsjd", "zdj"]) for v in norm_values):
                    score -= 2
                    reasons.append(f"sample_{type_candidate}_only_submunicipal")

    return score >= 2, ", ".join(reasons) if reasons else None



def preview_key_uniqueness_note(df: pd.DataFrame, column_name: str) -> str | None:
    if column_name not in df.columns or df.empty:
        return None
    try:
        series = df[column_name].dropna()
        if series.empty:
            return None
        if series.is_unique:
            return "hodnoty jsou v head preview unikátní"
        dup_ratio = 1.0 - (series.nunique(dropna=True) / max(len(series), 1))
        return f"v head preview se hodnoty opakují (odhad duplicity {dup_ratio:.0%})"
    except Exception:
        return None


def detect_primary_key(row: pd.Series, preview: TablePreview | None) -> tuple[bool | None, str | None, str | None, str | None]:
    if preview is None or preview.head_df is None:
        return None, None, None, "preview_nebyl_k_dispozici"

    columns = [str(c) for c in preview.column_names]
    norm_to_original = {normalize_name(c): c for c in columns}
    token_map = {str(c): set(_split_name_tokens(c)) for c in columns}
    municipality_context, context_note = infer_municipality_context(row, preview.head_df)

    for norm, original in norm_to_original.items():
        if norm in PK_EXACT_CANDIDATES:
            uniq_note = preview_key_uniqueness_note(preview.head_df, original)
            note = "nalezen přímý obecní klíč"
            if uniq_note:
                note = f"{note}; {uniq_note}"
            return True, original, "exact", note

    for original, tokens in token_map.items():
        if any(req.issubset(tokens) for req in PK_HINT_TOKEN_SETS):
            uniq_note = preview_key_uniqueness_note(preview.head_df, original)
            note = "sloupec názvem odpovídá obecnímu klíči"
            if uniq_note:
                note = f"{note}; {uniq_note}"
            return True, original, "exact-ish", note

    for norm, original in norm_to_original.items():
        if norm in PK_EQUIV_CANDIDATES:
            if municipality_context:
                note = f"územní kód použitelný jako obecní ekvivalent ({context_note})"
                uniq_note = preview_key_uniqueness_note(preview.head_df, original)
                if uniq_note:
                    note = f"{note}; {uniq_note}"
                return True, original, "equivalent", note
            return False, original, "territorial_non_municipal", f"nalezen územní kód, ale dataset nevypadá jako obecní ({context_note})"

    for original, tokens in token_map.items():
        compact = normalize_name(original)
        if municipality_context:
            if {"uzemi", "kod"}.issubset(tokens) or {"vuzemi", "kod"}.issubset(tokens):
                note = f"územní kód použitelný jako obecní ekvivalent ({context_note})"
                uniq_note = preview_key_uniqueness_note(preview.head_df, original)
                if uniq_note:
                    note = f"{note}; {uniq_note}"
                return True, original, "equivalent", note
            if {"uzemi", "cis"}.issubset(tokens) or {"vuzemi", "cis"}.issubset(tokens):
                note = f"územní číselník použitelný jako obecní ekvivalent ({context_note})"
                uniq_note = preview_key_uniqueness_note(preview.head_df, original)
                if uniq_note:
                    note = f"{note}; {uniq_note}"
                return True, original, "equivalent", note
            if compact in {"uzemi", "vuzemi"}:
                return True, original, "equivalent", f"obecní územní identifikátor bez suffixu ({context_note})"

    return False, None, None, context_note or "nebyl nalezen obecní klíč ani rozumný ekvivalent"
def target_years_status(
    years: Sequence[int] | None,
    *,
    target_years: Sequence[int],
    require_all: bool,
    row: pd.Series | None = None,
) -> tuple[bool | None, list[int], list[int], str | None]:
    if years:
        available = sorted(dict.fromkeys(int(y) for y in years))
        source = "data"
    else:
        available = parse_catalog_years(row.get("start") if row is not None else None, row.get("end") if row is not None else None)
        source = "catalog" if available else None
    if not available:
        return None, [], list(target_years), source

    target = sorted(dict.fromkeys(int(y) for y in target_years))
    present = [y for y in target if y in available]
    missing = [y for y in target if y not in available]
    if require_all:
        ok = len(missing) == 0
    else:
        ok = len(present) > 0
    return ok, present, missing, source



def classify_dataset(
    row: pd.Series,
    preview: TablePreview | None,
    *,
    status: str,
    target_years: Sequence[int],
    require_all_target_years: bool,
) -> tuple[str, str, bool | None, list[int], list[int], bool | None, str | None, str | None, str | None]:
    has_pk, pk_col, pk_kind, pk_note = detect_primary_key(row, preview)
    has_years, present_years, missing_years, years_basis = target_years_status(
        preview.years if preview is not None else None,
        target_years=target_years,
        require_all=require_all_target_years,
        row=row,
    )

    if status.startswith("OK"):
        if has_years is True and has_pk is True:
            return "A", f"obsahuje cílové roky ({years_basis}) a má primary key", has_years, present_years, missing_years, has_pk, pk_col, pk_kind, pk_note
        if has_years is True and has_pk is False:
            return "B", f"obsahuje cílové roky ({years_basis}), ale chybí primary key", has_years, present_years, missing_years, has_pk, pk_col, pk_kind, pk_note
        if has_years is False and has_pk is True:
            return "C", f"má primary key, ale neobsahuje cílové roky ({years_basis})", has_years, present_years, missing_years, has_pk, pk_col, pk_kind, pk_note
        return "D", "nesplňuje podmínky A/B/C", has_years, present_years, missing_years, has_pk, pk_col, pk_kind, pk_note

    # Failed or unsupported datasets always go to D so they are still visible.
    return "D", f"dataset se nepodařilo spolehlivě načíst ({status})", has_years, present_years, missing_years, has_pk, pk_col, pk_kind, pk_note


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------


def ensure_output_dirs(base_dir: Path) -> tuple[Path, Path, Path]:
    base_dir.mkdir(parents=True, exist_ok=True)
    previews_dir = base_dir / "previews"
    downloads_dir = base_dir / "_downloads"
    previews_dir.mkdir(parents=True, exist_ok=True)
    downloads_dir.mkdir(parents=True, exist_ok=True)
    return base_dir, previews_dir, downloads_dir



def write_preview_files(
    assessment_prefix: str,
    preview: TablePreview | None,
    previews_dir: Path,
) -> tuple[str | None, str | None, str | None]:
    head_rel: str | None = None
    tail_rel: str | None = None
    meta_rel: str | None = None

    if preview is not None and preview.head_df is not None:
        head_name = f"{assessment_prefix}_head.csv"
        preview.head_df.to_csv(previews_dir / head_name, index=False, encoding="utf-8-sig")
        head_rel = str(Path("previews") / head_name)
    if preview is not None and preview.tail_df is not None:
        tail_name = f"{assessment_prefix}_tail.csv"
        preview.tail_df.to_csv(previews_dir / tail_name, index=False, encoding="utf-8-sig")
        tail_rel = str(Path("previews") / tail_name)
    if preview is not None:
        meta_name = f"{assessment_prefix}_meta.json"
        metadata = {
            "row_count": preview.row_count,
            "column_count": preview.column_count,
            "column_names": preview.column_names,
            "time_columns": preview.time_columns,
            "years": preview.years,
            "years_source": preview.years_source,
            "selected_file": preview.selected_file,
            "selected_sheet": preview.selected_sheet,
            "selected_format": preview.selected_format,
            "notes": preview.notes,
        }
        (previews_dir / meta_name).write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
        meta_rel = str(Path("previews") / meta_name)
    return head_rel, tail_rel, meta_rel



def build_assessment_record(
    row: pd.Series,
    preview: TablePreview | None,
    *,
    order: int,
    category: str,
    category_reason: str,
    has_target_years: bool | None,
    present_years: list[int],
    missing_years: list[int],
    has_primary_key: bool | None,
    primary_key_column: str | None,
    primary_key_kind: str | None,
    primary_key_note: str | None,
    status: str,
    source_kind: str | None,
    source_code: str | None,
    source_title: str | None,
    head_csv: str | None,
    tail_csv: str | None,
    metadata_json: str | None,
    error: str | None,
) -> DatasetAssessment:
    years = preview.years if preview is not None else []
    return DatasetAssessment(
        order=order,
        category=category,
        category_reason=category_reason,
        relevance_pro_ikz=clean_string(row.get("relevance_pro_IKZ")),
        relevance_rank=int(row.get("relevance_rank", 99)),
        dataset_id=clean_string(row.get("dataset_id")),
        dataset_title=clean_string(row.get("dataset_title")) or clean_string(row.get("title")) or clean_string(row.get("rodina_datasetu")),
        rodina_datasetu=clean_string(row.get("rodina_datasetu")),
        hlavni_skupina=clean_string(row.get("hlavni_skupina")),
        detailni_skupina=clean_string(row.get("detailni_skupina")),
        uzemni_uroven=clean_string(row.get("uzemni_uroven")),
        zdroj_typ=clean_string(row.get("zdroj_typ")),
        status=status,
        source_kind=source_kind,
        source_code=source_code,
        source_title=source_title,
        selected_file=preview.selected_file if preview is not None else None,
        selected_sheet=preview.selected_sheet if preview is not None else None,
        selected_format=preview.selected_format if preview is not None else None,
        row_count=preview.row_count if preview is not None else None,
        column_count=preview.column_count if preview is not None else None,
        time_columns=", ".join(preview.time_columns) if preview and preview.time_columns else None,
        years_min=min(years) if years else None,
        years_max=max(years) if years else None,
        years_count=len(years) if years else 0,
        years_sample=format_years_sample(years),
        years_source=preview.years_source if preview is not None else None,
        has_target_years=has_target_years,
        target_years_present=", ".join(str(y) for y in present_years) if present_years else None,
        target_years_missing=", ".join(str(y) for y in missing_years) if missing_years else None,
        has_primary_key=has_primary_key,
        primary_key_column=primary_key_column,
        primary_key_kind=primary_key_kind,
        primary_key_note=primary_key_note,
        start_catalog=clean_string(row.get("start")),
        end_catalog=clean_string(row.get("end")),
        periodicita_text=clean_string(row.get("periodicita_text")),
        head_csv=head_csv,
        tail_csv=tail_csv,
        metadata_json=metadata_json,
        page=clean_string(row.get("page")),
        error=clean_string(error),
    )



def assessment_to_series(assessment: DatasetAssessment) -> pd.DataFrame:
    return pd.DataFrame({"hodnota": asdict(assessment)}).rename_axis("polozka")


DISPLAY_SUMMARY_FIELDS = [
    "target_years_present",
    "has_primary_key",
    "primary_key_column",
]


def assessment_display_series(assessment: DatasetAssessment) -> pd.DataFrame:
    payload = asdict(assessment)
    filtered = {key: payload.get(key) for key in DISPLAY_SUMMARY_FIELDS}
    return pd.DataFrame({"hodnota": filtered}).rename_axis("polozka")



def display_assessment_in_notebook(assessment: DatasetAssessment, head_df: pd.DataFrame | None, tail_df: pd.DataFrame | None) -> None:
    title = assessment.dataset_title or assessment.rodina_datasetu or assessment.dataset_id or "Dataset"
    heading = f"## {assessment.order:03d}. [{assessment.category}] {title}"
    if Markdown is None or display is None:
        print(heading)
        print(assessment_display_series(assessment))
        print("\nHEAD:\n", dataframe_to_pretty_string(head_df))
        print("\nTAIL:\n", dataframe_to_pretty_string(tail_df))
        return
    display(Markdown(heading))
    display(assessment_display_series(assessment))
    if head_df is not None:
        display(Markdown("**HEAD**"))
        display(head_df)
    if tail_df is not None:
        display(Markdown("**TAIL**"))
        display(tail_df)



def build_summary_tables(manifest_df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    out: dict[str, pd.DataFrame] = {}
    if manifest_df.empty:
        return out

    out["datasets_by_category"] = (
        manifest_df.groupby(["category", "relevance_pro_ikz"], dropna=False)
        .size()
        .reset_index(name="pocet_datasetu")
        .sort_values(["category", "pocet_datasetu", "relevance_pro_ikz"], ascending=[True, False, True])
        .reset_index(drop=True)
    )

    out["datasets_by_pk_and_years"] = (
        manifest_df.groupby(["has_primary_key", "has_target_years"], dropna=False)
        .size()
        .reset_index(name="pocet_datasetu")
        .sort_values(["has_primary_key", "has_target_years"], ascending=[False, False], na_position="last")
        .reset_index(drop=True)
    )

    out["datasets_by_status"] = (
        manifest_df.groupby("status", dropna=False)
        .size()
        .reset_index(name="pocet_datasetu")
        .sort_values("pocet_datasetu", ascending=False)
        .reset_index(drop=True)
    )
    return out



def write_markdown_report(output_dir: Path, manifest_df: pd.DataFrame, results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]]) -> Path:
    report_path = output_dir / "ikz_a_to_z_previews.md"
    lines: list[str] = []
    lines.append("# CZSO IKZ – end-to-end pipeline output")
    lines.append("")
    lines.append(f"Vygenerováno: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    if not manifest_df.empty:
        lines.append("## Souhrn")
        lines.append("")
        lines.append(manifest_df.groupby("category").size().to_string())
        lines.append("")

    current_category = None
    for assessment, head_df, tail_df in results:
        if assessment.category != current_category:
            current_category = assessment.category
            lines.append(f"# Kategorie {current_category}")
            lines.append("")
        title = assessment.dataset_title or assessment.dataset_id or "Dataset"
        lines.append(f"## {assessment.order:03d}. [{assessment.category}] {title}")
        lines.append("")
        lines.append(assessment_display_series(assessment).to_string())
        lines.append("")
        lines.append("### HEAD")
        lines.append("")
        lines.append("```")
        lines.append(dataframe_to_pretty_string(head_df))
        lines.append("```")
        lines.append("")
        lines.append("### TAIL")
        lines.append("")
        lines.append("```")
        lines.append(dataframe_to_pretty_string(tail_df))
        lines.append("```")
        lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


# ---------------------------------------------------------------------------
# Main workflow
# ---------------------------------------------------------------------------


def process_relevant_catalogue(
    catalog_xlsx: Path,
    *,
    output_dir: Path,
    target_years: Sequence[int] = TARGET_YEARS_DEFAULT,
    require_all_target_years: bool = True,
    head_rows: int = 5,
    tail_rows: int = 5,
    max_datasets: int | None = None,
    force_redownload: bool = False,
    cleanup_downloaded_files: bool = True,
    pause_seconds: float = 0.0,
    display_in_notebook: bool = False,
) -> tuple[pd.DataFrame, list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]]]:
    catalogue = read_catalogue(catalog_xlsx)
    relevant = select_relevant_datasets(catalogue)
    if max_datasets is not None:
        relevant = relevant.head(max_datasets).copy()

    out_dir, previews_dir, downloads_dir = ensure_output_dirs(output_dir)
    datastat_client = pyczso.CZSOClient()
    lkod_bridge = LKODBridge()
    results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]] = []

    try:
        for _, row in relevant.iterrows():
            dataset_id = clean_string(row.get("dataset_id"))
            title = clean_string(row.get("dataset_title")) or clean_string(row.get("rodina_datasetu")) or dataset_id or "dataset"
            print("=" * 100)
            print(f"Dataset: {dataset_id} :: {title}")

            preview: TablePreview | None = None
            source_kind: str | None = None
            source_code: str | None = None
            source_title: str | None = None
            status = "MISSING_DATASET_ID"
            error: str | None = None

            if dataset_id:
                try:
                    preview, source_kind, source_code, source_title, status, error = fetch_dataset_preview(
                        datastat_client,
                        lkod_bridge,
                        dataset_id,
                        head_rows=head_rows,
                        tail_rows=tail_rows,
                        download_dir=downloads_dir,
                        force_redownload=force_redownload,
                        cleanup_downloaded_files=cleanup_downloaded_files,
                    )
                except Exception as exc:  # pragma: no cover - defensive
                    status = "UNHANDLED_ERROR"
                    error = f"{exc}\n{traceback.format_exc()}"

            category, category_reason, has_target_years, present_years, missing_years, has_pk, pk_col, pk_kind, pk_note = classify_dataset(
                row,
                preview,
                status=status,
                target_years=target_years,
                require_all_target_years=require_all_target_years,
            )

            prefix = f"{sanitize_filename(category)}_{sanitize_filename(dataset_id or 'none')}_{sanitize_filename(title, max_len=60)}"
            head_csv, tail_csv, meta_json = write_preview_files(prefix, preview, previews_dir)

            assessment = build_assessment_record(
                row,
                preview,
                order=0,  # assigned after final sort
                category=category,
                category_reason=category_reason,
                has_target_years=has_target_years,
                present_years=present_years,
                missing_years=missing_years,
                has_primary_key=has_pk,
                primary_key_column=pk_col,
                primary_key_kind=pk_kind,
                primary_key_note=pk_note,
                status=status,
                source_kind=source_kind,
                source_code=source_code,
                source_title=source_title,
                head_csv=head_csv,
                tail_csv=tail_csv,
                metadata_json=meta_json,
                error=error,
            )
            results.append((assessment, preview.head_df if preview else None, preview.tail_df if preview else None))
            print(f"status   : {status}")
            print(f"category : {category} ({category_reason})")
            print(f"pk       : {has_pk} | {pk_col} | {pk_kind}")
            print(f"years    : {present_years} missing {missing_years}")
            if error:
                print(f"error    : {error}")
            if pause_seconds > 0:
                time.sleep(pause_seconds)
    finally:
        try:
            datastat_client.session.close()  # type: ignore[attr-defined]
        except Exception:
            pass
        try:
            lkod_bridge.close()
        except Exception:
            pass
        if cleanup_downloaded_files:
            clear_directory_contents(downloads_dir)

    manifest_rows = []
    for assessment, _, _ in results:
        manifest_rows.append(asdict(assessment))
    manifest_df = pd.DataFrame(manifest_rows)
    if manifest_df.empty:
        return manifest_df, results

    # Final ordering A -> D, then relevance, then primary key exactness, then title.
    pk_sort_map = {"exact": 0, "exact-ish": 1, "equivalent": 2, "territorial_non_municipal": 8, None: 9}
    manifest_df["_category_rank"] = manifest_df["category"].map(CATEGORY_ORDER).fillna(99).astype(int)
    manifest_df["_pk_sort"] = manifest_df["primary_key_kind"].map(pk_sort_map).fillna(9).astype(int)
    manifest_df["_has_pk_sort"] = manifest_df["has_primary_key"].fillna(False).astype(int) * -1
    manifest_df["_has_years_sort"] = manifest_df["has_target_years"].fillna(False).astype(int) * -1
    manifest_df["_years_max_sort"] = pd.to_numeric(manifest_df["years_max"], errors="coerce").fillna(-1)
    manifest_df = manifest_df.sort_values(
        ["_category_rank", "relevance_rank", "_pk_sort", "_has_years_sort", "_has_pk_sort", "_years_max_sort", "dataset_title", "dataset_id"],
        ascending=[True, True, True, True, True, False, True, True],
        na_position="last",
    ).reset_index(drop=True)
    manifest_df["order"] = range(1, len(manifest_df) + 1)
    manifest_df = manifest_df.drop(columns=["_category_rank", "_pk_sort", "_has_pk_sort", "_has_years_sort", "_years_max_sort"])

    # Push order back to results and sort them consistently.
    order_map = {tuple((row["dataset_id"], row["dataset_title"], row["category"], row["status"])): int(row["order"]) for _, row in manifest_df.iterrows()}
    reindexed_results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]] = []
    for assessment, head_df, tail_df in results:
        key = (assessment.dataset_id, assessment.dataset_title, assessment.category, assessment.status)
        assessment.order = order_map.get(key, assessment.order)
        reindexed_results.append((assessment, head_df, tail_df))
    reindexed_results.sort(key=lambda item: item[0].order)

    # Save outputs.
    manifest_path = out_dir / "ikz_a_to_z_manifest.csv"
    manifest_df.to_csv(manifest_path, index=False, encoding="utf-8-sig")
    try:
        with pd.ExcelWriter(out_dir / "ikz_a_to_z_manifest.xlsx", engine="openpyxl") as writer:
            manifest_df.to_excel(writer, sheet_name="manifest", index=False)
            for name, tbl in build_summary_tables(manifest_df).items():
                sheet = sanitize_filename(name, max_len=31)[:31] or name[:31]
                tbl.to_excel(writer, sheet_name=sheet, index=False)
    except Exception:
        pass

    summaries = build_summary_tables(manifest_df)
    for name, tbl in summaries.items():
        tbl.to_csv(out_dir / f"{name}.csv", index=False, encoding="utf-8-sig")
    relevant_sorted = relevant.merge(manifest_df[["dataset_id", "dataset_title", "category", "order"]], on=["dataset_id", "dataset_title"], how="left")
    relevant_sorted.sort_values("order", inplace=True, na_position="last")
    relevant_sorted.to_csv(out_dir / "selected_relevant_catalogue.csv", index=False, encoding="utf-8-sig")
    write_markdown_report(out_dir, manifest_df, reindexed_results)

    if display_in_notebook:
        for assessment, head_df, tail_df in reindexed_results:
            display_assessment_in_notebook(assessment, head_df, tail_df)

    return manifest_df, reindexed_results


# ---------------------------------------------------------------------------
# Notebook-friendly helper
# ---------------------------------------------------------------------------


def display_category_results(
    results: list[tuple[DatasetAssessment, pd.DataFrame | None, pd.DataFrame | None]],
    *,
    categories: Sequence[str] | None = None,
    max_items: int | None = None,
) -> None:
    wanted = {c.upper() for c in categories} if categories else None
    shown = 0
    for assessment, head_df, tail_df in results:
        if wanted and assessment.category not in wanted:
            continue
        display_assessment_in_notebook(assessment, head_df, tail_df)
        shown += 1
        if max_items is not None and shown >= max_items:
            break


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CZSO IKZ A-to-Z workflow: relevant dataset selection, A/B/C/D classification, head/tail previews.")
    parser.add_argument("--catalog-xlsx", required=True, help="Path to czso_katalog_trideny.xlsx")
    parser.add_argument("--output-dir", required=True, help="Directory for manifest, previews, and temporary downloads")
    parser.add_argument("--target-years", nargs="+", type=int, default=TARGET_YEARS_DEFAULT, help="Target years for category A/B logic. Default: 2023 2024")
    parser.set_defaults(require_all_target_years=True)
    parser.add_argument("--require-all-target-years", dest="require_all_target_years", action="store_true", help="Require all target years to be present (default).")
    parser.add_argument("--allow-any-target-year", dest="require_all_target_years", action="store_false", help="Relax classification: any overlap with target years is enough.")
    parser.add_argument("--head-rows", type=int, default=5, help="Number of rows for head() preview")
    parser.add_argument("--tail-rows", type=int, default=5, help="Number of rows for tail() preview")
    parser.add_argument("--max-datasets", type=int, default=None, help="Optional limit for quick testing")
    parser.add_argument("--force-redownload", action="store_true", help="Re-download datasets even if cached files exist")
    parser.add_argument("--keep-downloads", action="store_true", help="Keep downloaded source files in _downloads after previews are created")
    parser.add_argument("--pause-seconds", type=float, default=0.0, help="Optional sleep between datasets")
    parser.add_argument("--print-previews", action="store_true", help="Print head/tail previews to console after processing")
    return parser



def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    manifest_df, results = process_relevant_catalogue(
        Path(args.catalog_xlsx),
        output_dir=Path(args.output_dir),
        target_years=args.target_years,
        require_all_target_years=bool(args.require_all_target_years),
        head_rows=int(args.head_rows),
        tail_rows=int(args.tail_rows),
        max_datasets=args.max_datasets,
        force_redownload=bool(args.force_redownload),
        cleanup_downloaded_files=not bool(args.keep_downloads),
        pause_seconds=float(args.pause_seconds),
        display_in_notebook=False,
    )

    print("\nHotovo.")
    print(f"- manifest  : {Path(args.output_dir) / 'ikz_a_to_z_manifest.csv'}")
    print(f"- previews  : {Path(args.output_dir) / 'previews'}")
    print(f"- report    : {Path(args.output_dir) / 'ikz_a_to_z_previews.md'}")
    print(f"- downloads : {Path(args.output_dir) / '_downloads'}")
    if not args.keep_downloads:
        print("  (stažené zdrojové soubory se po vytvoření preview průběžně mažou)")
    print("\nPočty podle kategorií:")
    if manifest_df.empty:
        print("<prázdné>")
    else:
        print(manifest_df.groupby("category").size().to_string())

    if args.print_previews:
        for assessment, head_df, tail_df in results:
            print("=" * 100)
            print(f"{assessment.order:03d}. [{assessment.category}] {assessment.dataset_title or assessment.dataset_id}")
            print(assessment_display_series(assessment).to_string())
            print("\nHEAD:\n")
            print(dataframe_to_pretty_string(head_df))
            print("\nTAIL:\n")
            print(dataframe_to_pretty_string(tail_df))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
