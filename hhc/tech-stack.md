# Technology & Vendor Inventory — NYC Health + Hospitals

What H+H's public surfaces are built on and which third parties they depend on — fingerprinted from response headers, portal markup, and Epic's public FHIR endpoint directory during the crawl (2026-07-13). H+H is a **large public benefit corporation running on a vendor EHR (Epic)**, and the finding is that a **real, live, standards-based API already exists** — it is just read-mostly, patient-scoped, and vendor-owned.

## Three front doors

| Surface | URL | What it does |
|---|---|---|
| Informational / directory site | `www.nychealthandhospitals.org` | Locations, services, Find a Doctor, help-paying-your-bill — content only, **bot-walled** |
| **MyChart patient portal** | **`mychart.nychhc.org/MyChart/`** | The transactional patient layer: appointments, messaging, refills, bill pay — Epic MyChart |
| **Epic FHIR R4 API** | **`epicproxypda.nychhc.org/FHIRProxy/api/FHIR/R4`** | The machine-readable layer — SMART on FHIR, 59 resource types, patient-authorized |

## Informational site (nychealthandhospitals.org)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Bot management / edge | **Radware Bot Manager** | `server: rdwr`; every request 302-redirects to `validate.perfdrive.com/?...ssk=botmanager_support@radware.com`; `__uzma`/`__uzmb`/`uzmx` cookies |
| CMS | Not determinable from outside | The bot wall returns a challenge before any page HTML, so the underlying CMS could not be fingerprinted |

The site is protected aggressively enough that outside-in HTML crawling is blocked at the edge — a governance and accessibility note in itself: the public directory is not reachable by a well-behaved automated client.

## MyChart patient portal — the human transaction layer

| Property | Value | Evidence |
|---|---|---|
| Host | `mychart.nychhc.org` (also `mychart.nychealthandhospitals.org`) | 302 → `./MyChart/` |
| Product | **Epic MyChart** | `MyChartPersistence` + `mychart_persist` cookies |
| Web server | **Microsoft-IIS/10.0** | `server` header |
| Requirement | Login-walled, session-gated | portal login |

## Epic FHIR R4 API — the important part

The real machine-readable surface is **not** on the marketing site. It is a live **SMART on FHIR** endpoint, discoverable through Epic's public directory (`open.epic.com/Endpoints/R4`, which lists "NYC Health + Hospitals"):

| Property | Value | Evidence |
|---|---|---|
| FHIR base | `https://epicproxypda.nychhc.org/FHIRProxy/api/FHIR/R4/` | Epic endpoint directory |
| FHIR version | **4.0.1 (R4)** | `metadata` CapabilityStatement |
| Software | **Epic November 2025** | CapabilityStatement `software` |
| Resource types | **59** | Patient, Condition, Observation, Appointment, Location, Organization, Practitioner, PractitionerRole, MedicationRequest, DocumentReference, DiagnosticReport, Immunization, Coverage, ... |
| Auth | **SMART on FHIR / OAuth2** | `.well-known/smart-configuration`: `authorization_endpoint` + `token_endpoint` at `/FHIRProxy/oauth2`; capabilities include `launch-standalone`, `client-confidential-asymmetric`, `context-ehr-patient` |
| Access shape | Patient-scoped, read-mostly | unauthenticated `Location?_count=3` → **HTTP 401**; `Appointment` interactions = `read`, `search-type` only |

### The asymmetry that defines this domain

The standard is real and live, but it stops short in exactly the place that matters:

- **`Appointment`** — `read` + `search-type` only. **No `create`.**
- **No `Slot`** resource is exposed at all.
- **No `$book` / `$find`** scheduling operation.
- **`Patient`** supports `create` (+ `$match`, `$summary`), but the everyday transaction — **booking a visit** — has no contract.
- **`Location` / `Organization` / `Practitioner`** exist (read + search) but are **auth-gated**, so there is no *open* facility/provider directory.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in a vendor CRM → *unlock*.
- **H+H** = a **real health-data standard (Epic FHIR R4 / SMART on FHIR) is already running**, but it is read-mostly, patient-scoped, vendor-owned, with **no open directory and no booking** → **extend** the standard to booking + publish an open directory.

## Modernization implications

1. **Don't invent an API — extend the one that exists.** H+H already speaks FHIR. The gap is (a) an **open directory** (facilities, services, providers, pharmacies, financial assistance) that FHIR keeps behind auth and the site keeps behind a bot wall, and (b) a **booking write surface** the FHIR endpoint doesn't expose.
2. **Booking is the net-new write.** `AppointmentRequest` (report intent to be seen) is the single most common patient transaction and has no machine-readable contract anywhere today — not in MyChart's API, not in the live FHIR surface. See [OpenAPI](openapi/hhc.yaml).
3. **Vendor concentration is the governance risk.** The API, the portal, and the OAuth surface are all Epic; the public site is gated by Radware. H+H owns the data but not the contract. An owned, agent-native surface ([MCP artifact](mcp/hhc-mcp.json)) in front of it is the low-hanging fruit.
