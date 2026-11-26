from common import *

STYLE = r"""
:root{--bg:#f7f5f0;--paper:#fffdf8;--fg:#17201d;--muted:#4c5753;--accent:#0f6b58;--accent-2:#b4532a;--line:#dcd6c8;--chip:#e9f2ee;
  --sw-fg:#36403c;--sw-line:#cfc8b8;--sw-on-bg:#0f6b58;--sw-on-fg:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#101715;--paper:#151e1b;--fg:#ecefe9;--muted:#aab6b0;--accent:#6fd3b6;--accent-2:#f0a27c;--line:#2a3531;--chip:#1b2a25;
  --sw-fg:#cfd8d3;--sw-line:#34413c;--sw-on-bg:#6fd3b6;--sw-on-fg:#0b1311;--family-fg:#c4ccc8;--family-fg-strong:#fff;--family-bg:#1c1c1c}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.6 Inter,system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:var(--accent)}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.serif{font-family:"Iowan Old Style","Charter","Bitstream Charter",Georgia,serif}
.wrap{max-width:64rem;margin:0 auto;padding:0 1.25rem}
.top{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem 1.5rem;max-width:64rem;margin:0 auto;padding:.6rem 1.25rem 0}
.top .name{font-weight:700;color:var(--fg);text-decoration:none;letter-spacing:-.01em}
.own{display:flex;gap:1rem;margin-left:auto;font-size:.95rem}.own a{font-weight:600}
.hero{display:grid;grid-template-columns:auto 1fr;gap:2.5rem;align-items:center;padding:3.5rem 0 2.5rem}
.portrait{width:13rem;height:13rem;border-radius:50%;object-fit:cover;border:6px solid var(--paper);box-shadow:0 0 0 2px var(--accent),0 18px 40px rgba(0,0,0,.15)}
.eyebrow{font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);font-weight:700;margin:0 0 .5rem}
h1{font-size:clamp(2.6rem,7vw,4.6rem);line-height:1;margin:0 0 1rem;letter-spacing:-.03em}
.lede{font-size:clamp(1.1rem,2.2vw,1.35rem);color:var(--muted);margin:0 0 1.4rem;max-width:40rem}
.cta{display:flex;flex-wrap:wrap;gap:.75rem}
.btn{display:inline-block;padding:.7rem 1.2rem;border-radius:999px;font-weight:600;text-decoration:none;border:2px solid var(--accent)}
.btn.primary{background:var(--accent);color:var(--paper)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(11rem,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:14px;overflow:hidden;margin:1rem 0 4rem}
.stat{background:var(--paper);padding:1.3rem 1.2rem}
.stat b{display:block;font-size:2rem;line-height:1.1;letter-spacing:-.02em;color:var(--fg)}
.stat span{font-size:.9rem;color:var(--muted)}
h2{font-size:clamp(1.6rem,3.5vw,2.3rem);letter-spacing:-.02em;margin:0 0 .4rem;line-height:1.15}
.sub{color:var(--muted);margin:0 0 2rem;max-width:42rem}
.path{list-style:none;margin:0 0 4rem;padding:0;position:relative}
.path::before{content:"";position:absolute;left:7.25rem;top:.6rem;bottom:.6rem;width:3px;background:linear-gradient(var(--line),var(--accent))}
.step{display:grid;grid-template-columns:6.5rem 1fr;gap:2.25rem;padding:0 0 2.4rem;position:relative}
.step::before{content:"";position:absolute;left:6.8rem;top:.45rem;width:1.2rem;height:1.2rem;border-radius:50%;background:var(--bg);border:3px solid var(--accent)}
.step.now::before{background:var(--accent-2);border-color:var(--accent-2);box-shadow:0 0 0 6px color-mix(in srgb,var(--accent-2) 25%,transparent)}
.when{text-align:right;font-weight:700;font-variant-numeric:tabular-nums;color:var(--fg);font-size:.95rem;padding-top:.2rem}
.when small{display:block;font-weight:500;color:var(--muted)}
.card{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:1.3rem 1.4rem}
.card h3{margin:0;font-size:1.25rem;letter-spacing:-.01em}
.card .org{color:var(--accent);font-weight:600;margin:.1rem 0 .7rem}
.card p{margin:0 0 .7rem;color:var(--muted)}
.card ul{margin:.2rem 0 0;padding-left:1.1rem;color:var(--muted)}.card li{margin:.3rem 0}
.card .tags{padding-left:0}
.tags{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.8rem;padding:0;list-style:none}
.tags li{background:var(--chip);color:var(--fg);border-radius:999px;padding:.2rem .7rem;font-size:.82rem;margin:0}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:1rem;margin:0 0 1rem}
.grid2.four{grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));margin-bottom:4rem}
.glance{display:grid;grid-template-columns:repeat(auto-fit,minmax(12rem,1fr));gap:.4rem 1.5rem;margin:0 0 1.2rem;padding:1rem 1.2rem;border-left:4px solid var(--accent-2);background:var(--paper);border-radius:0 12px 12px 0}
.glance div{font-size:.95rem}.glance dt{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:700}.glance dd{margin:0;font-weight:600}
.mini h3{font-size:1.05rem}
.quote{font-size:clamp(1.3rem,3vw,1.9rem);line-height:1.35;margin:0 0 4rem;padding:2rem 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);max-width:52rem}
.quote p{margin:0}
.contact{background:var(--fg);color:var(--bg);border-radius:20px;padding:2.4rem 2rem;margin:0 0 3rem}
.contact h2{color:var(--bg)}.contact p{color:var(--bg);opacity:.9;max-width:40rem}
.contact a{color:var(--bg);font-weight:700}
.contact .btn{border-color:var(--bg)}
footer{border-top:1px solid var(--line);padding:1.5rem 0 1rem;font-size:.9rem;color:var(--muted)}
footer a{color:var(--accent);font-weight:600}
@media (max-width:44rem){
  .hero{grid-template-columns:1fr;gap:1.5rem;padding-top:2rem}.portrait{width:9rem;height:9rem}
  .path::before{left:.55rem}.step{grid-template-columns:1fr;gap:.4rem;padding-left:2.2rem}.step::before{left:0}.when{text-align:left}
  .own{margin:0;width:100%}
  .stats{grid-template-columns:1fr 1fr}.stat:last-child{grid-column:1/-1}.stat{padding:.9rem}.stat b{font-size:1.5rem}.glance{grid-template-columns:1fr 1fr;gap:.6rem 1rem}.card{padding:1rem}.step{padding-bottom:1.4rem}.grid2.four{margin-bottom:2.5rem}.stats{margin-bottom:2.5rem}.path{margin-bottom:2.5rem}
}
.outcomes{display:grid;grid-template-columns:repeat(auto-fit,minmax(18rem,1fr));gap:1rem;margin:0 0 4rem;padding:0;list-style:none}
.outcome{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:1.3rem 1.4rem;display:flex;flex-direction:column}
.outcome .kind{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-2);font-weight:700;margin:0}
.outcome .big{font-size:1.75rem;line-height:1.15;letter-spacing:-.02em;font-weight:700;margin:.35rem 0 .5rem;color:var(--fg)}
.outcome p{margin:0 0 .6rem;color:var(--muted)}
.outcome .where{margin-top:auto;padding-top:.6rem;border-top:1px solid var(--line);font-size:.9rem;color:var(--fg)}
.outcome .team{font-size:.9rem;font-style:italic}
.caps{display:grid;grid-template-columns:repeat(auto-fit,minmax(14rem,1fr));gap:1rem;margin:0 0 4rem}
.caps h3{font-size:1rem;margin:0 0 .3rem}
.arr{display:inline-block;font-size:.78rem;font-weight:600;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:.05rem .6rem;margin-left:.3rem;vertical-align:.1em;white-space:nowrap}
.phase{margin:0 0 2.5rem}
.phase h3{font-size:1.3rem;margin:0 0 .2rem}
.phase .sub{margin-bottom:1rem}
.rows{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.rows li{display:grid;grid-template-columns:11rem 1fr;gap:.2rem 1.5rem;padding:.8rem 0;border-bottom:1px solid var(--line)}
.rows .d{font-variant-numeric:tabular-nums;font-weight:600;font-size:.95rem}
.rows .r{font-weight:600}.rows .o{color:var(--accent);font-weight:600}
.rows p{margin:.15rem 0 0;color:var(--muted);font-size:.95rem}
.note{background:var(--paper);border-left:4px solid var(--accent-2);border-radius:0 12px 12px 0;padding:1rem 1.2rem;margin:0 0 2.5rem;color:var(--muted)}
.note strong{color:var(--fg)}
.inprog{color:var(--accent-2);font-weight:700}
@media (max-width:44rem){.rows li{grid-template-columns:1fr}.outcomes,.caps{margin-bottom:2.5rem}.outcome .big{font-size:1.45rem}}
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
     "Led master data quality remediation through formal service-management acceptance and assessed options for consolidating monitoring tools.",
     ["Completed master data remediation within budget and secured formal operational acceptance.",
      "Managed monthly cost forecasts, supplier invoice approvals and supplier handover.",
      "Presented monitoring consolidation options and recommended against proceeding with the proposal as scoped.",
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
    ("Deadline delivery", "No components deferred",
     "Completed the Unit4 ERP migration to SaaS and its required integrations by the fixed data-centre exit deadline. Across the applications under his accountability, migrations had no unplanned outages.",
     "The wider data-centre exit programme decommissioned approximately 150 servers.",
     "easyJet · Programme Manager · 2023 to 2024"),
    ("Commercial control", "Within budget, formally accepted",
     "Completed master data quality remediation within budget and secured formal operational acceptance, managing monthly cost forecasts and supplier invoice approvals.",
     None, "Gatwick Airport · Senior Project Manager · 2026"),
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


def tags(xs):
    return '<ul class="tags">' + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"


def page():
    c = contact_links("btn")
    links = " ".join(c[:1]).replace('class="btn"', 'class="btn primary"') + (" " + c[1] if len(c) > 1 else "")
    outcomes = "\n".join(
        f'<li class="outcome"><p class="kind">{k}</p><p class="big">{b}</p><p>{t}</p>'
        + (f'<p class="team">{team}</p>' if team else "") + f'<p class="where">{w}</p></li>'
        for k, b, t, team, w in OUTCOMES)
    caps = "\n".join(f'<div class="card mini"><h3>{h}</h3>{tags(xs)}</div>' for h, xs in CAPS)
    recent = []
    for i, (o, r, s, e, a, scope, hl) in enumerate(RECENT):
        recent.append(f"""  <li class="step{' now' if i == 0 else ''}">
    <div class="when">{when(s, e)}</div>
    <div class="card">
      <h3>{r}</h3>
      <p class="org">{o} {arr(a)}</p>
      <p>{scope}</p>
      <ul>{''.join(f'<li>{h}</li>' for h in hl)}</ul>
    </div>
  </li>""")
    phases = []
    for span, title, intro, rows in PHASES:
        rr = "\n".join(f'<li><span class="d">{when(s, e)}</span><div><span class="r">{r}</span>, <span class="o">{o}</span> {arr(a)}<p>{d}</p></div></li>' for o, r, s, e, a, d in rows)
        phases.append(f'<section class="phase"><h3>{span}: {title}</h3><p class="sub">{intro}</p><ol class="rows">\n{rr}\n</ol></section>')
    return head("Ben Fung, technology programme and project delivery", "/", STYLE) + f"""<header class="top">
  <a class="name" href="/">Ben Fung</a>
  <nav class="own" aria-label="This site">
    <a href="/start/">Start here</a>
    <a href="/agents/">Use with your AI</a>
  </nav>
