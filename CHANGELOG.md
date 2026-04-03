# Changelog

## 0.1.1 - 2026-04-03

### Fixed
- Add `.claude-plugin/plugin.json` so installed marketplace plugins register packaged skills correctly
- Bump plugin version to `0.1.1` so existing installs can update cleanly

## 0.1.0 - 2026-04-03

### Added
- Introduce canonical first-party monorepo layout under `skills/skent-*`
- Add `.claude-plugin/marketplace.json` with a single first-party plugin bundle
- Add root `README.md`, refreshed `CLAUDE.md`, and `THIRD_PARTY_SKILLS.md`
- Add `third_party/registry.json` to document external skill provenance
- Include `skent-session-reflect` in the first-party publish set

### Changed
- Standardize first-party `SKILL.md` frontmatter with `name` and `version`
- Align first-party skill docs on `{baseDir}` script path guidance
- Update skill indexing/orchestration metadata to prefer canonical `skent-*` skills
- Keep legacy unprefixed self-authored skills in `.claude/skills/` as compatibility aliases

### Maintenance
- Expand ignore rules for generated skill outputs and experiment directories
- Separate first-party publishing from third-party installed skills to avoid authorship ambiguity
