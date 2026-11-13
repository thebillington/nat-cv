#!/usr/bin/env python3
"""Check the generated PDF: structure, text extraction, and keyword coverage.

Fails (non-zero exit) on anything that would hurt an application:
wrong page count, missing sections, banned filler phrases, missing contact
details, or extraction problems.

Usage:
    python scripts/check_pdf.py output/cv-natalie-rebecchi.pdf
"""

import argparse
import os
import re
import subprocess
import sys

from data_loader import load_keywords


def pdf_text(path):
    result = subprocess.run(
        ["pdftotext", "-layout", path, "-"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    return result.stdout


def pdf_pages(path):
    result = subprocess.run(
        ["pdfinfo", path], capture_output=True, text=True
    )
    match = re.search(r"^Pages:\s+(\d+)", result.stdout, re.MULTILINE)
    return int(match.group(1)) if match else 0


def flatten_keywords(groups):
    terms = []
    for group in groups.values():
        terms.extend(group)
    return terms


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf")
    parser.add_argument("--expect-pages", type=int, default=2)
    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"FAIL: {args.pdf} does not exist")
        return 1

    text = pdf_text(args.pdf)
    lower = text.lower()
    pages = pdf_pages(args.pdf)

    failures = []
    warnings = []

    # Structure
    if pages != args.expect_pages:
        failures.append(f"page count is {pages}, expected {args.expect_pages}")

    required_sections = [
        "Profile",
        "Current portfolio",
        "Areas of expertise",
        "Experience",
        "Qualifications",
        "Board and voluntary roles",
    ]
    for section in required_sections:
        if section.lower() not in lower:
            failures.append(f"missing section: {section}")

    # Contact details, extracted from the body
    for needle in ["natalie.donna.edwards@gmail.com", "07793 280945", "Nottingham"]:
        if needle.lower() not in lower:
            failures.append(f"missing contact detail: {needle}")

    # Banned language
    keywords = load_keywords()
    for phrase in keywords.get("avoid", []):
        if phrase.lower() in lower:
            failures.append(f"banned phrase present: '{phrase}'")

    # Extraction sanity
    if "\ufffd" in text:
        failures.append("replacement characters in extracted text (font/encoding problem)")
    if re.search(r"[A-Za-z]-\n[A-Za-z]", text):
        warnings.append("hyphenated line break may split a keyword during extraction")

    # Keyword coverage. Match against whitespace-normalised text so a phrase that
    # wraps across a line still counts (ATS tokenisers do the same).
    flat = re.sub(r"\s+", " ", lower)
    terms = flatten_keywords(keywords["groups"])
    covered = [t for t in terms if t.lower() in flat]
    missing = [t for t in terms if t.lower() not in flat]
    coverage = len(covered) / len(terms) * 100
    core = [
        "programme governance",
        "benefits management",
        "benefits management",
        "RAID",
        "steering group",
        "risk management",
        "stakeholder",
        "target operating model",
        "change impact assessment",
        "equality impact assessment",
        "business analysis",
        "budget",
        "APM",
        "PMQ",
    ]
    core_missing = [t for t in core if t.lower() not in flat]

    print(f"PDF: {args.pdf}")
    print(f"Pages: {pages} (expected {args.expect_pages})")
    print(f"Words: {len(text.split())}")
    print(f"Keyword coverage: {len(covered)}/{len(terms)} ({coverage:.0f}%)")
    if core_missing:
        print(f"Core keywords missing: {', '.join(core_missing)}")
    print(f"Banned phrases: none" if not any("banned" in f for f in failures) else "")

    for w in warnings:
        print(f"WARN: {w}")
    for f in failures:
        print(f"FAIL: {f}")

    if failures:
        return 1

    print("PASS: structure, contact details, banned phrases and page count OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
