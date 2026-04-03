# steve-skills

混合来源的 Claude Code skill 仓库。

- `skills/skent-*`：第一方自研 skill，也是本仓库对外发布的唯一 skill 集合
- `.claude/skills/`：本地兼容层与已安装第三方 skill
- `third_party/registry.json` / `THIRD_PARTY_SKILLS.md`：第三方来源台账
- `.claude-plugin/marketplace.json`：只发布第一方 `skent-*`

## 目录结构

```text
skills/                 # canonical first-party skills
.claude/skills/         # local compatibility + installed third-party skills
.claude-plugin/         # marketplace manifest
third_party/            # provenance registry for external skills
```

## First-Party Skills

| Skill | Description |
|------|-------------|
| `skent-gold-analyst` | 黄金投资分析与仓位建议 |
| `skent-liquidity-report` | 全球流动性日报与宏观传导分析 |
| `skent-html-renderer` | Markdown 报告渲染为 HTML |
| `skent-session-reflect` | Session 复盘与行动建议沉淀 |
| `skent-autotune` | 通用 markdown prompt 优化迭代 |
| `skent-skill-indexer` | 扫描仓库 skill 并维护 registry |
| `skent-skill-orchestrator` | 复杂任务拆解与多技能编排 |

## Third-Party Skills

以下 skill 为外部来源，不纳入本仓库的第一方 marketplace 发布清单：

- `autoresearch`
- `find-skills`
- `frontend-design`
- `git-cleanup`
- `git-commit`
- `nano-banana-2`
- `news-aggregator-skill`

详见 `THIRD_PARTY_SKILLS.md`。

## Compatibility Policy

- 新的 canonical 第一方 skill 一律放在 `skills/skent-*`
- `.claude/skills/` 保留两类内容：
  - 第一方 skill 的本地兼容目录
  - 第三方安装 skill
- 历史旧名如 `gold-analyst`、`liquidity-report`、`html-renderer` 会继续保留，但只作为 legacy alias

## Marketplace

本仓库采用单 plugin 分发，配置位于 `.claude-plugin/marketplace.json`。

发布时只包含：

- `skills/skent-autotune`
- `skills/skent-gold-analyst`
- `skills/skent-html-renderer`
- `skills/skent-liquidity-report`
- `skills/skent-session-reflect`
- `skills/skent-skill-indexer`
- `skills/skent-skill-orchestrator`

## Maintenance Rules

- 新增自研 skill：使用 `skent-` 前缀，并同时更新 `README.md`、`CHANGELOG.md`、`CLAUDE.md`、`marketplace.json`
- 新增第三方 skill：更新 `THIRD_PARTY_SKILLS.md` 与 `third_party/registry.json`，不要加入 marketplace
- `skills-lock.json` 只保留 CLI 安装来源的锁定信息，不作为完整作者声明台账
