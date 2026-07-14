# Low-Hanging Fruit Index — NYC Health + Hospitals

**Agency:** NYC Health + Hospitals (H+H)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA). The public site `www.nychealthandhospitals.org` is behind a **Radware Bot Manager** (`server: rdwr`, 302 → `validate.perfdrive.com`), so HTML crawling is blocked at the edge. Fingerprinted the **MyChart** portal (`mychart.nychhc.org` → Microsoft-IIS/10.0, `MyChartPersistence` cookie = **Epic MyChart**) and discovered the **live Epic FHIR R4 / SMART on FHIR API** via Epic's public endpoint directory (`open.epic.com/Endpoints/R4`): base `https://epicproxypda.nychhc.org/FHIRProxy/api/FHIR/R4` — pulled its `metadata` (fhirVersion 4.0.1, "Epic November 2025", **59 resource types**) and `.well-known/smart-configuration`. Verified via the Socrata Discovery API that **no NYC Open Data dataset is owned by H+H** (health data there belongs to DOHMH).

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-hhc.md](opendata-hhc.md).

## Headline findings

1. **A real, live, standards-based API already exists.** H+H runs an **Epic FHIR R4 / SMART on FHIR** endpoint in production — 59 resource types, OAuth2 authorize/token, discoverable through Epic's public directory. This is the first domain in the project where the core layer already speaks a health-data standard.
2. **But it is read-mostly and patient-scoped.** `Appointment` is read + search only; there is **no `Slot` and no `$book`**; `Location`/`Organization`/`Practitioner` require SMART auth (unauthenticated `Location` search → **401**). So the standard exists but stops short of **booking** and of an **open directory**.
3. **No open directory.** "Which H+H hospital near me does cardiology and takes new patients?" has nothing to call — the directory is HTML on a bot-walled site, not open FHIR, not Open Data.
4. **No Open Data, everything is Epic.** H+H publishes **zero** datasets to NYC Open Data (health data there is DOHMH's); the API, portal, and OAuth are all **Epic**, and the site is gated by **Radware**. H+H owns the data, not the contract.

> **Reframe (fifth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; NYCHA = *unlock*; **H+H = extend the standard.** Here a genuine FHIR API is already live — the work is least about inventing an API and most about **extending the standard to booking** and **publishing an open facility/service/provider directory**, instead of leaving New Yorkers a bot-walled site plus a phone number.

## The fruit

| # | Name | Entity | Where the data lives | API today |
|---|---|---|---|---|
| 1 | Find a location / facility | `Facility` | site (bot-walled) + FHIR `Location`/`Organization` | 🟡 auth-gated, no open directory |
| 2 | Service lines & specialties | `Service` | site (bot-walled) | ❌ gap (FHIR `HealthcareService` not exposed) |
| 3 | Find a doctor / provider | `Provider` | site (bot-walled) + FHIR `Practitioner` | 🟡 auth-gated |
| 4 | Financial assistance / NYC Care / sliding-scale | `FinancialAssistance` | site (bot-walled) | ❌ gap |
| 5 | Pharmacy | `Pharmacy` | site (bot-walled) | ❌ gap |
| 6 | My appointments (MyChart) | `Appointment` | MyChart + FHIR `Appointment` | 🟡 read-only (SMART) |
| 7 | **Request / book an appointment** | `AppointmentRequest` | MyChart / 1-844-NYC-4NYC | ❌ **net-new** (no `Appointment.create`, no `Slot`, no `$book`) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Epic FHIR R4 / SMART on FHIR** — `epicproxypda.nychhc.org/FHIRProxy/api/FHIR/R4` (the one real, live, standards-based API; read-mostly, patient-scoped).
- **Epic MyChart** — the patient portal (Microsoft-IIS/10.0); login-walled, no open API.
- **Radware Bot Manager** — gates the public marketing/directory site; blocks automated crawling.
- Platform: **Epic** end to end (a fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's Livesite + Oracle Siebel).

## Reverse-engineered entities

`Facility` (→ FHIR `Location`/`Organization`) · `Service` (→ `HealthcareService`) · `Provider` (→ `Practitioner`/`PractitionerRole`) · `FinancialAssistance` (NYC Care / sliding-scale) · `Pharmacy` (→ `Location`) · `Appointment` (→ FHIR `Appointment`, read-only) · `AppointmentRequest` (net-new write; the booking the FHIR surface doesn't expose) — aligned to FHIR wherever natural so the design-first API composes with the standard H+H already runs.

## Next

1. **JSON Schema** per entity, FHIR-aligned where natural (Facility→Location, Provider→Practitioner, Appointment→Appointment) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing an open directory + mirroring the FHIR `Appointment` read + the net-new `POST /appointment-requests` — done ([openapi/hhc.yaml](openapi/hhc.yaml)).
3. **MCP** artifact: `find_facilities`, `get_facility`, `get_facility_services`, `find_services`, `find_providers`, `find_financial_assistance`, `find_pharmacies`, `list_my_appointments`, `request_appointment` — done ([mcp/hhc-mcp.json](mcp/hhc-mcp.json)).
