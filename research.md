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

---
*Sources & further reading: **[References](https://nyc.apievangelist.com/references.html)**. A living document — ideas added as they come. Part of the [NYC Digital Modernization](README.md) study.*
