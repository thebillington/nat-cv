import os
import yaml

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

MONTHS = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def format_date(date_str):
    if not date_str or date_str == "present":
        return "Present"
    parts = str(date_str).split("-")
    if len(parts) == 2:
        year, month = parts
        return f"{MONTHS[int(month)]} {year}"
    return str(date_str)


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def format_item_dates(items):
    for item in items:
        if "start" in item:
            item["start"] = format_date(item["start"])
        if "end" in item:
            item["end"] = format_date(item["end"])


def load_profile():
    return load_yaml(os.path.join(DATA_DIR, "profile.yml"))


def load_skills():
    return load_yaml(os.path.join(DATA_DIR, "skills.yml"))


def load_education():
    data = load_yaml(os.path.join(DATA_DIR, "education.yml"))
    format_item_dates(data.get("education", []))
    return data


def load_certifications():
    data = load_yaml(os.path.join(DATA_DIR, "certifications.yml"))
    for cert in data.get("certifications", []):
        if "awarded" in cert:
            cert["awarded"] = format_date(cert["awarded"])
    return data


def load_experience():
    exp_dir = os.path.join(DATA_DIR, "experience")
    roles = []
    for fname in sorted(os.listdir(exp_dir)):
        if fname.endswith(".yml"):
            data = load_yaml(os.path.join(exp_dir, fname))
            if isinstance(data, list):
                roles.extend(data)
            else:
                roles.append(data)
    roles.sort(key=lambda r: _start_key(r.get("start", "")), reverse=True)
    format_item_dates(roles)
    return roles


def _start_key(start):
    """Sort by real date, treating 'present' as the newest."""
    if start == "present":
        return "9999-99"
    return str(start)


def load_volunteering():
    return load_yaml(os.path.join(DATA_DIR, "volunteering.yml"))


def load_keywords():
    return load_yaml(os.path.join(DATA_DIR, "keywords.yml"))


def load_all():
    return {
        "profile": load_profile(),
        "skills": load_skills(),
        "education": load_education(),
        "certifications": load_certifications(),
        "experience": load_experience(),
        "volunteering": load_volunteering(),
        "keywords": load_keywords(),
    }
