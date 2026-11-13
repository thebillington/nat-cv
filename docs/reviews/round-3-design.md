# Review — Round 3: Design, Accessibility & ATS

**Artifacts reviewed (final build of 20:18:09, `b24f566d4d41e58995644bd28c38b837`):**

- `output/cv-natalie-rebecchi.pdf` — 2 pp, A4, tagged, 59.6 kB
- `output/preview/cv-natalie-rebecchi-{1,2}.png` — verified pixel-identical to the PDF above
- `output/preview/site-index.png` — desktop, built 20:18:10
- `templates/cv.typ`, `docs/stylesheets/cv.css`, `docs/index.md`, `mkdocs.yml`, `output/site/`

**Verdict: not ready for sign-off.** The visual language is close and the fundamentals (single column, no tables/images, embedded Unicode fonts, real tags) are genuinely good. But there is one structural page-break defect that makes page 2 look like leftover, a scale bug that makes the website 25 % too large throughout, three broken calls-to-action, two real WCAG failures, and a print decision (full-page cream tint) that will look wrong on paper. All are fixable in an afternoon; none require re-thinking the concept.

> Build note: the PDF was rebuilt three times during this review (20:15, 20:17, 20:18). Everything below refers to the 20:18:09 build. Two earlier builds had different pagination and a different section order, so if the parent session is still iterating, re-run the page-break and structure checks before closing this off.

---

## 0. Headline findings

| # | Severity | Finding |
|---|---|---|
| 1 | **MUST-FIX** | The Crisis role is sawn in half: heading + summary close page 1, all four bullets open page 2 with no job title above them. |
| 2 | **MUST-FIX** | Website type scale is 25 % too large (body 22 px, h1 43 px) because `1.05rem` is resolved against Material's 20 px root, not 16 px. The job-title h3 collapses to body size. |
| 3 | **MUST-FIX** | Three CTAs ("View experience", "Full experience") point at `experience.md`, which 404s in the built site. |
| 4 | **MUST-FIX** | Footer email icon has no accessible name (§4). |
| 5 | **MUST-FIX** | Header focus ring is teal on navy — 1.73:1, effectively invisible (§4). |
| 6 | **MUST-FIX** | Page 1 line length is 106–114 characters at 1.26 leading — dense, not "institutional quiet". |
| 7 | **MUST-FIX** | Full-page `#FBF9F5` fill prints as a cream block with a white unprintable border; no output intent. |
| 8 | **MUST-FIX** | `H2` contains a nested `P` in the tag tree (custom heading rule) while `H1` does not — an internal inconsistency and a likely PAC/veraPDF error. |
| 9 | High | "Current portfolio" restates the profile and the Experience bullets almost verbatim ("£2.5 million" ×3, "900 properties" ×3, "New Horizons" ×2). It costs ~130 pt of page 1 and reads as padding. |
| 10 | High | Job entries are separated by ~14 pt while headings get 31 pt below the rule — so sections feel airy and jobs collide. |
| 11 | High | Website heading rules overshoot the text measure by 190 px at ≥1200 px, breaking the alignment discipline the PDF has. |
| 12 | Medium | Site still carries three template tells: "Made with Material for MkDocs", a GitHub repo icon, and a docs search icon. |

---

## 1. Typography & layout

### What works

- Single column, consistent 18 mm side margins, text box 493 pt wide, all body copy flush left, no justification, no italics, no rules except the heading rules.
- Dates are right-aligned to a common edge (x = 544.25 pt) across all five roles and all six qualifications. That is exactly right, and the date baseline sits within 0.6 pt of the job-title baseline.
- Heading hierarchy is legible: 24 pt serif navy name → 12.5 pt serif navy H2 with a 0.6 pt teal rule → 11 pt bold role → 9 pt grey sector. No colour-only hierarchy.
- Page balance: page 1 content ends at y = 773 pt, page 2 at 775 pt, footer at 809 pt. The two pages are almost exactly equally full — the *balance* is deliberate; the *split point* is not.
- Pagination footer ("Natalie Rebecchi · Page 1 of 2") is right-aligned, 8.5 pt, and correct on both pages.

