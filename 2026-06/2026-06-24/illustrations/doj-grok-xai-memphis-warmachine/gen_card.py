#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""图02 (B类 fact-card): xAI/Grok 品牌标识 + 司法部动议的关键产业事实
- 用真实 xAI logo (Wikimedia Commons, 4 polygons 自绘)
- 配关键数据: Grok 政府版被军方采用 / "战争关键基础设施" 认定
- 合规: 无军事画面, 只有品牌标识 + 数字事实卡
中文字体 Noto Sans CJK SC, 中性配色, 禁科幻发光
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, re

OUT = os.path.dirname(os.path.abspath(__file__))
SVG = os.path.join(OUT, "xai_logo_raw.svg")

FONT_REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
FONT_BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"

# 配色 (与图表统一)
INK = (43, 43, 43)
PAPER = (251, 250, 247)
SLATE = (91, 107, 122)
RED = (181, 69, 58)
DUST = (138, 129, 117)
CARD = (255, 255, 255)
LINE = (225, 222, 215)

def load_logo_polys():
    txt = open(SVG).read()
    polys = []
    for m in re.findall(r'points="([^"]+)"', txt):
        pts = []
        nums = re.findall(r'[-\d.]+', m)
        for i in range(0, len(nums), 2):
            pts.append((float(nums[i]), float(nums[i+1])))
        polys.append(pts)
    return polys  # viewBox 0 0 841.89 595.28

