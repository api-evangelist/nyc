# NYC Open Data — Bronx Borough President Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Bronx Borough President (BPBX)"** (verified via the Socrata Discovery API, 2026-07-13). **2 assets**, sorted by lifetime page views. Machine-readable: [opendata-bronxbp.json](opendata-bronxbp.json).

The shape of the corpus is the story: it is **tiny**. Two hand-published datasets — a funding table and a community-board roster — are the office's entire machine-readable footprint. There is **no dataset for land use / ULURP recommendations, the newsroom, or events**; those live only on the Revize CMS site (PDFs, PHP pages, a borrowed Google Calendar). See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 1,433 | dataset | `mdgu-ar69` | Bronx Borough President Capital Funding | 20 |
| 1,262 | dataset | `wbau-xy7g` | Bronx Community Boards | 7 |

## Groupings

- **Discretionary funding:** Bronx Borough President Capital Funding (`mdgu-ar69`, 20c) — Organization, Purpose, Funding, Type, Fiscal Year, Project Location + the full NYC geography spine (BBL, BIN, Council/Community/Census/NTA, state & congressional districts). → `DiscretionaryFundingAward`.
- **Community boards:** Bronx Community Boards (`wbau-xy7g`, 7c) — First name, Last Name, Community Board, Recommending Official, Term expires, Year, Zip Code of Application. → `CommunityBoardAppointment`.

## What is NOT here (the gaps)

- **Land-use / ULURP recommendations** — the office's most consequential charter output; published only as PDFs in a Revize document center. No dataset, no API.
- **Newsroom** (releases, statements, letters, testimonies) — server-rendered PHP pages; no feed.
- **Events & meetings** — two imported Google Calendars; not owned, not machine-readable as data.
- **Community-board applications / constituent requests** — no inbound structured data at all (PDF / email). The net-new write surface.
