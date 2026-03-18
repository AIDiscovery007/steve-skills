#!/usr/bin/env python3
"""
流动性报告生成脚本
读取 fetch_data.py 的 JSON 输出，生成 Markdown 格式的流动性分析报告
"""

import json
import sys
from datetime import datetime

def signal_emoji(value, thresholds, higher_is_bad=True):
    """根据阈值返回信号 emoji"""
    lo, hi = thresholds
    if higher_is_bad:
        if value >= hi:   return "🔴"
        if value >= lo:   return "🟡"
        return "🟢"
    else:
        if value <= lo:   return "🔴"
        if value <= hi:   return "🟡"
        return "🟢"

def fmt_change(change, change_pct):
    sign = "+" if change >= 0 else ""
    return f"{sign}{change:.2f} ({sign}{change_pct:.1f}%)"

def assess_sofr(sofr):
    rate = sofr.get("rate", 0)
    # SOFR > 4.5% 危险，3.8-4.5 需关注，< 3.8 正常（当前降息周期）
    sig = signal_emoji(rate, (3.8, 4.5), higher_is_bad=True)
    note = ""
    if rate > 4.5:
        note = "⚠️ 短端资金明显偏紧，注意流动性压力"
    elif rate > 3.8:
        note = "短端资金略偏紧，需持续观察"
    else:
        note = "短端资金成本正常，无紧张信号"
    return sig, note

def assess_move(move):
    price = move.get("price", 0)
    # MOVE > 130 极端，100-130 偏高，< 100 正常
    sig = signal_emoji(price, (100, 130), higher_is_bad=True)
    note = ""
    if price > 130:
        note = "⚠️ 利率波动极高，杠杆头寸承压，去杠杆风险上升"
    elif price > 100:
        note = "利率波动偏高，中介缩表压力存在"
    else:
        note = "利率波动正常，杠杆环境相对稳定"
    return sig, note

def assess_usdjpy(usdjpy):
    price = usdjpy.get("price", 0)
    change_pct = usdjpy.get("change_pct", 0)
    # 日元快速升值（USDJPY 急跌）是 carry trade 平仓信号
    # 单日跌幅 > 1% 需关注，> 2% 危险
    if change_pct < -2:
        sig = "🔴"
        note = "⚠️ 日元急速升值，套息交易平仓风险极高"
    elif change_pct < -1:
        sig = "🟡"
        note = "日元升值加速，关注 carry trade 平仓动向"
    else:
        sig = "🟢"
        note = "日元走势平稳，套息交易未见明显平仓压力"
    return sig, note

def assess_hyg(hyg):
    price = hyg.get("price", 0)
    change_pct = hyg.get("change_pct", 0)
    w52_high = hyg.get("52w_high", price)
    drawdown = ((price - w52_high) / w52_high * 100) if w52_high else 0
    # HYG 从高位回撤 > 5% 信用收紧明显
    if drawdown < -5:
        sig = "🔴"
        note = f"⚠️ 高收益债信用利差走阔（从52周高位回撤 {drawdown:.1f}%），融资端收紧"
    elif drawdown < -2:
        sig = "🟡"
        note = f"高收益债小幅走弱（回撤 {drawdown:.1f}%），信用端需关注"
    else:
        sig = "🟢"
        note = "高收益债表现稳健，信用利差未见明显走阔"
    return sig, note

def assess_onrrp(onrrp):
    amount = onrrp.get("amount_bn", 0)
    # ON RRP 规模越低，说明流动性已充分释放到市场
    # < 100bn 流动性充裕，100-500bn 中性，> 500bn 流动性偏紧
    if amount > 500:
        sig = "🟡"
        note = f"ON RRP 余额 ${amount:.1f}bn，流动性尚在回收中"
    else:
        sig = "🟢"
        note = f"ON RRP 余额极低（${amount:.1f}bn），流动性已充分释放到市场"
    return sig, note

