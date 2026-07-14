#!/usr/bin/env python3
"""Generate REFERENCES.md from data/references.json (append references there)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
d = json.load(open("data/references.json"))
n = sum(len(c["refs"]) for c in d["categories"])
M = ["# References\n",
     f"A growing library of the sources behind the NYC Modernization strategy — **{n} references** across {len(d['categories'])} groups. Interactive: [references.html](https://nyc.apievangelist.com/references.html). Add entries in [`data/references.json`](data/references.json).\n"]
for c in d["categories"]:
    M.append(f"## {c['name']}\n")
    if c.get("blurb"):
        M.append(f"*{c['blurb']}*\n")
    for r in c["refs"]:
        meta = " · ".join(x for x in [r.get("source"), r.get("date")] if x)
        line = f"- [{r['title']}]({r['url']})" + (f" — {meta}" if meta else "")
        M.append(line)
        if r.get("note"):
            M.append(f"  - {r['note']}")
    M.append("")
M.append("---\n*Part of the [NYC Modernization](README.md) study.*\n")
open("REFERENCES.md", "w").write("\n".join(M))
print(f"REFERENCES.md: {n} references across {len(d['categories'])} categories")
