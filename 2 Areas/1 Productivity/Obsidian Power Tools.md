---
tags:
  - productivity
type: Idea
up:
  - []
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`
 
### Summary
These are code snippets that forms the base of being able programmatically interact with Obsidian notes

### List all Types
````
```dataviewjs 
let types = [] 
for (let type of dv.pages().type) { 
	if (tyoes.indexOf(type) == -1) { 
	types.push(type) 
	} 
}
dv.list(type)
```
````
```dataviewjs 
let types = [] 
for (let type of dv.pages().type) { 
	if (types.indexOf(type) == -1) { 
	types.push(type) 
	} 
}
dv.list(types)
```


### List all unique Tags
````
```dataviewjs 
let tags = [] 
for (let tag of dv.pages().file.tags) { 
	if (tags.indexOf(tag) == -1) { 
	tags.push(tag) 
	} 
}
dv.list(tags)
```
````
```dataviewjs 
let tags = [] 
for (let tag of dv.pages().file.tags) { 
	if (tags.indexOf(tag) == -1) { 
	tags.push(tag) 
	} 
}
dv.list(tags)
```


### List all the open tasks in #inbox 
````
```dataviewjs 
dv.taskList(dv.pages("#inbox").file.tasks .where(t => !t.completed)) 
```
// Bonus: tasks not in planner
dv.taskList(dv.pages("#inbox and -#planner").file.tasks .where(t => !t.completed)) 
````

```dataviewjs 
dv.taskList(dv.pages("#inbox").file.tasks .where(t => !t.completed)) 
```
### Randomly Audit Features of Files


````
```dataviewjs 
let tags = [] 
for (let tag of dv.pages().type) { 
	if (tags.indexOf(tag) == -1) { 
	tags.push(tag) 
	} 
}
dv.list(tags)


```dataviewjs 
dv.list(dv.pages().map(x => x.file.path + " TYPE: " + x.type + " " + x.tags))
```
````
```
```

## References
1. 