def assess_gold(gold):
    price = gold.get("price", 0)
    change_pct = gold.get("change_pct", 0)
    w52_high = gold.get("52w_high", price)
    pct_from_high = ((price - w52_high) / w52_high * 100) if w52_high else 0
    note = f"当前 ${price:,.0f}，距52周高点 {pct_from_high:.1f}%"
    if change_pct > 1:
        note += "，今日上涨，避险需求升温"
    elif change_pct < -1:
        note += "，今日下跌，避险情绪降温"
    return "🥇", note

def assess_dxy(dxy):
    price = dxy.get("price", 0)
    change_pct = dxy.get("change_pct", 0)
    w52_high = dxy.get("52w_high", price)
    w52_low = dxy.get("52w_low", price)
    # DXY 强势（高位）对黄金是压力；弱势（低位）对黄金是支撑
    # 以52周区间相对位置判断
    rng = w52_high - w52_low if w52_high != w52_low else 1
    pos_pct = (price - w52_low) / rng * 100
    if pos_pct > 75:
        sig = "🔴"
        note = f"美元处于年内高位（区间位置 {pos_pct:.0f}%），对黄金构成明显压制"
    elif pos_pct > 50:
        sig = "🟡"
        note = f"美元偏强（区间位置 {pos_pct:.0f}%），对黄金有一定压力"
    else:
        sig = "🟢"
        note = f"美元偏弱（区间位置 {pos_pct:.0f}%），对黄金形成支撑"
    if change_pct > 0.5:
        note += f"，今日走强 +{change_pct:.1f}%"
    elif change_pct < -0.5:
        note += f"，今日走弱 {change_pct:.1f}%"
    return sig, note

def assess_tip(tip):
    price = tip.get("price", 0)
    change_pct = tip.get("change_pct", 0)
    w52_high = tip.get("52w_high", price)
    w52_low = tip.get("52w_low", price)
    # TIP 价格与实际利率反向：TIP 涨 → 实际利率降 → 利好黄金
    rng = w52_high - w52_low if w52_high != w52_low else 1
    pos_pct = (price - w52_low) / rng * 100
    if pos_pct > 70:
        sig = "🟢"
        note = f"TIPS 价格偏高（区间位置 {pos_pct:.0f}%），实际利率偏低，对黄金有利"
    elif pos_pct > 40:
        sig = "🟡"
        note = f"TIPS 价格中性（区间位置 {pos_pct:.0f}%），实际利率中性"
    else:
        sig = "🔴"
        note = f"TIPS 价格偏低（区间位置 {pos_pct:.0f}%），实际利率偏高，对黄金不利"
    if change_pct > 0.2:
        note += f"，今日上涨（实际利率下行）→ 利好黄金"
    elif change_pct < -0.2:
        note += f"，今日下跌（实际利率上行）→ 压制黄金"
    return sig, note

def assess_tyx(tyx):
    price = tyx.get("price", 0)
    change_pct = tyx.get("change_pct", 0)
    w52_high = tyx.get("52w_high", price)
    # 30年名义利率高位（>4.8%）对长久期资产有压力
    if price > 5.0:
        sig = "🔴"
        note = f"30年国债收益率 {price:.2f}%，处于高位，长端利率压力大"
    elif price > 4.5:
        sig = "🟡"
        note = f"30年国债收益率 {price:.2f}%，偏高但可控"
    else:
        sig = "🟢"
        note = f"30年国债收益率 {price:.2f}%，处于相对低位"
    if change_pct > 1:
        note += f"，今日上行 +{change_pct:.1f}%"
    elif change_pct < -1:
        note += f"，今日下行 {change_pct:.1f}%"
    return sig, note

def overall_assessment(signals):
    red = signals.count("🔴")
    yellow = signals.count("🟡")
    if red >= 2:
        return "🔴 **高风险** — 多项指标同时亮红，流动性环境显著收紧，建议降低杠杆敞口"
    elif red == 1 or yellow >= 3:
        return "🟡 **中性偏紧** — 部分指标出现预警，流动性环境需持续观察"
    else:
        return "🟢 **相对宽松** — 各项指标未见明显压力，流动性环境尚可"

