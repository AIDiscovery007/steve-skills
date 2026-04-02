# Known Skills Reference

## 已安装技能

| 技能名称 | 职责说明 | 触发关键词 |
|---------|---------|-----------|
| session-reflect | Session 复盘（GRAI + KISS）| reflect, 复盘, review, session, /reflect |
| git-commit | Git 提交分析 | commit, git提交 |
| git-cleanup | 清理本地 Git 分支 | branch, cleanup, 清理 |
| gold-analyst | 黄金投资分析 | 黄金, gold, 投资 |
| liquidity-report | 全球流动性日报 | 流动性, liquidity |
| nano-banana-2 | Gemini 图片生成 | 图片, image, 生成 |
| news-aggregator-skill | 新闻聚合 | 新闻, news, 聚合 |
| find-skills | 技能发现安装 | find skill, 查找技能 |
| frontend-design | 高质量前端界面设计与实现 | 前端, UI, design |
| html-renderer | Markdown 报告渲染为精美 HTML 并自动打开浏览器 | render, HTML, 渲染, 美化报告 |
| autotune | 通用 prompt 优化迭代（任何 .md 文档） | optimize prompt, tune, autotune, 优化 prompt |
| autoresearch | Skill 优化迭代（仅限 SKILL.md） | optimize skill, autoresearch, 优化技能 |
| skill-orchestrator | 复杂任务拆解与多技能编排 | orchestrate, 编排, 多步骤 |
| skill-indexer | 同步维护 known_skills.md | 同步 skills, 更新索引 |

## 技能发现策略

- **投资相关** → gold-analyst, liquidity-report
- **代码/Git** → git-commit, git-cleanup
- **前端/UI** → frontend-design, html-renderer
- **图片生成** → nano-banana-2
- **新闻/情报** → news-aggregator-skill
- **技能安装与维护** → find-skills, skill-indexer, autoresearch, autotune
- **编排协调** → skill-orchestrator

## 动态发现技能

若为完成项目所需的技能不在已安装技能内，则使用 `npx skills find [关键词]` 进行动态搜索：

当需要安装新技能时，询问用户安装位置：
- **global (-g)**: 所有项目可用
- **project**: 仅当前项目可用

安装命令：`npx skills add <package> --skill <skill-name> [-g] -y`
