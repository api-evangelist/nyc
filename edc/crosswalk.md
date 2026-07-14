# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (EDC)

Maps the low-hanging fruit on **edc.nyc / nycedc.com** and **ferry.nyc** to (a) the **existing APIs** (Socrata SODA; there is no EDC API) and (b) the **5 EDC datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-edc.json](opendata-edc.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every transaction locked in a vendor CRM → *unlock the service layer.*
- **EDC:** a **public benefit corporation** whose **core business is not published at all** — only peripheral programs reach Open Data, and the site itself is bot-walled → **surface the portfolio.**

EDC inverts NYCHA. NYCHA's problem was that the *data* was open but the *transactions* were locked. EDC's problem is that its **core data barely exists in machine-readable form**: the real estate portfolio, the development projects, and the solicitations that *are* EDC live only as Drupal pages behind a Cloudflare challenge. What EDC does publish — a marketing company map, ferry ridership, WiredNYC broadband tables — sits off to the side of the mission. A partner or agent asking "what is EDC soliciting right now?" or "what EDC property is available in Sunset Park?" has nothing to call and nothing to even scrape.

Coverage: ✅ strong open twin · 🟡 partial/peripheral · ❌ gap (no API, no Open Data).

## Entity crosswalk

| Entity | Website | API today | Open Data | Cov. |
|---|---|---|---|---|
| `DevelopmentProject` | `/projects` | **none** | — | ❌ gap |
| `PropertyAsset` | `/work-with-us/real-estate` | **none** | — | ❌ gap |
| `Solicitation` (RFP/RFEI) | `/rfps` | **none** | — | ❌ gap |
| `MappedCompany` | Mapped In NY | SODA | Mapped In NY Companies (`f4yq-wry5`, 19c) | ✅ |
| `FerryRidership` | ferry.nyc | SODA | NYC Ferry Ridership (`t5n6-gx8c`, 7c) | ✅ |
| `WiredBuilding` | WiredNYC | SODA | WiredNYC All/Certified/Participating (`a6nj-cfbz`, `37it-gmcp`, `cfzn-4iza`) | 🟡 niche program |
| **`RFPResponse`** (respond to a solicitation) | `/rfps` + email | **email / manual only** | — | ❌ **net-new** |

## The coverage gap, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (5 datasets)** | Open, machine-readable; ferry ridership is genuinely operational | Only peripheral programs; nothing about EDC's real estate, projects, or solicitations |
| **edc.nyc (Drupal)** | Holds the real portfolio — projects, assets, RFPs | Bot-walled behind Cloudflare (403); no API, no JSON, not reliably scrapable; unusable by partners or agents |
| **Solicitation response (email / PASSPort)** | The real EDC transaction | No machine-readable front door; email, pre-submission conferences, manual documents |

## Implications for the API-first + MCP proposal

1. **Surface the core portfolio as owned resources.** Model `DevelopmentProject`, `PropertyAsset`, and `Solicitation` from the site and publish them behind one EDC contract ([OpenAPI](openapi/edc.yaml)) — so what EDC *does* becomes queryable instead of trapped in bot-walled Drupal.
2. **Present the real open datasets cleanly.** Mapped In NY, NYC Ferry ridership, and WiredNYC as coherent resources under the same model, not five Socrata IDs.
3. **Open the solicitation pipeline.** Add the one net-new write workflow — `submit_rfp_response` — so responding to an RFP/RFEI (from registering interest to a full proposal) has a machine-readable, agent-native contract.
4. **MCP server** so an agent can answer "which EDC projects are underway in the Bronx?", "what industrial space does EDC manage?", "what RFPs are open?", and — the point — "register my firm's interest in this RFEI."
