---
layout: page
title: Courses
order: 4
---

<section id="courses">
{% assign courses = site.data.courses %}
{% for c in courses %}
<div>
    <h3>{{ c.title }} ({{ c.target }})</h3>
    <ul>
        {% for year in c.years %}
        <li>{{ year }}</li>
        {% endfor %}
    </ul>
    <p>
    {{ c.desc }}
    </p>
</div>
{% endfor %}
</section>
