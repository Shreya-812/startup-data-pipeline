import os
import pandas as pd
from data_sources.pubmed import search_pubmed, fetch_details
from enrichment.email_infer import infer_email
from enrichment.location_parser import extract_location
from scoring.propensity_model import score_person


def generate_leads(output_path=None):
    pmids = search_pubmed("3D in vitro liver toxicity", max_results=15)
    people = fetch_details(pmids)

    enriched = []
    for p in people:
        p["email"] = infer_email(p["name"], p["company"])
        p["location"] = extract_location(p["company"])
        p["score"] = score_person(p)
        enriched.append(p)

    df = pd.DataFrame(enriched)
    df = df.sort_values("score", ascending=False)
    df["rank"] = range(1, len(df) + 1)

    # ✅ Only write to disk if path is provided
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)

    return df
