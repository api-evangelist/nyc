# Opportunity Ranking

Where NYC API modernization matters most — every domain scored **demand × gap × feasibility** (see method in [opportunity.json](data/opportunity.json)). Interactive: [opportunity.html](https://nyc.apievangelist.com/opportunity.html).

## Top 20 by opportunity score

| # | Domain | Score | Demand | Gap | Feasibility | Quadrant | Net-new write |
|--|--|--|--|--|--|--|--|
| 1 | NYC Citywide Admin Services (DCAS) | **87.0** | 0.967 | 0.9 | 1.0 | Quick win | `ExamRegistration — register for a civil-service exam (alt: JobApplication)` |
| 2 | NYC Buildings (DOB) | **85.7** | 0.952 | 0.9 | 1.0 | Quick win | `PermitApplication` |
| 3 | NYPD | **82.3** | 0.915 | 0.9 | 1.0 | Quick win | `PoliceReportRequest` |
| 4 | NYC Finance (DOF) | **82.2** | 0.913 | 0.9 | 1.0 | Quick win | `ParkingTicketPayment — pay a parking/camera violation via API instead of the CityPay-only web form.` |
| 5 | NYC Parks & Recreation | **81.0** | 0.9 | 0.9 | 1.0 | Quick win | `PermitApplication` |
| 6 | NYC Public Schools (DOE) | **81.0** | 0.9 | 0.9 | 1.0 | Quick win | `EnrollmentApplication` |
| 7 | NYC311 | **81.0** | 0.9 | 0.9 | 1.0 | Quick win | `ServiceRequest (Open311)` |
| 8 | NYC Transportation (DOT) | **81.0** | 0.9 | 0.9 | 1.0 | Quick win | `StreetWorkPermit` |
| 9 | NYC Health (DOHMH) | **81.0** | 0.9 | 0.9 | 1.0 | Quick win | `VitalRecordRequest` |
| 10 | NYC Environmental Protection (DEP) | **81.0** | 0.9 | 0.9 | 1.0 | Quick win | `WaterServiceRequest` |
| 11 | NYC Aging (DFTA) | **81.0** | 0.9 | 0.9 | 1.0 | Quick win | `ServiceReferral — connect an older adult to DFTA services (case management, meals, benefits, caregiver, elder abuse, center enrollment) with an urgent path to Aging Connect / Adult Protective Services.` |
| 12 | NYC Records (DORIS) | **81.0** | 0.9 | 0.9 | 1.0 | Quick win | `RecordsRequest — request/retrieve a record: order a copy of a historical vital record, an archival item/photo, a library publication, or file a FOIL request` |
| 13 | NYC Fire (FDNY) | **81.0** | 0.9 | 0.9 | 1.0 | Quick win | `FirePermitApplication — apply for and track a fire permit / Certificate of Operation / inspection request via FDNY Business` |
| 14 | NYC Landmarks (LPC) | **81.0** | 0.9 | 0.9 | 1.0 | Quick win | `LandmarkPermitApplication — file a Certificate of Appropriateness / No Effect / Minor Work application (today Salesforce Portico only, no API)` |
| 15 | NYC Health + Hospitals | **72.0** | 0.9 | 0.8 | 1.0 | Quick win | `AppointmentRequest — request/book an appointment (no write in the live FHIR surface)` |
| 16 | NYC Consumer & Worker Protection (DCWP) | **71.9** | 0.799 | 0.9 | 1.0 | Quick win | `File a consumer complaint (ConsumerComplaint) and apply for a business license (LicenseApplication) — the two citizen writes with no API` |
| 17 | NYC Small Business Services (SBS) | **70.3** | 0.781 | 0.9 | 1.0 | Quick win | `MWBECertificationApplication — apply for M/WBE (also EBE/LBE) certification; no API today, only the MyCity Business portal.` |
| 18 | NYC Taxi & Limousine (TLC) | **70.0** | 1.0 | 0.7 | 1.0 | Quick win | `LicenseApplication` |
| 19 | NYC School Construction Authority (SCA) | **69.7** | 0.774 | 0.9 | 1.0 | Quick win | `VendorPrequalification — apply to become a prequalified SCA vendor` |
| 20 | NYC Housing Authority (NYCHA) | **69.4** | 0.771 | 0.9 | 1.0 | Quick win | `WorkOrder` |

## Quick wins (high impact + already feasible)

- **NYC Citywide Admin Services (DCAS)** (87.0) — a private API to open; net-new `ExamRegistration — register for a civil-service exam (alt: JobApplication)`
- **NYC Buildings (DOB)** (85.7) — a private API to open, high-reach citizen transaction; net-new `PermitApplication`
- **NYPD** (82.3) — a private API to open; net-new `PoliceReportRequest`
- **NYC Finance (DOF)** (82.2) — a private API to open; net-new `ParkingTicketPayment — pay a parking/camera violation via API instead of the CityPay-only web form.`
- **NYC Parks & Recreation** (81.0) — a private API to open, high-reach citizen transaction; net-new `PermitApplication`
- **NYC Public Schools (DOE)** (81.0) — a private API to open, high-reach citizen transaction; net-new `EnrollmentApplication`
- **NYC311** (81.0) — a private API to open, high-reach citizen transaction; net-new `ServiceRequest (Open311)`
- **NYC Transportation (DOT)** (81.0) — open data to wrap, high-reach citizen transaction; net-new `StreetWorkPermit`
- **NYC Health (DOHMH)** (81.0) — a private API to open, high-reach citizen transaction; net-new `VitalRecordRequest`
- **NYC Environmental Protection (DEP)** (81.0) — a private API to open, high-reach citizen transaction; net-new `WaterServiceRequest`
- **NYC Aging (DFTA)** (81.0) — open data to wrap, high-reach citizen transaction; net-new `ServiceReferral — connect an older adult to DFTA services (case management, meals, benefits, caregiver, elder abuse, center enrollment) with an urgent path to Aging Connect / Adult Protective Services.`
- **NYC Records (DORIS)** (81.0) — a private API to open, high-reach citizen transaction; net-new `RecordsRequest — request/retrieve a record: order a copy of a historical vital record, an archival item/photo, a library publication, or file a FOIL request`
- **NYC Fire (FDNY)** (81.0) — a private API to open, high-reach citizen transaction; net-new `FirePermitApplication — apply for and track a fire permit / Certificate of Operation / inspection request via FDNY Business`
- **NYC Landmarks (LPC)** (81.0) — a private API to open, high-reach citizen transaction; net-new `LandmarkPermitApplication — file a Certificate of Appropriateness / No Effect / Minor Work application (today Salesforce Portico only, no API)`
- **NYC Health + Hospitals** (72.0) — an API already exists (expose/document), high-reach citizen transaction; net-new `AppointmentRequest — request/book an appointment (no write in the live FHIR surface)`
- **NYC Consumer & Worker Protection (DCWP)** (71.9) — a private API to open; net-new `File a consumer complaint (ConsumerComplaint) and apply for a business license (LicenseApplication) — the two citizen writes with no API`
- **NYC Small Business Services (SBS)** (70.3) — a private API to open; net-new `MWBECertificationApplication — apply for M/WBE (also EBE/LBE) certification; no API today, only the MyCity Business portal.`
- **NYC Taxi & Limousine (TLC)** (70.0) — an API already exists (expose/document); net-new `LicenseApplication`
- **NYC School Construction Authority (SCA)** (69.7) — a private API to open; net-new `VendorPrequalification — apply to become a prequalified SCA vendor`
- **NYC Housing Authority (NYCHA)** (69.4) — a private API to open; net-new `WorkOrder`
