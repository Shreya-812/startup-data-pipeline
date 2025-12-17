import pandas as pd
from data_sources.pubmed import search_pubmed, fetch_details
from enrichment.email_infer import infer_email
from enrichment.location_parser import extract_location
from scoring.propensity_model import score_person


def generate_leads():
    """
    Generates ranked leads as a pandas DataFrame.
    No disk writes. Streamlit-safe.
    """
    pmids = search_pubmed("3D in vitro liver toxicity", max_results=15)

    if not pmids:
        return pd.DataFrame(columns=[
            "rank", "name", "title", "company",
            "location", "email", "score"
        ])

    people = fetch_details(pmids)

    enriched = []
    for p in people:
        enriched.append({
            "name": p.get("name"),
            "title": p.get("title"),
            "company": p.get("company"),
            "location": extract_location(p.get("company")),
            "email": infer_email(p.get("name"), p.get("company")),
            "score": score_person(p)
        })

    df = pd.DataFrame(enriched)
    df = df.sort_values("score", ascending=False).reset_index(drop=True)
    df.insert(0, "rank", df.index + 1)

    return df


# Optional: local-only testing
if __name__ == "__main__":
    df = generate_leads()
    df.to_csv("output.lead.csv", index=False)
    print("Saved output.lead.csv locally")
