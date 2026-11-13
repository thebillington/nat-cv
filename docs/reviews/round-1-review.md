# Review — Round 1: Voice & Factual Fidelity

**Reviewer brief:** preserve Natalie's own phrasing while trimming 3 pages → 2.
**Verdict:** The **profile is largely hers** (four of five sentences are near-verbatim). The **achievement bullets are not** — they have been re-engineered into a generic "bold heading + fragment" consultancy template, and in the process roughly a dozen claims were invented. There is one **must-fix factual overstatement** (the APM qualification) and **six duplicated or invented bullet fragments**. Voice loss is concentrated in the *Areas of expertise* block and in the new closing sentence of the profile.

---

## 0. Headline findings

| # | Severity | Issue |
|---|---|---|
| 1 | **Critical** | "APM Project Management Qualification (PMQ) **qualified**" — source says "**Currently working towards**". Also dated October 2026 in source-says September 2026. |
| 2 | **Critical** | "SCQF Level 7, 6 credit points" — appears nowhere in the source. |
| 3 | High | Six invented fragments in experience (see §2). |
| 4 | High | *Areas of expertise* replaced her twelve broad skills with eight delivery-process nouns. Biggest single voice loss. |
| 5 | High | Three separate mentions of the LMS/CRM procurement; two mentions of "circa 100 volunteers"; two mentions of "many concurrent projects". |
| 6 | Medium | "exceptional" downgraded to "strong" in the profile. |
| 7 | Medium | "Leading Barnardo's benefits management framework" overstates: she led its *implementation*. |

---

## 1. Voice fidelity

### 1a. First, a correction to the brief

The phrases flagged in the brief as suspected drift are **all authentically hers** and must be left alone:

| Phrase | Source line | Verdict |
|---|---|---|
| "developing and delivering strategies and projects" | 4–5 | **Hers verbatim.** Keep. |
| "outcome-focused ways of working" | 5 | **Hers verbatim.** Keep. |
| "develop and coach teams to success" | 6 | **Hers verbatim.** Keep. |
| "keen eye for detail" | 7 | **Hers verbatim.** Keep. |
| "took the lead" | 65 | **Hers verbatim.** Keep. |
| "mobilisation and management" | 25 | **Hers verbatim.** Keep. |

The drift is not in those phrases — it is in the **material that was added around them**.

### 1b. Actual drift, side by side

**(i) Profile closing sentence — line 11 / `profile.yml` summary**

> **Final:** "Currently leading a **national transformation portfolio** at Barnardo's, and APM Project Management Qualification (PMQ) qualified."
> **Source (19–22):** "Key programmes include the national 'New Horizons' transformation programme… the Property Enhancement Programme… and the Workforce Development Programme…"

"Portfolio" is not her word and inflates three named programmes into an implied portfolio remit. "Qualified" is factually wrong (see §2).
**Replacement (her words only):**
> "Currently leading programmes at Barnardo's including the national 'New Horizons' transformation programme, and working towards the APM Project Management Qualification."

**(ii) Property bullet — lines 36–37**

> **Final:** "…circa 900 properties, **moving from fragmented local practice to a single operating model**."
> **Source (21–22):** "…a Target Operating Model in a directorate looking after circa 900 properties"

The clause is invented, is consultant-speak, and implicitly disparages colleagues ("fragmented local practice"). She never said it.
**Replacement:** delete the clause; the source sentence already lands. If a closing beat is wanted, use her own framing from line 26: "…with clear objectives, milestones and success measures."

**(iii) Workforce bullet — lines 38–40**

> **Final:** "…on a programme funded by a £2.5 million Department for Education budget, **coordinating partners, reporting and delivery milestones**."
> **Source (23–24):** "…with a £2.5 million Department for Education-funded budget."

Entirely invented job description. **Delete** after "budget."

**(iv) Crisis at Christmas — line 72**

> **Final:** "Leading the Crisis at Christmas project **end to end**, recruiting and managing circa 100 volunteers…"
> **Source (57):** "Led on the Crisis at Christmas project, recruiting and managing circa 100 volunteers to support annual events."

