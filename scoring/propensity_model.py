from datetime import datetime

KEYWORDS = ["toxicity", "liver", "3d", "organ", "hepatic"]
HUBS = ["Boston", "Cambridge", "Basel", "Uk"]


def score_person(person):
    score = 0

    # Role fit
    if "scientist" in person["title"].lower():
        score += 20

    # Scientific intent
    if any(k in (person.get("paper_title") or "").lower() for k in KEYWORDS):
        score += 40

    # Recency
    try:
        year = int(person.get("publication_year", 0))
        if datetime.now().year - year <= 2:
            score += 20
    except:
        pass

    # Location hub
    if person.get("location") in HUBS:
        score += 10

    return min(score, 100)
