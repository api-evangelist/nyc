#!/usr/bin/env python3
"""Generate a black-and-white line-drawing banner SVG for each blog post.

Deterministic per post (seeded by slug, so stable but every post differs) and
themed by post order — alternating NYC SKYLINE (bridges, buildings, water towers)
with STREET LIFE (people, market stalls, storefronts). Re-roll any post's art by
bumping its `imageVariant` in data/blog.json.

Writes blog/images/<slug>.svg, sets posts[].image/imageTheme in data/blog.json,
and injects the banner at the top of each post's markdown (idempotent).

Run from repo root: python3 scripts/build-blog-images.py
"""
import json, os, hashlib, random, re, xml.dom.minidom

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
W, H = 1200, 420
INK = "#141414"

# ---------- svg primitives ----------
def circle(cx, cy, r, fill="none"):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}"/>'
def line(x1, y1, x2, y2):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>'
def path(d, fill="none"):
    return f'<path d="{d}" fill="{fill}"/>'
def rectp(x, y, w, h, fill="#fff"):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}"/>'

# ---------- skyline pieces ----------
def watertank(r, cx, roof_y):
    e = []
    tw, th, lh = 26, 26, 12          # tank width, height, leg height
    ty = roof_y - lh - th            # tank top
    for dx in (-tw/2, -tw/6, tw/6, tw/2):   # legs
        e.append(line(cx+dx, ty+th, cx+dx*0.9, roof_y))
    e.append(line(cx-tw/2, ty+th, cx+tw/2, ty+th))               # tank bottom brace
    e.append(path(f"M{cx-tw/2:.1f},{ty+th:.1f} L{cx-tw/2+3:.1f},{ty:.1f} L{cx+tw/2-3:.1f},{ty:.1f} L{cx+tw/2:.1f},{ty+th:.1f} Z", fill="#fff"))
    e.append(path(f"M{cx-tw/2+3:.1f},{ty:.1f} L{cx:.1f},{ty-11:.1f} L{cx+tw/2-3:.1f},{ty:.1f}", fill="#fff"))  # conical roof
    return e

def building(r, x, top, bw, base_y):
    e = [rectp(x, top, bw, base_y-top)]
    # roof detail
    roll = r.random()
    if roll < 0.30:                          # antenna
        e.append(line(x+bw/2, top, x+bw/2, top-r.uniform(16, 34)))
    elif roll < 0.5:                         # small parapet box
        pw = bw*r.uniform(0.3, 0.5)
        e.append(rectp(x+bw/2-pw/2, top-9, pw, 9))
    # windows: light grid (floor lines + a few mullions), sometimes punched squares
    fh = r.choice([16, 18, 20])
    if r.random() < 0.5:                     # floor lines + mullions
        y = top+fh
        while y < base_y-6:
            e.append(line(x+3, y, x+bw-3, y)); y += fh
        cols = max(1, int(bw/18))
        for c in range(1, cols):
            e.append(line(x+bw*c/cols, top+5, x+bw*c/cols, base_y-3))
    else:                                    # punched windows
        cols = max(2, int(bw/16)); ww = bw/(cols*1.7)
        y = top+fh*0.6
        while y < base_y-fh:
            for c in range(cols):
                wx = x + (c+0.35)*(bw/cols)
                e.append(rectp(wx, y, ww, fh*0.55, fill="#fff"))
            y += fh
    # door
    dw = min(bw*0.28, 16)
    e.append(rectp(x+bw/2-dw/2, base_y-dw*1.3, dw, dw*1.3, fill="#fff"))
    return e

