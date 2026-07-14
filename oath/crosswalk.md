# Crosswalk — Website/Portal Fruit ↔ APIs ↔ NYC Open Data (OATH)

Maps the low-hanging fruit on **nyc.gov/site/oath** and the **ECB Ticket Finder** portal to (a) the **existing APIs** (Socrata SODA; the Struts portal) and (b) the **2 OATH datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-oath.json](opendata-oath.json).

## The reframe — the "already-open data, locked response" pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, every transaction locked in an Oracle **Siebel** CRM → *unlock the service layer.*
- **OATH:** the **adjudication data is already wide open** (2 Socrata datasets, one huge and daily), but the one thing a respondent must do — **respond to a summons** — is locked inside a legacy **Apache Struts / Oracle WebLogic** portal with no API → **let respondents *respond*.**

Like NYCHA, OATH inverts the usual problem. It is not that the data is trapped in HTML — every summons, charge, hearing, decision, penalty, and balance is machine-readable on Open Data, refreshed daily. It is that the thing a respondent *does* — look up a summons and **dispute it, request a hearing, submit a defense, reopen a default** — lives only behind a `.action` Struts form, mail, or an in-person visit. A respondent or agent asking "how do I contest this ticket?" has no API to call.

Coverage: ✅ strong open twin · 🟡 partial · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Portal | API today | Open Data | Cov. |
|---|---|---|---|---|
| `Summons` | ECB Ticket Finder lookup | SODA | Hearings Division Case Status (`jz4z-kudi`, 74c, daily) | ✅ |
| `Hearing` | `/hearings/hearings-and-defaults` | SODA | Hearing Date/Time, Status, Scheduled Location, Result in `jz4z-kudi` | ✅ |
| `Decision` | `/hearings/payments-penalties` | SODA | Hearing Result, Decision Date, Penalty Imposed, Judgment Docketed, Balance Due in `jz4z-kudi` | ✅ |
| `TrialCase` | `/site/oath` | SODA | Trials Division Case Status (`y3hw-z6bm`, 16c, monthly) | ✅ |
| Summons lookup | ECB Ticket Finder | **Struts UI only** | (data exists in `jz4z-kudi`, but no respondent-lookup API) | 🟡 |
| **`SummonsDispute`** (respond / dispute / request hearing) | ECB Ticket Finder + mail/in person | **Struts UI / mail only** | — | ❌ **net-new** |
| Reopen a default | `/hearings/reopen-a-missed-hearing-default-online` | **Struts UI only** | — | ❌ gap |
| Pay a penalty | Payments page → Dept. of Finance | **DOF, no OATH API** | — | ❌ gap |

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (2 datasets)** | Open, machine-readable; the flagship Hearings Division dataset is 74 columns, updated **daily**, ~400k views — every summons, charge, hearing, decision, penalty, balance | Only 2 datasets; read-only snapshots of *closed/decided* state; nothing a respondent can act through |
| **ECB Ticket Finder (Struts/WebLogic)** | The real transaction system — look up a summons and respond to it | Legacy `.action` server-rendered forms; no API, no OpenAPI, no JSON; not agent-accessible; mail/in-person are the fallbacks |

## Implications for the API-first + MCP proposal

1. **Publish the open case-status data as one clean resource model.** Summonses, hearings, decisions, and trial cases behind one owned OATH contract ([OpenAPI](openapi/oath.yaml)) — so consumers learn one model, not two Socrata IDs and a 74-column flat file.
2. **Let respondents respond.** Front the Struts portal with an API so the core transaction — **responding to / disputing a summons and requesting a hearing** — has a machine-readable, agent-native contract.
3. **Add the one net-new write workflow** — `dispute_summons` (create a `SummonsDispute`), with `requestType` covering dispute / request hearing / adjourn / reschedule / **reopen default** / admit-and-pay.
4. **Keep the issue/pay boundaries honest.** OATH adjudicates but does not issue summonses (DOB/DSNY/FDNY/DOHMH/DEP/DCWP do) and does not collect judgments (the Department of Finance does); the API scopes to *responding*.
5. **MCP server** so an agent can answer "what's the status of ticket #…?", "what were the charges and the penalty?", and — the point — "dispute this summons and request an online hearing."
