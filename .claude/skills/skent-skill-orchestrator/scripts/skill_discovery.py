#!/usr/bin/env python3
"""
skill_discovery.py - 封装动态发现逻辑（npx skills）

用法:
    python skill_discovery.py find [关键词]
    python skill_discovery.py list
    python skill_discovery.py match [关键词列表]
"""

import sys
import json
import subprocess
import re
from typing import Dict, List, Any, Optional


def run_npx_skills(args: List[str]) -> str:
    """运行 npx skills 命令"""
    try:
        result = subprocess.run(
            ["npx", "skills"] + args, capture_output=True, text=True, timeout=30
        )
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return "Error: Command timed out"
    except FileNotFoundError:
        return "Error: npx not found"
    except Exception as e:
        return f"Error: {str(e)}"


def find_skills(keyword: str) -> List[Dict[str, str]]:
    """
    搜索技能

    返回:
        [{"name": str, "description": str}, ...]
    """
    output = run_npx_skills(["find", keyword])

    skills = []
    # 解析 npx skills find 输出
    # 格式可能是:
    # skill-name - description
    lines = output.strip().split("\n")
    for line in lines:
        line = line.strip()
        if not line or line.startswith("npm") or line.startswith("Installing"):
            continue
        if " - " in line:
            parts = line.split(" - ", 1)
            skills.append(
                {
                    "name": parts[0].strip(),
                    "description": parts[1].strip() if len(parts) > 1 else "",
                }
            )
        elif line and not line.startswith("#"):
            skills.append({"name": line, "description": ""})

    return skills


def list_installed_skills() -> List[Dict[str, str]]:
    """
    列出已安装技能

    返回:
        [{"name": str, "description": str}, ...]
    """
    output = run_npx_skills(["list"])

    skills = []
    lines = output.strip().split("\n")
    for line in lines:
        line = line.strip()
        if not line or line.startswith("npm") or line.startswith("Listing"):
            continue
        # 解析技能名称
        if line.startswith("- "):
            line = line[2:]
        if line.startswith("* "):
            line = line[2:]
        if line:
            skills.append(
                {
                    "name": line.split(" ")[0] if " " in line else line,
                    "description": line,
                }
            )

    return skills


def match_skills_to_tasks(
    keywords: List[str], installed_only: bool = True
) -> Dict[str, List[Dict[str, str]]]:
    """
    将关键词匹配到技能

    参数:
        keywords: 任务关键词列表
        installed_only: 是否只返回已安装技能

    返回:
        {keyword: [{"name": str, "description": str}, ...]}
    """
    # 已知技能映射（快速匹配）
    known_skill_map = {
        "复盘": ["skent-session-reflect"],
        "reflect": ["skent-session-reflect"],
        "投资": ["skent-gold-analyst"],
        "黄金": ["skent-gold-analyst"],
        "流动性": ["skent-liquidity-report"],
        "新闻": ["news-aggregator-skill"],
        "图片": ["nano-banana-2"],
        "Git": ["git-commit"],
        "技能": ["find-skills", "autoresearch", "skent-autotune"],
        "分析": ["skent-gold-analyst", "skent-liquidity-report"],
        "报告": ["skent-liquidity-report", "skent-html-renderer"],
        "渲染": ["skent-html-renderer"],
        "编排": ["skent-skill-orchestrator"],
        "索引": ["skent-skill-indexer"],
    }

    matched = {}

    for keyword in keywords:
        if keyword in known_skill_map:
            matched[keyword] = [
                {"name": skill, "description": ""} for skill in known_skill_map[keyword]
            ]
        elif not installed_only:
            # 动态搜索
            search_results = find_skills(keyword)
            if search_results:
                matched[keyword] = search_results

    return matched


def check_skill_installed(skill_name: str) -> bool:
    """检查技能是否已安装"""
    installed = list_installed_skills()
    installed_names = [s["name"] for s in installed]
    return skill_name in installed_names


def get_install_command(skill_package: str, global_install: bool = True) -> str:
    """获取安装命令"""
    if global_install:
        return f"npx skills add {skill_package} -g -y"
    else:
        return f"npx skills add {skill_package} -y"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法:")
        print("  python skill_discovery.py find [关键词]")
        print("  python skill_discovery.py list")
        print("  python skill_discovery.py match [关键词1] [关键词2] ...")
        sys.exit(1)

    command = sys.argv[1]

    if command == "find":
        keyword = sys.argv[2] if len(sys.argv) > 2 else ""
        result = find_skills(keyword)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif command == "list":
        result = list_installed_skills()
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif command == "match":
        keywords = sys.argv[2:] if len(sys.argv) > 2 else []
        result = match_skills_to_tasks(keywords)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif command == "check":
        if len(sys.argv) > 2:
            skill_name = sys.argv[2]
            installed = check_skill_installed(skill_name)
            print(json.dumps({"skill": skill_name, "installed": installed}))

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
