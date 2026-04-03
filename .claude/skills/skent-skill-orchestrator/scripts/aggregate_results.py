#!/usr/bin/env python3
"""
aggregate_results.py - 聚合多技能输出

用法:
    python aggregate_results.py [result1.json] [result2.json] ...
    echo "result1" | python aggregate_results.py --stdin
"""

import sys
import json
from typing import Dict, List, Any, Optional


def aggregate_results(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    聚合多个技能的结果

    参数:
        results: 各技能的输出结果列表

    返回:
        聚合后的统一结果
    """
    if not results:
        return {"error": "No results to aggregate"}

    if len(results) == 1:
        return results[0]

    # 分类结果
    text_results = []
    data_results = []
    skill_names = []

    for result in results:
        skill_name = result.get("skill", "unknown")
        skill_names.append(skill_name)

        # 分类
        if "data" in result:
            data_results.append(result["data"])
        elif "text" in result:
            text_results.append(result["text"])
        elif "content" in result:
            text_results.append(result["content"])
        else:
            # 将整个 result 作为文本处理
            text_results.append(str(result))

    # 构建聚合结果
    aggregated = {
        "skills_used": skill_names,
        "execution_mode": determine_execution_mode(results),
        "summary": generate_summary(skill_names),
    }

    # 添加文本内容
    if text_results:
        aggregated["content"] = merge_text_content(text_results)

    # 添加数据内容
    if data_results:
        aggregated["data"] = merge_data_content(data_results)

    return aggregated


def determine_execution_mode(results: List[Dict[str, Any]]) -> str:
    """确定执行模式"""
    if len(results) == 1:
        return "single"

    # 检查是否有顺序依赖标记
    has_order = all("order" in r or "sequence" in r for r in results)
    if has_order:
        return "serial"

    return "parallel"


def generate_summary(skill_names: List[str]) -> str:
    """生成摘要"""
    unique_skills = list(set(skill_names))
    if len(unique_skills) == 1:
        return f"使用 {unique_skills[0]} 技能完成"
    elif len(unique_skills) == 2:
        return f"协调使用 {unique_skills[0]} 和 {unique_skills[1]} 技能完成"
    else:
        return f"协调使用 {len(unique_skills)} 个技能完成"


def merge_text_content(texts: List[str]) -> str:
    """合并文本内容"""
    merged = []

    for i, text in enumerate(texts):
        if text:
            # 添加分隔符
            if i > 0:
                merged.append("\n" + "=" * 40 + "\n")
            merged.append(text)

    return "".join(merged)


def merge_data_content(data_list: List[Any]) -> List[Any]:
    """合并数据内容"""
    if not data_list:
        return []

    # 如果都是字典，尝试合并
    if all(isinstance(d, dict) for d in data_list):
        merged = {}
        for d in data_list:
            merged.update(d)
        return [merged]

    return data_list


def format_markdown(aggregated: Dict[str, Any]) -> str:
    """格式化为 Markdown"""
    lines = []

    # 标题
    lines.append("# 聚合结果\n")

    # 使用的技能
    if "skills_used" in aggregated:
        lines.append("## 使用技能")
        for skill in aggregated["skills_used"]:
            lines.append(f"- {skill}")
        lines.append("")

    # 摘要
    if "summary" in aggregated:
        lines.append(f"**摘要**: {aggregated['summary']}\n")

    # 内容
    if "content" in aggregated:
        lines.append("## 内容")
        lines.append(aggregated["content"])
        lines.append("")

    # 数据
    if "data" in aggregated:
        lines.append("## 数据")
        lines.append("```json")
        lines.append(json.dumps(aggregated["data"], ensure_ascii=False, indent=2))
        lines.append("```")

    return "\n".join(lines)


def read_results_from_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    """从文件读取结果"""
    results = []
    for path in file_paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                result = json.load(f)
                results.append(result)
        except FileNotFoundError:
            print(f"Warning: File not found: {path}")
        except json.JSONDecodeError:
            print(f"Warning: Invalid JSON in: {path}")
    return results


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--stdin":
        # 从 stdin 读取
        input_data = sys.stdin.read()
        try:
            results = json.loads(input_data)
            if isinstance(results, list):
                aggregated = aggregate_results(results)
            else:
                aggregated = aggregate_results([results])
        except json.JSONDecodeError:
            # 作为纯文本处理
            aggregated = aggregate_results([{"content": input_data}])
    else:
        # 从文件读取
        file_paths = sys.argv[1:] if len(sys.argv) > 1 else []
        if not file_paths:
            print("Usage:")
            print("  python aggregate_results.py [result1.json] [result2.json] ...")
            print("  echo '[...]' | python aggregate_results.py --stdin")
            sys.exit(1)

        results = read_results_from_files(file_paths)
        aggregated = aggregate_results(results)

    # 输出
    if "--markdown" in sys.argv:
        print(format_markdown(aggregated))
    else:
        print(json.dumps(aggregated, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