### What is wrong

**1.1 Page 2 opens mid-sentence (MUST-FIX).**
Page 1 closes with the Crisis heading, its summary, and then nothing; page 2 begins:

> `• Launched and managed the Specialist Volunteering programme. …`

A reader starting on page 2 sees four bullets belonging to no visible employer. This is the single most damaging layout fault in the document. It is a `breakable: false` scoping bug: only the *role header* is non-breakable (`templates/cv.typ`, the `block(above: 7.5pt, …)` around the header), so Typst happily splits the list.

**Fix:** wrap the whole role (header + summary + achievements) in one unbreakable block, and remove the duplicate "Current portfolio" section (see 1.4) so the content still ends on two pages:

```typst
block(above: 12pt, below: 0pt, breakable: false)[
  …header…
  #if summary != "" [ #v(3pt) #text(size: 10pt)[#summary] ]
  #list(…)
]
```

**1.2 Line length and leading (MUST-FIX).**
The body is 10.5 pt Source Sans 3 on a 493 pt measure with a 13.2 pt baseline pitch (1.26). Measured characters per line:

| Line | Characters |
|---|---|
| Profile line 1 | 106 |
| Profile line 4 | 112 |
| Experience summary | 114 |
| Longest expertise line | 110 |

106–114 characters is roughly 40 % over a comfortable 65–80. Combined with 1.26 leading it reads as a dense block, not as quiet institutional typography. Two levers:

- Trim the copy. The profile is six lines and repeats the portfolio section; the Barnardo's bullets are 22 lines for one job. Removing the "Current portfolio" duplication alone buys ~130 pt.
- Raise the x-margin to 21–22 mm and the leading to ~0.75 em (13.2 → 14.5 pt). This buys readability and costs about 4 lines — which the copy trim pays for.

Do not push the type below 10 pt to compensate.

**1.3 Entry rhythm is inverted (High).**
Measured vertical gaps:

| Transition | Gap |
|---|---|
| H2 baseline → first body line | ~31 pt |
| Last role line → next job title | ~14 pt (≈ one line) |
| Job title → sector line | 12.8 pt |
| Sector line → summary | **8.1 pt** |
| Summary → first bullet | 18.9 pt |

So the space *after* a section heading (31 pt) is more than double the space *between two jobs* (14 pt), and the sector line is closer to the summary below it (8.1 pt) than any body line is to its neighbour (12.6 pt). Result: "National children's charity" visually fuses with the paragraph, and a new employer does not read as a new block.

**Fix:** heading rule → body 20 pt; role block above 22–24 pt; sector below title 1 pt, summary below sector 5 pt (not 1.5 pt).

**1.4 Page 1 repeats itself (High).**
Counts in the final PDF: "£2.5 million" ×3, "circa 900 properties" ×3, "New Horizons" ×2, "target operating model" ×2. The new "Current portfolio" block (3 bullets, ~130 pt) duplicates the Profile and the first three Barnardo's bullets almost word for word. It also duplicates what "Selected outcomes" used to do. That is why page 1 is overfull and the Crisis role had to be split.

Removing "Current portfolio" would (a) remove the repetition, (b) free enough room to keep the Crisis role whole on page 1, and (c) let page 2 open on a real heading. Expected result: page 1 ends inside the Crisis role or at its end; page 2 begins at "Volunteering and Involvement Lead" and finishes with the qualifications ~35 mm above the footer. That is a deliberate-looking last page.

**1.5 "Areas of expertise" is a wall.** 16 items in five full-width lines of 100–110 characters, with no visual grouping. The individual lines are well composed, but the block reads as a paragraph of nouns. Consider 3–4 per line with a short leading category ("Governance · …" / "Change · …"), or dropping to 12 stronger items.

