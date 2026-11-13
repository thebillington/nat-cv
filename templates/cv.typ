// Natalie Rebecchi CV
// Single column, ATS-safe, tagged PDF (PDF/UA-1).

#let navy = rgb("#16324F")
#let teal = rgb("#0F5E5A")
#let slate = rgb("#3F4A56")
#let meta = rgb("#5B6570")
#let ink = rgb("#1A1A1A")

#let sans = "Source Sans 3"
#let serif = "Source Serif 4"

#let cv(data) = {
  set document(
    title: data.profile.name + " CV",
    author: data.profile.name,
    keywords: (
      "programme management",
      "project management",
      "programme governance",
      "benefits management",
      "change management",
      "third sector",
    ),
  )

  set page(
    paper: "a4",
    margin: (x: 20mm, top: 12mm, bottom: 11mm),
    fill: white,
    footer: context {
      let total = counter(page).final().first()
      set text(font: sans, size: 8.5pt, fill: slate)
      pdf.artifact[
        #align(right)[
          #data.profile.name #h(1.2em) Page #counter(page).get().first() of #total
        ]
      ]
    },
  )

  set text(font: sans, size: 9.5pt, fill: ink, lang: "en", region: "GB", hyphenate: false)
  set par(justify: false, leading: 0.62em, spacing: 1em)
  set list(
    marker: text(fill: teal)[•],
    indent: 0.5em,
    body-indent: 0.45em,
    spacing: 0.38em,
  )

  show heading.where(level: 1): it => block(above: 0pt, below: 8pt)[
    #text(font: serif, size: 26pt, weight: 600, fill: navy)[#it.body]
  ]

  show heading.where(level: 2): it => {
    context if counter(page).get().first() > 1 { v(8pt) }
    v(12pt)
    text(font: serif, size: 13pt, weight: 600, fill: navy)[#it.body]
    v(3pt)
    pdf.artifact(line(length: 100%, stroke: 0.7pt + teal))
    v(5pt)
  }

  // Header
  heading(level: 1)[#data.profile.name]

  text(size: 11pt, weight: 600, fill: teal)[#data.profile.title]
  linebreak()
  text(size: 9.5pt, fill: slate)[
    #data.profile.location
    #h(1.4em) #link("tel:" + data.profile.phone.replace(" ", ""))[#data.profile.phone]
    #h(1.4em) #link("mailto:" + data.profile.email)[#data.profile.email]
    #if data.profile.links.linkedin != none and data.profile.links.linkedin != "" [
      #h(1.4em) #link(data.profile.links.linkedin)[LinkedIn]
    ]
  ]

  v(8pt)
  pdf.artifact(line(length: 100%, stroke: 1pt + teal))

  // Profile
  heading(level: 2)[Profile]
  text(size: 10pt)[#data.profile.summary]

  // Expertise
  heading(level: 2)[Areas of expertise]
  for (i, line) in data.skills.expertise.enumerate() {
    if i > 0 { linebreak() }
    text(size: 9.2pt, fill: slate)[#line]
  }

  // Experience
  heading(level: 2)[Experience]

  for role in data.experience {
    block(above: 22pt, below: 0pt, breakable: false)[
      #text(size: 11.5pt, weight: 600, fill: navy)[#role.company]
      #h(1fr)
      #text(size: 9.5pt, fill: slate)[#role.start to #role.end]
      #linebreak()
      #text(size: 10.5pt)[#role.title]
      #text(size: 9.5pt, fill: meta)[, #role.sector]
      #if role.at("summary", default: "") != "" [
        #v(5pt)
        #text(size: 9.5pt)[#role.summary]
      ]
      #if role.at("achievements", default: ()).len() > 0 [
        #v(3pt)
        #list(
          spacing: 0.36em,
          ..role.achievements.filter(a => a.at("include_pdf", default: true)).map(a => text(size: 9.5pt)[*#a.title.* #a.description]),
        )
      ]
    ]
  }

  // Board and voluntary
  heading(level: 2)[Board and voluntary roles]

  for item in data.volunteering.volunteering.filter(i => i.at("include_pdf", default: true)) [
    #text(size: 10pt)[*#item.role*]#text(size: 10pt, fill: slate)[, #item.organisation]#if item.at("year", default: none) != none [#text(size: 9.5pt, fill: meta)[ (#item.year)]]#if item.at("location", default: none) != none [#text(size: 9.5pt, fill: meta)[, #item.location]]#text(size: 10pt)[: #item.description]
    #parbreak()
  ]

  // Qualifications
  heading(level: 2)[Qualifications and professional development]

  for cert in data.certifications.certifications [
    #text(size: 10.5pt, weight: 600)[#cert.name]#h(1fr)#text(size: 9.5pt, fill: slate)[#cert.awarded]
    #linebreak()
    #text(size: 9.5pt, fill: meta)[#cert.issuer, #cert.grade]
    #h(0.8em)
    #text(size: 8.5pt)[#link("https://natalie.rebecchi.uk/assets/certificate.pdf")[View certificate]]
    #v(4pt)
  ]

  for edu in data.education.education.filter(e => e.at("include_pdf", default: true)) [
    #text(size: 10.5pt)[#edu.degree]#text(size: 10.5pt, fill: slate)[, #edu.institution]#if edu.at("grade", default: none) != none [#text(size: 9.5pt, fill: meta)[ (#edu.grade)]]#h(1fr)#text(size: 9.5pt, fill: slate)[#edu.start to #edu.end]
    #linebreak()
  ]
}
