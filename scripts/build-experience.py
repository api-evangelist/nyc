#!/usr/bin/env python3
"""Build the NYC "programmable city" experience layer — the API -> MCP -> Agent-Skill
chain across all 67 domains, in the format the API Experience tool renders
(experience.apicommons.org), minus the free/pro tiering and AI enrichment.

Reads every domain's openapi/*.yaml + mcp/*.json + the manifest/transactions, maps
each of the 721 REST operations to its MCP tool and to one of ten common
government-process Agent Skills, and emits:

  data/experience.json          — aggregated chain for the single-page doc
  experience/nyc.apis.json       — APIs.json 0.21 descriptor (experience-tool compatible)
  experience/nyc-openapi.json    — one unified OpenAPI 3.1 across all paths, each op
                                    carrying x-mcp-tool + x-agent-skill, top-level x-apis-io
  experience/nyc-mcp.json        — NYC-wide MCP definition: tool index + prompts + resources
  experience/skills/<id>.md      — the ten Agent Skills (+ index.json)
  EXPERIENCE.md                  — writeup
and enriches each domain mcp/*.json in place with per-tool x-agent-skill.

Run from repo root: python3 scripts/build-experience.py
"""
import yaml, json, glob, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
RAW = "https://raw.githubusercontent.com/api-evangelist/nyc/main"
SITE = "https://nyc.apievangelist.com"

manifest = json.load(open("data/manifest.json"))
DOMAINS = manifest["domains"]
short = {d["id"]: d["short"] for d in DOMAINS}
verb = {d["id"]: d.get("verb", "") for d in DOMAINS}

# ---------------- the ten common government-process Agent Skills ----------------
SKILLS = [
 {"id": "apply-for-a-permit-license-or-benefit", "name": "Apply for a permit, license, or benefit",
  "group": "Act", "primitive": "Apply", "accent": "#3098d8",
  "desc": "Start and track an application to the city — a building permit, business or professional license, benefit (SNAP/cash/Medicaid), grant, school or college admission, or lottery.",
  "whenToUse": "The resident wants to apply for, enroll in, or file for something the city grants. Resolve the right agency, collect the required fields against its schema, submit, and return a tracking id."},
 {"id": "report-a-problem-or-file-a-complaint", "name": "Report a problem or file a complaint",
  "group": "Act", "primitive": "Report/Complain", "accent": "#c0504d",
  "desc": "File a 311-style service request or a complaint/tip with the agency that owns it — noise, a pothole, a building condition, a consumer or rights complaint, a tip to an investigator.",
  "whenToUse": "The resident is reporting an issue or misconduct. Classify the problem, route it to the owning agency's report tool, attach a location (BBL/BIN/coordinates), and return a service-request id."},
 {"id": "request-public-records", "name": "Request public records",
  "group": "Act", "primitive": "Request-records", "accent": "#8e6fb8",
  "desc": "Make a records request — a FOIL request, a vital record (birth/death/marriage), a certified document, or a transcript.",
  "whenToUse": "The resident needs an official copy or a records disclosure. Identify the record type and custodian agency, submit the request, and track fulfillment."},
 {"id": "schedule-or-reserve", "name": "Schedule or reserve",
  "group": "Act", "primitive": "Schedule/Reserve", "accent": "#2e9e6b",
  "desc": "Book an appointment, inspection, hearing slot, facility, or hold — an OATH hearing, a DOB inspection, a park/venue reservation, a library hold.",
  "whenToUse": "The resident needs a time or a resource reserved. Find availability, reserve it, and return a confirmation."},
 {"id": "register-or-enroll", "name": "Register or enroll",
  "group": "Act", "primitive": "Register", "accent": "#d6923a",
  "desc": "Register or enroll with the city — register to vote or request a ballot, register a business or vendor, enroll in a program.",
  "whenToUse": "The resident is establishing a standing status. Collect the required identity/eligibility fields, register, and confirm."},
 {"id": "dispute-or-appeal", "name": "Dispute or appeal",
  "group": "Act", "primitive": "Dispute/File", "accent": "#b5701f",
  "desc": "Challenge a city determination — appeal a property-tax assessment, dispute a violation or ticket, respond to a summons, file a grievance.",
  "whenToUse": "The resident is contesting a charge or decision. Identify the case, assemble the response against the agency's rules, and file the dispute/appeal."},
 {"id": "pay-a-city-charge", "name": "Pay a city charge",
  "group": "Act", "primitive": "Pay", "accent": "#4b8f8c",
  "desc": "Pay a fine, fee, tax, or bill owed to the city and get a receipt.",
  "whenToUse": "The resident owes the city money. Resolve the charge, take payment, and return a confirmation."},
 {"id": "look-up-a-property-or-place", "name": "Look up a property or place",
  "group": "Know", "primitive": "Read · geography", "accent": "#2f7ecf",
  "desc": "Resolve a NYC address, BBL, or BIN and return everything the city knows about that place across agencies — its districts, who represents it, and its records (buildings, housing, environment, complaints).",
  "whenToUse": "The question is anchored to a location (\"what's near me?\", \"who represents this block?\", \"what's on file for this building?\"). Resolve to a nyc-commons Place and fan out across the agencies keyed on its BBL/BIN."},
 {"id": "check-application-or-case-status", "name": "Check application or case status",
  "group": "Know", "primitive": "Read · status", "accent": "#6a7f8c",
  "desc": "Look up the status of an application, permit, complaint, case, or request across agencies.",
  "whenToUse": "The resident wants to know where something stands. Identify the case by its id/owner and return its current status and history."},
 {"id": "search-city-data-and-records", "name": "Search city data and records",
  "group": "Know", "primitive": "Read · data", "accent": "#5b8a72",
  "desc": "Search and read the city's open records and datasets — filings, permits, violations, licenses, budgets, contracts, results — the read surface across all 67 agencies.",
  "whenToUse": "The question needs facts from a city dataset or record. Pick the owning agency's search/get tools and return the records."},
]
SKILL_IDS = {s["id"] for s in SKILLS}

