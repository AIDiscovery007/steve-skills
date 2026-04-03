"""
Core rendering logic for html-renderer skill.
Converts Markdown string to beautifully styled HTML.
"""

import os
import re
import datetime
from pathlib import Path

try:
    import markdown
except ImportError:
    raise ImportError(
        "markdown library not found. Install with: pip install markdown"
    )

try:
    from jinja2 import Environment, FileSystemLoader, Template
except ImportError:
    raise ImportError(
        "jinja2 library not found. Install with: pip install jinja2"
    )

# Detect report type from content patterns
ANALYTICAL_KEYWORDS = [
    "综合判断", "黄金", "流动性", "SOFR", "MOVE", "USDJPY",
    "TIP", "TYX", "HYG", "ON RRP", "DXY", "白银", "实际利率",
    "名义利率", "介入区间", "止损", "目标位", "仓位",
]
NEWS_KEYWORDS = ["Source", "Time", "Heat", "Discussion", "GitHub", "HN", "summary", "Summary"]


def detect_report_type(md_text: str) -> str:
    """Auto-detect report style from Markdown content."""
    if any(kw in md_text for kw in ANALYTICAL_KEYWORDS):
        return "analytical"
    if any(kw in md_text for kw in NEWS_KEYWORDS):
        return "news"
    return "generic"


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')[:40]


def make_links_external(html: str) -> str:
    """Make external links open in new tab."""
    def replace_link(m):
        href = m.group(1)
        if href.startswith('http://') or href.startswith('https://'):
            return f'<a href="{href}" target="_blank" rel="noopener noreferrer">'
        return f'<a href="{href}">'

    return re.sub(r'<a href="([^"]+)">', replace_link, html)


def wrap_emoji_in_span(html: str) -> str:
    """Wrap emoji characters in a span for consistent styling."""
    emoji_pattern = re.compile(
        '[\U0001F300-\U0001F9FF]'  # Emoji ranges
        '|[\U0001F600-\U0001F64F]'  # Emoticons
        '|[\U00002600-\U000026FF]'  # Misc symbols
        '|[\U0001FA00-\U0001FAFF]'  # Chess/symbols
        '|[\U0001F700-\U0001F77F]'  # Alchemical
        '|[\u2600-\u26FF]'  # Misc symbols (plain)
    )
    return emoji_pattern.sub(r'<span class="emoji">\g<0></span>', html)


def render_markdown(
    md_text: str,
    title: str = "Report",
    style: str = "auto",
    open_browser: bool = False,
    output_dir: str = None,
) -> str:
    """
    Render Markdown string as a beautiful HTML page.

    Args:
        md_text: Markdown string
        title: Page title
        style: "analytical" | "news" | "generic" | "auto" (default: auto)
        open_browser: If True, open HTML in browser after rendering
        output_dir: Output directory (default: skillDir/output)

    Returns:
        Path to the generated HTML file
    """
    if not md_text or not isinstance(md_text, str):
        raise ValueError("Empty or invalid markdown input")

    md_text = md_text.strip()

    # Resolve output directory
    if output_dir is None:
        skill_dir = Path(__file__).parent.parent.resolve()
        output_dir = skill_dir / "output"
    else:
        output_dir = Path(output_dir).resolve()

    output_dir.mkdir(parents=True, exist_ok=True)

    # Detect style
    report_type = detect_report_type(md_text) if style == "auto" else style

    # Convert Markdown to HTML
    body_html = markdown.markdown(
        md_text,
        extensions=[
            'tables',
            'fenced_code',
            'nl2br',
            'sane_lists',
        ],
        output_format='html5',
    )

    # Post-process HTML
    body_html = make_links_external(body_html)
    body_html = wrap_emoji_in_span(body_html)

    # Load template
    template_path = Path(__file__).parent / "template.html"
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    template = Template(template_content)

    # Generate timestamp and slug
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H%M")
    slug = slugify(title)
    filename = f"{timestamp}_{slug}.html"
    output_path = output_dir / filename

    # Render HTML
    generated_at = now.strftime("%Y-%m-%d %H:%M")
    html = template.render(
        title=title,
        body=body_html,
        generated_at=generated_at,
    )

    # Save file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Open in browser if requested
    if open_browser:
        _open_in_browser(str(output_path))

    return str(output_path)


def _open_in_browser(path: str) -> None:
    """Open file in default browser (macOS)."""
    import subprocess
    import sys

    path = os.path.abspath(path)

    try:
        if sys.platform == 'darwin':
            subprocess.run(['open', path], check=True)
        elif sys.platform == 'win32':
            os.startfile(path)  # type: ignore
        else:
            import webbrowser
            webbrowser.open(f'file://{path}')
    except Exception as e:
        print(f"Warning: Could not open browser: {e}")
        print(f"HTML saved to: {path}")
