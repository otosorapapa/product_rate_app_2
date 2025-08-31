import time
from decimal import Decimal
import streamlit as st
import plotly.graph_objects as go
from pydantic import ValidationError
from core.models import Master, Scenario, Result
from core.formulas import compute_rates
from core.constants import DEFAULT_MASTER, DEFAULT_SCENARIO
from core.audit import AuditLog
from ui.widgets import kpi_tile, sticky_control_bar
from ui.theming import apply_theme

apply_theme()
st.title("🧪 シミュレーション")

master_dict = st.session_state.get("master", DEFAULT_MASTER.model_dump())
scenario_dict = st.session_state.get("scenario", DEFAULT_SCENARIO.model_dump())

availability = st.slider("稼働率", 0.0, 1.0, float(scenario_dict["availability_rate"]), 0.01)
yield_rate = st.slider("良品率", 0.0, 1.0, float(scenario_dict["yield_rate"]), 0.01)
calc = st.button("計算")

if calc:
    scen_data = {
        "availability_rate": Decimal(str(availability)),
        "yield_rate": Decimal(str(yield_rate)),
    }
    try:
        master = Master(**master_dict)
        scenario = Scenario(**scen_data)
    except ValidationError as e:
        st.error(e)
    else:
        st.session_state["scenario"] = scenario.model_dump()
        cache = st.session_state.get("use_cache", True)

        @st.cache_data(show_spinner=False)
        def _calc(m: dict, s: dict) -> dict:
            m_obj = Master(**m)
            s_obj = Scenario(**s)
            return compute_rates(m_obj, s_obj).model_dump()

        start = time.time()
        if cache:
            result_dict = _calc(master_dict, scen_data)
        else:
            result_dict = compute_rates(master, scenario).model_dump()
        elapsed = (time.time() - start) * 1000

        log: AuditLog = st.session_state.setdefault("audit", AuditLog())
        log.add(f"compute_rates {elapsed:.2f} ms")
        st.session_state["result"] = result_dict

if "result" in st.session_state:
    res = Result(**st.session_state["result"])
    kpi_tile("必要賃率 (円/時)", res.required_rate)
    kpi_tile("損益分岐賃率 (円/時)", res.break_even_rate)

    master = Master(**master_dict)
    components = [
        ("直接人件費", master.direct_labor_cost),
        ("直接経費", master.direct_expenses),
        ("間接費配賦", master.indirect_cost),
        ("減価償却", master.depreciation),
        ("維持費", master.maintenance_cost),
        ("一般管理費配賦", master.admin_cost),
        ("目標利益", master.target_profit),
    ]
    labels = [c[0] for c in components] + ["合計"]
    values = [float(c[1]) for c in components]
    total = float(sum(c[1] for c in components))
    measures = ["relative"] * len(components) + ["total"]
    y = values + [total]
    fig = go.Figure(go.Waterfall(x=labels, measure=measures, y=y, connector={"line": {"color": "rgb(63, 63, 63)"}}))
    fig.update_layout(title="必要賃率 構成 (円/年)")
    st.plotly_chart(fig, use_container_width=True)

sticky_control_bar(master_dict, st.session_state.get("scenario", {}))
