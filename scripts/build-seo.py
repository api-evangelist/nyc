#!/usr/bin/env python3
"""Inject Open Graph + Twitter Card + canonical meta into the main site pages.

Reads each root-level *.html page's existing <title> and description, and adds a
delimited, idempotent SEO block before </head> so every page renders a proper
card on LinkedIn / Twitter / Slack. Blog post pages get their own per-post meta
(build-blog.py), so they're skipped here.
"""
import glob, os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SITE = "https://nyc.apievangelist.com"
IMG = f"{SITE}/assets/social.png"
START, END = "<!--seo:start-->", "<!--seo:end-->"

def attr(s):
    return html.escape((s or "").strip(), quote=True)

def block(title, desc, url):
    return "\n".join([START,
        f'<link rel="canonical" href="{url}">',
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="NYC — Digital Modernization">',
        f'<meta property="og:title" content="{attr(title)}">',
        f'<meta property="og:description" content="{attr(desc)}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{IMG}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{attr(title)}">',
        f'<meta name="twitter:description" content="{attr(desc)}">',
        f'<meta name="twitter:image" content="{IMG}">',
        END, ""])

n = 0
for f in sorted(glob.glob("*.html")):
    s = open(f).read()
    tm = re.search(r"<title>(.*?)</title>", s, re.S)
    title = html.unescape(tm.group(1).strip()) if tm else "NYC — Digital Modernization"
    dm = re.search(r'<meta\s+name="description"\s+content="(.*?)"', s, re.S)
    desc = html.unescape(dm.group(1).strip()) if dm else title
    url = SITE + "/" + ("" if f == "index.html" else f)
    s = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", s, flags=re.S)  # drop old block
    if "</head>" not in s:
        continue
    s = s.replace("</head>", block(title, desc, url) + "</head>", 1)
    open(f, "w").write(s)
    n += 1
print(f"SEO meta injected into {n} pages")