"End to end" is filler. **Replacement:** "Led on the Crisis at Christmas project, recruiting and managing circa 100 volunteers to support annual events." (Also fixes the tense clash — see §5.)

**(v) Crisis PM first bullet — line 55**

> **Final:** "…systems procurement side by side, **balancing competing priorities and dependencies**."
> **Source (39):** "Managed many concurrent projects, including…"

Invented, and generic. **Replacement:** "Managed many concurrent projects, including volunteering and lived experience transformation, Christmas volunteer recruitment and procurement of a new Learning Management System and CRM." — i.e. her original sentence, which is one line and needs no gloss.

**(vi) Crisis PM fifth bullet — lines 65–66**

> **Final:** "Led procurement of a Learning Management System and CRM. **Defining requirements, evaluating suppliers and planning implementation for two business-critical systems.**"
> **Source (40):** "…procurement of a new Learning Management System and CRM."

The whole second sentence is invented, and it is the third time the LMS/CRM appears. **Delete the bullet entirely** (it is already covered by the role summary and should be folded into the "many concurrent projects" bullet).

**(vii) *Areas of expertise* — lines 22–25. This is the real voice loss.**

Her *Core skills* block (source 10–13) is broad, literate and distinctive: **Strategy Design, Communication, Public Speaking / Presentation, Negotiation / Influencing Skills, Copy Editing / Writing, Training / Teaching / Coaching, Business Development, Translation**. The rewrite keeps only process nouns — RAID logs, target operating models, business readiness, benefits realisation, adoption and training, executive influencing.

The effect is that a manager whose differentiators are **language, writing, teaching and speaking** now reads as a delivery-process technician. Four of the replaced terms are directly backed by qualifications she holds (MA Translation Studies; Copy Editing, Merit; PGDE; ILM).

**Replacement for lines 22–25 (her vocabulary, reordered by seniority):**

> Programme management · Strategy design · Stakeholder management · Relationship management
> Programme governance · Benefits management · RAID and risk management · Line management
> Change and equality impact assessment · Business analysis · User research · Coaching
> Public speaking / presentation · Negotiation and influencing · Copy editing and writing · Translation

This keeps every one of her originals and adds only the terms she actually used in the Barnardo's bullets.

**(viii) Company descriptors.** "National children's charity", "National homelessness charity", "National disability charity" are additions but harmless and accurate. "Secondary education" under a named school is tautological — drop it or use "Secondary school".

---

## 2. Factual fidelity

Pedantic pass. Every claim in the final checked against the source.

### MUST-FIX: unsupported or overstated

| # | Final claim | Location | Source | Problem |
|---|---|---|---|---|
| F1 | "APM Project Management Qualification (PMQ) **qualified**" | line 11; `profile.yml:14` | line 88: "September 2026: **Currently working towards** APM Project Management Qualification" | **Direct overstatement of a credential.** Not "trimming". |
| F2 | "APM Project Management Qualification (APM PMQ) — **October 2026**" | line 95 | line 88: "**September** 2026" | Month changed. Note today is Nov 2026, so a 2026 date also implies completion. If she has now passed, the **source** must be updated — do not assert it from the trim. |
| F3 | "**SCQF Level 7, 6 credit points**" | line 96 | — | Not in source. Plausible for the real PMQ but is an unsourced credential detail. Confirm or delete. |
| F4 | "national transformation **portfolio**" | line 11 | lines 19–24: three named *programmes* | Scope inflation. |
| F5 | "moving from fragmented local practice to a single operating model" | lines 36–37 | — | Invented. |
| F6 | "coordinating partners, reporting and delivery milestones" | lines 39–40 | — | Invented. |
| F7 | "end to end" | line 72 | — | Invented. |
| F8 | "balancing competing priorities and dependencies" | line 55 | — | Invented. |
| F9 | "Defining requirements, evaluating suppliers and planning implementation for two business-critical systems" | line 66 | — | Invented. |
| F10 | "**Leading** Barnardo's benefits management framework" | lines 43, and bullet title | line 27: "Leading the **implementation of** Barnardo's benefits management framework" | She leads its *implementation*, not the framework. Pedantic but it is a promotion of scope. |
| F11 | "Led procurement of a Learning Management System and CRM" | line 65 | line 40: "procurement of a new LMS and CRM" (as one of many projects) | Source does not say she *led* the procurement; it lists it among projects managed. Soften to "managed the procurement of". |
| F12 | "**Delivered** volunteering and lived experience transformation…" | line 54 | line 39: "**Managed** many concurrent projects, including…" | "Delivered" is stronger than "managed". Also duplicates F13. |

