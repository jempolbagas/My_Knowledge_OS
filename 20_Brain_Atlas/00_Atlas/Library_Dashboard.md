---
type: dashboard
title: "Library & Brain Atlas Dashboard"
date_updated: 2026-08-02
tags:
  - dashboard
  - library
  - brain-atlas
---

# 📚 Library & Brain Atlas Dashboard

> [!info] Command Center Overview
> Central dashboard for monitoring external research sources (`10_Library/`), generated deep-dives (`Generated_Readings/`), the concept promotion pipeline, and atomic concept integrity (`20_Concepts/`).

---

## 📥 Unread & In-Progress Library Items

> [!abstract] Sources pending review, reading, or deep analysis.

```dataview
TABLE type, status, notes_by, date_added
FROM "20_Brain_Atlas/10_Library"
WHERE status != "done"
SORT date_added ASC
```

---

## 🚀 Concept Extraction Queue

> [!todo] Completed source notes with unchecked concepts to extract into `20_Concepts/`.

```dataview
TABLE type, status, date_added
FROM "20_Brain_Atlas/10_Library"
WHERE status = "done" AND length(filter(file.tasks, (t) => !t.completed)) > 0
SORT date_added DESC
```

---

## 🤖 Generated Deep Dives & Readings

> [!note] Synthesized readings and explainers stored in `10_Library/Generated_Readings/`.

```dataview
TABLE file.folder AS Subject, date_added, status
FROM "20_Brain_Atlas/10_Library/Generated_Readings"
SORT date_added DESC
```

---

## 🧠 Atomic Concepts Maintenance

> [!warning] Concepts Missing Source Backlink
> Standalone concepts or notes missing explicit `source` metadata linking back to a Library note or Generated Reading.

```dataview
LIST
FROM "20_Brain_Atlas/20_Concepts"
WHERE !source
SORT file.name ASC
```
