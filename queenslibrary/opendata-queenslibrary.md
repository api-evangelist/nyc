# NYC Open Data — Queens Public Library Datasets

All NYC Open Data assets whose **Dataset-Information_Agency = "Queens Library (QBPL)"** (verified via the Socrata Discovery API, 2026-07-13). **Exactly one asset.** Machine-readable: [opendata-queenslibrary.json](opendata-queenslibrary.json).

The near-absence *is* the story. Queens Public Library is an **independent nonprofit**, not a mayoral agency, so it publishes almost nothing to NYC Open Data. Full-text searches for "Queens Public Library" / "Queens Library" across data.cityofnewyork.us return only the single branch-directory dataset below (plus unrelated citywide datasets — public restrooms, Wi-Fi hotspots, public computer centers — that merely *mention* libraries, owned by OTI and the Mayor's Office of Operations, not QPL). Everything a patron actually uses — the catalog, events, digital lending, holds, and cards — lives inside **packaged SaaS platforms** (BiblioCommons, Communico, OverDrive/Libby, Axis 360, hoopla, Springshare), none of which surfaces an owned QPL API. See [crosswalk.md](crosswalk.md).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| 21,337 | dataset | `kh3d-xhq7` | Queens Library Branches | 21 |

## The one dataset

- **Queens Library Branches (`kh3d-xhq7`, 21c)** — hours and locations of QPL branches, with the full NYC geography spine (Borough, Community Board, Council District, Census Tract, BIN, BBL, NTA) and lat/long. 21,337 lifetime views, 6,193 downloads. This is the sole machine-readable, open QPL entity — the `Branch` object.

## What is *not* here (the gaps)

- **`CatalogItem`** — the bibliographic catalog is entirely inside **BiblioCommons** (`queenslibrary.bibliocommons.com`); no Open Data twin.
- **`Event`** — programs are managed in **Communico** (`queens.libnet.info`, `connect.queenslibrary.org`); no Open Data twin.
- **`DigitalCollection`** — eBooks/eAudiobooks/streaming are split across **OverDrive/Libby, Axis 360, and hoopla**; no Open Data twin.
- **`BookHold`** and **`LibraryCard`** — the login-walled patron transactions inside BiblioCommons; no Open Data twin and no owned API. `BookHold` (place a hold) is the net-new write surface.

> The three NYC public library systems — **Queens Public Library**, **Brooklyn Public Library**, and **The New York Public Library** (Manhattan/Bronx/Staten Island) — are **separate nonprofits** with separate catalogs, cards, and vendor stacks. There is no shared NYC library API. That absence is an opportunity, not just a gap.
