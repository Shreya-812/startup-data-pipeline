import requests
import xml.etree.ElementTree as ET
from datetime import datetime

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def search_pubmed(query, max_results=20):
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "sort": "pub date",
        "retmode": "json"
    }
    res = requests.get(PUBMED_SEARCH_URL, params=params)
    res.raise_for_status()
    return res.json()["esearchresult"]["idlist"]


def fetch_details(pmids):
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml"
    }
    res = requests.get(PUBMED_FETCH_URL, params=params)
    res.raise_for_status()

    root = ET.fromstring(res.text)
    people = []

    for article in root.findall(".//PubmedArticle"):
        title = article.findtext(".//ArticleTitle")
        year = article.findtext(".//PubDate/Year")

        for author in article.findall(".//Author"):
            last = author.findtext("LastName")
            first = author.findtext("ForeName")
            aff = author.findtext(".//Affiliation")

            if not (first and last and aff):
                continue

            people.append({
                "name": f"{first} {last}",
                "title": "Research Scientist",
                "company": aff,
                "paper_title": title,
                "publication_year": year
            })

    return people
