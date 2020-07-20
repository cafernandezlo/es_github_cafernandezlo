---
layout: page
permalink: /publications/
title: JCR-indexed journal publications
description: Publications by years in chronological order.
years: [2020,2019,2018,2017,2016,2015,2014,2013]
---
Summary:
<div class="wrapper">
Total publications with I.F: 32 <br>
Accumulated I.F.: 106,976 <br>
Q1 publications: 17 (53% indexed publications) <br>
D1 publications: 8 (22% indexed publications) <br>
Q2 publications: 11 (34% indexed publications) <br>
Publications with I.F. (first author): 15<br>
Publications with I.F. (second author): 6<br>
Publications with I.F. (no PhD supervisors): 19<br>
Publications with I.F. (no authors same institution): 3<br>
Publications with I.F. (corresponding): 12<br>
Publications with I.F. (senior): 1<br>
87% indexed publications with I.F in Q1-Q2<br>
<br>
</div>
Asteriks (*) indicate authors with equal contributions.

{% for y in page.years %}
  <h3 class="year">{{y}}</h3>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}
