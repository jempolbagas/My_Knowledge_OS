```dataview
TABLE status, notes_by, date_added
  FROM "20_Brain_Atlas/10_Library"
  WHERE status != "done"
  SORT date_added ASC
```
```dataview
TABLE status, date_added
  FROM "20_Brain_Atlas/10_Library"
  WHERE status = "done" AND length(filter(file.tasks, (t) => !t.completed)) > 0
```

```dataview
LIST
  FROM "20_Brain_Atlas/20_Concepts"
  WHERE !source
```
