
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="LaLaLeads — CRM Analytics", layout="wide")
st.title("LaLaLeads — CRM Analytics")
st.caption("This Streamlit app wraps your existing single-file HTML dashboard. Use the controls inside the embedded view.")

html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

# Render the full HTML dashboard inside Streamlit
components.html(html_content, height=1000, scrolling=True)
