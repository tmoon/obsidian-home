---
tags: planner
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

## Daily Reflections
1. 

## Daily Top-line Goals

- [ ] Task 1

### Other Tasks
```dataviewjs 
dv.taskList(dv.pages("#inbox").file.tasks .where(t => !t.completed)) 
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
- [ ] 07:00 Wake up
- [ ] 

### Work Block
- [ ] 10:30 Shahjalal / Tarik: Bi-Weekly 1-1
- [ ] 11:15 Leadership Weekly Sync and Planning
- [ ] 12:30 ❇️ Lunch (via Clockwise)
- [ ] 13:30 Tarik / Daniel 1-1
- [ ] 16:00 Tarik Adnan Moon and Yida Gao

### Evening Activities
- [ ] 19:00 Dinner
- [ ] 20:00 BREAK
- [ ] 21:00 Work reflection / next day tasks and journalin
- [ ] 23:00 Sleep
- [ ] 23:10 END

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
- [x] 07:00 Wake up
- [ ] 

### Work Block
- [x] 09:30 Task 1

### Evening Activities
- [ ] 19:00 Dinner
- [ ] 21:00 Work reflection / next day tasks and journaling
- [ ] 23:00 Sleep

