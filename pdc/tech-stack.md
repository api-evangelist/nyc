# Technology & Vendor Inventory — PDC

What the NYC Public Design Commission's public surfaces are built on and which third parties they depend on — fingerprinted from response headers and page markup during the crawl (2026-07-16). PDC is a small, **agency-facing design-review commission** (11 pro-bono members, small staff): an informational site on the shared NYC.gov platform, three NYC Open Data datasets, and a **submission process that is entirely manual** — a PDF application form emailed by a City agency liaison. There is no submission portal and no PDC-owned application at all.

## One front door, one back door

| Surface | URL | What it does |
|---|---|---|
| Informational site | `www.nyc.gov/site/designcommission/` | About, Design Review, Publications, Awards, Archive, Tours/Events — content only |
| **Submission "system"** | **email + PDF, no portal** | The transaction: a City agency's PDC liaison emails a signed PDF application form, checklist, and drawings by the deadline; approved projects deliver hard copies to City Hall |

## Informational site (nyc.gov/site/designcommission)

| Layer | Technology / Vendor | Evidence |
|---|---|---|
| CDN / edge | **Akamai** | `server: AkamaiGHost` on the bot-blocked path; `alt-svc: h3`; `server-timing: ak_p` |
| Web server | **nginx** | `server: nginx` |
| CMS platform | **NYC.gov shared publishing platform** ("Livesite") | `livesite-version: 22`; shared `/site/<agency>/` URL scheme across all NYC agencies |
| App tier / load balancing | **AWS ALB** | `set-cookie: AWSALB / AWSALBCORS`; `JSESSIONID` (Java) |
| Real-user monitoring | **Dynatrace** | `x-oneagent-js-injection: true`; `server-timing: dtSInfo/dtRpid`; `dtCookie` |
| Security headers | CSP `frame-ancestors 'self' https://*.nyc.gov https://*.csc.nycnet`, `x-content-type-options: nosniff` | response headers |

This is the **same NYC.gov chassis** every citywide agency site sits on — the same Akamai + nginx + Livesite + Dynatrace + AWS ALB stack seen on DDC and LPC. It is not a PDC-specific stack. PDC exposes **no content API, no OpenAPI, no JSON endpoint** on its informational site. (Note: unauthenticated bot requests to `index.page` return `403` from `AkamaiGHost`; a browser User-Agent returns `200` — a bot-management edge rule, not an application difference.)

## The submission process — the important part (and it is not a system at all)

PDC's application-process page is explicit about how a project reaches the Commission, and it is striking for 2026:

- **Only a City agency may submit.** The agency with jurisdiction over the property makes the formal submission. *"If an artist would like to install a work of art in a City park, the application to the Commission must come from the Department of Parks & Recreation."* There is no citizen submission path.
- **A designated liaison transmits it.** Each City agency has a PDC liaison who emails a written transmittal listing all projects to be reviewed and ensures each submission is complete and on time.
- **The application is a downloadable PDF form** plus a category-specific **checklist**, requiring the Community Board(s) and City Council District(s) for each project.
- **Digital delivery is by email** to PDC staff by **12:00pm on the submission deadline**; material samples and large models are coordinated separately.
- **Approved projects require hard copies** delivered to the Manhattan Municipal Building mail room / City Hall the Thursday after the meeting.

So the transactional layer for PDC's core function — reviewing every permanent design and artwork on City-owned property — is a **PDF form, an email, and a paper delivery**. There is no portal (no Salesforce community like LPC's Portico, no PASSPort), no upload API, and no machine-readable submission at all.

## Systems referenced (all read-only, none PDC-owned APIs)

| System | Host | What it does |
|---|---|---|
| **NYC Open Data (Socrata/Tyler)** | `data.cityofnewyork.us` | The 3 PDC datasets (Monthly Design Review, Annual Report, Outdoor Public Art Inventory) via SODA `/resource/<id>.json`. The one real machine-readable PDC surface. |
| **ACRIS** | `a836-acris.nyc.gov` | Property-ownership records — the site links applicants here to confirm which agency has jurisdiction. Owned by DOF, not PDC. |
| **YouTube** | `youtube.com` | Meetings are livestreamed; not a data surface. |
| **Microsoft Teams** | — | Remote meeting participation / testimony. |

## Contrast with earlier design/review peers

- **LPC** = reference data wide open across Socrata *and* Esri ArcGIS, but the permit **filing is locked in a Salesforce (Portico) portal** with no API → *bind*.
- **DDC** = a vendor-facing agency whose data is thin/historical and whose transactions run on citywide systems it doesn't own (PASSPort/MOCS) → *surface*.
- **PDC** = an agency-facing design-review commission whose read is decent (3 datasets, one of them a 43-column art inventory) but whose **write is not even a system** — a PDF form emailed by an agency liaison → **digitize.**

## Modernization implications

1. **The read is real but incomplete.** Three Socrata datasets cover the review log and the collection, but the calendar/agendas, commissioners, and awards are HTML/PDF only, and the rich art inventory is frozen at 2021. A modern PDC API ([OpenAPI](openapi/pdc.yaml)) should present projects, meetings, the collection, commissioners, and awards as one coherent resource model.
2. **The write is the story.** The one write surface PDC could own — an agency submitting a project for design review — is today a manual PDF/email transmittal. There is **no citizen write**; the honest net-new write is B2G (agency-to-Commission). Digitizing it as a structured [`DesignSubmission`](schemas/design-submission.json) — signed by all involved agencies, carrying the Community Board / Council District, category checklist, and attachments — is the low-hanging fruit.
3. **An agent-native contract** ([MCP artifact](mcp/pdc-mcp.json)) over both would let an agency (or its consultant) answer "what has PDC approved on this site?", "when is the next submission deadline?", and — the point — "submit this park artwork for conceptual review."
