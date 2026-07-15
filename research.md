# Research & Ideas — Using NYC Modernization Data to Solve Everyday Problems

*A working notebook. What can the [NYC Digital Modernization](README.md) data — 67 agencies assessed, the [citizen-transaction taxonomy](https://nyc.apievangelist.com/transactions.html), the [`nyc-commons`](https://nyc.apievangelist.com/commons.html) spine, and the [API → MCP → Agent-Skill experience layer](https://nyc.apievangelist.com/experience.html) — actually **do** for a New Yorker's everyday problems? This file collects ideas as they come. From [API Evangelist](https://apievangelist.com).*

---

## The prompt

Don Moynihan and Pamela Herd — the scholars who named **administrative burden** — [read the PIT Crew launch](https://donmoynihan.substack.com/p/mamdani-invests-in-tech-capacity) as something bigger than a tech office. In their words, and the Mayor's, it's about **delivering on core priorities — housing, childcare, consumer and worker protection — by improving the *experience* of government**:

> "Every confusing step and every dead-end portal makes it more difficult for government to deliver for New Yorkers, and for New Yorkers to trust that government is working to deliver for them. Every straightforward experience New Yorkers have on city platforms rebuilds that trust."

That is the everyday problem, named. Not a missing dataset — a **burden**. Herd & Moynihan break it into three costs a resident pays to get what they're entitled to:

- **Learning costs** — figuring out that a service exists, whether you qualify, and which of dozens of agencies and portals owns it.
- **Compliance costs** — the forms, documents, logins, and re-entry of the same facts across siloed systems.
- **Psychological costs** — the stress, stigma, and loss of trust from confusing, dead-end experiences.

**The thesis of this project, restated through their lens:** open data (2010–2018) made the city *readable*. It did nothing for burden. **APIs, MCP tools, and Agent Skills reduce all three costs** — because a copilot or agent that can *find the right agency, carry the resident's context across silos, and complete the transaction* is a burden-reduction machine. The 67-agency assessment is the map of where that burden lives; the [experience layer](https://nyc.apievangelist.com/experience.html) is the substrate for cutting it.

## How each layer cuts each cost

| Burden (Herd & Moynihan) | What cuts it | In this project |
|---|---|---|
| **Learning** — "who handles this, do I qualify?" | Discovery + routing | `find_agency_for_task`, the [APIs.json catalog](https://nyc.apievangelist.com/experience.html), and the 67-agency map so an agent answers "where do I even start?" |
| **Compliance** — forms, logins, re-entry | Write APIs + a shared identity/place spine | The **66 net-new write workflows** (permits, applications, complaints) + [`nyc-commons`](https://nyc.apievangelist.com/commons.html) `Place`/`Address` so a BBL or address is entered *once* and reused across agencies |
| **Psychological** — stress, dead-ends, distrust | Agent-native "experience" | The ten [government-process Agent Skills](https://nyc.apievangelist.com/experience.html) (apply, report, request-records, schedule, pay…) that finish the task instead of handing back a portal link |

## The article's priorities → buildable ideas

Each maps to agencies already assessed here, a modeled net-new **write** workflow, and a government-process **skill**.

### Childcare (affordability agenda)
- **Everyday problem:** a parent doesn't know childcare help exists, which program fits, or how to apply across three agencies.
- **In our data:** [DYCD](https://nyc.apievangelist.com/domain.html?d=dycd) (COMPASS / after-school), [ACS](https://nyc.apievangelist.com/domain.html?d=acs) (child-care vouchers, child welfare), [HRA](https://nyc.apievangelist.com/domain.html?d=hra) (child-care assistance via ACCESS HRA).
- **Idea — "One childcare front door":** an *Apply* skill that takes a family's situation once (income, children, ZIP → `nyc-commons` geography), checks eligibility across DYCD/ACS/HRA, and starts the single best application — collapsing three learning-cost mazes into one conversation.

### Housing (the flagship "reduce burden to build faster")
- **Everyday problem (resident):** the affordable-housing lottery is a bewildering per-project application. **(builder):** permitting delay is itself an administrative burden that slows housing supply.
- **In our data:** [HPD](https://nyc.apievangelist.com/domain.html?d=hpd) (net-new `HousingLotteryApplication`), [NYCHA](https://nyc.apievangelist.com/domain.html?d=nycha), [DOB](https://nyc.apievangelist.com/domain.html?d=dob) (net-new `PermitApplication` fronting the BIS/DOB NOW legacy app layer), [DCP](https://nyc.apievangelist.com/domain.html?d=dcp) (land use).
- **Idea — lottery copilot:** an *Apply* skill that carries one Housing Connect profile across every lottery a household is eligible for (compliance cost → near-zero).
- **Idea — permit status agent:** front DOB's browser-only BIS/DOB NOW with a read API + `check_application_or_case_status` skill so a builder (or their agent) gets status without the portal — the "reduce administrative burden to build housing" the Mayor named.

### Consumer & worker protection (the first PIT Crew, "Click to Cancel")
- **Everyday problem:** filing a complaint against a company that traps you in a subscription — exactly [crew #1's DCWP portal](https://donmoynihan.substack.com/p/mamdani-invests-in-tech-capacity).
- **In our data:** [DCWP](https://nyc.apievangelist.com/domain.html?d=dcwp) is already assessed; the complaint is a modeled net-new write; the **report-a-problem** skill + reference API + MCP already exist.
- **Idea — fork the DCWP complaint contract** as crew #1's starting point (see the [strategy](https://nyc.apievangelist.com/strategy.html)); the *Report* skill turns "which agency, which form?" into one sentence.

### 311 & potholes (the "nuts and bolts" the Mayor is spending capital on)
- **Everyday problem:** reporting a pothole/noise/condition means knowing it's 311, picking the right service type, and re-describing the location.
- **In our data:** [NYC311](https://nyc.apievangelist.com/domain.html?d=nyc311) (revive **Open311** — the standard NYC pioneered and retired; net-new `ServiceRequest`), [DOT](https://nyc.apievangelist.com/domain.html?d=dot) (street work).
- **Idea — Open311 revival + report skill:** one *Report* skill that classifies the problem, attaches a `nyc-commons` location, and files the service request — the pothole call, minus the maze.

### Benefits & affordability (SNAP, cash, Medicaid)
- **Everyday problem:** highest-burden of all — eligibility is opaque, forms are long, and stigma is real.
- **In our data:** [HRA](https://nyc.apievangelist.com/domain.html?d=hra) (net-new `BenefitsApplication`, today locked in ACCESS HRA).
- **Idea — benefits screener → application:** an *Apply* skill that screens eligibility conversationally (learning + psychological cost) and starts the application with fields pre-filled from the shared profile (compliance cost).

## Ten ideas, in one list

1. **"Where do I start?" router** — one `find_agency_for_task` skill over all 67 agencies; the antidote to learning cost.
2. **One childcare front door** across DYCD / ACS / HRA.
3. **Housing-lottery copilot** — one profile, every HPD lottery.
4. **DOB permit-status agent** — front the legacy app layer; the "build housing faster" burden cut.
5. **Fork the DCWP "Click to Cancel" complaint** as the reference *Report* build.
6. **Open311 revival** + a citywide *Report* skill for 311/potholes.
7. **Benefits screener → application** for SNAP/cash/Medicaid.
8. **"What's at this address?"** — resolve a `nyc-commons` `Place` and fan out across Buildings, Housing, Environment, complaints (learning cost for renters/owners).
9. **"Who represents this block?"** — the geography-spine prompt as a civic-literacy tool.
10. **A burden scorecard** — extend the [assessment](https://nyc.apievangelist.com/synthesis.html) with a per-service *administrative-burden* rating (learning / compliance / psychological), ranking where a PIT Crew cuts the most burden per build.

## Why this is the same argument, sharper

The [assessment](https://nyc.apievangelist.com/synthesis.html) already proved the structural gap: **65 of 67 agencies have no transactional write API, and all 67 have no agent surface.** Read through Herd & Moynihan, that gap *is* administrative burden made measurable. The [experience layer](https://nyc.apievangelist.com/experience.html) — every operation mapped to an MCP tool and a government-process skill — is the tool for paying it down. PIT Crew is the team to spend it.

## The everyday problems, diagnosed: OSC's "Caucus 2025" report library

The NY State Comptroller publishes **[Caucus 2025: Important Information for New Yorkers](https://www.osc.ny.gov/reports/caucus2025)** — ~40 reports that are, in effect, a catalog of New Yorkers' everyday problems, with the data behind each. They pair perfectly with this project: **OSC diagnoses the problem; the modernization layer (agencies → APIs → MCP → Skills) is the delivery mechanism.** Strikingly, many name the exact agencies and datasets this assessment covers — including several the [Excel sweep](https://nyc.apievangelist.com/technology.html) just surfaced (DOE attendance, DHS shelter LL34, DFTA senior-center LL140, NYPD collisions).

### The library, grouped by everyday problem

**Children, youth & education** — [Chronic Absenteeism](https://www.osc.ny.gov/files/reports/pdf/missing-school-ny-chronic-absenteeism.pdf) · [Academic Recovery / "Nation's Report Card"](https://www.osc.ny.gov/reports/nations-report-card-underscores-new-yorks-need-academic-recovery) · [Higher Ed Competitiveness](https://www.osc.ny.gov/files/reports/pdf/higher-education-nys.pdf) · [Higher Ed Economic Impact](https://www.osc.ny.gov/files/reports/pdf/higher-education-economic-impact.pdf) · [Children in Poverty](https://www.osc.ny.gov/files/reports/pdf/nys-children-in-need.pdf) · [Child Care Sector Challenges](https://www.osc.ny.gov/files/reports/pdf/child-care-challenges.pdf)

**Housing & homelessness** — [Homeownership Rates](https://www.osc.ny.gov/files/reports/pdf/homeownership-rates-in-ny.pdf) · [Housing Insecurity Crisis](https://www.osc.ny.gov/files/reports/pdf/new-york-housing-insecurity.pdf) · [Homelessness in NYS](https://www.osc.ny.gov/files/reports/pdf/new-yorkers-in-need-homelessness-nys.pdf) · [Veteran Homelessness](https://www.osc.ny.gov/files/reports/osdc/pdf/reductions-in-homelessness-among-new-yorks-veterans.pdf) · [Housing Discrimination Complaints (DHR audit)](https://www.osc.ny.gov/files/state-agencies/audits/pdf/sga-2025-23s26.pdf) · [Cost of Living in NYC: Housing](https://www.osc.ny.gov/files/reports/osdc/pdf/report-17-2024.pdf)

**Food security & income** — [Food Insecurity & Nutrition Assistance](https://www.osc.ny.gov/files/reports/pdf/new-yorkers-in-need-food-insecurity.pdf) · [Food Insecurity Post-Pandemic](https://www.osc.ny.gov/files/reports/pdf/food-insecurity-persists-post-pandemic.pdf) · [Poverty, Housing & Food Insecurity](https://www.osc.ny.gov/files/reports/pdf/new-yorkers-in-need.pdf) · [Social Insurance Programs: Benchmarking Benefits](https://www.osc.ny.gov/files/reports/pdf/social-insurance-programs.pdf)

**Health & public safety** — [Drug Overdose Deaths](https://www.osc.ny.gov/reports/continuing-crisis-drug-overdose-deaths-new-york) · [Domestic Violence Trends](https://www.osc.ny.gov/files/reports/pdf/domestic-violence-recent-trends-10-23.pdf) · [Mental Health Inpatient Capacity](https://www.osc.ny.gov/files/reports/pdf/mental-health-inpatient-service-capacity.pdf) · [Traffic Fatalities Growing](https://www.osc.ny.gov/files/reports/pdf/traffic-fatalities-are-growing-in-new-york-state.pdf) · [Growth of Hate Crimes](https://www.osc.ny.gov/reports/concerning-growth-hate-crime-new-york-state) · [MTA Subway Safety Equipment (audit)](https://www.osc.ny.gov/files/state-agencies/audits/pdf/sga-2024-22s20.pdf)

**Older adults** — [Elder Care Program Audits](https://www.osc.ny.gov/files/reports/pdf/select-elder-care-program-audits-2021-2023.pdf) · [Older Adults in NYC: Demographic & Service Trends](https://www.osc.ny.gov/files/press/pdf/report-22-2025.pdf)

**Economy, work & business** — [Where Do New Yorkers Work?](https://www.osc.ny.gov/files/reports/pdf/where-nyers-work.pdf) · [NYS Business Owners](https://www.osc.ny.gov/files/reports/pdf/business-owners-in-new-york-state.pdf) · [Role of Nonprofits](https://www.osc.ny.gov/files/reports/pdf/critical-role-of-nonprofits-in-new-york.pdf) · [MWBE Strategy](https://www.osc.ny.gov/files/reports/special-topics/pdf/mwbe-fiscal-2022-23.pdf) · [Doing Business With NYS](https://www.osc.ny.gov/files/procurement/pdf/doing-business-nys.pdf) · [Foreign-Born in the Workforce](https://www.osc.ny.gov/files/reports/osdc/pdf/report-20-2024.pdf) · [Post-Pandemic Travel](https://www.osc.ny.gov/files/reports/pdf/welcome-back-to-ny-an-analysis-of-post-pandemic-travel.pdf) · [Agriculture in NYS](https://www.osc.ny.gov/files/reports/pdf/profile-of-agriculture-in-nys.pdf)

**Infrastructure & digital access** — [Cost of Living in NYC: Transportation](https://www.osc.ny.gov/files/reports/pdf/report-16-2025.pdf) · [Broadband Availability, Access & Affordability in NYC](https://www.osc.ny.gov/files/reports/pdf/report-20-2025.pdf) · [MTA Financial Outlook](https://www.osc.ny.gov/files/reports/osdc/pdf/report-17-2025.pdf)

**NYC fiscal & workforce** — [Review of the Financial Plan of the City of NY](https://www.osc.ny.gov/files/reports/osdc/pdf/report-21-2025.pdf) · [NYC Staffing Trends](https://www.osc.ny.gov/files/reports/osdc/pdf/report-2-2025.pdf) · plus OSC's own fiscal oversight ([2025 Year in Review](https://www.osc.ny.gov/reports/2025-year-in-review), [ACFR](https://www.osc.ny.gov/reports/finance#acfr), [Budget Analysis](https://www.osc.ny.gov/reports/new-york-state-budget-analysis-and-financial-reporting)).

### Diagnosis → data we hold → idea

| OSC problem | NYC agencies & data in this project | Delivery |
|---|---|---|
| Chronic absenteeism, children in poverty | [DOE](https://nyc.apievangelist.com/domain.html?d=schools.nyc.gov) attendance data (swept Excel), [ACS](https://nyc.apievangelist.com/domain.html?d=acs), [DYCD](https://nyc.apievangelist.com/domain.html?d=dycd) | *check-status* + *find-services* skills; an early-warning + connect-to-support agent |
| Housing insecurity, homelessness, discrimination | [HPD](https://nyc.apievangelist.com/domain.html?d=hpd), [NYCHA](https://nyc.apievangelist.com/domain.html?d=nycha), [DHS](https://nyc.apievangelist.com/domain.html?d=dhs) shelter LL34 (swept), [CCHR](https://nyc.apievangelist.com/domain.html?d=cchr) | *Apply* (lottery/benefits) + *Report* (discrimination) skills |
| Food insecurity, income support | [HRA](https://nyc.apievangelist.com/domain.html?d=hra) (SNAP/cash) | *Apply* skill: screen → apply, fields pre-filled |
| Overdose, domestic violence, mental health | [DOHMH](https://nyc.apievangelist.com/domain.html?d=dohmh), [HHC](https://nyc.apievangelist.com/domain.html?d=hhc) | *find-services-near-me* + `nyc://place` resources |
| Traffic fatalities (Vision Zero) | [DOT](https://nyc.apievangelist.com/domain.html?d=dot), [NYPD](https://nyc.apievangelist.com/domain.html?d=nypd) collision data (swept Excel) | *Report* + a dangerous-corridor lookup |
| Hate crime | [NYPD](https://nyc.apievangelist.com/domain.html?d=nypd), [CCHR](https://nyc.apievangelist.com/domain.html?d=cchr) | *Report* skill with routing |
| Elder care, older adults | [DFTA](https://nyc.apievangelist.com/domain.html?d=dfta) senior-center LL140 (swept), HRA | *find-services* / *Apply* for older adults |
| MWBE, doing business, nonprofits | [SBS](https://nyc.apievangelist.com/domain.html?d=sbs), [EDC](https://nyc.apievangelist.com/domain.html?d=edc), [Comptroller](https://nyc.apievangelist.com/domain.html?d=comptroller.nyc.gov) | *Register* + an OCDS-standard procurement copilot |
| Broadband access | [OTI](https://nyc.apievangelist.com/domain.html?d=oti) | a broadband/affordability *look-up* by `nyc-commons` geography |

### More ideas, from the reports

11. **Absenteeism early-warning + support agent** — over DOE attendance data, flag a student's risk and connect the family to the right program (learning + psychological cost, in a Herd & Moynihan frame).
12. **"What's happening on my block" needs layer** — join the OSC neighborhood diagnoses (food access, overdose, traffic-fatality corridors) to a `nyc-commons` `Place`, so an agent answers *what applies here and what can I do about it*.
13. **Vision Zero agent** — over DOT/NYPD collision data (swept), surface dangerous corridors and file a *Report* for a specific hazard.
14. **Elder-care navigator** — DFTA senior-center + HRA, an *Apply/Find* skill for older adults and caregivers.
15. **Shelter & homelessness navigation** — over DHS LL34 shelter data (swept), find shelter/services and check status.
16. **MWBE & procurement copilot** — help a small or M/WBE business find and bid on city work (adopt **OCDS**), turning "doing business with the city" from a maze into a guided *Register/Apply*.
17. **State-report → city-service bridge** — the meta-idea: for each OSC report, map the diagnosis to the city agency, dataset, and the write workflow that acts on it — a standing rubric so every "New Yorkers in Need" report has a matching *build*.

## Observations from the field

*Specific things noticed while browsing the city's digital surface — the low-hanging fruit, logged as it's found.*

### "Summer in NYC" runs on a vendor Airtable form + a static CSV (2026-07-14)

The Mayor's Office **[Summer in NYC](https://www.nyc.gov/content/summer/pages/)** page is a custom React/Vite single-page app (`/assets/summer/builds/…/index.js`) with **Esri ArcGIS** for the map and **Google Translate**. Two data findings:

- **A real activities dataset, shipped as a flat file.** The app loads **`/assets/summer/data/activities.csv`** — a ~**570 KB** machine-readable CSV of summer activities/programs citywide. It's data, but a static one-way dump: no query, no filter-by-neighborhood, no API. Classic *Digitize→Expose* fruit — it should be a **Summer Activities API** (searchable by `nyc-commons` geography) with an MCP tool like `find_summer_activities_near_me`.
- **An embedded Airtable form is a shadow submission API.** The app embeds an **Airtable** form — base `appqq43uA2duSk0oM` (`https://airtable.com/appqq43uA2duSk0oM/…/form`) — almost certainly how organizations submit a summer activity. **Airtable is a commercial low-code database with a full REST API**, so the city already has a programmatic intake here — it's just **vendor-hosted and ungoverned** (an open-source path would be **Baserow / NocoDB / Grist**). The API-first move is *Expose + Own*: front the submission with a **city-owned `Register`/`Submit` write API** (the same *register-or-enroll* government-process skill), and treat the Airtable base as the backing store, not the public contract.

**Why it matters:** this is the whole project in one page — real data trapped in a CSV, a real transaction trapped in a vendor form, and no owned API or agent surface over either. It also confirms a pattern worth a dedicated sweep: **find every embedded Airtable / Google / Typeform / JotForm across `nyc.gov` — each is a form that should be a city-owned write API.** (Added to the backlog.)

---
*Sources & further reading: **[References](https://nyc.apievangelist.com/references.html)**. A living document — ideas and field notes added as they come. Part of the [NYC Digital Modernization](README.md) study.*
