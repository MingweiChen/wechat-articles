#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""压缩 + 命名 + 双落盘（draft 备份 + wechat 图床源）。宽≤560px，≤100KB。"""
import os
from PIL import Image

DRAFT = "/home/mchen/.openclaw/workspace/drafts/2026-06-24_0231/meta-entry-point-weaponize-search/illustrations"
WECHAT = "/home/mchen/.openclaw/workspace/wechat-articles/2026-06/2026-06-24/illustrations/meta-entry-point-weaponize-search"
os.makedirs(WECHAT, exist_ok=True)

MAXW = 560
MAXKB = 100

# (源文件, 输出名, 是否照片jpg)
jobs = [
    ("_zuck_raw.jpg",        "01-zuckerberg-portrait.jpg", True),
    ("_chart_strategy.png",  "02-model-vs-entry-strategy.png", False),
    ("_chart_revenue.png",   "03-entry-revenue-estimate.png", False),
    ("_meta_ai_logo_raw.png","04-meta-ai-logo.jpg", True),  # 转jpg压缩，logo是渐变照片型
]

def save_under_limit(img, out_path, is_jpg):
    if is_jpg:
        if img.mode in ("RGBA", "P"):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "RGBA":
                bg.paste(img, mask=img.split()[-1])
            else:
                bg.paste(img.convert("RGBA"), mask=img.convert("RGBA").split()[-1])
            img = bg
        else:
            img = img.convert("RGB")
        q = 88
        while q >= 40:
            img.save(out_path, "JPEG", quality=q, optimize=True, progressive=True)
            if os.path.getsize(out_path) <= MAXKB * 1024:
                break
            q -= 6
    else:
        # PNG：先尝试，超限则量化到 P 模式
        img.save(out_path, "PNG", optimize=True)
        if os.path.getsize(out_path) > MAXKB * 1024:
            pal = img.convert("RGB").quantize(colors=128, method=Image.FASTOCTREE)
            pal.save(out_path, "PNG", optimize=True)
        if os.path.getsize(out_path) > MAXKB * 1024:
            pal = img.convert("RGB").quantize(colors=64, method=Image.FASTOCTREE)
            pal.save(out_path, "PNG", optimize=True)
    return os.path.getsize(out_path)

for src, outname, is_jpg in jobs:
    sp = os.path.join(DRAFT, src)
    img = Image.open(sp)
    w, h = img.size
    if w > MAXW:
        nh = int(h * MAXW / w)
        img = img.resize((MAXW, nh), Image.LANCZOS)
    draft_out = os.path.join(DRAFT, outname)
    sz = save_under_limit(img, draft_out, is_jpg)
    # 复制到 wechat
    wp = os.path.join(WECHAT, outname)
    import shutil
    shutil.copy2(draft_out, wp)
    print(f"{outname:40s} {img.size}  {sz/1024:6.1f} KB")

print("\n--- wechat dir ---")
for f in sorted(os.listdir(WECHAT)):
    print(f, os.path.getsize(os.path.join(WECHAT, f)))
