#!/usr/bin/env python3
"""Standards analysis — two dimensions:
  A. domainStandards — the open/industry data standards each NYC domain SHOULD conform to,
     and its current conformance (0 none / 1 aware-or-partial / 2 partial-live / 3 adopted).
  B. projectStandards — the standards THIS project is built on (what they are, why they matter).
Writes data/standards.json + STANDARDS.md + feeds standards.html. From repo root."""
import json, glob, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
DOM = json.load(open("data/manifest.json"))["domains"]
short = {d["id"]: d["short"] for d in DOM}
apitext = {}
for d in DOM:
    fr = json.load(open(f"{d['id']}/fruit.json"))
    apitext[d["id"]] = " ".join(f"{a.get('endpoint','')} {a.get('type','')} {a.get('note','')}"
                                for a in fr.get("apis_observed", [])).lower()

# project-wide totals (derived from the manifest so the B-section counts never drift)
N = len(DOM)
T = {k: sum(d["counts"].get(k, 0) for d in DOM) for k in ("opendata", "schemas", "openapiOps", "mcpTools")}
ARAZZO = len(glob.glob("experience/workflows/*.arazzo.yaml"))
OVERLAYS = len(glob.glob("experience/overlays/**/*.overlay.yaml", recursive=True))

# ---- A. domain-facing standards: applicability (curated) + conformance detection ----
STD = [
 {"name": "Open311 (GeoReport v2)", "spec": "https://www.open311.org/", "cat": "Service requests",
  "what": "An open API standard for submitting and tracking non-emergency service requests / complaints.",
  "why": "The exact shape of a 311-style report. NYC pioneered it, then let it lapse — reviving it standardizes every complaint/inspection intake across agencies.",
  "applies": ["nyc311","dsny","dot","hpd","dep","dob","nypd","ccrb","dohmh","cchr","doi"],
  "conf": lambda d: 1 if d == "nyc311" else (2 if "open311" in apitext[d] else 0)},  # 311 ran it, now retired
 {"name": "HL7 FHIR / SMART on FHIR", "spec": "https://hl7.org/fhir/", "cat": "Health",
  "what": "The healthcare interoperability standard for clinical and administrative resources (Patient, Appointment, Location…).",
  "why": "H+H already runs a live FHIR endpoint; extending it (booking, an open facility directory) is standards-native modernization, not a bespoke build.",
  "applies": ["hhc","dohmh"],
  "conf": lambda d: 2 if "fhir" in apitext[d] else 0},
 {"name": "OpenReferral / HSDS", "spec": "https://openreferral.org/", "cat": "Human services",
  "what": "The Human Services Data Specification — a standard for directories of community services, programs, and eligibility.",
  "why": "Every human-services agency publishes a bespoke provider directory; HSDS would make them queryable and interoperable (and feed 211/ACCESS NYC).",
  "applies": ["dfta","dycd","dvs","hra","dhs","acs","sbs","mocj","dcla"],
  "conf": lambda d: 0},
 {"name": "Open Contracting (OCDS)", "spec": "https://standard.open-contracting.org/", "cat": "Procurement / spending",
  "what": "The Open Contracting Data Standard for planning, tender, award, contract, and spending records.",
  "why": "Checkbook NYC is a custom XML feed; procurement is scattered across PASSPort, City Record, and agency portals. OCDS would unify the money.",
  "applies": ["comptroller.nyc.gov","ddc","sca","dcas","dof","bic"],
  "conf": lambda d: 0},
 {"name": "GTFS / GTFS-realtime", "spec": "https://gtfs.org/", "cat": "Transit / mobility",
  "what": "The General Transit Feed Specification for schedules, stops, and real-time vehicle positions.",
  "why": "NYC Ferry and DOT mobility services could publish GTFS so trip-planners and agents consume them natively.",
  "applies": ["dot","edc","tlc"],
  "conf": lambda d: 1 if "gtfs" in apitext[d] else 0},
 {"name": "iCalendar (RFC 5545)", "spec": "https://icalendar.org/", "cat": "Calendars / events",
  "what": "The interoperable calendar standard for events and schedules.",
  "why": "School calendars, park events, council hearings, and library programs are HTML today; iCalendar makes them subscribable and agent-readable.",
  "applies": ["schools.nyc.gov","nycgovparks.org","council.nyc.gov","nypl","bklynlibrary","queenslibrary","dcla","nycem"],
  "conf": lambda d: 0},
 {"name": "Popolo / Open Civic Data", "spec": "https://www.popoloproject.com/", "cat": "Legislative / people",
  "what": "A standard for legislatures, people, organizations, memberships, and votes.",
  "why": "Council runs Legistar (structured but vendor); the borough presidents and DAs model people/offices ad hoc. Popolo standardizes who-represents-whom.",
  "applies": ["council.nyc.gov","manhattanbp","brooklynbp","queensbp","bronxbp","statenislandbp",
              "manhattanda","brooklynda","bronxda","queensda","statenislandda","pubadvocate"],
  "conf": lambda d: 1 if d == "council.nyc.gov" else 0},
]
domainStandards = []
for s in STD:
    doms = []
    for d in s["applies"]:
        c = s["conf"](d)
        doms.append({"id": d, "short": short.get(d, d), "conformance": c})
    adopted = sum(1 for x in doms if x["conformance"] >= 2)
    domainStandards.append({"name": s["name"], "spec": s["spec"], "category": s["cat"],
                            "what": s["what"], "why": s["why"], "applicableCount": len(doms),
                            "adoptedCount": adopted, "domains": doms})

