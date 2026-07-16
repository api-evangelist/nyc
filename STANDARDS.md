# Standards

Two views of standards in the NYC modernization assessment. Interactive: [standards.html](https://nyc.apievangelist.com/standards.html).

## A. Standards NYC agencies should conform to

Sector standards already exist for most of what NYC builds bespoke — and adoption is nearly zero. The city keeps declining the standards made for exactly its problems.

| Standard | Category | Applies to | Adopted (≥ partial-live) |
|--|--|--|--|
| [Open311 (GeoReport v2)](https://www.open311.org/) | Service requests | 11 domains | 0 |
| [HL7 FHIR / SMART on FHIR](https://hl7.org/fhir/) | Health | 2 domains | 1 |
| [OpenReferral / HSDS](https://openreferral.org/) | Human services | 9 domains | 0 |
| [Open Contracting (OCDS)](https://standard.open-contracting.org/) | Procurement / spending | 6 domains | 0 |
| [GTFS / GTFS-realtime](https://gtfs.org/) | Transit / mobility | 3 domains | 0 |
| [iCalendar (RFC 5545)](https://icalendar.org/) | Calendars / events | 8 domains | 0 |
| [Popolo / Open Civic Data](https://www.popoloproject.com/) | Legislative / people | 12 domains | 0 |

### Open311 (GeoReport v2)
An open API standard for submitting and tracking non-emergency service requests / complaints. **Why it matters:** The exact shape of a 311-style report. NYC pioneered it, then let it lapse — reviving it standardizes every complaint/inspection intake across agencies.

Applicable: NYC311, NYC Sanitation (DSNY), NYC Transportation (DOT), NYC Housing (HPD), NYC Environmental Protection (DEP), NYC Buildings (DOB), NYPD, NYC Civilian Complaint Review (CCRB), NYC Health (DOHMH), NYC Human Rights (CCHR), NYC Investigation (DOI)

### HL7 FHIR / SMART on FHIR
The healthcare interoperability standard for clinical and administrative resources (Patient, Appointment, Location…). **Why it matters:** H+H already runs a live FHIR endpoint; extending it (booking, an open facility directory) is standards-native modernization, not a bespoke build.

Applicable: NYC Health + Hospitals ✓, NYC Health (DOHMH)

### OpenReferral / HSDS
The Human Services Data Specification — a standard for directories of community services, programs, and eligibility. **Why it matters:** Every human-services agency publishes a bespoke provider directory; HSDS would make them queryable and interoperable (and feed 211/ACCESS NYC).

Applicable: NYC Aging (DFTA), NYC Youth & Community Dev (DYCD), NYC Veterans' Services (DVS), NYC Social Services (HRA), NYC Homeless Services (DHS), NYC Children's Services (ACS), NYC Small Business Services (SBS), NYC Criminal Justice (MOCJ), NYC Cultural Affairs (DCLA)

### Open Contracting (OCDS)
The Open Contracting Data Standard for planning, tender, award, contract, and spending records. **Why it matters:** Checkbook NYC is a custom XML feed; procurement is scattered across PASSPort, City Record, and agency portals. OCDS would unify the money.

Applicable: NYC Comptroller, NYC Design & Construction (DDC), NYC School Construction Authority (SCA), NYC Citywide Admin Services (DCAS), NYC Finance (DOF), NYC Business Integrity Commission (BIC)

### GTFS / GTFS-realtime
The General Transit Feed Specification for schedules, stops, and real-time vehicle positions. **Why it matters:** NYC Ferry and DOT mobility services could publish GTFS so trip-planners and agents consume them natively.

Applicable: NYC Transportation (DOT), NYC Economic Development (EDC), NYC Taxi & Limousine (TLC)

### iCalendar (RFC 5545)
The interoperable calendar standard for events and schedules. **Why it matters:** School calendars, park events, council hearings, and library programs are HTML today; iCalendar makes them subscribable and agent-readable.

Applicable: NYC Public Schools (DOE), NYC Parks & Recreation, NYC Council, New York Public Library (NYPL), Brooklyn Public Library (BPL), Queens Public Library (QPL), NYC Cultural Affairs (DCLA), NYC Emergency Management (NYCEM)

### Popolo / Open Civic Data
A standard for legislatures, people, organizations, memberships, and votes. **Why it matters:** Council runs Legistar (structured but vendor); the borough presidents and DAs model people/offices ad hoc. Popolo standardizes who-represents-whom.

Applicable: NYC Council, Manhattan Borough President, Brooklyn Borough President, Queens Borough President, Bronx Borough President, Staten Island Borough President, Manhattan District Attorney, Brooklyn District Attorney, Bronx District Attorney, Queens District Attorney, Staten Island District Attorney, NYC Public Advocate

## B. The standards this project is built on

The modernization itself is defined by a small stack of open standards — the design-first chain.

### JSON Schema (2020-12) — Object contract (439 in this project)
A vocabulary for describing and validating the shape of a JSON object. **Why it matters:** The atom of the whole design — one canonical, machine-validatable schema per entity (Park, Permit, School…). `$ref` lets schemas reuse shared definitions, which is exactly what makes a citywide `nyc-commons` possible.

### OpenAPI 3.1 — API contract (752 in this project)
A standard, language-agnostic description of a REST API — its paths, operations, and the schemas they read and write. **Why it matters:** Turns a pile of schemas into a described, resource-oriented API. It `$ref`s the JSON Schemas and drives docs, mocks, SDKs, and validation — the lingua franca every API tool speaks.

### Model Context Protocol (MCP) — Agent contract (653 in this project)
An open protocol for exposing tools and resources to AI agents/assistants. **Why it matters:** The agent-native layer. It maps the same resources as callable tools, mapped 1:1 to the OpenAPI operations — making a government service usable by an AI agent, not just a browser. Zero of 70 domains have this today.

### Agent Skills — Agent task contract (10 in this project)
Portable, model-agnostic skill definitions that package a task's instructions, the resources it needs, and the tools it orchestrates for an AI agent. **Why it matters:** The layer above MCP tools: one skill per common government process (apply, report, request records, schedule, pay…) that resolves the right agency and drives its tools to finish a citizen task. Ten are defined across the 70 agencies — see the Programmable City experience layer.

### Arazzo 1.0 — Workflow contract (1 in this project)
The OpenAPI Initiative's standard for describing a sequence of API calls across one or more APIs — a portable, versionable, testable description of a multi-step process. **Why it matters:** The cross-agency layer: a single government outcome (build affordable housing, open a business) rarely lives in one agency. Arazzo chains the per-agency OpenAPI operations into one machine-readable journey — the connective tissue for automating approval management across agencies, as an open standard rather than another siloed portal.

### APIs.json — Discovery / registry
A machine-readable index that catalogs an organization's APIs and their supporting artifacts (schemas, OpenAPI, docs). **Why it matters:** The connective tissue open data never had — a discoverable registry so humans and agents can find every agency's API. The planned citywide index (see roadmap).

### Socrata SODA / SoQL — Existing data source (2,681 in this project)
The query API + query language behind NYC Open Data (data.cityofnewyork.us). **Why it matters:** The existing citywide data layer (run by OTI) that this project crosswalks every domain against — the 2,681 assets we mapped and the read-side many proposed APIs would wrap.

