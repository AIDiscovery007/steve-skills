#!/usr/bin/env python3
"""
黄金投资分析报告生成脚本
从 stdin 读取 fetch_gold_data.py 的 JSON 输出，生成结构化分析报告
"""

import json
import sys

# ── 工具函数 ──────────────────────────────────────────────────────────────────

def fmt_chg(change, change_pct):
    s = "+" if change >= 0 else ""
    return f"{s}{change:.2f} ({s}{change_pct:.1f}%)"

def range_pos(price, low, high):
    """返回价格在52周区间的百分位（0-100）"""
    rng = high - low
    if rng <= 0:
        return 50
    return max(0, min(100, (price - low) / rng * 100))

def sig(value, red_thresh, yellow_thresh, higher_is_bad=True):
    if higher_is_bad:
        if value >= red_thresh:   return "🔴"
        if value >= yellow_thresh: return "🟡"
        return "🟢"
    else:
        if value <= red_thresh:   return "🔴"
        if value <= yellow_thresh: return "🟡"
        return "🟢"

# ── 各指标评估 ────────────────────────────────────────────────────────────────

def eval_gold(d):
    p = d["price"]
    h = d["52w_high"]
    l = d["52w_low"]
    pos = range_pos(p, l, h)
    pct_from_high = (p - h) / h * 100
    pct_from_low  = (p - l) / l * 100

    trend = "–"
    hist = d.get("history_30d", [])
    if len(hist) >= 10:
        avg10 = sum(hist[-10:]) / 10
        avg30 = sum(hist) / len(hist)
        if avg10 > avg30 * 1.01:
            trend = "📈 短期均线在长期均线上方，趋势偏多"
        elif avg10 < avg30 * 0.99:
            trend = "📉 短期均线在长期均线下方，趋势偏空"
        else:
            trend = "➡️ 均线粘合，趋势不明"

    return {
        "signal": "🥇",
        "price": p,
        "pos": pos,
        "pct_from_high": pct_from_high,
        "pct_from_low": pct_from_low,
        "trend": trend,
        "52w_high": h,
        "52w_low": l,
    }

def eval_dxy(d):
    p = d["price"]
    pos = range_pos(p, d["52w_low"], d["52w_high"])
    if pos > 75:
        s, note = "🔴", f"美元强势（年内区间位置 {pos:.0f}%），对黄金构成明显压制"
    elif pos > 50:
        s, note = "🟡", f"美元偏强（年内区间位置 {pos:.0f}%），对黄金有一定压力"
    else:
        s, note = "🟢", f"美元偏弱（年内区间位置 {pos:.0f}%），对黄金形成支撑"
    return s, note, pos

def eval_tip(d):
    p = d["price"]
    pos = range_pos(p, d["52w_low"], d["52w_high"])
    # TIP 价格高 → 实际利率低 → 利好黄金
    if pos > 70:
        s, note = "🟢", f"TIPS 价格高位（区间位置 {pos:.0f}%）→ 实际利率偏低，支撑黄金"
    elif pos > 40:
        s, note = "🟡", f"TIPS 价格中性（区间位置 {pos:.0f}%）→ 实际利率中性"
    else:
        s, note = "🔴", f"TIPS 价格低位（区间位置 {pos:.0f}%）→ 实际利率偏高，压制黄金"
    return s, note, pos

def eval_tyx(d):
    p = d["price"]
    if p > 5.0:
        s, note = "🔴", f"30年国债 {p:.2f}%，高位压力大，长端利率对贵金属不利"
    elif p > 4.5:
        s, note = "🟡", f"30年国债 {p:.2f}%，偏高但可控"
    else:
        s, note = "🟢", f"30年国债 {p:.2f}%，处于低位，对黄金友好"
    return s, note

def eval_move(d):
    p = d["price"]
    if p > 130:
        s, note = "🔴", f"MOVE {p:.0f}，利率波动极高，去杠杆风险大，黄金可能被短暂抛售"
    elif p > 100:
        s, note = "🟡", f"MOVE {p:.0f}，利率波动偏高，关注机构杠杆压力"
    elif p > 80:
        s, note = "🟡", f"MOVE {p:.0f}，利率波动温和偏高"
    else:
        s, note = "🟢", f"MOVE {p:.0f}，市场平静，杠杆环境宽松，有利于黄金持仓"
    return s, note

def eval_usdjpy(d):
    chg_pct = d.get("change_pct", 0)
    p = d["price"]
    if chg_pct < -2:
        s, note = "🔴", f"日元急速升值（USDJPY {p:.2f}，日内 {chg_pct:.1f}%），套息平仓风险极高"
    elif chg_pct < -1:
        s, note = "🟡", f"日元升值加速（USDJPY {p:.2f}），关注 carry trade 平仓"
    else:
        s, note = "🟢", f"USDJPY {p:.2f}，套息交易平稳，无平仓压力"
    return s, note

