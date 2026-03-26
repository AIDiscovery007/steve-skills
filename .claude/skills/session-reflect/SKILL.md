---
name: session-reflect
description: |
  Use when: user says "reflect", "复盘", "/reflect", "review this session", "post-mortem".
  Don't use when: simple Q&A, one-off tasks, or skill optimization (use autoresearch-skill).
  Counter-examples: "what's the weather", "fix this bug", "optimize my skill"
---

# Session Reflection — GRAI + KISS Method

This skill performs deep reflection on the current session using a two-layer model:

1. **GRAI Model**: Deep analysis of what happened
2. **KISS Model**: Actionable next steps

## Workflow

### Step 1: Locate Current Session & Determine Project

Dynamically determine project from current working directory:

```bash
# Get project slug from cwd and construct paths
CWD=$(pwd)
PROJECT_SLUG=$(basename "$CWD")
USER=$(whoami)
MEMORY_DIR="/Users/qiaochao/.claude/projects/-Users-${USER}-${PROJECT_SLUG}/memory"
SESSION_ID=$(ls -t ~/.claude/sessions/*.jsonl 2>/dev/null | head -1 | xargs basename -s .jsonl 2>/dev/null || echo "")

# If no session in ~/.claude/sessions, find in projects subdirs
if [ -z "$SESSION_ID" ]; then
    SESSION_FILE=$(find /Users/qiaochao/.claude/projects -name "*.jsonl" -newer "$MEMORY_DIR" 2>/dev/null | head -1)
else
    SESSION_FILE="/Users/qiaochao/.claude/sessions/${SESSION_ID}.jsonl"
fi
```

If no session file found, ask the user to provide the session file path directly.

**Variables established for later steps**:
- `PROJECT_SLUG` — project name derived from cwd
- `SESSION_ID` — current session UUID
- `MEMORY_DIR` — path to project's memory directory
- `SESSION_FILE` — path to session JSONL file

### Step 2: Read Session Content

Parse the JSONL file and extract the conversation:

```bash
cat <session_file> | python3 -c "
import sys, json
for line in sys.stdin:
    try:
        obj = json.loads(line)
        role = obj.get('role', obj.get('type', ''))
        content = obj.get('content', '')
        if isinstance(content, list):
            content = ' '.join([c.get('text','') for c in content if c.get('type')=='text'])
        if role in ('user', 'assistant'):
            print(f'=== {role.upper()} ===')
            print(content)
            print()
    except: pass
"
```

### Step 3: GRAI Deep Reflection

Analyze the session content using the GRAI model:

**G - Goal**: What was the user's original objective? What were they trying to accomplish?

**R - Result**: What actually happened? What was delivered or accomplished? Did we succeed?

**A - Analysis**: Why did we get these results?
- Key turning points in the conversation
- Critical decisions made
- Obstacles encountered and how they were handled
- What worked well / didn't work

**I - Insight**: What did we learn?
- Patterns that emerged
- Reusable approaches or techniques
- Things to remember for future sessions

### Step 4: KISS Action Items

Based on the reflection, determine next actions:

**KEEP**: What went well that we should continue doing?
- Effective communication approaches
- Good technical decisions
- Useful workflows or habits

**IMPROVE**: What could be done better?
- Areas where we were inefficient
- Communication that could be clearer
- Processes that could be refined

**STOP**: What should we stop doing?
- Approaches that didn't work
- Bad habits to eliminate
- Things that caused friction

**START**: What should we begin doing?
- New approaches worth trying
- Techniques or tools to explore
- Habits to develop

### Step 5: CRUD Operations on MEMORY.md

**Memory file location**: `{MEMORY_DIR}/MEMORY.md` (determined in Step 1)

First, check if this Session ID already exists in MEMORY.md:

```bash
grep -n "Session ID.*<session_id>" MEMORY.md
```

**CRUD Strategy**:

| Session ID exists? | Action | Behavior |
|--------------------|--------|----------|
| **No** | **Create** | Append new reflection entry |
| **Yes** | **Read** | Display existing reflection |
| **Yes** | **Update** | Append new reflection to existing entry |
| **Yes** | **Delete** | Delete existing only (no auto-create) |

**If session exists → Ask user**:
```
Session [ID] already has a reflection. Choose:
1. Read — show existing reflection
2. Update — append new reflection to existing entry
3. Delete — delete existing only (no auto-create)
```

**Format to append (Create/Update)**:

```markdown
## Session Reflection — [DATE]

- **Session ID**: `[session_id_from_filename]`
- **Reflection Time**: [current timestamp]

### GRAI Reflection

#### Goal
[User's original goal or question]

#### Result
[What actually happened / was delivered]

#### Analysis
[Deep analysis with specific examples from the conversation]
- Key turning points: [list]
- Critical decisions: [list]
- What worked: [list]
- What didn't work: [list]

#### Insight
[Key learnings and patterns identified]

### KISS Actions

#### KEEP
- [List items to keep doing]

#### IMPROVE
- [List items to improve]

#### STOP
- [List items to stop doing]

#### START
- [List items to start doing]

---
```

**Delete operation**: Remove the entire `## Session Reflection — [DATE]...---` block for that session ID. Delete only — do not create a new entry.

```markdown
## Session Reflection — [DATE]

- **Session ID**: `[session_id_from_filename]`
- **Reflection Time**: [current timestamp]

### GRAI Reflection

#### Goal
[User's original goal or question]

#### Result
[What actually happened / was delivered]

#### Analysis
[Deep analysis with specific examples from the conversation]
- Key turning points: [list]
- Critical decisions: [list]
- What worked: [list]
- What didn't work: [list]

#### Insight
[Key learnings and patterns identified]

### KISS Actions

#### KEEP
- [List items to keep doing]

#### IMPROVE
- [List items to improve]

#### STOP
- [List items to stop doing]

#### START
- [List items to start doing]

---
```

### Step 6: Confirm Completion

After writing to MEMORY.md, summarize:
- "Reflection complete and saved to MEMORY.md"
- Brief summary of key insights (2-3 bullets)
- Top KISS action item

## Output Format

The final reflection should be:
- **Specific**: Include concrete examples from the session
- **Actionable**: KISS items should be implementable
- **Balanced**: Cover both successes and areas for improvement
- **Concise**: Focus on most important points, not every detail

## Edge Cases

- **Empty session file**: Inform user and suggest they may want to paste session content manually
- **Very short session**: Adjust depth of reflection accordingly — don't force analysis where there's little content
- **Memory file doesn't exist**: Create MEMORY_DIR and MEMORY_FILE with appropriate header before appending
- **Delete last reflection**: If deleting the only reflection, leave MEMORY.md with just headers
- **Concurrent edits**: Not expected in single-user scenario
