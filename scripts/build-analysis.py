#!/usr/bin/env python3
"""Derive the second-order analysis from the recalibrated scorecard + artifacts:
  data/opportunity.json  + OPPORTUNITY.md   — rank domains by demand x gap x feasibility
  data/linkage.json      + LINKAGE.md       — shared join keys that connect agencies
  data/transactions.json + TRANSACTIONS.md  — the 66 write workflows as reusable primitives
Run AFTER build-manifest.py + build-scorecard.py. From repo root."""
import json, glob, os, re, math, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
M = json.load(open("data/manifest.json"))
SC = {d["id"]: d for d in json.load(open("data/scorecard.json"))["domains"]}
DOM = M["domains"]
short = {d["id"]: d["short"] for d in DOM}

# ============================ OPPORTUNITY ============================
# reach weight of the domain's net-new citizen transaction (population it touches)
HIGH = ["benefit", "enrollment", "admission", "permit", "marriage", "ballot", "service request",
        "servicerequest", "vital", "appointment", "housinglottery", "lottery", "tax"]
MED  = ["license", "work order", "workorder", "complaint", "pickup", "registration", "hold",
        "records", "referral", "dispute", "summons", "greenlight", "film"]
def reach(nn):
    s = (nn or "").lower()
    if any(t in s for t in HIGH): return 0.9
    if any(t in s for t in MED): return 0.55
    if s and "reference" not in s: return 0.3
    return 0.15

views = [SC[d["id"]].get("odViews", 0) for d in DOM]
maxlog = max((math.log10(v + 1) for v in views), default=1) or 1
rows = []
for d in DOM:
    did = d["id"]; s = SC[did]["scores"]; nn = d.get("netnew", "")
    odv = SC[did].get("odViews", 0)
    demand = max(math.log10(odv + 1) / maxlog, reach(nn))      # 0..1
    gap = 0.3 + (0.4 if reach(nn) >= 0.3 else 0) + (0.2 if s["siteApi"] <= 1 else 0) + (0.1 if s["coreData"] <= 1 else 0)
    gap = min(gap, 1.0)
    feas = 1.0 if s["siteApi"] >= 2 or s["openData"] >= 2 else 0.6 if (s["siteApi"] == 1 or s["openData"] == 1) else 0.3
    score = demand * gap * feas
    drivers = []
    if s["siteApi"] >= 2: drivers.append("an API already exists (expose/document)")
    elif s["siteApi"] == 1: drivers.append("a private API to open")
    elif s["openData"] >= 2: drivers.append("open data to wrap")
    else: drivers.append("data must be digitized")
    if reach(nn) >= 0.9: drivers.append("high-reach citizen transaction")
    rows.append({"id": did, "short": short[did], "verb": d.get("verb",""), "accent": d.get("accent","#3098d8"),
                 "netnew": nn, "odViews": odv,
                 "demand": round(demand, 3), "gap": round(gap, 3), "feasibility": round(feas, 3),
                 "score": round(score * 100, 1), "drivers": drivers})