### Checked and CORRECT

| Claim | Verdict |
|---|---|
| **£2.5 million** DfE-funded Workforce Development Programme | ✅ Matches source line 23 exactly. Not overstated — the source itself says "£2.5 million Department for Education-funded budget". |
| **circa 900 properties** | ✅ Matches "circa 900 properties" (line 22). "circa" retained, not converted to "c." or "900". |
| "45+ volunteers", "25+ staff", "circa 100 volunteers" | ✅ All match source lines 64, 59, 57. |
| "over fifteen years' experience" | ✅ Her own claim (line 4). See §2 note below. |
| Dates: Oct 2025–Present; Dec 2018–Oct 2025; Aug 2016–Nov 2018; Apr 2012–May 2016; Jul 2009–Apr 2012 | ✅ All match source exactly. |
| MA with Merit; PGDE; BA (2:1); ILM Level 3; Copy Editing Merit | ✅ All match. |
| Trustee, Advance NG + HR Working Group | ✅ Matches lines 99–101. |
| 500 Words judge 2013; Arches 2016; Age Concern 2007; Commonwealth Games 2022 | ✅ All match; "BBC Radio 2" and "national children's writing competition" are accurate external facts but are additions to her text. Acceptable. |

### Pedantic note on the fifteen years

Source line 4 makes the same claim, so it is hers to make. Strictly: seven of those years (2009–2012) were classroom teaching, not third sector; third-sector time (2012→2026) is **fourteen** years. If challenged in interview she has no defence. Low priority because it is her own sentence, but "over fifteen years' experience, the last fourteen in the third sector" would be bulletproof.

---

## 3. Lost substance

### Genuine losses — restore or acknowledge

| Lost | Source | Why it matters for a senior application |
|---|---|---|
| **Business analysis and user research workshops** — the whole achievement | 34–35 | The only bullet framed around *customer and business needs*, and the only evidence of service-design facilitation. Currently survives only as two words in *Areas of expertise*. **This is the most serious content loss.** |
| **Crisis members gain "personal and social skills, work experience, and develop positive social networks"** | 54–56 | Compressed to "acting as a source of expertise". The human outcome — her values, the third-sector substance — is gone entirely. |
| **Strategy Design** | 12 | Senior differentiator, and supported by her actual work (local volunteering strategy, national strategy at Guide Dogs). |
| **Translation; Copy Editing / Writing; Public Speaking / Presentation** | 10–13 | Three unusual, memorable, qualification-backed differentiators. All three now absent from a document that has an MA in Translation Studies and a Copy Editing merit. |
| **Language skills: French fluent, Spanish competent** | 96 | Dropped with no replacement. Directly supports the MA and the "Translation" skill. One line restores it. |
| **NVQ Spanish Level 2, 100% pass-rate** | 85 | The only hard metric in the teaching role. |
| **CLIL — teaching Maths and PSHE *in French*** | 83–84 | Distinctive, and evidences exactly the communication range a senior programme role needs. |
| **"greatly aiding my interpersonal skills"** | 106 | Her own reflective voice — the last surviving trace of first person outside the trustee entry. |

### Appropriate trimming — do not restore

- 4 A Levels (ABBB), 2 AS Levels (AA), 13 GCSEs (6 A*, 7 A) — correct cut for 15+ years' experience.
- "Self-motivated and innovative" — cliché; but note "innovative" is preserved in spirit by "accelerate innovation".
- Full home address to "Linby, Nottinghamshire" — correct (though "Nottingham" → "Nottinghamshire" is an addition; Linby is in Nottinghamshire, so accurate).
- Reducing five teaching bullets to one sentence — correct.
- Merging the two Guide Dogs training/marketing bullets — acceptable, though the merge is clumsy (see §5).

