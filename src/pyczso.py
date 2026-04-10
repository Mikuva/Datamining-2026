from __future__ import annotations

"""Lightweight Python client for the CZSO DataStat API.

The module is designed as a pragmatic Python equivalent to the most useful
catalogue-oriented parts of the R `czso` package. It focuses on catalogue
exploration, metadata access, codelists, predefined selection download, and
custom POST queries.

It works well inside a Conda/Anaconda environment and can be used either via
simple top-level functions or through the ``CZSOClient`` class.
"""

from dataclasses import dataclass
import io
import re
from typing import Any, Iterable, Mapping, Sequence

import pandas as pd
import requests

__all__ = [
    "CZSOAPIError",
    "CZSOClient",
    "czso_build_query",
    "czso_dimension",
    "czso_filter_catalogue",
    "czso_get_catalogue",
    "czso_get_codelist",
    "czso_get_custom_query",
    "czso_get_dataset_dimensions",
    "czso_get_dataset_indicators",
    "czso_get_dataset_metadata",
    "czso_get_dataset_selections",
    "czso_get_dimension_datasets",
    "czso_get_indicator_datasets",
    "czso_get_selection_metadata",
    "czso_get_table",
    "czso_get_table_schema",
    "czso_keep_latest_versions",
    "czso_normalize_catalogue",
    "czso_table_filter",
    "get_catalogue",
    "get_custom_query",
    "get_dataset_metadata",
    "get_selection_csv",
]

__version__ = "0.1.0"
BASE_URL = "https://data.csu.gov.cz/api"
DEFAULT_TIMEOUT = (10, 120)
DEFAULT_HEADERS = {
    "User-Agent": f"pyczso/{__version__} (+https://data.csu.gov.cz/api)",
    "Accept": "application/json, text/csv, text/plain, */*",
}


class CZSOAPIError(RuntimeError):
    """Raised when the CZSO DataStat API request fails."""


def _coerce_string_list(items: Iterable[Any] | None) -> list[str]:
    if items is None:
        return []
    return [str(item) for item in items]


def _dataframe_from_json(payload: Any) -> pd.DataFrame:
    if isinstance(payload, pd.DataFrame):
        return payload.copy()
    if isinstance(payload, list):
        if not payload:
            return pd.DataFrame()
        if isinstance(payload[0], Mapping):
            return pd.DataFrame(payload)
        return pd.DataFrame({"value": payload})
    if isinstance(payload, Mapping):
        return pd.DataFrame([payload])
    return pd.DataFrame({"value": [payload]})


def _read_csv_autodetect(text: str, csv_kwargs: Mapping[str, Any] | None = None) -> pd.DataFrame:
    kwargs: dict[str, Any] = {"sep": None, "engine": "python"}
    if csv_kwargs:
        kwargs.update(dict(csv_kwargs))
    return pd.read_csv(io.StringIO(text), **kwargs)


def _bool_to_api(value: bool | None) -> str | None:
    if value is None:
        return None
    return "true" if value else "false"


def _guess_column(df: pd.DataFrame, candidates: Sequence[str]) -> str | None:
    lowered = {col.lower(): col for col in df.columns}

    for candidate in candidates:
        if candidate.lower() in lowered:
            return lowered[candidate.lower()]

    normalized = {
        re.sub(r"[^a-z0-9]+", "", col.lower()): col for col in df.columns
    }
    for candidate in candidates:
        key = re.sub(r"[^a-z0-9]+", "", candidate.lower())
        if key in normalized:
            return normalized[key]

    for col in df.columns:
        compact = re.sub(r"[^a-z0-9]+", "", col.lower())
        for candidate in candidates:
            key = re.sub(r"[^a-z0-9]+", "", candidate.lower())
            if key and key in compact:
                return col
    return None


def _string_columns(df: pd.DataFrame) -> list[str]:
    cols: list[str] = []
    for col in df.columns:
        if pd.api.types.is_string_dtype(df[col]) or df[col].dtype == object:
            cols.append(col)
    return cols


