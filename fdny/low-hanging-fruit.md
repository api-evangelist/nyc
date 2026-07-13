# Low-Hanging Fruit Index — FDNY

**Agency:** Fire Department of the City of New York (FDNY)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/fdny` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace) and the **FDNY Business** portal at `fires.fdnycloud.org/CitizenAccess`, identified as an **Accela Civic Platform** (Citizen Access) application (`.aspx`, `*.accela.com`/`*.civicplatform` CSP allow-list, Datadog RUM) fronted by Cloudflare + an Azure Application Gateway. Verified the NYC Open Data agency label `Fire Department of New York City (FDNY)` via the Socrata Discovery API and pulled all **17** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-fdny.md](opendata-fdny.md).

## Headline findings

1. **FDNY is a split domain.** An informational site on the shared NYC.gov chassis, and a business **permitting portal running on a rented Accela Civic Platform** (`fires.fdnycloud.org`) with **no API**.
2. **The reference and incident data is unusually open.** **17 NYC Open Data datasets** cover firehouses, minute-level **Fire and EMS incident dispatch**, Bureau of Fire Prevention inspections, active violation orders, certificates of fitness, building vacate lists, and fire-cause investigations.
3. **But the business layer is rented and locked.** Applying for a permit, holding a Certificate of Fitness/Operation, scheduling an inspection, and answering a violation — the things businesses actually *do* — live only inside the login-walled, JavaScript-only Accela portal or on paper. None has a machine-readable contract.
4. **The open data is a rear-view mirror.** Inspections, violations, certificates, and building summaries are all published as **historical snapshots**; the live regulatory state lives inside Accela.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* an in-house vendor CRM; **FDNY = front the rented SaaS.** Here the data is already open — the work is least about liberating datasets and most about giving the **business transaction layer** (above all, applying for a fire permit) an owned, agent-native API instead of a rented Accela screen.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Firehouse Listing | `Firehouse` | SODA + map | ✅ FDNY Firehouse Listing (`hc8x-tcnd`, 12c) |
| 2 | Fire & EMS Incident Dispatch | `IncidentDispatch` | SODA (×2) | ✅ Fire (`8m42-w767`) + EMS (`76xm-jjuj`) dispatch |
| 3 | Bureau of Fire Prevention Inspections | `Inspection` | SODA (×3) | 🟡 BFP (`ssq6-fkht`) + RBIS (`itd7-gx3g`) — historical |
| 4 | Active Violation Orders | `Violation` | SODA | 🟡 Active Violation Orders (`bi53-yph3`) — historical |
| 5 | Certificates of Fitness | `CertificateOfFitness` | SODA | 🟡 Certificates of Fitness (`pdiy-9ae5`) — historical |
| 6 | Apply for a fire permit | `FirePermitApplication` | FDNY Business (Accela) | ❌ **net-new** |
| 7 | Hold / renew a Certificate of Fitness | `FirePermitApplication` | FDNY Business (Accela) | ❌ gap (no API) |
| 8 | Schedule an inspection | `FirePermitApplication` | FDNY Business (Accela) | ❌ gap (no API) |
| 9 | Answer a violation | `FirePermitApplication` | FDNY Business (Accela) | ❌ gap (no API) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 17 FDNY datasets (the one real, open API; reference/operational data only).
- **Accela Civic Platform** — the FDNY Business portal; login-walled, JavaScript-only, rented SaaS, no API. Fronted by Cloudflare + Azure Application Gateway, monitored by Datadog.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as Parks/DOE/Council/NYCHA.

## Reverse-engineered entities

`Firehouse` · `IncidentDispatch` (Fire + EMS) · `Inspection` (BFP / RBIS / mandatory) · `Violation` · `CertificateOfFitness` · `FirePermitApplication` (net-new write; also stands in for the Accela-locked C of F / inspection / violation-response transactions) — join keys: **BIN**, **BBL**, FDNY premises account **ACCT_NUM/ACCT_ID**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (BIN/BBL, ACCT_NUM, the geography spine, Fire vs EMS dispatch fields) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open reference/operational data as clean resources + the net-new `POST /permit-applications` (apply for a fire permit) — done ([openapi/fdny.yaml](openapi/fdny.yaml)).
3. **MCP** artifact: `find_firehouses`, `get_firehouse`, `find_incidents`, `get_incident`, `find_inspections`, `find_violations`, `find_certificates_of_fitness`, `list_my_permit_applications`, `apply_for_permit`, `get_permit_application` — done ([mcp/fdny-mcp.json](mcp/fdny-mcp.json)).
