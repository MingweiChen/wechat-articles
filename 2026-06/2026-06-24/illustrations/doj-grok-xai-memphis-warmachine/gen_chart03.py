#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""图03 重做: 三方对撞关系示意图 (B类关系图) — 修复文字不显示 + 标题重叠"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

FONT_PATH = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
fm.fontManager.addfont(FONT_PATH)
prop = fm.FontProperties(fname=FONT_PATH)
prop_bold = fm.FontProperties(fname=FONT_BOLD)
plt.rcParams["font.family"] = prop.get_name()
plt.rcParams["axes.unicode_minus"] = False

OUT = os.path.dirname(os.path.abspath(__file__))
INK = "#2b2b2b"; SLATE = "#5b6b7a"; TEAL = "#4a8a7b"; RED = "#b5453a"
PAPER = "#fbfaf7"

def chart_three_parties():
    fig, ax = plt.subplots(figsize=(8.6, 5.4), dpi=150)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9.2)
    ax.axis("off")

    # 标题 (留足顶部空间)
    ax.text(5.0, 8.85, "三方站在同一法庭，却像在三个房间各自喊话",
            ha="center", va="center", fontproperties=prop_bold,
            fontsize=14, color=INK, zorder=10)

    # 三方框
    nodes = [
        dict(xy=(0.35, 6.05), w=3.05, h=2.0, ec=TEAL, fc="#e9f2ee",
             title="NAACP / 社区",
             say="“你违法排污、害我健康”",
             real="争：一个特定社区的呼吸权"),
        dict(xy=(6.60, 6.05), w=3.05, h=2.0, ec=RED, fc="#f6e9e7",
             title="美国司法部",
             say="“关了它会威胁国家安全”",
             real="争：一台超算的军事价值"),
        dict(xy=(3.30, 0.55), w=3.40, h=1.9, ec=SLATE, fc="#e9eef2",
             title="法律学者 / 律所",
             say="“公民诉讼权不能被一句话抹掉”",
             real="争：普通人告状的制度入口"),
    ]
    centers = []
    for n in nodes:
        x, y = n["xy"]; w, h = n["w"], n["h"]
        box = FancyBboxPatch((x, y), w, h,
                             boxstyle="round,pad=0.05,rounding_size=0.12",
                             linewidth=1.6, edgecolor=n["ec"],
                             facecolor=n["fc"], zorder=2)
        ax.add_patch(box)
        cx = x + w/2
        centers.append((cx, y, w, h))
        # 文字 zorder 高于 box
        ax.text(cx, y + h - 0.40, n["title"], ha="center", va="center",
                fontproperties=prop_bold, fontsize=12, color=INK, zorder=5)
        ax.text(cx, y + h - 0.95, n["say"], ha="center", va="center",
                fontproperties=prop, fontsize=9.6, color="#444", zorder=5)
        ax.text(cx, y + 0.40, n["real"], ha="center", va="center",
                fontproperties=prop_bold, fontsize=9.4, color=n["ec"], zorder=5)

    # 中央法庭节点
    court_x, court_y, court_w, court_h = 3.95, 3.55, 2.1, 1.25
    court = FancyBboxPatch((court_x, court_y), court_w, court_h,
                           boxstyle="round,pad=0.06,rounding_size=0.14",
                           linewidth=1.8, edgecolor="#7a6f5f",
                           facecolor="#efe9dd", zorder=3)
    ax.add_patch(court)
    ccx, ccy = court_x + court_w/2, court_y + court_h/2
    ax.text(ccx, ccy + 0.24, "同一个法庭", ha="center", va="center",
            fontproperties=prop_bold, fontsize=12.5, color=INK, zorder=6)
    ax.text(ccx, ccy - 0.22, "案号 3:26-cv-00074", ha="center", va="center",
            fontproperties=prop, fontsize=8.5, color="#7a6f5f", zorder=6)

    # 箭头: 三方 -> 法庭 (从框边缘到法庭边缘)
    arrows = [
        ((centers[0][0]+0.5, 6.05), (court_x+0.35, court_y+court_h-0.05), TEAL),   # 社区左上->法庭左上
        ((centers[1][0]-0.5, 6.05), (court_x+court_w-0.35, court_y+court_h-0.05), RED),  # 司法部右上->法庭右上
        ((centers[2][0], 0.55+1.9), (ccx, court_y), SLATE),                         # 学者下->法庭底
    ]
    for (sx, sy), (tx, ty), c in arrows:
        arr = FancyArrowPatch((sx, sy), (tx, ty),
                              arrowstyle="-|>", mutation_scale=16,
                              linewidth=2.0, color=c, alpha=0.75, zorder=1)
        ax.add_patch(arr)

    # 底部说明
    ax.text(5.0, 0.18,
            "环境正义 · 国家安全 · 公民诉讼权 —— 被「Grok 被定性为战争资产」一次性焊在一起",
            ha="center", va="center", fontproperties=prop, fontsize=9, color="#8a8175", zorder=10)

    out = os.path.join(OUT, "03-three-parties.png")
    plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=PAPER)
    plt.close()
    print("saved", out)

if __name__ == "__main__":
    chart_three_parties()
