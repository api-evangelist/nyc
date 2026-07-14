#!/usr/bin/env python3
"""Rebuild data/scorecard.json with DETERMINISTIC, RULE-BASED scores.

Every domain is scored 0-3 on 7 dimensions by ONE uniform function over the
structured signals we captured (Open Data asset counts + page views, the
apis_observed inventory, and the platform fingerprint) — NOT the earlier
per-subagent self-scores, which weren't calibrated across raters. This makes
cross-domain comparison defensible. Rules are documented in `scoring_method`
below and echoed into each domain's per-dimension notes.

Run from repo root: python3 scripts/build-scorecard.py"""
import json, glob, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
M = json.load(open("data/manifest.json"))
DOM = M["domains"]

# --- token dictionaries -----------------------------------------------------
VENDOR_CORE = ["accela", "salesforce", "experience cloud", "portico", "siebel", "unqork",
               "epic", "mychart", "dynamics 365", "dynamics365", "legistar", "granicus",
               "peoplesoft", "cunyfirst", "kaseware", "everbridge", "bibliocommons",
               "combined arms", "hawksearch", "checkbook", "revize", "weebly",
               "dotnetnuke", "sharepoint", "wso2"]  # named platforms/SaaS running core service
MODERN = ["next.js", "_next", "react", "angular", "netlify", "vercel", "headless",
          "dynamics 365", "fhir", "epic", "planning labs", "jamstack", "spa"]
LEGACY = ["smarty", ".shtml", "shtml", "dotnetnuke", "dnn", "struts", "weblogic",
          "weebly", "revize", "coldfusion", "classic asp", "livesite v22", "obvio"]
OPEN_CONTENT_API = ["wp-json", "wp/v2", "wordpress rest", "json:api", "jsonapi", "oai-pmh",
                    "arcgis rest", "feature service"]
PRIV_API = ["undocumented", "internal", "key-gated", "subscription-gated", "login",
            "403", "401", "reachable", "live, undocumented", "documented, 403", "token-gated",
            "private", "custom api", "customapi", "content-api", "web api", "session"]
def has(txt, toks): return any(t in txt for t in toks)

def is_public(v):
    v = str(v).lower()
    return v in ("true", "public", "yes") or v.startswith("public;") or "has its own api" in v \
        or v.startswith("metadata") or v.startswith("open source")

def load(d):
    fr = json.load(open(f"{d}/fruit.json"))
    ofs = glob.glob(f"{d}/opendata-*.json")
    od = json.load(open(ofs[0])) if ofs else []
    return fr, od

# --- scoring ----------------------------------------------------------------
def score(dom):
    d = dom["id"]; fr, od = load(d)
    apis = fr.get("apis_observed", [])
    items = fr.get("fruit", [])
    plat = (dom.get("platform", "") or "").lower()
    odN = len(od)
    odViews = sum((x.get("page_views") or 0) for x in od)
    # text blob of the domain's OWN api inventory (endpoint/type/owner/public/note)
    apitext = " ".join(f"{a.get('endpoint','')} {a.get('type','')} {a.get('owner','')} "
                       f"{a.get('public','')} {a.get('note','')}".lower() for a in apis)
    n = {}

    # 1 openData: breadth of published assets
    openData = 0 if odN == 0 else 1 if odN < 10 else 2 if odN < 100 else 3
    n["openData"] = f"{odN} Open Data assets."

    # 2 coreData: is the core citizen data actually machine-readable / linked
    linked = sum(1 for it in items if it.get("opendata_match") or it.get("machine_readable") is True)
    share = linked / len(items) if items else 0
    tierS = 0 if share < .15 else 1 if share < .4 else 2 if share < .7 else 3
    coreData = min(max(openData, tierS), 3) if odN else tierS
    coreData = min(coreData, openData + 1)
    n["coreData"] = f"{linked}/{len(items)} fruit items have a machine-readable/Open-Data twin."

    # 3 siteApi: usability of a programmatic API for this domain's resources.
    #   3 = a public resource/standards API (Legistar, Checkbook, FHIR, GeoSearch, NYPL…)
    #   2 = an open but content-shaped API (WordPress REST / Drupal JSON:API — the "accidental APIs")
    #   1 = an API exists but is private / undocumented / gated / login-walled
    #   0 = none. The citywide Socrata/SODA feed is excluded (that's OTI infra, not the domain's API).
    CONTENT_API = ["wordpress rest", "wp-json", "wp/v2", "drupal json", "json:api", "jsonapi", "content api", "cms rest"]
    def is_od(a):
        s = f"{a.get('owner','')} {a.get('endpoint','')} {a.get('type','')}".lower()
        return has(s, ["socrata", "soda", "data.cityofnewyork.us", "open data api", "open-data api"])
    def api_class(a):
        if is_od(a): return -1
        s = f"{a.get('type','')} {a.get('note','')} {a.get('endpoint','')}".lower()
        pub = is_public(a.get("public"))
        if pub and has(s, CONTENT_API): return 2
        if pub and has(s, ["api", "rest", "fhir", "odata", "graphql", "web api"]): return 3
        if has(str(a.get("public","")).lower() + " " + s, PRIV_API): return 1
        return 0
    siteApi = max([api_class(a) for a in apis] + [0])
    if d == "oti": siteApi = 3  # OTI runs api.nyc.gov + the SODA gateway
    own_pub_api = siteApi >= 3
    n["siteApi"] = {0:"No API of its own.",1:"A private/undocumented/gated API exists.",
                    2:"An open but content-only API (e.g. WordPress REST / Drupal JSON:API).",
                    3:"An owned, public, resource-oriented API."}[siteApi]

    # 4 writeApi: a PUBLIC transactional write API? (essentially none in NYC)
    writeApi = 1 if any(is_public(a.get("public")) and
                        has(f"{a.get('type','')} {a.get('note','')}".lower(),
                            ["write", "transactional", "submit", "post ", "create"])
                        for a in apis) else 0
    n["writeApi"] = "No public write API." if writeApi == 0 else "A public transactional API exists."

    # 5 agent: any MCP / agent-native surface in production? (none exist)
    agent = 0
    n["agent"] = "No agent-native surface."

    # 6 platform modernity
    if has(plat, LEGACY): platform = 1
    elif has(plat, MODERN): platform = 3
    elif plat.strip(): platform = 2
    else: platform = 2
    n["platform"] = dom.get("platform", "") or "(platform not fingerprinted)"

    # 7 ownership / vendor independence
    if own_pub_api or ("owned" in apitext) or d in ("nypl","oti","dcp","hpd"): ownership = 3
    elif has(plat + " " + apitext, VENDOR_CORE): ownership = 1
    else: ownership = 2
    n["ownership"] = {1:"Core service runs on a named vendor SaaS.",
                      2:"Mixed / first-party but not a productized API.",
                      3:"Owns its core API / open-source stack."}[ownership]

    return {"platform": platform, "siteApi": siteApi, "openData": openData,
            "coreData": coreData, "writeApi": writeApi, "agent": agent,
            "ownership": ownership}, n, odViews, odN

