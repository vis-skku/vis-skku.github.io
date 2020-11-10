---
layout: post
title: Publications
order: 3
---

{% assign publications = site.data.publications %}

{% assign years = publications | group_by: "year" | sort: "name" | reverse %}

{% for year in years %}

<div class="d-flex pt-2">
<h3 class="mr-4">{{ year.name }}</h3>
{% assign sorted = year.items | sort: "index" %}
<div class="pt-1">
{% for pub in sorted %}
{% include publication.html pub = pub %}
{% endfor %}
</div>
</div>
{% endfor %}