rows.sort(key=lambda r: -r["score"])
# quadrants by median impact & feasibility
impacts = sorted(r["demand"] * r["gap"] for r in rows)
med_imp = impacts[len(impacts)//2]
for r in rows:
    imp = r["demand"] * r["gap"]; hi = imp >= med_imp; hf = r["feasibility"] >= 1.0
    r["impact"] = round(imp, 3)
    r["quadrant"] = ("Quick win" if hi and hf else "Big bet" if hi and not hf
                     else "Easy add" if not hi and hf else "Backlog")
opp = {"method": "opportunity = demand x gap x feasibility (each 0-1), x100. demand = max(log-scaled Open Data page-views, reach-weight of the net-new citizen transaction); gap = locked citizen transaction + low site-API + disconnected core data; feasibility = inverse build cost (an existing/private API or open data is cheaper than digitizing).",
       "domains": rows}
json.dump(opp, open("data/opportunity.json", "w"), indent=1)

L = ["# Opportunity Ranking\n",
     "Where NYC API modernization matters most — every domain scored **demand × gap × feasibility** (see method in [opportunity.json](data/opportunity.json)). Interactive: [opportunity.html](https://nyc.apievangelist.com/opportunity.html).\n",
     "## Top 20 by opportunity score\n",
     "| # | Domain | Score | Demand | Gap | Feasibility | Quadrant | Net-new write |", "|--|--|--|--|--|--|--|--|"]
for i, r in enumerate(rows[:20], 1):
    L.append(f"| {i} | {r['short']} | **{r['score']}** | {r['demand']} | {r['gap']} | {r['feasibility']} | {r['quadrant']} | `{r['netnew']}` |")
L.append("\n## Quick wins (high impact + already feasible)\n")
for r in [r for r in rows if r["quadrant"] == "Quick win"][:20]:
    L.append(f"- **{r['short']}** ({r['score']}) — {', '.join(r['drivers'])}; net-new `{r['netnew']}`")
open("OPPORTUNITY.md", "w").write("\n".join(L) + "\n")

# ============================ LINKAGE ============================
KEYS = collections.OrderedDict([
 ("BBL", ("property", [r"\bbbl\b", r"borough[- ]?block[- ]?lot"])),
 ("BIN", ("property", [r"\bbin\b", r"building identification"])),
 ("GISPropNum", ("property", [r"gispropnum", r"gis property"])),
 ("Borough", ("geography", [r"\bborough\b"])),
 ("Community Board", ("geography", [r"community[_ ]?board", r"communityboard", r"commboard"])),
 ("Council District", ("geography", [r"council[_ ]?district", r"councildistrict"])),
 ("Census Tract", ("geography", [r"census[_ ]?tract", r"censustract"])),
 ("NTA (neighborhood)", ("geography", [r"\bnta\b"])),
 ("Police Precinct", ("geography", [r"police[_ ]?precinct", r"\bprecinct\b"])),
 ("Coordinates (lat/long)", ("geography", [r"latitude", r"longitude", r"coordinates"])),
 ("DBN (school)", ("identity", [r"\bdbn\b"])),
 ("Council Member ID", ("identity", [r"councilmemberid", r"council member id"])),
 ("Matter ID (Legistar)", ("identity", [r"matterid", r"matter id", r"filenumber"])),
 ("Election District", ("identity", [r"election[_ ]?district", r"electiondistrict"])),
])
key_dom = collections.defaultdict(set)
dom_keys = {}
for d in DOM:
    blob = ""
    for sp in glob.glob(f"{d['id']}/schemas/*.json"):
        blob += open(sp, encoding="utf-8", errors="ignore").read().lower() + "\n"
    ks = [k for k, (cat, rx) in KEYS.items() if any(re.search(p, blob) for p in rx)]
    dom_keys[d["id"]] = ks
    for k in ks: key_dom[k].add(d["id"])
# domain pairs sharing a PROPERTY/IDENTITY key (strong links, not the near-universal geo ones)
strong = [k for k, (cat, _) in KEYS.items() if cat in ("property", "identity")]
pair = collections.Counter()
for k in strong:
    ds = sorted(key_dom[k])
    for i in range(len(ds)):
        for j in range(i+1, len(ds)):
            pair[(ds[i], ds[j])] += 1
link = {
 "keys": [{"key": k, "label": k, "category": KEYS[k][0], "count": len(key_dom[k]),
           "domains": [{"id": x, "short": short[x]} for x in sorted(key_dom[k])]} for k in KEYS if key_dom[k]],
 "byDomain": [{"id": d["id"], "short": d["short"], "keys": dom_keys[d["id"]]} for d in DOM],
 "topPairs": [{"a": short[a], "b": short[b], "shared": c} for (a, b), c in pair.most_common(25)],
}
json.dump(link, open("data/linkage.json", "w"), indent=1)
T = ["# Cross-Domain Linkage\n",
     "The join keys that connect agencies — the basis for `nyc-commons` and cross-domain interoperability. Detected in each domain's JSON Schemas. Interactive: [linkage.html](https://nyc.apievangelist.com/linkage.html).\n",
     "## Shared keys, by reach\n", "| Key | Category | # domains |", "|--|--|--|"]
for k in sorted(link["keys"], key=lambda x: -x["count"]):
    T.append(f"| `{k['key']}` | {k['category']} | {k['count']} |")
T.append("\n## The property spine (BBL/BIN — the strongest connectors)\n")
for k in link["keys"]:
    if k["category"] == "property":
        T.append(f"- **{k['key']}** ({k['count']}): {', '.join(x['short'] for x in k['domains'])}")
open("LINKAGE.md", "w").write("\n".join(T) + "\n")

# ============================ TRANSACTIONS ============================
PRIM = collections.OrderedDict([
 ("Apply", [r"application", r"apply", r"enrollment", r"admission", r"lottery", r"prequal"]),
 ("Pay", [r"payment", r"pay\b"]),
 ("Report / Complain", [r"complaint", r"tip", r"report", r"outreach", r"servicerequest", r"service request"]),
 ("Register / Subscribe", [r"registration", r"subscription", r"subscribe", r"testimony"]),
 ("Schedule / Reserve", [r"appointment", r"scheduling", r"pickup", r"hold\b", r"visit"]),
 ("Request records / service", [r"records?request", r"vitalrecord", r"deathrecord", r"referral", r"datarequest"]),
 ("Dispute / Appeal / File", [r"dispute", r"appeal", r"filing", r"claim", r"disclosure"]),
])
def prim(nn):
    s = (nn or "").lower()
    for p, rx in PRIM.items():
        if any(re.search(x, s) for x in rx): return p
    return "Other"
tx = collections.defaultdict(list)
for d in DOM:
    nn = d.get("netnew", "")
    if nn and "reference" not in nn.lower() and not nn.startswith("—"):
        tx[prim(nn)].append({"domain": d["short"], "object": nn})
transactions = {
 "note": "The net-new citizen write-workflows (one per domain) grouped into reusable transaction primitives. Build each primitive once; reuse across agencies.",
 "primitives": [{"primitive": p, "count": len(tx[p]),
                 "items": sorted(tx[p], key=lambda x: x["object"])} for p in list(PRIM) + ["Other"] if tx[p]],
}
json.dump(transactions, open("data/transactions.json", "w"), indent=1)
X = ["# Citizen-Transaction Taxonomy\n",
     f"The **{sum(len(v) for v in tx.values())} net-new write workflows** — one per domain — grouped into reusable primitives. The city needs a handful of transaction patterns, built once and reused. Interactive: [transactions.html](https://nyc.apievangelist.com/transactions.html).\n"]
for p in list(PRIM) + ["Other"]:
    if tx[p]:
        X.append(f"## {p} ({len(tx[p])})\n")
        for it in sorted(tx[p], key=lambda x: x["object"]):
            X.append(f"- **{it['domain']}** — `{it['object']}`")
        X.append("")
open("TRANSACTIONS.md", "w").write("\n".join(X) + "\n")

print("opportunity: top5", [(r["short"], r["score"]) for r in rows[:5]])
print("quadrants:", collections.Counter(r["quadrant"] for r in rows))
print("linkage keys:", [(k["key"], k["count"]) for k in sorted(link["keys"], key=lambda x:-x["count"])[:6]])
print("transactions:", [(p, len(tx[p])) for p in tx])
