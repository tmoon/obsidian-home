---
tags:
  - moc
  - resource
  - productivity
type: MOC
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

# Productivity Systems MOC

> **Map of Content**: All productivity-related notes, systems, and methodologies in one place.
> This aggregates content from Readwise, articles, books, and personal notes.

---

## Core Methodologies

### Getting Things Done (GTD)
```dataview
LIST
FROM "3 Resource"
WHERE contains(file.name, "Getting Things Done") OR contains(file.tags, "gtd")
```

**Key Principles:**
- Capture everything
- Clarify next actions
- Organize by context
- Reflect weekly
- Engage with trust

### Building a Second Brain (BASB)
**Core System Files:**
- [[CLAUDE]] - System analysis and recommendations
- [[Learn How to Get Stuff Done]] - Personal methodology
- [[Weekly Review Template]] - 30-minute Sunday ritual

**CODE Framework:**
- **Capture**: [[Braindump Inbox]]
- **Organize**: PARA (Projects/Areas/Resources/Archive)
- **Distill**: Progressive summarization
- **Express**: Create deliverables

### Deep Work & Focus
```dataview
LIST
FROM "3 Resource"
WHERE contains(file.content, "deep work") OR contains(file.content, "focus") OR contains(file.content, "concentration")
SORT file.mtime DESC
LIMIT 10
```

---

## Productivity Tools & Techniques

### Time Management
- **Pomodoro Technique**: 25-minute focus blocks
- **Time Blocking**: Schedule deep work in [[Day Planners/]]
- **2-Minute Rule**: If <2min, do it now
- **Eat the Frog**: Hardest task first (7:30 AM daily)

### Task Management
```dataview
LIST
FROM "3 Resource"
WHERE contains(file.content, "task") OR contains(file.content, "todo") OR contains(file.content, "productivity")
SORT file.mtime DESC
LIMIT 10
```

---

## Habits & Routines

### Morning Ritual
From [[Day Planners/]]:
- 7:00 Wake up, clean up
- 7:15 Meditate
- 7:30 Eat the frog (hardest task)

### Weekly Review
Every Sunday, 30 minutes:
- Process inbox to zero
- Review projects
- Plan week ahead

See: [[Weekly Review Template]]

---

## Reading Notes

### Books
```dataview
LIST
FROM "3 Resource/Readwise/Books"
WHERE contains(file.content, "productivity") OR contains(file.content, "habits") OR contains(file.content, "time")
SORT file.mtime DESC
```

### Articles
```dataview
LIST
FROM "3 Resource/Readwise/Articles"
WHERE contains(file.content, "productivity") OR contains(file.content, "focus") OR contains(file.content, "workflow")
SORT file.mtime DESC
LIMIT 15
```

---

## Personal Systems

### Current Workflow
1. **Capture**: Everything goes to [[Braindump Inbox]]
2. **Process**: Weekly review (Sunday 30min)
3. **Execute**: Daily planner with time blocks
4. **Review**: Evening reflection (21:00)

### Active Productivity Projects
```dataview
LIST
FROM "1 Projects"
WHERE contains(file.tags, "project") AND contains(file.content, "productivity")
```

---

## Key Insights & Principles

### From [[My Job As a CEO]]
- CEO role split: Internal operations + External relationships
- Strategic thinking requires dedicated time
- Delegate operational tasks

### From Experience
- System complexity kills execution
- Weekly review is non-negotiable
- One inbox, one dashboard
- Archive aggressively (30-day rule)

---

## Tools & Software

### Current Stack
- **Obsidian**: Second Brain / PKM
- **Dataview**: Automated task aggregation
- **Google Calendar**: Time blocking
- **Day Planners**: Daily execution

---

## Related MOCs

- [[Health Optimization MOC]] - Energy and focus optimization
- [[AI Tools & Prompts MOC]] - AI-assisted productivity
- [[MOC Home]] - Master MOC index

---

## Quick Reference Links

- [[Braindump Inbox]] - Capture point
- [[Dashboard - All Tasks]] - Task overview
- [[Weekly Review Template]] - Maintenance ritual
- [[Generic Project Template]] - Project structure
- [[CLAUDE]] - System critique

---

*This MOC auto-updates via Dataview queries. Add tags and content to your notes to automatically populate these sections.*