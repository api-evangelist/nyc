# NYC Open Data — Queens District Attorney Datasets

**Result: zero.** Queried the Socrata Discovery API (`api.us.socrata.com/api/catalog/v1`) on 2026-07-13 for a Queens County District Attorney agency label across four candidate spellings — `Queens County District Attorney`, `Queens District Attorney`, `Office of the Queens County District Attorney`, and the bare `District Attorney` — and every query returned `resultSetSize: 0`. Machine-readable index: [opendata-queensda.json](opendata-queensda.json) (an empty array).

| Views | Type | ID | Name | Cols |
|--:|---|---|---|--:|
| — | — | — | *(no NYC Open Data assets)* | — |

## Why this is the honest, expected result

District Attorney offices in New York are **county/state prosecutorial agencies**, not NYC mayoral agencies, and they do **not publish to NYC Open Data**. There is no DA equivalent of NYCHA's Development Data Book or a Parks facilities table. The office's public data instead lives entirely inside its **WordPress site** — and, as it happens, is exposed through the **accidental** WordPress REST API rather than a curated open-data portal. See [apis-observed.md](apis-observed.md) and [crosswalk.md](crosswalk.md).

So the crosswalk for Queens DA is not fruit ↔ Open Data; it is **fruit ↔ WordPress content (wp-json)**. What would be Socrata datasets elsewhere are, here, WordPress categories:

- **press-releases** — 1,216 posts
- **court-cases** — 378 · **arraignments** — 131 · **charges** — 127 · **indictments** — 119 · **announcements** — 120 (the prosecution-lifecycle "datasets," as prose)
- **cold-cases** — 67 · **identified** — 47 · **unidentified** — 19 (the NamUs unidentified-persons initiative — the one genuinely structured dataset)
- **weekly-newsletters** — 256 · **statements** — 15 · **events** — 19 · **conviction-integrity-unit** — 10

(Category counts read live from `queensda.org/wp-json/wp/v2/categories`, 2026-07-13. Total posts: 1,557; total pages: 60.)

## Implication

The modernization work here is **not** liberating datasets from a portal — there is no portal. It is **structuring the office's own narrative** into resources and giving it a designed contract, then (because all five borough DAs do the same thing) publishing that as **one shared five-borough DA API** instead of five accidental WordPress REST APIs.
