#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B类信息示意图: doj-grok-xai-memphis-warmachine
3 张 matplotlib 图: 排污数据 / 三方对撞关系 / AI军事化因果链时间线
中文字体 Noto Sans CJK SC, 中性配色, 禁科幻发光
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# 注册中文字体
FONT_PATH = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
fm.fontManager.addfont(FONT_PATH)
prop = fm.FontProperties(fname=FONT_PATH)
prop_bold = fm.FontProperties(fname=FONT_BOLD)
plt.rcParams["font.family"] = prop.get_name()
plt.rcParams["axes.unicode_minus"] = False

OUT = os.path.dirname(os.path.abspath(__file__))

# 中性配色板
INK = "#2b2b2b"
GRID = "#e6e6e6"
SLATE = "#5b6b7a"      # 数据中心蓝灰
AMBER = "#c77f2e"      # 排放橙
TEAL = "#4a8a7b"       # 环境绿
DUST = "#9aa4ad"       # 浅灰
RED = "#b5453a"        # 强调红(国安)
PAPER = "#fbfaf7"

# ============================================================
# 图01: 孟菲斯燃气电站环境负荷 (B类数据图)
# ============================================================
def chart_emissions():
    fig, axes = plt.subplots(1, 3, figsize=(8.6, 3.5), dpi=150)
    fig.patch.set_facecolor(PAPER)

    # (a) 涡轮机数量区间
    ax = axes[0]
    ax.set_facecolor(PAPER)
    stages = ["早期报道", "NAACP\n起诉主张"]
    low = [35, 57]
    high = [35, 59]
    x = np.arange(len(stages))
    ax.bar(x, high, width=0.55, color=SLATE, alpha=0.35, zorder=2)
    ax.bar(x, low, width=0.55, color=SLATE, zorder=3)
    for i, (lo, hi) in enumerate(zip(low, high)):
        lbl = f"{lo}台" if lo == hi else f"{lo}–{hi}台"
        ax.text(i, hi + 2.5, lbl, ha="center", va="bottom",
                fontproperties=prop_bold, fontsize=11, color=INK)
    ax.set_ylim(0, 72)
    ax.set_xticks(x)
    ax.set_xticklabels(stages, fontproperties=prop, fontsize=9.5, color=INK)
    ax.set_title("就地架设的燃气涡轮机", fontproperties=prop_bold, fontsize=11.5, color=INK, pad=10)
    ax.set_yticks([])
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(DUST)

    # (b) 每年氮氧化物排放
    ax = axes[1]
    ax.set_facecolor(PAPER)
    ax.bar([0], [5300], width=0.5, color=AMBER, zorder=3)
    ax.text(0, 5300 + 180, "5,300+ 吨/年", ha="center", va="bottom",
            fontproperties=prop_bold, fontsize=12.5, color=INK)
    ax.text(0, 2650, "氮氧化物\n(NOx)", ha="center", va="center",
            fontproperties=prop_bold, fontsize=11, color="white")
    ax.set_ylim(0, 6400)
    ax.set_xlim(-0.7, 0.7)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("成烟雾污染物排放", fontproperties=prop_bold, fontsize=11.5, color=INK, pad=10)
    ax.text(0, -650, "全美同类排放大户之一", ha="center", va="top",
            fontproperties=prop, fontsize=9, color=DUST)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(DUST)

    # (c) 每日冷却用水: 现状 vs 规划
    ax = axes[2]
    ax.set_facecolor(PAPER)
    labels = ["当前", "规划扩至"]
    water = [150, 1300]  # 万加仑/天
    x = np.arange(len(labels))
    bars = ax.bar(x, water, width=0.55, color=[TEAL, TEAL], zorder=3)
    bars[1].set_alpha(0.55)
    ax.text(0, 150 + 30, "150万", ha="center", va="bottom",
            fontproperties=prop_bold, fontsize=11, color=INK)
    ax.text(1, 1300 + 30, "1,300万", ha="center", va="bottom",
            fontproperties=prop_bold, fontsize=11, color=INK)
    ax.set_ylim(0, 1500)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontproperties=prop, fontsize=9.5, color=INK)
    ax.set_title("每日冷却用水(加仑)", fontproperties=prop_bold, fontsize=11.5, color=INK, pad=10)
    ax.set_yticks([])
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(DUST)

    fig.suptitle("孟菲斯近郊燃气电站的环境负荷",
                 fontproperties=prop_bold, fontsize=14, color=INK, y=1.02)
    fig.text(0.5, -0.04, "数据来源：NAACP 诉状、南方环境法律中心及公开报道",
             ha="center", fontproperties=prop, fontsize=8.5, color=DUST)
    plt.tight_layout(rect=[0, 0.02, 1, 0.96])
    out = os.path.join(OUT, "01-emissions-load.png")
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=PAPER)
    plt.close()
    print("saved", out)

