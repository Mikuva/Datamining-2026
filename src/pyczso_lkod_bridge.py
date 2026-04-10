from __future__ import annotations

"""Bridge helpers for CZSO LKOD/VDB open-data datasets.

This complements the existing `pyczso.py`, which targets DataStat.
The shortlist built from the R package `czso` commonly uses LKOD/VDB dataset IDs
like `110080`, `130141r25`, `sldb2021_pohlavi`, etc. Those IDs are fetched from
https://vdb.czso.cz/pll/eweb/lkod_ld.datova_sada?id=<dataset_id> and the actual
file download URL is taken from the metadata field `distribuce`.
"""

import json
from pathlib import Path
import re
import tempfile
import unicodedata
import zipfile
from typing import Any, Mapping

import pandas as pd
import requests

import pyczso

LKOD_BASE_URL = "https://vdb.czso.cz/pll/eweb"
DEFAULT_TIMEOUT = (10, 180)
DEFAULT_HEADERS = {
    "User-Agent": "pyczso-lkod-bridge/0.1.0",
    "Accept": "application/json, text/csv, application/zip, text/plain, */*",
}


class LKODBridgeError(RuntimeError):
    pass


def normalize_name(value: Any) -> str:
    text = str(value)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    return re.sub(r"[^a-z0-9]+", "", text)


def guess_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    if df is None or df.empty:
        return None

    lowered = {str(col).lower(): col for col in df.columns}
    for candidate in candidates:
        key = str(candidate).lower()
        if key in lowered:
            return lowered[key]

    normalized = {normalize_name(col): col for col in df.columns}
    for candidate in candidates:
        key = normalize_name(candidate)
        if key in normalized:
            return normalized[key]

    for col in df.columns:
        compact = normalize_name(col)
        for candidate in candidates:
            key = normalize_name(candidate)
            if key and key in compact:
                return col
    return None


def parse_json_response(response: requests.Response) -> Any:
    try:
        return response.json()
    except ValueError:
        try:
            return json.loads(response.text)
        except json.JSONDecodeError as exc:
            excerpt = response.text[:500].strip()
            raise LKODBridgeError(f"JSON parsing failed. Response excerpt: {excerpt}") from exc


def detect_encoding(raw: bytes) -> list[str]:
    encodings: list[str] = []
    try:
        from charset_normalizer import from_bytes  # type: ignore

        best = from_bytes(raw).best()
        if best and best.encoding:
            encodings.append(best.encoding)
    except Exception:
        pass

    for enc in ["utf-8-sig", "utf-8", "cp1250", "windows-1250", "latin-1"]:
        if enc not in encodings:
            encodings.append(enc)
    return encodings


def read_csv_file(path: str | Path, csv_kwargs: Mapping[str, Any] | None = None) -> pd.DataFrame:
    path = Path(path)
    raw = path.read_bytes()
    kwargs: dict[str, Any] = {"sep": None, "engine": "python"}
    if csv_kwargs:
        kwargs.update(dict(csv_kwargs))

    last_exc: Exception | None = None
    for enc in detect_encoding(raw[:200000]):
        try:
            return pd.read_csv(path, encoding=enc, **kwargs)
        except Exception as exc:
            last_exc = exc
    raise LKODBridgeError(f"CSV reading failed for {path}: {last_exc}")


def infer_extension(url: str | None, media_type: str | None) -> str:
    url = (url or "").split("?", 1)[0].rstrip("/")
    media_type = (media_type or "").lower()
    if url and "." in Path(url).name:
        return Path(url).suffix.lstrip(".").lower()
    if "csv" in media_type:
        return "csv"
    if "zip" in media_type:
        return "zip"
    if "excel" in media_type or media_type.endswith("sheet"):
        return "xlsx"
    return "bin"


def resource_score(resource_format: str | None, resource_url: str | None) -> int:
    fmt = (resource_format or "").lower()
    url = (resource_url or "").lower()
    score = 0
    if "csv" in fmt or url.endswith(".csv"):
        score += 100
    if "zip" in fmt or url.endswith(".zip"):
        score += 80
    if "json" in fmt or url.endswith(".json"):
        score += 40
    if "xlsx" in fmt or "excel" in fmt or url.endswith(".xlsx") or url.endswith(".xls"):
        score += 30
    if "schema" in url:
        score -= 10
    return score