def suspension_bridge(r, x0, span, base_y):
    e = []
    deck_y = base_y - r.uniform(26, 40)
    th = r.uniform(150, 210)                 # tower height above deck
    tow = [x0, x0+span]
    top_y = deck_y - th
    for tx in tow:                           # towers
        e.append(line(tx-6, deck_y+8, tx-6, top_y)); e.append(line(tx+6, deck_y+8, tx+6, top_y))
        e.append(line(tx-6, top_y, tx+6, top_y))
        e.append(line(tx-6, deck_y-th*0.45, tx+6, deck_y-th*0.45))   # cross-brace
        e.append(path(f"M{tx-6:.1f},{deck_y-th*0.62:.1f} L{tx+6:.1f},{deck_y-th*0.52:.1f} M{tx+6:.1f},{deck_y-th*0.62:.1f} L{tx-6:.1f},{deck_y-th*0.52:.1f}"))
    # main cables (catenary between towers + sweep to anchors)
    sag = th*0.7
    e.append(path(f"M{x0-60:.1f},{deck_y-th*0.15:.1f} Q{x0:.1f},{top_y:.1f} {x0:.1f},{top_y:.1f}"))
    e.append(path(f"M{x0:.1f},{top_y:.1f} Q{(x0+span/2):.1f},{top_y+sag:.1f} {x0+span:.1f},{top_y:.1f}"))
    e.append(path(f"M{x0+span:.1f},{top_y:.1f} Q{x0+span:.1f},{top_y:.1f} {x0+span+60:.1f},{deck_y-th*0.15:.1f}"))
    # suspenders
    n = 11
    for i in range(1, n):
        sx = x0 + span*i/n
        t = i/n
        cable_y = top_y + sag*4*t*(1-t)      # parabola approx of the quad curve
        e.append(line(sx, cable_y, sx, deck_y))
    # deck
    e.append(line(x0-60, deck_y, x0+span+60, deck_y))
    e.append(line(x0-60, deck_y+7, x0+span+60, deck_y+7))
    return e

def wave(r, y):
    d = f"M0,{y:.1f}"
    x = 0
    while x < W:
        step = r.uniform(28, 46)
        d += f" q{step/2:.1f},{r.uniform(-5,-2):.1f} {step:.1f},0"
        x += step
    return path(d)

def boat(r, y):
    bx = r.uniform(W*0.05, W*0.5); s = r.uniform(0.8, 1.3)
    hy = y + r.uniform(24, 44)
    e = [path(f"M{bx-26*s:.1f},{hy:.1f} Q{bx:.1f},{hy+12*s:.1f} {bx+26*s:.1f},{hy:.1f} Z", fill="#fff")]
    e.append(line(bx, hy, bx, hy-30*s))
    e.append(path(f"M{bx:.1f},{hy-30*s:.1f} L{bx+18*s:.1f},{hy-6*s:.1f} L{bx:.1f},{hy-6*s:.1f} Z", fill="#fff"))
    return e

def bird(r, x, y):
    s = r.uniform(6, 11)
    return path(f"M{x-s:.1f},{y:.1f} Q{x-s/2:.1f},{y-s*0.7:.1f} {x:.1f},{y:.1f} Q{x+s/2:.1f},{y-s*0.7:.1f} {x+s:.1f},{y:.1f}")

def scene_skyline(r):
    e = []
    water_y = H*0.80
    e.append(circle(r.uniform(W*0.62, W*0.9), r.uniform(H*0.12, H*0.26), r.uniform(22, 34)))  # sun/moon
    for _ in range(r.randint(2, 4)):
        e.append(bird(r, r.uniform(W*0.15, W*0.55), r.uniform(H*0.10, H*0.30)))
    # buildings
    x = r.uniform(-14, 18); tanks = r.randint(2, 3)
    while x < W:
        bw = r.uniform(46, 106)
        cf = 1 - abs((x+bw/2)/W - 0.5)*1.25
        top = water_y - r.uniform(80, 250)*max(0.32, cf) - 26
        top = max(top, H*0.15)
        e += building(r, x, top, bw, water_y)
        if tanks > 0 and bw > 56 and r.random() < 0.45:
            e += watertank(r, x+bw/2, top); tanks -= 1
        x += bw + r.uniform(-3, 7)
    for i in range(r.randint(3, 5)):
        e.append(wave(r, water_y+9+i*10))
    if r.random() < 0.9:
        span = r.uniform(230, 330); x0 = r.choice([r.uniform(40, 120), r.uniform(W-120-span, W-span-40)])
        e += suspension_bridge(r, x0, span, water_y)
    if r.random() < 0.7:
        e += boat(r, water_y)
    return e

