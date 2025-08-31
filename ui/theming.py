"""Theme utilities for applying a McKinsey-style design."""
from pathlib import Path
import streamlit as st

CONFIG_PATH = Path(".streamlit/config.toml")
STYLE_PATH = Path("ui/styles/mckinsey.css")


def load_theme() -> dict:
    """Load theme settings from config.toml if available."""
    if CONFIG_PATH.exists():
        return {"config_path": str(CONFIG_PATH)}
    return {}


def apply_theme() -> None:
    """Inject global CSS for a calm and refined design."""
    if STYLE_PATH.exists():
        css = STYLE_PATH.read_text()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
