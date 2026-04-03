#!/usr/bin/env python3
"""
流动性数据拉取脚本
并发获取所有数据源，输出 JSON 供报告生成使用
"""

import json
import sys
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json,*/*",
    "Accept-Language": "en-US,en;q=0.9",
}


def fetch(url, label):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            return label, data, None
    except Exception as e:
        return label, None, str(e)


def get_today_str():
    return datetime.now(CST).strftime("%Y-%m-%d")


def get_date_range(days_ago=17):
    end = datetime.now(CST)
    start = end - timedelta(days=days_ago)
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")


def build_urls():
    start_date, end_date = get_date_range(20)
    return {
        "sofr": f"https://markets.newyorkfed.org/api/rates/secured/sofr/last/10.json",
        "usdjpy": f"https://query1.finance.yahoo.com/v8/finance/chart/JPY=X?range=1mo&interval=1d",
        "move": f"https://query1.finance.yahoo.com/v8/finance/chart/%5EMOVE?range=1mo&interval=1d",
        "hyg": f"https://query1.finance.yahoo.com/v8/finance/chart/HYG?range=1mo&interval=1d",
        "onrrp": f"https://markets.newyorkfed.org/api/rp/reverserepo/propositions/search.json?startDate={start_date}&endDate={end_date}",
        "spx": f"https://query1.finance.yahoo.com/v8/finance/chart/%5EGSPC?range=1mo&interval=1d",
        "gold": f"https://query1.finance.yahoo.com/v8/finance/chart/GC%3DF?range=3mo&interval=1d",
        "silver": f"https://query1.finance.yahoo.com/v8/finance/chart/SI%3DF?range=3mo&interval=1d",
        "dxy": f"https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB?range=1mo&interval=1d",
        "tip": f"https://query1.finance.yahoo.com/v8/finance/chart/TIP?range=1mo&interval=1d",
        "tyx": f"https://query1.finance.yahoo.com/v8/finance/chart/%5ETYX?range=1mo&interval=1d",
    }


def parse_sofr(data):
    rates = data.get("refRates", [])
    if not rates:
        return {}
    latest = rates[0]
    return {
        "date": latest["effectiveDate"],
        "rate": latest["percentRate"],
        "vol_bn": latest["volumeInBillions"],
        "p25": latest["percentPercentile25"],
        "p75": latest["percentPercentile75"],
        "history": [
            {"date": r["effectiveDate"], "rate": r["percentRate"]} for r in rates[:5]
        ],
    }


def parse_yahoo(data, symbol):
    try:
        result = data["chart"]["result"][0]
        meta = result["meta"]
        closes = result["indicators"]["quote"][0]["close"]
        timestamps = result["timestamp"]
        # 过滤 None
        pairs = [(t, c) for t, c in zip(timestamps, closes) if c is not None]
        if not pairs:
            return {}
        latest_ts, latest_close = pairs[-1]
        prev_close = pairs[-2][1] if len(pairs) > 1 else latest_close
        change = latest_close - prev_close
        change_pct = (change / prev_close) * 100 if prev_close else 0
        recent = pairs[-5:]
        return {
            "symbol": symbol,
            "price": round(latest_close, 4),
            "change": round(change, 4),
            "change_pct": round(change_pct, 2),
            "52w_high": meta.get("fiftyTwoWeekHigh"),
            "52w_low": meta.get("fiftyTwoWeekLow"),
            "history": [{"ts": t, "close": round(c, 4)} for t, c in recent],
        }
    except Exception as e:
        return {"error": str(e)}


def parse_onrrp(data):
    ops = data.get("repo", {}).get("operations", [])
    if not ops:
        return {}
    latest = ops[0]
    total_bn = latest["totalAmtAccepted"] / 1e9
    history = [
        {"date": o["operationDate"], "amount_bn": round(o["totalAmtAccepted"] / 1e9, 3)}
        for o in ops[:5]
    ]
    return {
        "date": latest["operationDate"],
        "amount_bn": round(total_bn, 3),
        "history": history,
    }


def main():
    urls = build_urls()
    results = {}

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {
            executor.submit(fetch, url, label): label for label, url in urls.items()
        }
        for future in as_completed(futures):
            label, data, err = future.result()
            if err:
                results[label] = {"error": err}
            else:
                results[label] = data

    # 解析
    parsed = {
        "fetched_at": datetime.now(CST).strftime("%Y-%m-%d %H:%M:%S CST"),
        "sofr": parse_sofr(results.get("sofr", {})),
        "usdjpy": parse_yahoo(results.get("usdjpy", {}), "USDJPY"),
        "move": parse_yahoo(results.get("move", {}), "MOVE"),
        "hyg": parse_yahoo(results.get("hyg", {}), "HYG"),
        "onrrp": parse_onrrp(results.get("onrrp", {})),
        "spx": parse_yahoo(results.get("spx", {}), "SPX"),
        "gold": parse_yahoo(results.get("gold", {}), "GC=F"),
        "silver": parse_yahoo(results.get("silver", {}), "SI=F"),
        "dxy": parse_yahoo(results.get("dxy", {}), "DXY"),
        "tip": parse_yahoo(results.get("tip", {}), "TIP"),
        "tyx": parse_yahoo(results.get("tyx", {}), "TYX"),
    }

    print(json.dumps(parsed, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
