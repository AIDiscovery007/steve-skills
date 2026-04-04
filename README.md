# steve-skills

一组面向市场分析、报告生成、会话复盘与技能编排的第一方 Claude Code skills。  
First-party Claude Code skills for market analysis, reporting, reflection, and orchestration.

## 安装，使用指南

### 1. 添加 marketplace

```text
/plugin marketplace add https://github.com/AIDiscovery007/steve-skills.git
```

### 2. 安装 plugin

```text
/plugin install skent-skills@skent-skills
```

### 3. 调用 skill

```text
/skent-skills:skent-gold-analyst
/skent-skills:skent-liquidity-report
/skent-skills:skent-session-reflect
```

注意：

- 正确：`/skent-skills:skent-gold-analyst`
- 错误：`/skent-gold-analyst`

如需更新：

```text
/plugin update skent-skills@skent-skills
```

如需重装：

```text
/plugin uninstall skent-skills@skent-skills
/plugin install skent-skills@skent-skills
```

如果你的环境默认走 GitHub SSH，请继续使用 HTTPS 添加 marketplace，不要用 `owner/repo` 简写。

## Skills 列表

- `skent-gold-analyst`：基于宏观指标做黄金分析与交易区间判断。
- `skent-liquidity-report`：生成全球流动性日报并输出结构化分析。
- `skent-html-renderer`：将 Markdown 报告渲染成更适合阅读的 HTML 页面。
- `skent-session-reflect`：复盘 Claude Code 会话并整理后续动作。
- `skent-autotune`：优化 prompt 风格的 Markdown 文档。
- `skent-skill-indexer`：扫描并维护仓库内的 skill 索引信息。
- `skent-skill-orchestrator`：拆解复杂任务并协调多个 skill 共同完成。
