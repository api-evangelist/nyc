#!/usr/bin/env python3
"""Rebuild data/scorecard.json. The first 15 domains keep their hand-authored
entries; every newly-added domain self-scores via a "scorecard" + "scorecard_notes"
block in its fruit.json (0-3 per dimension). Idempotent. Run from repo root."""
import json, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

FIRST15 = ["nycgovparks.org","schools.nyc.gov","council.nyc.gov","vote.nyc","nyc311",
           "dob","hpd","dot","dohmh","dsny","nypd","tlc","dcp","comptroller.nyc.gov","nycha"]
DIMS = ["platform","siteApi","openData","coreData","writeApi","agent","ownership"]

sc = json.load(open("data/scorecard.json"))
kept = [d for d in sc["domains"] if d["id"] in FIRST15]
kept_ids = {d["id"] for d in kept}
net = [n for n in sc["netNew"]]  # keep existing 14
net_domains = {n["domain"] for n in net}

added = 0
for f in sorted(glob.glob("*/fruit.json")):
    d = os.path.dirname(f)
    if d in kept_ids: continue
    fruit = json.load(open(f))
    scb = fruit.get("scorecard")
    meta = fruit.get("meta", {})
    if not scb:
        print("WARN no scorecard block:", d); continue
    entry = {"id": d, "short": meta.get("short", d), "verb": meta.get("verb",""),
             "accent": meta.get("accent","#3098d8"),
             "scores": {k: scb.get(k, 0) for k in DIMS},
             "notes": fruit.get("scorecard_notes", {})}
    kept.append(entry); added += 1
    nn = meta.get("netnew","")
    if nn and not nn.startswith("—") and meta.get("short") not in net_domains:
        net.append({"domain": meta.get("short", d), "object": nn})

sc["domains"] = kept
sc["netNew"] = net
sc["note"] = f"Editorial maturity scores (0-3, higher = more mature) across {len(kept)} assessments. 0 = absent, 1 = legacy/hidden/rented, 2 = usable/partial, 3 = modern/owned/complete. First 15 hand-authored; the rest self-scored per domain. See SYNTHESIS.md."
json.dump(sc, open("data/scorecard.json","w"), indent=2)
print(f"scorecard: {len(kept)} domains ({added} appended), {len(net)} net-new")
wa=[d["scores"]["writeApi"] for d in kept]; ag=[d["scores"]["agent"] for d in kept]
print("writeApi max:", max(wa), "| agent max:", max(ag),
      "| writeApi>0:", sum(1 for x in wa if x>0), "| agent>0:", sum(1 for x in ag if x>0))
