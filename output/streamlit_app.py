import streamlit as st
import pandas as pd
import os
from main import generate_leads

st.set_page_config(
    page_title="Startup Lead Scoring Dashboard",
    layout="wide"
)

st.title("🔬 Startup Lead Scoring Dashboard")
st.caption("Reproducible lead-ranking pipeline based on public scientific data")

CSV_PATH = "data/output_leads.csv"


@st.cache_data
def load_or_generate_data():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)

    # Generate data directly (no subprocess)
    return generate_leads(CSV_PATH)


df = load_or_generate_data()
