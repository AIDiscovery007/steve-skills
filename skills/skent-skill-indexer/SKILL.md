---
name: skent-skill-indexer
description: 更新 steve-skills 的 skill registry 与 marketplace 清单。当需要同步 skills 列表、整理来源分类或维护 first-party/third-party 边界时使用。
version: 0.1.0
---

# skent-skill-indexer

同步和维护 `skent-skill-orchestrator` 的 `known_skills.md` 文档。

## Base Directory

- `{baseDir}` = 当前 `SKILL.md` 所在目录
- 扫描脚本路径：`python3 {baseDir}/scripts/scan_skills.py`

## 工作流程

### 1. 扫描 Skills

运行 `python3 {baseDir}/scripts/scan_skills.py` 获取仓库内的 canonical skill 与兼容层 skill：

- 优先扫描 `skills/` 下的 first-party `skent-*`
- 再扫描 `.claude/skills/` 下的第三方技能与兼容层
- 自动跳过带 `legacy_alias_of` frontmatter 的旧别名 skill

### 2. 分析变化

对比扫描结果与当前 known_skills.md：
- **新增**: 扫描到但未在列表中
- **删除**: 列表中有但扫描不到

### 3. 人工更新 known_skills.md

由我根据扫描结果人工编辑 `references/known_skills.md`：

**职责说明规则**：
- 中文为主，50字内
- 翻译或精简英文 description
- 保持简洁风格

**格式**：
| 技能名称 | 来源 | 职责说明 | 触发关键词 |
|---------|------|---------|-----------|

**分类策略**：观察 skill 功能后归类

## 使用场景

- 用户说"同步 skills" / "更新 known_skills"
- 发现某个 skill 分类不合理
- 调整 first-party / third-party 边界或 marketplace 发布清单