WRITE_RULES = [
 ("report-a-problem-or-file-a-complaint", ["report", "complaint", "complain", "tip", "service request", "servicerequest", "service_request", "311", "incident", "grievance"]),
 ("request-public-records", ["foil", "records request", "vital", "certificate request", "transcript", "record request", "public record"]),
 ("schedule-or-reserve", ["schedule", "appointment", "inspection", "reserve", "reservation", "book", "hold", "permit event", "event permit"]),
 ("register-or-enroll", ["register", "registration", "voter", "ballot"]),
 ("dispute-or-appeal", ["dispute", "appeal", "challenge", "contest", "hearing response", "respond to", "summons", "protest"]),
 ("pay-a-city-charge", ["pay", "payment", "invoice", "settle", " fine", "fee payment"]),
 ("apply-for-a-permit-license-or-benefit", ["apply", "application", "file ", "filing", "submit", "permit", "license", "benefit", "grant", "admission", "enroll", "enrollment", "register a business", "lottery", "onboard"]),
]

def classify(method, opid, path, summary, tags):
    text = " ".join([opid or "", path or "", summary or "", " ".join(tags or [])]).lower()
    if method in ("post", "put", "patch", "delete"):
        for skill, kws in WRITE_RULES:
            if any(k in text for k in kws):
                return skill
        return "apply-for-a-permit-license-or-benefit"
    if any(k in text for k in ["status", "track", " state of"]):
        return "check-application-or-case-status"
    if any(k in text for k in ["building", "property", "parcel", " bbl", " bin", "place", "address", "district", "poll site", "pollsite", "location", "geograph", " lot", "landmark", "park ", "facility", "premises", "zone", "borough"]):
        return "look-up-a-property-or-place"
    return "search-city-data-and-records"

