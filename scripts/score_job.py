#!/usr/bin/env python3
"""Score a job description against the CV keyword bank.

Usage:
    python scripts/score_job.py jd.txt [--verbose]
"""

import argparse
import re
import sys

from data_loader import load_keywords, load_skills, load_experience


def normalise(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9£%'./&+ -]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def extract_terms(jd_text, groups):
    jd = normalise(jd_text)
    found = {}
    for group, terms in groups.items():
        for term in terms:
            pattern = r"(?<![a-z0-9])" + re.escape(term.lower()) + r"(?![a-z0-9])"
            count = len(re.findall(pattern, jd))
            if count:
                found[term] = {"count": count, "group": group}
    return found


def cv_terms():
    skills = load_skills()
    terms = set()
    for cat in skills["categories"]:
        for s in cat["skills"]:
            terms.add(normalise(s).strip())
    for line in skills.get("expertise", []):
        for part in re.split(r"[·—]", line):
            terms.add(normalise(part).strip())
    for role in load_experience():
        for a in role.get("achievements", []):
            terms.add(normalise(a["title"]).strip())
            for tag in a.get("tags", []):
                terms.add(normalise(tag.replace("-", " ")).strip())
            terms.add(normalise(a["description"]).strip())
    return " ".join(terms)


def score_jd(jd_text):
    groups = load_keywords()["groups"]
    found = extract_terms(jd_text, groups)
    cv = cv_terms()

    matched, missing = {}, {}
    for term, meta in sorted(found.items(), key=lambda x: -x[1]["count"]):
        if normalise(term) in cv:
            matched[term] = meta
        else:
            missing[term] = meta

    total = len(found)
    return {
        "total": total,
        "matched": matched,
        "missing": missing,
        "match_rate": len(matched) / total * 100 if total else 0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("job_description")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    with open(args.job_description, "r") as f:
        result = score_jd(f.read())

    print(f"Keywords found in the advert: {result['total']}")
    print(f"Already evidenced in the CV:  {len(result['matched'])}")
    print(f"Not evidenced:                {len(result['missing'])}")
    print(f"Match rate:                   {result['match_rate']:.0f}%\n")

    print("Evidenced (highest frequency first):")
    for term, meta in list(result["matched"].items())[:20]:
        print(f"  {term} ({meta['count']}x, {meta['group']})")

    if result["missing"]:
        print("\nGaps to consider addressing honestly:")
        for term, meta in list(result["missing"].items())[:25]:
            print(f"  {term} ({meta['count']}x, {meta['group']})")

    return result


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
