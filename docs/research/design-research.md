# Design research and decisions

## Direction chosen: "Institutional Quiet"

A document that looks like it was produced by someone who stewards public money:
a serif-headed, single-column A4 report in navy and teal, not a personal brand.

This was chosen over two alternatives:

- **Public Service Plain** — Public Sans only, one colour, pure white. Maximum
  ATS safety and a trivial Word twin, but visually indistinguishable from a
  well-set default.
- **A more expressive/portfolio direction** — rejected. At senior level,
  over-design reads as compensation; senior recruiters consistently say the CV
  is a work sample, and the first work sample should look like a board paper.

## Evidence base

- UK charity recruiters expect **two pages**, reverse chronological, with a
  profile, and read for relevance rather than novelty (CharityJob, Harris Hill,
  TPP).
- APM recommends a **career highlights** block before detailed history for
  experienced candidates, with budget/team/scale figures.
- Eye-tracking research: the first scan goes to name, current title, employer
  and dates. So those must be unmistakable.
- Single column, no tables/text boxes: column layouts are the most common ATS
  parse failure and the most common accessibility failure.
- Senior CVs are damaged by skill bars, infographics, photos, duty lists, and
  "responsible for".
- Accessibility is a sector-credibility issue: charity and public-sector
  employers notice. GOV.UK and the British Dyslexia Association guidance both
  favour left-aligned text, no italics, no all-caps runs, high contrast and
  short line lengths.

## Specification

| Element | Decision |
|---|---|
| Page | A4, single column; 18mm sides, 16mm top, 15mm bottom |
| Name | Source Serif 4 SemiBold, 24pt, navy |
| Role line | Source Sans 3 SemiBold, 10.5pt, teal |
| Contact | Source Sans 3 Regular, 9.5pt, slate, in the body (not a header) |
| Section heading | Source Serif 4 SemiBold, 12.5pt, navy, title case, 0.6pt teal rule |
| Body | Source Sans 3 Regular, 10.5pt, 1.2 leading, left-aligned |
| Bullets | 10pt, teal bullet glyph, hanging indent, max two lines each |
| Dates | Source Sans 3 Regular, 9.5pt, slate, right-aligned on the role line |
| Colours | Body `#1A1A1A`; navy `#16324F`; teal `#0F5E5A`; slate `#3F4A56`; meta `#5B6570`; paper `#FBF9F5` |
| PDF | Tagged PDF/UA-1, `lang` en-GB, hyphenation off, document title and author set |
| Fonts | Source Sans 3 + Source Serif 4, SIL OFL, embedded subsets; WOFF2 on the web |

Contrast against the paper tint: body 16.5:1, navy 12.5:1, teal 7.2:1, slate
8.6:1, secondary meta 5.6:1. All exceed WCAG AA; most exceed AAA. Navy and teal
remain distinguishable in greyscale.

## Structure

1. Name, role, contact
2. Profile — three to four lines, in Natalie's voice
3. Current portfolio — three programme scope statements that survive a six-second scan
4. Areas of expertise — three dense lines, not a matrix or skill bars
5. Experience — reverse chronological; Barnardo's leads, earlier roles compress
6. Qualifications — APM PMQ first, then degrees and further study
7. Board and voluntary roles — trustee work carries real weight in the sector

No photo, date of birth, nationality, full address, hobbies, or references
section.

## Known trade-off

At 10.5pt across a 174mm measure, line length is roughly 85 characters, above
the dyslexia-friendly 60–70 ideal. Honouring that in print would cost about 15%
of the two-page capacity. The resolution: keep every bullet under two lines, and
make the website the fully reflowable, 68-character-measure version. This
trade-off is recorded rather than hidden.

## Website

The site is the accessible alternative, not a portfolio flourish:

- same content and palette as the PDF, self-hosted WOFF2 fonts
- 68ch measure, 1.65 line height, WCAG AA/AAA contrast
- semantic headings, visible focus states, no animation
- print stylesheet that reproduces a plain A4 layout
- accessibility statement and a contact route for alternative formats

## Sources

- CharityJob, CV layout: https://www.charityjob.co.uk/careeradvice/how-to-create-the-perfect-cv-layout/
- Harris Hill, charity CV: https://www.harrissill.co.uk/blog/2023/03/how-to-write-your-charity-sector-cv-part-1
- APM, CV tips: https://www.apm.org.uk/jobs-and-careers/tips-for-writing-a-winning-cv/
- APM Competence Framework: https://www.apm.org.uk/media/1cflfk3t/apm-competence-framework-3rd-editionfinalrevised.pdf
- National Careers Service, CV sections: https://nationalcareers.service.gov.uk/careers-advice/cv-sections
- GOV.UK, publishing accessible documents: https://www.gov.uk/guidance/publishing-accessible-documents
- BDA style guide: https://cdn.bdadyslexia.org.uk/uploads/documents/Advice/style-guide/BDA-Style-Guide-2023.pdf
- Typst accessibility: https://typst.app/docs/guides/accessibility/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Haired ATS study: https://www.haired.app/blog/10000-cvs-ats-errors-study
- TheLadders eye-tracking study: https://www.bu.edu/com/files/2018/10/TheLadders-EyeTracking-StudyC2.pdf