# ---------------- read each domain's OpenAPI + MCP ----------------
def load_openapi(did):
    fs = glob.glob(f"{did}/openapi/*.yaml") + glob.glob(f"{did}/openapi/*.yml")
    if not fs:
        return None, []
    oa = yaml.safe_load(open(fs[0]))
    ops = []
    for path, ms in (oa.get("paths") or {}).items():
        if not isinstance(ms, dict):
            continue
        for m, op in ms.items():
            if m in ("get", "post", "put", "patch", "delete") and isinstance(op, dict):
                ops.append({"method": m, "path": path, "operationId": op.get("operationId"),
                            "summary": op.get("summary", ""), "tags": op.get("tags", []) or []})
    return {"file": fs[0], "info": oa.get("info", {}), "servers": oa.get("servers", [])}, ops

def load_mcp(did):
    fs = glob.glob(f"{did}/mcp/*.json")
    if not fs:
        return None, fs
    return json.load(open(fs[0])), fs[0]

domain_blocks = []
skill_index = collections.defaultdict(lambda: {"operations": 0, "domains": set(), "tools": set()})
tot_ops = tot_tools = tot_write = 0

for d in DOMAINS:
    did = d["id"]
    oa, ops = load_openapi(did)
    mcp, mcp_path = load_mcp(did)
    op2tool = {}
    tools = []
    if mcp:
        for t in mcp.get("tools", []):
            tools.append({"name": t["name"], "title": t.get("title", ""), "description": t.get("description", ""),
                          "operationId": t.get("x-openapi-operation"),
                          "write": not (t.get("annotations", {}) or {}).get("readOnlyHint", False)})
            if t.get("x-openapi-operation"):
                op2tool[t["x-openapi-operation"]] = t["name"]
    op_rows = []
    for o in ops:
        write = o["method"] in ("post", "put", "patch", "delete")
        skill = classify(o["method"], o["operationId"], o["path"], o["summary"], o["tags"])
        tool = op2tool.get(o["operationId"])
        op_rows.append({**o, "write": write, "mcpTool": tool, "skill": skill})
        skill_index[skill]["operations"] += 1
        skill_index[skill]["domains"].add(did)
        if tool:
            skill_index[skill]["tools"].add(f"{did}:{tool}")
        tot_ops += 1
        tot_write += 1 if write else 0
    tot_tools += len(tools)
    # tool -> skill (from the tool's operation, else from tool name/desc)
    for t in tools:
        srow = next((r for r in op_rows if r["operationId"] == t["operationId"]), None)
        t["skill"] = srow["skill"] if srow else classify("post" if t["write"] else "get", t["name"], "", t.get("description", ""), [])
    dom_skills = sorted({r["skill"] for r in op_rows})
    info = (oa or {}).get("info", {})
    domain_blocks.append({
        "id": did, "short": short[did], "verb": verb.get(did, ""),
        "title": info.get("title", short[did]),
        "summary": info.get("summary", "") or (info.get("description", "") or "")[:240],
        "openapi": f"{RAW}/{oa['file']}" if oa else None,
        "mcp": f"{RAW}/{mcp_path}" if mcp else None,
        "operationCount": len(op_rows), "toolCount": len(tools), "writeCount": sum(1 for r in op_rows if r["write"]),
        "skills": dom_skills,
        "operations": op_rows, "tools": tools,
    })

# enrich each domain MCP in place with per-tool x-agent-skill
for db in domain_blocks:
    did = db["id"]
    fs = glob.glob(f"{did}/mcp/*.json")
    if not fs:
        continue
    j = json.load(open(fs[0]), object_pairs_hook=collections.OrderedDict)
    tskill = {t["name"]: t["skill"] for t in db["tools"]}
    for t in j.get("tools", []):
        if t["name"] in tskill:
            t["x-agent-skill"] = tskill[t["name"]]
    j.setdefault("x-agent-skills", {"index": f"{SITE}/experience/skills/index.json",
                                    "note": "Each tool maps to one of the ten NYC common government-process Agent Skills via x-agent-skill."})
    json.dump(j, open(fs[0], "w"), indent=2)
    open(fs[0], "a").write("\n")

