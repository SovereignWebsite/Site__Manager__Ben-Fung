from common import *

STYLE = r"""
:root{--bg:#f3efe6;--fg:#141414;--muted:#3f3f3f;--rule:#141414;--soft:#c9c1ae;--red:#a1121a;
  --sw-fg:#2b2b2b;--sw-line:#bfb7a4;--sw-on-bg:#141414;--sw-on-fg:#f3efe6}
@media (prefers-color-scheme:dark){:root{--bg:#191714;--fg:#eee8dc;--muted:#c5bdad;--rule:#eee8dc;--soft:#4a453c;--red:#ff8a8f;
  --sw-fg:#ddd6c8;--sw-line:#4a453c;--sw-on-bg:#eee8dc;--sw-on-fg:#191714;--family-fg:#cfc8ba;--family-fg-strong:#fff;--family-bg:#1c1c1c}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.55 "Iowan Old Style","Charter","Bitstream Charter",Georgia,serif}
a{color:var(--fg)}
main{max-width:70rem;margin:0 auto;padding:0 1.25rem 2rem}
.sans{font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif}
.mast{text-align:center;border-bottom:4px double var(--rule);padding:1rem 0 .6rem}
.mast .tag{font:600 .72rem/1 Inter,system-ui,sans-serif;letter-spacing:.24em;text-transform:uppercase;color:var(--muted);margin:0}
.mast .title{font-size:clamp(2.6rem,9vw,5.6rem);font-weight:700;letter-spacing:-.02em;line-height:1;margin:.4rem 0 .5rem;font-family:"Bitstream Charter","Charter",Georgia,serif}
.dateline{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:.35rem 0;font:600 .78rem/1.3 Inter,system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;margin-top:.4rem}
.front{display:grid;grid-template-columns:2fr 1fr;gap:2rem;padding:1.6rem 0;border-bottom:1px solid var(--rule)}
.kicker{font:700 .78rem/1 Inter,system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--red);margin:0 0 .6rem}
h1{font-size:clamp(2rem,5vw,3.4rem);line-height:1.05;margin:0 0 .8rem;letter-spacing:-.015em}
.stand{font-size:1.25rem;line-height:1.45;color:var(--muted);margin:0 0 1rem;font-style:italic}
.byline{font:600 .8rem/1.3 Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);border-top:1px solid var(--soft);padding-top:.5rem}
figure{margin:0}
figure{position:relative}figure img{width:100%;height:auto;aspect-ratio:1;object-fit:cover;filter:grayscale(1) contrast(1.15);border:1px solid var(--rule);display:block}
figure::after{content:"";position:absolute;inset:0 0 auto 0;aspect-ratio:1;background:radial-gradient(rgba(0,0,0,.22) 30%,transparent 32%) 0 0/4px 4px;mix-blend-mode:multiply;pointer-events:none}
figcaption{font:.78rem/1.4 Inter,system-ui,sans-serif;color:var(--muted);padding-top:.4rem}
.body{display:grid;grid-template-columns:3fr 1fr;gap:2rem;padding:1.6rem 0}
.story{columns:2 18rem;column-gap:2rem;column-rule:1px solid var(--soft)}
.story p{orphans:3;widows:3;margin:0 0 .9rem;text-align:justify;hyphens:auto}
@media (max-width:40rem){.story p{text-align:left}}
.story>p:first-child::first-letter{float:left;font-size:4.2rem;line-height:.85;padding:.3rem .5rem 0 0;font-weight:700}
.story h2{break-inside:avoid;break-after:avoid;font-size:1.2rem;margin:1.1rem 0 .5rem;font-family:Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.06em}
.pull{column-span:all;margin:1rem 0 1.4rem;padding:1rem 0;border-top:3px solid var(--rule);border-bottom:1px solid var(--rule);font-size:clamp(1.4rem,3vw,2rem);line-height:1.25;text-align:center;font-style:italic}
.story .pull{text-align:center;hyphens:manual;text-wrap:balance}
.aside .box{border:1px solid var(--rule);padding:1rem;margin-bottom:1.2rem}
.aside h2{font:800 .8rem/1.2 Inter,system-ui,sans-serif;letter-spacing:.16em;text-transform:uppercase;margin:0 0 .7rem;padding-bottom:.4rem;border-bottom:3px solid var(--rule)}
.figs{list-style:none;margin:0;padding:0}
.figs li{padding:.5rem 0;border-bottom:1px solid var(--soft)}
.figs b{display:block;font-size:1.7rem;line-height:1.1}
.figs span{font:.82rem/1.35 Inter,system-ui,sans-serif;color:var(--muted)}
.brief{list-style:none;margin:0;padding:0;font:.88rem/1.4 Inter,system-ui,sans-serif}
.brief li{padding:.35rem 0;border-bottom:1px dotted var(--soft)}
.brief b{display:inline-block;min-width:3.4rem}
.classified{background:var(--fg);color:var(--bg)}
.classified h2{border-color:var(--bg)}
.classified p{margin:0 0 .6rem;font-size:.95rem}
.classified a{color:var(--bg);font-weight:700}
.mailbtn{display:inline-block;margin-top:.5rem;padding:.7rem 1.1rem;border-radius:8px;font-weight:700;text-decoration:none;min-height:44px}
.mailbtn.top{background:var(--fg);color:var(--bg);margin:0 0 .8rem;font:700 .85rem/1.3 Inter,system-ui,sans-serif;overflow-wrap:anywhere}
.classified .mailbtn{background:var(--bg);color:var(--fg);overflow-wrap:anywhere}
footer{max-width:70rem;margin:0 auto;padding:1rem 1.25rem;font:.88rem/1.5 Inter,system-ui,sans-serif;color:var(--muted)}
footer::before{content:"";display:block;border-top:4px double var(--rule);margin-bottom:1rem}
@media (max-width:50rem){.body{grid-template-columns:1fr}.front{grid-template-columns:1fr 8.5rem;gap:1rem}figure img{max-width:none}figcaption{font-size:.72rem}}
"""


