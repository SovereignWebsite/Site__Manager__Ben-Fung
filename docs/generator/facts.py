"""Ben Fung's career facts, the one source every design draws on.

From Ben's Public Professional Profile v1.0 (his own JSON, 26 Nov 2026; not published), with his corrections
given in keeper.ben's session the same day: at Gatwick the project was a mobile device refresh, including
Mobile Device Management (MDM) enrolment, device profiles and correcting the asset management database records
(not master data management); he was responsible for a 2m pound budget on it; through his recommendation Gatwick
avoided 1m pounds of implementation spend; and (Ben, later the same day) his recommendation to cancel the
infrastructure monitoring project avoided a 50k pounds a year increase in licensing costs. Keep every line traceable to those; never add a fact here without a source.
"""
MON = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def when(s, e):
    sy, sm = s.split("-"); ey, em = e.split("-")
    a, b = MON[int(sm) - 1], MON[int(em) - 1]
    return f"{a} to {b} {sy}" if sy == ey else f"{a} {sy} to {b} {ey}"


ARR = {"consultancy": "Consultancy", "contract": "Contract", "other": "Associate", "unknown": None}


def arr(a):
    return f'<span class="arr">{ARR[a]}</span>' if ARR[a] else ""


# Every line below is taken from Ben's Public Professional Profile v1.0 (career facts), wording kept close.
RECENT = [
    ("Gatwick Airport", "Senior Project Manager", "2026-01", "2026-08", "consultancy",
     "Led a mobile device refresh project through formal service-management acceptance, responsible for its &#163;2m budget. It included Mobile Device Management (MDM) enrolment, creating the device profiles and correcting the asset management database records. He also assessed options for consolidating infrastructure monitoring tools.",
     ["Completed the correction of the asset management records within budget and secured formal operational acceptance.",
      "Managed monthly cost forecasts, supplier invoice approvals and supplier handover.",
      "Presented the options for consolidating infrastructure monitoring tools and recommended cancelling the project. Through his recommendation, Gatwick avoided &#163;1m of implementation spend and an increase of &#163;50k a year in licensing costs.",
      "Improved visibility of upcoming deployments so teams could plan resources earlier."]),
    ("HX / Hurtigruten Expeditions", "Separation Consultant", "2025-02", "2025-06", "consultancy",
     "Defined transition policies and facilitated master-data workshops for the Seaware ERP transition.",
     ["Defined master-data structure and transition policies for the Seaware ERP separation.",
      "Facilitated master-data workshops across business categories and presented transition risks to board stakeholders."]),
    ("easyJet", "Programme Manager", "2023-09", "2024-12", "consultancy",
     "Led the Agresso/Unit4 ERP migration to SaaS and coordinated application migrations supporting the data-centre exit.",
     ["Matrix-managed five project managers and coordinated dependencies, risks and reporting across assigned projects.",
      "Led integration testing, cutover and stabilisation for the Unit4 ERP move to SaaS.",
      "Completed the ERP migration and required integrations by the fixed data-centre exit deadline, with no components deferred.",
      "Across applications under his accountability, migrations had no unplanned outages.",
      "Obtained business-lead sign-off that training had been delivered to impacted teams."]),
    ("London Stock Exchange Group", "Cyber Security Senior Project Manager", "2022-05", "2023-05", "consultancy",
     "Led delivery of D3 security orchestration and automation, coordinated tooling integrations and established an in-house cyber forensics capability.",
     ["Delivered the D3 security orchestration and automation implementation to schedule and budget.",
      "Coordinated integration of monitoring, service management and endpoint security tools.",
      "Established an in-house cyber forensics capability."]),
]