### Judgement call

The closing personal line — *"I live in Nottingham with my husband and two young children and am a keen dancer, singer, pianist and regular gym goer"* — has gone. For a two-page senior CV in the UK third sector this is defensible, but it was **the single most distinctive voice marker in the document**, and its removal is a direct contributor to the anonymisation noted in §4. If a line can be found, I would keep a shortened version.

---

## 4. Tone

**The opening, verbatim:**

> "Programme and Project Manager with over fifteen years' experience developing and delivering strategies and projects within the third sector. Accustomed to creative and outcome-focused ways of working, with a proven ability to develop and coach teams to success. An effective communicator with strong people management and relationship building skills, adaptable, with a keen eye for detail. Currently leading a national transformation portfolio at Barnardo's, and APM Project Management Qualification (PMQ) qualified."

**Assessment: sentences 1–3 are unmistakably her.** Only two changes were made to her text ("exceptional"→"strong"; the full stop before "Adaptable" replaced by a comma), and both are regressions. Sentence 4 is entirely new and is the one that reads like a recruiter wrote it — "portfolio" is not her register, and the credential clause reads as a checkbox.

So the *profile* is recognisably her. **The rest of the document is not**, for two structural reasons:

1. **The "heading. fragment." template.** Her source bullets are flowing sentences with a subject and a verb ("Leading the delivery of complex projects…", "Providing programme governance through the mobilisation and management of…"). The rewrite converts each into a bolded noun-phrase title followed by a subordinate fragment. Some of these fragments are ungrammatical or nonsensical as standalone titles — "Member of the leadership team." and "Business planned service delivery against budget." are the worst offenders. This is the standard consultancy CV shape, not her voice.
2. **The vocabulary was swapped.** Where she wrote *Stakeholder Management, Relationship Management, Training / Teaching / Coaching, Strategy Design*, the final has *Executive influencing, Partnership working, Adoption and training, Business readiness*. Her words are warmer and broader; the replacements are colder and narrower — and, per §2, some of them were invented to fill the space.

**Recommendation:** keep the bold-lead-in device (it aids scanning and is legitimate structuring) but **restore her sentence to complete-sentence form wherever it already was one**, and revert the *Areas of expertise* vocabulary wholesale.

---

## 5. Grammar and consistency

