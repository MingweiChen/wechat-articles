#!/usr/bin/env python3
# B类信息示意图 — 干净扁平、Noto Sans CJK SC、无发光
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# 中文字体
FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
fp = fm.FontProperties(fname=FONT)
fm.fontManager.addfont(FONT)
plt.rcParams["font.family"] = fp.get_name()
plt.rcParams["axes.unicode_minus"] = False

# 品牌色
ANTH = "#D97757"   # Anthropic/Claude 橙
OAI  = "#10A37F"   # OpenAI 绿
GREY = "#9b9b9b"
DARK = "#2b2b2b"
BG   = "#FFFFFF"

def style_ax(ax):
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")
    ax.tick_params(colors=DARK, labelsize=11)

# ---------- 图02: 企业采用率对比柱状 34.4% vs 32.3% ----------
fig, ax = plt.subplots(figsize=(5.4, 3.7), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
labels = ["Anthropic\n(Claude)", "OpenAI\n(ChatGPT)"]
vals = [34.4, 32.3]
colors = [ANTH, OAI]
bars = ax.bar(labels, vals, color=colors, width=0.52, zorder=3)
for b, v in zip(bars, vals):
    ax.text(b.get_x()+b.get_width()/2, v+0.6, f"{v}%",
            ha="center", va="bottom", fontsize=16, fontweight="bold",
            color=DARK, fontproperties=fp)
# 总体采用率参考线
ax.axhline(50.6, color=GREY, ls="--", lw=1.2, zorder=2)
ax.text(1.46, 50.6, "全美企业\n整体 50.6%", ha="right", va="center",
        fontsize=9, color=GREY, fontproperties=fp)
ax.set_ylim(0, 56)
ax.set_ylabel("企业付费采用率", fontsize=12, color=DARK, fontproperties=fp)
ax.set_title("企业采用率：Anthropic 首次反超 OpenAI",
             fontsize=13.5, fontweight="bold", color=DARK, fontproperties=fp, pad=12)
# 月度变化小标注
ax.text(0, 2, "↑ +3.8", ha="center", color="white", fontsize=10, fontweight="bold", fontproperties=fp)
ax.text(1, 2, "↓ −2.9", ha="center", color="white", fontsize=10, fontweight="bold", fontproperties=fp)
for lbl in ax.get_xticklabels(): lbl.set_fontproperties(fp)
style_ax(ax)
ax.set_yticks([0,10,20,30,40,50])
plt.figtext(0.5, 0.015, "数据：Ramp AI Index 2026 年 5 月（5 万+ 美国企业刷卡/发票）",
            ha="center", fontsize=7.5, color=GREY, fontproperties=fp)
plt.tight_layout(rect=[0,0.04,1,1])
plt.savefig("chart_adoption.png", facecolor=BG, bbox_inches="tight", pad_inches=0.18)
plt.close()
print("chart_adoption.png done")

# ---------- 图03: 一年成长轨迹 9% -> 34.4% vs OpenAI 持平 ----------
fig, ax = plt.subplots(figsize=(5.4, 3.7), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
x = ["2025年5月", "2026年5月"]
anth = [9.0, 34.4]
oai = [32.0, 32.3]
ax.plot(x, anth, "-o", color=ANTH, lw=3, markersize=9, zorder=4, label="Anthropic")
ax.plot(x, oai, "-o", color=OAI, lw=3, markersize=9, zorder=4, label="OpenAI")
# 数值标注
ax.text(0, 9-2.6, "9%", ha="center", color=ANTH, fontsize=12, fontweight="bold", fontproperties=fp)
ax.text(1, 34.4+1.4, "34.4%", ha="center", color=ANTH, fontsize=13, fontweight="bold", fontproperties=fp)
ax.text(0, 32.0+1.4, "32.0%", ha="center", color=OAI, fontsize=12, fontweight="bold", fontproperties=fp)
ax.text(1, 32.3-3.0, "32.3%", ha="center", color=OAI, fontsize=12, fontweight="bold", fontproperties=fp)
# 翻两番标注
ax.annotate("一年翻两番", xy=(0.5, 21), fontsize=11, color=ANTH,
            fontweight="bold", ha="center", fontproperties=fp, rotation=24)
ax.set_ylim(0, 42)
ax.set_ylabel("企业付费采用率", fontsize=12, color=DARK, fontproperties=fp)
ax.set_title("过去一年：Anthropic 翻两番，OpenAI 几乎原地",
             fontsize=13, fontweight="bold", color=DARK, fontproperties=fp, pad=12)
leg = ax.legend(prop=fp, fontsize=11, loc="upper left", frameon=False)
for lbl in ax.get_xticklabels(): lbl.set_fontproperties(fp); lbl.set_fontsize(11)
style_ax(ax)
ax.set_yticks([0,10,20,30,40])
plt.figtext(0.5, 0.015, "数据：Ramp AI Index（OpenAI 同期约 +0.3 个百分点）",
            ha="center", fontsize=7.5, color=GREY, fontproperties=fp)
plt.tight_layout(rect=[0,0.04,1,1])
plt.savefig("chart_growth.png", facecolor=BG, bbox_inches="tight", pad_inches=0.18)
plt.close()
print("chart_growth.png done")

# ---------- 图04: 新客户首选率 Anthropic ~70% ----------
fig, ax = plt.subplots(figsize=(5.4, 3.4), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
# 水平堆叠条：新企业首次为AI付费的正面交锋
seg = [70, 30]
seg_c = [ANTH, OAI]
seg_lbl = ["Anthropic 70%", "OpenAI 30%"]
left = 0
for v, c, l in zip(seg, seg_c, seg_lbl):
    ax.barh(0, v, left=left, color=c, height=0.5, zorder=3)
    ax.text(left+v/2, 0, l, ha="center", va="center", color="white",
            fontsize=13, fontweight="bold", fontproperties=fp)
    left += v
ax.set_xlim(0, 100); ax.set_ylim(-0.6, 0.6)
ax.set_yticks([])
ax.set_xticks([0,25,50,75,100])
ax.set_xticklabels(["0%","25%","50%","75%","100%"], fontproperties=fp)
for s in ["top","right","left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color("#cccccc")
ax.tick_params(colors=DARK, labelsize=10)
ax.set_title("首次为 AI 付费的企业：正面交锋谁被选中",
             fontsize=13, fontweight="bold", color=DARK, fontproperties=fp, pad=14)
ax.text(50, 0.46, "没有历史包袱的新客户，约七成先选 Anthropic",
        ha="center", va="bottom", fontsize=10, color=DARK, fontproperties=fp)
plt.figtext(0.5, 0.02, "数据：Ramp AI Index（新企业首选率，约 70% 对 30%）",
            ha="center", fontsize=7.5, color=GREY, fontproperties=fp)
plt.tight_layout(rect=[0,0.05,1,1])
plt.savefig("chart_firstpick.png", facecolor=BG, bbox_inches="tight", pad_inches=0.18)
plt.close()
print("chart_firstpick.png done")
