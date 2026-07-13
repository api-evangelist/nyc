# Cross-Domain Synthesis

*What five New York City government domains — Parks, Public Schools, the City Council, the Board of Elections, and NYC311 — reveal when you assess them the same way, and what a citywide API modernization would actually take.*

Companion to the fifteen domain assessments (five deep-dive, ten in a follow-on batch). The interactive version, with the maturity scorecard, is at **[nyc.apievangelist.com/synthesis.html](https://nyc.apievangelist.com/synthesis.html)**.

---

## The premise, proven

This project started from a claim: the 2010–2018 open-data era **only partially worked**. Cities published data but never made themselves programmable — the data stayed disconnected from the front door, read-only, unproductized, and (now) not agent-ready.

Five domains, chosen to be different, each confirm the claim in a different way. None is close to programmable. But they fail *differently* — and the differences are the finding.

## Five domains, five verbs

Assessing each domain the same way (crawl → tech/vendor inventory → APIs-observed → Open Data crosswalk → schemas → OpenAPI → MCP) surfaced a one-word **modernization verb** per domain — the dominant shape of its gap:

| Domain | Platform | The gap | Verb |
|---|---|---|---|
| **Parks** (`nycgovparks.org`) | Smarty/PHP (2005-era) | Data-rich, but rendered as HTML on a legacy stack; twins sit unused on Open Data | **Replatform** |
| **Schools / DOE** (`schools.nyc.gov`) | Sitefinity (.NET) | Search rented to a vendor; the real backend hidden behind an internal API | **Reclaim** |
| **Council** (`council.nyc.gov`) | WordPress | Three APIs already exist (Legistar, WP REST, Open Data) — none owned or unified | **Consolidate & Own** |
| **Elections / BOE** (`vote.nyc`) | Drupal 9 | No site API, almost no Open Data; results and candidates are PDFs | **Digitize** |
| **NYC311** (`portal.311.nyc.gov`) | Dynamics 365 | The flagship dataset is the most-used in the city, but the Open311 standard it once ran is retired | **Standardize** |

These five verbs are a **diagnostic taxonomy**. Point the same assessment at a fifth or fiftieth NYC domain and it will land on one (or a blend) of them. That reusability is the point: modernization isn't one monolithic program, it's a repeatable diagnosis plus a repeatable build.

## The batch of ten: the service layer is the gap

A follow-on batch ran the identical method against ten more agencies — **Buildings (DOB), Housing (HPD), Transportation (DOT), Health (DOHMH), Sanitation (DSNY), Police (NYPD), Taxi & Limousine (TLC), City Planning (DCP), the Comptroller, and the Housing Authority (NYCHA)**. Fifteen domains total. Three things sharpened.

**1. The taxonomy expanded — and clustered.** Ten new domains yielded new verbs — **Transact** (DOB, DOHMH), **Expose** (HPD, DSNY, NYPD), **Unify** (DOT), **Operationalize** (TLC), **Consolidate & Own** (Comptroller), **Unlock** (NYCHA), **Anchor** (DCP). But nearly all cluster on one axis: *the data is open; the **service layer** is not.* The gap is rarely the data — it's the transaction.

**2. Many agencies already have an API — it's just private, undocumented, or vendor-locked.** HPD runs a modern versioned REST API behind a WSO2 gateway (private to one Angular app). DSNY runs live pickup/scheduling backends (undocumented). NYPD's live surfaces sit on an Azure Gov backend. The Comptroller's **Checkbook NYC** is a live, keyless public API (XML-envelope, POST-only, no OpenAPI/JSON/MCP). Council depends on Legistar; DCP runs an open-source geocoder behind a gated GeoClient. **The dominant move is Expose, not Build.**

**3. City Planning is the anchor.** DCP defines the BBL and every citywide geography (community districts, NTAs, census tracts, council/election boundaries) — the exact fields that recur in every other domain's `_common.json`. It is the natural authoritative source for the planned [`nyc-commons`](ROADMAP.md) shared spine.

Across all fifteen, the two decisive columns held: **the transactional (write) API is absent in 14 of 15** (only Council scored a 1, and City Planning is a reference agency with no citizen transaction), and **agent-readiness is 0 in all fifteen.** Platform diversity widened to roughly ten distinct stacks with still zero shared API layer. The batch didn't dilute the thesis — it hardened it.

## Cross-cutting findings

What holds *across* all fifteen domains matters more than any single assessment. (The interactive [synthesis](https://nyc.apievangelist.com/synthesis.html) lists the current nine.)

### 1. Five agencies, five platforms, zero shared API layer
Smarty/PHP, Sitefinity/.NET, WordPress, Drupal, Dynamics 365. Every agency picked its own stack, its own CMS, its own vendors — and none exposes a consistent, resource-oriented API. There is no citywide API layer, convention, or contract. Consistency has to be imposed *above* the platforms, not within them.

### 2. The website and the open data are always two worlds
Where Open Data exists (Parks, DOE, Council), the public website renders its **own** parallel HTML and never consumes the machine-readable twin. Two systems, separately maintained, free to drift. The most common defect isn't missing data — it's a **disconnect** between the data and the front door.

### 3. Open Data coverage is wildly uneven — and inversely related to stakes
**237 · 638 · 11 · 2** assets — plus NYC311's flagship dataset (`erm2-nwe9`: 1.26M views), the most-used in the city. The spread is enormous, and it tracks nothing rational. The **Board of Elections** — arguably the highest-stakes civic data in the city — publishes the **least** (2 datasets, poll sites only); election results and candidates are PDFs. Open data adoption was opportunistic, not strategic.

### 4. Every domain has exactly one un-API'd citizen write-workflow
The single most consistent finding. Each domain has one transactional thing a resident actually needs to *do*, and in every case it has **no API**:

| Domain | The action | Net-new object |
|---|---|---|
| Parks | Apply for a permit | `PermitApplication` |
| DOE | Apply to a school | `EnrollmentApplication` |
| Council | Testify at a hearing | `TestimonyRegistration` |
| Elections | Request a mail ballot | `BallotRequest` |
| NYC311 | Submit a 311 request | `ServiceRequest` (Open311, retired) |

Open data liberated *reporting*. It never touched *transactions*. **Five for five**, the citizen-facing verb is locked behind a login-gated form, a siloed app, or a retired standard. This is the universal gap — and the highest-value one.

### 5. Capability outsourcing is pervasive and uncoordinated
HawkSearch (DOE search), Legistar/Granicus (Council legislation), Viebit + StreamText (Council video/captions), CARTO (maps), Cloudinary (Parks images), Microsoft Dynamics 365 (the entire 311 front door), New Relic, Siteimprove, and Socrata itself. Each agency rents different capabilities from different vendors with no shared strategy. Sometimes the vendor *is* the only API (Legistar) — making a vendor the custodian of the city's legislative record.

### 6. Agent-readiness is zero, everywhere
Not one domain exposes an MCP server, a tool manifest, or any agent-native surface. In 2026 this is the gap that compounds: even where an API exists (Council's WP REST, Legistar), no agent can act on the city's behalf. Every MCP artifact in this project is net-new.

### 7. A shared geography spine already recurs in every schema
Writing one `_common.json` per domain surfaced the same fields over and over: **Borough · Community Board · Council District · Census Tract / NTA · BBL / BIN**. Parks facilities, DOE schools, Council funding, and BOE poll sites all carry them. That recurrence is a **latent citywide data model** — a shared spine that already exists implicitly and should be made explicit as a reusable schema set.

### 8. Every domain has its own join key; no cross-domain identity
Parks joins on `gisPropNum`, DOE on `DBN`, Council on `matterId`, Elections on election-district, 311 on `service_request_id`. A resident is the same person across all five, but nothing links them. There is no shared entity for a *place*, an *address*, or a *person* across agencies — so cross-domain questions ("what's near me?", "who represents this school's block?") can't be answered.

## The maturity scorecard

Scoring each domain 0–3 across seven dimensions (see [data/scorecard.json](data/scorecard.json); interactive heatmap for all fifteen at [synthesis.html](https://nyc.apievangelist.com/synthesis.html)) makes the pattern legible. The first six:

| Dimension | Parks | DOE | Council | Elections | 311 |
|---|---|---|---|---|---|
| Platform modernity | 1 | 2 | 2 | 1 | 2 |
| Site / content API | 1 | 1 | 2 | 0 | 1 |
| Open Data breadth | 3 | 3 | 2 | 0 | 3 |
| Core citizen-data machine-readable | 2 | 2 | 3 | 0 | 3 |
| **Transactional (write) API** | **0** | **0** | **1** | **0** | **0** |
| **Agent-readiness** | **0** | **0** | **0** | **0** | **0** |
| Vendor independence | 2 | 1 | 1 | 2 | 1 |

Two columns are effectively all zeros — **transactional API** and **agent-readiness**. Those are the citywide gaps, independent of any agency's platform or open-data maturity. Read the rows and the verbs fall out: Parks is strong on data / weak on delivery (**replatform**); DOE strong on data / weak on ownership (**reclaim**); Council strong on core data / weak on ownership (**consolidate & own**); Elections weak on everything data (**digitize**).

## What this means

Modernizing NYC is **not** one big rebuild. It is:

1. **A repeatable diagnosis** — the five verbs — that classifies any domain's gap in one assessment.
2. **A repeatable build** — schema-per-object → OpenAPI → MCP — that produces the same three contracts every time.
3. **A shared spine** — the geography (and eventually identity) fields every domain already uses — that turns five isolated APIs into an interoperable set.

The five domains aren't five one-off projects. They're five instances of one playbook.

## Recommendations — a NYC API playbook

1. **Publish `nyc-commons` shared schemas.** Promote the recurring `_common` fields (Borough, Community Board, Council District, Census Tract/NTA, BBL/BIN) into a single referenced schema set every agency `$ref`s. Add shared `Address` and `Place` objects to enable cross-domain joins (finding 7 + 8).
2. **Standardize the three-contract chain.** Make "one JSON Schema per object → an OpenAPI that `$ref`s them → an MCP server that maps to the same operations" the default deliverable for every agency. This project is the reference.
3. **Prioritize the write workflows.** The universal gap (finding 4) is also the highest citizen value. A permit, an enrollment, a testimony sign-up, a ballot request — ship these as real read/write APIs first.
4. **Make agent-native the default, not an afterthought.** Every agency API ships with an MCP surface. Agent-readiness is the 2026 table stakes no NYC domain currently meets.
5. **Own the vendor-held records.** Where a vendor API *is* the system of record (Legistar), front it with a city-owned contract so continuity and governance don't depend on a SaaS relationship.
6. **Register everything.** Catalog each agency's schemas, OpenAPI, and MCP in a discoverable index (APIs.json) so the citywide surface is navigable by humans and agents — the connective tissue open data never had.
7. **Connect the data to the front door.** Have the public websites consume their own APIs instead of maintaining parallel HTML (finding 2). One source of truth, many surfaces.

## Coda

"Data liberation" put the city's information on the shelf. It's still on the shelf — disconnected, read-only, and invisible to agents. The five domains here show the same story five different ways, and they show the way out: a repeatable method, a shared spine, and a bias toward the transactions and agent surfaces everyone skipped.

The goal was never more datasets. It's a city you can **program**.

---
*Assessed 2026 · [nyc.apievangelist.com](https://nyc.apievangelist.com) · [api-evangelist/nyc](https://github.com/api-evangelist/nyc). All APIs and MCP servers referenced are design-first artifacts, not deployments.*
