# Volunteering and governance

{% for item in data.volunteering.volunteering %}
## {{ item.role }}, {{ item.organisation }}

<p class="role-meta">{% if item.year %}{{ item.year }}{% endif %}{% if item.location %}{% if item.year %} ({% endif %}{{ item.location }}{% if item.year %}){% endif %}{% endif %}</p>

{{ item.description }}

{% endfor %}

## Outside work

{% for line in data.volunteering.personal %}
{{ line }}
{% endfor %}