PHASES = [
    ("2018 to 2022", "Security, procurement and resilience consulting",
     "Short consultancy engagements across government, policing and financial services. Some ran at the same time; the dates are as given.",
     [("Defra", "Technology Infrastructure Consultant", "2022-01", "2022-02", "consultancy", "Assessed infrastructure resilience and documented recommendations following an external audit."),
      ("HMRC", "Security operating model consulting<small> (a description of the work, not a job title)</small>", "2021-01", "2021-03", "consultancy", "Coordinated the definition and stakeholder review of cybersecurity services. The definitions were still in review when the engagement ended."),
      ("Metropolitan Police Service", "Senior Consultant", "2020-04", "2020-11", "consultancy", "Supported procurement for an integration-platform upgrade: requirements and supplier workshops, evaluation scoring, training evaluators."),
      ("National Crime Agency", "Senior Consultant / Procurement", "2020-02", "2020-05", "consultancy", "Developed a standard framework for lower-value technology procurement."),
      ("M&amp;G", "Operational Resilience Senior Consultant", "2019-08", "2020-01", "consultancy", "Helped assess infrastructure resilience across the prioritised pipeline for separation from Prudential."),
      ("Metropolitan Police Service", "Senior Consultant / Procurement", "2019-05", "2019-08", "consultancy", "Managed requirements and supplier evaluation for the Command &amp; Control procurement."),
      ("National Crime Agency", "Senior Consultant", "2019-01", "2019-04", "consultancy", "Supported competitive procurement for a strategic technology partner: requirements, supplier scoring models, bidder clarifications."),
      ("HMRC / Home Office", "Senior Consultant", "2018-01", "2018-10", "consultancy", "Helped develop the security target operating model, service catalogue and process handoffs.")]),
    ("2009 to 2016", "Programme and project management",
     "Separation, migration, automation and portfolio work in financial services and government.",
     [("HMRC", "IT Solution Programme Manager", "2015-10", "2016-10", "consultancy", "Managed the integrated application, data and user migration plan for his assigned delivery within the Columbus programme."),
      ("Credit Suisse", "Portfolio Optimisation &amp; ServiceNow Programme Manager", "2014-03", "2015-09", "consultancy", "Led ServiceNow provisioning automation and developed a weighted scoring framework for portfolio prioritisation."),
      ("Direct Line Group", "Separation Project Manager, Applications", "2011-11", "2013-12", "consultancy", "Managed Direct Line Group&#8217;s side of the separation from RBS, covering mainframe systems and migration of applications and websites."),
      ("Nomura", "Fixed Income Project Manager", "2010-02", "2011-06", "consultancy", "Managed fixed-income technology delivery."),
      ("Coller Capital", "Technology Outsourcing Programme Consultant", "2009-04", "2009-11", "consultancy", "Advised on technology outsourcing.")]),
    ("1997 to 2009", "From infrastructure engineering to project leadership",
     "Server and infrastructure engineering, then technical and project leadership.",
     [("MF Global", "Technical Lead, Enterprise Security Management Project (CyberArk)", "2008-04", "2009-03", "contract", "Provided technical leadership for a CyberArk enterprise security management project."),
      ("MF Global", "Project Lead, Virtualisation Project (VMware)", "2007-06", "2008-05", "contract", "Led VMware virtualisation and server decommissioning, including hands-on engineering. The project decommissioned more than 200 servers."),
      ("WPP", "Group ERP Technical Solution Consultant", "2006-11", "2007-04", "contract", "Provided technical consulting for group ERP."),
      ("Man Financial", "Wintel Infrastructure Engineer", "2003-05", "2006-10", "contract", "Worked in Windows infrastructure engineering."),
      ("Australian Stock Exchange", "Information Technology Infrastructure Engineer", "2000-11", "2003-02", "unknown", "Worked in IT infrastructure engineering."),
      ("Westpac", "Server Support Engineer", "1997-03", "2000-10", "unknown", "Supported server infrastructure.")]),
]

OUTCOMES = [
    ("Commercial judgement", "&#163;1m implementation spend avoided",
     "Assessing a proposed project to consolidate infrastructure monitoring tools, he recommended cancelling it. Through his recommendation, Gatwick avoided &#163;1m of implementation spend and an increase of &#163;50k a year in licensing costs. He also led a mobile device refresh with a &#163;2m budget, including Mobile Device Management (MDM) enrolment and device profiles, and completed the correction of the asset management records within budget, with formal operational acceptance.",
     None, "Gatwick Airport · Senior Project Manager · 2026"),
    ("Deadline delivery", "No components deferred",
     "Completed the Unit4 ERP migration to SaaS and its required integrations by the fixed data-centre exit deadline. Across the applications under his accountability, migrations had no unplanned outages.",
     "The wider data-centre exit programme decommissioned approximately 150 servers.",
     "easyJet · Programme Manager · 2023 to 2024"),
    ("Cyber security", "To schedule and budget",
     "Delivered the D3 security orchestration and automation implementation, coordinated the tooling integrations and established an in-house cyber forensics capability.",
     None, "London Stock Exchange Group · 2022 to 2023"),
    ("Go-live quality", "Zero priority-one defects",
     "Met the deadline for his assigned migration delivery in the Columbus programme, with zero priority-one defects at go-live and through stabilisation.",
     None, "HMRC · IT Solution Programme Manager · 2015 to 2016"),
    ("Automation", "About 15 working days to one",
     "Led ServiceNow automation that reduced measured virtual-server provisioning processing time from approximately 15 working days to one. The comparison excluded time waiting for manual business-owner approval.",
     None, "Credit Suisse · 2014 to 2015"),
    ("Procurement", "Scoring a major procurement",
     "Built the scoring calculations, trained the evaluators and consolidated evaluation scores for the 2019 Command &amp; Control procurement, after managing the requirements and bidder clarifications.",
     None, "Metropolitan Police Service · 2019"),
]

CAPS = [
    ("Delivery and governance", ["Programme and project delivery", "Senior stakeholder governance", "Risk, issue and dependency management", "Matrix team leadership", "Agile and hybrid delivery", "Project recovery"]),
    ("Migration and implementation", ["Cloud and data-centre migration", "Enterprise SaaS implementation", "Data migration and integration coordination", "Testing, cutover and stabilisation"]),
    ("Commercial and procurement", ["Commercial and budget management", "Supplier and contract management", "Procurement and vendor evaluation"]),
    ("Security and separation", ["Security and target operating model design", "Business separation and transition", "Infrastructure engineering and virtualisation (earlier career)"]),
]

