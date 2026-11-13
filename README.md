# nat-cv

Natalie Rebecchi's CV, built from structured data. One set of YAML files
generates both the A4 PDF and the companion website, so the two cannot drift
apart.

The content and voice are Natalie's: the pipeline trims and structures her own
wording rather than rewriting it. See `docs/design/voice.md`.

## Quick start

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# build PDF + website + checks
.venv/bin/python scripts/build.py

# PDF only
.venv/bin/python scripts/build.py --pdf

# website only
.venv/bin/python scripts/build.py --website

# visual previews
.venv/bin/python scripts/preview.py output/cv-natalie-rebecchi.pdf
.venv/bin/python scripts/screenshot_site.py
```

Typst is required. `scripts/build.py` uses `~/.local/bin/typst` if present,
otherwise `typst` on `PATH`.

Output: `output/cv-natalie-rebecchi.pdf` and `output/site/`.

## Architecture

```
data/                YAML source of truth
  profile.yml        name, contact, profile, selected outcomes
  experience/*.yml   one file per role, with achievements
  skills.yml         areas of expertise + skill groups
  certifications.yml APM PMQ
  education.yml      degrees and qualifications
  volunteering.yml   trustee and voluntary roles
  keywords.yml       keyword bank + banned phrases for checks
templates/cv.typ     PDF template (Typst)
scripts/             build, checks, previews, tailoring
docs/                website source (MkDocs Material)
  research/          market and design research memos
  design/            design decisions and voice guide
  reviews/           review rounds and outcomes
templates/           PDF template
assets/fonts/        Source Sans 3 / Source Serif 4 (SIL OFL)
```

## Quality gates

`scripts/build.py` runs `scripts/check_pdf.py`, which fails the build on:

- wrong page count (must be 2)
- missing required sections
- missing contact details
- banned filler phrases (`data/keywords.yml`)
- broken text extraction

It also reports keyword coverage against the market keyword bank.

## Tailoring and scoring

```bash
.venv/bin/python scripts/score_job.py job-description.txt
.venv/bin/python scripts/generate_variant.py -j job-description.txt -o output/tailored.pdf
```

## Deployment

GitHub Actions builds the PDF and site on every push to `main` and deploys to
GitHub Pages at https://thebillington.github.io/nat-cv.

## Accessibility

The PDF is exported as PDF/UA-1 with tagged headings and reading order. The
website is the reflowable alternative, with WCAG AA contrast and an
accessibility statement. See `docs/accessibility.md`.

## Licence

CV content © Natalie Rebecchi. Source Sans 3 and Source Serif 4 are licensed
under the SIL Open Font License 1.1 (`assets/fonts/OFL.txt`).
