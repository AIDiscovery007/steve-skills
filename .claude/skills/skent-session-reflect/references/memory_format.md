# MEMORY.md Format Reference

This document defines the structure for session reflections stored in MEMORY.md.

## File Location

```
/Users/qiaochao/.claude/projects/-Users-qiaochao-steve-skills/memory/MEMORY.md
```

## Overall Structure

```markdown
# Project Memory — steve-skills

## Session Reflections

[Individual session reflections appended here, newest first]

---

## Project Patterns

[Optional: Cross-session patterns and learnings accumulated over time]

---

## User Preferences

[Optional: Known user preferences and working style]
```

## Individual Session Entry Format

```markdown
## Session Reflection — YYYY-MM-DD

- **Session ID**: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- **Reflection Time**: YYYY-MM-DD HH:MM CST

### GRAI Reflection

#### Goal
What the user was trying to accomplish.

#### Result
What actually happened — deliverables, outcomes, decisions made.

#### Analysis
Why the results happened:
- Key turning points
- Critical decisions
- What worked / didn't work
- Challenges faced and how addressed

#### Insight
Patterns identified, learnings, things to remember.

### KISS Actions

#### KEEP
- Things that went well and should continue

#### IMPROVE
- Things that could be better next time

#### STOP
- Things that should be discontinued

#### START
- New things to try in future sessions

---
```

## Guidelines

1. **Date format**: Use YYYY-MM-DD for consistency
2. **Session ID**: Extract from the JSONL filename (format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.jsonl`)
3. **Timezone**: Use CST (China Standard Time) as default
4. **Separators**: Use `---` to separate individual reflection entries
5. **Deduplication**: Check for existing entry with same Session ID before appending

## Example Entry

```markdown
## Session Reflection — 2026-03-25

- **Session ID**: `38f33e9e-6dd9-4d1f-ab30-910201c770de`
- **Reflection Time**: 2026-03-25 14:30 CST

### GRAI Reflection

#### Goal
User wanted to create a session reflection skill using GRAI + KISS models.

#### Result
Successfully designed and implemented session-reflect skill with:
- GRAI deep reflection framework
- KISS action item framework
- MEMORY.md integration for long-term storage

#### Analysis
- Key decision: Used project-level installation for memory specificity
- Chose simple /reflect trigger for user control
- Session content accessed via JSONL file parsing

#### Insight
GRAI + KISS provides good balance between analysis depth and actionable output.
Two-layer model (reflection + action) helps extract both learnings and next steps.

### KISS Actions

#### KEEP
- Breaking complex skills into GRAI + KISS两层模型
- Writing specific examples rather than generic instructions
- Project-level memory for user-specific context

#### IMPROVE
- Could add support for selective message range reflection
- Could provide quick summary option for short sessions

#### STOP
- Over-engineering the skill structure before validating with user

#### START
- Consider adding visual dashboard for reflection history
- Explore automatic session summary at day end

---
```
