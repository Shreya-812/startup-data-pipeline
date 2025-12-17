import sys
import os

# Ensure project root is importable
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
import pandas as pd
from main import generate_leads


st.set_page_config(
    page_title="Startup Lead Scoring Dashboard",
    layout="wide"
)

st.title("🔬 Startup Lead Scoring Dashboard")
st.caption("Reproducible lead-ranking pipeline based on public scientific data")


@st.cache_data
def load_data():
    return generate_leads()


with st.spinner("Generating and ranking leads..."):
    df = load_data()


st.subheader("Pipeline Status")
st.write("Rows generated:", len(df))

if df.empty:
    st.warning("No leads were generated for the current query.")
    st.stop()


st.subheader("Ranked Leads")
st.dataframe(df, use_container_width=True)


st.download_button(
    label="⬇️ Download CSV",
    data=df.to_csv(index=False),
    file_name="output.lead.csv",
    mime="text/csv"
)
