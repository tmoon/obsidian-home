---
tags:
  - moc
  - resource
  - ai
  - llm
type: MOC
---

> **Modified**: `=dateformat(this.file.mtime, "DDDD, HH:mm:ss")`
> **Created**: `=dateformat(this.file.ctime, "DDDD, HH:mm")`

# AI Tools & Prompts MOC

> **Map of Content**: All AI tools, LLM prompts, and AI-assisted workflows.
> Your library of AI productivity multipliers.

---

## AI Productivity Tools

### Current AI Stack

**Active Tools:**
- **Claude Code**: Engineering assistant (this session!)
- **GitHub Copilot**: Code completion ([copilot-instructions.md](../.github/copilot-instructions.md))
- **ChatGPT**: General ideation and research

**Use Cases:**
- Task orchestration and planning
- Code generation and review
- Research and summarization
- Writing and editing
- Data analysis

---

## Prompt Library

### Productivity & Planning Prompts

**From [[Cool LLM Prompts/]]:**
```dataview
LIST
FROM "3 Resource/Cool LLM Prompts"
```

#### Copilot Workflow (from [.github/copilot-instructions.md](../.github/copilot-instructions.md))

**Your Personal Chief of Staff Prompt:**
> You are a productivity-focused task orchestration assistant helping a CEO. You are a world-class therapist and startup coach for high-performance founders, tasked to help me ruthlessly prioritize daily tasks and become extremely productive.

**Key Behaviors:**
- Radical Candor (care deeply, challenge directly)
- Inbox processing with 2-minute rule
- Project clustering and task decomposition
- Time/stress management
- GTD + Deep Work + PARA principles

---

## Useful AI Prompts

### Inbox Processing
```
Process my braindump inbox. For each item:
1. Categorize (2-min task, project, area, reference, someday)
2. Suggest next actions
3. Identify delegation opportunities
4. Flag items not aligned with goals
```

### Project Planning
```
I have a project: [PROJECT NAME]

Help me:
1. Define clear deliverables (intermediate packets)
2. Break into <2min atomic tasks
3. Identify dependencies
4. Estimate effort and timeline
5. Suggest metrics for success
```

### Weekly Review Assistant
```
Review my week. Analyze:
1. Projects: Progress vs. stagnation
2. Inbox: Patterns in uncompleted items
3. Time: Where did energy go?
4. Wins: What shipped?
5. Next week: 3-5 high-leverage priorities
```

### Strategic Thinking
```
I'm facing: [CHALLENGE/DECISION]

Provide:
1. Framework for thinking about this
2. Key questions to answer
3. Pros/cons of each approach
4. What successful founders do
5. Next action to gain clarity
```

---

## AI-Assisted Workflows

### Morning Planning (AI + Human)
1. **AI**: Review calendar, inbox, projects → suggest priorities
2. **Human**: Pick "eat the frog" task
3. **AI**: Break task into steps, identify blockers
4. **Human**: Execute with time blocks

### Research & Learning
1. **AI**: Summarize article/book/paper
2. **Human**: Progressive summarization (bold → highlight)
3. **AI**: Connect to existing knowledge
4. **Human**: Add to relevant MOC

### Content Creation
1. **AI**: Generate outline from rough ideas
2. **Human**: Fill in insights and experience
3. **AI**: Polish and edit
4. **Human**: Final review and personal touch

---

## SignalPilot & Product Development

### Current AI Product Work

**Active Project:** Transitioning from Multiplyr to SignalPilot

From [[Braindump Inbox]]:
- Think through how to close Multiplyr
- How to transition to SignalPilot (new AI product pivot)
- Customer acquisition channels

**AI Product Strategy Prompts:**
```
For SignalPilot (AI product):
1. What are 5 customer acquisition channels?
2. How to position vs. competitors?
3. What features create most value?
4. How to validate market fit quickly?
```

---

## Prompt Engineering Resources

### Learning Resources
```dataview
LIST
FROM "3 Resource/Readwise"
WHERE contains(file.content, "AI") OR contains(file.content, "GPT") OR contains(file.content, "prompt") OR contains(file.content, "LLM")
SORT file.mtime DESC
```

### Prompt Patterns

**Task Decomposition:**
```
Break this into steps a junior engineer could follow:
[TASK]
```

**Rubber Duck Debugging:**
```
I'm stuck on [PROBLEM]. Ask me clarifying questions to help me think through this.
```

**Expert Consultation:**
```
You are a [EXPERT ROLE]. I need advice on [SITUATION]. What would you recommend and why?
```

**Code Review:**
```
Review this code for:
1. Bugs and edge cases
2. Performance issues
3. Readability improvements
4. Security vulnerabilities
```

---

## AI for CEOs & Founders

### Multiplier Use Cases

**From [[My Job As a CEO]]:**

**Internal Operations:**
- Draft investor updates
- Analyze metrics and trends
- Create meeting agendas
- Summarize team discussions

**External Relationships:**
- Research potential partners
- Draft outreach emails
- Prepare pitch materials
- Competitive analysis

### Delegation to AI

**Good for AI:**
- First drafts
- Research and summarization
- Data analysis
- Brainstorming options
- Formatting and structure

**Keep for Human:**
- Final decisions
- Relationship building
- Strategic vision
- Creative breakthroughs
- Empathy and emotion

---

## GitHub Copilot Setup

**Current Configuration:** [.github/copilot-instructions.md](../.github/copilot-instructions.md)

**Principles:**
- Task orchestration focus
- Radical Candor approach
- Inbox processing workflow
- Project clustering
- Daily planning with deep work

**Applied To:** All Markdown files (`**/*.md`)

---

## AI Tools Comparison

### When to Use What

**Claude Code:**
- Complex multi-file changes
- System design and architecture
- Detailed explanations
- Research and analysis

**GitHub Copilot:**
- Inline code completion
- Quick edits in editor
- Pattern-based suggestions
- Markdown note assistance

**ChatGPT:**
- Quick brainstorming
- General questions
- Image analysis
- Web browsing

---

## Future AI Experiments

### To Explore
- [ ] Voice-to-text for inbox capture
- [ ] AI-powered meeting summaries
- [ ] Automated weekly review insights
- [ ] Smart task prioritization
- [ ] AI reading assistant for Readwise

### Projects
```dataview
LIST
FROM "1 Projects"
WHERE contains(file.tags, "project") AND (contains(file.content, "AI") OR contains(file.content, "automation"))
```

---

## Related MOCs

- [[Productivity Systems MOC]] - AI as productivity multiplier
- [[4 Archive/ChatGPT Learning/]] - Early AI experiments
- [[Cool LLM Prompts/]] - Curated prompt library

---

## Key Insights

### AI Principles for Founders

1. **AI amplifies, doesn't replace**: Use for leverage, not abdication
2. **Iterate on prompts**: Good prompts = good outputs
3. **Context is king**: More context = better results
4. **Verify everything**: AI assists, human validates
5. **Build prompt library**: Reuse what works

### Productivity Multipliers

- AI drafts → Human edits (10x faster than blank page)
- AI research → Human synthesis (compress hours to minutes)
- AI brainstorm → Human decides (more options, better choices)
- AI structure → Human insights (better organization)

---

*This MOC aggregates AI-related content. As you experiment with new prompts and tools, add them here for future reference.*