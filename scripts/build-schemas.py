#!/usr/bin/env python3
"""Schema index — data/schemas.json for the per-schema detail page (schema.html).

For every distinct object-schema TITLE across all domains, record each domain that
models it: the raw schema file (fetched live by schema.html), the domain's OpenAPI,
and the operations in that OpenAPI that $ref the schema (the APIs that use it).

Keyed on schema title, matching data/entities.json (both come from schemas/*.json
titles), so entities.html can link every entity row straight to schema.html?e=<title>.

Run from repo root: python3 scripts/build-schemas.py
"""
import json, glob, os, collections, sys
try:
    import yaml
except ImportError:
    print("pyyaml required (pip install pyyaml)"); sys.exit(1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
DOMAINS = json.load(open("data/manifest.json"))["domains"]

def collect_refs(node):
    out = []
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "$ref" and isinstance(v, str):
                out.append(v)
            else:
                out.extend(collect_refs(v))
    elif isinstance(node, list):
        for x in node:
            out.extend(collect_refs(x))
    return out

def ref_basename(ref):
    p = ref.split("#")[0]
    return p.rsplit("/", 1)[-1] if p else ""

by_title = collections.defaultdict(list)   # title -> [instance]

for d in DOMAINS:
    did = d["id"]
    # 1) parse the domain's OpenAPI once: component-schema -> referenced filenames, and operations
    oa_path = None
    ops = []                       # [{method,path,operationId,summary,write,files:set}]
    comp_files = {}                # componentSchemaName -> set(filenames)
    oa_files = glob.glob(f"{did}/openapi/*.yaml")
    if oa_files:
        oa_path = oa_files[0]
        try:
            doc = yaml.safe_load(open(oa_path))
        except Exception:
            doc = None
        if isinstance(doc, dict):
            for cname, cspec in (doc.get("components", {}).get("schemas", {}) or {}).items():
                comp_files[cname] = {ref_basename(r) for r in collect_refs(cspec)}
            for path, methods in (doc.get("paths", {}) or {}).items():
                if not isinstance(methods, dict):
                    continue
                for mth, spec in methods.items():
                    if not isinstance(spec, dict) or "operationId" not in spec:
                        continue
                    files = set()
                    for r in collect_refs(spec):
                        bn = ref_basename(r)
                        if bn:
                            files.add(bn)
                        else:  # in-doc ref like #/components/schemas/Name
                            name = r.split("/")[-1]
                            files |= comp_files.get(name, set())
                    ops.append({"method": mth.upper(), "path": path,
                                "operationId": spec["operationId"],
                                "summary": spec.get("summary", ""),
                                "write": mth.lower() in ("post", "put", "patch", "delete"),
                                "files": files})

    # 2) each schema file (except shared _common.json) becomes an instance under its title
    for sp in sorted(glob.glob(f"{did}/schemas/*.json")):
        base = os.path.basename(sp)
        if base == "_common.json":
            continue
        try:
            sd = json.load(open(sp))
        except Exception:
            continue
        title = sd.get("title") or base
        used_by = [{"method": o["method"], "path": o["path"], "operationId": o["operationId"],
                    "summary": o["summary"], "write": o["write"]}
                   for o in ops if base in o["files"]]
        by_title[title].append({
            "domain": did, "short": d["short"], "verb": d.get("verb", ""), "accent": d.get("accent", "#3098d8"),
            "file": f"{did}/schemas/{base}",
            "description": (sd.get("description", "") or "")[:280],
            "openapi": (f"{did}/openapi/{os.path.basename(oa_path)}" if oa_path else None),
            "ops": used_by,
        })

schemas = [{"title": t, "count": len(insts),
            "instances": sorted(insts, key=lambda x: x["short"].lower())}
           for t, insts in sorted(by_title.items(), key=lambda kv: kv[0].lower())]

out = {
    "generated_from": "schemas/*.json titles across all domains; ops from openapi/*.yaml $refs",
    "count": len(schemas),
    "total_instances": sum(s["count"] for s in schemas),
    "schemas": schemas,
}
json.dump(out, open("data/schemas.json", "w"), indent=1)
print(f"wrote data/schemas.json — {out['count']} distinct schema titles, {out['total_instances']} instances")
multi = [s for s in schemas if s["count"] > 1]
print(f"  {len(multi)} modeled in 2+ domains; e.g.",
      ", ".join(f"{s['title']}({s['count']})" for s in sorted(multi, key=lambda s: -s['count'])[:6]))
