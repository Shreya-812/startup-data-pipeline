import streamlit as st
import pandas as pd
import os
import subprocess

st.set_page_config(
    page_title="Startup Lead Scoring Dashboard",
    layout="wide"
)

st.title("🔬 Startup Lead Scoring Dashboard")
st.caption("Reproducible lead-ranking pipeline based on public scientific data")

CSV_PATH = "data/output_leads.csv"


@st.cache_data
def load_or_generate_data():
    # If CSV doesn't exist, generate it by running main.py
    if not os.path.exists(CSV_PATH):
        with st.spinner("Generating lead data (first run)..."):
            subprocess.run(
                ["python", "main.py"],
                check=True
            )

    return pd.read_csv(CSV_PATH)


df = load_or_generate_data()

# Sidebar filters
st.sidebar.header("Filters")

location_filter = st.sidebar.multiselect(
    "Filter by Location",
    options=sorted(df["location"].dropna().unique())
)

keyword = st.sidebar.text_input("Search Keyword (name / title / paper)")

filtered_df = df.copy()

if location_filter:
    filtered_df = filtered_df[filtered_df["location"].isin(location_filter)]

if keyword:
    keyword = keyword.lower()
    filtered_df = filtered_df[
        filtered_df.apply(
            lambda row: keyword in " ".join(row.astype(str)).lower(),
            axis=1
        )
    ]

filtered_df = filtered_df.sort_values("score", ascending=False)

st.subheader(f"Results ({len(filtered_df)} leads)")
st.dataframe(filtered_df, use_container_width=True)

st.download_button(
    label="⬇️ Download CSV",
    data=filtered_df.to_csv(index=False),
    file_name="ranked_leads.csv",
    mime="text/csv"
)
