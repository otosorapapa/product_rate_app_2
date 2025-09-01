import streamlit as st
from core.constants import DEFAULT_MASTER, DEFAULT_SCENARIO
from core.models import Master, Scenario, Result
from core.formulas import compute_rates
from core.genai import summarize_inputs
from ui.widgets import kpi_tile, sticky_control_bar
from ui.theming import apply_theme

apply_theme()
st.title("📊 ダッシュボード")

master_dict = st.session_state.get("master", DEFAULT_MASTER.model_dump())
scenario_dict = st.session_state.get("scenario", DEFAULT_SCENARIO.model_dump())

master = Master(**master_dict)
scenario = Scenario(**scenario_dict)
if "result" not in st.session_state:
    res = compute_rates(master, scenario)
    st.session_state["result"] = res.model_dump()

res = Result(**st.session_state["result"])
kpi_tile("必要賃率 (円/時)", res.required_rate)
kpi_tile("損益分岐賃率 (円/時)", res.break_even_rate)

st.subheader("AI要約")
st.write(summarize_inputs(master, scenario))

sticky_control_bar(master_dict, scenario_dict)
