#!/usr/bin/env python3
"""
analyze_goal.py - 解析用户目标，提取关键实体和意图

用法:
    python analyze_goal.py "用户目标文本"
"""

import sys
import json
import re
from typing import Dict, List, Any


def extract_intent_and_entities(goal_text: str) -> Dict[str, Any]:
    """
    从用户目标文本中提取意图和实体

    返回:
        {
            "final_goal": str,          # 最终目标
            "constraints": List[str],    # 约束条件
            "expected_output": str,     # 期望交付物
            "keywords": List[str],       # 关键词（用于技能匹配）
            "complexity": str,          # 复杂度评估: simple, moderate, complex
        }
    """
    goal_text = goal_text.strip()

    # 移除句末标点
    goal_text = re.sub(r"[。.。]+$", "", goal_text)

    # 提取关键词（用于技能匹配）
    keywords = extract_keywords(goal_text)

    # 识别约束条件
    constraints = extract_constraints(goal_text)

    # 识别期望交付物
    expected_output = extract_expected_output(goal_text)

    # 判断复杂度
    complexity = assess_complexity(goal_text, keywords)

    # 确定最终目标
    final_goal = extract_final_goal(goal_text)

    return {
        "final_goal": final_goal,
        "constraints": constraints,
        "expected_output": expected_output,
        "keywords": keywords,
        "complexity": complexity,
    }


def extract_keywords(text: str) -> List[str]:
    """提取关键词用于技能匹配"""
    keyword_map = {
        "投资": ["投资", "买入", "加仓", "配置", "理财"],
        "黄金": ["黄金", "gold", "金价"],
        "流动性": ["流动性", "liquidity", "市场", "资金"],
        "新闻": ["新闻", "news", "资讯", "聚合"],
        "图片": ["图片", "生成图片", "image", "画"],
        "Git": ["git", "commit", "提交"],
        "技能": ["技能", "skill", "创建", "优化"],
        "分析": ["分析", "研究", "评估"],
        "报告": ["报告", "report", "生成报告"],
    }

    found_keywords = []
    for category, words in keyword_map.items():
        for word in words:
            if word.lower() in text.lower():
                found_keywords.append(category)
                break

    return list(set(found_keywords))


def extract_constraints(text: str) -> List[str]:
    """识别约束条件"""
    constraints = []

    # 时间约束
    time_patterns = [
        (r"(\d+)\s*分钟", "分钟"),
        (r"(\d+)\s*小时", "小时"),
        (r"(\d+)\s*天", "天"),
        (r"今天", "今天"),
        (r"明天", "明天"),
        (r"本周", "本周"),
    ]

    for pattern, label in time_patterns:
        if re.search(pattern, text):
            constraints.append(f"时间: {label}")

    # 格式约束
    if "markdown" in text.lower() or "md" in text.lower():
        constraints.append("格式: Markdown")
    if "pdf" in text.lower():
        constraints.append("格式: PDF")
    if "表格" in text or "excel" in text.lower():
        constraints.append("格式: 表格/Excel")

    # 风格约束
    if "简洁" in text:
        constraints.append("风格: 简洁")
    if "详细" in text:
        constraints.append("风格: 详细")
    if "专业" in text:
        constraints.append("风格: 专业")

    return constraints


def extract_expected_output(text: str) -> str:
    """识别期望交付物"""
    output_patterns = [
        (r"生成.*?报告", "报告"),
        (r"分析.*?结果", "分析结果"),
        (r"给出.*?建议", "建议"),
        (r"创建.*?技能", "新技能"),
        (r"生成.*?图片", "图片"),
        (r"总结.*?", "总结"),
    ]

    for pattern, output in output_patterns:
        if re.search(pattern, text):
            return output

    return "综合结果"


