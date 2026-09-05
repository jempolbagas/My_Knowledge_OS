---
type: dashboard
title: Learning Dashboard
created: 2026-09-03
tags: [dashboard, meta]
---

# Learning Dashboard

## All Notes by Subject

```dataview
TABLE subject, created, length(prerequisites) AS "# Prereqs"
FROM "20 Brain Atlas/20 Notes"
WHERE type = "note"
SORT subject ASC, created DESC
```

## Notes Ready to Learn

```dataview
LIST
FROM "20 Brain Atlas/20 Notes"
WHERE length(prerequisites) = 0 OR all(prerequisites, (p) => contains(file.outlinks, p))
```

## Skill Trees

- [[Skill_Tree_Mathematics]]
- [[Skill_Tree_AI]]
- [[Skill_Tree_Image_Segmentation]]
- [[Skill_Tree_Cybersecurity]]

## Reference Library

```dataview
LIST
FROM "20 Brain Atlas/30 Reference Lib"
SORT file.name ASC
```
