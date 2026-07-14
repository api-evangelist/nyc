# Master Entity List

Every object modeled across the **67 assessed domains** — 422 object schemas, **328 distinct entity names**. Generated from each domain's `schemas/*.json` titles. Interactive: [entities.html](https://nyc.apievangelist.com/entities.html).

## Recurring entities (shared across domains)

Entities modeled in 2+ domains — the natural candidates for shared, citywide schemas.

| Entity | # domains | Domains |
|---|---|---|
| `Event` | 8 | NYC Parks & Recreation, Brooklyn Public Library (BPL), Bronx Borough President, Brooklyn Borough President, New York Public Library (NYPL), Queens Borough President, Queens Public Library (QPL), Staten Island Borough President |
| `Program` | 8 | Bronx District Attorney, Brooklyn District Attorney, NYC Youth & Community Dev (DYCD), NYC Social Services (HRA), Manhattan District Attorney, NYC Criminal Justice (MOCJ), Queens District Attorney, Staten Island District Attorney |
| `PressRelease` | 7 | Bronx Borough President, Bronx District Attorney, Brooklyn District Attorney, Manhattan District Attorney, Queens Borough President, Queens District Attorney, Staten Island District Attorney |
| `CommunityBoardApplication` | 5 | Bronx Borough President, Brooklyn Borough President, Manhattan Borough President, Queens Borough President, Staten Island Borough President |
| `Complaint` | 5 | NYC Buildings (DOB), NYC Housing (HPD), NYC Business Integrity Commission (BIC), NYC Civilian Complaint Review (CCRB), NYC Correction (DOC) |
| `Inspection` | 5 | NYC Health (DOHMH), NYC Taxi & Limousine (TLC), NYC Consumer & Worker Protection (DCWP), NYC Fire (FDNY), NYC School Construction Authority (SCA) |
| `LandUseRecommendation` | 5 | Bronx Borough President, Brooklyn Borough President, Manhattan Borough President, Queens Borough President, Staten Island Borough President |
| `TipSubmission` | 5 | Bronx District Attorney, Brooklyn District Attorney, Manhattan District Attorney, Queens District Attorney, Staten Island District Attorney |
| `VictimService` | 5 | Bronx District Attorney, Brooklyn District Attorney, Manhattan District Attorney, Queens District Attorney, Staten Island District Attorney |
| `CommunityResource` | 4 | Bronx District Attorney, Brooklyn District Attorney, Queens District Attorney, Staten Island District Attorney |
| `Solicitation` | 4 | NYC Design & Construction (DDC), NYC Economic Development (EDC), NYC Criminal Justice (MOCJ), NYC School Construction Authority (SCA) |
| `Branch` | 3 | Brooklyn Public Library (BPL), New York Public Library (NYPL), Queens Public Library (QPL) |
| `CapitalProject` | 3 | NYC Parks & Recreation, NYC Design & Construction (DDC), NYC School Construction Authority (SCA) |
| `CatalogItem` | 3 | Brooklyn Public Library (BPL), New York Public Library (NYPL), Queens Public Library (QPL) |
| `CommunityBoard` | 3 | Brooklyn Borough President, Manhattan Borough President, Queens Borough President |
| `CommunityBoardAppointment` | 3 | Bronx Borough President, Queens Borough President, Staten Island Borough President |
| `DiscretionaryFundingAward` | 3 | Bronx Borough President, Queens Borough President, Staten Island Borough President |
| `Facility` | 3 | NYC Parks & Recreation, NYC Correction (DOC), NYC Health + Hospitals |
| `Legislation` | 3 | NYC Council, Manhattan Borough President, NYC Public Advocate |
| `PermitApplication` | 3 | NYC Parks & Recreation, NYC Buildings (DOB), NYC Landmarks (LPC) |
| `Provider` | 3 | NYC Children's Services (ACS), NYC Youth & Community Dev (DYCD), NYC Health + Hospitals |
| `Violation` | 3 | NYC Buildings (DOB), NYC Business Integrity Commission (BIC), NYC Fire (FDNY) |
| `BoardAppointment` | 2 | Brooklyn Borough President, Manhattan Borough President |
| `BookHold` | 2 | Brooklyn Public Library (BPL), Queens Public Library (QPL) |
| `Building` | 2 | NYC Buildings (DOB), NYC Housing (HPD) |
| `Candidate` | 2 | NYC Board of Elections, NYC Campaign Finance Board (CFB) |
| `Case` | 2 | NYC Veterans' Services (DVS), Queens District Attorney |
| `CaseStatistics` | 2 | Brooklyn District Attorney, NYC Medical Examiner (OCME) |
| `Committee` | 2 | NYC Council, NYC Campaign Finance Board (CFB) |
| `Contract` | 2 | NYC Comptroller, NYC Youth & Community Dev (DYCD) |
| `DigitalCollection` | 2 | Brooklyn Public Library (BPL), Queens Public Library (QPL) |
| `DigitalItem` | 2 | NYC Records (DORIS), New York Public Library (NYPL) |
| `FundingAward` | 2 | Brooklyn Borough President, Manhattan Borough President |
| `Hearing` | 2 | NYC Standards & Appeals (BSA), NYC Admin Trials & Hearings (OATH) |
| `LibraryCard` | 2 | Brooklyn Public Library (BPL), Queens Public Library (QPL) |
| `LicenseApplication` | 2 | NYC Taxi & Limousine (TLC), NYC Consumer & Worker Protection (DCWP) |
| `Permit` | 2 | NYC Buildings (DOB), NYC Environmental Protection (DEP) |
| `Publication` | 2 | NYC Independent Budget Office (IBO), NYC Law Department |
| `Report` | 2 | Brooklyn Borough President, NYC Public Advocate |
| `Resolution` | 2 | NYC Standards & Appeals (BSA), Staten Island Borough President |
| `ServiceReferral` | 2 | NYC Aging (DFTA), NYC Veterans' Services (DVS) |
| `ServiceRequest` | 2 | NYC311, NYC Technology & Innovation (OTI) |
| `Vehicle` | 2 | NYC Taxi & Limousine (TLC), NYC Business Integrity Commission (BIC) |
| `VendorPrequalification` | 2 | NYC Design & Construction (DDC), NYC School Construction Authority (SCA) |

