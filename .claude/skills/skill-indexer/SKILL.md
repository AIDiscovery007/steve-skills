---
name: skill-indexer
description: 更新 orchestrator 的 known_skills.md。当需要同步 skills 列表、整理 skill 分类时使用。
---

# Skill Indexer

同步和维护 orchestrator-skill 的 known_skills.md 文档。

## 工作流程

### 1. 扫描 Skills

运行 `python scripts/scan_skills.py` 获取所有已安装 skill 的 name 和 description。

### 2. 分析变化

对比扫描结果与当前 known_skills.md：
- **新增**: 扫描到但未在列表中
- **删除**: 列表中有但扫描不到

### 3. 人工更新 known_skills.md

由我根据扫描结果人工编辑 known_skills.md：

**职责说明规则**：
- 中文为主，50字内
- 翻译或精简英文 description
- 保持简洁风格

**格式**：
| 技能名称 | 职责说明 | 触发关键词 |
|---------|---------|-----------|

**分类策略**：观察 skill 功能后归类

## 使用场景

- 用户说"同步 skills" / "更新 known_skills"
- 发现某个 skill 分类不合理
