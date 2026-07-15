#!/usr/bin/env python3
"""Rasterize the line-art banners into 1200x630 PNG social cards (og:image).

LinkedIn/Twitter need a real PNG (not SVG) ~1200x630. This turns each blog
banner SVG into blog/images/<slug>-card.png and produces a default site card
at assets/social.png. Run after build-blog-images.py.
"""
import json, os, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def raster(svg, png):
    subprocess.run(["node", "scripts/svg2png.mjs", svg, png, "1200", "630"], check=True,
                   stdout=subprocess.DEVNULL)

blog = json.load(open("data/blog.json"))
os.makedirs("assets", exist_ok=True)
for p in blog["posts"]:
    svg = p.get("image")
    if svg and os.path.exists(svg):
        card = svg[:-4] + "-card.png"
        raster(svg, card)
        p["card"] = card
        print("  card:", card)
json.dump(blog, open("data/blog.json", "w"), indent=2, ensure_ascii=False)

# default site card: prefer a skyline banner
default = next((p for p in blog["posts"] if p.get("imageTheme") == "skyline"),
               blog["posts"][0] if blog["posts"] else None)
if default and default.get("image"):
    raster(default["image"], "assets/social.png")
    print("  default: assets/social.png")
print("social cards generated")