**1.6 Minor typographic polish.**
- Job titles and the qualification rows still use straight apostrophes (`Barnardo's`, `children's`, `years'`). Typst only curls literal source quotes, not interpolated data. Convert `'` → `’` in the data or add a text-replace rule.
- Single-word last lines: "mapping.", "presentations.", "Games.", "year." A `text(hyphenate: true)` is off by design; at 10 pt on a 493 pt measure these are avoidable by trimming one clause.
- The "Current portfolio" bullets use a lowercase lead after the em dash ("— leading the…") while Experience bullets start with a capital ("Leading the…"). Pick one pattern.

---

## 2. Colour & print

### Measured contrast (all pass WCAG AA)

| Pair | Ratio |
|---|---|
| Ink `#1A1A1A` on paper `#FBF9F5` | 16.55:1 |
| Navy `#16324F` on paper | 12.46:1 |
| Teal `#0F5E5A` on paper | 7.21:1 |
| Slate `#3F4A56` on paper | 8.59:1 |
| Meta grey `#5B6570` on paper | 5.64:1 |
| White on teal (primary button) | 7.58:1 |
| White on navy (header) | 13.10:1 |

### Greyscale

Rendered both pages with `pdftoppm -gray`: hierarchy survives. Navy → ~30 % black, teal → ~35 %, meta grey holds at 5.6:1, the 0.6 pt heading rules remain visible (fine at 300 dpi, and at office-laser 600 dpi). Nothing is carried by colour alone. This is a pass.

### The paper tint (MUST-FIX for print)

The page is filled edge-to-edge with `#FBF9F5` (`set page(fill: paper, …)`), and the document has **no `/OutputIntents`**.

- No desktop printer can print to the edge: the tint will stop 4–5 mm short and leave a white border, so the page will look like a badly-cropped cream card rather than a considered warm white.
- On uncoated stock a 2 % tint prints as a dirty white; on laser it often bands.
- With no output intent, a commercial printer has no idea what cream you intended and will convert RGB ad hoc.
- Recruiters routinely print CVs in mono. Cream on mono is grey.

**Fix:** set the PDF page fill to white and keep `#FBF9F5` for the website (where it reads well on screen). If the tint is a non-negotiable brand decision, then add an sRGB output intent and accept that it is a screen-first document.

---

## 3. ATS / extraction

### Method

`pdftotext` (Poppler 22.12) in layout and raw modes, `pypdf` 7.1.0, `pdftotext -bbox`, `pdfimages -list`. No tables, no images, no columns, no text boxes: the file is text-only and every font is an embedded subset with a ToUnicode map. That is the ideal starting point.

### Result: good

`pdftotext -layout`, page 1:

```
Natalie         Rebecchi
Programme Manager — Transformation, Governance and Benefits
Linby, Nottinghamshire · 07793 280945 · natalie.donna.edwards@gmail.com

Profile
…
Experience
Programme Manager, Barnardo's                       October 2025 – Present
National children's charity
Leading the delivery of complex projects…
 • Leading the national New Horizons transformation programme. …
```

`pypdf` produces the same in clean reading order: name on one line, employer + title + dates on one line, sector line, summary, bullets in order. Dates are all consistently `Month YYYY – Month YYYY` (with `Present` for the current role), and the "(PMQ)" acronym is spelled out in the qualification row. Nothing is nested or reversed. **No parser-scrambling of name, employer, title, dates or bullets.**

### Risks

| Risk | Detail | Severity |
|---|---|---|
| Name drawn as two runs | `pdftotext -raw` returns `Natalie` / `Rebecchi` on separate lines (5.3 pt gap between runs). Layout and pypdf parsers merge it; content-order parsers may not. | Low |
| Job titles are not headings | In the tag tree each role is a `Span`, not `H3`, so structural parsers see only five `H2`s. Extraction is unaffected, but see §4. | Low (ATS) / High (a11y) |
| Footer in the text layer | "Natalie Rebecchi · Page 1 of 2" is tagged as an artifact but still extracts at the end of each page. Harmless; some naive parsers append it to the last bullet. | Low |
| "Current portfolio" bullets | Bold lead-in + em dash ("National transformation portfolio — leading…") extracts cleanly, but gives the parser three "programme" entries before Experience. Could be read as a separate employer block. Removing the section removes the ambiguity. | Low |