# ---------- street pieces ----------
def _hat(cx, cy, hr):                                    # simple brim + shallow crown
    bw = hr*2.5
    return [line(cx-bw/2, cy, cx+bw/2, cy),
            path(f"M{cx-hr*1.05:.1f},{cy:.1f} Q{cx:.1f},{cy-hr*1.7:.1f} {cx+hr*1.05:.1f},{cy:.1f}", fill="#fff")]

def person(r, cx, gy, s, flip):
    """A minimal, elegant walking figure: round head, A-line coat, two legs."""
    e = []
    top = gy - s
    hr = 0.085*s
    hcy = top + hr
    e.append(circle(cx, hcy, hr))                        # head
    if r.random() < 0.30:
        e += _hat(cx, hcy-hr*0.35, hr)
    y_sh = top + 2*hr + 0.02*s                           # shoulders, tucked under head
    y_hem = gy - r.uniform(0.36, 0.44)*s                 # coat hem (varied length)
    wsh = 0.095*s; whem = r.uniform(0.12, 0.155)*s
    e.append(path(                                       # A-line coat silhouette
        f"M{cx-wsh:.1f},{y_sh:.1f} Q{cx:.1f},{y_sh-0.05*s:.1f} {cx+wsh:.1f},{y_sh:.1f} "
        f"L{cx+whem:.1f},{y_hem:.1f} Q{cx:.1f},{y_hem+0.03*s:.1f} {cx-whem:.1f},{y_hem:.1f} Z",
        fill="#fff"))
    st = r.uniform(0.03, 0.06)*s                         # gentle forward stride
    lx, rx = cx-0.05*s, cx+0.05*s
    e.append(line(lx, y_hem, lx-st*flip, gy))
    e.append(line(rx, y_hem, rx+st*0.4*flip, gy))
    fl = 0.055*s*flip
    e.append(line(lx-st*flip, gy, lx-st*flip+fl, gy))    # feet, pointing in walk direction
    e.append(line(rx+st*0.4*flip, gy, rx+st*0.4*flip+fl, gy))
    k = r.random()                                       # optional carried item (no stick arms otherwise)
    if k < 0.20:                                         # tote bag at the side
        hx = cx+whem*0.9*flip; hy = (y_sh+y_hem)/2+0.05*s
        e.append(line(cx+wsh*0.55*flip, y_sh+0.05*s, hx, hy))
        e.append(rectp(hx-0.045*s, hy, 0.09*s, 0.12*s, fill="#fff"))
        e.append(path(f"M{hx-0.028*s:.1f},{hy:.1f} q{0.028*s:.1f},{-0.04*s:.1f} {0.056*s:.1f},0"))
    elif k < 0.30:                                       # briefcase held low
        hx = cx+whem*0.95*flip; hy = y_hem+0.03*s
        e.append(line(cx+wsh*0.55*flip, y_sh+0.06*s, hx, hy-0.02*s))
        e.append(rectp(hx-0.06*s, hy, 0.12*s, 0.07*s, fill="#fff"))
    return e

def couple(r, cx, gy, s):
    return person(r, cx-0.13*s, gy, s, 1) + person(r, cx+0.13*s, gy, s*r.uniform(0.9, 1.0), -1)

