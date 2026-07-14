# Master Entity List

Every object modeled across the **67 assessed domains** — 422 object schemas, **328 distinct entity names**. Generated from each domain's `schemas/*.json` titles. Interactive: [entities.html](https://nyc.apievangelist.com/entities.html).

## Recurring entities (shared across domains)

Entities modeled in 2+ domains — the natural candidates for shared, citywide schemas.

| Entity | # domains | Domains |
|---|---|---|
| `BoardAppointment` | 2 | Brooklyn Borough President, Manhattan Borough President |
| `BookHold` | 2 | Brooklyn Public Library (BPL), Queens Public Library (QPL) |
| `Branch` | 3 | Brooklyn Public Library (BPL), New York Public Library (NYPL), Queens Public Library (QPL) |
| `Building` | 2 | NYC Buildings (DOB), NYC Housing (HPD) |
| `Candidate` | 2 | NYC Board of Elections, NYC Campaign Finance Board (CFB) |
| `CapitalProject` | 3 | NYC Parks & Recreation, NYC Design & Construction (DDC), NYC School Construction Authority (SCA) |
| `Case` | 2 | NYC Veterans' Services (DVS), Queens District Attorney |
| `CaseStatistics` | 2 | Brooklyn District Attorney, NYC Medical Examiner (OCME) |
| `CatalogItem` | 3 | Brooklyn Public Library (BPL), New York Public Library (NYPL), Queens Public Library (QPL) |
| `Committee` | 2 | NYC Council, NYC Campaign Finance Board (CFB) |
| `CommunityBoard` | 3 | Brooklyn Borough President, Manhattan Borough President, Queens Borough President |
| `CommunityBoardApplication` | 5 | Bronx Borough President, Brooklyn Borough President, Manhattan Borough President, Queens Borough President, Staten Island Borough President |
| `CommunityBoardAppointment` | 3 | Bronx Borough President, Queens Borough President, Staten Island Borough President |
| `CommunityResource` | 4 | Bronx District Attorney, Brooklyn District Attorney, Queens District Attorney, Staten Island District Attorney |
| `Complaint` | 5 | NYC Buildings (DOB), NYC Housing (HPD), NYC Business Integrity Commission (BIC), NYC Civilian Complaint Review (CCRB), NYC Correction (DOC) |
| `Contract` | 2 | NYC Comptroller, NYC Youth & Community Dev (DYCD) |
| `DigitalCollection` | 2 | Brooklyn Public Library (BPL), Queens Public Library (QPL) |
| `DigitalItem` | 2 | NYC Records (DORIS), New York Public Library (NYPL) |
| `DiscretionaryFundingAward` | 3 | Bronx Borough President, Queens Borough President, Staten Island Borough President |
| `Event` | 8 | NYC Parks & Recreation, Brooklyn Public Library (BPL), Bronx Borough President, Brooklyn Borough President, New York Public Library (NYPL), Queens Borough President, Queens Public Library (QPL), Staten Island Borough President |
| `Facility` | 3 | NYC Parks & Recreation, NYC Correction (DOC), NYC Health + Hospitals |
| `FundingAward` | 2 | Brooklyn Borough President, Manhattan Borough President |
| `Hearing` | 2 | NYC Standards & Appeals (BSA), NYC Admin Trials & Hearings (OATH) |
| `Inspection` | 5 | NYC Health (DOHMH), NYC Taxi & Limousine (TLC), NYC Consumer & Worker Protection (DCWP), NYC Fire (FDNY), NYC School Construction Authority (SCA) |
| `LandUseRecommendation` | 5 | Bronx Borough President, Brooklyn Borough President, Manhattan Borough President, Queens Borough President, Staten Island Borough President |
| `Legislation` | 3 | NYC Council, Manhattan Borough President, NYC Public Advocate |
| `LibraryCard` | 2 | Brooklyn Public Library (BPL), Queens Public Library (QPL) |
| `LicenseApplication` | 2 | NYC Taxi & Limousine (TLC), NYC Consumer & Worker Protection (DCWP) |
| `Permit` | 2 | NYC Buildings (DOB), NYC Environmental Protection (DEP) |
| `PermitApplication` | 3 | NYC Parks & Recreation, NYC Buildings (DOB), NYC Landmarks (LPC) |
| `PressRelease` | 7 | Bronx Borough President, Bronx District Attorney, Brooklyn District Attorney, Manhattan District Attorney, Queens Borough President, Queens District Attorney, Staten Island District Attorney |
| `Program` | 8 | Bronx District Attorney, Brooklyn District Attorney, NYC Youth & Community Dev (DYCD), NYC Social Services (HRA), Manhattan District Attorney, NYC Criminal Justice (MOCJ), Queens District Attorney, Staten Island District Attorney |
| `Provider` | 3 | NYC Children's Services (ACS), NYC Youth & Community Dev (DYCD), NYC Health + Hospitals |
| `Publication` | 2 | NYC Independent Budget Office (IBO), NYC Law Department |
| `Report` | 2 | Brooklyn Borough President, NYC Public Advocate |
| `Resolution` | 2 | NYC Standards & Appeals (BSA), Staten Island Borough President |
| `ServiceReferral` | 2 | NYC Aging (DFTA), NYC Veterans' Services (DVS) |
| `ServiceRequest` | 2 | NYC311, NYC Technology & Innovation (OTI) |
| `Solicitation` | 4 | NYC Design & Construction (DDC), NYC Economic Development (EDC), NYC Criminal Justice (MOCJ), NYC School Construction Authority (SCA) |
| `TipSubmission` | 5 | Bronx District Attorney, Brooklyn District Attorney, Manhattan District Attorney, Queens District Attorney, Staten Island District Attorney |
| `Vehicle` | 2 | NYC Taxi & Limousine (TLC), NYC Business Integrity Commission (BIC) |
| `VendorPrequalification` | 2 | NYC Design & Construction (DDC), NYC School Construction Authority (SCA) |
| `VictimService` | 5 | Bronx District Attorney, Brooklyn District Attorney, Manhattan District Attorney, Queens District Attorney, Staten Island District Attorney |
| `Violation` | 3 | NYC Buildings (DOB), NYC Business Integrity Commission (BIC), NYC Fire (FDNY) |

