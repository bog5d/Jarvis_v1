---
tags: [dashboard, home]
---

# 🧠 Jarvis 认知中枢

> 由 AI 自动生成的个人知识仪表盘 | 更新时间: 2026-01-11 08:24

---

## 👥 人脉雷达 (Top 10)

```dataviewjs
// 统计 key_people 出现频率
let peopleCount = {};

for (let page of dv.pages()) {
    let meta = page.jarvis_ai_meta;
    if (meta && meta.key_people) {
        let people = meta.key_people;
        if (Array.isArray(people)) {
            for (let person of people) {
                if (person && person.trim()) {
                    let name = person.trim();
                    peopleCount[name] = (peopleCount[name] || 0) + 1;
                }
            }
        }
    }
}

// 排序取 Top 10
let sorted = Object.entries(peopleCount)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10);

if (sorted.length > 0) {
    dv.table(["人物", "出现次数"], sorted);
} else {
    dv.paragraph("暂无人脉数据");
}
```

---

## 🎭 决策心境分布

```dataviewjs
// 统计 mood 分布
let moodCount = {};

for (let page of dv.pages()) {
    let meta = page.jarvis_ai_meta;
    if (meta && meta.mood) {
        let mood = meta.mood.trim();
        if (mood) {
            moodCount[mood] = (moodCount[mood] || 0) + 1;
        }
    }
}

let sorted = Object.entries(moodCount)
    .sort((a, b) => b[1] - a[1]);

if (sorted.length > 0) {
    dv.table(["心境", "笔记数"], sorted);
} else {
    dv.paragraph("暂无心境数据");
}
```

---

## 📍 时空足迹 (最近 10 个地点)

```dataviewjs
// 提取 time_space.location
let locations = [];

for (let page of dv.pages()) {
    let meta = page.jarvis_ai_meta;
    if (meta && meta.time_space && meta.time_space.location) {
        let loc = meta.time_space.location.trim();
        if (loc) {
            locations.push({
                location: loc,
                date: meta.time_space.date || "",
                file: page.file.name
            });
        }
    }
}

// 按日期排序，取最近 10 个
locations.sort((a, b) => (b.date || "").localeCompare(a.date || ""));
let recent = locations.slice(0, 10);

if (recent.length > 0) {
    dv.table(
        ["地点", "日期", "笔记"],
        recent.map(l => [l.location, l.date, l.file])
    );
} else {
    dv.paragraph("暂无地点数据");
}
```

---

## 📈 知识库统计

```dataviewjs
let total = dv.pages().length;
let tagged = dv.pages().where(p => p.jarvis_ai_meta).length;

dv.paragraph(`📁 总笔记数: **${total}**`);
dv.paragraph(`🏷️ AI 已标记: **${tagged}** (${(tagged/total*100).toFixed(1)}%)`);
```

---

## 🔍 快速导航

- [[#人脉雷达 (Top 10)|👥 人脉雷达]]
- [[#决策心境分布|🎭 心境分布]]
- [[#时空足迹 (最近 10 个地点)|📍 时空足迹]]

---

*Powered by Jarvis AI Pipeline v3.0*
