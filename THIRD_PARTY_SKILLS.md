# Third-Party Skills

以下 skill 为外部来源，不属于 `steve-skills` 的第一方原创 skill。

它们保留在当前仓库中是为了本地工作流兼容、研究、或协同使用。

## Policy

- 不进入 `.claude-plugin/marketplace.json`
- 不改名为 `skent-*`
- 在 README、registry 和索引里明确标记为 third-party

## Registry

| Skill | Current Path | Upstream | Notes |
|------|--------------|----------|-------|
| `autoresearch` | `.claude/skills/autoresearch-skill/` | `github/awesome-copilot@autoresearch` | 依据 `npx skills find autoresearch` 的优先 registry 结果记录 |
| `find-skills` | `.claude/skills/find-skills/` | `vercel-labs/skills@find-skills` | 已在 `skills-lock.json` 锁定 |
| `frontend-design` | `.claude/skills/frontend-design/` | `anthropics/skills@frontend-design` | 已在 `skills-lock.json` 锁定 |
| `git-cleanup` | `.claude/skills/git-cleanup/` | `trailofbits/skills@git-cleanup` | 已在 `skills-lock.json` 锁定 |
| `git-commit` | `.claude/skills/git-commit/` | `github/awesome-copilot@git-commit` | 已在 `skills-lock.json` 锁定 |
| `nano-banana-2` | `.claude/skills/nano-banana-2/` | `inferen-sh/skills@nano-banana-2` | 已在 `skills-lock.json` 锁定 |
| `news-aggregator-skill` | `.claude/skills/news-aggregator-skill/` | `cclank/news-aggregator-skill@news-aggregator-skill` | 目录内 README 直接指向上游仓库 |

机器可读版本见 `third_party/registry.json`。
