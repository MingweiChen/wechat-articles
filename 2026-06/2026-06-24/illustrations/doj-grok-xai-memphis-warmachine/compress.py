#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""压缩插图: 宽度<=560px, 单图<=100KB, 转 RGB jpg/优化 png"""
from PIL import Image
import os

OUT = os.path.dirname(os.path.abspath(__file__))
MAXW = 560
MAXKB = 100

# 源 -> 目标 (规范命名). 图表用 png(线条锐利), card 用 png
files = [
    ("01-emissions-load.png", "01-emissions-load.png"),
    ("02-grok-warmachine-facts.png", "02-grok-warmachine-facts.png"),
    ("03-three-parties.png", "03-three-parties.png"),
    ("04-causal-chain.png", "04-causal-chain.png"),
]

def flatten(im, bg=(251,250,247)):
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        canvas = Image.new("RGB", im.size, bg)
        canvas.paste(im, mask=im.split()[-1])
        return canvas
    return im.convert("RGB")

def save_under_limit(im, base):
    """先试 PNG(优化+量化), 不行再 JPG 降质, 保证 <=100KB."""
    png_path = os.path.join(OUT, base)
    # 尝试 PNG 256 色量化 (信息图色彩少, 量化几乎无损)
    q = im.convert("RGB").quantize(colors=128, method=Image.MEDIANCUT, dither=Image.NONE)
    q.save(png_path, "PNG", optimize=True)
    kb = os.path.getsize(png_path) // 1024
    if kb <= MAXKB:
        return base, kb, "png"
    # 试 64 色
    q = im.convert("RGB").quantize(colors=64, method=Image.MEDIANCUT, dither=Image.NONE)
    q.save(png_path, "PNG", optimize=True)
    kb = os.path.getsize(png_path) // 1024
    if kb <= MAXKB:
        return base, kb, "png"
    # 退回 JPG
    jpg_base = base.rsplit(".",1)[0] + ".jpg"
    jpg_path = os.path.join(OUT, jpg_base)
    for qual in (88, 82, 76, 70, 64):
        im.convert("RGB").save(jpg_path, "JPEG", quality=qual, optimize=True, progressive=True)
        kb = os.path.getsize(jpg_path) // 1024
        if kb <= MAXKB:
            if os.path.exists(png_path):
                os.remove(png_path)
            return jpg_base, kb, "jpg"
    return jpg_base, kb, "jpg"

results = []
for src, dst in files:
    sp = os.path.join(OUT, src)
    im = Image.open(sp)
    im = flatten(im)
    if im.width > MAXW:
        h = round(im.height * MAXW / im.width)
        im = im.resize((MAXW, h), Image.LANCZOS)
    name, kb, fmt = save_under_limit(im, dst)
    results.append((name, im.size, kb, fmt))
    print(f"{name}: {im.size[0]}x{im.size[1]}  {kb}KB  ({fmt})")

print("---")
for r in results:
    print(r)
