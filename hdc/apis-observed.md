# APIs Observed While Crawling — HDC

Backend/service APIs the HDC surfaces call or expose, surfaced during the crawl (2026-07-16). The finding is even starker than DDC's: **HDC exposes no API of its own AND owns no NYC Open Data at all.** Its machine-readable record is entirely on systems it does not own — **HPD** (the LIHTC award datasets that *are* HDC's bond-financed deals), **OMB** (Debt Issuance by Issuer, where HDC is one `Issuer Name` value), and the **federal MSRB EMMA** platform (investor disclosure documents). The one transaction HDC owns — the **Developer Intake Portal** — has no API. Machine-readable index: [fruit.json](fruit.json) `apis_observed`.

| API / endpoint | Type | Owner | Public? | Notes |
|---|---|---|---|---|
| `www.nychdc.com` | Informational site | HDC (Drupal 10 on Pantheon, Fastly CDN) | Public (HTML) | Content only — Find / Invest / Develop / Manage. No content API, no JSON. `/developments` and `/where-we-fund` return 404 — no map/locator API. |
| **HDC Developer Intake Portal** | Intake / proposal submission | **HDC** | Login/contact-walled UI; **no public API** | The one HDC-owned transaction: *"All new project proposals must be submitted through HDC Developer Intake Portal."* Emits nothing machine-readable. |
| `data.cityofnewyork.us` (SODA) — **HPD-labeled** | Open Data API | **HPD** (Socrata / Tyler) | Yes — open, but **not HDC's** | HPD's LIHTC **4% award** datasets (`p8i7-ix2s`, `h9ws-rfd9`) are HDC's bond-financed deals — but published under the HPD label, not HDC. |
| `data.cityofnewyork.us` (SODA) — **OMB-labeled** | Open Data API | **OMB** | Yes — open, but **not HDC's** | Debt Issuance by Issuer (`n5n4-5k5r`) — HDC appears only as an `Issuer Name` value. |
| **MSRB EMMA** (`emma.msrb.org`) | Investor disclosure | **Federal (MSRB)** | Public (documents) | HDC's primary disclosure surface — Official Statements, financial statements, SDB annual reports — as PDFs on a **federal** platform, outside NYC Open Data. |
| `googletagmanager.com` / `google-analytics.com` | Analytics / tag mgmt | Google | Vendor | GTM + gtag on the site. |

## Takeaways

- **HDC has no owned API — and no owned Open Data.** Verified: **0** datasets are attributed to HDC. Not for developments, not for programs/term sheets, not for bonds, not for borrowers. This is thinner than DDC, which at least owns four Socrata datasets.
- **The record is dispersed across three other owners.** Developments → **HPD**; debt → **OMB**; investor disclosure → **federal MSRB EMMA**. HDC's own systems (the website and the Developer Intake Portal) publish nothing structured.
- **No citizen surface at all.** HDC is a financier: it serves developers and bond investors. There is no citizen service or citizen write anywhere in the domain; the honest net-new write is **applyForFinancing** (the Developer Intake Form, B2G).
- **No agent-native surface.** The [OpenAPI](openapi/hdc.yaml) + [MCP artifact](mcp/hdc-mcp.json) here propose one owned contract that consolidates the dispersed financing record (developments, programs, bonds) *and* fronts the Developer Intake flow with the net-new `apply_for_financing` write.
