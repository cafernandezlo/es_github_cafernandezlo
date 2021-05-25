---
layout: page
permalink: /publications/
title: JCR-indexed journal publications
description: Publications by years in chronological order.
years: [2021,2020,2019,2018,2017,2016,2015,2014,2013]
lastyear: 2021
---
I have published {% bibliography_count -f papers --query @article[year<={{page.lastyear}} ] %} research manuscripts in JCR-indexed journals.
<br>
<br>
<small>Asteriks (*) indicate authors with equal contributions.</small>

{% for y in page.years %}
  <h3 class="year">{{y}}</h3>
  <h4 class="number">{% bibliography_count -f papers --query @article[year={{y}} ] %}</h4>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}
