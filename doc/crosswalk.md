# Crosswalk — Website/Lookup Fruit ↔ APIs ↔ NYC Open Data (DOC)

Maps the low-hanging fruit on **nyc.gov/site/doc** and the **Inmate Lookup Service** to (a) the **existing APIs** (Socrata SODA; the JSF lookup) and (b) the **15 DOC datasets** on NYC Open Data. Built 2026-07-13 from [fruit.json](fruit.json) × [opendata-doc.json](opendata-doc.json).

## The reframe — fifth distinct pattern

- **Parks:** data-rich HTML on a legacy platform → *replatform + unify.*
- **DOE:** data-rich, search rented to a vendor, backend hidden → *reclaim + unify.*
- **Council:** the data already has three APIs, none owned → *consolidate + own.*
- **NYCHA:** reference data wide open, service layer locked in a vendor CRM → *unlock.*
- **DOC:** accountability data **wide open** (15 datasets) **and** a **live custody lookup already running** — but the lookup is a legacy JSF screen with no API, and the public transactions (visit, complaint) have no digital surface → **expose the live lookup and the missing writes.**

DOC is the transparency-heavy, transaction-poor case. It is not that the data is trapped in HTML — the in-custody population, incidents, and security indicators are all machine-readable on Open Data. And unlike the earlier domains, DOC even runs a **live, real-time person-in-custody lookup**. But that lookup is a browser-only JavaServer Faces app, and the two things the public needs to *do* — **visit** someone in custody and **file a complaint / records request** — have no API, no Open Data twin, and no status contract. A person or agent asking "is my relative in custody, and can I book a visit?" can neither call the lookup nor schedule the visit.

Coverage: ✅ strong open twin · 🟡 partial/aggregate · ❌ gap (no API).

## Entity crosswalk

| Entity | Website / Lookup | API today | Open Data | Cov. |
|---|---|---|---|---|
| `PersonInCustody` | Inmate Lookup ("P.I.C. Lookup") | **SODA** (snapshot) / **JSF UI only** (live) | Daily Inmates In Custody (`7479-ugqb`, 13c); Admissions (`6teu-xtgp`); Discharges (`94ri-3ium`) | 🟡 open snapshot; live lookup has no API |
| `Facility` | `/about/facilities` | — | derived from `FACILITY` dimension across incident datasets; no roster dataset | 🟡 derived |
| `DailyPopulation` | — | SODA | Local Law 33 Security Indicators (`2wuc-x56b`); Article 730 Waitlist (`q9w2-yi4x`); Medical Non-production (`5n4h-km5r`); LL85 Visitation (`b3eu-nmy6`) | ✅ |
| `IncidentReport` | — | SODA | Deaths (`f64t-5yiv`), Slashing/Stabbing (`gakf-suji`), Fights (`k548-32d3`), Assault on Staff (`erra-pzy8`), Staff Injuries (`7hi3-kaps`), Lock-In (`9dab-x6kn`) | ✅ |
| **`Visit`** (schedule a visit) | Visiting pages + vendor portal | **offline / vendor only** | Local Law 85 Visitation (`b3eu-nmy6`) — **aggregate only** | ❌ **net-new** |
| **`Complaint`** (complaint / records request) | OpenRecords portal + phone/mail | **offline / portal only** | — | ❌ **net-new** |

Remaining datasets — Aggregate Employee Statistics (`eddp-3v5g`) and DOC Hart Island Burial Records (`f5mc-f3zp`) — sit alongside as workforce and DOC-administered burial accountability, folded under the indicators / person families.

## The mismatch, concretely

| Source | Strength | Weakness |
|---|---|---|
| **Socrata SODA (15 datasets)** | Open, machine-readable; unusually strong accountability corpus — custody snapshot, admissions/discharges, six incident streams, security indicators | Anonymized snapshots and aggregates only; nothing about live named lookup or public transactions |
| **Inmate Lookup ("P.I.C. Lookup")** | The real, live person-in-custody search keyed on NYSID / Book & Case / name | Legacy JavaServer Faces web app; postback/view-state, JavaScript-only; no API, no OpenAPI, no JSON; not agent-accessible |
| **Public transactions** | Visiting and complaint/records workflows are documented on the site | Phone/mail/in-person or vendor/OpenRecords portals; no API, no status, no Open Data twin |

## Implications for the API-first + MCP proposal

1. **Publish the open accountability data as one clean resource model.** People in custody, facilities, daily population/indicators, and incidents behind one owned DOC contract ([OpenAPI](openapi/doc.yaml)) — so consumers learn one model, not 15 Socrata IDs.
2. **Expose the live lookup.** Front the JSF "P.I.C. Lookup" with an API so a real-time person-in-custody search — by NYSID, Book & Case number, or inmate id — has a machine-readable, agent-native contract.
3. **Add the net-new write workflows** — `schedule_visit` (VisitScheduling) and `file_complaint` (complaint / records / FOIL request), each returning a tracking number and a status.
4. **Treat person-in-custody data as sensitive.** Named lookup and visit/complaint records are handled under access controls; the accountability datasets stay anonymized/aggregate as published.
5. **MCP server** so an agent can answer "how many stabbings at GRVC this year?", "what is the average daily population?", and — the point — "is this person in custody, and schedule a visit."
