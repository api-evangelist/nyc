# Low-Hanging Fruit Index — MOME

**Agency:** NYC Mayor's Office of Media & Entertainment (MOME)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/mome` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace) and the film-permit application system at `nyceventpermits.nyc.gov/film`, identified as an **ASP.NET Core app titled "MOME E-Apply"** (`Microsoft-IIS/10.0`, `X-Powered-By: ASP.NET`, `.AspNetCore.Antiforgery` cookie, `/Web/Login` redirect). Verified the NYC Open Data agency label `Mayor's Office of Media And Entertainment (MOME)` via the Socrata Discovery API (note the capitalized "And") and pulled both assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-mome.md](opendata-mome.md).

## Headline findings

1. **MOME is a split domain.** An informational site on the shared NYC.gov chassis, and a film-permit **application portal ("MOME E-Apply")** on the citywide event-permitting host (`nyceventpermits.nyc.gov/film`) with **no API**.
2. **The flagship output is heroically open.** **Film Permits** (`tg4x-b46p`) is one of the most-viewed datasets in all of NYC Open Data (~530k views), automated and updated **daily** — every location shoot the Film Office greenlights, as a public geography record.
3. **But the intake is closed.** Applying for a permit — the everyday production transaction — lives only inside the login-walled E-Apply portal or a Letter-in-Lieu email. None of it has a machine-readable contract.
4. **The footprint is unusually narrow.** Just **2 datasets** under the MOME label — Film Permits and MARCH nightlife inspections (`b84a-xy2t`). Everything else (Made in NY, workforce, Public Access Media) is HTML only. The applicant / production company is never published.

> **Reframe (fifth distinct pattern):** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a service layer locked in a CRM; **MOME = greenlight the intake.** Here the *output* is already the busiest dataset in the city — the work is least about liberating data and most about giving the **application** (submitting and tracking a film permit) an owned, agent-native API instead of a portal login.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Film Permits | `FilmPermit` | SODA | ✅ Film Permits (`tg4x-b46p`, 14c) |
| 2 | Held filming locations | `ScreenActivity` | SODA (derived) | ✅ `ParkingHeld` + DOT twin (`c2az-nhru`) |
| 3 | MARCH nightlife inspections | `MarchInspection` | SODA | ✅ MARCH Inspections (`b84a-xy2t`, 35c) |
| 4 | MOME programs / Public Access Media | `MediaProgram` | HTML | ❌ gap (no dataset) |
| 5 | Production company (applicant) | `ProductionCompany` | E-Apply portal | 🟡 partial (DOT twin contacts) |
| 6 | Do I need a permit? / Insurance / Letter in Lieu | `FilmPermitApplication` | HTML + email | ❌ gap (no API) |
| 7 | **Apply for a permit** | `FilmPermitApplication` | E-Apply portal + email | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 2 MOME datasets (the one real, open API; the flagship Film Permits feed + MARCH).
- **ASP.NET Core "MOME E-Apply"** — the film-permit application portal; login-walled, JavaScript-only, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as Parks/DOE/Council/NYCHA; MOME's distinct tech is the packaged event-permit portal.

## Reverse-engineered entities

`FilmPermit` · `ScreenActivity` (held location) · `MarchInspection` · `MediaProgram` (incl. PublicAccessMedia) · `ProductionCompany` (applicant; never published) · `FilmPermitApplication` (net-new write; the E-Apply-locked intake) — join keys: **EventID**, and the geography spine (**borough**, **community board**, **police precinct**, **ZIP**).

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (EventID, ParkingHeld, Category/SubCategoryName, the geography spine) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open output as clean resources + the net-new `POST /permit-applications` (apply for a permit) — done ([openapi/mome.yaml](openapi/mome.yaml)).
3. **MCP** artifact: `find_film_permits`, `get_film_permit`, `get_film_permit_locations`, `find_screen_activity`, `find_programs`, `find_march_inspections`, `list_my_permit_applications`, `apply_for_film_permit` — done ([mcp/mome-mcp.json](mcp/mome-mcp.json)).
