# Qualifications and professional development

{% for cert in data.certifications.certifications %}
## {{ cert.name }}

<p class="role-meta">{{ cert.issuer }}, {{ cert.awarded }}, {{ cert.grade }}</p>

{% endfor %}

## Education and further study

<ul class="qualification-list">
{% for edu in data.education.education %}
  <li>
    <strong>{{ edu.degree }}</strong>, {{ edu.institution }}
    {% if edu.grade %}<span class="qual-grade">, {{ edu.grade }}</span>{% endif %}
    <br />
    <span class="qual-grade">{{ edu.start }} to {{ edu.end }}</span>
  </li>
{% endfor %}
</ul>

## Languages

French (fluent) and Spanish (competent)
