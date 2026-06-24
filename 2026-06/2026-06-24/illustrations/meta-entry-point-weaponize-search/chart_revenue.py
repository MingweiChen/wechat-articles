#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B类信息示意图：摩根士丹利对 AI Mode 入口规模与潜在年收入的估算口径。
传达：27亿月活 → 估算留存约10亿 → 提问变现10% → 年收入超100亿美元。"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch

# 中文字体 Noto Sans CJK SC
fp = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
font_manager.fontManager.addfont(fp)
cjk = font_manager.FontProperties(fname=fp)
plt.rcParams["font.family"] = cjk.get_name()
plt.rcParams["axes.unicode_minus"] = False

BLUE = "#1877F2"   # Facebook 蓝
DARK = "#1c2b33"
GREY = "#8a96a0"
LIGHT = "#e8eef3"

fig, ax = plt.subplots(figsize=(7.0, 4.5), dpi=200)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# 漏斗式三段：月活 -> 估算留存 -> 潜在年收入（用并排卡片表示量级递进）
stages = [
    ("Facebook\n全球月活", "约 27 亿", "人", BLUE),
    ("估算留存\n(约 1/3)", "约 10 亿", "人", "#4a90e2"),
    ("潜在年收入\n(提问 10% 变现)", "100+", "亿美元", "#34a853"),
]

xs = [0.16, 0.5, 0.84]
ytop = 0.70
box_w = 0.24
box_h = 0.34

for (title, big, unit, color), x in zip(stages, xs):
    # 卡片
    ax.add_patch(plt.Rectangle((x - box_w/2, ytop - box_h), box_w, box_h,
                               transform=ax.transAxes, facecolor=color,
                               edgecolor="none", zorder=2, alpha=0.95,
                               clip_on=False))
    ax.text(x, ytop - 0.07, big, transform=ax.transAxes, ha="center",
            va="center", fontsize=23, color="white", fontproperties=cjk,
            fontweight="bold", zorder=3)
    ax.text(x, ytop - 0.155, unit, transform=ax.transAxes, ha="center",
            va="center", fontsize=12.5, color="white", fontproperties=cjk, zorder=3)
    ax.text(x, ytop - 0.27, title, transform=ax.transAxes, ha="center",
            va="center", fontsize=12, color="white", fontproperties=cjk, zorder=3)

# 箭头连接
for x0, x1 in [(xs[0], xs[1]), (xs[1], xs[2])]:
    arr = FancyArrowPatch((x0 + box_w/2 + 0.005, ytop - box_h/2),
                          (x1 - box_w/2 - 0.005, ytop - box_h/2),
                          transform=ax.transAxes, arrowstyle="-|>",
                          mutation_scale=22, color=GREY, lw=2.2, zorder=1,
                          clip_on=False)
    ax.add_patch(arr)

# 标题
ax.text(0.5, 0.93, "摩根士丹利怎么给「入口」估价", transform=ax.transAxes,
        ha="center", va="center", fontsize=18, color=DARK,
        fontproperties=cjk, fontweight="bold")
ax.text(0.5, 0.85, "不靠模型更强，只靠「十亿量级、每天有人用的入口」",
        transform=ax.transAxes, ha="center", va="center", fontsize=12.5,
        color=GREY, fontproperties=cjk)

# 底部提示：估算口径
ax.text(0.5, 0.085, "※ 均为分析师基于月活量级的估算口径，非已发生业绩或承诺",
        transform=ax.transAxes, ha="center", va="center", fontsize=10.5,
        color=GREY, fontproperties=cjk, style="italic")

ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.axis("off")
plt.tight_layout(pad=0.4)
plt.savefig("_chart_revenue.png", dpi=200, bbox_inches="tight",
            facecolor="white", pad_inches=0.12)
print("saved _chart_revenue.png")