Verdict: **ATS-safe as it stands.** The layout defects in §1 are the ones that hurt a human reader, not a parser.

---

## 4. Accessibility

### PDF

Verified present and correct:

- `/MarkInfo /Marked true`, `/Lang en-GB`, `dc:title` + `/Title`, `DisplayDocTitle`, `/Tabs /S` on both pages, `/StructParents`, `/ParentTree`, `/RoleMap`.
- `/H1` for the name, `/H2` for each section, `/L` → `/LI` → `/Lbl` + `/LBody` for every bullet list.
- Both link annotations have `/Contents` ("Telephone 07793280945", "Email …"), `/Border 0` and a `/StructParent`.
- Footer and heading rules are correctly marked as artifacts.
- Bookmarks: one parent ("Natalie Rebecchi") with six section children.
- XMP claims `pdfuaid:part 1`, which is ambitious given the points below.

Defects:

**4.1 `H2` wraps a `P` (MUST-FIX, likely UA failure).**
The structure is internally inconsistent:

```
/H1
  MCID 0
/H2
  /P
    MCID 8
```

`H1` contains inline content directly; every `H2` contains a `P`. Cause: the custom level-2 show rule wraps the heading body in a `block(…)[…]` so it can append the teal line (`templates/cv.typ`, `show heading.where(level: 2)`). Tagged headings should contain inline content, not block-level children, and PAC 2024/veraPDF is likely to flag "P not permitted inside H2". It also means the rule is nested inside the heading element rather than being an artifact sibling.

**Fix:** emit the heading text and the rule as siblings, not as a block wrapping the heading:

```typst
show heading.where(level: 2): it => {
  block(above: 11pt, below: 0pt)[#text(font: serif, size: 12.5pt, weight: 600, fill: navy)[#it.body]]
  v(2.5pt)
  pdf.artifact(line(length: 100%, stroke: 0.6pt + teal))
  v(4.5pt)
}
```

Then re-check with PAC 2024 (not installed here — see "Limitations").

**4.2 Job titles are not headings (High).**
Roles are `Span`s, so a screen-reader user navigating by heading hears only Profile / Current portfolio / Areas of expertise / Experience / Board and voluntary roles / Qualifications. They cannot jump between jobs. Mark each role line as `H3` (and the `<company>` page grouping on the site already does this correctly — mirror it in the PDF).

**4.3 Hero title and contact line are bare `Span`s at document level (Medium).**
`/Span` children directly under `/Document` (job title, then Span/Link/Span/Link for the contact strip) are not block-level containers. Wrap each in `P`.

**4.4 Poppler reports a syntax error on every run (Medium).**
`pdfinfo` and `pdftotext` both print:

```
Syntax Error: Suspects object is wrong type (boolean)
```

Traced to `/MarkInfo /Suspects false`. Removing that key makes the warning disappear (verified with a patched copy). It is a Typst export quirk, not corruption, but automated CV pipelines that treat stderr as failure will reject the file, and it burns credibility in any "does the PDF validate?" check. Post-process it out (it is the default value) or raise upstream.

**4.5 Smaller items (NICE).**
- `/L` declares `/ListNumbering /Circle` while the glyph is a disc (`•`) — screen readers may say "circle". Should be `/Disc`.
- No `/OutputIntents` (see §2).
- No `/H3` and no job-level bookmarks.
- Links (phone, email) are visually identical to body text — no underline or colour. Fine for print, poor affordance on screen.

### Website