def page():
    return head("Ben Fung: The Delivery Record", "/designs/broadsheet/", STYLE, "The Delivery Record: a newspaper profile of Ben Fung, the technology project and programme manager who recovers, separates and migrates.", card="card-broadsheet.jpg") + f"""{switcher("broadsheet")}
<main id="main">
<header class="mast">
  <p class="tag">Technology · Delivery · Change</p>
  <p class="title" aria-hidden="true">The Delivery Record</p>
  <div class="dateline"><span>London</span><span>Four roles since 2009</span><span>Special edition: Ben Fung</span></div>
</header>

<article>
<div class="front">
  <div>
    <p class="kicker">Profile</p>
    <h1>Ben Fung: the project manager who recovers, separates and migrates</h1>
    <p class="contact-top">{mail_button("mailbtn top")}</p>
    <p class="stand">More than 25 years in technology, about 20 in project management and delivery leadership, most recently at London Gatwick.</p>
    <p class="byline">The Delivery Record · Profile of a technology project and programme manager</p>
  </div>
  <figure>
    <img src="/assets/img/ben-fung-400.jpg" width="400" height="400" alt="Ben Fung">
    <figcaption>Ben Fung, technology project and programme manager, based in London.</figcaption>
  </figure>
</div>

<div class="body">
  <div class="story">
    <p>Ben Fung manages complex change across enterprise applications, infrastructure, cloud, cyber security and business separation. His work brings technical teams, business owners and suppliers together around delivery plans, clear responsibilities and practical decisions on risks, dependencies and costs.</p>
    <p>He brings an infrastructure engineering background to delivery leadership, which helps him work closely with technical specialists while keeping attention on business readiness, commercial control and operational handover.</p>
    <h2>Fourteen years with Finyx</h2>
    <p>From March 2009 to June 2023, Ben was an associate consultant with Finyx Consulting, a relationship spanning separately listed client assignments. Among them, and listed with his recent assignments, was cyber security project management at London Stock Exchange Group, delivering security orchestration and cyber forensic capabilities.</p>
    <p>His earlier work also includes Direct Line Group's separation from RBS, HMRC's Columbus programme and ServiceNow provisioning automation at Credit Suisse, where measured processing lead time fell from about 15 working days to one, excluding business-owner approval waiting time.</p>
    <p class="pull">Proceed, retender or cancel: he presented the options; the resulting cancellation avoided £1m of uncommitted forecast spend.</p>
    <h2>Migrations and separations</h2>
    <p>At easyJet, from September 2023 to December 2024, Ben was Programme Manager for enterprise application migrations and data-centre exit activity, including the Agresso/Unit4 SaaS ERP migration against a fixed data-centre exit deadline.</p>
    <p>In 2025, as a Separation Consultant for Tessiant, he worked on a client assignment for HX (Hurtigruten Expeditions), supporting business separation through Seaware ERP transition policies and master-data definition.</p>
    <h2>Recovery at Gatwick</h2>
    <p>From January to August 2026, as Senior Project Manager at London Gatwick, Ben recovered master data management delivery, with direct responsibility for an approximately £2m project budget. He rebased the delivery plan with stakeholders and the delivery team while keeping scheduled deployments, and aligned upstream processes with downstream information requirements.</p>
    <p>He managed monthly forecasts and supplier invoice approvals, completing remediation within budget and securing formal operational and service-management acceptance. He assessed a proposed monitoring consolidation investment and presented proceed, retender and cancel options. The resulting cancellation avoided £1m of uncommitted forecast implementation expenditure and £50k in additional annual licensing costs.</p>
  </div>
  <div class="aside">
    <section class="box" aria-labelledby="figures">
      <h2 id="figures">By the numbers</h2>
      <ul class="figs">
        <li><b>25+</b><span>years in technology</span></li>
        <li><b>~20</b><span>years in project management and delivery leadership</span></li>
        <li><b>~£2m</b><span>project budget, direct responsibility, London Gatwick</span></li>
        <li><b>£50k</b><span>additional annual licensing avoided</span></li>
      </ul>
    </section>
    <section class="box" aria-labelledby="brief">
      <h2 id="brief">Career in brief</h2>
      <ul class="brief">
        <li><b>2026</b> London Gatwick</li>
        <li><b>2025</b> Tessiant, for HX</li>
        <li><b>2023</b> easyJet</li>
        <li><b>2009</b> Finyx Consulting</li>
      </ul>
    </section>
    <section class="box classified" aria-labelledby="wanted">
      <h2 id="wanted">Classified: positions wanted</h2>
      <p>Senior Technology Project Manager, Programme Manager or Technology Delivery Lead. Permanent preferred; selective consulting. London and one other location, hybrid or remote. PRINCE2 Practitioner, ITIL v3.</p>
      <p>{mail_button()}</p>
    </section>
  </div>
</div>
</article>
</main>
<footer>
{site_links()}
{credit_line()}
</footer>
""" + END
