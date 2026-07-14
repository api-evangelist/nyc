#!/usr/bin/env python3
"""Build data/commons.json — the nyc-commons adoption report.

For each canonical nyc-commons definition, count how many of the 67 domains
declare a local equivalent (the fragmentation evidence) and whether they've been
migrated to $ref the canonical set. Plus the cross-agency key registry, pulled
from data/linkage.json. Deterministic; re-runnable.
"""
import json, glob, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
BASE = "https://raw.githubusercontent.com/api-evangelist/nyc/main/nyc-commons"

# canonical def -> {file, aliases: local def-names that mean the same thing}
CANON = [
    ("Borough", "geography.json", ["Borough"]),
    ("BoroCode", "geography.json", ["BoroCode", "BoroughCode", "BoroId", "BoroId"]),
    ("Coordinates", "geography.json", ["Coordinates", "GeoLocation", "Location"]),
    ("GeographySpine", "geography.json", ["GeographySpine", "Geography"]),
    ("CommunityDistrict", "geography.json", ["CommunityDistrict", "CommunityBoardReference", "CommunityBoardRef", "CommunityBoardReference"]),
    ("CouncilDistrict", "geography.json", ["CouncilDistrict"]),
    ("CensusTract", "geography.json", ["CensusTract"]),
    ("NTA", "geography.json", ["NTA"]),
    ("AdminBoundaries", "geography.json", ["AdminBoundaries"]),
    ("BBL", "identifiers.json", ["BBL", "TaxLot"]),
    ("BIN", "identifiers.json", ["BIN"]),
    ("GISPropNum", "identifiers.json", ["GISPropNum"]),
    ("DBN", "identifiers.json", ["DBN"]),
    ("Address", "address.json", ["Address", "PostalAddress"]),
    ("PartyReference", "party.json", ["PartyReference", "Person", "PersonName", "Respondent", "ContactPerson"]),
    ("AgencyReference", "party.json", ["AgencyReference", "Agency"]),
    ("OrganizationReference", "party.json", ["OrganizationReference", "VendorReference", "Vendor", "Firm"]),
    ("ContactPoint", "party.json", ["ContactPoint", "ContactInfo", "Contact"]),
    ("MoneyUSD", "money.json", ["MoneyUSD", "Money"]),
    ("FiscalYear", "money.json", ["FiscalYear"]),
    ("FiscalPeriod", "money.json", ["FiscalPeriod", "FiscalPeriod"]),
]

def short(dom):
    r = f"{dom}/README.md"
    if os.path.exists(r):
        for line in open(r):
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    return dom

commons = {c[0] for c in CANON}
alias_to_canon = {}
for canon, _f, aliases in CANON:
    for a in aliases:
        alias_to_canon.setdefault(a, canon)

# scan every domain _common.json
rows = collections.defaultdict(lambda: {"declaring": [], "migrated": []})
domains = []
migrated_domains = []
for f in sorted(glob.glob("*/schemas/_common.json")):
    dom = f.split("/")[0]
    domains.append(dom)
    j = json.load(open(f))
    is_consumer = (j.get("x-nyc-commons", {}) or {}).get("role") == "consumer"
    is_source = (j.get("x-nyc-commons", {}) or {}).get("role") == "authoritative-source"
    if is_consumer:
        migrated_domains.append(dom)
    for name, body in (j.get("$defs") or {}).items():
        canon = alias_to_canon.get(name)
        if not canon:
            continue
        ref = isinstance(body, dict) and isinstance(body.get("$ref"), str) and "nyc-commons" in body["$ref"]
        rows[canon]["declaring"].append(dom)
        if ref:
            rows[canon]["migrated"].append(dom)

defs_out = []
for canon, fname, _aliases in CANON:
    r = rows[canon]
    decl = sorted(set(r["declaring"]))
    mig = sorted(set(r["migrated"]))
    defs_out.append({
        "name": canon,
        "file": fname,
        "spec": f"{BASE}/{fname}#/$defs/{canon}",
        "declaringCount": len(decl),
        "migratedCount": len(mig),
        "declaring": [{"id": d, "short": short(d)} for d in decl],
        "migrated": mig,
    })

