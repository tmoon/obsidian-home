---
tags: planner
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

---

## 📅 WEEKLY REVIEW (Sundays Only - 30min)

> **If today is Sunday, do your weekly review FIRST before daily planning.**
> Use the [[Weekly Review Template]] or follow the checklist below.

**Quick Weekly Review Checklist:**
- [ ] Process [[Braindump Inbox]] to zero (10min)
- [ ] Review all [[1 Projects/|Projects]] - update or archive (10min)
- [ ] Plan next week's 5-7 high-leverage tasks (5min)
- [ ] Pick 3 Focus Areas for the week (5min)
- [ ] Archive Day Planners older than 7 days

**→ For full weekly review, open:** [[Weekly Review Template]]

---

## Daily Reflections
1. 

## Daily Top-line Goals

- [ ] Task 1

### Other Tasks
```dataviewjs 
dv.taskList(
  dv.pages("#inbox")
    .where(p =>
      !p.file.path.toLowerCase().includes("archive") &&
      !p.file.path.toLowerCase().includes("templates")
    )
    .file.tasks
    .where(t => !t.completed)
)
```


## [[Day Planning Timeline]]

![[Daily Rituals#Division of a Day]]

### Today's Gcal: Dynamic Calendar View
```dataviewjs
   const {getEvents} = this.app.plugins.plugins["google-calendar"].api
	function date_str_to_hour_min(e) {
		try {
		const ts = e.start.dateTime;
			return ` [ ] ${ts.slice(11,16)} ${e.summary}`;
		} catch(error){
			return ` [ ] 00:00 ${e.summary}`
		}
		
	}
	const fname = dv.current().file.name;
	const file_date = window.moment("07/07/2023 23:59:59");
	
	const file_date2 = window.moment(fname.slice(-8) + " 00:00:00", "YYYYMMDD hh:mm:ss").startOf('day');
	const file_date3 = window.moment(fname.slice(-8) + " 00:00:00", "YYYYMMDD hh:mm:ss").endOf('day');
	
   try{
      const events = await getEvents({
         startDate: file_date2,
         endDate: file_date3
      });
	// console.log(events);
      
      dv.paragraph(dv.markdownList(events.map(e => date_str_to_hour_min(e))));
      } catch(error){
      console.log(error);
   }

```
## Day Planner
### Morning
- [ ] 7:00 Wake up
	- [ ] clean up
	- [ ] morning ritual
- [ ] 7:15 meditate
- [ ] 7:30 eat the frog

### Work Block
- [ ] 9:30 Task 1
- [ ] 17:00 BREAK

### Evening Activities
- [ ] 19:00 Dinner
- [ ] 21:00 Work reflection / next day tasks and journaling
- [ ] 23:00 Sleep
- [ ] 23:00 END

## Tomorrow's Day Plan
```dataviewjs
   const {getEvents} = this.app.plugins.plugins["google-calendar"].api
	function date_str_to_hour_min(e) {
		try {
		const ts = e.start.dateTime;
			return ` [ ] ${ts.slice(11,16)} ${e.summary}`;
		} catch(error){
			return ` [ ] 00:00 ${e.summary}`
		}
		
	}
	const fname = dv.current().file.name;
	const file_date = window.moment("07/07/2023 23:59:59");
	
	const file_date2 = window.moment(fname.slice(-8) + " 00:00:00", "YYYYMMDD hh:mm:ss").add(1, 'days').startOf('day');
	const file_date3 = window.moment(fname.slice(-8) + " 00:00:00", "YYYYMMDD hh:mm:ss").add(1, 'days').endOf('day');
	
   try{
      const events = await getEvents({
         startDate: file_date2,
         endDate: file_date3
      });
	// console.log(events);
      
      dv.paragraph(dv.markdownList(events.map(e => date_str_to_hour_min(e))));
      } catch(error){
      console.log(error);
   }

```
### Morning
- [ ] 7:00 Wake up
- [ ] 

### Work Block
- [ ] 9:30 Task 1

### Evening Activities
- [ ] 19:00 Dinner
- [ ] 21:00 Work reflection / next day tasks and journaling
- [ ] 23:00 Sleep