## All entities by domain

- **NYC Parks & Recreation** (`nycgovparks.org`) — `CapitalProject`, `Event`, `Facility`, `Monument`, `Park`, `PermitApplication`, `Tree`
- **NYC Public Schools (DOE)** (`schools.nyc.gov`) — `CalendarEvent`, `EnrollmentApplication`, `SchoolDemographics`, `School`, `TestResult`
- **NYC Council** (`council.nyc.gov`) — `Committee`, `CouncilMember`, `DiscretionaryFunding`, `District`, `Legislation`, `Meeting`, `TestimonyRegistration`
- **NYC Board of Elections** (`vote.nyc`) — `BallotRequest`, `Candidate`, `Contest`, `ElectionDistrict`, `ElectionResult`, `Election`, `PollSite`
- **NYC311** (`nyc311`) — `Agency`, `ServiceDefinition`, `ServiceRequest`, `ServiceType`
- **NYC Buildings (DOB)** (`dob`) — `Building`, `CertificateOfOccupancy`, `Complaint`, `JobFiling`, `PermitApplication`, `Permit`, `Violation`
- **NYC Housing (HPD)** (`hpd`) — `AffordableHousingProject`, `Building`, `Complaint`, `HousingLotteryApplication`, `LitigationCase`, `Registration`, `HousingMaintenanceViolation`
- **NYC Transportation (DOT)** (`dot`) — `BikeRoute`, `Bridge`, `ParkingRegulation`, `PedestrianPlaza`, `SpeedHump`, `StreetWorkPermit`, `TrafficSignal`
- **NYC Health (DOHMH)** (`dohmh`) — `ChildcareCenter`, `EnvironmentalComplaint`, `FoodEstablishment`, `HealthFacility`, `Inspection`, `RodentInspection`, `VitalRecordRequest`
- **NYC Sanitation (DSNY)** (`dsny`) — `BulkPickupRequest`, `CollectionSchedule`, `DropOffSite`, `LitterBasket`, `SanitationDistrict`, `Tonnage`
- **NYPD** (`nypd`) — `Arrest`, `ComplaintReport`, `Officer`, `PoliceReportRequest`, `Precinct`, `ShootingIncident`
- **NYC Taxi & Limousine (TLC)** (`tlc`) — `Base`, `DriverLicense`, `Inspection`, `LicenseApplication`, `TaxiZone`, `TripRecord`, `Vehicle`
- **NYC City Planning (DCP)** (`dcp`) — `CensusGeography`, `CommunityDistrict`, `LandUseApplication`, `NTA`, `TaxLot`, `ZoningDistrict`
- **NYC Comptroller** (`comptroller.nyc.gov`) — `Audit`, `ClaimFiling`, `ClaimAgainstCity`, `Contract`, `PensionHolding`, `SpendingTransaction`
- **NYC Housing Authority (NYCHA)** (`nycha`) — `CommunityFacility`, `Development`, `ResidentStatistics`, `ResidentialAddress`, `UtilityConsumption`, `WorkOrder`
- **NYC Children's Services (ACS)** (`acs`) — `ChildCareComplaint`, `ChildWelfareIndicator`, `FosterCareStatistics`, `JuvenileJusticeStatistics`, `PreventionService`, `Provider`
- **NYC Business Integrity Commission (BIC)** (`bic`) — `Complaint`, `Licensee`, `MarketBusiness`, `Registrant`, `TradeWasteLicenseApplication`, `Vehicle`, `Violation`
- **Brooklyn Public Library (BPL)** (`bklynlibrary`) — `BookHold`, `Branch`, `CatalogItem`, `DigitalCollection`, `ElectronicResource`, `Event`, `LibraryCard`
- **Bronx Borough President** (`bronxbp`) — `CommunityBoardApplication`, `CommunityBoardAppointment`, `DiscretionaryFundingAward`, `Event`, `LandUseRecommendation`, `PressRelease`
- **Bronx District Attorney** (`bronxda`) — `CaseStatistic`, `CommunityResource`, `PressRelease`, `Program`, `TipSubmission`, `VictimService`
- **Brooklyn Borough President** (`brooklynbp`) — `BoardAppointment`, `CommunityBoardApplication`, `CommunityBoard`, `Event`, `FundingAward`, `LandUseRecommendation`, `Report`
- **Brooklyn District Attorney** (`brooklynda`) — `CaseStatistics`, `CommunityResource`, `PressRelease`, `Program`, `TipSubmission`, `VictimService`
- **NYC Standards & Appeals (BSA)** (`bsa`) — `Application`, `Hearing`, `PreApplicationMeeting`, `Resolution`, `VarianceApplication`, `ZoningLot`
- **NYC Human Rights (CCHR)** (`cchr`) — `DiscriminationComplaint`, `InquiryStatistic`, `LegalGuidance`, `ProtectedClass`, `ResolutionStatistic`, `TrainingEvent`
- **NYC Civilian Complaint Review (CCRB)** (`ccrb`) — `Allegation`, `Complaint`, `MisconductComplaint`, `Penalty`, `PoliceOfficer`
- **NYC Campaign Finance Board (CFB)** (`cfb`) — `Candidate`, `Committee`, `Contribution`, `DisclosureFiling`, `Expenditure`, `PublicMatchingFundsPayment`
- **NYC City Clerk** (`cityclerk`) — `Ceremony`, `FundraisingReport`, `LobbyistFiling`, `LobbyistRegistration`, `MarriageLicenseApplication`, `MarriageLicense`
- **NYC Conflicts of Interest Board (COIB)** (`coib`) — `AdvisoryOpinion`, `AgencyDonation`, `EnforcementDisposition`, `FinancialDisclosureFiling`, `LegalDefenseTrustTransaction`, `Policymaker`
- **City University of New York (CUNY)** (`cuny`) — `AdmissionsApplication`, `Campus`, `Course`, `DegreeProgram`, `EnrollmentStatistics`, `FacultyResearch`
- **NYC Citywide Admin Services (DCAS)** (`dcas`) — `CityBuilding`, `CivilServiceTitle`, `EligibleListEntry`, `ExamRegistration`, `ExamSchedule`, `FleetVehicle`, `JobPosting`
- **NYC Cultural Affairs (DCLA)** (`dcla`) — `CapitalFunding`, `CulturalInstitution`, `CulturalOrganization`, `GrantApplication`, `MaterialsForTheArts`, `ProgramFunding`, `PublicArtwork`
- **NYC Consumer & Worker Protection (DCWP)** (`dcwp`) — `BusinessLicense`, `Charge`, `ConsumerComplaint`, `Inspection`, `LicenseApplication`, `WorkerProtectionCase`
- **NYC Design & Construction (DDC)** (`ddc`) — `AwardedContract`, `CapitalProject`, `Division`, `Solicitation`, `VendorPrequalification`, `Vendor`
- **NYC Environmental Protection (DEP)** (`dep`) — `GreenInfrastructure`, `Hydrant`, `Permit`, `ReservoirLevel`, `WaterConsumption`, `WaterQualitySample`, `WaterServiceRequest`
- **NYC Aging (DFTA)** (`dfta`) — `OlderAdultCenter`, `Participation`, `ProgramActivity`, `ServiceProvider`, `ServiceReferral`, `ServiceUnit`
- **NYC Homeless Services (DHS)** (`dhs`) — `DHSContact`, `DropInCenter`, `OutreachRequest`, `ShelterCensus`, `ShelterFacility`, `StreetHomelessCount`
- **NYC Correction (DOC)** (`doc`) — `Complaint`, `DailyPopulation`, `Facility`, `IncidentReport`, `PersonInCustody`, `Visit`
- **NYC Finance (DOF)** (`dof`) — `ACRISDocument`, `ParkingTicketPayment`, `ParkingViolation`, `PropertyExemption`, `PropertyTaxBill`, `PropertyValuation`
- **NYC Investigation (DOI)** (`doi`) — `CorruptionComplaint`, `Eviction`, `MarshalRevenue`, `PerformanceIndicator`, `PolicyRecommendation`, `PublicReport`
- **NYC Records (DORIS)** (`doris`) — `ArchivalCollection`, `DigitalItem`, `GovernmentPublication`, `HistoricalVitalRecord`, `HonoraryStreetName`, `RecordsRequest`
- **NYC Veterans' Services (DVS)** (`dvs`) — `AssistanceRequest`, `Case`, `ClientStatistics`, `ServiceReferral`, `VeteranOwnedBusiness`, `VeteranResource`
- **NYC Youth & Community Dev (DYCD)** (`dycd`) — `Contract`, `ParticipantDemographics`, `ProgramApplication`, `ProgramSite`, `Program`, `Provider`, `ServiceArea`
- **NYC Economic Development (EDC)** (`edc`) — `DevelopmentProject`, `FerryRidership`, `MappedCompany`, `PropertyAsset`, `RFPResponse`, `Solicitation`, `WiredBuilding`
- **NYC Fire (FDNY)** (`fdny`) — `CertificateOfFitness`, `FirePermitApplication`, `Firehouse`, `IncidentDispatch`, `Inspection`, `Violation`
- **NYC Health + Hospitals** (`hhc`) — `AppointmentRequest`, `Appointment`, `Facility`, `FinancialAssistance`, `Pharmacy`, `Provider`, `Service`
- **NYC Social Services (HRA)** (`hra`) — `BenefitsApplication`, `BenefitsEligibility`, `CaseAction`, `CaseloadStatistic`, `Center`, `Program`
- **NYC Independent Budget Office (IBO)** (`ibo`) — `DataRequest`, `FiscalDataTable`, `FiscalSeries`, `Publication`, `SchoolSpending`, `TaxDistribution`
- **NYC Law Department** (`law`) — `LawInternshipApplication`, `LegalCase`, `LegalDivision`, `MwbeStatistic`, `PublicServiceProgram`, `Publication`
- **NYC Landmarks (LPC)** (`lpc`) — `DesignatedBuilding`, `DesignationReport`, `HistoricDistrict`, `LandmarkPermitApplication`, `Landmark`, `PermitApplication`, `ViolationOrder`
- **Manhattan Borough President** (`manhattanbp`) — `BoardAppointment`, `CommunityBoardApplication`, `CommunityBoard`, `ConstituentCase`, `FundingAward`, `LandUseRecommendation`, `Legislation`
- **Manhattan District Attorney** (`manhattanda`) — `Office`, `PressRelease`, `Program`, `Prosecution`, `TipSubmission`, `VictimService`
- **NYC Criminal Justice (MOCJ)** (`mocj`) — `DataReport`, `JailPopulationMetric`, `ProgramReferral`, `Program`, `Solicitation`, `SupervisedReleaseDocket`
- **NYC Media & Entertainment (MOME)** (`mome`) — `FilmPermitApplication`, `FilmPermit`, `MarchInspection`, `MediaProgram`, `ProductionCompany`, `ScreenActivity`
- **NYC Emergency Management (NYCEM)** (`nycem`) — `EmergencyIncident`, `EmergencyNotification`, `EvacuationCenter`, `HurricaneEvacuationZone`, `MitigationAction`, `NotifyNYCSubscription`, `PreparednessResource`
- **New York Public Library (NYPL)** (`nypl`) — `Branch`, `CatalogItem`, `Collection`, `DigitalItem`, `Event`, `Hold`
- **NYC Admin Trials & Hearings (OATH)** (`oath`) — `Decision`, `Hearing`, `SummonsDispute`, `Summons`, `TrialCase`
- **NYC Medical Examiner (OCME)** (`ocme`) — `CaseStatistics`, `DeathRecordRequest`, `FamilyServicesCenter`, `ForensicService`, `MissingPerson`, `MonthlyIndicator`
- **NYC Technology & Innovation (OTI)** (`oti`) — `APIGatewayService`, `BroadbandAsset`, `LinkNYCKiosk`, `OpenDataset`, `ServiceRequest`, `WiFiHotspot`
- **NYC Public Advocate** (`pubadvocate`) — `Legislation`, `OmbudsmanComplaint`, `PublicInterestRequest`, `Report`, `WatchlistBuilding`, `WorstLandlord`
- **Queens Borough President** (`queensbp`) — `CommunityBoardApplication`, `CommunityBoardAppointment`, `CommunityBoard`, `DiscretionaryFundingAward`, `Event`, `LandUseRecommendation`, `PressRelease`
- **Queens District Attorney** (`queensda`) — `Case`, `ColdCase`, `CommunityResource`, `PressRelease`, `Program`, `TipSubmission`, `VictimService`
- **Queens Public Library (QPL)** (`queenslibrary`) — `BookHold`, `Branch`, `CatalogItem`, `DigitalCollection`, `Event`, `LibraryCard`
- **NYC Small Business Services (SBS)** (`sbs`) — `BusinessImprovementDistrict`, `BusinessIncentive`, `CertifiedBusiness`, `JobListing`, `MWBECertificationApplication`, `ServiceLocation`, `WorkforceEvent`
- **NYC School Construction Authority (SCA)** (`sca`) — `CapitalProject`, `EnrollmentCapacity`, `Inspection`, `PrequalifiedFirm`, `Solicitation`, `UpcomingContract`, `VendorPrequalification`
- **Staten Island Borough President** (`statenislandbp`) — `CommunityBoardApplication`, `CommunityBoardAppointment`, `ConstituentRequest`, `DiscretionaryFundingAward`, `Event`, `LandUseRecommendation`, `Resolution`
- **Staten Island District Attorney** (`statenislandda`) — `CommunityResource`, `PressRelease`, `Program`, `ProsecutionStatistics`, `TipSubmission`, `VictimService`
- **NYC Tax Commission** (`taxcommission`) — `Article7Petition`, `AssessmentAction`, `AssessmentAppeal`, `Determination`, `Property`, `Representative`
