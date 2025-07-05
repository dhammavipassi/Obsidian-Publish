---
layout: page
id: home
---

# 🌱 {{ site.title }}

欢迎来到我的数字花园，这里收录了关于阿毗达摩、佛学修行的笔记和思考。

## 📚 最近更新的笔记

<style>
.notes-list {
  list-style: none;
  padding: 0;
}

.note-item {
  margin: 1em 0;
  padding: 1em;
  border-left: 3px solid #4a9eff;
  background: #f8f9fa;
  border-radius: 4px;
}

.note-title {
  font-weight: bold;
  color: #333;
  text-decoration: none;
  font-size: 1.1em;
}

.note-title:hover {
  color: #4a9eff;
}

.note-date {
  color: #666;
  font-size: 0.9em;
  margin-top: 0.3em;
}

.graph-section {
  margin: 2em 0;
  text-align: center;
}

.graph-container {
  max-width: 600px;
  margin: 1em auto;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}
</style>

<ul class="notes-list">
{% assign recent_notes = site.notes | sort: 'last_modified_at' | reverse | limit: 8 %}
{% for note in recent_notes %}
  <li class="note-item">
    <a href="{{ note.url }}" class="note-title">{{ note.title }}</a>
    <div class="note-date">
      {% if note.last_modified_at %}
        最后更新：{{ note.last_modified_at | date: "%Y年%m月%d日" }}
      {% elsif note.date %}
        发布于：{{ note.date | date: "%Y年%m月%d日" }}
      {% endif %}
    </div>
  </li>
{% endfor %}
</ul>

---

## 🕸️ 笔记关系图

<div class="graph-section">
  <div class="graph-container">
    {% include notes_graph.html %}
  </div>
  <p><small>点击节点可以跳转到对应的笔记</small></p>
</div>

---

## 🧭 分类导航

- **基础概念**：心、心所、色法的基本理论
- **心路过程**：认知过程的详细分析  
- **禅修实践**：止观禅法的理论与实践
- **戒律研究**：戒学的深入探讨

> *"正如花园需要悉心照料才能繁茂，数字花园也需要持续的思考和更新。"*