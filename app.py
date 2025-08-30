import streamlit as st
from core.constants import DEFAULT_MASTER, DEFAULT_SCENARIO

st.set_page_config(page_title="賃率ダッシュボード", layout="wide")

st.title("製品賃率ダッシュボード")
st.caption("製造業向けの標準賃率計算ツール")

# Initialise session state
st.session_state.setdefault("master", DEFAULT_MASTER.model_dump())
st.session_state.setdefault("scenario", DEFAULT_SCENARIO.model_dump())

st.page_link("ui/pages/1_📊_ダッシュボード.py", label="📊 ダッシュボード", icon="📊")
st.page_link("ui/pages/2_🧮_入力_マスター.py", label="🧮 入力 マスター", icon="🧮")
st.page_link("ui/pages/3_🧪_シミュレーション.py", label="🧪 シミュレーション", icon="🧪")
st.page_link("ui/pages/4_📑_結果_エクスポート.py", label="📑 結果 エクスポート", icon="📑")
st.page_link("ui/pages/9_🛠️_DevTools_ログ.py", label="🛠️ DevTools ログ", icon="🛠️")
