# Low-Hanging Fruit Index — Bronx District Attorney

**Agency:** Office of the Bronx District Attorney (Darcel D. Clark)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted `bronxda.nyc.gov` (Akamai edge + AWS ALB origin + Dynatrace/`ruxit` and Akamai mPulse RUM), identified the site as a legacy NYC.gov `/html/` **SHTML** application (meta-refresh stub → `/html/home/home.shtml`; SSI pages; JS-built nav in `nav-nodes.js`; jQuery/Bootstrap/Tether), and identified the `/html/data/` dashboards as **Microsoft Power BI (Gov)** iframes (`app.powerbigov.us`, report "Public Dash Case v9a"). Queried the NYC Open Data agency label via the Socrata Discovery API and confirmed **zero** datasets.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-bronxda.md](opendata-bronxda.md).

## Headline findings

1. **No API and zero Open Data.** The Socrata Discovery API returns **0** datasets for every Bronx DA agency label; the office exposes no JSON, no OpenAPI, no feed. Prosecution is a county function outside the NYC Open Data program.
2. **Legacy `.shtml` platform.** The public site is a hand-built NYC.gov `/html/` SHTML application (server-side-includes, a JavaScript nav, jQuery/Bootstrap) behind Akamai and an AWS ALB — not the shared "Livesite" chassis.
3. **The only data is trapped in Power BI.** Aggregate prosecution figures — arrests, charging decisions, case outcomes, defendant demographics — are published *only* as Microsoft Power BI (Gov) iframes: rendered pixels with no download, no query endpoint, no Open Data twin.
4. **No write surface.** Crime tips and Civilian Complaint Unit complaints are a phone call (718-590-2300); FOIL requests are a plain email (FOILREQUEST@BRONXDA.NYC.GOV). Neither returns a tracking number or status.
5. **One of five identical offices.** Manhattan, Brooklyn (Kings), Queens, and Staten Island (Richmond) DAs run the same charter functions — so the fix is not a bespoke Bronx build but **one shared District Attorney API**.

> **Reframe:** Parks = *replatform* a legacy site; NYCHA = *unlock* a CRM-locked service layer; Borough President = *templatize* a vendor brochure site; **Bronx DA = standardize.** Here there is almost nothing machine-readable to liberate — the work is to build the office's *first* data + API layer at all, free the aggregate figures from their Power BI iframe, add a trackable tip/complaint/FOIL intake, and do it once as a shared contract across all five boroughs.

## The fruit

| # | Name | Entity | Where it lives | Open Data twin |
|---|---|---|---|---|
| 1 | Press releases (2016-2025) | `PressRelease` | `.shtml` newsroom pages | ❌ none (HTML only) |
| 2 | Case statistics dashboards | `CaseStatistic` | Power BI (Gov) iframes | ❌ none (locked in Power BI) |
| 3 | Bureaus, divisions & programs | `Program` | `/html/bureaus/`, `/html/outreach/` | ❌ none (HTML only) |
| 4 | Community resources & important numbers | `CommunityResource` | `/html/outreach/`, homepage | ❌ none (HTML only) |
| 5 | Crime-victim services | `VictimService` | Crime Victims Assistance / Special Victims | ❌ none (HTML only) |
| 6 | **Tip / complaint / FOIL request** | `TipSubmission` | phone 718-590-2300 · FOIL email | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **No Bronx DA API** — no JSON, no OpenAPI, no Open Data. Confirmed zero Socrata datasets.
- **Microsoft Power BI (Gov)** — the `/html/data/` dashboards; embed-only, no data API.
- Platform: legacy NYC.gov `/html/` **SHTML** (Akamai edge, AWS ALB origin, Dynatrace + Akamai mPulse RUM, Google Analytics/Translate).

## Reverse-engineered entities

`PressRelease` · `CaseStatistic` (aggregate; never an individual case/defendant) · `Program` (bureau/division/outreach) · `CommunityResource` · `VictimService` · `TipSubmission` (net-new write; also stands in for the FOIL request and Civilian Complaint intake). Cross-office key: `OfficeReference` (office / county / borough / DA) so the same model serves all five borough DAs.

## Next

1. **JSON Schema** per entity, written generically across the five offices — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the content + the Power-BI-locked figures as clean resources + the net-new `POST /submissions` (tip / complaint / FOIL) — done ([openapi/bronxda.yaml](openapi/bronxda.yaml)).
3. **MCP** artifact: `find_press_releases`, `get_press_release`, `find_case_statistics`, `find_programs`, `find_community_resources`, `find_victim_services`, `submit_tip`, `check_submission` — done ([mcp/bronxda-mcp.json](mcp/bronxda-mcp.json)).
4. **Shared DA API:** promote this contract to a single `io.nyc.districtattorney` model that Manhattan, Brooklyn, Queens, and Staten Island DAs adopt.
