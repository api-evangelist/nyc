# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (Manhattan DA)

Maps the low-hanging fruit on **manhattanda.org** to (a) the **existing APIs** (the accidental WordPress REST feed; delegated OpenRecords) and (b) **NYC Open Data** — of which there is **none** for this office. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-manhattanda.json](opendata-manhattanda.json) (empty).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, service layer locked in a vendor CRM → *unlock.*
- **Manhattan DA:** a WordPress newsroom whose only API is accidental, **no open data at all**, FOIL delegated, tips un-built — and **four sibling DA offices on the identical stack** → **standardize**: define one shared DA contract, then replicate it.

The Manhattan DA inverts NYCHA. NYCHA's problem was too much open data and a locked service layer; here there is **essentially no structured surface of any kind**. The only machine-readable thing is the newsroom, and only because WordPress ships a REST API. Everything the office does — prosecute, run bureaus and diversion programs, help victims, take tips — exists as HTML pages or prose, never as data. A resident or agent asking "how do I report elder-abuse fraud to the DA?" gets a contact form; asking "how many cases did the office decline last quarter?" gets a press release, not a number.

Coverage: ✅ machine-readable · 🟡 HTML/prose only · ❌ gap (no API, no data).

## Entity crosswalk

| Entity | Website | API today | Open Data | Cov. |
|---|---|---|---|---|
| `PressRelease` | `/category/news/*` | **WP REST** (`wp/v2/posts`, 3,029) | — (none) | ✅ |
| `Program` (bureaus/initiatives) | `/our-work/*` | — (HTML) | — (none) | 🟡 HTML only |
| `VictimService` | `/victim-resources/*` | — (HTML) | — (none) | 🟡 HTML only |
| `Prosecution` (aggregate caseload) | reports as prose | — | — (none) | ❌ gap |
| `Office` (locations) | `/contact-us/` | — (HTML) | — (none) | 🟡 HTML only |
| FOIL records request | `/contact-us/` (FOIL) | **NYC OpenRecords** (delegated, off-site) | — | ❌ delegated |
| **`TipSubmission`** (report to a bureau) | `/contact-us/` (contact form) | **generic CF7 form only** | — | ❌ **net-new** |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **WordPress REST API** | Open, machine-readable; the full newsroom (3,029 posts) as JSON | Accidental (WP default), undocumented, content-only; nothing about cases, programs, or services |
| **NYC OpenRecords** (FOIL) | A real records-request workflow exists | Off-site, citywide, generic; no DA-owned API; the office's statutory intake is invisible from its own domain |
| **Contact Form 7 form** | The only write path on the site | Generic, unstructured, reCAPTCHA-gated; not a tip API, not agent-accessible, no status/tracking |
| **NYC Open Data** | — | **Does not exist for this office.** The DA is an elected county prosecutor outside the mayoral open-data program. |

## Implications for the API-first + MCP proposal

1. **Promote the accidental feed.** Turn `wp/v2/posts` into a clean, documented `PressRelease` resource with real types and topics instead of raw WP post JSON.
2. **Structure the HTML.** Give the office's bureaus/initiatives (`Program`, including diversion and conviction integrity), victim resources (`VictimService`), and locations (`Office`) machine-readable contracts they lack today.
3. **Publish aggregate accountability data.** Offer `Prosecution` statistics (arraignments, dispositions, convictions, declinations, diversions) as data, not prose — aggregate only, never an individual case.
4. **Build the net-new write workflow** — `submit_tip`: a structured, routable tip-intake API to a named bureau, replacing the generic contact form, with an anonymous option.
5. **Stop hiding FOIL.** At minimum, surface the OpenRecords delegation as a first-class, linkable step rather than a paragraph on the Contact page.
6. **Design once, deploy five times.** All five NYC DAs share these functions — ship this as **one shared DA API** ([OpenAPI](openapi/manhattanda.yaml)) with an [MCP artifact](mcp/manhattanda-mcp.json), not five bespoke builds.
