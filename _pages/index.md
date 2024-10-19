---
layout: page
title: Home
id: home
permalink: /
---




![202208211431065.svg](https://img2.oldwinter.top/202208211431065.svg)




## Recently updated notes

---


<strong>🆕 最近创建：</strong>

<ul>
  {% assign recent_notes = site.notes | sort: "date created" | reverse %}
  {% for note in recent_notes limit: 6 %}
    <li>
      {{ note['date created'] }} — <a class="internal-link" href=" {{ note.url }} "> {{ note.title }} </a>
    </li>
  {% endfor %}
</ul>


<strong>⏰ 最近更新：</strong>

<ul>
  {% assign recent_notes = site.notes | sort: "date modified" | reverse %}
  {% for note in recent_notes limit: 6 %}
    <li>
      {{ note['date modified'] }} — <a class="internal-link" href=" {{ note.url }} "> {{ note.title }} </a>
    </li>
  {% endfor %}
</ul>

<style>
  .wrapper {
    max-width: 46em;
  }
</style>
