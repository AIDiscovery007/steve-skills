---
name: liquidity-report
description: |
  Use when: user requests global liquidity report, market data review, liquidity transmission analysis, or says "liquidity report" / "show me liquidity" / "market data"
  Don't use when: user needs stock analysis, technical analysis, or specific gold/silver investment advice (use gold-analyst instead)
---

# liquidity-report — 全球流动性日报

## 数据获取

### 纽约联储（直接 HTTP，用脚本拉）

```bash
python3 {skillDir}/scripts/fetch_data.py
```

输出 JSON，包含：`sofr`、`onrrp`

### Yahoo Finance（必须用 web_fetch 工具，不能直接 HTTP）

并发调用 web_fetch 获取以下 URL：

| 字段 | URL |
|------|-----|
| usdjpy | `https://query1.finance.yahoo.com/v8/finance/chart/JPY=X?range=1mo&interval=1d` |
| move | `https://query1.finance.yahoo.com/v8/finance/chart/^MOVE?range=1mo&interval=1d` |
| hyg | `https://query1.finance.yahoo.com/v8/finance/chart/HYG?range=1mo&interval=1d` |
| spx | `https://query1.finance.yahoo.com/v8/finance/chart/^GSPC?range=1mo&interval=1d` |
| gold | `https://query1.finance.yahoo.com/v8/finance/chart/GC=F?range=3mo&interval=1d` |
| silver | `https://query1.finance.yahoo.com/v8/finance/chart/SI=F?range=3mo&interval=1d` |
| dxy | `https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB?range=1mo&interval=1d` |
| tip | `https://query1.finance.yahoo.com/v8/finance/chart/TIP?range=1mo&interval=1d` |
| tyx | `https://query1.finance.yahoo.com/v8/finance/chart/^TYX?range=1mo&interval=1d` |

从每个 Yahoo 响应中提取：
- `chart.result[0].meta.regularMarketPrice` → 最新价
- `chart.result[0].meta.fiftyTwoWeekHigh/Low` → 52周高低
- `chart.result[0].indicators.quote[0].close` 最后两个非 null 值 → 计算涨跌幅

## 报告生成

### 强制引用要求

在生成最终报告时，**必须**从 `references/macro-knowledge.md` 中引用相关内容，格式为 **[MK-行号]**（精确到行）。

引用规则：
- 每个分析章节（净流动性、SOFR、MOVE、USDJPY、HYG、CME）至少引用一条对应的 [MK-行号]
- 引用应嵌入分析句子末尾，例如：「SOFR 异常上升说明短端资金变贵，市场进入抛售-偿贷连锁 [MK-53~54]」
- 若当前市场数据触发了"高估值+流动性偏紧"的组合，引用 [MK-3] 和 [MK-5~6]
- 若检测到日元升值信号，引用 [MK-17~19] 和 [MK-67]
- 若 TGA 快速上升，引用 [MK-23~27]
- 若贵金属波动且涉及 CME 保证金话题，引用 [MK-33~37]
- 净流动性公式说明处引用 [MK-45]

在报告末尾添加「引用来源」小节，列出本次报告所有 [MK-行号] 的完整原文。

### 生成脚本调用

将所有数据整合为 JSON 后，调用生成脚本：

```bash
echo '<JSON数据>' | python3 {skillDir}/scripts/generate_report.py
```

**后处理 — 必须添加 MK 引用：**

调用脚本后，还必须完成以下两步：

1. **读取宏观知识库**：立即读取 `references/macro-knowledge.md`，了解各 [MK-行号] 对应的具体内容。

2. **嵌入 MK 引用**：将脚本输出的报告文本作为草稿，在以下位置自然嵌入至少 3 处 [MK-行号] 引用：
   - SOFR 相关分析处 → 参考 [MK-53~54] 或其他 SOFR 相关条目
   - USDJPY/carry trade 处 → 参考 [MK-17~19] 或 [MK-67]
   - HYG/信用利差处 → 参考 [MK-73]
   - ON RRP/净流动性处 → 参考 [MK-45]
   - 综合判断处 → 参考 [MK-3]、[MK-5~6]（高估值+流动性偏紧组合）
   - 黄金/TIPS 处 → 参考 [MK-33~37]（若涉及 CME 保证金）

   引用格式：在分析句子末尾加上 `[MK-行号]`，例如：`短端资金偏紧将放大市场波动 [MK-5~6]`

