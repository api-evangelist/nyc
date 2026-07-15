#!/usr/bin/env python3
"""Generate a static, share-ready HTML page per blog post (blog/<slug>.html).

Each post gets real per-post Open Graph + Twitter Card + canonical meta and a
PNG og:image, so LinkedIn/Twitter/Slack render a proper card (the JS docs viewer
can't — crawlers don't run JS). The body renders the post markdown client-side
(paths rewritten to root-absolute so it works from the /blog/ subdirectory).
Run after build-social.py. Also rewrites blog.html post links to these pages.
"""
import json, os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SITE = "https://nyc.apievangelist.com"
ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'"
        "%3E%3Ccircle cx='50' cy='50' r='46' fill='%233098d8'/%3E%3C/svg%3E")

def esc(s):
    return html.escape(str(s or ""), quote=True)

blog = json.load(open("data/blog.json"))
os.makedirs("blog", exist_ok=True)

TPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — NYC Digital Modernization</title>
<meta name="description" content="{summary}">
<link rel="canonical" href="{url}">
<meta name="author" content="{author}">
<link rel="icon" href="{icon}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="NYC — Digital Modernization">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{summary}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{card}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{title}">
<meta property="article:published_time" content="{date}">
<meta property="article:author" content="{author}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{summary}">
<meta name="twitter:image" content="{card}">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BlogPosting","headline":{title_json},"description":{summary_json},"image":"{card}","datePublished":"{date}","author":{{"@type":"Person","name":"{author}"}},"publisher":{{"@type":"Organization","name":"API Evangelist"}},"mainEntityOfPage":"{url}"}}
</script>
</head>
<body>
<div id="nav"></div>
<section class="plain"><div class="wrap" style="max-width:840px">
  <p class="small"><a href="/blog.html">← Blog</a></p>
  <article class="md" id="post"><h1>{title}</h1><p class="muted">{summary}</p></article>
  <p class="small" style="margin-top:2em"><a href="/blog.html">← More posts</a></p>
</div></section>
<div id="footer"></div>
<script src="/assets/app.js"></script>
<script>
(async function(){{
  document.getElementById("nav").innerHTML=navBar();
  document.getElementById("footer").innerHTML=footer();
  try{{
    let md=await getText("{mdfile}");
    let h=mdToHtml(md);
    // make relative resource paths root-absolute so they resolve from /blog/
    h=h.replace(/(href|src)="(?!https?:\\/\\/|\\/|#|mailto:|data:)([^"]*)"/g,
      (m,a,p)=>a+'="/'+p.replace(/^(\\.\\.\\/)+/,'').replace(/^\\.\\//,'')+'"');
    document.getElementById("post").innerHTML=h;
    document.title="{title} — NYC Digital Modernization";
  }}catch(e){{}}
}})();
</script>
</body>
</html>
"""

for p in blog["posts"]:
    slug = p["slug"]
    url = f"{SITE}/blog/{slug}.html"
    card = f"{SITE}/{p['card']}" if p.get("card") else f"{SITE}/assets/social.png"
    mdfile = os.path.basename(p["file"])  # sibling of the html page, inside blog/
    page = TPL.format(
        title=esc(p["title"]), summary=esc(p["summary"]), url=url, card=card,
        author=esc(p.get("author", "Kin Lane")), date=esc(p["date"]), icon=ICON,
        mdfile=mdfile, title_json=json.dumps(p["title"]), summary_json=json.dumps(p["summary"]))
    open(f"blog/{slug}.html", "w").write(page)
    print("  page: blog/%s.html" % slug)

# point blog.html cards at the static pages instead of the docs viewer
bh = open("blog.html").read()
bh2 = bh.replace("docs.html?f=${encodeURIComponent(p.file)}", "blog/${esc(p.slug)}.html")
if bh2 != bh:
    open("blog.html", "w").write(bh2)
    print("  blog.html links -> static post pages")
print("blog pages generated:", len(blog["posts"]))
