# Dashboard Dataview Queries

These live in `00_Atlas/Dashboard_Self_Study.md` (or a new `00_Atlas/Library_Dashboard.md`). Requires the Dataview plugin. They give both the user and the agent a live view instead of manually re-scanning frontmatter — the agent still does the actual promoting/reorganizing.

## Unread / in-progress Library items
```dataview
TABLE status, notes_by, date_added
FROM "20_Brain_Atlas/10_Library"
WHERE status != "done"
SORT date_added ASC
```

## Promotion queue
`status: done` notes that still have unchecked "Concepts to extract" boxes:
```dataview
TABLE status, date_added
FROM "20_Brain_Atlas/10_Library"
WHERE status = "done" AND length(filter(file.tasks, (t) => !t.completed)) > 0
```

## Concept notes missing a source backlink
Either originally standalone or missing a link — worth a periodic check:
```dataview
LIST
FROM "20_Brain_Atlas/20_Concepts"
WHERE !source
```
