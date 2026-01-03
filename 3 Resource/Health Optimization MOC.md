---
tags:
  - moc
  - resource
  - health
type: MOC
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

# Health Optimization MOC

> **Map of Content**: All health, wellness, and performance optimization notes.
> Aggregates research from Readwise, personal experiments, and protocols.

---

## Core Health Areas

### Physical Health
```dataview
LIST
FROM "3 Resource/Readwise"
WHERE contains(file.content, "exercise") OR contains(file.content, "fitness") OR contains(file.content, "workout") OR contains(file.content, "strength")
SORT file.mtime DESC
LIMIT 10
```

### Mental Health & Cognition
```dataview
LIST
FROM "3 Resource/Readwise"
WHERE contains(file.content, "mental") OR contains(file.content, "cognitive") OR contains(file.content, "brain") OR contains(file.content, "memory")
SORT file.mtime DESC
LIMIT 10
```

### Sleep Optimization
```dataview
LIST
FROM "3 Resource/Readwise"
WHERE contains(file.content, "sleep") OR contains(file.content, "rest") OR contains(file.content, "recovery")
SORT file.mtime DESC
LIMIT 10
```

---

## Nutrition & Supplements

### Diet & Nutrition
```dataview
LIST
FROM "3 Resource/Readwise"
WHERE contains(file.content, "nutrition") OR contains(file.content, "diet") OR contains(file.content, "food") OR contains(file.content, "eating")
SORT file.mtime DESC
LIMIT 10
```

### Supplements & Nootropics
```dataview
LIST
FROM "3 Resource/Readwise"
WHERE contains(file.content, "supplement") OR contains(file.content, "nootropic") OR contains(file.content, "vitamin") OR contains(file.content, "plant")
SORT file.mtime DESC
LIMIT 10
```

---

## Performance & Energy

### ADHD & Focus
```dataview
LIST
FROM "3 Resource/Readwise"
WHERE contains(file.content, "ADHD") OR contains(file.content, "attention") OR contains(file.content, "focus")
SORT file.mtime DESC
```

### Energy Management
- **Morning Routine**: Meditation (7:15 AM), Eat the Frog (7:30 AM)
- **Work Blocks**: 25-minute Pomodoros with breaks
- **Recovery**: Evening reflection (21:00)

```dataview
LIST
FROM "3 Resource/Readwise"
WHERE contains(file.content, "energy") OR contains(file.content, "fatigue") OR contains(file.content, "stamina")
SORT file.mtime DESC
LIMIT 10
```

---

## Habits & Behavior Change

### Building Habits
```dataview
LIST
FROM "3 Resource/Readwise"
WHERE contains(file.content, "habit") OR contains(file.content, "behavior") OR contains(file.content, "routine")
SORT file.mtime DESC
LIMIT 10
```

### Stress Management
```dataview
LIST
FROM "3 Resource/Readwise"
WHERE contains(file.content, "stress") OR contains(file.content, "anxiety") OR contains(file.content, "calm")
SORT file.mtime DESC
LIMIT 10
```

---

## Daily Health Practices

### Morning (7:00 - 9:30)
- Wake up & clean up
- **7:15**: Meditate
- **7:30**: Eat the frog (cognitive peak)
- Healthy breakfast

### Throughout Day
- Pomodoro breaks (movement, hydration)
- Lunch (mindful eating)
- Afternoon walk/movement
- Limit caffeine after 2 PM

### Evening (19:00 - 23:00)
- **19:00**: Dinner
- **21:00**: Reflection & journaling
- Wind-down routine
- **23:00**: Sleep

From: [[Day Planners/]]

---

## Health Tracking & Projects

### Active Health Projects
```dataview
LIST
FROM "1 Projects"
WHERE contains(file.tags, "project") AND (contains(file.content, "health") OR contains(file.content, "fitness") OR contains(file.content, "wellness"))
```

### Health Area Notes
See: [[2 Areas/1 Health and Wealth/]]

---

## Research & Articles

### General Health
```dataview
LIST
FROM "3 Resource/Readwise/Articles"
WHERE contains(file.content, "health") OR contains(file.content, "wellness")
SORT file.mtime DESC
LIMIT 15
```

### Books
```dataview
LIST
FROM "3 Resource/Readwise/Books"
WHERE contains(file.content, "health") OR contains(file.content, "body") OR contains(file.content, "mind")
SORT file.mtime DESC
```

### Podcasts
```dataview
LIST
FROM "3 Resource/Readwise/Podcasts"
WHERE contains(file.content, "health") OR contains(file.content, "performance")
SORT file.mtime DESC
```

---

## Key Principles

### CEO Health as Foundation
From [[My Job As a CEO]]:
- Peak performance requires peak health
- Energy management > Time management
- Recovery is as important as work

### Optimization Stack
1. **Sleep**: 7-8 hours (23:00 - 7:00)
2. **Nutrition**: Whole foods, mindful eating
3. **Movement**: Daily activity, strength training
4. **Stress**: Meditation, reflection, boundaries
5. **Social**: Connection and relationships

---

## Related MOCs

- [[Productivity Systems MOC]] - Energy enables productivity
- [[2 Areas/1 Health and Wealth/]] - Active health area
- [[2 Areas/2 Cooking/]] - Nutrition and meal prep

---

## Quick Actions

- [ ] Schedule weekly workout sessions
- [ ] Track sleep quality
- [ ] Experiment with new morning routine
- [ ] Review supplement stack
- [ ] Book annual physical

---

*This MOC auto-updates via Dataview queries. Add health-related content to your Readwise imports or notes to populate automatically.*