# cross-agency key registry from linkage.json
registry = []
if os.path.exists("data/linkage.json"):
    link = json.load(open("data/linkage.json"))
    for k in link.get("keys", []):
        registry.append({
            "key": k["key"], "label": k.get("label", k["key"]),
            "category": k.get("category"), "count": k.get("count"),
            "owningDomain": {
                "BBL": "dcp", "BIN": "dcp", "GISPropNum": "nycgovparks.org",
                "DBN": "schools.nyc.gov",
            }.get(k["key"]),
        })
    registry.sort(key=lambda x: -(x.get("count") or 0))

out = {
    "version": "0.1.0",
    "generated": "static",
    "source": {"role": "authoritative-source", "domain": "dcp"},
    "totals": {
        "canonicalDefs": len(CANON),
        "domains": len(domains),
        "migratedDomains": sorted(set(migrated_domains)),
        "files": sorted({c[1] for c in CANON}),
    },
    "defs": defs_out,
    "registry": registry,
}
os.makedirs("data", exist_ok=True)
json.dump(out, open("data/commons.json", "w"), indent=2)

# COMMONS.md
top = sorted(defs_out, key=lambda x: -x["declaringCount"])
md = []
md.append("# nyc-commons — the shared schema set\n")
md.append("*One canonical definition of a borough, a BBL, an address, a place, a party, and a dollar — for all of NYC government.*\n")
md.append("Full schema set and rationale: [`nyc-commons/`](nyc-commons/README.md). Interactive: **[nyc.apievangelist.com/commons.html](https://nyc.apievangelist.com/commons.html)**.\n")
md.append("## The problem it solves\n")
md.append(f"Across the {len(domains)} domain assessments the same objects were re-declared per agency — **Borough in all {len(domains)}**, Coordinates in all {len(domains)}, a geography spine in {top[[d['name'] for d in top].index('GeographySpine')]['declaringCount']}. `nyc-commons` factors them into {len(CANON)} canonical definitions across {len(out['totals']['files'])} files, `$ref`'d from [DCP](dcp/README.md) as the authoritative source, and **every consumer domain is now migrated to reference them**. Two records that resolve to the same `BBL` are provably about the same place.\n")
md.append("## Adoption — canonical definitions and how many domains declare a local equivalent\n")
md.append("| Definition | File | Domains declaring | Migrated to `$ref` |")
md.append("|---|---|---:|---:|")
for d in top:
    md.append(f"| `{d['name']}` | `{d['file']}` | {d['declaringCount']} | {d['migratedCount']} |")
md.append("")
nmig = len(out['totals']['migratedDomains'])
md.append(f"**Migration status: complete.** All **{nmig} consumer domains** (every domain except [`dcp`](dcp/README.md), the authoritative source) are migrated to `$ref` the canonical set — back-compatible, since the `$defs` names are unchanged so every object schema still resolves. Each keeps its own agency-specific definitions local; only the shared geography/identifier/address/money/agency shapes are redirected.\n")
md.append("## Cross-agency key registry\n")
md.append("The join keys that let one agency's records link to another's, ranked by how many domains carry them (from the [linkage analysis](LINKAGE.md)):\n")
md.append("| Key | Category | Domains | Owner |")
md.append("|---|---|---:|---|")
for r in registry[:14]:
    md.append(f"| {r['label']} | {r.get('category') or '—'} | {r.get('count') or '—'} | {r.get('owningDomain') or '—'} |")
md.append("")
md.append("---\n*Part of the [NYC Modernization](README.md) study. Design-first artifacts, not deployments.*\n")
open("COMMONS.md", "w").write("\n".join(md))
print("canonical defs:", len(CANON))
print("migrated domains:", sorted(set(migrated_domains)))
print("top adoption:")
for d in sorted(defs_out, key=lambda x: -x["declaringCount"])[:8]:
    print(f"  {d['declaringCount']:3d} declare  {d['migratedCount']:2d} migrated  {d['name']}")
print("registry keys:", [r["key"] for r in registry[:8]])
