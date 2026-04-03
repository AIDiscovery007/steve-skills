#!/usr/bin/env python3
"""
CLI entry point for html-renderer.
Reads Markdown from stdin, renders as HTML, optionally opens in browser.

Usage:
    echo "$markdown" | python3 render.py --open --title "My Report"
    cat report.md | python3 render.py --open --title "Gold Analysis"
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path so we can import renderer
sys.path.insert(0, str(Path(__file__).parent))

from renderer import render_markdown


def main():
    parser = argparse.ArgumentParser(
        description="Render Markdown as a beautiful HTML page"
    )
    parser.add_argument(
        '--title',
        type=str,
        default="Report",
        help='Report title (shown in browser tab)'
    )
    parser.add_argument(
        '--open',
        action='store_true',
        help='Auto-open in browser after render'
    )
    parser.add_argument(
        '--style',
        type=str,
        default='auto',
        choices=['analytical', 'news', 'generic', 'auto'],
        help='Report style preset (default: auto-detect)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Output directory (default: skill output/ dir)'
    )

    args = parser.parse_args()

    # Read Markdown from stdin
    if sys.stdin.isatty():
        print("Error: No input provided. Pipe Markdown to this script.", file=sys.stderr)
        print("Example: echo '# Hello' | python3 render.py --open", file=sys.stderr)
        sys.exit(1)

    md_text = sys.stdin.read()

    if not md_text.strip():
        print("Error: Empty input", file=sys.stderr)
        sys.exit(1)

    try:
        output_path = render_markdown(
            md_text=md_text,
            title=args.title,
            style=args.style,
            open_browser=args.open,
            output_dir=args.output,
        )
        print(f"HTML saved to: {output_path}")
        if args.open:
            print("Opened in browser.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