- h1 → h2 → h3 order is correct on `/` and on `/experience/`; skip link present; one `h1` per page.
- Body/link contrast passes comfortably (table above). Button text 7.58:1; outline button 7.21:1.
- **4.6 Footer email icon has no accessible name (MUST-FIX, WCAG 2.4.4 / 4.1.2).** The link renders as `<a href="mailto:…" title="" class="md-social__link">` with an SVG and no text. `aria-label`, `title` and text are all empty — verified in the browser. Add `name:` to the `social` entry in `mkdocs.yml` (Material turns it into `title`/aria) or inject an `aria-label`.
- **4.7 Focus indication in the header fails 1.4.11 (MUST-FIX).** `a:focus-visible { outline: 2px solid var(--cv-teal) }` gives teal on navy = **1.73:1**. On the header/nav-overlay, the ring is invisible. Add a dark-surface variant:
  ```css
  .md-header a:focus-visible, .md-header button:focus-visible,
  .md-footer a:focus-visible { outline-color: #FBF9F5; }
  ```
  The ring on the teal primary button is fine (it sits on paper with `outline-offset: 2px`).
- `<html lang="en">` while the document is `en-GB` (and the PDF says `en-GB`). Not a 3.1.1 failure, but setting `theme.language: en-GB` would be consistent.
- The /experience/ page is semantically the strongest part of the site (h1 Experience → h2 employer → h3 role). The homepage's "Current role" is a thinner mirror of it.

---

## 5. Website

### Strengths

- The content column is well behaved: 68 ch measure (748 px), left-aligned, 36 px line-height, generous margins; no italics; consistent navy/teal pairing with the PDF.
- The two-button hero (filled "Download CV (PDF)" + outline "View experience") is clear, and the download serves a byte-identical copy of the current PDF (verified md5).
- Mobile reflows without horizontal scroll (scrollWidth = clientWidth = 390 px); buttons are ~56 px tall, well over the 44 px target.
- The /experience/ page (employer → role headings, dates, bullets) is a good long-form counterpart to page 2 of the PDF.

### Problems

**5.1 Everything is 25 % too big (MUST-FIX).**
Material sets `html { font-size: 20px }`. The stylesheet then uses rem as if the root were 16 px:

| Element | Computed | Intended |
|---|---|---|
| Body | **22 px** / 36.3 px | ~17 px |
| h1 | **43 px** | ~32 px |
| h2 | **27 px** | ~22 px |
| h3 (job title) | **22 px** — same as body | ~19 px |

Consequences: a one-screen CV becomes a four-screen scroll; h1 is billboard-sized; and because h3 equals body size, the job title is distinguished only by serif + weight, which weakens the most important line on the page.

**Fix:** set `.md-typeset { font-size: 0.85rem }` (17 px), `h1: 1.7rem`, `h2: 1.2rem`, `h3: 0.95rem`; keep the 68 ch cap.

**5.2 Three CTAs are dead (MUST-FIX).**
`docs/index.md` lines 8 and 45 use raw HTML links to `experience.md`. MkDocs does not rewrite `.md` links inside raw HTML, so the built page contains `href="experience.md"` — confirmed **404**. This hits "View experience" (the secondary hero button) and "Full experience" (the primary next step at the bottom of the home page). Use `experience/` or `{{ 'experience/' | url }}`.

**5.3 Heading rules overshoot the text (High).**
At 1280 px: `.md-content__inner` is 938 px but `p, li { max-width: 68ch }` caps text at 748 px. The h2 `border-bottom` spans the full 938 px, so every rule runs ~190 px past the last character (measured: rule right edge 1234, text right edge 1044). At the 1024 px screenshot width the two nearly coincide, which is why it has gone unnoticed. Move the 68 ch cap to a wrapper (or `.md-typeset`) rather than to each `p`, so rules and text share an edge.

**5.4 The "Current portfolio" block reads as a quotation (High).**
`.outcomes li { border-left: 2px solid teal; padding-left: .85rem }` renders three tall teal bars — the universal visual grammar for a blockquote — around bold-led text. In the PDF the same content is a bullet list. Either use proper bullets (matching the PDF) or drop the section (see 1.4). Note the class is still called `.outcomes` after the copy was renamed — stale naming that will confuse the next person.

**5.5 Template tells (MUST-FIX for the "not a template" bar).**
A senior programme leader's site should not announce its generator. Currently: "Made with Material for MkDocs" in the footer, a GitHub repository icon top right and in the drawer, and a search icon that searches five pages. The left nav also exposes a docs-style deep TOC, including "Programme Manager, Barnardo's" broken over two lines with no hanging indent.