def eval_hyg(d):
    p = d["price"]
    h = d["52w_high"]
    drawdown = (p - h) / h * 100 if h else 0
    if drawdown < -5:
        s, note = "🔴", f"HYG ${p:.2f}，从高位回撤 {drawdown:.1f}%，信用利差走阔，融资端收紧"
    elif drawdown < -2:
        s, note = "🟡", f"HYG ${p:.2f}，小幅回撤 {drawdown:.1f}%，信用端需关注"
    else:
        s, note = "🟢", f"HYG ${p:.2f}，信用利差稳定，融资环境正常"
    return s, note

# ── 综合评分与建议 ────────────────────────────────────────────────────────────

def score_and_suggest(signals, gold_info, dxy_pos, tip_pos):
    reds    = signals.count("🔴")
    yellows = signals.count("🟡")
    greens  = signals.count("🟢")

    # 0-100 分，每个绿+15，黄+7，红-20
    score = greens * 15 + yellows * 7 - reds * 20
    score = max(0, min(100, score))

    pos = gold_info["pos"]
    pct_from_high = gold_info["pct_from_high"]

    # 仓位建议
    if score >= 70:
        stance = "🟢 **积极做多**"
        action = "多指标支撑，趋势明确，可持仓/加仓"
    elif score >= 50:
        stance = "🟡 **谨慎持有**"
        action = "环境偏友好但有分歧，维持现有仓位，等待更强信号"
    elif score >= 30:
        stance = "🟡 **观望为主**"
        action = "信号混杂，建议等待关键指标明朗后再动"
    else:
        stance = "🔴 **规避/减仓**"
        action = "多项指标亮红，流动性压力或美元走强，建议降低敞口"

    # 入场区间建议（基于当前价和技术位）
    price = gold_info["price"]
    entry_low  = round(price * 0.97, 0)   # -3%
    entry_high = round(price * 0.99, 0)   # -1%
    stop_loss  = round(price * 0.95, 0)   # -5%
    target     = round(price * 1.08, 0)   # +8%

    if pos > 80:
        entry_note = f"当前价格处于年内高位（区间 {pos:.0f}%），**不建议追高**，等回调至 ${entry_low:,.0f}–${entry_high:,.0f} 再介入"
    elif pos > 50:
        entry_note = f"价格在区间中上段（{pos:.0f}%），可分批建仓，理想介入区间 ${entry_low:,.0f}–${entry_high:,.0f}"
    else:
        entry_note = f"价格在区间中下段（{pos:.0f}%），性价比较好，可考虑积极介入"

    return score, stance, action, entry_note, stop_loss, target

# ── 报告生成 ──────────────────────────────────────────────────────────────────

