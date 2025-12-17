import re

CITIES = {
    "boston": "Boston, USA",
    "cambridge": "Cambridge, USA",
    "san francisco": "San Francisco, USA",
    "bay area": "Bay Area, USA",
    "basel": "Basel, Switzerland",
    "london": "London, UK",
    "oxford": "Oxford, UK",
    "cambridge uk": "Cambridge, UK",
    "berlin": "Berlin, Germany",
    "munich": "Munich, Germany",
    "paris": "Paris, France",
    "tokyo": "Tokyo, Japan",
    "beijing": "Beijing, China",
    "shanghai": "Shanghai, China",
    "bangalore": "Bangalore, India",
    "bengaluru": "Bangalore, India",
    "hyderabad": "Hyderabad, India",
    "pune": "Pune, India"
}

COUNTRIES = {
    "usa": "USA",
    "united states": "USA",
    "u.s.": "USA",
    "uk": "UK",
    "united kingdom": "UK",
    "england": "UK",
    "germany": "Germany",
    "switzerland": "Switzerland",
    "france": "France",
    "india": "India",
    "china": "China",
    "japan": "Japan",
    "canada": "Canada",
    "australia": "Australia"
}


def extract_location(text):
    """
    Extracts best-effort location from affiliation or company text.
    Priority: City → Country → Other → No Info
    """
    if not text or not isinstance(text, str):
        return "No Info"

    text_lower = text.lower()

    # 1️⃣ City-level match
    for key, value in CITIES.items():
        if re.search(rf"\b{re.escape(key)}\b", text_lower):
            return value

    # 2️⃣ Country-level match
    for key, value in COUNTRIES.items():
        if re.search(rf"\b{re.escape(key)}\b", text_lower):
            return value

    # 3️⃣ Something exists but not identifiable
    return "not Identified"
