# Development pipeline

This repo is built as a small product, not a one-off document. The pipeline is:

```
source documents
      │
      ├── extraction (structured YAML, facts only)
      │
      ├── research rounds (market + design, forum-led)
      │
      ├── design direction + data model
      │
      ├── build (Typst PDF + MkDocs site from one source)
      │
      ├── automated gates (page count, sections, banned phrases, extraction)
      │
      └── independent review rounds (voice, market, design)
                │
                └── fixes → rebuild → re-review
```

## Why this shape

A CV is a persuasive document with a hard constraint (two pages) and two very
different readers (a human in six seconds, a parser in milliseconds). Separating
the content from the layout means the same facts can be rendered twice without
drift, and it makes review possible: reviewers can critique the text without
arguing about the template.

## Source of truth

`data/` holds facts and Natalie's own wording. Nothing in `templates/` invents
content. Any change to a claim happens in `data/`, is reviewed, and then flows
to both outputs.

## Automated gates

`scripts/check_pdf.py` runs on every build:

- exactly two pages
- all required sections present
- contact details extractable
- no banned filler phrases (`data/keywords.yml`)
- no broken glyphs in extracted text
- keyword coverage reported against the market bank

The build fails rather than shipping a broken PDF. This is deliberate: a CV with
three pages or a missing email is worse than no build.

## Review rounds

Reviews are independent and adversarial. Each writes a memo to `docs/reviews/`,
and fixes are applied to `data/` or `templates/` before a rebuild.

1. **Voice and fidelity** — a line-by-line comparison with the source CV,
   checking that the trimmed text still sounds like Natalie and that no claim
   has been overstated.
2. **Market and seniority** — a hiring-panel read against the keyword and
   salary research: does it read senior, is the scope visible, what would be
   asked at interview?
3. **Design and accessibility** — typography, layout, print, ATS extraction,
   tagged-PDF structure and website quality.

Reviewers are given the source document as well as the output, so they can catch
invention as well as omission.

## Tailoring

`scripts/score_job.py` scores a job description against the keyword bank and
`scripts/generate_variant.py` selects the most relevant achievements. Neither
rewrites Natalie's sentences; they only choose which evidence leads.

## Adding a role or achievement

1. Add or edit a YAML file in `data/experience/`.
2. Use Natalie's wording; do not paraphrase into corporate language.
3. Tag it with the terms in `data/keywords.yml`.
4. Build. If it breaks the two-page limit, trim an older role rather than
   shrinking the type.
5. Re-run the review rounds if the change is substantive.
