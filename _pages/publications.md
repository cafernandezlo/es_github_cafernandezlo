---
layout: page
permalink: /publications/
title: JCR-indexed journal publications
description: Publications by years in chronological order.
years: [2019,2018,2017,2016,2015,2014,2013]
---
Summary:
<div class="wrapper">
Total publications with I.F: 30 <br>
Accumulated I.F.: 101,466 <br>
Q1 publications: 16 (53% indexed publications) <br>
D1 publications: 7 (22% indexed publications) <br>
Q2 publications: 10 (33% indexed publications) <br>
Publications with I.F. (first author): 14<br>
Publications with I.F. (second author): 5<br>
Publications with I.F. (no PhD supervisors): 17<br>
Publications with I.F. (no authors same institution): 3<br>
Publications with I.F. (corresponding): 11<br>
Publications with I.F. (senior): 1<br>
86% indexed publications with I.F in Q1-Q2<br>
<br>
</div>

{% for y in page.years %}
  <h3 class="year">{{y}}</h3>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}
