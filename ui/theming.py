"""Theme synchronisation utilities."""
import json
from pathlib import Path

CONFIG_PATH = Path(".streamlit/config.toml")


def load_theme() -> dict:
    """Load theme settings from config.toml if available."""
    if CONFIG_PATH.exists():
        return {"config_path": str(CONFIG_PATH)}
    return {}
