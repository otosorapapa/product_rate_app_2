import streamlit as st
from decimal import Decimal
from pydantic import ValidationError
from core.constants import DEFAULT_MASTER
from core.models import Master
from ui.widgets import sticky_control_bar

st.title("🧮 入力 マスター")

master_dict = st.session_state.get("master", DEFAULT_MASTER.model_dump())

with st.form("master_form"):
    direct_labor_cost = st.number_input("直接人件費 (円/年)", value=float(master_dict["direct_labor_cost"]))
    direct_expenses = st.number_input("直接経費 (円/年)", value=float(master_dict["direct_expenses"]))
    indirect_cost = st.number_input("間接費配賦 (円/年)", value=float(master_dict["indirect_cost"]))
    depreciation = st.number_input("減価償却費 (円/年)", value=float(master_dict["depreciation"]))
    maintenance_cost = st.number_input("維持費 (円/年)", value=float(master_dict["maintenance_cost"]))
    admin_cost = st.number_input("一般管理費配賦 (円/年)", value=float(master_dict["admin_cost"]))
    target_profit = st.number_input("目標利益 (円/年)", value=float(master_dict["target_profit"]))
    variable_cost_per_hour = st.number_input("変動費 (円/時)", value=float(master_dict["variable_cost_per_hour"]))
    fixed_cost = st.number_input("固定費 (円/年)", value=float(master_dict["fixed_cost"]))
    annual_operating_days = st.number_input("年間稼働日", value=int(master_dict["annual_operating_days"]))
    operating_hours_per_day = st.number_input("稼働時間/日", value=float(master_dict["operating_hours_per_day"]))
    equipment_count = st.number_input("稼働設備台数 or 人員", value=int(master_dict["equipment_count"]))
    submitted = st.form_submit_button("保存")

if submitted:
    data = {
        "direct_labor_cost": Decimal(str(direct_labor_cost)),
        "direct_expenses": Decimal(str(direct_expenses)),
        "indirect_cost": Decimal(str(indirect_cost)),
        "depreciation": Decimal(str(depreciation)),
        "maintenance_cost": Decimal(str(maintenance_cost)),
        "admin_cost": Decimal(str(admin_cost)),
        "target_profit": Decimal(str(target_profit)),
        "variable_cost_per_hour": Decimal(str(variable_cost_per_hour)),
        "fixed_cost": Decimal(str(fixed_cost)),
        "annual_operating_days": int(annual_operating_days),
        "operating_hours_per_day": Decimal(str(operating_hours_per_day)),
        "equipment_count": int(equipment_count),
    }
    try:
        master = Master(**data)
    except ValidationError as e:
        st.error(e)
    else:
        st.session_state["master"] = master.model_dump()
        st.success("マスターを保存しました。")

sticky_control_bar(st.session_state.get("master", {}), st.session_state.get("scenario", {}))