class LKODBridge:
    def __init__(self, timeout: tuple[int, int] = DEFAULT_TIMEOUT, verify_ssl: bool = True):
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)

    def close(self) -> None:
        self.session.close()

    def _request(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        try:
            response = self.session.request(
                method,
                url,
                timeout=self.timeout,
                verify=self.verify_ssl,
                **kwargs,
            )
        except requests.RequestException as exc:
            raise LKODBridgeError(f"Request failed: {exc}") from exc
        if not response.ok:
            detail = response.text[:500].strip()
            raise LKODBridgeError(f"HTTP {response.status_code} for {url}. Response excerpt: {detail}")
        return response

    def get_dataset_metadata(self, dataset_id: str) -> dict[str, Any]:
        url = f"{LKOD_BASE_URL}/lkod_ld.datova_sada"
        response = self._request("GET", url, params={"id": str(dataset_id)})
        payload = parse_json_response(response)
        if not isinstance(payload, dict):
            raise LKODBridgeError("Unexpected response type for LKOD dataset metadata.")
        return payload

    def get_resources(self, dataset_id: str) -> pd.DataFrame:
        payload = self.get_dataset_metadata(dataset_id).get("distribuce", [])
        if isinstance(payload, list):
            return pd.DataFrame(payload)
        if isinstance(payload, dict):
            return pd.DataFrame([payload])
        return pd.DataFrame()

    def choose_resource(self, dataset_id: str, resource_num: int | None = None) -> dict[str, Any]:
        resources = self.get_resources(dataset_id)
        if resources.empty:
            raise LKODBridgeError(f"Dataset {dataset_id} has no distributions in LKOD metadata.")

        url_col = guess_column(resources, ["přístupové_url", "pristupove_url", "accessurl", "downloadurl", "url"])
        format_col = guess_column(resources, ["formát", "format", "mediatype", "mimetype"])
        title_col = guess_column(resources, ["název", "nazev", "title"])
        schema_col = guess_column(resources, ["schéma", "schema", "describedby"])
        if url_col is None:
            raise LKODBridgeError(f"Unable to locate resource URL column for dataset {dataset_id}.")

        df = resources.copy()
        if format_col is None:
            df["_format"] = ""
            format_col = "_format"
        if title_col is None:
            df["_title"] = ""
            title_col = "_title"

        df["_score"] = [resource_score(row.get(format_col), row.get(url_col)) for _, row in df.iterrows()]
        if resource_num is not None:
            idx = int(resource_num) - 1
            if idx < 0 or idx >= len(df):
                raise LKODBridgeError(f"resource_num={resource_num} is out of range for dataset {dataset_id}.")
            best = df.iloc[idx]
            chosen_num = int(resource_num)
        else:
            best = df.sort_values("_score", ascending=False).iloc[0]
            chosen_num = int(df.index.get_loc(best.name) + 1)

        return {
            "resource_num": chosen_num,
            "url": str(best[url_col]),
            "format": str(best[format_col]) if format_col in best.index else None,
            "title": str(best[title_col]) if title_col in best.index else None,
            "meta_link": str(best[schema_col]) if schema_col and schema_col in best.index else None,
        }

    def download_resource(
        self,
        dataset_id: str,
        *,
        dest_dir: str | Path | None = None,
        force_redownload: bool = False,
        resource_num: int | None = None,
    ) -> dict[str, Any]:
        pointer = self.choose_resource(dataset_id, resource_num=resource_num)
        base_dir = Path(dest_dir) if dest_dir is not None else Path(tempfile.gettempdir())
        dataset_dir = base_dir.expanduser().resolve() / str(dataset_id)
        dataset_dir.mkdir(parents=True, exist_ok=True)

        ext = infer_extension(pointer.get("url"), pointer.get("format"))
        download_path = dataset_dir / f"ds_{dataset_id}.{ext}"
        if not download_path.exists() or force_redownload:
            response = self._request("GET", str(pointer["url"]), stream=True)
            with download_path.open("wb") as f:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
        pointer["download_path"] = download_path
        pointer["extension"] = ext
        return pointer

    def get_table(
        self,
        dataset_id: str,
        *,
        dest_dir: str | Path | None = None,
        force_redownload: bool = False,
        resource_num: int | None = None,
        csv_kwargs: Mapping[str, Any] | None = None,
        use_first_csv_from_multi_zip: bool = True,
    ) -> pd.DataFrame | list[str] | str:
        pointer = self.download_resource(
            dataset_id,
            dest_dir=dest_dir,
            force_redownload=force_redownload,
            resource_num=resource_num,
        )
        file_path = Path(pointer["download_path"])
        ext = str(pointer.get("extension") or file_path.suffix.lstrip(".")).lower()
        if ext == "csv":
            return read_csv_file(file_path, csv_kwargs=csv_kwargs)
        if ext in {"xlsx", "xls", "xlsm"}:
            return pd.read_excel(file_path)
        if ext == "zip":
            extract_dir = file_path.parent / f"extract_{file_path.stem}"
            extract_dir.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(file_path, "r") as zf:
                zf.extractall(extract_dir)
            csv_files = sorted([p for p in extract_dir.rglob("*.csv") if p.is_file()])
            if len(csv_files) == 1:
                return read_csv_file(csv_files[0], csv_kwargs=csv_kwargs)
            if len(csv_files) > 1 and use_first_csv_from_multi_zip:
                return read_csv_file(csv_files[0], csv_kwargs=csv_kwargs)
            if len(csv_files) > 1:
                return [str(p) for p in csv_files]
            return [str(p) for p in sorted(extract_dir.rglob("*")) if p.is_file()]
        return str(file_path)