def stall(r, cx, gy):
    e = []; w = r.uniform(120, 175); h = w*0.72
    top = gy-h
    e.append(line(cx-w/2, gy-h*0.28, cx-w/2, top)); e.append(line(cx+w/2, gy-h*0.28, cx+w/2, top))  # poles
    # scalloped awning
    d = f"M{cx-w/2:.1f},{top:.1f} L{cx+w/2:.1f},{top:.1f} L{cx+w/2:.1f},{top+14:.1f}"
    n = int(w/18); x = cx+w/2
    for i in range(n):
        d += f" q{-9:.1f},{9:.1f} {-18:.1f},0"; x -= 18
    d += f" L{cx-w/2:.1f},{top:.1f} Z"
    e.append(path(d, fill="#fff"))
    for i in range(1, n):                    # awning stripes
        e.append(line(cx-w/2+i*18, top, cx-w/2+i*18, top+13))
    ty = gy-h*0.28                           # table
    e.append(rectp(cx-w/2+8, ty, w-16, 10, fill="#fff"))
    e.append(line(cx-w/2+14, ty+10, cx-w/2+14, gy)); e.append(line(cx+w/2-14, ty+10, cx+w/2-14, gy))
    for i in range(r.randint(5, 9)):         # produce
        e.append(circle(cx-w/2+16+i*(w-32)/8, ty-4, r.uniform(3.5, 5.5)))
    return e

def tree(r, cx, gy):
    h = r.uniform(70, 110)
    e = [line(cx, gy, cx, gy-h*0.5)]
    cy = gy-h*0.65; cr = h*0.36
    d = f"M{cx-cr:.1f},{cy:.1f}"
    for a in range(8):
        import math
        ang = math.pi*(a+1)/8*2 - math.pi
        d += f" q{r.uniform(-6,6):.1f},{-cr*0.55:.1f} {cr/4:.1f},0"
    e.append(path(f"M{cx:.1f},{cy-cr:.1f} a{cr:.1f},{cr:.1f} 0 1,0 0.1,0 Z", fill="#fff"))
    return e

def lamp(r, cx, gy):
    h = r.uniform(120, 150)
    return [line(cx, gy, cx, gy-h),
            path(f"M{cx:.1f},{gy-h:.1f} q{18:.1f},0 {20:.1f},{16:.1f}"),
            path(f"M{cx+20:.1f},{gy-h+16:.1f} l{-5:.1f},{12:.1f} l{10:.1f},0 Z", fill="#fff")]

def hydrant(r, cx, gy):
    return [rectp(cx-6, gy-18, 12, 18, fill="#fff"),
            path(f"M{cx-6:.1f},{gy-18:.1f} q6,-6 12,0", fill="#fff"),
            line(cx-9, gy-12, cx+9, gy-12), circle(cx, gy-13, 2.5)]

def bench(r, cx, gy):
    w = 60
    return [line(cx-w/2, gy-16, cx+w/2, gy-16), line(cx-w/2, gy-28, cx+w/2, gy-28),
            line(cx-w/2, gy-28, cx-w/2, gy), line(cx+w/2, gy-28, cx+w/2, gy),
            line(cx-w/2, gy-16, cx-w/2, gy), line(cx+w/2, gy-16, cx+w/2, gy)]

def storefront(r, x, w, base_y):
    top = base_y - r.uniform(120, 170)
    e = [rectp(x, top, w, base_y-top)]
    ay = base_y - r.uniform(56, 78)          # awning
    d = f"M{x+4:.1f},{ay:.1f} L{x+w-4:.1f},{ay:.1f} L{x+w-4:.1f},{ay+12:.1f}"
    n = int((w-8)/16); xi = x+w-4
    for i in range(n):
        d += f" q{-8:.1f},{8:.1f} {-16:.1f},0"; xi -= 16
    d += f" L{x+4:.1f},{ay:.1f} Z"
    e.append(path(d, fill="#fff"))
    for i in range(1, n):
        e.append(line(x+4+i*16, ay, x+4+i*16, ay+11))
    # upper windows
    fh = 22; y = top+14
    while y < ay-16:
        cols = max(2, int(w/40))
        for c in range(cols):
            e.append(rectp(x+6+c*(w-12)/cols, y, (w-12)/cols-8, fh*0.6, fill="#fff"))
        y += fh
    # door + display window
    dw = min(20, w*0.2)
    e.append(rectp(x+8, base_y-40, dw, 40, fill="#fff"))
    e.append(rectp(x+dw+16, base_y-40, w-dw-24, 32, fill="#fff"))
    return e

