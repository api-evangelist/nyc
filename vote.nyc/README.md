# vote.nyc — Low-Hanging Fruit Assessment

Fourth domain in the [NYC Modernization](../README.md) project. An outside-in [low-hanging-fruit assessment](https://apievangelist.com/2016/04/13/formalizing-my-approach-to-identifying-the-low-hanging-api-fruit/) of the **New York City Board of Elections (BOENY)** — the least-modernized domain assessed, and the one that most sharply validates the project's premise.

## Files

- [low-hanging-fruit.md](low-hanging-fruit.md) / [fruit.json](fruit.json) — the fruit index (poll sites, districts, elections, contests, candidates, results, ballot request).
- [tech-stack.md](tech-stack.md) — technology & vendor inventory (Drupal 9, Cloudflare/Varnish, New Relic; the ENR + requestballot apps).
- [apis-observed.md](apis-observed.md) — the near-absence of APIs (Drupal JSON:API disabled; 2 poll-site datasets only).
- [crosswalk.md](crosswalk.md) — fruit ↔ Open Data (the shortest crosswalk in the project).
- [opendata-boeny.md](opendata-boeny.md) / [opendata-boeny.json](opendata-boeny.json) — the 2 BOENY Open Data assets.
- [schemas/](schemas/) — JSON Schema per object: `poll-site` · `election-district` · `election` · `contest` · `candidate` · `election-result` · `ballot-request` (+ shared `_common`).
- [openapi/nyc-elections.yaml](openapi/nyc-elections.yaml) — OpenAPI 3.1 contract `$ref`ing each object.
- [mcp/nyc-elections-mcp.json](mcp/nyc-elections-mcp.json) — design-first MCP server definition (7 agent tools; artifact, not a deployment).

## What was found — the fourth (and starkest) pattern

BOE is the closest thing to the **original, pre-open-data low-hanging-fruit case**, still live in 2026:

- **No site API** — Drupal 9 with JSON:API disabled.
- **Two Open Data assets total** — both poll sites. Nothing else.
- **The two things voters most need have no API and no dataset** — *who's running* (candidates) and *the results* are **PDFs** (one "Recap" + one "EDLevel" file per contest), plus a separate legacy viewer (`enr.boenyc.gov`, with ranked-choice at `/rcv/`).
- **The transactional flow is siloed** — mail-ballot request/tracking is a separate app (`requestballot.vote.nyc`).

**Reframe — the four verbs, in evidence:**

| Domain | Machine-readable coverage | Verb |
|---|---|---|
| Parks | 237 Open Data assets (HTML site) | **replatform** |
| DOE | 638 assets (rented search, hidden backend) | **reclaim** |
| Council | 3 APIs, none owned | **consolidate + own** |
| **BOE / vote.nyc** | **2 assets; results/candidates PDF-only** | **digitize** |

Here the precondition isn't unifying or reclaiming APIs — it's **creating machine-readable election data at all**. Several schemas in this domain are deliberately **aspirational**: `election-result` (with ranked-choice rounds), `candidate`, and `contest` define the shape BOE data *should* take, giving the digitization a design-first target.

## Reverse-engineered entities

`PollSite` · `ElectionDistrict` · `Election` · `Contest` · `Candidate` · `ElectionResult` · `BallotRequest` (net-new).

## Method & caveats

Outside-in crawl (browser UA, robots-respecting). Drupal 9; JSON:API 404. Key pages sampled; results/candidates/contests confirmed PDF-only. Open Data checked under `Board of Elections (BOENY)`. A sample, not a full spider.

## Status & next

- **Done (2026-07-13):** assessment ✅ · tech/vendor inventory ✅ · APIs-observed ✅ · Open Data crosswalk (2 assets) ✅ · JSON Schemas (7) ✅ · OpenAPI 3.1 (10 paths/11 ops) ✅ · MCP artifact (7 tools) ✅.
- **Next:** a proof-of-concept that parses the result PDFs / ENR into the `ElectionResult` shape (the highest-value digitization); then a fifth domain from [../domains.md](../domains.md), or a cross-domain synthesis.