# ---------------- NYC-wide MCP prompts + resources ----------------
PROMPTS = [
 {"name": "who_represents_this_address", "description": "Given a NYC address, return the council member, community board, borough, and every district that represents it.", "uses": ["look-up-a-property-or-place"], "arguments": ["address"]},
 {"name": "everything_about_this_place", "description": "Everything the city knows about a BBL/BIN/address across agencies — buildings, housing, environment, complaints, landmarks.", "uses": ["look-up-a-property-or-place", "search-city-data-and-records"], "arguments": ["address_or_bbl"]},
 {"name": "how_do_i_apply_for", "description": "Explain how to apply for a given permit, license, or benefit and start the application with the owning agency.", "uses": ["apply-for-a-permit-license-or-benefit"], "arguments": ["what"]},
 {"name": "report_a_problem_at", "description": "File a 311-style report or complaint for a location and route it to the owning agency.", "uses": ["report-a-problem-or-file-a-complaint"], "arguments": ["problem", "location"]},
 {"name": "whats_the_status_of_my", "description": "Look up the status of an application, permit, complaint, or case across agencies by its id.", "uses": ["check-application-or-case-status"], "arguments": ["case_id"]},
 {"name": "what_agency_handles", "description": "Identify which NYC agency owns a given task or record and hand off to its tools.", "uses": ["search-city-data-and-records"], "arguments": ["task"]},
 {"name": "find_a_service_near_me", "description": "Find city services or facilities near a location (parks, libraries, clinics, offices).", "uses": ["look-up-a-property-or-place"], "arguments": ["location", "service_type"]},
]
RESOURCES = [
 {"uri": "nyc://catalog", "name": "NYC API catalog", "description": "All 67 agency APIs with their OpenAPI, MCP server, and Agent Skills.", "mimeType": "application/json", "backing": "data/manifest.json"},
 {"uri": "nyc://commons/geography", "name": "nyc-commons geography spine", "description": "The shared Borough / BBL / BIN / district vocabulary every place resolves to.", "mimeType": "application/schema+json", "backing": "nyc-commons/geography.json"},
 {"uri": "nyc://transactions", "name": "Citizen-transaction taxonomy", "description": "The common government processes (Apply, Report, Request-records, Schedule, Register, Dispute, Pay) and the domains behind each.", "mimeType": "application/json", "backing": "data/transactions.json"},
 {"uri": "nyc://linkage", "name": "Cross-agency key registry", "description": "The join keys (BBL, BIN, council district, ...) that link one agency's records to another's.", "mimeType": "application/json", "backing": "data/linkage.json"},
 {"uri": "nyc://skills", "name": "Government-process skills index", "description": "The ten common government-process Agent Skills and the operations each orchestrates.", "mimeType": "application/json", "backing": "experience/skills/index.json"},
 {"uri": "nyc://place/{bbl}", "name": "Resolved place (templated)", "description": "A nyc-commons Place for a BBL — its geography spine plus the agencies keyed on it.", "mimeType": "application/json", "template": True},
 {"uri": "nyc://agency/{slug}", "name": "Agency profile (templated)", "description": "One agency's API + MCP + skills profile.", "mimeType": "application/json", "template": True},
]

# finalize skill index
skills_out = []
for s in SKILLS:
    idx = skill_index.get(s["id"], {"operations": 0, "domains": set(), "tools": set()})
    doms = sorted(idx["domains"])
    skills_out.append({**s, "operationCount": idx["operations"], "domainCount": len(doms),
                       "toolCount": len(idx["tools"]),
                       "domains": [{"id": x, "short": short[x]} for x in doms],
                       "spec": f"{SITE}/experience/skills/{s['id']}.md"})

