#!/usr/bin/env python3
"""Build the static reference API — genuinely GET-callable example data for the
Programmable City, served straight off GitHub Pages, plus the bundled data file
the @api-common/nyc-mcp stdio server reads.

For each agency it synthesizes 2 example records per object schema (resolving
_common.json + nyc-commons $refs), writes them at stable static URLs, and builds
a catalog. No backend — every endpoint is a static JSON file, clearly example data.

  experience/api/index.json                 — catalog root (agencies + example endpoints)
  experience/api/<slug>/index.json          — one agency's collections
  experience/api/<slug>/<collection>.json   — { data: [example records], meta }
  experience/mcp-server/data.json           — compact bundle for the MCP server

Run from repo root: python3 scripts/build-gateway.py
"""
import json, glob, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
RAW = "https://raw.githubusercontent.com/api-evangelist/nyc/main"
SITE = "https://nyc.apievangelist.com"
API_BASE = f"{SITE}/experience/api"

manifest = json.load(open("data/manifest.json"))
DOMAINS = manifest["domains"]
short = {d["id"]: d["short"] for d in DOMAINS}

# ---- $ref resolver (local _common.json + nyc-commons absolute URLs) ----
_cache = {}
def load_json(path):
    if path not in _cache:
        _cache[path] = json.load(open(path))
    return _cache[path]

def resolve_ref(ref, base_dir):
    """Return the schema fragment a $ref points at, or None."""
    try:
        if ref.startswith("http"):
            m = re.search(r"/nyc-commons/([^#]+)#/\$defs/(.+)$", ref)
            if m:
                doc = load_json(f"nyc-commons/{m.group(1)}")
                return doc.get("$defs", {}).get(m.group(2))
            return None
        file_part, _, frag = ref.partition("#")
        doc = load_json(os.path.join(base_dir, file_part)) if file_part else None
        if doc is None:
            return None
        node = doc
        for seg in [s for s in frag.split("/") if s]:
            seg = seg.replace("~1", "/").replace("~0", "~")
            node = node.get(seg) if isinstance(node, dict) else None
            if node is None:
                return None
        return node
    except Exception:
        return None

# ---- example value synthesis ----
def ex_string(name, schema):
    n = name.lower()
    enum = schema.get("enum")
    if enum:
        return next((e for e in enum if e is not None), None)
    fmt = schema.get("format", "")
    if "bbl" == n or n.endswith("bbl"): return "1000160001"
    if "bin" == n or n.endswith("bin"): return "1000000"
    if "borough" in n: return "Manhattan"
    if n in ("zip", "zipcode", "postcode", "postalcode") or "zip" in n: return "10007"
    if "censustract" in n or n == "ct2020": return "000100"
    if n.startswith("nta"): return "MN0101"
    if "email" in n or fmt == "email": return "info@example.nyc.gov"
    if "phone" in n: return "311"
    if fmt == "date" or n.endswith("date"): return "2025-06-01"
    if fmt == "date-time": return "2025-06-01T09:00:00-04:00"
    if fmt == "uri" or n in ("url", "href", "link"): return "https://www.nyc.gov"
    if "status" in n: return "Active"
    if "borocode" in n or "borocd" in n: return "1"
    if n in ("housenumber", "house_number"): return "280"
    if "street" in n: return "Broadway"
    if "name" in n or "title" in n: return f"Example {name}"
    if n.endswith("id") or "number" in n or n.endswith("no"): return "EX-0001"
    return f"example {name}"

def synth(schema, base_dir, depth=0, name="root"):
    if not isinstance(schema, dict):
        return None
    if "$ref" in schema:
        tgt = resolve_ref(schema["$ref"], base_dir)
        return synth(tgt, base_dir, depth, name) if tgt and depth < 5 else None
    for comb in ("allOf", "anyOf", "oneOf"):
        if comb in schema and schema[comb]:
            return synth(schema[comb][0], base_dir, depth, name)
    t = schema.get("type")
    if isinstance(t, list):
        t = next((x for x in t if x != "null"), t[0])
    if "enum" in schema:
        return next((e for e in schema["enum"] if e is not None), None)
    if t == "object" or "properties" in schema:
        if depth >= 4:
            return {}
        out = {}
        for k, v in (schema.get("properties") or {}).items():
            val = synth(v, base_dir, depth + 1, k)
            if val is not None:
                out[k] = val
        return out
    if t == "array":
        item = synth(schema.get("items", {}), base_dir, depth + 1, name)
        return [item] if item is not None else []
    if t == "integer":
        n = name.lower()
        if "district" in n: return 1
        if "board" in n: return 101
        if "year" in n: return 2025
        return 1
    if t == "number":
        n = name.lower()
        if "lat" in n: return 40.7127
        if "lon" in n or "lng" in n: return -74.0059
        if "amount" in n or "money" in n or "total" in n: return 125000.0
        return 1.0
    if t == "boolean":
        return True
    if t == "null":
        return None
    return ex_string(name, schema)

