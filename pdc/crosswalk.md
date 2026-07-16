# Crosswalk — Website/Process Fruit ↔ APIs ↔ NYC Open Data (PDC)

Maps the low-hanging fruit on **nyc.gov/site/designcommission** and PDC's design-review process to (a) the **existing APIs** (Socrata SODA over 3 datasets) and (b) the **3 PDC datasets** on NYC Open Data. Built 2026-07-16 from [fruit.json](fruit.json) × [opendata-pdc.json](opendata-pdc.json).

## The reframe — a design-review commission whose write is a PDF

- **LPC:** reference data wide open across Socrata *and* Esri ArcGIS, but the permit filing is locked in a Salesforce (Portico) portal with no API → *bind.*
- **DDC:** a vendor-facing agency whose own data is thin/historical and whose transactions all run on citywide systems it doesn't own → *surface.*
- **PDC:** an **agency-facing design-review commission** whose read is decent (3 Socrata datasets, one a 43-column art inventory) but whose **core transaction is not even a system** — a signed PDF application form emailed by a City agency liaison, hard copies delivered to City Hall → **digitize.**

PDC is the design-review analogue of LPC, but a step further back: where LPC at least has a Salesforce portal for filings, PDC's submission is a **PDF + email + paper delivery**. And where LPC serves owners/architects (citizens), PDC serves **only City agencies** — an artist installing a work in a park submits *through* Parks, not directly. So there is no citizen and no citizen transaction. A City agency (or its design consultant) asking "what's on the next agenda for my project, and how do I submit the artwork for conceptual review?" has three read datasets to reconcile and **nothing at all to call for the submission**.

Coverage: ✅ open twin (even if stale) · 🟡 partial/derived · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Process | API today | Open Data | Cov. |
|---|---|---|---|---|
| `DesignProject` | `/design-review` | SODA (snapshots) | Monthly Design Review (`tfrc-rjtr`, 10c); Annual Report (`5fsv-ze7v`, 12c) | ✅ (two views of the review log) |
| `CollectionItem` | `/archive` | SODA | Outdoor Public Art Inventory (`2pg3-gcaa`, 43c) | 🟡 rich but frozen at 2021 |
| `ReviewMeeting` (agenda/minutes) | `/design-review/meetings` | — | — (HTML/PDF only) | ❌ gap (no API) |
| `Commissioner` | `/about` | — | — (HTML only) | ❌ gap (no API) |
| `DesignAward` | `/awards` | — | — (HTML/PDF only) | ❌ gap (no API) |
| **`DesignSubmission`** (submit for review) | `/design-review/application-process` | **PDF form + email only** | — | ❌ **net-new** (B2G; no citizen write exists) |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (3 datasets)** | Open, machine-readable; the review log is kept current (to 2026) and captures the consent-vs-hearing action and the conceptual/preliminary/final level of review; the art inventory is genuinely rich (43 cols, artist/architect credits, material, inscription, Block/Lot, lat/long) | No calendar/agenda/minutes, no commissioners, no awards; the art inventory is frozen at 2021; only *outcomes* are published — nothing about a submission before it is reviewed |
| **Submission process (PDF + email)** | Clear, checklist-driven, category-specific; signed by all involved agencies; lists Community Board / Council District | Not a system at all — no portal, no upload API, no structured record; paper hard copies still required; only City agencies may submit |

## Implications for the API-first + MCP proposal

1. **Surface the whole record.** Present reviewed projects, meeting agendas/minutes, the public-art collection, commissioners, and awards behind one owned PDC contract ([OpenAPI](openapi/pdc.yaml)) — keyed on PROJECT_ID — instead of three Socrata IDs plus HTML/PDF pages.
2. **Digitize the submission.** Expose a PDC-owned write path so an agency liaison can file a structured [`DesignSubmission`](schemas/design-submission.json) — category, requested level of review, lead + secondary agencies, Community Board / Council District, interagency approvals (e.g. LPC), and attachments — instead of emailing a PDF.
3. **Add the one net-new write workflow** — `submit_design_review` (`submitDesignReview`), with `getDesignReviewStatus` to track it through Submitted → Under Review → Calendared for Consent/Hearing → Approved. Be honest: this is **B2G**; there is **no citizen write** in this domain.
4. **Name the gap.** The finding is not missing data so much as a **missing transaction layer**: PDC reviews every permanent design on City-owned property, yet the act of submitting one is a PDF and an email. Digitizing it is the modernization.
5. **MCP server** so an agent can answer "which DPR artworks did PDC approve in Brooklyn last year?", "what's on the next consent calendar?", and — the point — "submit this park sculpture for conceptual review and tell me when it's calendared."
