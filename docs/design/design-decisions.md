# Design decisions

See `docs/research/design-research.md` for the evidence and the alternatives
considered. This file records what was built and why.

## The one decision that matters

The CV is set as a **single-column, serif-headed document** rather than a
designed "personal brand". At senior level the CV is read as a work sample: if
it looks like a board paper, that is evidence; if it looks like a portfolio
piece, that is a distraction. Every visual choice follows from that.

## Type

- **Source Serif 4** (SIL OFL) for the name and section headings. It gives
  authority at display size without the wedding-invitation register of a
  high-contrast serif.
- **Source Sans 3** (SIL OFL) for everything else. Generous counters,
  unambiguous `l/I/1`, and a public-service register rather than a tech-product
  one.
- Both are statically instanced at weights 400/600/700 and embedded as subsets,
  so the PDF renders identically everywhere and does not depend on system fonts.
- No italics anywhere: italics slow dyslexic readers and are unnecessary here.
- Hyphenation is off, so keywords never split across lines for an ATS.

## Colour

| Role | Hex | Contrast on paper |
|---|---|---|
| Body | `#1A1A1A` | 16.5:1 |
| Navy (name, headings) | `#16324F` | 12.5:1 |
| Teal (role line, rules, bullets) | `#0F5E5A` | 7.2:1 |
| Slate (dates, employers) | `#3F4A56` | 8.6:1 |
| Secondary meta | `#5B6570` | 5.6:1 |
| Paper | `#FBF9F5` | — |

Colour is decorative only; nothing is encoded by colour alone. Navy and teal
separate cleanly in greyscale. The palette deliberately avoids Barnardo's house
colours — a CV in an employer's brand reads as over-eager and clashes with
recruiter reformatting.

## Layout

- A4, 18mm sides, 16mm top, 15mm bottom.
- The name is the only level-1 heading, so the tagged PDF has a sensible
  bookmark tree (name, then sections).
- Job headers are one paragraph with a fill, not a grid or table: a grid splits
  the title, employer and dates into separate content streams and parsers
  scramble them.
- Dates are right-aligned on the role line so the chronology can be scanned
  vertically.
- The footer is an artefact, so screen readers do not announce it as content.
- Bullets are capped at two lines. This is the compromise that keeps the
  document at 10.5pt without producing an intimidating wall of text.

## What was deliberately left out

- Photo, date of birth, nationality, marital status, full address.
- Skill bars, dot ratings, icons, infographics, sidebars, timelines.
- Hobbies and "references available on request".
- A separate tools list: the relevant systems appear inside the work that used
  them.
- Any claim not present in Natalie's source CV.

## Website

The site reuses the same YAML. It is not a separate document with a separate
truth. It carries the same sections plus full experience and an accessibility
statement, with a print stylesheet so the web page and the PDF look like the
same document.
