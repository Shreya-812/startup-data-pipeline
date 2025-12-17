import sys
import os

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

CSV_PATH = "data/output_leads.csv"


@st.cache_data
def load_or_generate_data():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)

    # Generate in-memory dataframe (cloud-safe)
    return generate_leads()



df = load_or_generate_data()
