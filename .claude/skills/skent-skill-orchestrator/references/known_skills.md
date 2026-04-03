# Known Skills Reference

## First-Party Skills

| 技能名称 | 来源 | 职责说明 | 触发关键词 |
|---------|------|---------|-----------|
| skent-session-reflect | first-party | Session 复盘（GRAI + KISS） | reflect, 复盘, review, session |
| skent-gold-analyst | first-party | 黄金投资分析与仓位建议 | 黄金, gold, 投资 |
| skent-liquidity-report | first-party | 全球流动性日报与宏观传导分析 | 流动性, liquidity, 宏观 |
| skent-html-renderer | first-party | Markdown 报告渲染为 HTML 并自动打开浏览器 | render, HTML, 渲染, 报告 |
| skent-autotune | first-party | 通用 markdown prompt 优化迭代 | autotune, tune, prompt, 优化 |
| skent-skill-indexer | first-party | 扫描本仓库 skill 并维护 registry | 索引, sync skills, 更新索引 |
| skent-skill-orchestrator | first-party | 复杂任务拆解与多技能编排 | orchestrate, 编排, 多步骤 |

## Third-Party Skills

| 技能名称 | 来源 | 职责说明 | 触发关键词 |
|---------|------|---------|-----------|
| autoresearch | third-party | Skill 优化迭代（外部安装） | optimize skill, autoresearch |
| find-skills | third-party | 技能发现安装 | find skill, 查找技能 |
| frontend-design | third-party | 高质量前端界面设计与实现 | 前端, UI, design |
| git-cleanup | third-party | 清理本地 Git 分支 | branch, cleanup, 清理 |
| git-commit | third-party | Git 提交分析 | commit, git提交 |
| nano-banana-2 | third-party | Gemini 图片生成 | 图片, image, 生成 |
| news-aggregator-skill | third-party | 新闻聚合与早报生成 | 新闻, news, 聚合 |

## Legacy Aliases

- `.claude/skills/` 里保留了旧名称兼容层，例如 `session-reflect`、`gold-analyst`、`liquidity-report`、`html-renderer`、`autotune`、`skill-indexer`、`skill-orchestrator`
- 这些旧名称用于本地兼容，不作为 canonical registry 条目，也不会进入 marketplace 发布清单

## 技能发现策略

- **复盘/回顾** → `skent-session-reflect`
- **宏观/投资** → `skent-gold-analyst`, `skent-liquidity-report`
- **报告展示** → `skent-html-renderer`
- **Prompt/Skill 维护** → `skent-autotune`, `skent-skill-indexer`, `find-skills`, `autoresearch`
- **Git** → `git-commit`, `git-cleanup`
- **前端/UI** → `frontend-design`
- **图片生成** → `nano-banana-2`
- **新闻/情报** → `news-aggregator-skill`
- **编排协调** → `skent-skill-orchestrator`

## 动态发现技能

若为完成项目所需的技能不在已知列表内，则使用 `npx skills find [关键词]` 进行动态搜索。

安装第三方技能时：

1. 询问用户安装位置（global 或 project）
2. 更新 `skills-lock.json`（仅记录通过 CLI 安装的技能）
3. 更新 `THIRD_PARTY_SKILLS.md` / `third_party/registry.json`
4. 不要将第三方技能加入 `.claude-plugin/marketplace.json`
