# Low-Hanging Fruit Index — DCLA

**Agency:** Department of Cultural Affairs (DCLA)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/dcla` (Akamai + nginx + NYC.gov "Livesite" v22 + Dynatrace) and the **DCLA Grants Management System** at `dclagms.nyc.gov/grants/s/` (a **Salesforce Experience Cloud** community — `LSKey-c$` cookies, `/grants/s/` path, backed by `culturalaffairsnyc.my.salesforce.com` via SAML SSO). Verified the NYC Open Data agency label `Department of Cultural Affairs (DCLA)` via the Socrata Discovery API and pulled all **9** assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-dcla.md](opendata-dcla.md).

## Headline findings

1. **DCLA publishes funding outcomes, not the application pipeline.** **9 NYC Open Data datasets** publish who was funded and for how much — program grants, capital funding, Cultural Institutions Group operating support — plus a geocoded cultural-organization directory, completed Percent for Art commissions, and Materials for the Arts donation summaries. Every one is an *outcome*.
2. **The core transaction is locked in Salesforce.** Applying for a Cultural Development Fund grant — the single most important interaction between DCLA and its constituency — lives only in the **Grants Management System**, a Salesforce Experience Cloud portal reached by login. It has no public API and no Open Data twin.
3. **No owned contract binds organizations to their funding.** The funding datasets key on organization *name* and *application #* with no stable id, so an agent must stitch names across 9 Socrata IDs by hand. There is no single DCLA API.
4. **Donors stay private by design.** Materials for the Arts data is published only in aggregate by year and category; no individual donor is ever exposed.

> **Reframe (the grantmaker pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a CRM; DCWP = *bind* the open lifecycle and add the writes; **DCLA = open the grant pipeline.** Here the funding *results* are open but the funding *request* is closed — the work is to bind the outcome data into one owned contract and to open the grant application (net-new write) that today lives only in a Salesforce portal.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Cultural Organizations directory | `CulturalOrganization` | SODA | ✅ Cultural Organizations (`u35m-9t32`, 16c) + Resources (`rb2h-bgai`) |
| 2 | Program Funding (grant awards) | `ProgramFunding` | SODA | ✅ Programs Funding (`y6fv-k6p7`); FY11 (`rskq-5bfv`); FY2010 (`j8p3-8ufc`) |
| 3 | Capital Funding | `CapitalFunding` | SODA | ✅ Capital Funding (`7hgn-sgmk`, 6c) |
| 4 | Cultural Institutions Group (CIG) | `CulturalInstitution` | SODA | ✅ CIG Funding (`ka27-qx5k`) |
| 5 | Percent for Art public artworks | `PublicArtwork` | SODA | ✅ Completed Percent for Art projects (`gzdv-qiga`, 7c) |
| 6 | Materials for the Arts donations | `MaterialsForTheArts` | SODA | 🟡 MFTA Donor Information (`vhtt-kpwy`) — aggregate only |
| 7 | **Apply for a grant** | `GrantApplication` | Grants Management System | ❌ **net-new write** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 9 DCLA datasets (the one real, open API; funding outcomes and directory as reference data).
- **DCLA Grants Management System** (`dclagms.nyc.gov`) — a Salesforce Experience Cloud community; login-gated, browser-only, no public API.
- Platform: informational site on the **NYC.gov shared "Livesite" v22 platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as NYCHA and every citywide agency site.

## Reverse-engineered entities

`CulturalOrganization` · `ProgramFunding` (grant award) · `CapitalFunding` · `CulturalInstitution` (CIG) · `PublicArtwork` (Percent for Art) · `MaterialsForTheArts` (aggregate; never individual donor) · `GrantApplication` (net-new write) — join keys: **Organization Name**, **Application #**, **Fiscal Year (FY)**, **BIN/BBL**.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Organization, Application #, Fiscal Year, Discipline, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** binding the open funding data as clean resources (10 operations) + the net-new `POST /grant-applications` (apply for a grant) — done ([openapi/dcla.yaml](openapi/dcla.yaml)).
3. **MCP** artifact: `find_cultural_organizations`, `get_cultural_organization`, `find_program_funding`, `find_capital_funding`, `find_cultural_institutions`, `find_public_artworks`, `find_materials_for_the_arts`, `list_my_grant_applications`, `apply_for_grant` — done ([mcp/dcla-mcp.json](mcp/dcla-mcp.json)).
