#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B类信息示意图：模型战 vs 入口战——Meta 的扬长避短。
传达：Meta 在「比模型」维度落后，转而在「比入口/分发」维度发力。"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

fp = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
font_manager.fontManager.addfont(fp)
cjk = font_manager.FontProperties(fname=fp)
plt.rcParams["font.family"] = cjk.get_name()
plt.rcParams["axes.unicode_minus"] = False

DARK = "#1c2b33"
GREY = "#8a96a0"
RED = "#d64545"     # 短板
GREEN = "#2e9e5b"   # 长板
BLUE = "#1877F2"

fig, ax = plt.subplots(figsize=(7.0, 4.4), dpi=200)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# 两栏对比
ax.text(0.5, 0.95, "两个维度，Meta 换了张牌桌", transform=ax.transAxes,
        ha="center", va="center", fontsize=18, color=DARK,
        fontproperties=cjk, fontweight="bold")

# 左栏：模型战（短板，认了）
lx = 0.27
ax.add_patch(plt.Rectangle((0.04, 0.18), 0.42, 0.62, transform=ax.transAxes,
             facecolor="#fdecec", edgecolor=RED, lw=1.6, zorder=1, clip_on=False))
ax.text(lx, 0.745, "模型战", transform=ax.transAxes, ha="center", fontsize=16,
        color=RED, fontproperties=cjk, fontweight="bold")
ax.text(lx, 0.685, "「谁的模型更聪明」", transform=ax.transAxes, ha="center",
        fontsize=11.5, color="#a85050", fontproperties=cjk)
left_items = [
    "Llama 4 哑火，被同行甩开",
    "基本搁置开源战略",
    "Muse Spark 转闭源",
    "正面比拼 → 认了落后",
]
for i, t in enumerate(left_items):
    y = 0.60 - i*0.095
    ax.text(0.075, y, "•", transform=ax.transAxes, ha="left", fontsize=14,
            color=RED, fontproperties=cjk)
    ax.text(0.11, y, t, transform=ax.transAxes, ha="left", fontsize=11.5,
            color=DARK, fontproperties=cjk)
ax.text(lx, 0.225, "短板：拼不过", transform=ax.transAxes, ha="center",
        fontsize=11.5, color=RED, fontproperties=cjk, fontweight="bold")

# 右栏：入口战（长板，发力）
rx = 0.73
ax.add_patch(plt.Rectangle((0.54, 0.18), 0.42, 0.62, transform=ax.transAxes,
             facecolor="#eafaf0", edgecolor=GREEN, lw=1.6, zorder=1, clip_on=False))
ax.text(rx, 0.745, "入口战", transform=ax.transAxes, ha="center", fontsize=16,
        color=GREEN, fontproperties=cjk, fontweight="bold")
ax.text(rx, 0.685, "「人们在哪儿提问」", transform=ax.transAxes, ha="center",
        fontsize=11.5, color="#3a7d54", fontproperties=cjk)
right_items = [
    "Facebook 搜索上线 AI Mode",
    "27 亿月活现成入口",
    "Groups/Reels 独家存量内容",
    "扬长避短 → 正面切 Google",
]
for i, t in enumerate(right_items):
    y = 0.60 - i*0.095
    ax.text(0.575, y, "•", transform=ax.transAxes, ha="left", fontsize=14,
            color=GREEN, fontproperties=cjk)
    ax.text(0.61, y, t, transform=ax.transAxes, ha="left", fontsize=11.5,
            color=DARK, fontproperties=cjk)
ax.text(rx, 0.225, "长板：没人比它更会分发", transform=ax.transAxes, ha="center",
        fontsize=11.5, color=GREEN, fontproperties=cjk, fontweight="bold")

# 中间箭头
ax.annotate("", xy=(0.535, 0.49), xytext=(0.465, 0.49),
            xycoords="axes fraction",
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.6,
                            mutation_scale=24))
ax.text(0.5, 0.55, "换桌", transform=ax.transAxes, ha="center", fontsize=11,
        color=BLUE, fontproperties=cjk, fontweight="bold")

# 底注
ax.text(0.5, 0.09, "输赢标准从「模型谁更强」悄悄换成「入口谁更稳」",
        transform=ax.transAxes, ha="center", fontsize=11.5, color=GREY,
        fontproperties=cjk, style="italic")

ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.axis("off")
plt.tight_layout(pad=0.4)
plt.savefig("_chart_strategy.png", dpi=200, bbox_inches="tight",
            facecolor="white", pad_inches=0.12)
print("saved _chart_strategy.png")
