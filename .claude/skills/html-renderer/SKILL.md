---
name: html-renderer
description: Render Markdown reports as beautiful HTML pages with auto browser open. Use when user wants to view a generated report (from gold-analyst, liquidity-report, news-aggregator, etc.) in a browser instead of TUI. Also use when user says "render this", "open in browser", "view as HTML", "pretty print this report", or asks to make a Markdown report look better. Trigger proactively when any skill outputs a Markdown report and the user would benefit from a visual HTML version.
version: 0.1.0
legacy_alias_of: skent-html-renderer
---

# HTML Renderer

> Legacy alias. Canonical first-party skill: `/skent-html-renderer` in `skills/skent-html-renderer/`.

Render Markdown string into a beautifully styled HTML page that auto-opens in the browser.

## When to Use

- After any skill generates a Markdown report (gold-analyst, liquidity-report, news-aggregator, etc.)
- When user asks to "render this", "open in browser", "view as HTML", "美化报告", "HTML 版本"
- When a Markdown report output is long or hard to read in TUI

## How It Works

1. Read Markdown from stdin
2. Auto-detect report style (`analytical` | `news` | `generic`)
3. Convert Markdown → HTML with full GFM support
4. Apply beautiful CSS (distinctive typography, dark/light theme, animations, emoji)
5. Save to `output/` directory
6. Auto-open in default browser

## CLI Usage

```bash
# Standard: pipe Markdown to renderer
echo "$markdown" | python3 {skillDir}/scripts/render.py --open --title "报告标题"

# With explicit style
cat report.md | python3 {skillDir}/scripts/render.py --open --title "黄金分析" --style analytical

# Save only (no browser open)
python3 {skillDir}/scripts/render.py --title "My Report" --output ./reports/
```

## CLI Options

| Flag | Description | Default |
|------|-------------|---------|
| `--title` | Report title shown in browser tab | "Report" |
| `--open` | Auto-open in browser after render | false |
| `--style` | `analytical` (gold/liquidity), `news`, `generic` | auto-detect |
| `--output` | Output directory | `{skillDir}/output/` |

## Python API

```python
from html_renderer import render_markdown

# Simple
html_path = render_markdown(markdown_text, title="Gold Analysis", open_browser=True)

# With options
html_path = render_markdown(
    md_text=markdown_text,
    title="流动性日报",
    style="analytical",
    open_browser=True,
    output_dir="./reports/"
)
```

## Auto-Detection Logic

The renderer auto-detects report type from content patterns:

| Style | Detection Keywords |
|-------|------------------|
| `analytical` | `综合判断`, `黄金`, `流动性`, `SOFR`, `MOVE`, `TIP`, `TYX` |
| `news` | `Source`, `Time`, `Heat`, `Discussion`, `GitHub` |
| `generic` | Anything else |

## Design Principles

CSS styling follows these principles (from front-design skill):

- **Typography**: Crimson Pro (display) + IBM Plex Sans (body) — NOT Inter/Arial/Roboto
- **Color (analytical)**: Dark theme (`#0f1419` bg) + gold accent (`#d4af37`)
- **Color (news)**: Light theme (`#fafafa` bg) + blue accent (`#3b82f6`)
- **Motion**: `fadeInUp` animations on section load, staggered 0.1s delay per element
- **Tables**: Zebra striping + hover highlight
- **Emoji**: Native emoji rendering preserved
- **Links**: External links open in new tab (`target="_blank"`)

## Output Files

- HTML saved to: `{output_dir}/{timestamp}_{slug}.html`
- Example: `output/2026-03-21_1234_gold-analysis.html`

## Error Handling

- Empty input → raise `ValueError("Empty markdown input")`
- Missing dependencies → graceful error with install instructions
- Browser open failure → still save HTML, warn user to open manually