def generate(data: dict) -> str:
    fetched_at = data.get("fetched_at", "N/A")
    sofr   = data.get("sofr", {})
    usdjpy = data.get("usdjpy", {})
    move   = data.get("move", {})
    hyg    = data.get("hyg", {})
    onrrp  = data.get("onrrp", {})
    spx    = data.get("spx", {})
    gold   = data.get("gold", {})
    silver = data.get("silver", {})

    dxy    = data.get("dxy", {})
    tip    = data.get("tip", {})
    tyx    = data.get("tyx", {})

    sig_sofr,  note_sofr  = assess_sofr(sofr)
    sig_move,  note_move  = assess_move(move)
    sig_usd,   note_usd   = assess_usdjpy(usdjpy)
    sig_hyg,   note_hyg   = assess_hyg(hyg)
    sig_rrp,   note_rrp   = assess_onrrp(onrrp)
    sig_gold,  note_gold  = assess_gold(gold)
    sig_dxy,   note_dxy   = assess_dxy(dxy)
    sig_tip,   note_tip   = assess_tip(tip)
    sig_tyx,   note_tyx   = assess_tyx(tyx)

    overall = overall_assessment([sig_sofr, sig_move, sig_usd, sig_hyg, sig_dxy, sig_tip])

    lines = []
    lines.append(f"# 全球流动性日报")
    lines.append(f"")
    lines.append(f"> 数据更新时间：{fetched_at}")
    lines.append(f"")
    lines.append(f"## 综合判断")
    lines.append(f"")
    lines.append(f"{overall}")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 一、结算层资金（净流动性水位）")
    lines.append(f"")
    lines.append(f"{sig_rrp} **ON RRP（隔夜逆回购）**")
    lines.append(f"- 最新余额：**${onrrp.get('amount_bn', 'N/A'):.2f}B**（{onrrp.get('date', 'N/A')}）")
    lines.append(f"- {note_rrp}")
    lines.append(f"- *注：净流动性 = 美联储总资产 - TGA - ON RRP，ON RRP 余额低 → 流动性已流入市场*")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 二、短端资金价格（SOFR）")
    lines.append(f"")
    lines.append(f"{sig_sofr} **SOFR：{sofr.get('rate', 'N/A')}%**（{sofr.get('date', 'N/A')}）")
    lines.append(f"- 成交量：${sofr.get('vol_bn', 'N/A')}B | P25: {sofr.get('p25', 'N/A')}% | P75: {sofr.get('p75', 'N/A')}%")
    lines.append(f"- {note_sofr}")
    if sofr.get("history"):
        lines.append(f"- 近5日走势：{' → '.join([str(r['rate'])+'%' for r in sofr['history'][:5]])}")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 三、利率波动（MOVE 指数）")
    lines.append(f"")
    lines.append(f"{sig_move} **MOVE：{move.get('price', 'N/A')}**（今日 {fmt_change(move.get('change',0), move.get('change_pct',0))}）")
    lines.append(f"- 52周区间：{move.get('52w_low', 'N/A')} - {move.get('52w_high', 'N/A')}")
    lines.append(f"- {note_move}")
    lines.append(f"- *MOVE 上行 → 利率波动增大 → 中介缩表 → 去杠杆压力上升*")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 四、全球去杠杆链条（USDJPY）")
    lines.append(f"")
    lines.append(f"{sig_usd} **USDJPY：{usdjpy.get('price', 'N/A')}**（今日 {fmt_change(usdjpy.get('change',0), usdjpy.get('change_pct',0))}）")
    lines.append(f"- 52周区间：{usdjpy.get('52w_low', 'N/A')} - {usdjpy.get('52w_high', 'N/A')}")
    lines.append(f"- {note_usd}")
    lines.append(f"- *日元快速升值（USDJPY 急跌）→ 套息交易平仓 → 突发流动性危机*")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 五、信用市场确认（HYG）")
    lines.append(f"")
    lines.append(f"{sig_hyg} **HYG：${hyg.get('price', 'N/A')}**（今日 {fmt_change(hyg.get('change',0), hyg.get('change_pct',0))}）")
    lines.append(f"- 52周区间：${hyg.get('52w_low', 'N/A')} - ${hyg.get('52w_high', 'N/A')}")
    lines.append(f"- {note_hyg}")
    lines.append(f"- *HYG 下跌 = 高收益债利差走阔 = 融资端收紧的确认信号*")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 六、黄金定价核心指标")
    lines.append(f"")
    lines.append(f"{sig_dxy} **美元指数（DXY）：{dxy.get('price', 'N/A'):.3f}**（今日 {fmt_change(dxy.get('change',0), dxy.get('change_pct',0))}）")
    lines.append(f"- 52周区间：{dxy.get('52w_low', 'N/A')} - {dxy.get('52w_high', 'N/A')}")
    lines.append(f"- {note_dxy}")
    lines.append(f"- *美元走强 → 黄金承压；美元走弱 → 黄金受益*")
    lines.append(f"")
    lines.append(f"{sig_tip} **TIPS ETF（TIP）：${tip.get('price', 'N/A'):.2f}**（今日 {fmt_change(tip.get('change',0), tip.get('change_pct',0))}）")
    lines.append(f"- 52周区间：${tip.get('52w_low', 'N/A')} - ${tip.get('52w_high', 'N/A')}")
    lines.append(f"- {note_tip}")
    lines.append(f"- *TIP 价格与实际利率反向；实际利率降 → 黄金最强驱动*")
    lines.append(f"")
    lines.append(f"{sig_tyx} **30年国债收益率（TYX）：{tyx.get('price', 'N/A'):.3f}%**（今日 {fmt_change(tyx.get('change',0), tyx.get('change_pct',0))}）")
    lines.append(f"- 52周区间：{tyx.get('52w_low', 'N/A')}% - {tyx.get('52w_high', 'N/A')}%")
    lines.append(f"- {note_tyx}")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 七、风险资产与避险资产")
    lines.append(f"")
    lines.append(f"**S&P 500：{spx.get('price', 'N/A')}**（今日 {fmt_change(spx.get('change',0), spx.get('change_pct',0))}）")
    lines.append(f"- 52周区间：{spx.get('52w_low', 'N/A')} - {spx.get('52w_high', 'N/A')}")
    lines.append(f"")
    lines.append(f"{sig_gold} **黄金（GC=F）：${gold.get('price', 'N/A'):,.1f}**（今日 {fmt_change(gold.get('change',0), gold.get('change_pct',0))}）")
    lines.append(f"- {note_gold}")
    lines.append(f"")
    lines.append(f"**白银（SI=F）：${silver.get('price', 'N/A')}**（今日 {fmt_change(silver.get('change',0), silver.get('change_pct',0))}）")
    lines.append(f"- 52周区间：${silver.get('52w_low', 'N/A')} - ${silver.get('52w_high', 'N/A')}")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 八、流动性传导链路状态")
    lines.append(f"")
    lines.append(f"```")
    lines.append(f"净流动性水位  {sig_rrp}  ON RRP ${onrrp.get('amount_bn','N/A'):.1f}B")
    lines.append(f"      ↓")
    lines.append(f"短端资金价格  {sig_sofr}  SOFR {sofr.get('rate','N/A')}%")
    lines.append(f"      ↓")
    lines.append(f"利率波动      {sig_move}  MOVE {move.get('price','N/A')}")
    lines.append(f"      ↓")
    lines.append(f"套息交易      {sig_usd}  USDJPY {usdjpy.get('price','N/A')}")
    lines.append(f"      ↓")
    lines.append(f"信用确认      {sig_hyg}  HYG ${hyg.get('price','N/A')}")
    lines.append(f"```")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"*数据来源：纽约联储 Markets Data API、Yahoo Finance v8 API*")

    return "\n".join(lines)

def main():
    raw = sys.stdin.read()
    data = json.loads(raw)
    report = generate(data)
    print(report)

if __name__ == "__main__":
    main()