def vary(rec, i):
    """Make record i distinct by tweaking an id/name-ish field."""
    if not isinstance(rec, dict):
        return rec
    r = dict(rec)
    for k in r:
        kl = k.lower()
        if isinstance(r[k], str) and (kl.endswith("id") or "number" in kl or kl == "id" or "name" in kl or "title" in kl):
            r[k] = f"{r[k]}-{i+1}" if "-" in r[k] else f"{r[k]} {i+1}"
            break
    return r

# ---- build per-agency example collections + catalog ----
catalog = {"name": "NYC — Programmable City (reference API)", "base": API_BASE,
           "note": "Static reference API — every endpoint is example data at a stable URL, served off GitHub Pages. Reads only; write operations are documented in the OpenAPI but not executed here. Data is synthesized for demonstration.",
           "agencies": []}
mcp_bundle = {"generatedFrom": "static reference API", "base": API_BASE, "agencies": {}, "schemas": {}}
os.makedirs("experience/api", exist_ok=True)
total_records = total_collections = 0

for d in DOMAINS:
    did = d["id"]
    sdir = f"{did}/schemas"
    schemas = [s for s in sorted(glob.glob(f"{sdir}/*.json")) if os.path.basename(s) != "_common.json"]
    colls = []
    for sp in schemas[:8]:
        try:
            sc = load_json(sp)
        except Exception:
            continue
        title = sc.get("title") or os.path.basename(sp)[:-5]
        cslug = re.sub(r"[^a-z0-9]+", "-", os.path.basename(sp)[:-5].lower()).strip("-")
        base_one = synth(sc, sdir)
        if not isinstance(base_one, dict) or not base_one:
            continue
        recs = [vary(base_one, i) for i in range(2)]
        url = f"{API_BASE}/{did}/{cslug}.json"
        payload = {"agency": short[did], "collection": title, "schema": f"{RAW}/{sp}",
                   "count": len(recs), "example": True, "data": recs}
        os.makedirs(f"experience/api/{did}", exist_ok=True)
        json.dump(payload, open(f"experience/api/{did}/{cslug}.json", "w"), indent=1)
        colls.append({"collection": title, "slug": cslug, "url": url, "count": len(recs),
                      "schema": f"{RAW}/{sp}"})
        total_records += len(recs); total_collections += 1
    if not colls:
        continue
    agency_index = {"agency": short[did], "id": did, "profile": f"{SITE}/domain.html?d={did}",
                    "openapi": f"{RAW}/{glob.glob(f'{did}/openapi/*.y*ml')[0]}" if glob.glob(f"{did}/openapi/*.y*ml") else None,
                    "mcp": f"{RAW}/{glob.glob(f'{did}/mcp/*.json')[0]}" if glob.glob(f"{did}/mcp/*.json") else None,
                    "collections": colls}
    json.dump(agency_index, open(f"experience/api/{did}/index.json", "w"), indent=1)
    catalog["agencies"].append({"id": did, "agency": short[did], "index": f"{API_BASE}/{did}/index.json",
                                "collections": len(colls)})
    mcp_bundle["agencies"][did] = {"agency": short[did], "collections":
        [{"collection": c["collection"], "slug": c["slug"], "url": c["url"], "data": json.load(open(f"experience/api/{did}/{c['slug']}.json"))["data"]} for c in colls]}

json.dump(catalog, open("experience/api/index.json", "w"), indent=1)

# a nyc-commons place example (for look_up_place)
place_example = {"example": True, "bbl": "1000160001", "bin": "1001234",
    "name": "Example Building", "address": {"houseNumber": "280", "streetName": "Broadway", "borough": "Manhattan", "zip": "10007"},
    "coordinates": {"latitude": 40.7127, "longitude": -74.0059},
    "geography": {"borough": "Manhattan", "borocode": 1, "communityBoard": 101, "councilDistrict": 1, "censusTract": "000100", "nta": "MN0101"},
    "keys": [{"keyType": "BBL", "value": "1000160001", "owningDomain": "dcp"},
             {"keyType": "BIN", "value": "1001234", "owningDomain": "dcp"}],
    "agenciesKeyedHere": ["dob", "dof", "hpd", "dcp", "nyc311", "dep"]}
json.dump(place_example, open("experience/api/place-example.json", "w"), indent=1)

# compact bundle for the MCP server (catalog + examples + skills + geography)
mcp_bundle["catalog"] = catalog
mcp_bundle["place_example"] = place_example
mcp_bundle["skills"] = json.load(open("experience/skills/index.json"))["skills"]
mcp_bundle["geography"] = json.load(open("nyc-commons/geography.json"))["$defs"]
mcp_bundle["prompts"] = json.load(open("experience/nyc-mcp.json"))["prompts"]
os.makedirs("experience/mcp-server", exist_ok=True)
json.dump(mcp_bundle, open("experience/mcp-server/data.json", "w"), indent=1)

print(f"static API: {len(catalog['agencies'])} agencies, {total_collections} collections, {total_records} example records")
print(f"mcp bundle: {os.path.getsize('experience/mcp-server/data.json')//1024} KB")
