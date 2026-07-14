# Crosswalk — Website Fruit ↔ APIs ↔ NYC Open Data (Staten Island Borough President)

Maps the low-hanging fruit on **statenislandusa.com** to (a) the **existing APIs** (there are none of the office's own) and (b) the **NYC Open Data assets** under the agency label `Staten Island Borough President (BPSI)`. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-statenislandbp.json](opendata-statenislandbp.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every transaction locked in an Oracle Siebel CRM → *unlock.*
- **Staten Island BP:** a **Weebly brochure site** with **two trivial datasets and no API** — and **four identical sibling offices** → **federate.**

This domain inverts the abundance problem. It is not that data is trapped in HTML or a CRM — it is that **the data essentially does not exist in machine-readable form at all**. The office's real charter powers (land-use review, community board appointments, discretionary budget, borough board resolutions) are published only as PDFs and web pages. And the same is true, page-for-page, of the Manhattan, Bronx, Brooklyn, and Queens borough-president offices. The modernization is not to liberate a dataset but to **define one shared model and contract for all five offices.**

Coverage: ✅ open twin · 🟡 partial/aggregate · ❌ gap (no API or data).

## Entity crosswalk

| Entity | Website | API today | Open Data | Cov. |
|---|---|---|---|---|
| `LandUseRecommendation` (ULURP) | `/notices`, Land Use office | none (City Planning ZAP elsewhere) | — | ❌ gap |
| `CommunityBoardAppointment` | `/cbapplication`, `/borough-board` | none | — | ❌ gap |
| `DiscretionaryFundingAward` | `/budget` (mail/email only) | none (Schedule C elsewhere) | — | ❌ gap |
| `Resolution` (Borough Board) | `/borough-board` (monthly PDFs) | none | — | ❌ gap |
| `Event` | `/community-events`, `/summerconcerts` | none | — | ❌ gap |
| `ConstituentRequest` (BP Assist) | `/bpassist` | none | BP Assist Helpline Requests (`3fes-huds`) — **aggregate counts, ends FY20** | 🟡 aggregate |
| **`CommunityBoardApplication`** (apply to a board) | `/cbapplication` | **Weebly form only** | — | ❌ **net-new** |
| — (lookup) | — | none | Category Master File (`mmut-uup9`) — zero-column blob | 🟡 trivial |

## The absence, concretely

| Source | Strength | Weakness |
|---|---|---|
| **NYC Open Data (2 assets)** | Open; `3fes-huds` gives a real request-type vocabulary | Aggregate only, stale (FY20); `mmut-uup9` is a blob. Nothing about land use, appointments, budget, or resolutions |
| **Weebly site** | Human-readable; publishes PDFs and a couple of intake forms | No API, no JSON, no iCal, no structured data; forms relay to Weebly with opaque field names; not agent-accessible |

## Implications for the API-first + MCP proposal

1. **Define the model that does not exist yet.** Give the BP's charter functions — land-use recommendations, community board appointments, discretionary awards, borough board resolutions, events — clean JSON Schemas ([schemas/](schemas/)) so there is a first machine-readable target.
2. **Federate, don't duplicate.** Keep `borough` citywide in the schema so **one shared Borough President API** ([OpenAPI](openapi/statenislandbp.yaml)) serves all five offices; this assessment instantiates Staten Island.
3. **Contract the two real transactions first.** `report_quality_of_life_issue` (BP Assist) and the net-new `apply_to_community_board`, replacing an opaque Weebly form.
4. **Reuse the one honest dataset.** Wire `3fes-huds`'s request-type dimension into `ConstituentRequest` as an aggregate read.
5. **MCP server** so an agent can answer "what did the BP recommend on this rezoning?", "who's on Community Board 2?", and — the point — "report this pothole" and "help me apply to my community board."
