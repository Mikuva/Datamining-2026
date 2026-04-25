from __future__ import annotations

"""CZSO IKZ robust patch v10.

Hardened against three systematic false-negative risks:
1. inconsistent time-column names like ``obdobi_kod``;
2. large CSV files where time values are not visible in the first rows only;
3. fragile CSV encoding detection (UTF-8 vs. CP1250 / Windows-1250).

The high-level workflow (historical exclusions, municipality-first ordering,
family grouping, preview cleanup) is delegated to the latest patch layer. This
module only replaces time detection and preview loading.
"""

import argparse
import contextlib
import math
import re
import sys
from pathlib import Path
from typing import Any, Iterator, Sequence

import pandas as pd

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

import czso_ikz_v8_clean_patch as prev  # noqa: E402
import czso_ikz_v7_patch as v7  # noqa: E402
import czso_ikz_a_to_z_v5 as pipeline  # noqa: E402
import czso_ikz_territory_patch as territory  # noqa: E402
import _czso_ikz_a_to_z_v4_base as base  # noqa: E402
import pyczso  # noqa: E402
from pyczso_lkod_bridge import LKODBridge, detect_encoding  # noqa: E402

TablePreview = pipeline.TablePreview
DatasetAssessment = pipeline.DatasetAssessment
TARGET_YEARS_DEFAULT = list(pipeline.TARGET_YEARS_DEFAULT)
PROBE_ROWS_DEFAULT = pipeline.PROBE_ROWS_DEFAULT
read_catalogue = pipeline.read_catalogue
select_relevant_datasets = prev.select_relevant_datasets
build_summary_tables = prev.build_summary_tables
assessment_display_series = prev.assessment_display_series
format_years_sample = pipeline.format_years_sample
sanitize_filename = prev.sanitize_filename
Markdown = prev.Markdown
_display = prev._display
display_results_by_territory = territory.display_results_by_territory
quick_resort_existing_output = territory.quick_resort_existing_output

_CURRENT_TARGET_YEARS_FOR_PREVIEW: list[int] | None = None
_FILTER_PREVIEW_TO_TARGET_YEARS: bool = True

YEAR_MIN = 1800
YEAR_MAX = 2100
TARGET_DETECTION_YEAR_MIN = 1990
TARGET_DETECTION_YEAR_MAX = 2035

TIME_EXACT_PRIORITY = {
    "rok": 100,
    "year": 100,
    "sldbrok": 98,
    "datum": 96,
    "date": 96,
    "sldbdatum": 95,
    "casref": 94,
    "casrefod": 93,
    "casrefdo": 93,
    "obdobi": 92,
    "period": 92,
    "mesic": 88,
    "month": 88,
    "ctvrtleti": 86,
    "quarter": 86,
    "tyden": 84,
    "week": 84,
}
TIME_TOKEN_PRIORITY = {
    "rok": 100,
    "year": 100,
    "datum": 96,
    "date": 96,
    "casref": 94,
    "obdobi": 92,
    "period": 92,
    "mesic": 88,
    "month": 88,
    "ctvrtleti": 86,
    "quarter": 86,
    "tyden": 84,
    "week": 84,
    "sldb": 70,
}
NON_TIME_EXACT_NAMES = {
    "hodnota",
    "value",
    "idhod",
    "id",
    "vuk",
    "vukid",
    "vukkod",
    "staprokod",
    "ukazkod",
    "ukaztxt",
}
NON_TIME_TOKENS = {
    "hodnota",
    "value",
    "count",
    "pocet",
    "idhod",
    "vuk",
    "ukaz",
    "txt",
    "text",
    "label",
    "nazev",
    "popis",
    "description",
}
NON_TIME_SUFFIXES = ("kod", "cis", "id", "txt", "text")
MOJIBAKE_PATTERNS = ("�", "Ã", "Â", "Ä", "Å", "Ð", "Ñ", "Ĺ", "¤", "Ï", "Ď", "ќ")

YEAR_WORD_RE = re.compile(r"(?<!\d)(18\d{2}|19\d{2}|20\d{2}|2100)(?!\d)")
YEAR_COMPACT_MONTH_RE = re.compile(r"^(18|19|20)\d{2}(0[1-9]|1[0-2])$")
YEAR_COMPACT_DATE_RE = re.compile(r"^(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])$")


def _normalize(value: Any) -> str:
    return base.normalize_name(value)


def _tokens(value: Any) -> list[str]:
    return base._split_name_tokens(value)


def _time_name_priority(column_name: Any) -> int:
    norm = _normalize(column_name)
    if norm in TIME_EXACT_PRIORITY:
        return TIME_EXACT_PRIORITY[norm]
    toks = set(_tokens(column_name))
    if {"sldb", "rok"}.issubset(toks):
        return 98
    if {"sldb", "datum"}.issubset(toks):
        return 95
    if "casref" in toks or norm.startswith("casref"):
        return 94
    for token, priority in TIME_TOKEN_PRIORITY.items():
        if token in toks:
            return priority
    if norm.startswith("obdobi"):
        return 92
    if norm.startswith("rok"):
        return 100
    if norm.startswith("datum"):
        return 96
    return 0