## All entities by domain

- **NYC Parks & Recreation** (`nycgovparks.org`) — `CapitalProject`, `Event`, `Facility`, `Monument`, `Park`, `PermitApplication`, `Tree`
- **NYC Public Schools (DOE)** (`schools.nyc.gov`) — `CalendarEvent`, `EnrollmentApplication`, `School`, `SchoolDemographics`, `TestResult`
- **NYC Council** (`council.nyc.gov`) — `Committee`, `CouncilMember`, `DiscretionaryFunding`, `District`, `Legislation`, `Meeting`, `TestimonyRegistration`
- **NYC Board of Elections** (`vote.nyc`) — `BallotRequest`, `Candidate`, `Contest`, `Election`, `ElectionDistrict`, `ElectionResult`, `PollSite`
- **NYC311** (`nyc311`) — `Agency`, `ServiceDefinition`, `ServiceRequest`, `ServiceType`
- **NYC Buildings (DOB)** (`dob`) — `Building`, `CertificateOfOccupancy`, `Complaint`, `JobFiling`, `Permit`, `PermitApplication`, `Violation`
- **NYC Housing (HPD)** (`hpd`) — `AffordableHousingProject`, `Building`, `Complaint`, `HousingLotteryApplication`, `HousingMaintenanceViolation`, `LitigationCase`, `Registration`
- **NYC Transportation (DOT)** (`dot`) — `BikeRoute`, `Bridge`, `ParkingRegulation`, `PedestrianPlaza`, `SpeedHump`, `StreetWorkPermit`, `TrafficSignal`
- **NYC Health (DOHMH)** (`dohmh`) — `ChildcareCenter`, `EnvironmentalComplaint`, `FoodEstablishment`, `HealthFacility`, `Inspection`, `RodentInspection`, `VitalRecordRequest`
- **NYC Sanitation (DSNY)** (`dsny`) — `BulkPickupRequest`, `CollectionSchedule`, `DropOffSite`, `LitterBasket`, `SanitationDistrict`, `Tonnage`
- **NYPD** (`nypd`) — `Arrest`, `ComplaintReport`, `Officer`, `PoliceReportRequest`, `Precinct`, `ShootingIncident`
- **NYC Taxi & Limousine (TLC)** (`tlc`) — `Base`, `DriverLicense`, `Inspection`, `LicenseApplication`, `TaxiZone`, `TripRecord`, `Vehicle`
- **NYC City Planning (DCP)** (`dcp`) — `CensusGeography`, `CommunityDistrict`, `LandUseApplication`, `NTA`, `TaxLot`, `ZoningDistrict`
- **NYC Comptroller** (`comptroller.nyc.gov`) — `Audit`, `ClaimAgainstCity`, `ClaimFiling`, `Contract`, `PensionHolding`, `SpendingTransaction`
- **NYC Housing Authority (NYCHA)** (`nycha`) — `CommunityFacility`, `Development`, `ResidentialAddress`, `ResidentStatistics`, `UtilityConsumption`, `WorkOrder`
- **NYC Children's Services (ACS)** (`acs`) — `ChildCareComplaint`, `ChildWelfareIndicator`, `FosterCareStatistics`, `JuvenileJusticeStatistics`, `PreventionService`, `Provider`
- **NYC Business Integrity Commission (BIC)** (`bic`) — `Complaint`, `Licensee`, `MarketBusiness`, `Registrant`, `TradeWasteLicenseApplication`, `Vehicle`, `Violation`
- **Brooklyn Public Library (BPL)** (`bklynlibrary`) — `BookHold`, `Branch`, `CatalogItem`, `DigitalCollection`, `ElectronicResource`, `Event`, `LibraryCard`
- **Bronx Borough President** (`bronxbp`) — `CommunityBoardApplication`, `CommunityBoardAppointment`, `DiscretionaryFundingAward`, `Event`, `LandUseRecommendation`, `PressRelease`
- **Bronx District Attorney** (`bronxda`) — `CaseStatistic`, `CommunityResource`, `PressRelease`, `Program`, `TipSubmission`, `VictimService`
- **Brooklyn Borough President** (`brooklynbp`) — `BoardAppointment`, `CommunityBoard`, `CommunityBoardApplication`, `Event`, `FundingAward`, `LandUseRecommendation`, `Report`
- **Brooklyn District Attorney** (`brooklynda`) — `CaseStatistics`, `CommunityResource`, `PressRelease`, `Program`, `TipSubmission`, `VictimService`
- **NYC Standards & Appeals (BSA)** (`bsa`) — `Application`, `Hearing`, `PreApplicationMeeting`, `Resolution`, `VarianceApplication`, `ZoningLot`
- **NYC Human Rights (CCHR)** (`cchr`) — `DiscriminationComplaint`, `InquiryStatistic`, `LegalGuidance`, `ProtectedClass`, `ResolutionStatistic`, `TrainingEvent`
- **NYC Civilian Complaint Review (CCRB)** (`ccrb`) — `Allegation`, `Complaint`, `MisconductComplaint`, `Penalty`, `PoliceOfficer`
- **NYC Campaign Finance Board (CFB)** (`cfb`) — `Candidate`, `Committee`, `Contribution`, `DisclosureFiling`, `Expenditure`, `PublicMatchingFundsPayment`
- **NYC City Clerk** (`cityclerk`) — `Ceremony`, `FundraisingReport`, `LobbyistFiling`, `LobbyistRegistration`, `MarriageLicense`, `MarriageLicenseApplication`
- **NYC Conflicts of Interest Board (COIB)** (`coib`) — `AdvisoryOpinion`, `AgencyDonation`, `EnforcementDisposition`, `FinancialDisclosureFiling`, `LegalDefenseTrustTransaction`, `Policymaker`
- **City University of New York (CUNY)** (`cuny`) — `AdmissionsApplication`, `Campus`, `Course`, `DegreeProgram`, `EnrollmentStatistics`, `FacultyResearch`
- **NYC Citywide Admin Services (DCAS)** (`dcas`) — `CityBuilding`, `CivilServiceTitle`, `EligibleListEntry`, `ExamRegistration`, `ExamSchedule`, `FleetVehicle`, `JobPosting`
- **NYC Cultural Affairs (DCLA)** (`dcla`) — `CapitalFunding`, `CulturalInstitution`, `CulturalOrganization`, `GrantApplication`, `MaterialsForTheArts`, `ProgramFunding`, `PublicArtwork`
- **NYC Consumer & Worker Protection (DCWP)** (`dcwp`) — `BusinessLicense`, `Charge`, `ConsumerComplaint`, `Inspection`, `LicenseApplication`, `WorkerProtectionCase`
- **NYC Design & Construction (DDC)** (`ddc`) — `AwardedContract`, `CapitalProject`, `Division`, `Solicitation`, `Vendor`, `VendorPrequalification`
- **NYC Environmental Protection (DEP)** (`dep`) — `GreenInfrastructure`, `Hydrant`, `Permit`, `ReservoirLevel`, `WaterConsumption`, `WaterQualitySample`, `WaterServiceRequest`
- **NYC Aging (DFTA)** (`dfta`) — `OlderAdultCenter`, `Participation`, `ProgramActivity`, `ServiceProvider`, `ServiceReferral`, `ServiceUnit`
- **NYC Homeless Services (DHS)** (`dhs`) — `DHSContact`, `DropInCenter`, `OutreachRequest`, `ShelterCensus`, `ShelterFacility`, `StreetHomelessCount`
- **NYC Correction (DOC)** (`doc`) — `Complaint`, `DailyPopulation`, `Facility`, `IncidentReport`, `PersonInCustody`, `Visit`
- **NYC Finance (DOF)** (`dof`) — `ACRISDocument`, `ParkingTicketPayment`, `ParkingViolation`, `PropertyExemption`, `PropertyTaxBill`, `PropertyValuation`
- **NYC Investigation (DOI)** (`doi`) — `CorruptionComplaint`, `Eviction`, `MarshalRevenue`, `PerformanceIndicator`, `PolicyRecommendation`, `PublicReport`
- **NYC Records (DORIS)** (`doris`) — `ArchivalCollection`, `DigitalItem`, `GovernmentPublication`, `HistoricalVitalRecord`, `HonoraryStreetName`, `RecordsRequest`
- **NYC Veterans' Services (DVS)** (`dvs`) — `AssistanceRequest`, `Case`, `ClientStatistics`, `ServiceReferral`, `VeteranOwnedBusiness`, `VeteranResource`
- **NYC Youth & Community Dev (DYCD)** (`dycd`) — `Contract`, `ParticipantDemographics`, `Program`, `ProgramApplication`, `ProgramSite`, `Provider`, `ServiceArea`
- **NYC Economic Development (EDC)** (`edc`) — `DevelopmentProject`, `FerryRidership`, `MappedCompany`, `PropertyAsset`, `RFPResponse`, `Solicitation`, `WiredBuilding`
- **NYC Fire (FDNY)** (`fdny`) — `CertificateOfFitness`, `Firehouse`, `FirePermitApplication`, `IncidentDispatch`, `Inspection`, `Violation`
- **NYC Health + Hospitals** (`hhc`) — `Appointment`, `AppointmentRequest`, `Facility`, `FinancialAssistance`, `Pharmacy`, `Provider`, `Service`
- **NYC Social Services (HRA)** (`hra`) — `BenefitsApplication`, `BenefitsEligibility`, `CaseAction`, `CaseloadStatistic`, `Center`, `Program`
- **NYC Independent Budget Office (IBO)** (`ibo`) — `DataRequest`, `FiscalDataTable`, `FiscalSeries`, `Publication`, `SchoolSpending`, `TaxDistribution`
- **NYC Law Department** (`law`) — `LawInternshipApplication`, `LegalCase`, `LegalDivision`, `MwbeStatistic`, `Publication`, `PublicServiceProgram`
- **NYC Landmarks (LPC)** (`lpc`) — `DesignatedBuilding`, `DesignationReport`, `HistoricDistrict`, `Landmark`, `LandmarkPermitApplication`, `PermitApplication`, `ViolationOrder`
- **Manhattan Borough President** (`manhattanbp`) — `BoardAppointment`, `CommunityBoard`, `CommunityBoardApplication`, `ConstituentCase`, `FundingAward`, `LandUseRecommendation`, `Legislation`
- **Manhattan District Attorney** (`manhattanda`) — `Office`, `PressRelease`, `Program`, `Prosecution`, `TipSubmission`, `VictimService`
- **NYC Criminal Justice (MOCJ)** (`mocj`) — `DataReport`, `JailPopulationMetric`, `Program`, `ProgramReferral`, `Solicitation`, `SupervisedReleaseDocket`
- **NYC Media & Entertainment (MOME)** (`mome`) — `FilmPermit`, `FilmPermitApplication`, `MarchInspection`, `MediaProgram`, `ProductionCompany`, `ScreenActivity`
- **NYC Emergency Management (NYCEM)** (`nycem`) — `EmergencyIncident`, `EmergencyNotification`, `EvacuationCenter`, `HurricaneEvacuationZone`, `MitigationAction`, `NotifyNYCSubscription`, `PreparednessResource`
- **New York Public Library (NYPL)** (`nypl`) — `Branch`, `CatalogItem`, `Collection`, `DigitalItem`, `Event`, `Hold`
- **NYC Admin Trials & Hearings (OATH)** (`oath`) — `Decision`, `Hearing`, `Summons`, `SummonsDispute`, `TrialCase`
- **NYC Medical Examiner (OCME)** (`ocme`) — `CaseStatistics`, `DeathRecordRequest`, `FamilyServicesCenter`, `ForensicService`, `MissingPerson`, `MonthlyIndicator`
- **NYC Technology & Innovation (OTI)** (`oti`) — `APIGatewayService`, `BroadbandAsset`, `LinkNYCKiosk`, `OpenDataset`, `ServiceRequest`, `WiFiHotspot`
- **NYC Public Advocate** (`pubadvocate`) — `Legislation`, `OmbudsmanComplaint`, `PublicInterestRequest`, `Report`, `WatchlistBuilding`, `WorstLandlord`
- **Queens Borough President** (`queensbp`) — `CommunityBoard`, `CommunityBoardApplication`, `CommunityBoardAppointment`, `DiscretionaryFundingAward`, `Event`, `LandUseRecommendation`, `PressRelease`
- **Queens District Attorney** (`queensda`) — `Case`, `ColdCase`, `CommunityResource`, `PressRelease`, `Program`, `TipSubmission`, `VictimService`
- **Queens Public Library (QPL)** (`queenslibrary`) — `BookHold`, `Branch`, `CatalogItem`, `DigitalCollection`, `Event`, `LibraryCard`
- **NYC Small Business Services (SBS)** (`sbs`) — `BusinessImprovementDistrict`, `BusinessIncentive`, `CertifiedBusiness`, `JobListing`, `MWBECertificationApplication`, `ServiceLocation`, `WorkforceEvent`
- **NYC School Construction Authority (SCA)** (`sca`) — `CapitalProject`, `EnrollmentCapacity`, `Inspection`, `PrequalifiedFirm`, `Solicitation`, `UpcomingContract`, `VendorPrequalification`
- **Staten Island Borough President** (`statenislandbp`) — `CommunityBoardApplication`, `CommunityBoardAppointment`, `ConstituentRequest`, `DiscretionaryFundingAward`, `Event`, `LandUseRecommendation`, `Resolution`
- **Staten Island District Attorney** (`statenislandda`) — `CommunityResource`, `PressRelease`, `Program`, `ProsecutionStatistics`, `TipSubmission`, `VictimService`
- **NYC Tax Commission** (`taxcommission`) — `Article7Petition`, `AssessmentAction`, `AssessmentAppeal`, `Determination`, `Property`, `Representative`
