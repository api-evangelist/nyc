# Crosswalk — Website Fruit ↔ NYC Open Data (BOENY)

Maps the low-hanging fruit on **vote.nyc** to NYC Open Data. This is the shortest crosswalk in the project — because there is almost nothing to map to. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-boeny.json](opendata-boeny.json).

## The reframe — the fourth (and starkest) pattern

| Domain | Machine-readable coverage | Modernization verb |
|---|---|---|
| Parks | 237 Open Data assets; site renders HTML | **replatform** |
| DOE | 638 assets; search rented, backend hidden | **reclaim** |
| Council | 3 APIs (Legistar, WP REST, SODA), none owned | **consolidate + own** |
| **BOE / vote.nyc** | **2 assets (poll sites only); everything else PDF** | **digitize** |

At BOE the open-data era barely happened. The precondition isn't unifying or reclaiming APIs — it's **creating machine-readable data that does not exist**. This is the *original* 2013 low-hanging-fruit case (data trapped in PDFs and a legacy viewer), still live in 2026 for the city's election infrastructure.

Coverage: ✅ machine-readable · ❌ PDF/viewer-only (true gap).

## Entity crosswalk

| Entity | vote.nyc today | Open Data | Coverage |
|---|---|---|---|
| `PollSite` | locator (JS) | **Voting/Poll Sites** (`mifw-tguq`, 29c) | ✅ |
| `ElectionDistrict` | — | Election Districts (DCP) + Election District Poll Sites (`i3a3-qxkf`, BOENY) | ✅ |
| `ElectionResult` | **PDF per contest (Recap + EDLevel) + `enr.boenyc.gov`** | — | ❌ **flagship gap** |
| `Candidate` | PDF listings | — | ❌ gap |
| `Contest` | PDF contest lists + random-draw positions | — | ❌ gap |
| `Election` | calendar + PDF filing notices | — | ❌ gap |
| `BallotRequest` | `requestballot.vote.nyc` app | — | ❌ **net-new (write)** |

## What "digitize" means here, concretely

The valuable work is not wiring existing datasets together — there aren't any (beyond poll sites). It's:

1. **Structure election results.** Parse the per-contest result PDFs / the ENR system into a machine-readable `ElectionResult` resource (by contest, by election district, with the ranked-choice rounds `enr.boenyc.gov/rcv/` already computes).
2. **Structure candidates & contests.** Turn the candidate and contest-list PDFs into `Candidate` and `Contest` resources — so "who's on my ballot?" has an answer an app or agent can use.
3. **Structure the election calendar** — `Election` with dates, types (primary/general/special), and deadlines, instead of PDF filing calendars.
4. **Expose the transactional flow** — a `BallotRequest` read/write API in front of `requestballot.vote.nyc`.

## Implications for the API-first + MCP proposal

1. **Define the shape before the data exists.** The JSON Schemas here (`election-result`, `candidate`, `contest`) are *aspirational* — they specify the machine-readable form BOE data should take. That's the point: design-first gives the digitization a target.
2. **Anchor on poll sites** (the one solid dataset) and build outward to elections → contests → candidates → results.
3. **Results are the highest-value, highest-stakes gap** — a real `ElectionResult` API (including ranked-choice rounds) would replace a PDF-scraping status quo that the press and public re-solve every election.
4. **MCP server** so an agent can answer "where do I vote / who's on my ballot / what were the results / request my mail ballot" — none of which is possible against the current site.
