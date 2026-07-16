# Making Affordable-Housing Permitting Programmable

*An [API Evangelist](https://apievangelist.com) brief for New York City — how to link the City's housing-permitting portals behind shared APIs, give builders and agencies live visibility into review status and queues, and make the whole cross-agency approval chain agent-native. Built on the [NYC Modernization](README.md) study and offered to inform the City's technology teams; not an official City document.*

Interactive: **[nyc.apievangelist.com](https://nyc.apievangelist.com)** · Strategy context: **[STRATEGY.md](STRATEGY.md)** · The workflow: **[experience/workflows/](experience/workflows/build-affordable-housing.arazzo.yaml)**

---

## The problem, stated plainly

Building one affordable apartment building in New York City means clearing **roughly forty distinct procedures and permits across about fifteen City agencies**, plus utilities and state/federal bodies — DCP, DOB, DEP, HPD, HDC, FDNY, DOT, DOF, LPC, PDC, MOER, DPR, and more. Each runs its own portal, its own form, its own queue, and its own status page. **None of them share a thread.** A builder — or the staffer shepherding a project — reassembles the picture by hand, portal by portal, and no one can see, in one place, *where a project is stuck or how long each queue really is.*

That is not a policy problem; it is an **integration** problem. And it is exactly the gap this study measured across all 70 City agencies: open data is broad, but the **service layer that ties agencies together does not exist** — [68 of 70 agencies have no transactional write API, and none is agent-ready](STRATEGY.md).

## What the moment calls for — and what already exists

Four capabilities keep coming up as the way to move faster. For each, the design-first artifact is **already drafted** in this repo — so the work starts at "implement," not "discover."

| The need | Already drafted here |
|---|---|
| **APIs that link the back-end data across the agencies' permitting portals** | Per-agency [OpenAPI contracts](README.md) for DOB, DEP, FDNY, DCP, DOT, DOF, HPD, HDC, LPC, PDC, MOER, DPR — plus the unified [experience OpenAPI](experience/nyc-openapi.json) that stitches all 70 into one surface. |
| **A shared spine so every agency composes around the *project/parcel*, not the org chart** | [`nyc-commons`](nyc-commons/README.md) — one canonical **BBL / address / borough / party / money** vocabulary, with all 69 consumer domains migrated to reference it. The join key the portals never shared. |
| **Live metrics on review timing and queue length; automated approval management across agencies** | The [**"Build Affordable Housing in NYC"** Arazzo workflow](experience/workflows/build-affordable-housing.arazzo.yaml) — the forty-permit journey as one machine-readable thread across twelve agencies — plus the [**"check application or case status"**](experience/skills/check-application-or-case-status.md) government-process skill (20 agencies) where status and queue are modeled read operations. |
| **A plain-language "what permits do I need" guide that is also machine-readable** | The [**"apply for a permit"**](experience/skills/apply-for-a-permit-license-or-benefit.md) skill and the `how_do_i_apply_for` MCP prompt — the same index, human-readable *and* callable by an agent. |

## The connective artifact: one workflow across twelve agencies

The single most useful new artifact is the **[affordable-housing Arazzo workflow](experience/workflows/build-affordable-housing.arazzo.yaml)** — an open [OpenAPI-Initiative standard](https://spec.openapis.org/arazzo/latest.html) description of the whole journey, gated on a project's shape (rezoning vs. as-of-right, City-owned vs. private, landmark, environmental designation, office conversion):

1. **Planning** — geocode the site (DCP) → parcel baseline (DOF) → land-use / ULURP (DCP) → environmental Notice to Proceed (MOER)
2. **Financing** — bond + subsidy financing (HDC) → HPD project record
3. **Permitting** — design review (PDC) → landmark Certificate of Appropriateness (LPC) → stormwater/SWPPP + asbestos (DEP) → building permit (DOB) → fire-alarm plan (FDNY) → curb/street work (DOT) → sewer/water connection (DEP) → tree sign-off (DPR)
4. **Lease-up** — Certificate of Occupancy (DOB) → Housing Connect lottery (HPD)

Everything flows on the parcel's **BBL**. This is precisely what "link the permitting portals and automate approval management across agencies" needs — expressed as a portable, versionable, testable open standard rather than yet another siloed portal. And the lottery/lease-up end already maps to HPD's modeled `HousingLotteryApplication`, ready for a Housing Connect successor system to implement against.

## Why this compounds

- **Vendor-independent by default.** Every proprietary tool in the City's housing stack has a [named open-source alternative](https://nyc.apievangelist.com/technology.html) in this study — so this can be built as a durable public good, not a new lock-in.
- **Agent-native, not just API-native.** The same contracts are exposed as an [installable MCP server](EXPERIENCE.md), so an AI assistant acting for a builder — "what permits does my project still need, and which queue is it stuck in?" — is a first-class consumer from day one.
- **Repeatable and forkable.** The method that produced the housing chain is the same [seven-step method](README.md) that covers all 70 agencies; the next cross-agency journey (open a restaurant, open a business) is the same pattern.

## What to do first

1. **Adopt the affordable-housing Arazzo workflow** as the reference map for cross-agency approval management — and implement it against the agencies' real endpoints as they come online.
2. **Make `nyc-commons` (BBL/address/party) the shared spine** every housing portal references, so status can be joined across agencies at all.
3. **Ship the status/queue read layer first** — the highest-leverage, lowest-controversy win: builders and staff seeing where every project sits, in one place.
4. **Draft the handful of still-missing writes** the workflow names honestly — a DOF tax-lot subdivision, a dedicated DEP SWPPP and asbestos submission, a DCP pre-certification write.
5. **Make an MCP surface a standard deliverable** so the whole chain is usable by agents, not just applications.

---
*Sources and further reading: [References](REFERENCES.md) · [Strategy](STRATEGY.md). Part of the [NYC Modernization](README.md) study. From [API Evangelist](https://apievangelist.com); offered to inform the City's technology teams, not an official City document.*
