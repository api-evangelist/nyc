# Low-Hanging Fruit Index — PDC

**Agency:** New York City Public Design Commission (PDC)
**Assessed:** 2026-07-16
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/designcommission` (Akamai + nginx + NYC.gov "Livesite" platform + Dynatrace + AWS ALB) and read the Design Review / Application Process / About pages, which document the manual PDF-and-email submission process, the 11-member pro-bono Commission, and the consent-vs-public-hearing meeting structure. Verified the NYC Open Data attribution `Public Design Commission (PDC)` via the Socrata Discovery API and pulled all **3** assets with column schemas and real distinct values (level of review, action, result, project/construction type).

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-pdc.md](opendata-pdc.md).

## Headline findings

1. **PDC is the City's design-review agency (NYC Charter Chapter 37).** Eleven pro-bono members review and vote monthly on projects — permanent architecture, landscape architecture, and art — proposed **on or over City-owned property**. It is also caretaker and curator of the City's public art collection and archive.
2. **PDC is agency-facing, not citizen-facing.** Only a City agency with jurisdiction over the property may submit; an artist or community works *through* the sponsoring agency (Parks, DOT, EDC…). There is **no citizen and no citizen transaction** anywhere in the domain.
3. **The read is decent but lopsided.** Three NYC Open Data datasets publish the monthly review log (current to 2026), the annual roll-up, and a rich 43-column outdoor public-art inventory (frozen at 2021). But the **meeting calendar/agendas/minutes, the commissioners, and the design awards** are HTML/PDF only.
4. **The write is not even a system.** Submitting a project for design review — PDC's core function — is a **signed PDF application form emailed by the agency's PDC liaison** by the submission deadline, with paper hard copies delivered to City Hall afterward. There is no portal (unlike LPC's Salesforce Portico) and no API.

> **Reframe:** LPC = *bind* a scattered read to a Salesforce-locked filing; DDC = *surface* a thin, historical portfolio whose transactions run on citywide systems; **PDC = digitize.** Here the read is real (3 datasets, one of them a rich art inventory) but the core transaction — submitting a design for review — is a PDF and an email. The work is to *digitize* that submission into an owned, agent-native contract and to surface the calendar/commissioners/awards the datasets leave out.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | Reviewed projects (monthly + annual) | `DesignProject` | SODA | ✅ Monthly (`tfrc-rjtr`) + Annual (`5fsv-ze7v`) |
| 2 | City public art & monument collection | `CollectionItem` | SODA | 🟡 Outdoor Public Art Inventory (`2pg3-gcaa`, 43c, 2021) |
| 3 | Monthly meetings / agendas / minutes | `ReviewMeeting` | HTML/PDF | ❌ gap (no API) |
| 4 | Commissioners (11 pro-bono members) | `Commissioner` | HTML | ❌ gap (no API) |
| 5 | Awards for Excellence in Design | `DesignAward` | HTML/PDF | ❌ gap (no API) |
| 6 | **Submit a project for design review** | `DesignSubmission` | PDF form + email | ❌ **net-new (B2G)** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 3 PDC datasets (the one real, open data surface; review log current, art inventory rich but frozen at 2021).
- **Project submission** — a manual **PDF application form + checklist emailed** by the City agency's PDC liaison; no portal, no upload API.
- **ACRIS** (DOF) — linked so applicants can confirm jurisdiction; not PDC-owned.
- **YouTube / MS Teams** — meeting livestream and remote participation; not data surfaces.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM, AWS ALB) — the same chassis as DDC/LPC peers.

## Reverse-engineered entities

`DesignProject` (reviewed project) · `CollectionItem` (artwork/monument) · `ReviewMeeting` (agenda/minutes; no twin) · `Commissioner` (no twin) · `DesignAward` (no twin) · `DesignSubmission` (net-new B2G write) — join key **PROJECT_ID**; collection joins on **Block/Lot → BBL** and lat/long.

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (PROJECT_ID, LEVEL_OF_REVIEW, ACTION, RESULT, CONSTRUCTION_TYPE, the 43 inventory columns) and the documented submission process — done ([schemas/](schemas/)).
2. **OpenAPI** surfacing projects + meetings + collection + commissioners + awards as clean resources + the net-new `POST /submissions` (`submitDesignReview`) and `GET /submissions/{id}` (`getDesignReviewStatus`) — done ([openapi/pdc.yaml](openapi/pdc.yaml)).
3. **MCP** artifact: `find_projects`, `get_project`, `find_meetings`, `get_meeting`, `search_collection`, `get_collection_item`, `list_commissioners`, `find_awards`, `list_my_submissions`, `submit_design_review` — done ([mcp/pdc-mcp.json](mcp/pdc-mcp.json)).
