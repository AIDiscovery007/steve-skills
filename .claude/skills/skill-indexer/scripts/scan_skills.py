#!/usr/bin/env python3
"""
scan_skills.py - 扫描所有已安装的 skills

扫描 ~/.agents/skills/ 和项目级 .claude/skills/ 目录，
读取每个 skill 的 SKILL.md 提取 name 和 description。
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional

# Skills 目录（仅项目级）
SKILL_DIRS = [
    Path.home() / "steve-skills" / ".claude" / "skills",
]


def extract_skill_info(skill_path: Path) -> Optional[Dict[str, str]]:
    """从 SKILL.md 提取 skill 信息"""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return None

    content = skill_md.read_text(encoding="utf-8")

    # 提取 name（从 YAML frontmatter）
    name = None
    description = None

    # 解析 frontmatter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            # 提取 name
            name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
            if name_match:
                name = name_match.group(1).strip()

            # 提取 description
            desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
            if desc_match:
                description = desc_match.group(1).strip()

    # 如果 frontmatter 没有 name，用目录名
    if not name:
        name = skill_path.name

    # 如果没有 description，尝试从内容第一行提取
    if not description:
        lines = content.split("\n")
        for line in lines:
            line = line.strip()
            if line and not line.startswith("---") and not line.startswith("#"):
                # 取第一个非标题、非空行作为简短描述
                description = line[:100] if len(line) > 100 else line
                break

    return {
        "name": name,
        "description": description or "",
        "path": str(skill_path),
    }


def scan_skills() -> List[Dict[str, str]]:
    """扫描所有 skills 目录"""
    all_skills = []
    seen_names = set()

    for skill_dir in SKILL_DIRS:
        if not skill_dir.exists():
            continue

        for item in skill_dir.iterdir():
            if item.is_dir() and not item.name.startswith("."):
                # 跳过自己的目录
                if item.name == "skill-indexer":
                    continue

                skill_info = extract_skill_info(item)
                if skill_info and skill_info["name"] not in seen_names:
                    all_skills.append(skill_info)
                    seen_names.add(skill_info["name"])

    return all_skills


def generate_trigger_keywords(name: str, description: str) -> List[str]:
    """根据 name 和 description 生成触发关键词"""
    keywords = [name.replace("-", " "), name.replace("-", "")]

    # 从 description 提取关键词
    if description:
        # 简单分词
        words = re.findall(r"[\w]+", description.lower())
        # 取前3个有意义的词
        for word in words[:5]:
            if len(word) > 2 and word not in keywords:
                keywords.append(word)

    return list(set(keywords))[:5]


if __name__ == "__main__":
    skills = scan_skills()
    print(json.dumps(skills, ensure_ascii=False, indent=2))
