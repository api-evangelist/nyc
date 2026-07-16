# NYC Open Data — PDC Datasets

All NYC Open Data assets whose **attribution = "Public Design Commission (PDC)"** (verified via the Socrata Discovery API, 2026-07-16). Exactly **3** assets, sorted by lifetime page views. Machine-readable: [opendata-pdc.json](opendata-pdc.json).

The shape of the corpus is better than most thin agencies but lopsided: it captures **the review record and the collection**, but not the **calendar, agendas, minutes, commissioners, or awards**. Two datasets are the design-review log (one monthly, kept current; one annual roll-up), and the third is a genuinely rich **outdoor public-art inventory** (43 columns) — but that one has not been refreshed since 2021. There is **no dataset for the meeting calendar/agendas, submissions, commissioners, or design awards** — those live only as HTML/PDF on nyc.gov/site/designcommission. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols | Last updated |
|--:|---|---|---|--:|---|
| 4,013 | dataset | `2pg3-gcaa` | Public Design Commission Outdoor Public Art Inventory | 43 | 2021-07-02 |
| 2,312 | dataset | `tfrc-rjtr` | Public Design Commission Monthly Design Review | 10 | 2026-04-26 |
| 1,443 | dataset | `5fsv-ze7v` | Public Design Commission Annual Report | 12 | 2025-07-17 |

## Groupings

- **Design-review log (current):** Monthly Design Review (`tfrc-rjtr`, 10c) — DATE, CERTIFICATE_NUMBER, PROJECT_ID, PROJECT_TYPE, PUBLIC_PRIVATE, LEVEL_OF_REVIEW, AGENCY, BOROUGH, ACTION, TITLE. This is the live-ish per-meeting review record (last updated April 2026). ACTION carries the consent-vs-hearing distinction: `Calendared for Consent`, `Calendared for Committee and Consent`, `Calendared for Public Hearing`, `Delegation Approval`. LEVEL_OF_REVIEW carries the phase: Conceptual → Preliminary → Final (+ Amended variants).
- **Design-review roll-up (annual):** Annual Report (`5fsv-ze7v`, 12c) — adds SECONDARY_AGENCY, LEAD_AGENCY, RESULT (`Approved`, `Approved with conditions`, `Approved per delegation`, `Commented`, `Tabled`, `Withdrawn`, `Rejected`, `Found Incomplete`, `No quorum`), CONSTRUCTION_TYPE, REVIEW_CYCLES, PREVIOUS_YEAR_SUBMISSION.
- **The collection:** Outdoor Public Art Inventory (`2pg3-gcaa`, 43c) — City-owned monuments, memorials, artworks, and markers on City-owned property. Title/alternate title, artwork type, material, full artist/architect/landscape-architect credits, foundry/fabricator, creation & dedication dates, acquisition, inscription, subject keywords, location name, managing City agency, PDC record refs, address, borough, latitude/longitude, and Block/Lot (→ BBL). Genuinely rich — but frozen since 2021.

## What the datasets tell us about the domain

- **Top submitting agencies** (by reviewed-project count in the Monthly Design Review log): **DPR** (Parks, ~1,009), **DOT** (~316), **EDC** (~221), **DEP** (~187), **FDNY** (~93), **BNYDC** (~89), **DDC** (~88), **DOE** (~87), plus joint submissions like DDC/DOT, EDC/DPR, DDC/DPR, DPR/CPC. This confirms PDC is **agency-facing**: every project comes from a City agency, never a citizen.
- **Project types** reviewed: Architecture, Landscape architecture, Artwork, Signage, Street furniture, Newsstand, Bridge, Distinctive sidewalk, Distinctive lighting, Building systems & Modifications.

## What is missing

- **No meeting calendar / agenda / minutes dataset** — the monthly calendar, submission deadlines, agendas, and minutes are HTML/PDF only.
- **No submissions dataset and no submission portal** — project submission is a manual PDF application form + checklist emailed by the agency liaison; only the *outcome* lands in the review datasets.
- **No commissioners dataset** — the 11 members are listed only on the About/People page.
- **No design-awards dataset** — Awards for Excellence in Design recipients are HTML/PDF only.
- **The collection is stale** — the 43-column inventory is a strong asset but has not been updated since 2021.
