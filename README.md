# steve-skills

<div align="center">

First-party Claude Code skills for market analysis, reporting, reflection, and orchestration.

[![GitHub stars](https://img.shields.io/github/stars/AIDiscovery007/steve-skills?style=flat-square)](https://github.com/AIDiscovery007/steve-skills/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/AIDiscovery007/steve-skills?style=flat-square)](https://github.com/AIDiscovery007/steve-skills/commits/main)

</div>

`steve-skills` is a mixed-origin Claude Code skills repository.

- `skills/skent-*` contains the first-party skills published by this repo
- `.claude/skills/` keeps compatibility aliases and installed third-party skills
- third-party provenance is documented instead of being mixed into the marketplace

## Install

### 1. Add the marketplace

```text
/plugin marketplace add https://github.com/AIDiscovery007/steve-skills.git
```

### 2. Install the plugin

```text
/plugin install skent-skills@skent-skills
```

### 3. Run a skill

```text
/skent-skills:skent-gold-analyst
/skent-skills:skent-liquidity-report
/skent-skills:skent-session-reflect
```

Use the namespaced form:

- correct: `/skent-skills:skent-gold-analyst`
- incorrect: `/skent-gold-analyst`

## Included Skills

| Skill | Purpose |
|------|---------|
| `skent-gold-analyst` | Gold analysis with macro indicators and trading levels |
| `skent-liquidity-report` | Global liquidity report generation |
| `skent-html-renderer` | Render Markdown reports as polished HTML |
| `skent-session-reflect` | Reflect on a Claude Code session and extract follow-ups |
| `skent-autotune` | Tune prompt-style Markdown documents |
| `skent-skill-indexer` | Index skills and maintain registry metadata |
| `skent-skill-orchestrator` | Coordinate multi-step tasks across skills |

## Example Prompts

### Gold

```text
/skent-skills:skent-gold-analyst
Help me analyze gold. Is this a buy now or a wait-for-pullback setup?
```

### Liquidity

```text
/skent-skills:skent-liquidity-report
Generate today's global liquidity report.
```

### HTML

```text
/skent-skills:skent-html-renderer
Render this Markdown report as HTML and open it.
```

### Reflection

```text
/skent-skills:skent-session-reflect
Reflect on this session and summarize next actions.
```

## Update

```text
/plugin update skent-skills@skent-skills
```

If something looks off, reinstall:

```text
/plugin uninstall skent-skills@skent-skills
/plugin install skent-skills@skent-skills
```

## Troubleshooting

### SSH authentication failed

If `owner/repo` resolves to GitHub SSH in your environment, use HTTPS instead:

```text
/plugin marketplace add https://github.com/AIDiscovery007/steve-skills.git
```

### Plugin installed, but no skills appear

1. Run `/plugin update skent-skills@skent-skills`
2. If needed, reinstall the plugin
3. Test with `/skent-skills:skent-session-reflect`

### Two `/plugin` commands were pasted together

Run them separately:

```text
/plugin marketplace add https://github.com/AIDiscovery007/steve-skills.git
/plugin install skent-skills@skent-skills
```

## Repository Layout

```text
skills/                 # canonical first-party skills
.claude/skills/         # compatibility aliases + installed third-party skills
.claude-plugin/         # plugin and marketplace manifests
third_party/            # provenance registry for external skills
```

## Third-Party Transparency

This repository also keeps some external skills for local workflows, but they are not published as first-party plugin content.

Current third-party skills:

- `autoresearch`
- `find-skills`
- `frontend-design`
- `git-cleanup`
- `git-commit`
- `nano-banana-2`
- `news-aggregator-skill`

See `THIRD_PARTY_SKILLS.md` for provenance details.

## For Maintainers

User-facing content stays in `README.md`.

Maintainer-focused publishing workflow, version sync rules, validation steps, and failure cases live in:

- `docs/plugin-publishing-knowhow.md`
- `CLAUDE.md`