totals = {"apis": len(domain_blocks), "operations": tot_ops, "writeOperations": tot_write,
          "tools": tot_tools, "prompts": len(PROMPTS), "resources": len(RESOURCES), "skills": len(SKILLS)}

# ---------------- data/experience.json (for the single-page doc) ----------------
experience = {
 "generated_from": "openapi/*.yaml + mcp/*.json + manifest across all domains",
 "totals": totals,
 "chain": ["REST operation", "MCP tool", "Agent Skill"],
 "skills": skills_out,
 "prompts": PROMPTS,
 "resources": RESOURCES,
 "apis": [{k: v for k, v in db.items()} for db in domain_blocks],
}
json.dump(experience, open("data/experience.json", "w"), indent=1)

# ---------------- experience/nyc-mcp.json (NYC-wide MCP definition) ----------------
os.makedirs("experience/skills", exist_ok=True)
nyc_mcp = {
 "x-artifact": {"kind": "mcp-server-definition", "designFirst": True, "deployed": False,
   "note": "Design-first NYC-wide MCP surface. Aggregates the 67 per-agency MCP servers behind one contract, adds cross-agency prompts and resources, and exposes the ten common government-process Agent Skills. Not a running server."},
 "server": {"name": "io.nyc.gateway", "title": "NYC — Programmable City (gateway)", "version": "0.1.0",
   "description": "One agent-native surface over all 67 NYC government domains — every REST operation has an MCP tool, every tool maps to one of ten common government-process Agent Skills, plus cross-agency prompts and resources anchored on the nyc-commons geography spine.",
   "instructions": "Start from a resource (nyc://catalog to find the right agency, nyc://commons/geography or nyc://place/{bbl} to anchor a location). Use a prompt for a whole task (who_represents_this_address, how_do_i_apply_for, report_a_problem_at). Each agency's tools live in its own MCP server (see nyc://catalog); this gateway routes and orchestrates them by government process."},
 "capabilities": {"tools": {"listChanged": False}, "prompts": {"listChanged": False}, "resources": {"listChanged": False, "subscribe": False}},
 "x-tool-index": {"count": tot_tools, "note": "624 tools across 67 per-agency MCP servers; see each agency's mcp/*.json (indexed at nyc://catalog).",
   "byAgency": [{"id": db["id"], "server": (json.load(open(glob.glob(f'{db["id"]}/mcp/*.json')[0])).get("server", {}) or {}).get("name", ""), "tools": db["toolCount"]} for db in domain_blocks if db["mcp"]]},
 "prompts": PROMPTS,
 "resources": RESOURCES,
 "x-agent-skills": {"index": f"{SITE}/experience/skills/index.json", "count": len(SKILLS)},
}
json.dump(nyc_mcp, open("experience/nyc-mcp.json", "w"), indent=2)

# ---------------- experience/nyc-openapi.json (unified, x- extensions on every op) ----------------
paths = collections.OrderedDict()
op_map = {}
for db in domain_blocks:
    slug = db["id"].replace(".", "-")
    for o in db["operations"]:
        p = f"/{slug}{o['path']}"
        entry = paths.setdefault(p, {})
        oid = o["operationId"] or f"{slug}_{o['method']}_{re.sub(r'[^a-z0-9]+','_',o['path'].lower())}"
        entry[o["method"]] = {
            "operationId": oid, "summary": o["summary"] or f"{o['method'].upper()} {o['path']}",
            "tags": [db["short"]],
            "responses": {"200": {"description": "OK"}},
            "x-domain": db["id"], "x-mcp-tool": o["mcpTool"], "x-agent-skill": o["skill"],
            "x-source-openapi": db["openapi"],
        }
        op_map[oid] = {"mcpTool": o["mcpTool"], "agentSkill": o["skill"], "domain": db["id"]}
