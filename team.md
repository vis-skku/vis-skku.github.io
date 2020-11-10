---
layout: page
title: Team
order: 1
---

<section id="team">
<div class="d-flex">
{% assign team = site.data.team %}
{% for person in team %}
<div class="text-center person">
<img src="{{ person.pic }}" height="160">

<div class="name">{{ person.name }}</div>
<div class="pos">{{ person.pos }}</div>
<div class="email">{{ person.email }}</div>

<div class="text-center">
{% if person.website %}
    <a href="{{ person.website }}" target="_blank"><i class="fas fa-home" aria-hidden="true"></i> Website</a>
{% endif %}
</div>
</div>
{% endfor %}
</div>
</section>
