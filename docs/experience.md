# Experience

{% for role in data.experience %}
## {{ role.company }}

### {{ role.title }}

<p class="role-meta">{{ role.start }} to {{ role.end }} · {{ role.sector }}</p>

<p class="role-summary">{{ role.summary }}</p>

{% if role.achievements %}
<ul class="role-list">
{% for a in role.achievements %}
  <li><strong>{{ a.title }}.</strong> {{ a.description }}</li>
{% endfor %}
</ul>
{% endif %}

{% endfor %}