nyc_openapi = {
 "openapi": "3.1.0",
 "info": {"title": "NYC — Programmable City (unified surface)", "version": "0.1.0",
   "summary": f"Every NYC government API in one design-first contract — {tot_ops} operations across {len(domain_blocks)} agencies, each mapped to an MCP tool and a common government-process Agent Skill.",
   "description": "A unified, design-first OpenAPI across all 67 assessed NYC government domains, generated by scripts/build-experience.py from each agency's own OpenAPI. Paths are namespaced by agency slug; every operation carries x-mcp-tool (its MCP tool) and x-agent-skill (one of ten common government-process skills). This is the machine artifact behind the single-page documentation at " + SITE + "/experience.html. Design-first — not a deployed gateway. Full per-operation detail lives in each agency's source OpenAPI (x-source-openapi).",
   "contact": {"name": "API Evangelist — NYC Modernization", "url": "https://github.com/api-evangelist/nyc"}},
 "servers": [{"url": "https://api.nyc.gov", "description": "Illustrative unified gateway host (design-first)."}],
 "x-apis-io": {
   "mcp": {"definition": f"{RAW}/experience/nyc-mcp.json", "note": "NYC-wide MCP gateway (design-first)."},
   "agentSkills": {"index": f"{SITE}/experience/skills/index.json", "count": len(SKILLS)},
   "prompts": PROMPTS,
   "resources": RESOURCES,
   "operations": op_map,
 },
 "paths": paths,
}
json.dump(nyc_openapi, open("experience/nyc-openapi.json", "w"), indent=1)

# ---------------- experience/nyc.apis.json (APIs.json 0.21 descriptor) ----------------
apis_json = {
 "specificationVersion": "0.21",
 "aid": "nyc-programmable-city",
 "name": "NYC — Programmable City",
 "description": f"Every New York City government API, MCP server, and Agent Skill in one place — {totals['apis']} agency APIs, {totals['operations']} operations, {totals['tools']} MCP tools, {totals['prompts']} prompts, {totals['resources']} resources, and {totals['skills']} common government-process skills. Design-first artifacts from the NYC Modernization assessment.",
 "image": f"{SITE}/assets/social.png",
 "url": f"{SITE}/experience/nyc.apis.json",
 "tags": ["NYC", "Government", "API", "MCP", "Agent Skills", "APIs.json", "Programmable City"],
 "apis": [
   {"aid": "nyc:gateway", "name": "NYC — Programmable City (unified)",
    "description": "The unified surface across all 67 agencies — every operation mapped to an MCP tool and a government-process Agent Skill.",
    "humanURL": f"{SITE}/experience.html", "baseURL": "https://api.nyc.gov",
    "tags": ["NYC", "Gateway", "MCP", "Agent Skills"],
    "properties": [
      {"type": "OpenAPI", "url": f"{RAW}/experience/nyc-openapi.json"},
      {"type": "Documentation", "url": f"{SITE}/experience.html"},
      {"type": "MCPServer", "url": f"{RAW}/experience/nyc-mcp.json"},
      {"type": "AgentSkills", "url": f"{SITE}/experience/skills/index.json"},
    ]},
 ] + [
   {"aid": f"nyc:{db['id']}", "name": db["title"], "description": db["summary"],
    "humanURL": f"{SITE}/domain.html?d={db['id']}", "tags": [db["short"], verb.get(db['id'], "")],
    "properties": ([{"type": "OpenAPI", "url": db["openapi"]}] if db["openapi"] else []) +
                  ([{"type": "MCPServer", "url": db["mcp"]}] if db["mcp"] else []) +
                  [{"type": "Documentation", "url": f"{SITE}/domain.html?d={db['id']}"}]}
   for db in domain_blocks],
 "maintainers": [{"FN": "Kin Lane", "email": "info@apievangelist.com"}],
}
json.dump(apis_json, open("experience/nyc.apis.json", "w"), indent=1)

# ---------------- experience/skills/<id>.md + index.json ----------------
skills_index = {"version": "0.1.0", "count": len(SKILLS),
                "description": "The ten common government-process Agent Skills across NYC. Each orchestrates the REST operations and MCP tools of one or more agencies to complete a citizen task.",
                "skills": []}
