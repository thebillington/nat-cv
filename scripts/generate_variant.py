#!/usr/bin/env python3
"""Generate a tailored PDF for a job description.

Selects the most relevant achievements by tag overlap. It never rewrites
Natalie's sentences; it only chooses which evidence leads.

Usage:
    python scripts/generate_variant.py -j jd.txt -o output/cv-tailored.pdf
"""

import argparse
import json
import os
import subprocess
import sys

from data_loader import load_all
from score_job import extract_terms, load_keywords

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")
TEMPLATES_DIR = os.path.join(ROOT_DIR, "templates")
FONTS_DIR = os.path.join(ROOT_DIR, "assets", "fonts")


def relevance(achievement, jd_terms):
    tags = {t.replace("-", " ").lower() for t in achievement.get("tags", [])}
    title = achievement["title"].lower()
    score = len(tags & set(jd_terms))
    score += sum(1 for term in jd_terms if term in title)
    if achievement.get("impact") == "high":
        score += 1
    return score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--job-description", "-j", required=True)
    parser.add_argument("--output", "-o", default=os.path.join(OUTPUT_DIR, "cv-tailored.pdf"))
    parser.add_argument("--max-per-role", type=int, default=6)
    args = parser.parse_args()

    with open(args.job_description) as f:
        jd_text = f.read()

    groups = load_keywords()["groups"]
    jd_terms = extract_terms(jd_text, groups)

    data = load_all()
    for role in data["experience"]:
        ranked = sorted(
            role.get("achievements", []),
            key=lambda a: relevance(a, jd_terms),
            reverse=True,
        )
        role["achievements"] = ranked[: args.max_per_role]

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data_path = os.path.join(OUTPUT_DIR, "data-tailored.json")
    with open(data_path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    out_dir = os.path.dirname(os.path.abspath(args.output))
    template_rel = os.path.relpath(os.path.join(TEMPLATES_DIR, "cv.typ"), out_dir)
    data_rel = os.path.relpath(data_path, out_dir)

    typ_path = args.output.replace(".pdf", ".typ")
    with open(typ_path, "w") as f:
        f.write(
            f'#import "{template_rel}": cv\n'
            f'#let data = json("{data_rel}")\n'
            "#cv(data)\n"
        )

    typst = os.path.expanduser("~/.local/bin/typst")
    if not os.path.exists(typst):
        typst = "typst"

    result = subprocess.run(
        [
            typst, "compile",
            "--root", ROOT_DIR,
            "--font-path", FONTS_DIR,
            "--pdf-standard", "ua-1",
            typ_path, args.output,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        return 1

    print(f"Generated: {args.output}")
    print(f"Advert keywords: {len(jd_terms)}")
    for role in data["experience"]:
        print(f"  {role['company']}: {len(role['achievements'])} achievements selected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