3. **添加引用来源节**：在报告末尾（在 `*数据来源：...*` 注释之前）添加：
   ```markdown
   ## 引用来源
   - [MK-行号] 引用条目的完整原文
   ```
   从 macro-knowledge.md 中提取被引用条目的原文内容。

JSON 结构：
```json
{
  "fetched_at": "2026-03-18 15:00:00 CST",
  "sofr":   { "date": "...", "rate": 3.70, "vol_bn": 3178, "p25": 3.67, "p75": 3.76, "history": [...] },
  "onrrp":  { "date": "...", "amount_bn": 0.797, "history": [...] },
  "usdjpy": { "price": 158.83, "change": 0.5, "change_pct": 0.32, "52w_high": 159.63, "52w_low": 139.89 },
  "move":   { "price": 79.23, "change": -6.02, "change_pct": -7.07, "52w_high": 140.03, "52w_low": 0 },
  "hyg":    { "price": 79.81, "change": 0.0, "change_pct": 0.0, "52w_high": 81.36, "52w_low": 75.08 },
  "spx":    { "price": 6716.09, "change": -83.13, "change_pct": -1.22, "52w_high": 7002.28, "52w_low": 4835.04 },
  "gold":   { "price": 5011.9, "change": 10.9, "change_pct": 0.22, "52w_high": 5586.2, "52w_low": 2949.7 },
  "silver": { "price": 79.83, "change": 0.3, "change_pct": 0.38, "52w_high": 121.3, "52w_low": 28.31 },
  "dxy":    { "price": 100.38, "change": 3.22, "change_pct": 3.31, "52w_high": 104.68, "52w_low": 95.55 },
  "tip":    { "price": 111.45, "change": 0.22, "change_pct": 0.20, "52w_high": 112.26, "52w_low": 106.47 },
  "tyx":    { "price": 4.852, "change": 0.169, "change_pct": 3.61, "52w_high": 5.152, "52w_low": 0.0 }
}
```

## 发布到 Redoc（可选）

用户说「发给我」「发到文档」时：

```bash
/app/skills/hi-redoc-curd/scripts/hi-redoc-curd.sh -c '<报告内容>'
# 或更新已有文档：
/app/skills/hi-redoc-curd/scripts/hi-redoc-curd.sh -c '<报告内容>' -u <docId>
```

## 分析框架

见 `references/framework.md`，包含：
- 完整流动性传导链路逻辑
- 各指标含义与信号阈值
- CME 保证金机制说明

## 宏观知识库

见 `references/macro-knowledge.md`，包含：
- 高估值 + 流动性偏紧的组合效应机制（"高处的大风"）
- 日债跳涨 → 套息去杠杆 → 全球资产抛售的传导链
- TGA 釜底抽薪机制（银行准备金 → 信贷收缩 → 连锁反应）
- CME 保证金历史案例（白银 11%→18% 的完整过程）
- 各流动性指标的因果逻辑（结算层水位 / 短端钱价 / 利率波动 / 套息底盘 / 信用确认）
- 引用格式：[MK-行号]，**报告中必须精确引用**

## 注意事项

- Yahoo Finance 接口**必须**通过 web_fetch 工具调用，直接 HTTP 请求会被拦截（429）
- 纽约联储接口可直接 HTTP，用脚本拉更高效
- 黄金/白银数据为 3 个月范围，其他为 1 个月
- SOFR 数据通常滞后 1 个交易日
- TIP ETF 价格与实际利率**反向**：TIP 涨 → 实际利率降 → 利好黄金
- DXY 与黄金负相关：美元走强通常压制金价，是黄金最重要的短期对冲变量
- TYX 为 30 年名义利率，配合 TIP 可粗略推算通胀预期（TYX - 实际利率 ≈ 盈亏平衡通胀率）
