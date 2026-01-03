---
tags:
  - inbox
  - dashboard
type: Dashboard
up:
  - - Braindump Inbox
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

# Dashboard - All Tasks

> **⚠️ READ-ONLY VIEW - Do not add tasks here**
>
> This dashboard auto-aggregates tasks from all your projects using Dataview.
> It's meant for **viewing** your task landscape, not for adding new tasks.
>
> **To capture new tasks:** Go to [[Braindump Inbox]]
> **To work on tasks:** Open the actual project files in [[1 Projects/]]

---

### High level



# Life Tasks


## Automated List of Projects
```dataview 
LIST join(file.tags, ", ") from #project 
WHERE contains(file.path, "Archive") = false
```
```
```

## ==Automated Task Lists==

```dataviewjs 
dv.taskList(dv.pages('"1 Projects"').file.tasks .where(t => !t.completed)) 
```
This
## References
1. [[Braindump Inbox]]
2. [[3 Resource/Readwise/Books/Getting Things Done|Getting Things Done]]
3. [[Learn How to Get Stuff Done]]