def _combine_searchable_text(df: pd.DataFrame, columns: Sequence[str] | None = None) -> pd.Series:
    if df.empty:
        return pd.Series(dtype="string")

    use_columns = list(columns) if columns else _string_columns(df)
    if not use_columns:
        use_columns = list(df.columns)
    return df[use_columns].fillna("").astype(str).agg(" | ".join, axis=1)


@dataclass
class CZSOClient:
    """Client for the CZSO DataStat API."""

    base_url: str = BASE_URL
    timeout: tuple[int, int] = DEFAULT_TIMEOUT
    verify_ssl: bool = True
    session: requests.Session | None = None

    def __post_init__(self) -> None:
        if self.session is None:
            self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)

    def close(self) -> None:
        if self.session is not None:
            self.session.close()

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json_body: Mapping[str, Any] | None = None,
    ) -> requests.Response:
        url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json_body,
                timeout=self.timeout,
                verify=self.verify_ssl,
            )
        except requests.RequestException as exc:
            raise CZSOAPIError(f"Request to CZSO API failed: {exc}") from exc

        if not response.ok:
            detail = response.text[:500].strip()
            raise CZSOAPIError(
                f"CZSO API returned HTTP {response.status_code} for {url}. "
                f"Response excerpt: {detail}"
            )
        return response

    def _get_json(self, path: str, *, params: Mapping[str, Any] | None = None) -> Any:
        response = self._request("GET", path, params=params)
        try:
            return response.json()
        except ValueError as exc:
            raise CZSOAPIError(f"Expected JSON response from {path}, but parsing failed.") from exc

    def get_catalogue(self, *, as_frame: bool = True) -> pd.DataFrame | list[dict[str, Any]]:
        payload = self._get_json("/katalog/v1/sady")
        return _dataframe_from_json(payload) if as_frame else payload

    def get_dataset_metadata(self, dataset_code: str) -> dict[str, Any]:
        payload = self._get_json(f"/katalog/v1/sady/{dataset_code}")
        if not isinstance(payload, dict):
            raise CZSOAPIError("Unexpected response type for dataset metadata.")
        return payload

    def get_dataset_selections(
        self, dataset_code: str, *, as_frame: bool = True
    ) -> pd.DataFrame | list[dict[str, Any]]:
        payload = self._get_json(f"/katalog/v1/sady/{dataset_code}/vybery")
        return _dataframe_from_json(payload) if as_frame else payload

    def get_dataset_indicators(
        self, dataset_code: str, *, as_frame: bool = True
    ) -> pd.DataFrame | list[dict[str, Any]]:
        payload = self._get_json(f"/katalog/v1/sady/{dataset_code}/ukazatele")
        return _dataframe_from_json(payload) if as_frame else payload

    def get_dataset_dimensions(
        self, dataset_code: str, *, as_frame: bool = True
    ) -> pd.DataFrame | list[dict[str, Any]]:
        payload = self._get_json(f"/katalog/v1/sady/{dataset_code}/dimenze")
        return _dataframe_from_json(payload) if as_frame else payload

    def get_selection_metadata(self, selection_code: str) -> dict[str, Any]:
        payload = self._get_json(f"/katalog/v1/vybery/{selection_code}")
        if not isinstance(payload, dict):
            raise CZSOAPIError("Unexpected response type for selection metadata.")
        return payload

    def get_indicator_datasets(
        self, indicator_code: str | int, *, as_frame: bool = True
    ) -> pd.DataFrame | list[dict[str, Any]]:
        payload = self._get_json(f"/katalog/v1/ukazatele/{indicator_code}/sady")
        return _dataframe_from_json(payload) if as_frame else payload

    def get_dimension_datasets(
        self, dimension_code: str, *, as_frame: bool = True
    ) -> pd.DataFrame | list[dict[str, Any]]:
        payload = self._get_json(f"/katalog/v1/dimenze/{dimension_code}/sady")
        return _dataframe_from_json(payload) if as_frame else payload

    def get_codelist(
        self, dimension_code: str, *, as_frame: bool = True
    ) -> pd.DataFrame | list[dict[str, Any]]:
        payload = self._get_json(f"/katalog/v1/dimenze/{dimension_code}/polozky")
        return _dataframe_from_json(payload) if as_frame else payload

    def get_table(
        self,
        selection_code: str,
        *,
        format: str = "CSV",
        csv_kwargs: Mapping[str, Any] | None = None,
        jsonstat_as_dataframe: bool = False,
    ) -> pd.DataFrame | dict[str, Any] | str | bytes:
        fmt = format.upper()
        response = self._request(
            "GET",
            f"/dotaz/v1/data/vybery/{selection_code}",
            params={"format": fmt},
        )
        return _parse_content(response, fmt, csv_kwargs, jsonstat_as_dataframe)

    def get_custom_query(
        self,
        dataset_code: str,
        version: int,
        body: Mapping[str, Any],
        *,
        format: str = "CSV",
        include_codes: bool | None = None,
        notes: bool | None = None,
        scope: str | None = None,
        note_format: str | None = None,
        csv_kwargs: Mapping[str, Any] | None = None,
        jsonstat_as_dataframe: bool = False,
    ) -> pd.DataFrame | dict[str, Any] | str | bytes:
        fmt = format.upper()
        params: dict[str, Any] = {"verzeSady": int(version), "format": fmt}
        bool_flags = {
            "kodZvlast": _bool_to_api(include_codes),
            "poznamky": _bool_to_api(notes),
        }
        for key, value in bool_flags.items():
            if value is not None:
                params[key] = value
        if scope is not None:
            params["rozsah"] = scope
        if note_format is not None:
            params["formatPoznamek"] = note_format

        response = self._request(
            "POST",
            f"/dotaz/v1/data/sady/{dataset_code}/vlastni",
            params=params,
            json_body=dict(body),
        )
        return _parse_content(response, fmt, csv_kwargs, jsonstat_as_dataframe)

    def get_table_schema(self, dataset_code: str) -> dict[str, Any]:
        """Return a synthetic schema assembled from multiple catalogue endpoints.

        This is a convenience helper, not a dedicated DataStat endpoint.
        """
        return {
            "metadata": self.get_dataset_metadata(dataset_code),
            "selections": self.get_dataset_selections(dataset_code, as_frame=True),
            "indicators": self.get_dataset_indicators(dataset_code, as_frame=True),
            "dimensions": self.get_dataset_dimensions(dataset_code, as_frame=True),
        }


