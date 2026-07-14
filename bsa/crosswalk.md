# Crosswalk — Website/Records Fruit ↔ APIs ↔ NYC Open Data (BSA)

Maps the low-hanging fruit on **nyc.gov/site/bsa** and its records/intake surfaces to (a) the **existing APIs** (Socrata SODA; the Livesite search widget) and (b) the **4 BSA datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-bsa.json](opendata-bsa.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, resident transactions locked in a vendor CRM → *unlock the service layer.*
- **BSA:** the **case outcomes are open** (4 Socrata datasets + a search widget), but the **intake is paper PDF forms** with no online portal → **digitize the intake.**

BSA is a records-forward agency. It publishes *what it decided* generously — every application filed since 1998 with its type, premises, zoning district, status (Granted / Denied / Withdrawn / Dismissed), and a link to the decision PDF, plus a legacy calendar index back to 1916. What it offers no machine surface for is *doing anything*: filing a variance or appeal is a download-a-PDF-and-file-on-paper process, and even tracking a pending filing, reading a structured resolution, or seeing the hearing calendar has no API.

Coverage: ✅ strong open twin · 🟡 partial / unstructured · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Records | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Application` (case) | resolutions search | SODA | Applications Status (`yvxd-uipr`, 34c); Decisions Map (`99rv-74dm`) | ✅ |
| `ZoningLot` (property) | ZOLA / applications map | SODA | Action Portal legacy index (`f72e-3i4c`, 18c) + premise fields | ✅ |
| `PreApplicationMeeting` | — | SODA | Pre-Application Meetings (`855v-w7mc`, 17c) | ✅ |
| `Resolution` (decision) | decision PDFs | SODA link only | `decisions_url` in `yvxd-uipr` → PDF | 🟡 unstructured (PDF) |
| `Hearing` (calendar) | upcoming-hearing-info page | **HTML/PDF only** | — | ❌ gap (no dataset) |
| **`VarianceApplication`** (file a case) | PDF forms + paper filing | **PDF forms only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (4 datasets)** | Open, machine-readable; strong on case status, disposition, premises, and the legacy index back to 1916 | Outcomes only; a status snapshot; resolutions are just a PDF link; no filing, no hearing calendar |
| **Livesite records search** | Public search over decided cases 1998–present | Server-rendered widget; no JSON/OpenAPI; not agent-accessible |
| **PDF application forms** | The real intake — every case type has a form and checklist | Paper process; no online portal, no API, no way to file or track a filing by machine |

## Implications for the API-first + MCP proposal

1. **Publish the open case data as one clean resource model.** Applications, resolutions, pre-application meetings, and the property/zoning-lot index behind one owned BSA contract ([OpenAPI](openapi/bsa.yaml)) — so consumers learn one model, not 4 Socrata IDs and a search widget.
2. **Structure the decisions.** Model `Resolution` as a resource (status, section, conditions, term, PDF link) instead of leaving the reasoning trapped in a document.
3. **Publish the hearing calendar** — the one core read surface with no dataset today.
4. **Add the one net-new write workflow** — `file_variance_application` (file a variance / special permit / extension / appeal), with the required exhibits and an optional pre-application-meeting reference — replacing the paper PDF-form intake.
5. **MCP server** so an agent can answer "which variances were granted on my block?", "show me this lot's BSA history back to 1916", and — the point — "file my variance and tell me its status."
