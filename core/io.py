"""Data I/O helpers (CSV/XLSX/JSON).

These are placeholders for future implementation in later phases."""
from __future__ import annotations
from pathlib import Path
from typing import Any


def load_workbook(path: str | Path) -> Any:
    """Placeholder for heavy I/O loading of workbooks.

    In later phases this function will be wrapped with ``st.cache_resource``.
    """
    raise NotImplementedError("Workbook loading not implemented yet")