def _parse_content(
    response: requests.Response,
    fmt: str,
    csv_kwargs: Mapping[str, Any] | None,
    jsonstat_as_dataframe: bool,
) -> pd.DataFrame | dict[str, Any] | str | bytes:
    fmt = fmt.upper()
    if fmt == "CSV":
        return _read_csv_autodetect(response.text, csv_kwargs=csv_kwargs)
    if fmt in {"JSON", "JSON_STAT", "JSON-STAT"}:
        payload = response.json()
        if jsonstat_as_dataframe:
            try:
                from pyjstat import pyjstat  # type: ignore
            except ImportError as exc:
                raise ImportError(
                    "Package 'pyjstat' is required for jsonstat_as_dataframe=True. "
                    "Install it with: pip install pyjstat"
                ) from exc
            return pyjstat.Dataset.read(payload).write('dataframe')
        return payload
    if fmt == "HTML":
        return response.text
    return response.content


_DEFAULT_CLIENT: CZSOClient | None = None


def _get_default_client() -> CZSOClient:
    global _DEFAULT_CLIENT
    if _DEFAULT_CLIENT is None:
        _DEFAULT_CLIENT = CZSOClient()
    return _DEFAULT_CLIENT


def czso_get_catalogue(*, as_frame: bool = True) -> pd.DataFrame | list[dict[str, Any]]:
    return _get_default_client().get_catalogue(as_frame=as_frame)


def czso_get_dataset_metadata(dataset_code: str) -> dict[str, Any]:
    return _get_default_client().get_dataset_metadata(dataset_code)


