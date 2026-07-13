# Low-Hanging Fruit Index — vote.nyc

**Agency:** New York City Board of Elections (BOENY)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, robots-respecting). Drupal 9 site; JSON:API disabled (404). Key pages sampled (poll-site locator, election-results-summary, candidates, contest list, important notices); results/candidates/contests found to be PDFs. Open Data checked under agency `Board of Elections (BOENY)`.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-boeny.md](opendata-boeny.md).

## Headline findings

1. **The least-modernized domain in the project.** Drupal 9 with JSON:API disabled (no site API) and only **2 Open Data assets** — both poll sites.
2. **The two things voters most need have no API and no dataset.** *Who's running* (candidates) and *the results* are **PDFs** — one "Recap" and one "EDLevel" PDF per contest — plus a separate legacy viewer (`enr.boenyc.gov`).
3. **Poll sites are the one bright spot** — Voting/Poll Sites (29 cols, with accessibility + geo) and Election District Poll Sites are on Open Data; ED geometry via DCP.
4. **The transactional workflow is siloed** — ballot request/tracking lives in a separate app (`requestballot.vote.nyc`) with no public API.

> **Reframe (fourth distinct pattern):** Parks = *replatform*; DOE = *reclaim*; Council = *consolidate + own*; **BOE = digitize.** This is the **original pre-open-data low-hanging-fruit case, essentially untouched** — the precondition here isn't unifying or reclaiming APIs, it's *creating machine-readable election data at all* (results, candidates, contests), then building the transactional ballot API. The sharpest proof that "data liberation only partially worked": for the highest-stakes civic data, it barely happened.

## The fruit

| # | Name | Entity | Format today | Machine-readable? | Open Data |
|---|---|---|---|---|---|
| 1 | Poll Sites (locator) | `PollSite` | locator + dataset | ✅ | ✅ Voting/Poll Sites (`mifw-tguq`, 29c) |
| 2 | Election Districts | `ElectionDistrict` | geo | ✅ | ✅ DCP + BOENY (`i3a3-qxkf`) |
| 3 | **Election Results** | `ElectionResult` | **PDF-per-contest + ENR viewer** | ❌ | ❌ **flagship gap** |
| 4 | Candidates | `Candidate` | PDF listings | ❌ | ❌ gap |
| 5 | Contests / Ballot | `Contest` | PDF contest lists | ❌ | ❌ gap |
| 6 | Elections / Dates | `Election` | calendar + PDF notices | ❌ | ❌ gap |
| 7 | Ballot Request / Tracking | `BallotRequest` | separate app | ❌ | ❌ **net-new** |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **No site API** — Drupal 9 JSON:API disabled. **Socrata SODA** exposes only 2 poll-site datasets.
- Separate apps: **`enr.boenyc.gov`** (results viewer + `/rcv/` ranked-choice), **`requestballot.vote.nyc`** (ballot request/tracking).
- Platform: **Drupal 9** on Cloudflare + Varnish; **New Relic** monitoring; GTM. Fourth distinct platform.

## Reverse-engineered entities

`PollSite` · `ElectionDistrict` · `Election` · `Contest` · `Candidate` · `ElectionResult` · `BallotRequest` (net-new) — join keys: **election date**, **contest/office + district**, **ED number**.

## Next

1. **JSON Schema** per entity — especially the ones that have *no* source data yet (`ElectionResult`, `Candidate`, `Contest`), defining the machine-readable shape that should exist.
2. **OpenAPI** — a real elections API (poll sites, elections, contests, candidates, results) + the ballot-request write workflow.
3. **MCP** artifact: `find_poll_site`, `find_candidates`, `get_results`, `list_elections`, `request_ballot`, `track_ballot`.
