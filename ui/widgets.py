"""Reusable Streamlit UI widgets."""
from __future__ import annotations
import streamlit as st
from decimal import Decimal


def sticky_control_bar(master: dict, scenario: dict) -> None:
    """Render a simple sticky control bar with key parameters.

    Parameters are displayed for quick inspection and editing.
    """
    st.session_state.setdefault("use_cache", True)
    with st.container():
        st.checkbox("Use cache", value=st.session_state["use_cache"], key="use_cache")
        st.write("Current scenario:")
        st.json({"master": master, "scenario": scenario})


def kpi_tile(label: str, value: Decimal, delta: Decimal | None = None) -> None:
    """Render a KPI metric tile."""
    delta_str = f"{delta:+.2f}" if delta is not None else None
    st.metric(label, f"{value:,.2f}", delta=delta_str)