for s in skills_out:
    body = [f"# {s['name']}\n",
            f"*Common government process — {s['group']} · {s['primitive']}.* Part of the [NYC Programmable City]({SITE}/experience.html) experience layer.\n",
            f"**{s['desc']}**\n",
            "## When to use\n", s["whenToUse"] + "\n",
            "## What it orchestrates\n",
            f"This skill spans **{s['domainCount']} agencies** and **{s['operationCount']} operations** across the corpus. It resolves the right agency for the task, then calls that agency's MCP tools (each backed by a REST operation) to complete it — anchoring any location on the [nyc-commons]({SITE}/commons.html) geography spine.\n",
            "## Agencies\n"]
    body += [f"- [{x['short']}]({SITE}/domain.html?d={x['id']})" for x in s["domains"]] or ["- (none detected)"]
    body += ["\n---", f"*Design-first Agent Skill · [all skills]({SITE}/experience/skills/index.json) · [experience.html]({SITE}/experience.html)*\n"]
    open(f"experience/skills/{s['id']}.md", "w").write("\n".join(body))
    skills_index["skills"].append({"id": s["id"], "name": s["name"], "group": s["group"],
        "primitive": s["primitive"], "description": s["desc"],
        "operationCount": s["operationCount"], "domainCount": s["domainCount"],
        "file": f"{s['id']}.md"})
json.dump(skills_index, open("experience/skills/index.json", "w"), indent=1)

# ---------------- EXPERIENCE.md ----------------
M = [f"# NYC — Programmable City (the experience layer)\n",
 f"*Every NYC government API, MCP server, and Agent Skill in one place — the API → MCP → Agent-Skill chain across all {totals['apis']} agencies.*\n",
 f"Interactive: **[{SITE.split('//')[1]}/experience.html]({SITE}/experience.html)**. Machine artifacts: [unified OpenAPI](experience/nyc-openapi.json) · [NYC-wide MCP](experience/nyc-mcp.json) · [APIs.json descriptor](experience/nyc.apis.json) · [Skills](experience/skills/).\n",
 "## The opportunity in one number set\n",
 f"| Surface | Count |", "|---|---|",
 f"| Agency APIs | {totals['apis']} |",
 f"| REST operations | {totals['operations']} |",
 f"| — of which net-new write operations | {totals['writeOperations']} |",
 f"| MCP tools | {totals['tools']} |",
 f"| MCP prompts (cross-agency) | {totals['prompts']} |",
 f"| MCP resources (cross-agency) | {totals['resources']} |",
 f"| Common government-process skills | {totals['skills']} |", "",
 "Built on the [API Experience](https://experience.apicommons.org) chain — **REST operation → MCP tool → Agent Skill** — minus the free/pro tiering and AI enrichment: a clean view of the whole programmable surface the city could have.\n",
 "## Ten common government processes (Agent Skills)\n",
 "| Skill | Group | Agencies | Operations |", "|---|---|---|---|"]
for s in skills_out:
    M.append(f"| [{s['name']}](experience/skills/{s['id']}.md) | {s['group']} | {s['domainCount']} | {s['operationCount']} |")
M += ["", "## Cross-agency MCP prompts & resources\n",
 "**Prompts** — whole-task entry points: " + ", ".join(f"`{p['name']}`" for p in PROMPTS) + ".\n",
 "**Resources** — shared context: " + ", ".join(f"`{r['uri']}`" for r in RESOURCES) + ".\n",
 "---", f"*Design-first artifacts, not deployments. Part of the [NYC Modernization](README.md) study.*\n"]
open("EXPERIENCE.md", "w").write("\n".join(M))

print(f"experience: {totals}")
print("skills:", [(s['id'], s['operationCount'], s['domainCount']) for s in skills_out])
print("unified openapi paths:", len(paths), "| op_map:", len(op_map))
