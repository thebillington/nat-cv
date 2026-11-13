#!/usr/bin/env python3
"""Screenshot the built website for visual review.

Usage:
    python scripts/screenshot_site.py [--width 1280] [--mobile]
"""

import argparse
import os
import sys

from playwright.sync_api import sync_playwright

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")
SITE = os.path.join(ROOT_DIR, "output", "site", "index.html")
OUT = os.path.join(ROOT_DIR, "output", "preview")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=900)
    parser.add_argument("--mobile", action="store_true")
    parser.add_argument("--path", default="index.html")
    args = parser.parse_args()

    os.makedirs(OUT, exist_ok=True)
    url = "file://" + os.path.join(ROOT_DIR, "output", "site", args.path)
    out = os.path.join(OUT, "site-" + args.path.replace("/", "-").replace(".html", "") + (".mobile" if args.mobile else "") + ".png")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        if args.mobile:
            ctx = browser.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2)
        else:
            ctx = browser.new_context(viewport={"width": args.width, "height": args.height}, device_scale_factor=1)
        page = ctx.new_page()
        page.goto(url)
        page.screenshot(path=out, full_page=True)
        browser.close()

    print(out)


if __name__ == "__main__":
    sys.exit(main())