def is_time_like_column_name(column_name: Any) -> bool:
    return _time_name_priority(column_name) > 0


def _is_obvious_non_time_column(column_name: Any) -> bool:
    if _time_name_priority(column_name) > 0:
        return False
    norm = _normalize(column_name)
    toks = set(_tokens(column_name))
    if norm in NON_TIME_EXACT_NAMES:
        return True
    if toks & NON_TIME_TOKENS:
        return True
    if norm.endswith(NON_TIME_SUFFIXES):
        return True
    if toks & {"kod", "cis", "id"}:
        return True
    return False


def _extract_years_for_detection(value: Any) -> list[int]:
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
            if YEAR_MIN <= year <= YEAR_MAX:
                return [year]
        except Exception:
            pass
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        try:
            if math.isfinite(float(value)) and float(value).is_integer():
                ivalue = int(float(value))
                digits = str(abs(ivalue))
                if len(digits) == 4 and digits.startswith(("18", "19", "20")):
                    year = int(digits)
                    if YEAR_MIN <= year <= YEAR_MAX:
                        years.add(year)
                elif len(digits) in {6, 8} and digits[:4].startswith(("18", "19", "20")):
                    year = int(digits[:4])
                    if YEAR_MIN <= year <= YEAR_MAX:
                        years.add(year)
        except Exception:
            pass
        return sorted(years)
    text = str(value).strip()
    if not text:
        return []
    for match in YEAR_WORD_RE.findall(text):
        year = int(match)
        if YEAR_MIN <= year <= YEAR_MAX:
            years.add(year)
    compact = re.sub(r"\s+", "", text)
    if YEAR_COMPACT_MONTH_RE.fullmatch(compact):
        years.add(int(compact[:4]))
    if YEAR_COMPACT_DATE_RE.fullmatch(compact):
        years.add(int(compact[:4]))
    return sorted(years)


def parse_year_series(series: pd.Series, *, limit: int | None = None) -> pd.Series:
    if series is None:
        return pd.Series(dtype=object)
    values = series
    if limit is not None:
        values = values.head(limit)
    return values.map(_extract_years_for_detection)


def _analyse_year_signal(series: pd.Series, *, sample_limit: int | None = None) -> dict[str, Any]:
    sample = series.dropna()
    if sample_limit is not None and len(sample) > sample_limit:
        sample = sample.head(sample_limit)
    if sample.empty:
        return {
            "sample_size": 0,
            "hit_count": 0,
            "hit_ratio": 0.0,
            "unique_years": [],
            "unique_year_count": 0,
            "value_unique_count": 0,
            "numeric_non_year_count": 0,
        }
    extracted = parse_year_series(sample)
    hit_count = int(extracted.map(bool).sum())
    unique_years = sorted({year for years in extracted.tolist() for year in years if TARGET_DETECTION_YEAR_MIN <= year <= TARGET_DETECTION_YEAR_MAX})
    value_unique_count = int(sample.astype(str).nunique(dropna=True))
    numeric_non_year_count = 0
    for value, years in zip(sample.tolist(), extracted.tolist()):
        if years:
            continue
        try:
            num = float(value)
            if math.isfinite(num):
                numeric_non_year_count += 1
                continue
        except Exception:
            pass
        txt = str(value).strip()
        if txt.isdigit():
            numeric_non_year_count += 1
    return {
        "sample_size": int(len(sample)),
        "hit_count": hit_count,
        "hit_ratio": hit_count / max(len(sample), 1),
        "unique_years": unique_years,
        "unique_year_count": len(unique_years),
        "value_unique_count": value_unique_count,
        "numeric_non_year_count": numeric_non_year_count,
    }


def _time_candidates_from_probe(df: pd.DataFrame) -> list[tuple[float, str, dict[str, Any]]]:
    if df is None or df.empty:
        return []
    candidates: list[tuple[float, str, dict[str, Any]]] = []
    sample_size_hint = max(len(df), 1)
    for col in df.columns:
        priority = _time_name_priority(col)
        if priority == 0 and _is_obvious_non_time_column(col):
            continue
        info = _analyse_year_signal(df[col])
        if info["hit_count"] <= 0:
            continue
        unique_year_count = int(info["unique_year_count"])
        hit_ratio = float(info["hit_ratio"])
        value_unique_count = int(info["value_unique_count"])
        numeric_non_year_count = int(info["numeric_non_year_count"])
        sample_size = int(info["sample_size"] or sample_size_hint)
        if priority > 0:
            if 1 <= unique_year_count <= 250:
                penalty = 15.0 if numeric_non_year_count > hit_ratio * sample_size else 0.0
                score = 1000.0 + float(priority) + (hit_ratio * 100.0) - (unique_year_count * 0.08) - penalty
                candidates.append((score, str(col), info))
            continue
        if unique_year_count > 30:
            continue
        if hit_ratio < 0.90:
            continue
        if value_unique_count > max(50, int(sample_size * 0.50)):
            continue
        if numeric_non_year_count > max(0, int(sample_size * 0.05)):
            continue
        score = (hit_ratio * 100.0) - (unique_year_count * 0.20)
        candidates.append((score, str(col), info))
    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates


def detect_time_columns_from_probe(df: pd.DataFrame) -> list[str]:
    return [col for _, col, _ in _time_candidates_from_probe(df)]


def detect_year_column(df: pd.DataFrame) -> tuple[str | None, list[int], list[str]]:
    candidates = _time_candidates_from_probe(df)
    if not candidates:
        return None, [], []
    _, best_col, best_info = candidates[0]
    time_columns = [col for _, col, _ in candidates]
    return best_col, list(best_info.get("unique_years") or []), time_columns


def mask_series_for_target_years(series: pd.Series, target_years: Sequence[int]) -> pd.Series:
    target = {int(y) for y in target_years}
    if not target:
        return pd.Series([True] * len(series), index=series.index)
    if pd.api.types.is_datetime64_any_dtype(series):
        parsed = pd.to_datetime(series, errors="coerce")
        return parsed.dt.year.isin(target).fillna(False)
    return series.map(lambda value: bool(target.intersection(_extract_years_for_detection(value))))


def filter_dataframe_to_target_years(df: pd.DataFrame, year_column: str, target_years: Sequence[int]) -> tuple[pd.DataFrame, int]:
    if year_column not in df.columns:
        return df.head(0).copy(), 0
    mask = mask_series_for_target_years(df[year_column], target_years)
    filtered = df.loc[mask].copy()
    return filtered, int(mask.sum())


def _years_from_dataframe(df: pd.DataFrame, time_columns: Sequence[str], column_names: Sequence[str]) -> tuple[list[int], str | None]:
    header_years = base.years_from_strings(column_names)
    years: set[int] = set(header_years)
    years_source: str | None = "header_columns" if header_years else None
    if time_columns:
        extracted: set[int] = set(years)
        for col in time_columns:
            if col in df.columns:
                extracted.update(base.series_years(df[col]))
        years = sorted(extracted)
        if extracted:
            years_source = "data_columns"
    return sorted(dict.fromkeys(years)), years_source


def read_bytes_sample(path: Path, size: int = 2_000_000) -> bytes:
    with path.open("rb") as f:
        return f.read(size)


def _mojibake_penalty(text: str) -> int:
    return sum(text.count(token) for token in MOJIBAKE_PATTERNS)


def _score_csv_probe(df: pd.DataFrame, encoding: str) -> float:
    text_parts = [" ".join(str(c) for c in df.columns)]
    try:
        sample_obj = df.select_dtypes(include=["object"]).head(25)
        if not sample_obj.empty:
            text_parts.extend(sample_obj.astype(str).stack().tolist()[:200])
    except Exception:
        pass
    text = " ".join(text_parts)
    bad = _mojibake_penalty(text)
    unnamed = sum(1 for c in df.columns if str(c).startswith("Unnamed:"))
    preferred_bonus = 5 if encoding in {"utf-8-sig", "utf-8", "cp1250", "windows-1250"} else 0
    return float((len(df.columns) * 10) - (bad * 20) - (unnamed * 5) + preferred_bonus)


def select_csv_encoding(path: Path, *, probe_rows: int = 250) -> str:
    raw = read_bytes_sample(path)
    encodings: list[str] = []
    for enc in detect_encoding(raw):
        if enc not in encodings:
            encodings.append(enc)
    for enc in ["utf-8-sig", "utf-8", "cp1250", "windows-1250", "cp1252", "latin-1"]:
        if enc not in encodings:
            encodings.append(enc)
    best_encoding: str | None = None
    best_score: float | None = None
    last_exc: Exception | None = None
    for enc in encodings:
        try:
            probe_df = pd.read_csv(path, encoding=enc, sep=None, engine="python", nrows=probe_rows)
            score = _score_csv_probe(probe_df, enc)
            if best_score is None or score > best_score:
                best_score = score
                best_encoding = enc
        except Exception as exc:
            last_exc = exc
            continue
    if best_encoding is None:
        raise RuntimeError(f"CSV reading failed for {path.name}: {last_exc}")
    return best_encoding


