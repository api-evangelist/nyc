# Technology & Vendor Inventory — NYPD

What the New York City Police Department's public web presence is built on and which third parties it depends on — fingerprinted from response headers and page markup during the crawl (2026-07-13). NYPD is unusual: the informational site is standard NYC.gov, but the department also runs **two custom Angular single-page transparency apps** on a **separate Azure Government backend**.

## Platform & hosting — the three surfaces

| Surface | Platform / hosting | Evidence |
|---|---|---|
| **nyc.gov/site/nypd** (informational) | **Oracle WebCenter Sites** CMS behind **Akamai** CDN + **nginx** origin | `livesite-version` header (WebCenter Sites), `server: nginx`, `x-akamai-transformed`, `server-timing: cdn-cache; desc=HIT` |
| **nypdonline.org** (Officer Profile / transparency) | **Angular** SPA + **Kendo UI (Telerik)** | `runtime`/`polyfills`/`main.<hash>.js` bundles, `styles.<hash>.css`, Kendo licensing strings in `main.js` |
| **compstat.nypdonline.org** (CompStat 2.0) | **Angular** SPA + **Kendo UI (Telerik)** | `main-<hash>.js` / `polyfills-<hash>.js` / `styles-<hash>.css` bundles |

## Monitoring & edge

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `server-timing: dtSInfo/dtRpid` on nyc.gov |
| CDN / edge | **Akamai** | `x-akamai-transformed`, `alt-svc: h3`, `ak_p` server-timing |
| Web server | **nginx** | `server: nginx` |

## The Azure Government backend (the important part)

The NYPD's interactive transparency data — officer profiles, shields, commands, and **disciplinary history** — is **not** on NYC's usual Socrata/Tyler stack. The `nypdonline.org` Angular bundle references a backend at:

| Property | Domain | Role |
|---|---|---|
| Officer search backend | **`officer.search.azure.us`** | Azure **Government** cloud API powering the Officer Profile search (undocumented; no public contract) |
| Officer Profile app | `nypdonline.org` | Public officer lookup + discipline history (Angular/Kendo SPA) |
| CompStat 2.0 app | `compstat.nypdonline.org` | Interactive weekly crime statistics by precinct (Angular/Kendo SPA) |

`officer.search.azure.us` sitting on **Azure Government** (`.azure.us`, not `.azure.com`) is a distinct hosting posture from every other NYC domain assessed so far — the record is real and queryable inside the app, but there is no published, owned API in front of it.

## Contrast with prior domains

- **Data isn't the problem — it's the richest domain in the project.** 42 Open Data datasets (vs. Council's 11), including the portal's single most-viewed dataset. But it is published as **flattened periodic snapshots**, not a live incident API.
- **The live/interactive record is app-trapped.** CompStat 2.0 and Officer Profile are Angular SPAs on an undocumented Azure Government backend — no public contract, no agent surface.
- **Two entirely different stacks in one department:** Oracle WebCenter Sites for content, a bespoke Angular + Azure Gov application tier for transparency tools.

## Modernization implications

1. **Expose, don't just publish.** Stand up one owned, resource-oriented API over the snapshot datasets **and** the app-trapped CompStat/Officer backends so consumers query live resources (complaints, arrests, shootings, officers), not download CSVs or scrape a SPA.
2. **Own the officer-transparency contract.** The disciplinary record already exists behind `officer.search.azure.us`; front it with a documented, versioned NYPD contract ([OpenAPI](openapi/nypd.yaml)) instead of an undocumented Azure Gov endpoint.
3. **Add the missing write workflow.** Requesting a copy of a police/collision report or filing a FOIL request is a set of disconnected forms today — surface it as one `PoliceReportRequest` resource.
