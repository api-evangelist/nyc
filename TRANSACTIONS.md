# Citizen-Transaction Taxonomy

The **66 net-new write workflows** — one per domain — grouped into reusable primitives. The city needs a handful of transaction patterns, built once and reused. Interactive: [transactions.html](https://nyc.apievangelist.com/transactions.html).

## Apply (30)

- **City University of New York (CUNY)** — `AdmissionsApplication (submit a CUNY application)`
- **NYC Cultural Affairs (DCLA)** — `Apply for a Cultural Development Fund grant (GrantApplication) — the core transaction with no API, locked in the Salesforce Grants Management System`
- **NYC Tax Commission** — `AssessmentAppeal — file a property-tax assessment appeal (Application for Correction).`
- **NYC Social Services (HRA)** — `BenefitsApplication — apply for and track SNAP / Cash Assistance / Medicaid, today locked in the ACCESS HRA portal`
- **Queens Public Library (QPL)** — `BookHold — place a hold/reservation on a catalog item (also: library-card application)`
- **Brooklyn Borough President** — `CommunityBoardApplication — apply to serve on a Brooklyn community board (net-new write; today only a web form).`
- **Manhattan Borough President** — `CommunityBoardApplication — apply to serve on a Manhattan community board (today a Forminator web form / PDF, no API)`
- **Queens Borough President** — `CommunityBoardApplication — apply to serve on a Queens community board (today an HTML/PDF form)`
- **Staten Island Borough President** — `CommunityBoardApplication — apply to serve on a Staten Island community board (today an opaque Weebly form)`
- **Bronx Borough President** — `CommunityBoardApplication — apply to serve on one of the Bronx's twelve community boards (today a PDF/email; no structured intake or status).`
- **NYC Campaign Finance Board (CFB)** — `DisclosureFiling — a filer submits a disclosure statement (today only via the login-walled C-SMART disclosure application)`
- **NYC Public Schools (DOE)** — `EnrollmentApplication`
- **NYC Citywide Admin Services (DCAS)** — `ExamRegistration — register for a civil-service exam (alt: JobApplication)`
- **NYC Consumer & Worker Protection (DCWP)** — `File a consumer complaint (ConsumerComplaint) and apply for a business license (LicenseApplication) — the two citizen writes with no API`
- **NYC Media & Entertainment (MOME)** — `FilmPermitApplication — apply for a film/photography permit via API instead of the login-walled E-Apply portal`
- **NYC Fire (FDNY)** — `FirePermitApplication — apply for and track a fire permit / Certificate of Operation / inspection request via FDNY Business`
- **NYC Housing (HPD)** — `HousingLotteryApplication`
- **NYC Landmarks (LPC)** — `LandmarkPermitApplication — file a Certificate of Appropriateness / No Effect / Minor Work application (today Salesforce Portico only, no API)`
- **NYC Law Department** — `LawInternshipApplication — submit a legal internship / fellowship application (the one citizen-initiated transaction with this agency)`
- **NYC Taxi & Limousine (TLC)** — `LicenseApplication`
- **NYC Small Business Services (SBS)** — `MWBECertificationApplication — apply for M/WBE (also EBE/LBE) certification; no API today, only the MyCity Business portal.`
- **NYC City Clerk** — `MarriageLicenseApplication — a couple applies for a NYC marriage license (today only via Project Cupid's Unqork screens)`
- **NYC Parks & Recreation** — `PermitApplication`
- **NYC Buildings (DOB)** — `PermitApplication`
- **NYC Youth & Community Dev (DYCD)** — `ProgramApplication — apply to a program (e.g. an SYEP application)`
- **NYC Aging (DFTA)** — `ServiceReferral — connect an older adult to DFTA services (case management, meals, benefits, caregiver, elder abuse, center enrollment) with an urgent path to Aging Connect / Adult Protective Services.`
- **NYC Business Integrity Commission (BIC)** — `TradeWasteLicenseApplication — apply for a trade waste license/registration`
- **NYC Standards & Appeals (BSA)** — `VarianceApplication — file a zoning variance / special permit / extension / appeal (today a paper PDF-form process)`
- **NYC Design & Construction (DDC)** — `VendorPrequalification — a firm submits a prequalification / expression of interest (optionally against a solicitation, with an optional City Record notice opt-in). A B2G write; DDC is vendor-facing, so there is no citizen write in this domain.`
- **NYC School Construction Authority (SCA)** — `VendorPrequalification — apply to become a prequalified SCA vendor`

## Pay (1)

- **NYC Finance (DOF)** — `ParkingTicketPayment — pay a parking/camera violation via API instead of the CityPay-only web form.`

## Report / Complain (17)

- **NYC Human Rights (CCHR)** — `A typed DiscriminationComplaint intake API (report discrimination) — replacing the untyped Report Discrimination HTML form.`
- **NYC Children's Services (ACS)** — `ChildCareComplaint — submit a complaint about a child care provider (models the provider concern, never case data; abuse routed to the State Central Register)`
- **NYC Investigation (DOI)** — `CorruptionComplaint — file and track a fraud/waste/corruption tip (with anonymous filing and Whistleblower-Law protection), the transaction that starts every DOI investigation and today lives only in a vendor Kaseware form.`
- **NYC Medical Examiner (OCME)** — `DeathRecordRequest — request and track a decedent's medical-examiner casefile record/report`
- **NYC Conflicts of Interest Board (COIB)** — `FinancialDisclosureFiling — a public servant files/attests an annual financial disclosure report, today locked inside the login-only COIB filing website with no API`
- **NYC Civilian Complaint Review (CCRB)** — `MisconductComplaint — file a police-misconduct complaint against an officer via API (today an online web form only)`
- **NYC Public Advocate** — `OmbudsmanComplaint — file and track a 'help with a city agency' case against a NYC agency`
- **NYC Homeless Services (DHS)** — `OutreachRequest — request street outreach for a person experiencing homelessness (today only via NYC311)`
- **NYPD** — `PoliceReportRequest`
- **NYC311** — `ServiceRequest (Open311)`
- **Bronx District Attorney** — `TipSubmission — a structured, trackable intake for a crime tip, a Civilian Complaint Unit complaint of police misconduct, or a FOIL records request (today a phone call to 718-590-2300 or an email to FOILREQUEST@BRONXDA.NYC.GOV, with no tracking number).`
- **Staten Island District Attorney** — `TipSubmission — an API for the confidential drug/scam tip forms (today Contact Form 7 email only)`
- **Manhattan District Attorney** — `TipSubmission — submit a routable tip to a DA bureau (no API today; only a generic reCAPTCHA contact form). FOIL is delegated off-site to NYC OpenRecords.`
- **Queens District Attorney** — `TipSubmission — submit a tip, cold-case lead, or FOIL request (no inbound channel today)`
- **Brooklyn District Attorney** — `TipSubmission — submit and track a confidential tip (report fraud, an unsafe landlord, a hate incident, trafficking, or information on an open case)`
- **NYC Correction (DOC)** — `VisitScheduling — schedule a visit with a person in custody (no API today; arranged by phone, in person, or vendor portal). Complaint / records request is a second net-new write.`
- **NYC Environmental Protection (DEP)** — `WaterServiceRequest`

## Register / Subscribe (2)

- **NYC Emergency Management (NYCEM)** — `NotifyNYCSubscription — subscribe to Notify NYC emergency alerts by channel, location, and category through an owned write API`
- **NYC Council** — `TestimonyRegistration`

## Schedule / Reserve (4)

- **NYC Health + Hospitals** — `AppointmentRequest — request/book an appointment (no write in the live FHIR surface)`
- **NYC Sanitation (DSNY)** — `BulkPickupRequest`
- **New York Public Library (NYPL)** — `Hold (BookHold) — place and track a reservation on a catalog item via a clean, agent-native public API (backed by NYPL's existing internal hold services)`
- **Brooklyn Public Library (BPL)** — `place a hold (BookHold)`

## Request records / service (5)

- **NYC Independent Budget Office (IBO)** — `DataRequest — an API for the 'Ask IBO' data/analysis request, today a web form / email only`
- **NYC Criminal Justice (MOCJ)** — `ProgramReferral — route a person or court case to a MOCJ-coordinated program`
- **NYC Records (DORIS)** — `RecordsRequest — request/retrieve a record: order a copy of a historical vital record, an archival item/photo, a library publication, or file a FOIL request`
- **NYC Veterans' Services (DVS)** — `ServiceReferral — make a VetConnectNYC care-coordination referral connecting a veteran to services (housing, benefits, VA claims, health, employment, education, food, legal), routed to DVS Care Coordinators with an urgent path to a Veteran Resource Center.`
- **NYC Health (DOHMH)** — `VitalRecordRequest`

## Dispute / Appeal / File (2)

- **NYC Comptroller** — `ClaimFiling`
- **NYC Admin Trials & Hearings (OATH)** — `SummonsDispute — respond to / dispute a summons (request a hearing) via an owned API`

## Other (5)

- **NYC Board of Elections** — `BallotRequest`
- **NYC Technology & Innovation (OTI)** — `One owned, unified gateway + catalog API — plus two write surfaces: register a dataset, and request an api.nyc.gov gateway key.`
- **NYC Economic Development (EDC)** — `RFPResponse — register interest in / submit a proposal to an EDC solicitation (RFP/RFEI)`
- **NYC Transportation (DOT)** — `StreetWorkPermit`
- **NYC Housing Authority (NYCHA)** — `WorkOrder`

