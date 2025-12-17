def infer_email(name, company):
    if not company:
        return None

    domain = company.lower()
    domain = domain.split()[-1].replace(",", "")
    domain = domain.replace("university", "edu")

    first, last = name.lower().split(" ")[0], name.lower().split(" ")[-1]
    return f"{first}.{last}@{domain}.com"