# ============================================================
# 图03: 三方对撞关系示意图 (B类关系图)
# ============================================================
def chart_three_parties():
    fig, ax = plt.subplots(figsize=(8.4, 4.6), dpi=150)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.4)
    ax.axis("off")

    # 中央法庭节点
    court = FancyBboxPatch((4.05, 3.0), 1.9, 1.1,
                           boxstyle="round,pad=0.06,rounding_size=0.14",
                           linewidth=1.6, edgecolor="#7a6f5f",
                           facecolor="#efe9dd", zorder=4)
    ax.add_patch(court)
    ax.text(5.0, 3.55, "同一个法庭", ha="center", va="center",
            fontproperties=prop_bold, fontsize=12, color=INK)
    ax.text(5.0, 3.18, "案号 3:26-cv-00074", ha="center", va="center",
            fontproperties=prop, fontsize=8, color="#7a6f5f")

    # 三方框: 位置(x,y), 颜色, 标题, 在说什么, 真正争什么
    nodes = [
        # 左上 社区
        dict(xy=(0.35, 5.0), w=3.0, h=1.9, ec=TEAL, fc="#e9f2ee",
             title="NAACP / 社区",
             say="“你违法排污、害我健康”",
             real="争：一个特定社区的呼吸权"),
        # 右上 司法部
        dict(xy=(6.65, 5.0), w=3.0, h=1.9, ec=RED, fc="#f6e9e7",
             title="美国司法部",
             say="“关了它会威胁国家安全”",
             real="争：一台超算的军事价值"),
        # 正下 法律学者
        dict(xy=(3.35, 0.25), w=3.3, h=1.75, ec=SLATE, fc="#e9eef2",
             title="法律学者 / 律所",
             say="“公民诉讼权不能被一句话抹掉”",
             real="争：普通人告状的制度入口"),
    ]
    centers = []
    for n in nodes:
        x, y = n["xy"]; w, h = n["w"], n["h"]
        box = FancyBboxPatch((x, y), w, h,
                             boxstyle="round,pad=0.05,rounding_size=0.12",
                             linewidth=1.5, edgecolor=n["ec"],
                             facecolor=n["fc"], zorder=4)
        ax.add_patch(box)
        cx, cy = x + w/2, y + h/2
        centers.append((cx, cy, x, y, w, h))
        ax.text(cx, y + h - 0.34, n["title"], ha="center", va="center",
                fontproperties=prop_bold, fontsize=11.5, color=INK)
        ax.text(cx, y + h - 0.86, n["say"], ha="center", va="center",
                fontproperties=prop, fontsize=9.3, color="#444")
        ax.text(cx, y + 0.34, n["real"], ha="center", va="center",
                fontproperties=prop_bold, fontsize=9.0, color=n["ec"])

    # 箭头: 三方 -> 法庭
    court_cx, court_cy = 5.0, 3.55
    targets = [
        (centers[0][0], centers[0][1]-0.05, 4.4, 3.95),   # 社区
        (centers[1][0], centers[1][1]-0.05, 5.6, 3.95),   # 司法部
        (centers[2][0], centers[2][1]+0.05, 5.0, 3.0),    # 学者
    ]
    cols = [TEAL, RED, SLATE]
    for (sx, sy, tx, ty), c in zip(targets, cols):
        arr = FancyArrowPatch((sx, sy), (tx, ty),
                              arrowstyle="-|>", mutation_scale=15,
                              linewidth=1.8, color=c, alpha=0.7,
                              connectionstyle="arc3,rad=0.0", zorder=2)
        ax.add_patch(arr)

    ax.text(5.0, 6.95, "三方站在同一法庭，却像在三个房间各自喊话",
            ha="center", va="center", fontproperties=prop_bold,
            fontsize=13.5, color=INK)
    ax.text(5.0, 2.62, "环境正义 · 国家安全 · 公民诉讼权 —— 被「Grok 被定性为战争资产」一次性焊在一起",
            ha="center", va="center", fontproperties=prop, fontsize=8.6, color="#8a8175")

    out = os.path.join(OUT, "03-three-parties.png")
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=PAPER)
    plt.close()
    print("saved", out)

