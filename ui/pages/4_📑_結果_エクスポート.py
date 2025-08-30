import json
import streamlit as st
from core.models import Result
from ui.widgets import sticky_control_bar

st.title("📑 結果 エクスポート")

if "result" in st.session_state:
    data = st.session_state["result"]
    st.download_button(
        "結果をJSONでダウンロード",
        data=json.dumps(data, ensure_ascii=False, indent=2),
        file_name="result.json",
        mime="application/json",
    )
else:
    st.info("まだ計算結果がありません。『シミュレーション』で計算してください。")

sticky_control_bar(st.session_state.get("master", {}), st.session_state.get("scenario", {}))
