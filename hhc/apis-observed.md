# APIs Observed While Crawling — NYC Health + Hospitals

Backend/service APIs the H+H surfaces call or expose, surfaced during the crawl (2026-07-13). The finding is the opposite of NYCHA's: **H+H's core layer HAS a real, live, standards-based API — Epic FHIR R4 / SMART on FHIR — but it is read-mostly, patient-scoped, and vendor-owned, and there is no OPEN directory and no booking.** Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| **`epicproxypda.nychhc.org/FHIRProxy/api/FHIR/R4`** | FHIR R4 (SMART on FHIR) | H+H on **Epic** | Metadata public; **data SMART-authorized** | The real H+H API. `metadata`: fhirVersion **4.0.1**, software **"Epic November 2025"**, **59 resource types**. `.well-known/smart-configuration`: OAuth2 authorize/token at `/FHIRProxy/oauth2`. `Appointment` = read+search only; **no `Slot`, no `$book`**; `Location` search unauthenticated → **401**. |
| **`mychart.nychhc.org`** | Patient portal (Epic MyChart) | H+H on **Epic** | Login-walled UI; **no open API** | Microsoft-IIS/10.0, `MyChartPersistence` cookie. The human UI over the same Epic system — appointments, messaging, refills, bill pay. Its machine surface is the FHIR endpoint above. |
| `open.epic.com/Endpoints/R4` | Vendor endpoint directory | Epic | **Yes — open** | Epic's public FHIR endpoint directory (480 orgs). Lists "NYC Health + Hospitals" → the FHIRProxy base URL. How the endpoint is discoverable at all. |
| `www.nychealthandhospitals.org` | Informational / directory site | H+H | Public HTML, **bot-walled** | Locations, services, Find a Doctor, help-paying-your-bill. Behind **Radware Bot Manager** (`server: rdwr`, 302 → `validate.perfdrive.com`). No content API; crawl blocked at the edge. |
| `data.cityofnewyork.us` (SODA) | Open Data API | NYC (Socrata) — **DOHMH**, not H+H | Yes | Health datasets here belong to the **Department of Health and Mental Hygiene**. H+H owns **zero** datasets. Adjacent, not owned. |

## Takeaways

- **The standard already exists — that is the story.** H+H is the first domain in this project where the core layer speaks a live, machine-readable **health-data standard (FHIR R4 / SMART on FHIR)**, in production, discoverable through Epic's public directory. The modernization question shifts from "is there an API?" to "why is the API read-mostly, closed-directory, and vendor-owned?"
- **Booking has no contract anywhere.** The single most common patient transaction — requesting/booking a visit — is missing from MyChart's machine surface **and** from the live FHIR endpoint (no `Appointment.create`, no `Slot`, no `$book`). `AppointmentRequest` is genuinely net-new. See [crosswalk.md](crosswalk.md).
- **No open directory.** Facilities, services, providers, and pharmacies are HTML on a bot-walled site or auth-gated FHIR `Location`/`Practitioner` — a patient or agent cannot openly ask "which H+H hospital near me does cardiology and takes new patients?"
- **No Open Data twin.** H+H publishes nothing to NYC Open Data; its data is clinical and lives in Epic. See [opendata-hhc.md](opendata-hhc.md).
- **Everything is Epic (plus Radware).** The API, the portal, and the OAuth surface are all Epic; the site is gated by Radware. The [OpenAPI](openapi/hhc.yaml) + [MCP artifact](mcp/hhc-mcp.json) here propose one owned contract that publishes an open directory cleanly, mirrors the FHIR `Appointment` read, and adds the net-new `request_appointment` write.