</header>
{switcher("path")}
<main id="main" class="wrap">
<section class="hero" aria-labelledby="who">
  <img class="portrait" src="/assets/img/ben-fung-400.jpg" srcset="/assets/img/ben-fung-400.jpg 400w, /assets/img/ben-fung-800.jpg 800w" sizes="13rem" width="400" height="400" alt="Ben Fung, smiling, in a dark jacket and striped shirt">
  <div>
    <p class="eyebrow">Technology programme and project delivery</p>
    <h1 id="who">Ben Fung</h1>
    <p class="lede serif">Ben Fung leads technology change across aviation, financial services and government. His work covers enterprise migrations, business separation, cybersecurity delivery and operational resilience, building on an earlier career in infrastructure engineering.</p>
    <div class="cta">{links}</div>
  </div>
</section>

<section aria-labelledby="does">
<h2 id="does">What he does</h2>
<p class="sub">The capabilities he brings to a programme, grouped.</p>
<div class="caps">
{caps}
</div>
</section>

<section aria-labelledby="out">
<h2 id="out">Selected outcomes</h2>
<p class="sub">Six results, each showing a different strength. Each figure belongs to the project named beneath it; where a result was the wider programme&#8217;s rather than his, it says so.</p>
<ul class="outcomes">
{outcomes}
</ul>
</section>

