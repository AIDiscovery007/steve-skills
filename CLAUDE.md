# CLAUDE.md

## Repository Purpose

`steve-skills` 是一个混合来源的 Claude Code skills 仓库。

- 第一方自研 skill 放在 `skills/skent-*`
- `.claude/skills/` 保留本地兼容层与第三方安装 skill
- 第三方来源通过 `THIRD_PARTY_SKILLS.md` 和 `third_party/registry.json` 明确标注

## Documentation Policy

- `README.md` 面向仓库外部用户，优先写仓库介绍、安装方式、使用教程、常见问题
- 维护者发布流程、内部规则、故障排查 know-how 优先写入 `docs/` 和 `CLAUDE.md`

## Canonical Layout

```text
skills/                 # canonical first-party skills only
.claude/skills/         # local compatibility + third-party installed skills
.claude-plugin/         # marketplace manifest
third_party/            # provenance registry for external skills
```

## Naming Rules

- 所有第一方 skill 必须使用 `skent-` 前缀
- 历史旧名只允许作为 `.claude/skills/` 下的 legacy alias 保留
- 第三方 skill 保持上游名称，不改成 `skent-*`

## Publishing Rules

- `.claude-plugin/marketplace.json` 只包含 `skills/skent-*`
- `.claude-plugin/plugin.json` 必须存在；缺失时 plugin 可能能安装但 skills 不会注册
- 第三方 skill 绝不进入 marketplace
- 发布时同步更新 `.claude-plugin/plugin.json`、`.claude-plugin/marketplace.json` 中的版本号
- 新增第一方 skill 后，必须同步更新：
  - `README.md`
  - `CHANGELOG.md`
  - `.claude-plugin/marketplace.json`
  - `skills/skent-skill-orchestrator/references/known_skills.md`
- 详细发布流程与故障排查见 `docs/plugin-publishing-knowhow.md`

## First-Party Skills

- `skent-session-reflect`
- `skent-gold-analyst`
- `skent-liquidity-report`
- `skent-html-renderer`
- `skent-autotune`
- `skent-skill-indexer`
- `skent-skill-orchestrator`

## Third-Party Skills

当前明确视为第三方的 skill：

- `autoresearch`
- `find-skills`
- `frontend-design`
- `git-cleanup`
- `git-commit`
- `nano-banana-2`
- `news-aggregator-skill`

## Maintenance Workflow

### Adding a First-Party Skill

1. 在 `skills/skent-<name>/` 创建 canonical skill
2. 如需本地兼容，在 `.claude/skills/` 增加对应目录
3. 更新 marketplace、README、CHANGELOG、known_skills

### Adding a Third-Party Skill

1. 询问安装位置：global 或 project
2. 如果通过 CLI 安装，更新 `skills-lock.json`
3. 更新 `THIRD_PARTY_SKILLS.md` 和 `third_party/registry.json`
4. 不要将该 skill 加入 marketplace

## Indexing and Discovery

- `skent-skill-indexer` 优先扫描 `skills/`，再扫描 `.claude/skills/`
- 带 `legacy_alias_of` frontmatter 的 skill 会被视为兼容别名并从 canonical registry 中排除
- `skent-skill-orchestrator` 的已知技能表位于 `skills/skent-skill-orchestrator/references/known_skills.md`
- 已安装 plugin skill 默认使用 `/skent-skills:<skill-name>` 这种 namespaced 调用方式

## Third-Party Install Checklist

1. **Request location** — For external installs, ask user: global (`-g`) or project-only?
2. **Lock it** — Add externally installed skills to `skills-lock.json` for tracking
3. **Index it** — Use `/skill-indexer` to update `known_skills.md` table and categories
4. **Ignore it** — Add skill output directories to `.gitignore` (e.g., `autotune-*/`, `autoresearch-*/`, `reports/`, `output/`)

## Compact Instructions

When auto compaction triggers, preserve the following in this priority order:

1. **Project architecture information** — must never be compacted or lost
2. **Modified files, resolved issues, and key changes**
3. **Unresolved TODOs, rollback notes, and plans**
4. **Tool output content may be deleted, but always preserve pass/fail conclusions**
5. **Verification status: pass/fail**

**STRICT RULE: Never modify fixed objective values** — identifiers, UUIDs, UIDs, IDs, hashes, IPs, ports, URLs, filenames, and similar stable references. Changing these will cause downstream integrations and calls to fail.