### British spelling ✅
All correct: *programme, organisational, maximising* (source's American "maximizing" at line 69 correctly fixed), *mobilising, coordinating*. No Americanisms found.

### Must fix

| # | Issue | Location | Fix |
|---|---|---|---|
| G1 | **Comma splice / run-on.** "…relationship building skills, adaptable, with a keen eye for detail." Source has a full stop and a capital: "…skills. Adaptable, with a keen eye for detail." | line 9–10; `profile.yml:12–13` | Restore the full stop: "…relationship building skills. Adaptable, with a keen eye for detail." (Only the comma-join is wrong; her words are fine.) |
| G2 | **Tense clash inside one bullet.** "**Line managed** the Events and Christmas Coordinator. **Leading** the Crisis at Christmas project…" | lines 71–72 | Both past: "Line managed the Events and Christmas Coordinator and led on the Crisis at Christmas project, recruiting and managing circa 100 volunteers to support annual events." |
| G3 | **Fragment headings that are not achievements.** "Member of the leadership team." is a status, not an outcome; "Business planned service delivery against budget." is verb-initial and breaks the noun-phrase pattern used by every other bullet. | lines 75, 82 | "Member of the leadership team — devising strategic and leadership approaches for 25+ staff." / "Business planned service delivery against budget and resource allocation…" as a running sentence. |
| G4 | **Triple duplication, Crisis PM.** The LMS/CRM appears in the summary (line 53) *and* bullet 1 (line 54) *and* bullet 5 (line 65). "Many concurrent projects" appears in the summary *and* as a bullet title within three lines. | lines 52–66 | Delete bullet 5; rewrite bullet 1 or delete the summary sentence. One statement, not three. |
| G5 | **Duplication, Crisis V&I.** Summary (69–70) and bullet 1 (71–72) both say "recruiting and managing circa 100 volunteers to support annual events." | lines 69–72 | Keep once. |
| G6 | **Repetition inside a bullet.** "Designed and delivered disability awareness **training**. **Training** volunteers, carers…" | line 86 | "…disability awareness training for volunteers, carers, service providers and businesses, and marketed the service locally and nationally through case studies, press releases and presentations." |
| G7 | **Dangling list.** "…to ensure successful adoption of organisational change, including change impact assessments, equality impact assessments, communications planning, readiness activities and training coordination." Reads as if the impact assessments ensure adoption. Two source bullets were merged into one sentence. | lines 46–49 | Split with a full stop: "…to ensure successful adoption of organisational change. Leading structured change management activity including change impact assessments, equality impact assessments, communications planning, readiness activities and training coordination." (Her source heading, line 32.) |
| G8 | **Ampersand inconsistency.** Header title "Programme **&** Project Manager"; summary "Programme **and** Project Manager". | line 2 vs line 7 | Pick "and" in both, matching her source line 4. |
| G9 | **Acronym defined oddly:** "APM Project Management Qualification (**APM PMQ**)". | line 95 | "APM Project Management Qualification (PMQ)". |

### Nice to have

| # | Issue | Location |
|---|---|---|
| G10 | **Qualifications not in date order.** Sequence is 2026, 2022, 2009, 2007, 2015, 2012 — the ILM (2015) and Copy Editing (2012) are stranded after the 2007 degree. | lines 95–103 |
| G11 | **ILM date wraps across lines**: "September 2014 –" / "February 2015". Layout bug in the right-hand date column. | lines 101–102 |
| G12 | **Inconsistent date presentation in voluntary section**: trustee has none, Games has "2022" fused into the org name, others use "(2016)" "(2013)" "(2007)". | lines 107–115 |
| G13 | **Punctuation system differs between sections**: Experience uses "Heading." + sentence; Governance uses "Role, Org: sentence". Pick one. | lines 30–92 vs 107–115 |
| G14 | **Tautology**: "Athlete Services Team Member…: Volunteered as part of the athlete services team during the Games." | lines 110–111 |
| G15 | "Distance learning" — inconsistent capitalisation against "Merit", "Institute of Leadership & Management". | line 103 |
| G16 | "Terms of Reference" and "Steering Groups" capitalised mid-sentence while "RAID logs" is not. Source is inconsistent here too; standardise. | lines 41–42 |
| G17 | Header name renders as "Natalie&nbsp;&nbsp;&nbsp;&nbsp;Rebecchi" with a large gap — check this is intentional letter-spacing, not a broken layout. | line 1 |
| G18 | "Befriender" is presented as a role title; source gives no title. | line 115 |

### Verified consistent ✅
En dashes in all date ranges and role titles; "circa" used consistently (never "c."); bullet terminal punctuation consistent (none); section headings all sentence case; footer "Natalie Rebecchi · Page 1 of 2" correct on both pages; email and phone unchanged (07793280945 → 07793 280945 ✅).

---

## 6. Prioritised edits

### MUST-FIX (factual accuracy — do not ship without these)

1. **`data/profile.yml:14`** — replace
   `"…detail. Currently leading a national transformation portfolio at Barnardo's, and APM Project Management Qualification (PMQ) qualified."`
   with
   `"…detail. Currently leading programmes at Barnardo's including the national 'New Horizons' transformation programme, and working towards the APM Project Management Qualification."`

2. **`docs/reviews/_final_text.txt:95–96`** — `October 2026` → `September 2026` (per source); and if she has *not* now passed, the qualification row must read "working towards", not a completion date. **Confirm with Natalie which is true**; if passed, correct the source, not just the CV.

3. **`_final_text.txt:96`** — remove `· SCQF Level 7, 6 credit points` unless Natalie confirms it and the source is updated to carry it.

4. **`_final_text.txt:36–37`** — delete `, moving from fragmented local practice to a single operating model`.

5. **`_final_text.txt:39–40`** — delete `, coordinating partners, reporting and delivery milestones`.

6. **`_final_text.txt:54–55`** — restore her sentence: `Managed many concurrent projects, including volunteering and lived experience transformation, Christmas volunteer recruitment and procurement of a new Learning Management System and CRM.` (removes "Delivered", "systems procurement", "balancing competing priorities and dependencies").

7. **`_final_text.txt:65–66`** — delete the fifth Crisis bullet in full (third mention of LMS/CRM; entirely invented detail).

8. **`_final_text.txt:43` + `barnardos.yml:44`** — `Leading Barnardo's benefits management framework` → `Leading the implementation of Barnardo's benefits management framework`.

9. **`_final_text.txt:71–72`** — delete `end to end`; fix the tense clash (G2).

10. **`_final_text.txt:11` / `profile.yml:12–13`** — restore `exceptional` in place of `strong`, and restore the full stop before `Adaptable` (G1).

11. **`_final_text.txt:22–25`** — replace the *Areas of expertise* block with her vocabulary (replacement in §1b(vii)). Must include **Strategy design**, **Communication**, and at minimum **Copy editing and writing** and **Translation**.

12. **`_final_text.txt:69–72`** — de-duplicate the "circa 100 volunteers" sentence (G5).

13. **`_final_text.txt:2`** — `Programme & Project Manager` → `Programme and Project Manager` (G8).

### NICE-TO-HAVE (substance and polish)

14. **`_final_text.txt` after :49** — restore the dropped Barnardo's achievement: *"Facilitating business analysis and user research workshops to inform the design and delivery of services, systems, processes and organisational structures that meet customer and business needs."* This is the biggest genuine content loss.

15. **`_final_text.txt:73–74`** — restore the members' outcome: *"…acting as a source of expertise on volunteering opportunities for members within Crisis and in the wider area, helping them to gain personal and social skills, work experience and positive social networks."*

16. **`_final_text.txt:103`** — add one line: `Languages: French — Fluent; Spanish — Competent`.

17. **`_final_text.txt:89–92`** — add back `(100% pass-rate)` for NVQ Spanish, and mention teaching Maths and PSHE in French through CLIL. One clause, real differentiation.

18. **`_final_text.txt:46–49`** — split the merged stakeholder / change-management sentence (G7).

19. **`_final_text.txt:75`, `:82`** — repair the two broken fragment headings (G3).

20. **`_final_text.txt:86–88`** — fix "training… Training" repetition and restore "marketed" as a parallel verb (G6).

21. **`_final_text.txt:82`** — restore `and resource allocation` after "against budget".

22. **`_final_text.txt:110–111`** — rewrite the tautological Commonwealth Games line.

23. **`_final_text.txt:95–103`** — reorder qualifications reverse-chronologically; fix the ILM date wrap.

24. **`_final_text.txt:107–115`** — restore first person in the trustee entry ("I am a trustee for…" → or at least "Overseeing…" kept but with a first-person framing); it is the last first-person voice in the document.

25. Consider one short personal line (dancer/singer/pianist/gym, or the family line) if space permits — it is the most distinctive voice marker she has.

### Do NOT change

"Self-motivated" is already cut — fine. But leave **"developing and delivering strategies and projects"**, **"creative and outcome-focused ways of working"**, **"develop and coach teams to success"**, **"keen eye for detail"**, **"took the lead"** and **"mobilisation and management"** exactly as they are. They are hers, they are the reason the profile still sounds like her, and replacing them would be the exact failure this review exists to prevent.

---

### One-line summary for the file

> Round 1: profile is ~80% Natalie's own language and should be preserved almost untouched (restore "exceptional", fix the comma splice, remove the invented "portfolio" and the false "qualified"). Experience bullets need six invented fragments removed and three duplications collapsed. *Areas of expertise* must revert to her vocabulary — the current block is the single largest voice loss in the rewrite. One critical factual error: APM PMQ is "working towards", not "qualified".
