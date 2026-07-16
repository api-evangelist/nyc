# Why This Work Matters — New York's Moment to Lead

*A strategic case for the NYC Modernization project as the substrate for the Public Interest Technology (PIT) Crew — and for New York setting the standard other cities fork. From [API Evangelist](https://apievangelist.com); offered to inform the PIT Crew, not an official City document.*

Interactive: **[nyc.apievangelist.com/strategy.html](https://nyc.apievangelist.com/strategy.html)**. Sources: **[References](https://nyc.apievangelist.com/references.html)**.

---

## The moment

On **July 13, 2026**, Mayor Zohran Mamdani and CTO / OTI Commissioner Lisa Gelobter launched the **[Public Interest Technology (PIT) Crew](https://www.nyc.gov/content/pitcrew/pages/)** — five teams of product managers, designers, engineers, user researchers, and data experts embedded in agencies to **["Rapidly Build Digital Solutions to Public Problems,"](https://www.nyc.gov/mayors-office/news/2026/07/mayor-mamdani-launches--public-interest-technology--pit--crew--t)** moving "from idea to implementation in a matter of months" instead of years. The first crew builds a **DCWP** complaint portal enforcing the nation's first "Click to Cancel" protections.

This project exists to make that speed possible — and repeatable across all 70 agencies.

## The argument in one sentence

**A PIT Crew should never start from a blank page.** For every NYC agency, the resource models, API contracts, agent tools, and the *exact missing write workflows* are already drafted — design-first, open-source, and forkable — so a Crew starts at "implement," not "discover."

## This is a fifteen-year argument, now proven

API Evangelist has made this case since 2011. The NYC assessment is the evidence.

- **2011 — [Every City, County, and State Should Have an API](https://apievangelist.com/2011/09/06/every-city-county-and-state-should-have-an-api/).** The problem was never bureaucracy; it's the vendor tooling agencies are handed (Tyler/Munis, and later Socrata). *"PDF is not Portable Data Format… we need to expect more out of the technology purchased with our tax dollars."*
- **2012 — [APIs Can Save Money and Make Government More Efficient](https://apievangelist.com/2012/10/25/apis-can-save-money-and-make-government-more-efficient/).** The Department of Energy estimated **$882,000** saved by bundling one API with a study.
- **2013 — [The Next Iteration of Government Data](https://apievangelist.com/2013/07/16/the-next-iteration-of-government-data/).** Do it *"agency by agency, project by project,"* with an open, collaborative, forkable process on GitHub.
- **2013 — [A Huge Need for Writeable APIs in Government](https://apievangelist.com/2013/09/25/a-huge-need-for-writeable-apis-in-government/).** *"There isn't much in the wild… huge demand… this could be the thing that changes how government operates."* The write-layer gap, called thirteen years ago.

The through-line: the **open-data era (2010–2018) only half-worked.** It published *reporting* data and never touched the *transaction*. That unfinished half — the write layer and now the agent layer — is exactly what the PIT Crew is chartered to finish.

## The evidence (not opinion)

The [assessment](SYNTHESIS.md) ran the identical outside-in method across **70 agencies** ([69/70 re-verified](https://nyc.apievangelist.com/qa.html)) and found **two columns flat across the entire city**:

| Capability | Result |
|---|---|
| Transactional **write** API | **68 of 70 agencies score zero** — the citizen action has no API |
| **Agent** readiness | **70 of 70 score zero** — no agency is agent-native |
| Vendor independence | Median agency stack is **71% proprietary** — yet an [open-source alternative exists for all 62 commercial tools](https://nyc.apievangelist.com/technology.html) |

The service layer, not the data, is the universal gap — the same finding, now measured across a whole city instead of asserted in a blog post.

## Directly addressing the PIT Crew's objectives

| PIT Crew objective (their words) | What this project already provides |
|---|---|
| **"Rapidly build" / "months, not years"** | A design-first contract per agency: JSON Schema → OpenAPI → MCP → Agent Skill. The Crew forks the contract and implements against it. |
| **First crew: DCWP "Click to Cancel" complaint portal** | [DCWP is already assessed](https://nyc.apievangelist.com/domain.html?d=dcwp); the complaint is a modeled **net-new write workflow**; the **"report-a-problem-or-file-a-complaint"** government-process skill, plus a reference API and installable MCP, already exist. A worked head start for crew #1. |
| **"Digital public goods… in-house"** | Everything is open-source and **vendor-independent**, with a named OSS alternative for every proprietary incumbent. |
| **"Dignified and delightful for every New Yorker"** | One shared **[nyc-commons](https://nyc.apievangelist.com/commons.html)** geography/identity spine plus agent-native surfaces, so services compose around the *resident* — not the org chart. |
| **Five crews, many agencies** | A repeatable **seven-step method** and open generators — not five bespoke starts from scratch. |

## How New York leads other cities

NYC can author the pattern every other city forks. Publish three things:

1. **Standards** — [`nyc-commons`](https://nyc.apievangelist.com/commons.html) (the shared geography/identity spine), an [APIs.json](https://apisjson.org) catalog of the civic surface, the [ten common government-process skills](https://nyc.apievangelist.com/experience.html), and the design-first chain.
2. **Tooling** — the [experience layer](https://nyc.apievangelist.com/experience.html), the callable reference API, the installable MCP (`@api-common/nyc-mcp`), and the open generators.
3. **Processes** — the outside-in assessment method and the whole repository, forkable as a **civic API kit**. Watertown, Philadelphia, any city clones it and runs its own assessment.

The open-data era *did* have a standard — but it was a **vendor's** (Socrata/SODA). This time the standard is **open, forkable, and agent-native**, and New York authors it. That is the difference between publishing data and leading a movement.

## What to do next — the ask

1. **Fork the DCWP complaint contract** as crew #1's starting point.
2. **Adopt `nyc-commons`** as the citywide geography/identity spine.
3. **Register every agency in an APIs.json catalog** — the connective tissue open data never had.
4. **Make an MCP surface a standard deliverable** for every PIT Crew build.
5. **Require an open-source-alternative assessment** for every new proprietary purchase.
6. **Publish the kit** so other cities fork it — NYC as the reference city.

---
*Sources and further reading: **[References](https://nyc.apievangelist.com/references.html)**. Part of the [NYC Modernization](README.md) study.*