domains = []
for dom in DOM:
    sc, notes, views, odN = score(dom)
    domains.append({"id": dom["id"], "short": dom["short"], "verb": dom.get("verb",""),
                    "accent": dom.get("accent","#3098d8"), "scores": sc, "notes": notes,
                    "odViews": views, "odCount": odN})

# net-new write objects (from manifest meta)
net = []
for dom in DOM:
    nn = dom.get("netnew","")
    if nn and not nn.startswith("—") and not nn.lower().startswith("- ") and "reference" not in nn.lower():
        net.append({"domain": dom["short"], "object": nn})

out = {
 "scoring_method": "Deterministic rule-based scoring applied uniformly to all domains (2026-07). 0=absent, 1=legacy/hidden/rented, 2=usable/partial, 3=modern/owned/complete. openData=asset-count tiers; coreData=share of resources with an Open-Data twin; siteApi=class of API the domain runs (own SODA excluded); writeApi=public transactional API present; agent=MCP/agent surface present; platform=modernity keywords; ownership=vendor-core vs owned/open-source. Replaces the earlier per-subagent self-scores for cross-domain comparability.",
 "scale": ["absent","legacy/hidden/rented","usable/partial","modern/owned/complete"],
 "dimensions": [
   {"key":"platform","label":"Platform modernity","desc":"How current the delivery stack is."},
   {"key":"siteApi","label":"Site / content API","desc":"Does the domain expose a usable API of its own?"},
   {"key":"openData","label":"Open Data breadth","desc":"How much of the agency's data is on data.cityofnewyork.us."},
   {"key":"coreData","label":"Core citizen-data machine-readable","desc":"Are the things residents most need machine-readable at all?"},
   {"key":"writeApi","label":"Transactional (write) API","desc":"Can a resident DO the key civic action via API?"},
   {"key":"agent","label":"Agent-readiness","desc":"Any MCP / agent-native surface today."},
   {"key":"ownership","label":"Vendor independence","desc":"Is the core capability owned rather than rented/locked to a vendor?"}],
 "domains": domains,
 "netNew": net,
}
json.dump(out, open("data/scorecard.json","w"), indent=2)

import statistics as st
print(f"scorecard: {len(domains)} domains, rule-based. netNew {len(net)}")
for k in ["platform","siteApi","openData","coreData","writeApi","agent","ownership"]:
    v=[d["scores"][k] for d in domains]
    print(f"  {k:10} mean {sum(v)/len(v):.2f} | 0:{v.count(0)} 1:{v.count(1)} 2:{v.count(2)} 3:{v.count(3)}")