# ---- B. the standards THIS project is built on ----
projectStandards = [
 {"name": "JSON Schema (2020-12)", "spec": "https://json-schema.org/", "role": "Object contract",
  "what": "A vocabulary for describing and validating the shape of a JSON object.",
  "why": "The atom of the whole design — one canonical, machine-validatable schema per entity (Park, Permit, School…). `$ref` lets schemas reuse shared definitions, which is exactly what makes a citywide `nyc-commons` possible.", "count": T["schemas"]},
 {"name": "OpenAPI 3.1", "spec": "https://www.openapis.org/", "role": "API contract",
  "what": "A standard, language-agnostic description of a REST API — its paths, operations, and the schemas they read and write.",
  "why": "Turns a pile of schemas into a described, resource-oriented API. It `$ref`s the JSON Schemas and drives docs, mocks, SDKs, and validation — the lingua franca every API tool speaks.", "count": T["openapiOps"]},
 {"name": "OpenAPI Overlays", "spec": "https://spec.openapis.org/overlay/latest.html", "role": "Interface transformation / localization",
  "what": "A separate document of targeted updates (JSONPath actions) applied to a base OpenAPI description, without forking or editing the base.",
  "why": f"The transformation layer. One base contract + N thin overlays = N variants — used here to localize the INTERFACE (titles, summaries, descriptions) into the ten citywide languages of NYC Local Law 30, never touching paths, operationIds, schema fields, or data. Because MCP tools derive 1:1 from OpenAPI operations, the same overlay yields a localized MCP server. {OVERLAYS} language overlays for the HPD worked example — see experience/overlays.", "count": OVERLAYS},
 {"name": "Model Context Protocol (MCP)", "spec": "https://modelcontextprotocol.io/", "role": "Agent contract",
  "what": "An open protocol for exposing tools and resources to AI agents/assistants.",
  "why": f"The agent-native layer. It maps the same resources as callable tools, mapped 1:1 to the OpenAPI operations — making a government service usable by an AI agent, not just a browser. Zero of {N} domains have this today.", "count": T["mcpTools"]},
 {"name": "Agent Skills", "spec": "https://code.claude.com/docs/en/skills", "role": "Agent task contract",
  "what": "Portable, model-agnostic skill definitions that package a task's instructions, the resources it needs, and the tools it orchestrates for an AI agent.",
  "why": f"The layer above MCP tools: one skill per common government process (apply, report, request records, schedule, pay…) that resolves the right agency and drives its tools to finish a citizen task. Ten are defined across the {N} agencies — see the Programmable City experience layer.", "count": 10},
 {"name": "Arazzo 1.0", "spec": "https://spec.openapis.org/arazzo/latest.html", "role": "Workflow contract",
  "what": "The OpenAPI Initiative's standard for describing a sequence of API calls across one or more APIs — a portable, versionable, testable description of a multi-step process.",
  "why": "The cross-agency layer: a single government outcome (build affordable housing, open a business) rarely lives in one agency. Arazzo chains the per-agency OpenAPI operations into one machine-readable journey — the connective tissue for automating approval management across agencies, as an open standard rather than another siloed portal.", "count": ARAZZO},
 {"name": "APIs.json", "spec": "https://apisjson.org/", "role": "Discovery / registry",
  "what": "A machine-readable index that catalogs an organization's APIs and their supporting artifacts (schemas, OpenAPI, docs).",
  "why": "The connective tissue open data never had — a discoverable registry so humans and agents can find every agency's API. The planned citywide index (see roadmap).", "count": None},
 {"name": "Socrata SODA / SoQL", "spec": "https://dev.socrata.com/", "role": "Existing data source",
  "what": "The query API + query language behind NYC Open Data (data.cityofnewyork.us).",
  "why": f"The existing citywide data layer (run by OTI) that this project crosswalks every domain against — the {T['opendata']:,} assets we mapped and the read-side many proposed APIs would wrap.", "count": T["opendata"]},
]

out = {"note": "Two dimensions: (A) the open/industry data standards NYC domains should conform to (and their current, mostly-zero adoption); (B) the standards this project itself is built on.",
       "domainStandards": domainStandards, "projectStandards": projectStandards}
json.dump(out, open("data/standards.json", "w"), indent=1)

L = ["# Standards\n",
     "Two views of standards in the NYC modernization assessment. Interactive: [standards.html](https://nyc.apievangelist.com/standards.html).\n",
     "## A. Standards NYC agencies should conform to\n",
     "Sector standards already exist for most of what NYC builds bespoke — and adoption is nearly zero. The city keeps declining the standards made for exactly its problems.\n",
     "| Standard | Category | Applies to | Adopted (≥ partial-live) |", "|--|--|--|--|"]
for s in domainStandards:
    L.append(f"| [{s['name']}]({s['spec']}) | {s['category']} | {s['applicableCount']} domains | {s['adoptedCount']} |")
L.append("")
for s in domainStandards:
    L.append(f"### {s['name']}\n{s['what']} **Why it matters:** {s['why']}\n")
    L.append("Applicable: " + ", ".join(f"{x['short']}" + (" ✓" if x["conformance"] >= 2 else "") for x in s["domains"]) + "\n")
L.append("## B. The standards this project is built on\n")
L.append("The modernization itself is defined by a small stack of open standards — the design-first chain.\n")
for p in projectStandards:
    cnt = f" ({p['count']:,} in this project)" if p.get("count") else ""
    L.append(f"### {p['name']} — {p['role']}{cnt}\n{p['what']} **Why it matters:** {p['why']}\n")
open("STANDARDS.md", "w").write("\n".join(L) + "\n")
print("standards A:", [(s["name"], s["applicableCount"], s["adoptedCount"]) for s in domainStandards])
print("standards B:", [p["name"] for p in projectStandards])
