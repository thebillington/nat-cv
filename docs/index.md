# {{ data.profile.name }}

<p class="hero-role">{{ data.profile.title }}</p>
<p class="hero-contact">{{ data.profile.location }}<br /><a href="mailto:{{ data.profile.email }}">{{ data.profile.email }}</a></p>

<p class="button-row">
  <a class="md-button md-button--primary" href="cv-{{ data.profile.name.lower().replace(' ', '-') }}.pdf">Download CV (PDF)</a>
  <a class="md-button" href="experience/">View experience</a>
</p>

## Profile

{{ data.profile.summary }}

## Current work at Barnardo's

<ul class="outcomes">
{% for item in data.profile.portfolio %}
  <li><strong>{{ item.label }}</strong>: {{ item.text }}</li>
{% endfor %}
</ul>

## Areas of expertise

<div class="expertise">
{% for line in data.skills.expertise %}
<p>{{ line }}</p>
{% endfor %}
</div>

## Current role

### {{ data.experience[0].title }}, {{ data.experience[0].company }}

<p class="role-meta">{{ data.experience[0].start }} to {{ data.experience[0].end }} ({{ data.experience[0].sector }})</p>

{{ data.experience[0].summary }}

<ul class="role-list">
{% for a in data.experience[0].achievements %}
  <li><strong>{{ a.title }}.</strong> {{ a.description }}</li>
{% endfor %}
</ul>

<a class="md-button" href="experience/">Full experience</a>