def _take_evenly_spaced(values: pd.Series, count: int) -> list[Any]:
    if count <= 0 or values.empty:
        return []
    if len(values) <= count:
        return values.tolist()
    step = max(len(values) / float(count), 1.0)
    idxs = []
    pos = 0.0
    while len(idxs) < count and int(pos) < len(values):
        idxs.append(int(pos))
        pos += step
    idxs = sorted(set(min(i, len(values) - 1) for i in idxs))[:count]
    return values.iloc[idxs].tolist()


def build_probe_from_dataframe(df: pd.DataFrame, *, rows_per_slice: int = 120, slices: int = 5) -> pd.DataFrame:
    if df is None or df.empty:
        return df.head(0).copy()
    if len(df) <= rows_per_slice * slices:
        return df.copy()
    n = len(df)
    starts = [0]
    if slices > 2:
        for frac in [i / (slices - 1) for i in range(1, slices - 1)]:
            start = int(max(0, min(n - rows_per_slice, round(frac * max(n - rows_per_slice, 0)))))
            starts.append(start)
    starts.append(max(0, n - rows_per_slice))
    starts = sorted(set(starts))
    parts = [df.iloc[s:s + rows_per_slice] for s in starts]
    return pd.concat(parts, ignore_index=True).reset_index(drop=True)


def sample_csv_for_time_detection(path: Path, *, encoding: str, chunksize: int = 50000, rows_per_chunk: int = 30, max_samples_per_column: int = 2000) -> tuple[pd.DataFrame, list[str], int]:
    samples: dict[str, list[Any]] = {}
    column_names: list[str] = []
    total_rows = 0
    for chunk in pd.read_csv(path, encoding=encoding, sep=None, engine="python", chunksize=chunksize):
        total_rows += len(chunk)
        if not column_names:
            column_names = [str(c) for c in chunk.columns]
            samples = {str(c): [] for c in chunk.columns}
        for col in chunk.columns:
            col_name = str(col)
            current = samples.setdefault(col_name, [])
            remaining = max_samples_per_column - len(current)
            if remaining <= 0:
                continue
            non_null = chunk[col].dropna()
            if non_null.empty:
                continue
            take_n = min(rows_per_chunk, remaining)
            current.extend(_take_evenly_spaced(non_null, take_n))
    probe_df = pd.DataFrame({col: pd.Series(values, dtype=object) for col, values in samples.items()}) if samples else pd.DataFrame()
    return probe_df, column_names, int(total_rows)