Minimum: remove the generator and repo link, hide search, and flatten the side nav to About / Experience / Skills / Qualifications / Volunteer work / Download. The hero + measure + colours are strong enough to carry the page without the furniture.

**5.6 Consistency with the PDF (Medium).**
- Website role meta says "October 2025 **to** Present"; the PDF uses an en dash. Use `– Present`.
- The website omits the phone number (defensible for privacy — just make it a decision, not an accident).
- JSON-LD `jobTitle` is still "Programme & Project Manager" while the PDF headline is "Programme Manager — Transformation, Governance and Benefits". `extra.person.title` is stale.
- The site has "Current portfolio" but the PDF section is the same — good — yet the site's "Areas of expertise" wraps mid-phrase and one line begins with a dangling "· Coaching and line management". Never let a separator start a line: render the items as `<span>`s with CSS separators, or hard-break only between groups.

**5.7 Deliverable missing.** `output/preview/site-index.mobile.png` does not exist (only `site-index.png`). I captured my own 390 × 844 render to check mobile; the build should emit that screenshot so this review is reproducible.

---

## 6. Concrete defects

### MUST-FIX

| ID | File | Defect | Fix |
|---|---|---|---|
| M1 | `templates/cv.typ` | Crisis role split: header+summary on p1, all four bullets on p2 with no context. Page 2 looks like leftover. | `breakable: false` around the whole role block; trim content so it still fits 2 pp. |
| M2 | `docs/index.md`, `templates/cv.typ` | Body measure 106–114 ch at 1.26 leading. | 21–22 mm side margins, leading ~0.75 em, and cut ~10 lines (start with M3). |
| M3 | `templates/cv.typ`, `output/data.json` | "Current portfolio" duplicates profile + Experience; "£2.5 million" ×3, "900 properties" ×3, "New Horizons" ×2. | Delete the section; it is also the cheapest way to fix M1. |
| M4 | `templates/cv.typ` | Job-to-job gap ~14 pt vs 31 pt under headings; sector line is 8.1 pt above the summary. | Role block `above: 22pt`; sector→summary 5 pt. |
| M5 | `templates/cv.typ` | `H2 > P` nesting; `H1` has inline content. Likely PDF/UA error. | Move the teal rule out of the heading's block (snippet in 4.1). |
| M6 | `templates/cv.typ` | Full-page cream fill with no output intent; prints with a white border and as dirty grey/white. | `fill: white` for the PDF; keep tint on web. |
| M7 | `docs/stylesheets/cv.css` | rem sizes resolved against Material's 20 px root: body 22 px, h1 43 px, h3 = body. | `0.85rem` body, `1.7/1.2/0.95rem` for h1/h2/h3. |
| M8 | `docs/index.md` (×2) | `href="experience.md"` → 404 on "View experience" and "Full experience". | `experience/` or `{{ 'experience/' \| url }}`. |
| M9 | `mkdocs.yml` / template | Footer email link has no accessible name. | `name: Email` on the social entry, or `aria-label`. |
| M10 | `docs/stylesheets/cv.css` | Header focus ring 1.73:1 (teal on navy) — invisible. | Light outline colour on `.md-header`/`.md-footer` focus. |
| M11 | `docs/stylesheets/cv.css` | Heading rules 190 px wider than body text at ≥1200 px. | Cap the measure on a wrapper, not on each `p`/`li`. |
| M12 | `mkdocs.yml`, footer | "Made with Material for MkDocs", GitHub repo icon, search icon — generator furniture. | Remove/hide all three; flatten nav. |
| M13 | `output/preview/` | `site-index.mobile.png` missing. | Emit in the screenshot step. |

### NICE-TO-HAVE