def generate(data: dict) -> str:
    fetched_at = data.get("fetched_at", "N/A")

    gold_raw   = data.get("gold", {})
    silver_raw = data.get("silver", {})
    dxy_raw    = data.get("dxy", {})
    tip_raw    = data.get("tip", {})
    tyx_raw    = data.get("tyx", {})
    move_raw   = data.get("move", {})
    usdjpy_raw = data.get("usdjpy", {})
    hyg_raw    = data.get("hyg", {})
    spx_raw    = data.get("spx", {})

    gold_info          = eval_gold(gold_raw)
    sig_dxy, note_dxy, dxy_pos = eval_dxy(dxy_raw)
    sig_tip, note_tip, tip_pos = eval_tip(tip_raw)
    sig_tyx, note_tyx          = eval_tyx(tyx_raw)
    sig_move, note_move        = eval_move(move_raw)
    sig_usd,  note_usd         = eval_usdjpy(usdjpy_raw)
    sig_hyg,  note_hyg         = eval_hyg(hyg_raw)

    all_signals = [sig_dxy, sig_tip, sig_tyx, sig_move, sig_usd, sig_hyg]
    score, stance, action, entry_note, stop_loss, target = score_and_suggest(
        all_signals, gold_info, dxy_pos, tip_pos
    )

    g = gold_raw
    s = silver_raw
    spx = spx_raw

    lines = []
    lines.append("# 黄金投资分析报告")
    lines.append("")
    lines.append(f"> 数据更新：{fetched_at}")
    lines.append("")

    # ── 综合判断 ──
    lines.append("## 综合判断")
    lines.append("")
    lines.append(f"**评分：{score}/100**　　{stance}")
    lines.append("")
    lines.append(f"> {action}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── 黄金本体 ──
    lines.append("## 一、黄金价格（GC=F）")
    lines.append("")
    lines.append(f"- **现价：${g['price']:,.1f}**　今日 {fmt_chg(g.get('change',0), g.get('change_pct',0))}")
    lines.append(f"- 52周区间：${g['52w_low']:,.0f} – ${g['52w_high']:,.0f}　区间位置：**{gold_info['pos']:.0f}%**")
    lines.append(f"- 距52周高点：{gold_info['pct_from_high']:.1f}%　距52周低点：+{gold_info['pct_from_low']:.1f}%")
    lines.append(f"- 趋势：{gold_info['trend']}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── 黄金定价三要素 ──
    lines.append("## 二、黄金定价核心三要素")
    lines.append("")
    lines.append(f"### {sig_dxy} 美元指数（DXY）：{dxy_raw.get('price', 'N/A'):.3f}")
    lines.append(f"- 今日 {fmt_chg(dxy_raw.get('change',0), dxy_raw.get('change_pct',0))}")
    lines.append(f"- {note_dxy}")
    lines.append(f"- *美元与黄金负相关，是最重要的短期压制/支撑变量*")
    lines.append("")
    lines.append(f"### {sig_tip} 实际利率（TIP ETF）：${tip_raw.get('price', 'N/A'):.2f}")
    lines.append(f"- 今日 {fmt_chg(tip_raw.get('change',0), tip_raw.get('change_pct',0))}")
    lines.append(f"- {note_tip}")
    lines.append(f"- *TIP 价格上涨 = 实际利率下降 = 黄金最强结构性驱动力*")
    lines.append("")
    lines.append(f"### {sig_tyx} 名义长端利率（TYX 30年）：{tyx_raw.get('price', 'N/A'):.3f}%")
    lines.append(f"- 今日 {fmt_chg(tyx_raw.get('change',0), tyx_raw.get('change_pct',0))}")
    lines.append(f"- {note_tyx}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── 流动性风险指标 ──
    lines.append("## 三、流动性与风险环境")
    lines.append("")
    lines.append(f"### {sig_move} 利率波动（MOVE）：{move_raw.get('price', 'N/A'):.1f}")
    lines.append(f"- 今日 {fmt_chg(move_raw.get('change',0), move_raw.get('change_pct',0))}")
    lines.append(f"- {note_move}")
    lines.append("")
    lines.append(f"### {sig_usd} 套息交易压力（USDJPY）：{usdjpy_raw.get('price', 'N/A'):.3f}")
    lines.append(f"- 今日 {fmt_chg(usdjpy_raw.get('change',0), usdjpy_raw.get('change_pct',0))}")
    lines.append(f"- {note_usd}")
    lines.append("")
    lines.append(f"### {sig_hyg} 信用市场（HYG）：${hyg_raw.get('price', 'N/A'):.2f}")
    lines.append(f"- 今日 {fmt_chg(hyg_raw.get('change',0), hyg_raw.get('change_pct',0))}")
    lines.append(f"- {note_hyg}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── 参考资产 ──
    lines.append("## 四、参考资产")
    lines.append("")
    if spx:
        lines.append(f"- **S&P 500：{spx.get('price', 'N/A'):,.2f}**　今日 {fmt_chg(spx.get('change',0), spx.get('change_pct',0))}")
    if s:
        lines.append(f"- **白银（SI=F）：${s.get('price', 'N/A'):.2f}**　今日 {fmt_chg(s.get('change',0), s.get('change_pct',0))}　（金银比：{g['price']/s['price']:.1f}x）")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── 操作建议 ──
    lines.append("## 五、操作建议")
    lines.append("")
    lines.append(f"**{entry_note}**")
    lines.append("")
    lines.append(f"| 参数 | 价位 |")
    lines.append(f"|------|------|")
    lines.append(f"| 当前价 | ${g['price']:,.1f} |")
    lines.append(f"| 止损参考 | ${stop_loss:,.0f}（-{(g['price']-stop_loss)/g['price']*100:.1f}%） |")
    lines.append(f"| 目标参考 | ${target:,.0f}（+{(target-g['price'])/g['price']*100:.1f}%） |")
    lines.append("")
    lines.append("**主要关注变量（按优先级）：**")
    lines.append("1. DXY 是否在 101 上方企稳或转头 → 黄金最关键短期变量")
    lines.append("2. TIP 走势 → 实际利率方向，决定中期仓位")
    lines.append("3. MOVE 是否持续回落 → 市场稳定性确认")
    lines.append("")
    lines.append("---")
    lines.append("*数据来源：Yahoo Finance v8 API*")

    return "\n".join(lines)

def main():
    raw = sys.stdin.read()
    data = json.loads(raw)
    print(generate(data))

if __name__ == "__main__":
    main()
