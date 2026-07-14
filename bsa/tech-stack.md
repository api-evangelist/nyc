# Technology & Vendor Inventory — BSA

What the NYC Board of Standards & Appeals' public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-13). BSA is **content + case-index on the shared NYC.gov platform**, with **no online application portal**: the intake workflow is downloadable PDF forms filed on paper.

## Front doors

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/bsa/` | About, applications, public hearings, resolutions, archives — content |
| Resolutions / applications search | `/site/bsa/resolutions/search-for-resolutions.page` | Server-rendered Livesite search widget over decided cases (1998–present) |
| Decision PDFs | `/assets/bsa/downloads/pdf/decisions/<calendar>.pdf` | The written resolution for each case, as a PDF |
| Application forms | `/assets/bsa/downloads/pdf/forms_instructions/*.pdf` | **The intake** — `bz_form.pdf`, `appeal_form.pdf`, `bzy_form.pdf`, `soc_form.pdf`, checklists, drawing/radius-map guidelines. Filed on paper. |
| NYC Open Data | `data.cityofnewyork.us` | 4 BSA case-index datasets (SODA) |

## Informational site (nyc.gov/site/bsa)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `x-akamai-transformed: 9 …`, `server-timing: cdn-cache; desc=HIT`, `alt-svc: h3` |
| Web server | **nginx** | `server: nginx` |
| App tier / load balancer | AWS ALB | `set-cookie: AWSALB`, `AWSALBCORS` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme; `JSESSIONID` |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`, `dtCookie`, `server-timing: dtSInfo/dtRpid` |
| Security headers | CSP `frame-ancestors 'self' *.nyc.gov *.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — the identical fingerprint as NYCHA, DOB, DCP, and the rest. BSA has **no agency-specific platform of its own**.

## The search / records surface

The resolutions and pre-1998 application searches are **server-rendered Livesite components**, not APIs: the page posts back to itself (`search-for-resolutions.page?submit=true&componentID=…` via an inline `searchRecords()` handler). There is **no JSON endpoint, no OpenAPI**. Older records (pre-1998, back to 1916) are not online at all — the site directs researchers to a **Records Request** page.

## The intake — the important part

BSA has **no online application portal**. To file a variance, special permit, extension, or appeal, an applicant:

1. downloads the matching PDF form (`bz_form.pdf`, `soc_form.pdf`, `bzy_form.pdf`, `appeal_form.pdf`, `lsc_form.pdf`, TAHP forms),
2. assembles the checklist exhibits (zoning analysis, drawings, radius map, CEQR/EAS, photos, affidavit of ownership),
3. and **files on paper**.

Only the resulting case **status** later surfaces in Open Data. The act of filing — and tracking a filing before decision — has **no machine-readable contract**.

## Contrast with earlier domains

- **Parks** = data-as-HTML on a legacy platform → *replatform*.
- **DOE** = search rented to a vendor, backend hidden → *reclaim*.
- **Council** = three real-but-fragmented APIs, none owned → *consolidate + own*.
- **NYCHA** = reference data wide open, service layer locked in a vendor CRM → *unlock*.
- **BSA** = case **outcomes** are open (4 datasets + a search widget), but the **intake is paper PDF forms** with no online portal → **digitize the intake.**

## Modernization implications

1. **The gap is intake, not outcomes.** BSA publishes what it *decided* (status, disposition, decision PDF) but offers no way to *file* or *track* a case by machine. A property owner or agent asking "file my variance" or "what's the status of my application?" has nothing to call.
2. **Structure the decisions.** Resolutions are PDFs; the reasoning, conditions, and vote are trapped in the document. An owned API ([OpenAPI](openapi/bsa.yaml)) should publish resolutions as resources.
3. **Publish the hearing calendar.** It exists only as HTML/PDF (plus Zoom links) — no dataset. It should be a resource.
4. **Add the one net-new write workflow** — filing a **variance application** — and front it with an agent-native contract ([MCP artifact](mcp/bsa-mcp.json)).