def render_logo(target_h, color=INK, pad_frac=0.0):
    """渲染 xAI logo 到透明 PNG, 高度=target_h (超采样抗锯齿)。logo 实际占 y56-538."""
    polys = load_logo_polys()
    # bounding box of actual ink
    xs = [p[0] for poly in polys for p in poly]
    ys = [p[1] for poly in polys for p in poly]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    w0, h0 = maxx - minx, maxy - miny
    SS = 4
    scale = (target_h * SS) / h0
    W = int(w0 * scale) + 2
    H = int(h0 * scale) + 2
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for poly in polys:
        pp = [((x - minx) * scale + 1, (y - miny) * scale + 1) for (x, y) in poly]
        d.polygon(pp, fill=color + (255,))
    im = im.resize((W // SS, H // SS), Image.LANCZOS)
    return im

def text_w(draw, s, font):
    b = draw.textbbox((0, 0), s, font=font)
    return b[2] - b[0]

def build_card():
    W, H = 1120, 760
    SS = 2  # 整图超采样
    img = Image.new("RGB", (W*SS, H*SS), PAPER)
    d = ImageDraw.Draw(img)

    def F(path, size):
        return ImageFont.truetype(path, size*SS)

    f_title = F(FONT_BOLD, 30)
    f_brand = F(FONT_BOLD, 40)
    f_sub = F(FONT_REG, 19)
    f_big = F(FONT_BOLD, 52)
    f_big_unit = F(FONT_BOLD, 21)
    f_lbl = F(FONT_REG, 18)
    f_tag = F(FONT_BOLD, 23)
    f_foot = F(FONT_REG, 16)
    f_quote = F(FONT_BOLD, 26)

    M = 60 * SS
    # ---- 顶部标题 ----
    d.text((M, 42*SS), "司法部动议捅破的一层窗户纸", font=f_title, fill=INK)
    d.text((M, 86*SS), "一个人人能在手机上调用的商用聊天机器人，被正式写进战争关键基础设施",
           font=f_sub, fill=DUST)

    # ---- 品牌行: xAI logo + 文字 ----
    brand_y = 150 * SS
    logo = render_logo(target_h=46*SS, color=INK)
    img.paste(logo, (M, brand_y), logo)
    lx = M + logo.size[0] + 22*SS
    d.text((lx, brand_y - 2*SS), "xAI · Grok", font=f_brand, fill=INK)
    by2 = brand_y + 52*SS
    d.text((lx, by2), "已并入 SpaceX · 政府版被国防部深度采用",
           font=f_lbl, fill=SLATE)

    # 分隔线
    ly = 250 * SS
    d.line([(M, ly), (W*SS - M, ly)], fill=LINE, width=2*SS)

    # ---- 三联数据卡: 司法部宣誓证词披露 ----
    d.text((M, ly + 24*SS), "司法部宣誓证词披露的关键产业事实",
           font=F(FONT_BOLD, 22), fill=INK)

    card_y = ly + 70*SS
    card_h = 200*SS
    gap = 26*SS
    cw = (W*SS - 2*M - 2*gap) // 3
    cards = [
        ("96", "小时", "对伊朗军事行动的时间窗口"),
        ("2,000+", "枚弹药", "由 Grok 政府版协助投放"),
        ("2,000", "个目标", "在同一行动中被覆盖"),
    ]
    for i, (num, unit, lbl) in enumerate(cards):
        cx = M + i * (cw + gap)
        # 卡片底
        d.rounded_rectangle([cx, card_y, cx + cw, card_y + card_h],
                            radius=18*SS, fill=CARD, outline=LINE, width=2*SS)
        # 左侧色条
        d.rounded_rectangle([cx, card_y, cx + 8*SS, card_y + card_h],
                            radius=4*SS, fill=SLATE)
        # 数字
        nb = d.textbbox((0,0), num, font=f_big)
        nw = nb[2]-nb[0]
        d.text((cx + cw//2 - nw//2, card_y + 34*SS), num, font=f_big, fill=INK)
        # 单位
        ub = d.textbbox((0,0), unit, font=f_big_unit)
        uw = ub[2]-ub[0]
        d.text((cx + cw//2 - uw//2, card_y + 104*SS), unit, font=f_big_unit, fill=SLATE)
        # 标签 (居中, 可能换行)
        words = lbl
        lb = d.textbbox((0,0), words, font=f_lbl)
        lw = lb[2]-lb[0]
        if lw > cw - 24*SS:
            # 简单二分换行
            mid = len(words)//2
            # 找最近空格/标点 — 中文按字符
            line1, line2 = words[:mid], words[mid:]
            for s, yy in [(line1, 150), (line2, 174)]:
                b = d.textbbox((0,0), s, font=f_lbl); ww=b[2]-b[0]
                d.text((cx + cw//2 - ww//2, card_y + yy*SS), s, font=f_lbl, fill=DUST)
        else:
            d.text((cx + cw//2 - lw//2, card_y + 158*SS), words, font=f_lbl, fill=DUST)

    # ---- 底部认定标签条 ----
    tag_y = card_y + card_h + 36*SS
    tag_h = 88*SS
    d.rounded_rectangle([M, tag_y, W*SS - M, tag_y + tag_h],
                        radius=16*SS, fill=(246, 233, 231), outline=RED, width=2*SS)
    # 红色标记点
    d.ellipse([M + 28*SS, tag_y + tag_h//2 - 7*SS, M + 42*SS, tag_y + tag_h//2 + 7*SS], fill=RED)
    d.text((M + 60*SS, tag_y + 16*SS),
           "政府用法庭文件正式认定：", font=F(FONT_REG, 19), fill=(120,60,52))
    d.text((M + 60*SS, tag_y + 44*SS),
           "国防部「主要的涉密算力基础设施提供方」· 提供其他前沿模型没有的功能",
           font=F(FONT_BOLD, 20), fill=(150,55,48))

    # ---- 页脚 ----
    d.text((M, H*SS - 40*SS),
           "数据来源：美国司法部 6 月 15 日动议 · 国防部首席数字和人工智能官宣誓证词　|　标识：xAI (Wikimedia Commons)",
           font=f_foot, fill=DUST)

    img = img.resize((W, H), Image.LANCZOS)
    out = os.path.join(OUT, "02-grok-warmachine-facts.png")
    img.save(out, "PNG")
    print("saved", out, img.size)

if __name__ == "__main__":
    build_card()
    print("DONE")
