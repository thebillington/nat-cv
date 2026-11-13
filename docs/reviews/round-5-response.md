# Review round 5 — rendered PDF layout

Reviewer examined the actual rendered pages at 150 dpi and measured ink gaps
against the PDF bounding boxes.

## What the review found

- The spacing was structural, not cosmetic: inline `v()` calls were added to
  paragraph spacing, so the air above section headings varied from 16.8pt to
  32.2pt depending on what preceded them.
- The heading rule sat 13 to 17pt below the heading but only 11pt above the
  body, so it read as a divider rather than an underline.
- The gap above "Barnardo's" was larger than the gap above "Experience", making
  the employer compete with the section heading.
- Subtitle and contact line were only 3.4pt apart, so the masthead read as a
  two-line blob.
- Stray spaces appeared before commas in five strings (`Programme Manager ,
  National children's charity`), caused by newlines between inline text calls.
- Page 2 had a large empty area at the foot.

## What was changed

- Rebuilt the level-2 heading as a single block with `above: 30pt`, `below:
  10pt`, a 0.7pt teal bottom stroke and 4pt inset. Heading gaps are now
  consistent at roughly 27pt, and the rule sits 3 to 4pt under the heading.
- Rebuilt the masthead with `stack()` and explicit spacing, so name, title,
  contact and rule have a consistent rhythm.
- Page margins set to 20mm sides, 14mm top, 13mm bottom.
- Role spacing set to 20.5pt, giving a clean progression: bullet 12pt, role
  18pt, section 27pt.
- Removed the stray spaces before punctuation by composing each line inside a
  single text call.
- Levelled body sizes to 9.5/10/10.5pt and increased the summary-to-bullet gap.
- Footer reduced to the page number only.

## Accepted white space

Page 2 remains about three-quarters full. The review recommended filling it
with the website's "Current work at Barnardo's" block, but that block belongs
before Experience, and placing it at the end would be worse than the white
space. The facts are carried by the Barnardo's bullets. The white space is
accepted rather than padded with stretched leading.