def czso_get_dataset_selections(
    dataset_code: str, *, as_frame: bool = True
) -> pd.DataFrame | list[dict[str, Any]]:
    return _get_default_client().get_dataset_selections(dataset_code, as_frame=as_frame)


def czso_get_dataset_indicators(
    dataset_code: str, *, as_frame: bool = True
) -> pd.DataFrame | list[dict[str, Any]]:
    return _get_default_client().get_dataset_indicators(dataset_code, as_frame=as_frame)


def czso_get_dataset_dimensions(
    dataset_code: str, *, as_frame: bool = True
) -> pd.DataFrame | list[dict[str, Any]]:
    return _get_default_client().get_dataset_dimensions(dataset_code, as_frame=as_frame)


def czso_get_selection_metadata(selection_code: str) -> dict[str, Any]:
    return _get_default_client().get_selection_metadata(selection_code)


def czso_get_indicator_datasets(
    indicator_code: str | int, *, as_frame: bool = True
) -> pd.DataFrame | list[dict[str, Any]]:
    return _get_default_client().get_indicator_datasets(indicator_code, as_frame=as_frame)


def czso_get_dimension_datasets(
    dimension_code: str, *, as_frame: bool = True
) -> pd.DataFrame | list[dict[str, Any]]:
    return _get_default_client().get_dimension_datasets(dimension_code, as_frame=as_frame)


def czso_get_codelist(
    dimension_code: str, *, as_frame: bool = True
) -> pd.DataFrame | list[dict[str, Any]]:
    return _get_default_client().get_codelist(dimension_code, as_frame=as_frame)


def czso_get_table(
    selection_code: str,
    *,
    format: str = "CSV",
    csv_kwargs: Mapping[str, Any] | None = None,
    jsonstat_as_dataframe: bool = False,
) -> pd.DataFrame | dict[str, Any] | str | bytes:
    return _get_default_client().get_table(
        selection_code,
        format=format,
        csv_kwargs=csv_kwargs,
        jsonstat_as_dataframe=jsonstat_as_dataframe,
    )


def czso_dimension(kod_dimenze: str, polozky: Iterable[Any] | None = None) -> dict[str, Any]:
    """Create a dimension specification for a custom POST query."""
    spec = {"kodDimenze": str(kod_dimenze), "filtr": []}
    items = _coerce_string_list(polozky)
    if items:
        spec["filtr"] = [{"zobrazitPolozky": items}]
    return spec


def czso_table_filter(kod_dimenze: str, filtr_tabulky_kod: Any) -> dict[str, Any]:
    """Create a table-filter specification for XLSX/HTML style custom queries."""
    return {
        "kodDimenze": str(kod_dimenze),
        "filtrTabulkyKod": str(filtr_tabulky_kod),
    }


