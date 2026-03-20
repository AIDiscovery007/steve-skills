# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a personal Claude Code skills repository (`steve-skills`). It contains installed skills that extend Claude's capabilities for investment analysis, git workflows, image generation, news aggregation, and skill development.

## Installed Skills

Skills are installed in `.claude/skills/`. See `skill-orchestrator/references/known_skills.md` for the registry.

## Common Commands

```bash
# 安装新 skill
npx skills add <package> [-g] -y

# 搜索可用 skills
npx skills find <keyword>
```

## Architecture

- `skill-orchestrator/` - 主编排器，维护 known_skills.md 作为技能注册表
- `skill-indexer/` - 用于同步和维护 known_skills.md
- Skills communicate via skill-orchestrator for multi-step tasks

## Workflow

### Complexity Analysis
After receiving the user's prompt, ALWAYS analyze its complexity first.

**MUST invoke `skill-orchestrator/` when:**
- User asks to "完成XX任务" / "实现YY效果" without specifying how
- Problem requires multiple skills or tools working together
- User says "需要多种工具" / "不确定怎么做"
- Task spans multiple domains (e.g., git + analysis + news)
- Any multi-step problem that cannot be answered in one response

**Single-step tasks (do NOT over-engineer):**
- Simple code edits, typo fixes, file reads
- Questions that have direct answers
- One specific tool/skill can solve it directly

### Skill Invocation
- Use `/skill-name` format to invoke skills directly
- Skills are listed in `skill-orchestrator/references/known_skills.md`

## Adding New Skills

**AFTER installing and creating new skills, you MUST follow these 3 steps in order:**

1. **Request location** — Ask user: global (`-g`) or project-only?
2. **Lock it** — Add to `skills-lock.json` for tracking
3. **Index it** — Use `/skill-indexer` to update `known_skills.md` table and categories
4. **Ignore it** — Add skill output directories to `.gitignore` (e.g., `autotune-*/`, `autoresearch-*/`, `reports/`, `output/`)
