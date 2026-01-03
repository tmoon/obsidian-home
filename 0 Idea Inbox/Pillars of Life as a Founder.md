---
tags: productivity
type: Idea
up: [[]]
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

These are the pillars of life to ensure that it is worth living as we should continuously examine life--[[An unexamined life is not worth living]].

### Active Important Areas
> [!info] Active Important Areas
> The following are the active important areas for both Notion and Obsidian
```dataviewjs 

let tags = [] 
for (let tag of dv.current().file.tags) { 
	if (tags.indexOf(tag) == -1) { 
	tags.push(tag) 
	} 
}
dv.list(tags)

```



## Pillar 1: Work Life #work
1. [[My Job As a CEO]]

## Pillar 2: Relationships and Personal Life #relation

## Pillar 3: Health and Wellness #wellness

## Pillar 4: Hobbies #hobby

## Pillar 5: Learning New Things / Curiosity #learning 





## References
1. [[Types of Documents]]
2. 