# ============================================================
# 图04: AI军事化因果链 (B类时间线/流程)
# ============================================================
def chart_causal_chain():
    fig, ax = plt.subplots(figsize=(8.0, 5.4), dpi=150)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)
    ax.axis("off")

    steps = [
        dict(y=9.2, c=SLATE, fc="#e9eef2", n="第一环",
             t="AI 数据中心吞电，xAI 绕过常规许可，\n就地架起数十台燃气涡轮机供电"),
        dict(y=7.1, c=TEAL, fc="#e9f2ee", n="第二环",
             t="工厂紧邻以非裔为主的社区，触发环境正义诉讼，\n原告握有用了五十年的「公民诉讼」工具"),
        dict(y=5.0, c=AMBER, fc="#f6efe2", n="第三环 · 拐点",
             t="xAI 训练的 Grok 被军方深度采用，\n政府因此有了亲自下场保这家工厂的动机"),
        dict(y=2.9, c=RED, fc="#f6e9e7", n="第四环",
             t="政府保它的方式不是自证合法，\n而是搬出「国家安全」让整桩公民诉讼失效"),
    ]
    box_w = 7.6
    box_h = 1.45
    cx = 5.0
    for i, s in enumerate(steps):
        x = cx - box_w/2
        y = s["y"] - box_h/2
        box = FancyBboxPatch((x, y), box_w, box_h,
                             boxstyle="round,pad=0.05,rounding_size=0.12",
                             linewidth=1.5, edgecolor=s["c"],
                             facecolor=s["fc"], zorder=4)
        ax.add_patch(box)
        # 序号徽标
        badge = mpatches.FancyBboxPatch((x+0.12, s["y"]-0.34), 1.32, 0.68,
                                        boxstyle="round,pad=0.02,rounding_size=0.1",
                                        linewidth=0, facecolor=s["c"], zorder=5)
        ax.add_patch(badge)
        ax.text(x+0.78, s["y"], s["n"], ha="center", va="center",
                fontproperties=prop_bold, fontsize=9.5, color="white", zorder=6)
        ax.text(x+1.62, s["y"], s["t"], ha="left", va="center",
                fontproperties=prop, fontsize=9.6, color=INK, zorder=6)
        # 向下箭头
        if i < len(steps) - 1:
            arr = FancyArrowPatch((cx, s["y"]-box_h/2-0.02),
                                  (cx, steps[i+1]["y"]+box_h/2+0.02),
                                  arrowstyle="-|>", mutation_scale=17,
                                  linewidth=2.0, color="#9aa4ad", zorder=3)
            ax.add_patch(arr)

    # 结论条
    concl = FancyBboxPatch((0.6, 0.25), 8.8, 1.25,
                           boxstyle="round,pad=0.05,rounding_size=0.12",
                           linewidth=1.6, edgecolor="#7a6f5f",
                           facecolor="#efe9dd", zorder=4)
    ax.add_patch(concl)
    ax.text(5.0, 0.88,
            "一旦商用 AI 被写进战争机器，它的工厂可能获得普通企业拿不到的法律豁免——\n而代价未必落在战场上，可能落在它隔壁社区的空气里",
            ha="center", va="center", fontproperties=prop_bold,
            fontsize=9.8, color="#5a4f3f", zorder=5)

    ax.text(5.0, 10.55, "一条没人串起来的因果链",
            ha="center", va="center", fontproperties=prop_bold,
            fontsize=14.5, color=INK)

    out = os.path.join(OUT, "04-causal-chain.png")
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=PAPER)
    plt.close()
    print("saved", out)

if __name__ == "__main__":
    chart_emissions()
    chart_three_parties()
    chart_causal_chain()
    print("ALL DONE")