def czso_build_query(
    sloupce: Sequence[Mapping[str, Any]] | None = None,
    radky: Sequence[Mapping[str, Any]] | None = None,
    filtry_tabulky: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Build the JSON body expected by the custom POST query endpoint."""
    return {
        "sloupce": list(sloupce or []),
        "radky": list(radky or []),
        "filtryTabulky": list(filtry_tabulky or []),
    }


def czso_get_custom_query(
    dataset_code: str,
    version: int,
    body: Mapping[str, Any],
    *,
    format: str = "CSV",
    include_codes: bool | None = None,
    notes: bool | None = None,
    scope: str | None = None,
    note_format: str | None = None,
    csv_kwargs: Mapping[str, Any] | None = None,
    jsonstat_as_dataframe: bool = False,
) -> pd.DataFrame | dict[str, Any] | str | bytes:
    return _get_default_client().get_custom_query(
        dataset_code,
        version,
        body,
        format=format,
        include_codes=include_codes,
        notes=notes,
        scope=scope,
        note_format=note_format,
        csv_kwargs=csv_kwargs,
        jsonstat_as_dataframe=jsonstat_as_dataframe,
    )


def czso_get_table_schema(dataset_code: str) -> dict[str, Any]:
    return _get_default_client().get_table_schema(dataset_code)


def czso_normalize_catalogue(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize raw catalogue columns to a stable analysis-friendly schema.

    The function tries to support both:
    - the current DataStat catalogue API response,
    - legacy or manually exported CZSO catalogue CSV files.
    """
    out = df.copy()
    mapping: dict[str, list[str]] = {
        "dataset_code": ["kodSady", "kod", "dataset_id", "dataset_code"],
        "dataset_title": ["nazevSady", "nazev", "title", "dataset_title"],
        "dataset_version": ["verzeSady", "verze", "version", "dataset_version"],
        "description": ["popis", "description", "anotace"],
        "modified": ["datumAktualizace", "modified", "updated", "zmeneno"],
        "periodicity": ["periodicita", "periodicity"],
        "keywords": ["klicovaSlova", "keywords", "keywords_all"],
        "dataset_page": ["stranka", "page", "url", "dataset_url"],
    }

    rename_map: dict[str, str] = {}
    for target, candidates in mapping.items():
        source = _guess_column(out, candidates)
        if source is not None and source != target:
            rename_map[source] = target

    out = out.rename(columns=rename_map)
    for column in mapping:
        if column not in out.columns:
            out[column] = pd.NA
    return out


def czso_keep_latest_versions(
    catalogue: pd.DataFrame,
    *,
    code_column: str | None = None,
    version_column: str | None = None,
) -> pd.DataFrame:
    """Keep only the highest version per dataset code when possible."""
    if catalogue.empty:
        return catalogue.copy()

    df = catalogue.copy()
    code_col = code_column or _guess_column(df, ["dataset_code", "kodSady", "kod", "dataset_id"])
    version_col = version_column or _guess_column(df, ["dataset_version", "verzeSady", "verze", "version"])

    if code_col is None or version_col is None:
        return df

    tmp_version = pd.to_numeric(df[version_col], errors="coerce")
    if tmp_version.isna().all():
        return df

    df = df.assign(_version_numeric=tmp_version)
    latest_idx = (
        df.sort_values([code_col, "_version_numeric"], ascending=[True, False])
        .groupby(code_col, dropna=False)
        .head(1)
        .index
    )
    out = df.loc[latest_idx].drop(columns=["_version_numeric"])
    return out.reset_index(drop=True)


def czso_filter_catalogue(
    catalogue: pd.DataFrame,
    *,
    text: str | Sequence[str] | None = None,
    regex: str | None = None,
    columns: Sequence[str] | None = None,
    latest_only: bool = False,
    normalize: bool = False,
) -> pd.DataFrame:
    """Filter catalogue rows by keyword search across string columns.

    Parameters
    ----------
    catalogue:
        Raw or normalized catalogue DataFrame.
    text:
        One keyword or a list of keywords. All provided keywords must match.
    regex:
        Optional regular expression applied over the combined searchable text.
    columns:
        Restrict search to selected columns.
    latest_only:
        If True, keep only the highest available version per dataset.
    normalize:
        If True, run ``czso_normalize_catalogue`` before filtering.
    """
    df = czso_normalize_catalogue(catalogue) if normalize else catalogue.copy()
    if df.empty:
        return df

    searchable = _combine_searchable_text(df, columns=columns)
    mask = pd.Series(True, index=df.index)

    if text is not None:
        terms = [text] if isinstance(text, str) else list(text)
        for term in terms:
            clean_term = str(term).strip()
            if clean_term:
                mask &= searchable.str.contains(re.escape(clean_term), case=False, regex=True)

    if regex:
        mask &= searchable.str.contains(regex, case=False, regex=True)

    out = df.loc[mask].reset_index(drop=True)
    if latest_only:
        out = czso_keep_latest_versions(out)
    return out


# R-style / snippet-style aliases -------------------------------------------------
get_catalogue = czso_get_catalogue
get_dataset_metadata = czso_get_dataset_metadata


def get_selection_csv(
    selection_code: str,
    *,
    csv_kwargs: Mapping[str, Any] | None = None,
) -> pd.DataFrame:
    return czso_get_table(selection_code, format="CSV", csv_kwargs=csv_kwargs)


get_custom_query = czso_get_custom_query
