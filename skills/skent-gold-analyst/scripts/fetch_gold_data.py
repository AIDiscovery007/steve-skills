#!/usr/bin/env python3
"""
黄金分析数据拉取脚本
直接通过 Yahoo Finance HTTP 接口获取所有所需指标
注意：此脚本在 agent 环境外运行时可能被 Yahoo 拦截（429）
      在 agent 内部请通过 web_fetch 工具调用各 URL，再将结果 pipe 给 analyze.py
"""

import json
import sys
import urllib.request
from datetime import datetime, timezone

URLS = {
    "gold":   "https://query1.finance.yahoo.com/v8/finance/chart/GC=F?range=3mo&interval=1d",
    "silver": "https://query1.finance.yahoo.com/v8/finance/chart/SI=F?range=3mo&interval=1d",
    "dxy":    "https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB?range=1mo&interval=1d",
    "tip":    "https://query1.finance.yahoo.com/v8/finance/chart/TIP?range=1mo&interval=1d",
    "tyx":    "https://query1.finance.yahoo.com/v8/finance/chart/^TYX?range=1mo&interval=1d",
    "move":   "https://query1.finance.yahoo.com/v8/finance/chart/^MOVE?range=1mo&interval=1d",
    "usdjpy": "https://query1.finance.yahoo.com/v8/finance/chart/JPY=X?range=1mo&interval=1d",
    "spx":    "https://query1.finance.yahoo.com/v8/finance/chart/^GSPC?range=1mo&interval=1d",
    "hyg":    "https://query1.finance.yahoo.com/v8/finance/chart/HYG?range=1mo&interval=1d",
}

def parse_yahoo(raw_json: dict, key: str) -> dict:
    try:
        result = raw_json["chart"]["result"][0]
        meta = result["meta"]
        closes = [x for x in result["indicators"]["quote"][0]["close"] if x is not None]
        price = meta.get("regularMarketPrice", closes[-1] if closes else None)
        prev = closes[-2] if len(closes) >= 2 else price
        change = round(price - prev, 4) if price and prev else 0
        change_pct = round(change / prev * 100, 2) if prev else 0
        return {
            "price": price,
            "change": change,
            "change_pct": change_pct,
            "52w_high": meta.get("fiftyTwoWeekHigh"),
            "52w_low": meta.get("fiftyTwoWeekLow"),
            "history_30d": closes[-30:],
        }
    except Exception as e:
        return {"error": str(e)}

def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

def main():
    now = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    result = {"fetched_at": now}
    for key, url in URLS.items():
        try:
            raw = fetch(url)
            result[key] = parse_yahoo(raw, key)
        except Exception as e:
            result[key] = {"error": str(e)}
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
