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

## Adding New Skills

AFTER installing and creating new skills:

1. Request installation location: global (-g) vs project-only
2. Add to `skills-lock.json` for tracking
3. IMPORTANT: USE MUST use `skill-indexer` skill to Update `known_skills.md` table and categories
