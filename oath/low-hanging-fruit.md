# Low-Hanging Fruit Index — OATH

**Agency:** NYC Office of Administrative Trials & Hearings (OATH)
**Assessed:** 2026-07-13
**Method:** Outside-in crawl (browser UA, respecting robots.txt — `nyc.gov/robots.txt` only disallows `/html/misc/`). Fingerprinted the informational site `nyc.gov/site/oath` (Akamai + nginx + NYC.gov "Livesite" v22 + Dynatrace) and the **ECB Ticket Finder / Respond-to-a-Summons portal** at `a820-ecbticketfinder.nyc.gov/searchHome.action`, identified as **Apache Struts 2 on Oracle WebLogic** (`.action` routing, `X-ORACLE-DMS-ECID`, WebLogic `JSESSIONID`, ISO-8859-1). Verified the NYC Open Data agency label `Office of Administrative Trials and Hearings (OATH)` via the Socrata Discovery API and pulled both assets with column schemas.

Companion artifacts: [tech-stack.md](tech-stack.md), [apis-observed.md](apis-observed.md), [crosswalk.md](crosswalk.md), [opendata-oath.md](opendata-oath.md).

## Headline findings

1. **OATH is a split domain.** An informational site on the shared NYC.gov chassis, and the **ECB Ticket Finder** (`a820-ecbticketfinder.nyc.gov`) running **Apache Struts on Oracle WebLogic** with **no API**.
2. **The adjudication data is exceptionally open.** The flagship **OATH Hearings Division Case Status** (`jz4z-kudi`, 74 columns, updated **daily**, ~400k views) publishes essentially the entire ECB summons docket — charges, respondent, violation location, hearing, decision, penalty, and balance — plus **OATH Trials Division Case Status** (`y3hw-z6bm`) for the tribunal side.
3. **But the response layer is locked.** Looking up and **responding to a summons** — dispute it, request or reschedule a hearing, submit a defense, reopen a default — the thing a respondent actually *does*, lives only inside a legacy Struts portal, by mail, or in person. None has a machine-readable contract.
4. **OATH adjudicates; it does not issue or collect.** Summonses come from DOB/DSNY/FDNY/DOHMH/DEP/DCWP and others; unpaid decisions become docketed judgments collected by the Department of Finance.

> **Reframe:** Parks = *replatform* a legacy site; DOE = *reclaim* rented search + a hidden backend; Council = *consolidate + own* three fragmented APIs; NYCHA = *unlock* a Siebel-locked service layer; **OATH = let respondents *respond*.** Here the data is already wide open — the work is least about liberating datasets and most about giving the **respondent transaction** (above all, disputing a summons and requesting a hearing) an owned, agent-native API instead of a legacy Struts form.

## The fruit

| # | Name | Entity | Where the data lives | Open Data twin |
|---|---|---|---|---|
| 1 | ECB Summonses (Hearings Division) | `Summons` | SODA | ✅ Hearings Division Case Status (`jz4z-kudi`, 74c, daily) |
| 2 | Hearings & Defaults | `Hearing` | SODA | ✅ hearing fields in `jz4z-kudi` |
| 3 | Decisions, Penalties & Payments | `Decision` | SODA | ✅ decision/penalty fields in `jz4z-kudi` |
| 4 | OATH Trials Division Cases | `TrialCase` | SODA | ✅ Trials Division Case Status (`y3hw-z6bm`, 16c) |
| 5 | Look up a summons | `Summons` | Struts portal | 🟡 data in `jz4z-kudi`, no lookup API |
| 6 | **Respond to / dispute a summons** | `SummonsDispute` | Struts portal + mail | ❌ **net-new** |
| 7 | Reopen a missed hearing (default) | `SummonsDispute` | Struts portal | ❌ gap (no API) |

## APIs & vendors observed (see [apis-observed.md](apis-observed.md), [tech-stack.md](tech-stack.md))

- **Socrata SODA** — 2 OATH datasets (the one real, open API; case-status data only, one file huge and daily).
- **Apache Struts / Oracle WebLogic** — the ECB Ticket Finder; server-rendered `.action` forms, no API.
- Platform: informational site on the **NYC.gov shared "Livesite" platform** (Akamai edge, nginx, Dynatrace RUM) — the same chassis as Parks/DOE/Council/NYCHA; OATH's distinct stack is the legacy Struts portal.

## Reverse-engineered entities

`Summons` (ECB ticket) · `Hearing` · `Decision` (disposition/penalty) · `TrialCase` · `SummonsDispute` (net-new write; also stands in for the Struts-locked reopen-default / adjournment / reschedule transactions) — with the sub-objects `Respondent`, `Charge`, and `ViolationLocation`; join key **Ticket Number** (and **Case Number** for the Trials Division).

## Next

1. **JSON Schema** per entity, reconciling real Open Data column names (Ticket Number, the ten Charge #N sets, Violation Location Borough/Block/Lot, decision/penalty fields) — done ([schemas/](schemas/)).
2. **OpenAPI** publishing the open case-status data as clean resources + the net-new `POST /summons-disputes` (respond to / dispute a summons) — done ([openapi/oath.yaml](openapi/oath.yaml)).
3. **MCP** artifact: `find_summonses`, `get_summons`, `get_summons_hearing`, `get_summons_decision`, `find_trial_cases`, `get_trial_case`, `list_my_disputes`, `get_dispute_status`, `dispute_summons` — done ([mcp/oath-mcp.json](mcp/oath-mcp.json)).
