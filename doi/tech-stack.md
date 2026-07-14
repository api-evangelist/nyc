# Technology & Vendor Inventory — DOI

What the New York City Department of Investigation's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). DOI is **New York City's Inspector General**: an informational site on the shared NYC.gov platform, a library of **PDF-only** public reports, and a corruption-complaint intake running on a **third-party case-management SaaS (Kaseware)**.

## Three surfaces

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/doi/` | About, units, news, the Reports index, "report corruption" — content only |
| Public reports | `www.nyc.gov/assets/doi/reports/pdf/<year>/*.pdf` | DOI's core work product — investigation findings and reform recommendations, as **static PDFs** |
| **Report Corruption** | **`app.kaseware.us/public/#NYCDOI/…`** | The transactional layer: filing a fraud/waste/corruption complaint — a **third-party Kaseware intake form** |

## Informational site (nyc.gov/site/doi)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — it is not DOI-specific. DOI's distinct technology is (1) a PDF report library and (2) the Kaseware complaint portal.

## Public reports — PDFs, not data

The Reports pages list investigations as links to static PDFs under a predictable path:

```
/assets/doi/reports/pdf/2026/13AnnualAntiCorrRpt.Release.06.17.2026.pdf
/assets/doi/reports/pdf/2026/05NYCHAReclaim.Release.Rpt.03.03.2026.pdf
/assets/doi/reports/pdf/2026/08OIGNYPD.AR.Release.Rpt.04.15.2026.pdf
```

There is **no structured metadata, no report API, and no Open Data twin** for the reports. The agency's central output — what DOI actually produces — is a folder of PDFs.

## Report Corruption — the important part

The corruption-complaint intake is **not** a NYC.gov form. Following "Report Corruption" → "Submit Report Online" leads off-domain to a packaged case-management SaaS:

| Property | Value | Evidence |
|---|---|---|
| Host | `app.kaseware.us` | link target on report-corruption.page |
| Path | `/public/#NYCDOI/eab8c602-…` | public intake form for tenant `NYCDOI` |
| Product | **Kaseware** (investigation/case-management platform) | `<title>Kaseware Portal</title>`, `Kaseware` markers in markup |
| Edge | **Cloudflare** | `server: cloudflare`, `cf-ray`, `cf-cache-status` |
| UI framework | Client-rendered SPA (hash-routed `#NYCDOI/…`) | JavaScript-only public portal |

There is **no documented API, no OpenAPI, no JSON endpoint** — the complaint is a client-rendered vendor form. Phone (212-3-NYC-DOI), fax, and mail are the fallbacks. Every corruption tip is trapped behind the Kaseware SPA or a phone queue.

## Contrast with earlier domains

- **DORIS** = open indexes, records trapped in a vendor DAMS → *retrieve*.
- **OCME** = one stale dataset, no application, paper forms → *instrument*.
- **DVS** = open service data, referral runs through a third-party vendor form → *coordinate*.
- **DOI** = the investigative reports exist only as **PDFs** and the corruption complaint runs on a **third-party Kaseware form** → **digitize the outputs and the intake.**

## Modernization implications

1. **The core output is unstructured.** DOI's public reports — findings, subject agencies, and recommendations — are PDFs. An index/API over them ([OpenAPI](openapi/doi.yaml) `PublicReport`) is pure low-hanging fruit; the PPR dataset shows DOI can already publish recommendations structured.
2. **Own the intake.** The corruption complaint — the transaction that starts every investigation — should have an owned, machine-readable contract ([`createComplaint`](openapi/doi.yaml)) rather than a client-rendered Kaseware form, so anonymous, whistleblower-protected, and EO-16 obligatory reports can be filed programmatically.
3. **Depending on a vendor SaaS for the city's corruption-reporting front door is a governance and accessibility risk.** An agent-native contract in front of it ([MCP artifact](mcp/doi-mcp.json)) is the fruit worth picking.
