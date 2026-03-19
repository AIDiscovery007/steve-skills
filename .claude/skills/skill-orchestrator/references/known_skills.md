# Known Skills Reference

## 已安装技能

| 技能名称 | 职责说明 | 触发关键词 |
|---------|---------|-----------|
| git-commit | Git 提交分析 | commit, git提交 |
| git-cleanup | 清理本地 Git 分支 | branch, cleanup, 清理 |
| gold-analyst | 黄金投资分析 | 黄金, gold, 投资 |
| liquidity-report | 全球流动性日报 | 流动性, liquidity |
| nano-banana-2 | Gemini 图片生成 | 图片, image, 生成 |
| news-aggregator-skill | 新闻聚合 | 新闻, news, 聚合 |
| find-skills | 技能发现安装 | find skill, 查找技能 |
| skill-creator | 创建新 skill | create skill, 创建技能 |
| autoresearch | Skill 优化迭代 | optimize, improve, 优化 |
| skill-orchestrator | 多技能编排协调 | 复杂任务, 编排, 协调 |

## 技能发现策略

- **投资相关** → gold-analyst, liquidity-report
- **代码/Git** → git-commit, git-cleanup
- **图片生成** → nano-banana-2
- **新闻/情报** → news-aggregator-skill
- **技能创建** → skill-creator, find-skills, autoresearch
- **编排协调** → skill-orchestrator

## 动态发现

使用 `npx skills find [关键词]` 进行动态搜索：

当需要安装新技能时，询问用户安装位置：
- **global (-g)**: 所有项目可用
- **project**: 仅当前项目可用

安装命令：`npx skills add <package> [-g] -y`
