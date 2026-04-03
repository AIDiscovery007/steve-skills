# steve-skills

<div align="center">

First-party Claude Code skills for market analysis, reporting, reflection, and orchestration.  
面向市场分析、报告生成、会话复盘与技能编排的第一方 Claude Code skills。

[![GitHub stars](https://img.shields.io/github/stars/AIDiscovery007/steve-skills?style=flat-square)](https://github.com/AIDiscovery007/steve-skills/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/AIDiscovery007/steve-skills?style=flat-square)](https://github.com/AIDiscovery007/steve-skills/commits/main)

</div>

`steve-skills` is a mixed-origin Claude Code skills repository.  
`steve-skills` 是一个混合来源的 Claude Code skills 仓库。

- `skills/skent-*` contains the first-party skills published by this repo  
  `skills/skent-*` 是本仓库对外发布的第一方 skills
- `.claude/skills/` keeps compatibility aliases and installed third-party skills  
  `.claude/skills/` 保留兼容别名与已安装第三方 skills
- third-party provenance is documented instead of being mixed into the marketplace  
  第三方来源会被明确标注，而不是混进第一方 marketplace

## Install / 安装

### 1. Add the marketplace / 添加 marketplace

```text
/plugin marketplace add https://github.com/AIDiscovery007/steve-skills.git
```

### 2. Install the plugin / 安装 plugin

```text
/plugin install skent-skills@skent-skills
```

### 3. Run a skill / 调用 skill

```text
/skent-skills:skent-gold-analyst
/skent-skills:skent-liquidity-report
/skent-skills:skent-session-reflect
```

Use the namespaced form.  
请使用带命名空间的调用方式。

- correct / 正确: `/skent-skills:skent-gold-analyst`
- incorrect / 错误: `/skent-gold-analyst`

## Included Skills / 内置技能

| Skill | Purpose | 用途 |
|------|---------|------|
| `skent-gold-analyst` | Gold analysis with macro indicators and trading levels | 黄金分析与交易区间判断 |
| `skent-liquidity-report` | Global liquidity report generation | 全球流动性日报生成 |
| `skent-html-renderer` | Render Markdown reports as polished HTML | 将 Markdown 报告渲染为 HTML |
| `skent-session-reflect` | Reflect on a Claude Code session and extract follow-ups | 复盘会话并沉淀后续动作 |
| `skent-autotune` | Tune prompt-style Markdown documents | 优化 prompt 类 Markdown 文档 |
| `skent-skill-indexer` | Index skills and maintain registry metadata | 维护技能索引与元数据 |
| `skent-skill-orchestrator` | Coordinate multi-step tasks across skills | 编排多步骤、多技能任务 |

## Example Prompts / 示例

### Gold / 黄金分析

```text
/skent-skills:skent-gold-analyst
帮我分析一下黄金，现在是直接买，还是等回调更合适？
```

### Liquidity / 流动性报告

```text
/skent-skills:skent-liquidity-report
生成今天的全球流动性日报。
```

### HTML / 报告渲染

```text
/skent-skills:skent-html-renderer
把这份 Markdown 报告渲染成 HTML 并打开。
```

### Reflection / 会话复盘

```text
/skent-skills:skent-session-reflect
复盘一下这次会话，并整理后续待办。
```

## Update / 更新

```text
/plugin update skent-skills@skent-skills
```

If something looks off, reinstall:  
如果有异常，可以直接重装：

```text
/plugin uninstall skent-skills@skent-skills
/plugin install skent-skills@skent-skills
```

## Troubleshooting / 常见问题

### SSH authentication failed / SSH 认证失败

If `owner/repo` resolves to GitHub SSH in your environment, use HTTPS instead.  
如果你的环境把 `owner/repo` 解析成 GitHub SSH，请改用 HTTPS。

```text
/plugin marketplace add https://github.com/AIDiscovery007/steve-skills.git
```

### Plugin installed, but no skills appear / plugin 装好了但没有 skills

1. Run `/plugin update skent-skills@skent-skills`  
   先执行 `/plugin update skent-skills@skent-skills`
2. If needed, reinstall the plugin  
   不行就重装 plugin
3. Test with `/skent-skills:skent-session-reflect`  
   再用 `/skent-skills:skent-session-reflect` 测试

### Two `/plugin` commands were pasted together / 两条命令粘在了一起

Run them separately.  
请一条一条执行。

```text
/plugin marketplace add https://github.com/AIDiscovery007/steve-skills.git
/plugin install skent-skills@skent-skills
```

## Repository Layout / 仓库结构

```text
skills/                 # canonical first-party skills
.claude/skills/         # compatibility aliases + installed third-party skills
.claude-plugin/         # plugin and marketplace manifests
third_party/            # provenance registry for external skills
```

## Third-Party Transparency / 第三方来源说明

This repository also keeps some external skills for local workflows, but they are not published as first-party plugin content.  
仓库中也保留了一些第三方 skills 供本地工作流使用，但它们不会作为第一方 plugin 内容发布。

Current third-party skills / 当前第三方 skills:

- `autoresearch`
- `find-skills`
- `frontend-design`
- `git-cleanup`
- `git-commit`
- `nano-banana-2`
- `news-aggregator-skill`

See `THIRD_PARTY_SKILLS.md` for provenance details.  
详细来源见 `THIRD_PARTY_SKILLS.md`。

## For Maintainers / 维护者说明

User-facing content stays in `README.md`.  
面向用户的内容放在 `README.md`。

Maintainer-focused publishing workflow, version sync rules, validation steps, and failure cases live in:  
面向维护者的发布流程、版本同步、验证步骤和故障排查见：

- `docs/plugin-publishing-knowhow.md`
- `CLAUDE.md`
