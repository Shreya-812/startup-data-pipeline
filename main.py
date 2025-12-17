import pandas as pd
from data_sources.pubmed import search_pubmed, fetch_details
from enrichment.email_infer import infer_email
from enrichment.location_parser import extract_location
from scoring.propensity_model import score_person


def run():
    print("🔍 Searching PubMed...")
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

    df.to_csv("data/output_leads.csv", index=False)
    print("✅ Output written to data/output_leads.csv")


if __name__ == "__main__":
    run()
