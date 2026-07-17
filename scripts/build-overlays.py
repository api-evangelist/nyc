#!/usr/bin/env python3
"""Interface localization via OpenAPI Overlays.

Demonstrates how ONE base API contract + N per-language Overlay documents
(OpenAPI Overlay Specification 1.0) yield N localized interfaces — translating
only the human-readable INTERFACE strings (title, operation summaries/
descriptions), never the paths, operationIds, schema field names, enums, or
DATA. Because the MCP tool layer is generated 1:1 from the OpenAPI operations,
the same overlay also produces a localized MCP server.

Worked example: NYC HPD (Housing Connect affordable-housing lottery) — whose
applicants are exactly the limited-English population NYC Local Law 30 serves.

Pipeline (from repo root):
  translations.json  ->  per-language *.overlay.yaml   (the standard artifact)
                     ->  dist/hpd.<code>.openapi.yaml   (localized OpenAPI)
                     ->  dist/hpd.<code>.mcp.json       (localized MCP tools)
                     ->  dist/index.json                (manifest for the site)

Run: python3 scripts/build-overlays.py
"""
import json, os, re, copy, sys
try:
    import yaml
except ImportError:
    print("pyyaml required (pip install pyyaml)"); sys.exit(1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
OVL = "experience/overlays"
AGENCY = "hpd"
BASE = f"{OVL}/{AGENCY}"
DIST = f"{BASE}/dist"
os.makedirs(DIST, exist_ok=True)

langs = json.load(open(f"{OVL}/languages.json"))
tr = json.load(open(f"{BASE}/translations.json"))
strings = tr["strings"]
base_openapi = yaml.safe_load(open(tr["base_openapi"]))
base_mcp = json.load(open(tr["base_mcp"]))

# --- minimal JSONPath setter for the simple targets used in these overlays ---
# supports $.a.b and $['x'].y forms (dotted keys + ['bracketed'] keys); no arrays.
TOKEN = re.compile(r"\.([^.\[\]]+)|\['([^']*)'\]")

def path_tokens(target):
    if not target.startswith("$"):
        raise ValueError(f"unsupported target: {target}")
    return [g1 or g2 for g1, g2 in TOKEN.findall(target[1:])]

def apply_action(doc, target, value):
    toks = path_tokens(target)
    node = doc
    for t in toks[:-1]:
        if t not in node:
            raise KeyError(f"target not found in base document: {target} (missing '{t}')")
        node = node[t]
    node[toks[-1]] = value

# --- build one language ---
def build_lang(lang):
    code = lang["code"]
    strand = tr["translations"].get(code, {})
    # 1) the Overlay document (the standard artifact)
    actions = []
    for s in strings:
        if s["id"] in strand:
            actions.append({"target": s["target"], "update": strand[s["id"]]})
    overlay = {
        "overlay": "1.0.0",
        "info": {"title": f"NYC HPD API — {lang['name']} ({code}) interface localization",
                 "version": base_openapi.get("info", {}).get("version", "0.1.0")},
        "x-language": code,
        "x-language-name": lang["name"],
        "x-language-endonym": lang["endonym"],
        "x-text-direction": lang["dir"],
        "extends": f"../../../{tr['base_openapi']}",
        "actions": actions,
    }
    with open(f"{BASE}/hpd.{code}.overlay.yaml", "w") as f:
        yaml.safe_dump(overlay, f, allow_unicode=True, sort_keys=False, width=1000)

    # 2) apply the overlay -> localized OpenAPI (interface only; data untouched)
    localized = copy.deepcopy(base_openapi)
    for a in actions:
        apply_action(localized, a["target"], a["update"])
    localized.setdefault("info", {})["x-language"] = code
    localized["info"]["x-text-direction"] = lang["dir"]
    with open(f"{DIST}/hpd.{code}.openapi.yaml", "w") as f:
        yaml.safe_dump(localized, f, allow_unicode=True, sort_keys=False, width=1000)

    # 3) same overlay -> localized MCP tools (tools derive 1:1 from OpenAPI ops)
    op2str = {s["operationId"]: strand.get(s["id"]) for s in strings if s.get("operationId")}
    mcp = copy.deepcopy(base_mcp)
    localized_tools = 0
    for tool in mcp.get("tools", []):
        oid = tool.get("x-openapi-operation")
        if oid in op2str and op2str[oid]:
            tool["description"] = op2str[oid]
            localized_tools += 1
    mcp.setdefault("server", {})["x-language"] = code
    with open(f"{DIST}/hpd.{code}.mcp.json", "w") as f:
        json.dump(mcp, f, ensure_ascii=False, indent=1)

    return {"code": code, "name": lang["name"], "endonym": lang["endonym"], "dir": lang["dir"],
            "overlay": f"hpd.{code}.overlay.yaml", "openapi": f"dist/hpd.{code}.openapi.yaml",
            "mcp": f"dist/hpd.{code}.mcp.json", "strings": len(actions), "mcpToolsLocalized": localized_tools}

built = [build_lang(l) for l in langs["languages"]]

manifest = {
    "agency": AGENCY,
    "base_openapi": tr["base_openapi"],
    "base_mcp": tr["base_mcp"],
    "spec": "https://spec.openapis.org/overlay/latest.html",
    "caveat": tr["caveat"],
    "base_language": langs["base"],
    "translated_strings_per_language": len(strings),
    "targets": [{"id": s["id"], "target": s["target"], "en": s["en"], "operationId": s.get("operationId")} for s in strings],
    "languages": built,
}
json.dump(manifest, open(f"{BASE}/index.json", "w"), ensure_ascii=False, indent=1)
# also expose the manifest to the site data dir for experience.html
json.dump(manifest, open("data/overlays.json", "w"), ensure_ascii=False, indent=1)

# top-level catalog across all overlay-localized agencies (currently one: hpd)
catalog = {
    "note": "Overlay-based interface localization sets across the NYC Modernization study. Each agency set localizes the API/agent interface (never the data) into the ten citywide languages of NYC Local Law 30, from one base contract.",
    "spec": "https://spec.openapis.org/overlay/latest.html",
    "base_language": langs["base"],
    "languages": langs["languages"],
    "agencies": [{
        "agency": AGENCY,
        "base_openapi": tr["base_openapi"],
        "languages": len(built),
        "translated_strings_per_language": len(strings),
        "manifest": f"{AGENCY}/index.json",
        "readme": "README.md",
    }],
}
json.dump(catalog, open(f"{OVL}/index.json", "w"), ensure_ascii=False, indent=1)

print(f"overlays: {len(built)} languages x {len(strings)} interface strings for '{AGENCY}'")
print("  wrote per-language overlay.yaml + dist/openapi.yaml + dist/mcp.json + index.json + data/overlays.json")
for b in built:
    print(f"   {b['code']:<7} {b['name']:<20} {b['strings']} strings, {b['mcpToolsLocalized']} MCP tools localized")
