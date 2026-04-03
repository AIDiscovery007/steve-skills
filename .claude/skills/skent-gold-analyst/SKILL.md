---
name: skent-gold-analyst
description: 黄金投资分析。基于实际利率（TIP）、美元指数（DXY）、名义长端利率（TYX）、MOVE、USDJPY、HYG、白银、S&P500 等指标，生成综合评分、仓位建议和具体操作参数（介入区间、止损、目标位）。当用户说「分析黄金」「黄金要不要买」「黄金加仓」「黄金投资建议」「黄金怎么看」「帮我看看黄金」时使用。
version: 0.1.0
---

# skent-gold-analyst — 黄金投资分析

## Base Directory

- `{baseDir}` = 当前 `SKILL.md` 所在目录
- 脚本路径统一使用 `{baseDir}/scripts/...`
- 参考资料路径统一使用 `{baseDir}/references/...`

## 数据获取

所有数据通过 Yahoo Finance v8 API 获取，**必须使用 web_fetch 工具**（直接 HTTP 会被拦截）。

并发调用以下 URL：

| 字段 | URL | 范围 |
|------|-----|------|
| gold | `https://query1.finance.yahoo.com/v8/finance/chart/GC=F?range=3mo&interval=1d` | 3mo |
| silver | `https://query1.finance.yahoo.com/v8/finance/chart/SI=F?range=3mo&interval=1d` | 3mo |
| dxy | `https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB?range=1mo&interval=1d` | 1mo |
| tip | `https://query1.finance.yahoo.com/v8/finance/chart/TIP?range=1mo&interval=1d` | 1mo |
| tyx | `https://query1.finance.yahoo.com/v8/finance/chart/^TYX?range=1mo&interval=1d` | 1mo |
| move | `https://query1.finance.yahoo.com/v8/finance/chart/^MOVE?range=1mo&interval=1d` | 1mo |
| usdjpy | `https://query1.finance.yahoo.com/v8/finance/chart/JPY=X?range=1mo&interval=1d` | 1mo |
| hyg | `https://query1.finance.yahoo.com/v8/finance/chart/HYG?range=1mo&interval=1d` | 1mo |
| spx | `https://query1.finance.yahoo.com/v8/finance/chart/^GSPC?range=1mo&interval=1d` | 1mo |

从每个 Yahoo 响应中提取：
- `chart.result[0].meta.regularMarketPrice` → 最新价
- `chart.result[0].meta.fiftyTwoWeekHigh/Low` → 52周高低
- `chart.result[0].indicators.quote[0].close` 最后两个非 null 值 → 日涨跌幅
- `chart.result[0].indicators.quote[0].close` 最后30个非 null 值 → history_30d（黄金/白银用）

## 报告生成

将数据整合为 JSON 后调用分析脚本：

```bash
echo '<JSON>' | python3 {baseDir}/scripts/analyze.py
```

JSON 结构：
```json
{
  "fetched_at": "2026-03-18 16:00:00 CST",
  "gold":   { "price": 5011.9, "change": 10.9, "change_pct": 0.22, "52w_high": 5586.2, "52w_low": 2949.7, "history_30d": [...] },
  "silver": { "price": 79.83,  "change": 0.3,  "change_pct": 0.38, "52w_high": 121.3,  "52w_low": 28.31,  "history_30d": [...] },
  "dxy":    { "price": 100.38, "change": 0.65,  "change_pct": 0.65, "52w_high": 104.68, "52w_low": 95.55 },
  "tip":    { "price": 111.45, "change": 0.22,  "change_pct": 0.20, "52w_high": 112.26, "52w_low": 106.47 },
  "tyx":    { "price": 4.852,  "change": 0.04,  "change_pct": 0.83, "52w_high": 5.152,  "52w_low": 0.0 },
  "move":   { "price": 79.23,  "change": -6.02, "change_pct": -7.07,"52w_high": 140.03, "52w_low": 0.0 },
  "usdjpy": { "price": 158.83, "change": 0.5,   "change_pct": 0.32, "52w_high": 159.63, "52w_low": 139.89 },
  "hyg":    { "price": 79.81,  "change": -0.10, "change_pct": -0.12,"52w_high": 81.36,  "52w_low": 75.08 },
  "spx":    { "price": 6716.09,"change": -83.13,"change_pct": -1.22,"52w_high": 7002.28,"52w_low": 4835.04 }
}
```

## 分析框架

见 `references/indicators.md`，包含：
- 核心三要素（实际利率、美元、名义利率）的逻辑和阈值
- 流动性风险指标（MOVE、USDJPY、HYG）的用法
- 综合评分逻辑
- 金银比参考

## 注意事项

- 所有 Yahoo Finance URL **必须**通过 web_fetch 工具调用
- TIP 价格与实际利率**反向**：TIP 涨 = 实际利率降 = 利好黄金
- DXY 是黄金最关键的短期变量，关注 101 关口
- MOVE 只做辅助过滤器，不单独作为交易信号
- 止损/目标位为参考，非精确预测
