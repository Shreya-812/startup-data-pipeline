# Startup Lead Scoring Pipeline

A reproducible data pipeline that identifies, enriches, and ranks scientific professionals
based on their likelihood to adopt 3D in-vitro models for therapy research.

## Objective
Build a lightweight, verifiable alternative to commercial lead-gen tools by:
- Crawling public scientific data
- Enriching researcher profiles
- Scoring leads using transparent, rule-based logic
- Presenting results in a live, inspectable dashboard

## Data Sources
- **PubMed**: Recent publications related to liver toxicity, 3D in-vitro models
- Public affiliation metadata (institutions, locations)

> Note: LinkedIn scraping was intentionally avoided due to ToS constraints.  
> The architecture supports future integration with APIs such as Proxycurl, Clay, or Apollo.

## Pipeline Architecture
data_sources → enrichment → scoring → presentation


### Identification
- Fetches recent PubMed papers using domain-specific keywords
- Extracts author names and affiliations

### Enrichment
- Infers business emails using heuristics
- Extracts geographic location from affiliation text

### Scoring (0–100)
Weighted signals include:
- Role relevance
- Scientific intent (keyword match)
- Recency of publications
- Geographic relevance

### Output
- Ranked, filterable table
- CSV download (`output.lead.csv`)
- Live Streamlit dashboard

## Live Demo
👉 https://startup-data-pipeline-lgfx3h8dzbk5avaygry3zy.streamlit.app

## Reproducibility
The Streamlit app is fully stateless:
- No credentials required
- No disk persistence
- Data generated in-memory on each run

## Future Extensions
- Conference attendee ingestion
- Funding signal enrichment (Crunchbase, NIH RePORTER)
- ML-based propensity scoring