def load_csv_preview(path: Path, *, head_rows: int, tail_rows: int, chunksize: int = 50000, probe_rows: int = PROBE_ROWS_DEFAULT, target_years: Sequence[int] | None = None, filter_preview_to_target_years: bool = False) -> TablePreview:
    encoding = select_csv_encoding(path)
    probe_df, column_names, total_rows_probe = sample_csv_for_time_detection(
        path,
        encoding=encoding,
        chunksize=chunksize,
        rows_per_chunk=max(10, min(60, probe_rows // 4 or 10)),
        max_samples_per_column=max(800, probe_rows * 8),
    )
    if not column_names:
        return TablePreview(pd.DataFrame(), pd.DataFrame(), 0, 0, [], [], [], None, path.name, None, "csv", f"encoding={encoding}; prázdný soubor")
    best_time_col, _candidate_years, time_columns = detect_year_column(probe_df)
    header_years = base.years_from_strings(column_names)
    years: set[int] = set(header_years)
    years_source: str | None = "header_columns" if header_years else None
    total_rows = 0
    matched_rows = 0
    full_head_df: pd.DataFrame | None = None
    full_tail_df: pd.DataFrame | None = None
    filtered_head_df: pd.DataFrame | None = None
    filtered_tail_df: pd.DataFrame | None = None
    for chunk in pd.read_csv(path, encoding=encoding, sep=None, engine="python", chunksize=chunksize):
        total_rows += len(chunk)
        if full_head_df is None:
            full_head_df = chunk.head(head_rows).copy()
        elif len(full_head_df) < head_rows:
            full_head_df = pd.concat([full_head_df, chunk], ignore_index=True).head(head_rows).copy()
        full_tail_df = chunk.tail(tail_rows).copy() if full_tail_df is None else pd.concat([full_tail_df, chunk], ignore_index=True).tail(tail_rows).copy()
        for col in time_columns:
            if col in chunk.columns:
                years.update(base.series_years(chunk[col]))
        if filter_preview_to_target_years and target_years and best_time_col and best_time_col in chunk.columns:
            filtered_chunk, matched = filter_dataframe_to_target_years(chunk, best_time_col, target_years)
            matched_rows += matched
            if filtered_head_df is None:
                filtered_head_df = filtered_chunk.head(head_rows).copy()
            elif len(filtered_head_df) < head_rows and not filtered_chunk.empty:
                filtered_head_df = pd.concat([filtered_head_df, filtered_chunk], ignore_index=True).head(head_rows).copy()
            filtered_tail_df = filtered_chunk.tail(tail_rows).copy() if filtered_tail_df is None else pd.concat([filtered_tail_df, filtered_chunk], ignore_index=True).tail(tail_rows).copy()
        else:
            filtered_tail_df = chunk.tail(tail_rows).copy() if filtered_tail_df is None else pd.concat([filtered_tail_df, chunk], ignore_index=True).tail(tail_rows).copy()
    if total_rows == 0:
        total_rows = total_rows_probe
    years_sorted = sorted(years)
    if years_sorted and time_columns:
        years_source = "data_columns"
    notes = [f"encoding={encoding}", "časové sloupce detekovány z průběžného vzorku přes celý CSV soubor, ne jen z prvních řádků"]
    if v7._should_use_full_preview_for_single_snapshot(years_sorted):
        head_df = full_head_df.copy() if full_head_df is not None else pd.DataFrame(columns=column_names)
        tail_df = full_tail_df.copy() if full_tail_df is not None else pd.DataFrame(columns=column_names)
        notes.append(f"dataset obsahuje jediný rok {years_sorted[0]} v intervalu {v7.SNAPSHOT_FULL_PREVIEW_MIN_YEAR}-{v7.SNAPSHOT_FULL_PREVIEW_MAX_YEAR}; head/tail jsou z celého datasetu")
    elif filter_preview_to_target_years and target_years:
        if best_time_col:
            notes.append(f"head/tail filtrovány na target years {list(target_years)} přes sloupec `{best_time_col}`; matching_rows={matched_rows}")
            head_df = filtered_head_df if filtered_head_df is not None else pd.DataFrame(columns=column_names)
            tail_df = filtered_tail_df if filtered_tail_df is not None else pd.DataFrame(columns=column_names)
        else:
            notes.append("head/tail zůstaly nefiltrované: nebyl nalezen spolehlivý řádkový časový sloupec")
            head_df = full_head_df.copy() if full_head_df is not None else pd.DataFrame(columns=column_names)
            tail_df = full_tail_df.copy() if full_tail_df is not None else pd.DataFrame(columns=column_names)
    else:
        head_df = full_head_df.copy() if full_head_df is not None else pd.DataFrame(columns=column_names)
        tail_df = full_tail_df.copy() if full_tail_df is not None else pd.DataFrame(columns=column_names)
    return TablePreview(head_df, tail_df, int(total_rows), int(len(column_names)), column_names, time_columns, years_sorted, years_source, path.name, None, "csv", " | ".join(notes))


def load_excel_preview(path: Path, *, head_rows: int, tail_rows: int, probe_rows: int = PROBE_ROWS_DEFAULT, target_years: Sequence[int] | None = None, filter_preview_to_target_years: bool = False) -> TablePreview:
    full = pd.read_excel(path)
    probe_df = build_probe_from_dataframe(full, rows_per_slice=max(head_rows, min(150, probe_rows)), slices=5)
    column_names = [str(c) for c in full.columns]
    best_time_col, _candidate_years, time_columns = detect_year_column(probe_df)
    years, years_source = _years_from_dataframe(full, time_columns, column_names)
    notes = ["roky načteny z celého sešitu", "časové sloupce detekovány z více řezů sešitem"]
    if v7._should_use_full_preview_for_single_snapshot(years):
        preview_df = full
        notes.append(f"dataset obsahuje jediný rok {years[0]} v intervalu {v7.SNAPSHOT_FULL_PREVIEW_MIN_YEAR}-{v7.SNAPSHOT_FULL_PREVIEW_MAX_YEAR}; head/tail jsou z celého datasetu")
    elif filter_preview_to_target_years and target_years:
        if best_time_col and best_time_col in full.columns:
            preview_df, matched_rows = filter_dataframe_to_target_years(full, best_time_col, target_years)
            notes.append(f"head/tail filtrovány na target years {list(target_years)} přes sloupec `{best_time_col}`; matching_rows={matched_rows}")
        else:
            preview_df = full
            notes.append("head/tail zůstaly nefiltrované: nebyl nalezen spolehlivý řádkový časový sloupec")
    else:
        preview_df = full
    return TablePreview(preview_df.head(head_rows).copy(), preview_df.tail(tail_rows).copy(), int(len(full)), int(len(full.columns)), column_names, time_columns, years, years_source, path.name, None, path.suffix.lower().lstrip('.'), " | ".join(notes))


def load_dataframe_preview(df: pd.DataFrame, *, head_rows: int, tail_rows: int, selected_file: str | None = None, probe_rows: int = PROBE_ROWS_DEFAULT, target_years: Sequence[int] | None = None, filter_preview_to_target_years: bool = False) -> TablePreview:
    probe_df = build_probe_from_dataframe(df, rows_per_slice=max(head_rows, min(150, probe_rows)), slices=5)
    column_names = [str(c) for c in df.columns]
    best_time_col, _candidate_years, time_columns = detect_year_column(probe_df)
    years, years_source = _years_from_dataframe(df, time_columns, column_names)
    notes = ["roky načteny z celého DataFrame", "časové sloupce detekovány z více řezů DataFrame"]
    if v7._should_use_full_preview_for_single_snapshot(years):
        preview_df = df
        notes.append(f"dataset obsahuje jediný rok {years[0]} v intervalu {v7.SNAPSHOT_FULL_PREVIEW_MIN_YEAR}-{v7.SNAPSHOT_FULL_PREVIEW_MAX_YEAR}; head/tail jsou z celého datasetu")
    elif filter_preview_to_target_years and target_years:
        if best_time_col and best_time_col in df.columns:
            preview_df, matched_rows = filter_dataframe_to_target_years(df, best_time_col, target_years)
            notes.append(f"head/tail filtrovány na target years {list(target_years)} přes sloupec `{best_time_col}`; matching_rows={matched_rows}")
        else:
            preview_df = df
            notes.append("head/tail zůstaly nefiltrované: nebyl nalezen spolehlivý řádkový časový sloupec")
    else:
        preview_df = df
    return TablePreview(preview_df.head(head_rows).copy(), preview_df.tail(tail_rows).copy(), int(len(df)), int(len(df.columns)), column_names, time_columns, years, years_source, selected_file, None, "datastat_csv", " | ".join(notes))


def load_zip_preview(path: Path, *, head_rows: int, tail_rows: int, target_years: Sequence[int] | None = None, filter_preview_to_target_years: bool = False) -> TablePreview:
    temp_prefix = f"extract_{base.sanitize_filename(path.stem, max_len=40)}_"
    with base.tempfile.TemporaryDirectory(dir=path.parent, prefix=temp_prefix) as tmpdir:
        extract_dir = Path(tmpdir)
        with base.zipfile.ZipFile(path, "r") as zf:
            zf.extractall(extract_dir)
        candidates = [p for p in extract_dir.rglob("*") if p.is_file() and p.suffix.lower() in {".csv", ".xlsx", ".xls", ".xlsm"}]
        if not candidates:
            return TablePreview(None, None, None, None, [], [], [], None, None, None, "zip", "Archiv neobsahuje CSV/XLSX soubor, který by šel automaticky profilovat.")
        def _candidate_key(p: Path) -> tuple[int, int, str]:
            ext_rank = 0 if p.suffix.lower() == ".csv" else 1
            return (ext_rank, len(str(p.relative_to(extract_dir))), str(p.relative_to(extract_dir)).lower())
        selected = sorted(candidates, key=_candidate_key)[0]
        if selected.suffix.lower() == ".csv":
            preview = load_csv_preview(selected, head_rows=head_rows, tail_rows=tail_rows, target_years=target_years, filter_preview_to_target_years=filter_preview_to_target_years)
        else:
            preview = load_excel_preview(selected, head_rows=head_rows, tail_rows=tail_rows, target_years=target_years, filter_preview_to_target_years=filter_preview_to_target_years)
        preview.selected_file = str(selected.relative_to(extract_dir))
        preview.selected_format = f"zip->{selected.suffix.lower().lstrip('.')}"
        preview.notes = f"Archiv obsahuje {len(candidates)} čitelných souborů; profilován byl `{preview.selected_file}` | {preview.notes}"
        return preview


def fetch_dataset_preview(datastat_client: pyczso.CZSOClient, lkod_bridge: LKODBridge, dataset_id: str, *, head_rows: int, tail_rows: int, download_dir: Path, force_redownload: bool, cleanup_downloaded_files: bool = True) -> tuple[TablePreview | None, str | None, str | None, str | None, str, str | None]:
    lkod_error: str | None = None
    local_path: Path | None = None
    try:
        try:
            pointer = lkod_bridge.download_resource(dataset_id, dest_dir=download_dir, force_redownload=force_redownload)
            local_path = Path(pointer["download_path"])
            ext = str(pointer.get("extension") or local_path.suffix.lstrip(".")).lower()
            source_title = pipeline.clean_string(pointer.get("title")) or pipeline.clean_string(pointer.get("format"))
            if ext == "csv":
                preview = load_csv_preview(local_path, head_rows=head_rows, tail_rows=tail_rows, target_years=_CURRENT_TARGET_YEARS_FOR_PREVIEW, filter_preview_to_target_years=_FILTER_PREVIEW_TO_TARGET_YEARS)
            elif ext in {"xlsx", "xls", "xlsm"}:
                preview = load_excel_preview(local_path, head_rows=head_rows, tail_rows=tail_rows, target_years=_CURRENT_TARGET_YEARS_FOR_PREVIEW, filter_preview_to_target_years=_FILTER_PREVIEW_TO_TARGET_YEARS)
            elif ext == "zip":
                preview = load_zip_preview(local_path, head_rows=head_rows, tail_rows=tail_rows, target_years=_CURRENT_TARGET_YEARS_FOR_PREVIEW, filter_preview_to_target_years=_FILTER_PREVIEW_TO_TARGET_YEARS)
            else:
                return None, "LKOD", f"resource#{pointer.get('resource_num')}", source_title, "UNSUPPORTED_FORMAT", f"Stažený formát `{ext}` není podporovaný pro preview head/tail."
            return preview, "LKOD", f"resource#{pointer.get('resource_num')}", source_title, "OK_LKOD", preview.notes
        except Exception as exc:
            lkod_error = str(exc)
    finally:
        if cleanup_downloaded_files:
            base.remove_path_quietly(local_path)
    try:
        selections = datastat_client.get_dataset_selections(dataset_id, as_frame=True)
    except Exception as exc:
        msg = f"LKOD/VDB selhalo: {lkod_error} | DataStat metadata selhala: {exc}" if lkod_error else f"DataStat metadata selhala: {exc}"
        return None, None, None, None, "ERROR_SELECTIONS", msg
    selection_code, selection_title, selection_count = base.choose_selection(selections)
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
    preview = load_dataframe_preview(df, head_rows=head_rows, tail_rows=tail_rows, selected_file=f"selection_{selection_code}.csv", target_years=_CURRENT_TARGET_YEARS_FOR_PREVIEW, filter_preview_to_target_years=_FILTER_PREVIEW_TO_TARGET_YEARS)
    return preview, "DATASTAT", selection_code, selection_title, "OK_DATASTAT", lkod_error


@contextlib.contextmanager
def _runtime_overrides() -> Iterator[None]:
    originals = {
        "pipeline_detect_year_column": pipeline.detect_year_column,
        "pipeline_detect_time_columns_from_probe": getattr(pipeline, "detect_time_columns_from_probe", None),
        "pipeline_is_time_like_column_name": getattr(pipeline, "is_time_like_column_name", None),
        "base_fetch_dataset_preview": base.fetch_dataset_preview,
        "base_detect_time_columns_from_probe": getattr(base, "detect_time_columns_from_probe", None),
        "base_is_time_like_column_name": getattr(base, "is_time_like_column_name", None),
        "v7_fetch_dataset_preview": v7.fetch_dataset_preview,
    }
    pipeline.detect_year_column = detect_year_column  # type: ignore[assignment]
    pipeline.detect_time_columns_from_probe = detect_time_columns_from_probe  # type: ignore[assignment]
    pipeline.is_time_like_column_name = is_time_like_column_name  # type: ignore[assignment]
    base.fetch_dataset_preview = fetch_dataset_preview  # type: ignore[assignment]
    base.detect_time_columns_from_probe = detect_time_columns_from_probe  # type: ignore[assignment]
    base.is_time_like_column_name = is_time_like_column_name  # type: ignore[assignment]
    v7.fetch_dataset_preview = fetch_dataset_preview  # type: ignore[assignment]
    try:
        yield
    finally:
        pipeline.detect_year_column = originals["pipeline_detect_year_column"]  # type: ignore[assignment]
        if originals["pipeline_detect_time_columns_from_probe"] is not None:
            pipeline.detect_time_columns_from_probe = originals["pipeline_detect_time_columns_from_probe"]  # type: ignore[assignment]
        if originals["pipeline_is_time_like_column_name"] is not None:
            pipeline.is_time_like_column_name = originals["pipeline_is_time_like_column_name"]  # type: ignore[assignment]
        base.fetch_dataset_preview = originals["base_fetch_dataset_preview"]  # type: ignore[assignment]
        if originals["base_detect_time_columns_from_probe"] is not None:
            base.detect_time_columns_from_probe = originals["base_detect_time_columns_from_probe"]  # type: ignore[assignment]
        if originals["base_is_time_like_column_name"] is not None:
            base.is_time_like_column_name = originals["base_is_time_like_column_name"]  # type: ignore[assignment]
        v7.fetch_dataset_preview = originals["v7_fetch_dataset_preview"]  # type: ignore[assignment]


def process_relevant_catalogue(catalog_xlsx: Path, *, output_dir: Path, target_years: Sequence[int] = TARGET_YEARS_DEFAULT, require_all_target_years: bool = True, head_rows: int = 5, tail_rows: int = 5, max_datasets: int | None = None, force_redownload: bool = False, cleanup_downloaded_files: bool = True, pause_seconds: float = 0.0, display_in_notebook: bool = False, filter_preview_to_target_years: bool = True, refresh_recent_single_year: bool = True, drop_rows_without_preview: bool = True):
    global _CURRENT_TARGET_YEARS_FOR_PREVIEW, _FILTER_PREVIEW_TO_TARGET_YEARS
    old_years = _CURRENT_TARGET_YEARS_FOR_PREVIEW
    old_filter = _FILTER_PREVIEW_TO_TARGET_YEARS
    _CURRENT_TARGET_YEARS_FOR_PREVIEW = [int(y) for y in target_years]
    _FILTER_PREVIEW_TO_TARGET_YEARS = bool(filter_preview_to_target_years)
    try:
        with _runtime_overrides():
            manifest_df, results = pipeline.process_relevant_catalogue(Path(catalog_xlsx), output_dir=Path(output_dir), target_years=target_years, require_all_target_years=require_all_target_years, head_rows=head_rows, tail_rows=tail_rows, max_datasets=max_datasets, force_redownload=force_redownload, cleanup_downloaded_files=cleanup_downloaded_files, pause_seconds=pause_seconds, display_in_notebook=False, filter_preview_to_target_years=filter_preview_to_target_years)
        manifest_df, results, summary = prev.apply_output_postprocessing(manifest_df, results, output_dir=Path(output_dir), refresh_recent_single_year=refresh_recent_single_year, target_years=target_years, force_redownload=force_redownload, pause_seconds=pause_seconds, cleanup_downloaded_files=cleanup_downloaded_files, persist=True, drop_rows_without_preview=drop_rows_without_preview)
        if display_in_notebook:
            territory.display_results_by_territory(results)
        return manifest_df, results, summary
    finally:
        _CURRENT_TARGET_YEARS_FOR_PREVIEW = old_years
        _FILTER_PREVIEW_TO_TARGET_YEARS = old_filter


def repair_existing_output(output_dir: Path, *, refresh_recent_single_year: bool = True, target_years: Sequence[int] = TARGET_YEARS_DEFAULT, force_redownload: bool = False, pause_seconds: float = 0.0, cleanup_downloaded_files: bool = True, persist: bool = True):
    with _runtime_overrides():
        return prev.repair_existing_output(Path(output_dir), refresh_recent_single_year=refresh_recent_single_year, target_years=target_years, force_redownload=force_redownload, pause_seconds=pause_seconds, cleanup_downloaded_files=cleanup_downloaded_files, persist=persist)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CZSO IKZ robust patch v10")
    parser.add_argument("--catalog-xlsx", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--target-years", nargs="+", type=int, default=TARGET_YEARS_DEFAULT)
    parser.set_defaults(require_all_target_years=True)
    parser.add_argument("--require-all-target-years", dest="require_all_target_years", action="store_true")
    parser.add_argument("--allow-any-target-year", dest="require_all_target_years", action="store_false")
    parser.set_defaults(filter_preview_to_target_years=True)
    parser.add_argument("--no-filter-preview-target-years", dest="filter_preview_to_target_years", action="store_false")
    parser.add_argument("--head-rows", type=int, default=5)
    parser.add_argument("--tail-rows", type=int, default=5)
    parser.add_argument("--max-datasets", type=int, default=None)
    parser.add_argument("--force-redownload", action="store_true")
    parser.add_argument("--keep-downloads", action="store_true")
    parser.add_argument("--pause-seconds", type=float, default=0.0)
    parser.add_argument("--print-previews", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    manifest_df, results, summary = process_relevant_catalogue(
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
        filter_preview_to_target_years=bool(args.filter_preview_to_target_years),
        refresh_recent_single_year=True,
        drop_rows_without_preview=True,
    )
    print("\nHotovo.")
    print(f"- manifest  : {Path(args.output_dir) / 'ikz_a_to_z_manifest.csv'}")
    print(f"- previews  : {Path(args.output_dir) / 'previews'}")
    print(f"- report    : {Path(args.output_dir) / 'ikz_a_to_z_previews.md'}")
    print(f"- downloads : {Path(args.output_dir) / '_downloads'}")
    if not args.keep_downloads:
        print("  (stažené zdrojové soubory se po vytvoření preview průběžně mažou)")
    if args.filter_preview_to_target_years:
        print(f"  (head/tail jsou filtrované jen na target years: {list(args.target_years)})")
    print(f"  notes: {summary.get('notes')}")
    if args.print_previews:
        for assessment, head_df, tail_df in results:
            print("=" * 120)
            print(f"{assessment.order:03d}. [{assessment.category}] {assessment.dataset_title}")
            print(f"dataset_id      : {assessment.dataset_id}")
            print(f"status          : {assessment.status}")
            print(f"target_years_present : {assessment.target_years_present}")
            print(f"has_primary_key     : {assessment.has_primary_key}")
            print(f"primary_key_column  : {assessment.primary_key_column}")
            print("HEAD:")
            print(prev.dataframe_to_pretty_string(head_df))
            print("TAIL:")
            print(prev.dataframe_to_pretty_string(tail_df))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
