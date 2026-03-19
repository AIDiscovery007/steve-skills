# Known Skills Reference

## 已安装技能

| 技能名称 | 职责说明 | 触发关键词 |
|---------|---------|-----------|
| git-commit | Git提交分析 | commit, git提交 |
| gold-analyst | 黄金投资分析 | 黄金, gold, 投资分析 |
| liquidity-report | 全球流动性日报 | 流动性, liquidity, 市场分析 |
| nano-banana-2 | 图片生成 | 图片, 生成图片, image |
| news-aggregator-skill | 新闻聚合 | 新闻, news, 聚合 |
| find-skills | 技能发现 | 查找技能, find skill |
| skill-creator | 技能创建 | 创建技能, create skill |
| autoresearch-skill | 技能优化 | 优化技能, improve skill |

## 技能发现策略

- **投资相关** → gold-analyst, liquidity-report
- **代码/Git相关** → git-commit, git-cleanup
- **图片生成** → nano-banana-2
- **新闻/情报** → news-aggregator-skill
- **创建/优化技能** → skill-creator, autoresearch-skill

## 动态发现

使用 `npx skills find [关键词]` 进行动态搜索。

当需要安装新技能时，询问用户安装位置：
- **global (-g)**: 所有项目可用
- **project**: 仅当前项目可用

安装命令：`npx skills add <package> [-g] -y`