| ID | File | Defect | Fix |
|---|---|---|---|
| N1 | `templates/cv.typ` | Role titles are `Span`, not `H3`; no job bookmark. | Tag role lines as `H3`; add bookmarks. |
| N2 | `templates/cv.typ` | Hero title + contact strip are bare `Span`s under `/Document`. | Wrap each in `P`. |
| N3 | `output/data.json` | Straight apostrophes throughout (`Barnardo's`, `children's`, `years'`). | Replace with `’`. |
| N4 | Typst export | `/MarkInfo /Suspects false` makes Poppler print a syntax error. | Strip in post-process (default value) or fix upstream. |
| N5 | `templates/cv.typ` | `/ListNumbering /Circle` for disc markers. | `/Disc`. |
| N6 | `output/cv-*.pdf` | No `/OutputIntents`; no sRGB ICC. | Add if any colour-managed print is expected. |
| N7 | `mkdocs.yml` | `extra.person.title` and JSON-LD `jobTitle` still "Programme & Project Manager". | Point at the current headline. |
| N8 | `mkdocs.yml` | `theme.language: en` → `<html lang="en">`; PDF is `en-GB`. | `en-GB`. |
| N9 | `docs/stylesheets/cv.css` | `.outcomes li` teal bars read as blockquotes. | Plain bullets or no section. |
| N10 | `output/site/index.html` | "Areas of expertise" wraps mid-phrase; a line starts with "· ". | Render separators via CSS, not as leading text. |
| N11 | `docs/index.md` | "October 2025 **to** Present". | "– Present". |
| N12 | `templates/cv.typ` | "Areas of expertise": 16 items in 5 flat 100–110 ch lines. | Group under 3–4 short category leads. |
| N13 | `templates/cv.typ` | Order: Board and voluntary roles before Qualifications; PMQ lands at the very bottom of p2. | Move Qualifications (or at least the PMQ) above voluntary roles. |
| N14 | `templates/cv.typ` | Phone/email links look like body text. | Underline or a subtle teal, or accept for print. |
| N15 | `templates/cv.typ` | Single-word last lines ("mapping.", "presentations.", "Games.", "year."). | Trim one clause in those bullets. |
| N16 | `docs/index.md` | Website omits the phone number present in the PDF. | Decide and record the reason. |

---

## 7. What is genuinely fine (do not change)

- **One column, no tables, no images, no sidebars.** `pdfimages -list` is empty; both fonts are embedded subsets with ToUnicode. This is the right foundation and it is why extraction works.
- **Extraction order.** Name → title → contact → sections → employer → title/date → sector → summary → bullets, in `pdftotext` and `pypdf`, page 1 and page 2.
- **Date formatting and alignment.** En dashes, `Present`, right-aligned to a single edge, consistent across roles and education.
- **Colour pairings and contrast.** Every text pair is between 5.6:1 and 16.6:1; hierarchy is not carried by colour; greyscale survives.
- **Page geometry.** A4, 18 mm side margins, correct pagination, correct "Page n of 2".
- **The site's core layout.** 68 ch measure, left-aligned, no italics, honest British spelling, proper h1/h2/h3, skip link, generous mobile tap targets, working PDF download (identical bytes).
- **British English.** No `-ize`/`-yze`, no "center", no "program" outside "programme"; "organisation", "optimisation" and "prioritise" all correct.
- **Terminology.** "programme" used consistently for programmes; "project" for projects. The PMQ is spelled out in the qualification row and abbreviated in the profile.

---

## 8. Limitations

- No PDF/UA validator was available in this environment (`veraPDF`, `PAC`, `pdfcpu` and `jhove` are all absent), so the UA findings in §4 are structural inspections, not a conformance verdict. The `H2 > P` nesting (M5) is the one I would expect a validator to fail; run PAC 2024 before publishing the PDF/UA-1 claim on `/accessibility/`.
- `qpdf` is not installed; `pdfinfo`/`pdftotext` parsing plus `pikepdf` were used for integrity checks.
- The PDF changed three times during the review; the page-break and structure findings were re-verified against `b24f566d…` at 20:18:09, but should be re-run after any further rebuild.
- Screenshots were regenerated from the current build; the supplied desktop screenshot matches, the mobile one was missing and was re-captured at 390 × 844.
