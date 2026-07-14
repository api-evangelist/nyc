# Low-Hanging Fruit Index — EDC

**Agency:** New York City Economic Development Corporation (EDC)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt). `edc.nyc` and `nycedc.com` both sit behind a **Cloudflare bot challenge** (HTTP 403 `cf-mitigated: challenge`), so the HTML is not directly fetchable; the site is fingerprinted as **Drupal** from `robots.txt` (`/core/`, `/profiles/`) and Cloudflare from headers. NYC Ferry's `ferry.nyc` resolves via Cloudflare + CloudFront. Verified the NYC Open Data agency label `Economic Development Corporation (EDC)` via the Socrata Discovery API — it returns only **5** assets, all pulled with column schemas. EDC's core entities (projects, real estate, solicitations) are **modeled** from how the site presents them; EDC publishes none of them to Open Data.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-edc.md](opendata-edc.md).

## Headline findings

1. **EDC is a public benefit corporation, not a mayoral agency** — and its data footprint reflects that. Only **5 NYC Open Data assets** carry the `Economic Development Corporation (EDC)` label, and they are peripheral: a marketing company map, NYC Ferry ridership, and three WiredNYC broadband tables.
2. **EDC's actual business is invisible to machines.** Its **~60M sq ft real-estate portfolio**, its development/capital projects, and its solicitations (RFPs/RFEIs) — the core of what EDC does — have **no Open Data twin and no API**; they exist only as Drupal pages on edc.nyc.
3. **The site itself is bot-walled.** edc.nyc and nycedc.com return **403 with a Cloudflare challenge** to non-browser clients, so even the project/asset/RFP listings can't be reliably scraped — let alone consumed by a partner or agent.
4. **The one operational open dataset is NYC Ferry Ridership** (`t5n6-gx8c`); the rest are a promotional "Mapped In NY" company map and the WiredNYC broadband-certification program.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a vendor CRM; **EDC = surface the portfolio.** Here the problem is least about liberating datasets or unlocking transactions and most about the fact that EDC's **core business is not published in machine-readable form at all** — the work is to give its real estate, projects, and solicitations an owned, agent-native API.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Development Projects | `DevelopmentProject` | edc.nyc (Drupal) | ❌ gap (no API/data) |
| 2 | EDC-Managed Real Estate | `PropertyAsset` | edc.nyc (Drupal) | ❌ gap (no API/data) |
| 3 | Solicitations (RFP/RFEI/RFQ/RFI) | `Solicitation` | edc.nyc (Drupal) | ❌ gap (no API/data) |
| 4 | Mapped In NY Companies | `MappedCompany` | SODA | ✅ Mapped In NY (`f4yq-wry5`, 19c) |
| 5 | NYC Ferry Ridership | `FerryRidership` | SODA | ✅ NYC Ferry Ridership (`t5n6-gx8c`, 7c) |
| 6 | WiredNYC Broadband Buildings | `WiredBuilding` | SODA (×3) | 🟡 WiredNYC (`a6nj-cfbz` + certified/participating) |
| 7 | **Respond to a solicitation** | `RFPResponse` | edc.nyc + email | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 5 EDC datasets (the only open API; all peripheral to the mission).
- **Drupal on Cloudflare** — edc.nyc / nycedc.com; bot-challenged, 403 to non-browser clients, no API.
- **NYC Ferry (ferry.nyc)** — Cloudflare + CloudFront; operated via contractor; ridership on Open Data.
- Platform: **Drupal behind Cloudflare** — the fifth distinct platform after Parks' Smarty/PHP, DOE's Sitefinity/.NET, Council's WordPress, and NYCHA's NYC.gov Livesite + Oracle Siebel.

## Reverse-engineered entities

`DevelopmentProject` · `PropertyAsset` (EDC-managed real estate) · `Solicitation` (RFP/RFEI/RFQ/RFI) · `MappedCompany` · `FerryRidership` · `WiredBuilding` · `RFPResponse` (net-new write) — join keys: **BBL**, **BIN**, neighborhood, and the NYC geography spine (borough, community board, council district).

## Next

1. **JSON Schema** per entity — reconciling the real Open Data column names (Mapped In NY, ferry ridership, WiredNYC) and modeling the unpublished core (projects, assets, solicitations) — done ([schemas/](schemas/)).
2. **OpenAPI** surfacing the modeled portfolio + real open datasets as clean resources, plus the net-new `POST /rfp-responses` (respond to a solicitation) — done ([openapi/edc.yaml](openapi/edc.yaml)).
3. **MCP** artifact: `find_projects`, `get_project`, `find_properties`, `get_property`, `find_solicitations`, `get_solicitation`, `find_mapped_companies`, `find_ferry_ridership`, `find_wired_buildings`, `list_my_rfp_responses`, `submit_rfp_response` — done ([mcp/edc-mcp.json](mcp/edc-mcp.json)).
