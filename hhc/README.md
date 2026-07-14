# hhc — Low-Hanging Fruit Assessment

Domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of **NYC Health + Hospitals (H+H)** — the city's public hospital system — through the full design-first method: assessment → tech/vendor inventory → APIs-observed → FHIR/Open Data crosswalk → JSON Schemas → OpenAPI → MCP artifact.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (facilities, services, providers, financial assistance, pharmacies, appointments, and the net-new booking write).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (**Epic** MyChart on IIS + the **live Epic FHIR R4 / SMART on FHIR** endpoint; the site behind **Radware Bot Manager**).
- [apis-observed.md](apis-observed.md) — the **one real, live API** (Epic FHIR R4, read-mostly + patient-scoped) vs. the bot-walled site and the absent Open Data.
- [crosswalk.md](crosswalk.md) — fruit ↔ APIs ↔ **FHIR** ↔ Open Data mapping with coverage verdicts.
- [opendata-hhc.md](opendata-hhc.md) / [opendata-hhc.json](opendata-hhc.json) — the Open Data check: **zero** H+H-owned datasets, and why.
- [schemas/](schemas/) — individual JSON Schema per object: `facility` · `service` · `provider` · `financial-assistance` · `pharmacy` · `appointment` · `appointment-request` (+ shared `_common`), FHIR-aligned where natural.
- [openapi/hhc.yaml](openapi/hhc.yaml) — OpenAPI 3.1 contract `$ref`ing each object; ≥1 WRITE path (`POST /appointment-requests`).
- [mcp/hhc-mcp.json](mcp/hhc-mcp.json) — design-first MCP server definition (9 agent tools; artifact, not a deployment).

## What was found — the fifth distinct pattern

H+H is the first domain in this project where **a real, live, standards-based API already exists** — and that is the finding:

1. **The standard is already running.** H+H exposes an **Epic FHIR R4 / SMART on FHIR** endpoint (`epicproxypda.nychhc.org`, "Epic November 2025") with **59 resource types** and an OAuth2 authorize/token surface, discoverable through Epic's public directory. A genuine health-data standard is in production.
2. **But it stops short.** The FHIR surface is **read-mostly and patient-scoped**: `Appointment` is read + search only, there is **no `Slot` and no `$book`**, and `Location`/`Organization`/`Practitioner` are auth-gated (unauthenticated `Location` search → **401**). So there is **no open directory** and **no booking**. The public site is bot-walled (Radware) and H+H publishes **nothing** to NYC Open Data (health data there is DOHMH's).

**The gap here is booking and openness, not the existence of an API.** A New Yorker asking "which H+H hospital near me does cardiology and takes new patients?" or "book me a primary-care visit next week" has nothing to call — even though H+H already speaks FHIR.

**Reframe (vs. the earlier domains):**

| | Parks | DOE | Council | NYCHA | **H+H** |
|---|---|---|---|---|---|
| Platform | Smarty/PHP (legacy) | Sitefinity (.NET) | WordPress | Livesite + Oracle Siebel | **Epic (MyChart + FHIR R4) + Radware** |
| Core problem | data as HTML, no API | search rented, backend hidden | three APIs, none owned | data open, service layer in a CRM | **a real FHIR standard, but read-only, closed-directory, vendor-owned, no booking** |
| Modernization verb | **replatform** | **reclaim** | **consolidate + own** | **unlock** | **extend** |

## Reverse-engineered entities

`Facility` (→ FHIR `Location`/`Organization`) · `Service` (→ `HealthcareService`) · `Provider` (→ `Practitioner`/`PractitionerRole`) · `FinancialAssistance` (NYC Care / sliding-scale) · `Pharmacy` (→ `Location`) · `Appointment` (→ FHIR `Appointment`, read-only) · `AppointmentRequest` (net-new booking write) — aligned to FHIR wherever natural so the design-first API composes with the standard H+H already runs.

## Method & caveats

Outside-in crawl (browser UA). The marketing site could not be spidered — it sits behind a **Radware Bot Manager** that 302-redirects automated clients to a challenge. The **MyChart** portal was fingerprinted as **Epic** from its markup/cookies without authenticating; the **FHIR endpoint** was discovered through Epic's public directory and characterized from its unauthenticated `metadata` and `.well-known/smart-configuration` (data itself is SMART-authorized and was not accessed). The Open Data check is a full Socrata Discovery API query (zero H+H-owned assets). A sample and a standards fingerprint, not a full clinical integration; the proposed schemas/OpenAPI/MCP are a **design-first** proposal, not a live booking into a real EHR.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · FHIR/Open Data crosswalk ✅ · Open Data check (0 datasets) ✅ · JSON Schemas (7 + common) ✅ · OpenAPI 3.1 (13 ops, 1 write) ✅ · MCP artifact (9 tools) ✅.
- **Next:** an example implementation that publishes the open directory and mediates `request_appointment` on top of the live Epic FHIR surface; then the next domain from [../domains.md](../domains.md).