def scene_street(r):
    e = []
    side_y = H*0.74; curb_y = side_y+14
    x = r.uniform(-10, 10)
    while x < W:
        w = r.uniform(150, 240); e += storefront(r, x, w, side_y-2); x += w + r.uniform(2, 8)
    e.append(line(0, side_y, W, side_y)); e.append(line(0, curb_y, W, curb_y))
    for lx in range(40, W, 92):
        e.append(line(lx, (curb_y+H)/2, lx+34, (curb_y+H)/2))
    # a stall or two + street furniture
    for _ in range(r.randint(1, 2)):
        e += stall(r, r.uniform(W*0.12, W*0.88), side_y)
    for fn in r.sample([tree, lamp, hydrant, bench, tree], r.randint(2, 4)):
        e += fn(r, r.uniform(40, W-40), side_y)
    # people evenly spaced across the foreground (jittered), varied size for depth
    n = r.randint(6, 9)
    for i in range(n):
        px = (i+0.5)*W/n + r.uniform(-W/(n*3.2), W/(n*3.2))
        s = r.uniform(80, 118)
        gy = side_y + r.uniform(2, 9)        # feet near the sidewalk
        if r.random() < 0.16:
            e += couple(r, px, gy, s)
        else:
            e += person(r, px, gy, s, r.choice([-1, 1]))
    return e

# ---------- compose + write ----------
def build_svg(slug, theme, seed):
    r = random.Random(seed)
    els = scene_skyline(r) if theme == "skyline" else scene_street(r)
    title = "NYC skyline — line drawing" if theme == "skyline" else "NYC street life — line drawing"
    body = "\n".join(els)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{title}">'
           f'<title>{title}</title><rect width="{W}" height="{H}" fill="#ffffff"/>'
           f'<g stroke="{INK}" stroke-width="2.1" fill="none" stroke-linecap="round" stroke-linejoin="round">'
           f'{body}</g></svg>')
    xml.dom.minidom.parseString(svg)         # validate well-formed
    return svg

def main():
    blog = json.load(open("data/blog.json"))
    os.makedirs("blog/images", exist_ok=True)
    for i, p in enumerate(blog["posts"]):
        slug = p["slug"]
        theme = p.get("imageTheme") or ("skyline" if i % 2 == 0 else "street")
        variant = int(p.get("imageVariant", 0))
        seed = int(hashlib.sha256(f"{slug}:{variant}".encode()).hexdigest()[:12], 16)
        svg = build_svg(slug, theme, seed)
        out = f"blog/images/{slug}.svg"
        open(out, "w").write(svg + "\n")
        p["image"] = out; p["imageTheme"] = theme
        # inject banner at top of the post markdown (idempotent)
        mdf = p["file"]
        if os.path.exists(mdf):
            md = open(mdf).read()
            banner = f"![{theme} line drawing of New York City]({out})"
            if "blog/images/" not in md:
                lines = md.split("\n")
                # place after the first H1 (title), before the byline
                for j, ln in enumerate(lines):
                    if ln.startswith("# "):
                        lines.insert(j+1, "\n" + banner)
                        break
                else:
                    lines.insert(0, banner + "\n")
                open(mdf, "w").write("\n".join(lines))
        print(f"  {theme:8} {out}")
    json.dump(blog, open("data/blog.json", "w"), indent=2)
    print(f"generated {len(blog['posts'])} blog image(s)")

if __name__ == "__main__":
    main()
