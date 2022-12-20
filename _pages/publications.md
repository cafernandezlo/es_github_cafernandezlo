---
layout: page
permalink: /publications/
title: publications
description: Publications by years in reverse chronological order and type.
years: [2022,2021,2020,2019,2018,2017,2016,2015,2014,2013]
confyears: [2021,2020,2019,2018,2017,2016,2015,2013,2012,2011]
bookyears: [2019,2018,2014,2013,2012,2011]
---
I have published {% bibliography_count -f papers --query @article[year<={{2022}} ] %} JCR-indexed papers
({{site.total_q1}}-Q1 ranked) and {% bibliography_count -f conferences --query @inproceedings[year<={{2022}} ] %} 
contributions in conferences. Moreover, I have published {% bibliography_count -f bookchapter --query @inbook[year<={{2022}} ] %}
book chapters.
<br>
<br>
PhD students are highlighted in blue.
<br>
<br>
<small>Asteriks (*) indicate authors with equal contributions.</small>

<strong>JCR-indexed journal publications list</strong>

{% for y in page.years %}
  <h3 class="year">{{y}}</h3>
  <h4 class="number">{% bibliography_count -f papers --query @article[year={{y}} ] %}</h4>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

<strong>Conference publications list</strong>

{% for y in page.confyears %}
  <h3 class="year">{{y}}</h3>
  <h4 class="number">{% bibliography_count -f conferences --query @inproceedings[year={{y}} ] %}</h4>
  {% bibliography -f conferences -q @*[year={{y}}]* %}
{% endfor %}

<strong>Book chapters list</strong>

{% for y in page.bookyears %}
  <h3 class="year">{{y}}</h3>
  <h4 class="number">{% bibliography_count -f bookchapter --query @inbook[year={{y}} ] %}</h4>
  {% bibliography -f bookchapter -q @*[year={{y}}]* %}
{% endfor %}
