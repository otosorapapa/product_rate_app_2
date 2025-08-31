import streamlit as st
from core.audit import AuditLog
from ui.widgets import sticky_control_bar
from ui.theming import apply_theme

apply_theme()
st.title("🛠️ DevTools ログ")

log: AuditLog | None = st.session_state.get("audit")
if log is None or not log.entries:
    st.info("まだログがありません。")
else:
    st.write("計算ログ:")
    for entry in log.entries:
        st.write("- ", entry)

sticky_control_bar(st.session_state.get("master", {}), st.session_state.get("scenario", {}))