<section aria-labelledby="recent">
<h2 id="recent">Recent roles</h2>
<p class="sub">His four most recent engagements, newest first. All were consultancy engagements with the client named.</p>
<ol class="path">
{chr(10).join(recent)}
</ol>
</section>

<section aria-labelledby="earlier">
<h2 id="earlier">Earlier career</h2>
<p class="sub">Grouped into three phases, newest first. Each role shows how it was held: a consultancy engagement, a contract, or nothing where the arrangement is not stated.</p>
<p class="note"><strong>Finyx Consulting, Associate Consultant, Mar 2009 to Jun 2023.</strong> An associate consultancy relationship that spanned overlapping client assignments.</p>
{chr(10).join(phases)}
</section>

<section aria-labelledby="creds">
<h2 id="creds">Certifications and professional development</h2>
<div class="grid2">
  <article class="card mini"><h3>PRINCE2 Practitioner</h3><p>Achieved</p></article>
  <article class="card mini"><h3>ITIL v3</h3><p>Achieved</p></article>
  <article class="card mini"><h3>Microsoft Certified: AI Transformation Leader</h3><p>Exam AB-731 · <span class="inprog">In progress</span></p></article>
</div>
</section>

<section class="contact" aria-labelledby="talk">
  <h2 id="talk">Talk to Ben</h2>
  <p>To talk about a technology programme or project, email Ben.</p>
  <p>{" · ".join(contact_links())}</p>
</section>
</main>
<footer class="wrap">
{site_links()}
{credit_line()}
</footer>
""" + END