def assess_complexity(text: str, keywords: List[str]) -> str:
    """评估任务复杂度"""
    # 复杂度指标
    complexity_score = 0

    # 多技能关键词
    if len(keywords) >= 3:
        complexity_score += 2
    elif len(keywords) >= 2:
        complexity_score += 1

    # 多步骤指示
    multi_step_indicators = ["然后", "接下来", "再", "首先", "其次", "最后"]
    for indicator in multi_step_indicators:
        if indicator in text:
            complexity_score += 1
            break

    # 不确定表述
    uncertainty_indicators = ["不知道", "不确定", "怎么", "如何"]
    for indicator in uncertainty_indicators:
        if indicator in text:
            complexity_score += 1
            break

    # 跨领域指示
    cross_domain = ["既要", "又要", "同时", "并且", "和"]
    for indicator in cross_domain:
        if indicator in text:
            complexity_score += 1
            break

    if complexity_score >= 4:
        return "complex"
    elif complexity_score >= 2:
        return "moderate"
    else:
        return "simple"


def extract_final_goal(text: str) -> str:
    """提取最终目标（简化文本）"""
    # 移除常见前缀
    prefixes_to_remove = [
        r"^帮我",
        r"^请帮我",
        r"^我想",
        r"^我要",
        r"^帮我完成",
        r"^帮我创建",
        r"^帮我生成",
    ]

    result = text
    for prefix in prefixes_to_remove:
        result = re.sub(prefix, "", result)

    return result.strip()


def decompose_task(goal_text: str, keywords: List[str]) -> List[Dict[str, Any]]:
    """
    将复杂目标分解为原子任务

    返回:
        [
            {
                "task_id": str,
                "description": str,
                "required_skills": List[str],
                "depends_on": List[str],  # 依赖的任务ID
            }
        ]
    """
    tasks = []

    # 基于关键词生成任务
    task_templates = {
        "投资": [{"description": "分析投资机会", "skills": ["gold-analyst"]}],
        "黄金": [{"description": "黄金投资分析", "skills": ["gold-analyst"]}],
        "流动性": [{"description": "生成流动性报告", "skills": ["liquidity-report"]}],
        "新闻": [{"description": "聚合新闻资讯", "skills": ["news-aggregator-skill"]}],
        "图片": [{"description": "生成图片", "skills": ["nano-banana-2"]}],
        "Git": [{"description": "Git提交分析", "skills": ["git-commit"]}],
        "技能": [
            {
                "description": "发现或优化技能",
                "skills": ["find-skills", "autoresearch", "autotune"],
            }
        ],
        "分析": [{"description": "综合分析", "skills": []}],
        "报告": [{"description": "生成报告", "skills": ["liquidity-report"]}],
    }

    task_id = 1
    covered_keywords = set()

    for keyword in keywords:
        if keyword in task_templates:
            for template in task_templates[keyword]:
                if keyword not in covered_keywords:
                    task = {
                        "task_id": f"task_{task_id}",
                        "description": template["description"],
                        "required_skills": template["skills"],
                        "depends_on": [],
                    }
                    tasks.append(task)
                    covered_keywords.add(keyword)
                    task_id += 1

    # 如果没有匹配的任务，创建一个通用任务
    if not tasks:
        tasks.append(
            {
                "task_id": "task_1",
                "description": "处理用户请求",
                "required_skills": [],
                "depends_on": [],
            }
        )

    return tasks


def analyze_goal(goal_text: str) -> Dict[str, Any]:
    """
    完整分析用户目标

    返回完整的分析结果，包括分解后的任务
    """
    result = extract_intent_and_entities(goal_text)
    result["tasks"] = decompose_task(goal_text, result["keywords"])

    # 分析任务依赖关系
    result["execution_mode"] = analyze_execution_mode(result["tasks"])

    return result


def analyze_execution_mode(tasks: List[Dict[str, Any]]) -> str:
    """
    分析执行模式：并行或串行

    返回: "parallel", "serial", 或 "hybrid"
    """
    has_dependencies = any(task["depends_on"] for task in tasks)

    if not has_dependencies and len(tasks) > 1:
        return "parallel"
    elif has_dependencies:
        return "serial"
    elif len(tasks) == 1:
        return "single"
    else:
        return "parallel"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        goal_text = " ".join(sys.argv[1:])
    else:
        goal_text = input("请输入目标: ")

    result = analyze_goal(goal_text)
    print(json.dumps(result, ensure_ascii=False, indent=2))
