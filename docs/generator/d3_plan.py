from common import *

STYLE = r"""
:root{--bg:#eef1f5;--paper:#fff;--fg:#14213d;--muted:#475569;--line:#d5dbe4;--grid:#e6eaf0;--blue:#1d4ed8;--teal:#2f7f86;--violet:#334e7d;--orange:#4a6fa5;--now:#116331;
  --sw-fg:#334155;--sw-line:#c5cdd8;--sw-on-bg:#14213d;--sw-on-fg:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#0b1220;--paper:#111a2c;--fg:#e5ecf6;--muted:#a3b1c6;--line:#24324a;--grid:#1a2540;--blue:#7aa2ff;--teal:#4fd1c5;--violet:#9fb4d9;--orange:#b7c8e6;--now:#5be38c;
  --sw-fg:#cbd5e1;--sw-line:#2c3b55;--sw-on-bg:#e5ecf6;--sw-on-fg:#0b1220;--family-fg:#c3ccd8;--family-fg-strong:#fff;--family-bg:#1c1c1c}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 Inter,system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:var(--blue)}
main{max-width:72rem;margin:0 auto;padding:.5rem 1rem 2rem}
.sheet{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:1.5rem;margin-bottom:1.25rem;box-shadow:0 1px 2px rgba(15,23,42,.06)}
.titlebar{display:grid;grid-template-columns:auto 1fr auto;gap:1.25rem;align-items:center}
.titlebar img{width:5.5rem;height:5.5rem;border-radius:8px;object-fit:cover}
.doc{font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 .2rem;font-weight:600}
h1{margin:0;font-size:clamp(1.7rem,4vw,2.5rem);letter-spacing:-.02em;line-height:1.1}
.titlebar p{margin:.3rem 0 0;color:var(--muted)}
.status{display:grid;gap:.3rem;font-size:.85rem;text-align:right}
.pill{display:inline-block;padding:.2rem .6rem;border-radius:999px;font-weight:700;font-size:.75rem;letter-spacing:.06em;text-transform:uppercase;background:color-mix(in srgb,var(--now) 16%,transparent);color:var(--now)}
.kv{display:grid;grid-template-columns:repeat(auto-fit,minmax(10rem,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:8px;margin-top:1.25rem;overflow:hidden}
.kv div{padding:.8rem 1rem;background:var(--paper)}
@media (max-width:40rem){.kv{grid-template-columns:1fr 1fr}.kv div:last-child:nth-child(odd){grid-column:1/-1}}
.kv dt{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600}
.kv dd{margin:.15rem 0 0;font-size:1.35rem;font-weight:700;font-variant-numeric:tabular-nums;letter-spacing:-.01em}
h2{font-size:1.05rem;margin:0 0 1rem;display:flex;align-items:center;gap:.6rem}
h2::before{content:"";width:.6rem;height:.6rem;border-radius:2px;background:var(--blue)}
.gantt{display:grid;gap:.5rem;font-size:.82rem}
.grow{display:grid;grid-template-columns:17.5rem 1fr;align-items:center;gap:.8rem}
.track{display:grid;grid-template-columns:repeat(216,minmax(0,1fr));position:relative;min-height:1.9rem;
  background:repeating-linear-gradient(90deg,var(--grid) 0 1px,transparent 1px calc(100%/18));border-radius:4px}
.yrs{min-height:0;background:none}
.yr{font-size:.8rem;color:var(--muted);border-left:1px solid var(--line);padding:0 0 .2rem .2rem;font-variant-numeric:tabular-nums;grid-row:1}
.lbl{font-weight:600;line-height:1.25}
.lbl small{display:block;font-weight:400;color:var(--muted);font-size:.8rem}
.bar{grid-row:1;grid-column:var(--s)/var(--e);align-self:center;height:1.7rem;border-radius:5px;min-width:14px;color:#fff;font-weight:600;font-size:.75rem;display:flex;align-items:center;padding:0 .5rem;white-space:nowrap;overflow:hidden;min-width:6px}
@media (prefers-color-scheme:dark){.bar{color:#0b1220}}
@media (max-width:40rem){.grow{grid-template-columns:1fr;gap:.25rem}.grow.head .lbl{display:none}.yr.odd{visibility:hidden}.yr{font-size:.65rem;padding-left:.1rem}.bar span{display:none}}
.bnext{background:repeating-linear-gradient(45deg,var(--now) 0 6px,transparent 6px 10px);border:2px solid var(--now)}
.b1{background:var(--violet)}.b2{background:var(--orange)}.b3{background:var(--teal)}.b4{background:var(--blue)}
@media (prefers-color-scheme:dark){}
.note{color:var(--muted);font-size:.85rem;margin:.9rem 0 0}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(20rem,1fr));gap:1.25rem}
table{width:100%;border-collapse:collapse;font-size:.92rem}
th,td{text-align:left;padding:.6rem .6rem;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
td.num{font-variant-numeric:tabular-nums;font-weight:700;white-space:nowrap}
.ws{list-style:none;margin:0;padding:0;display:grid;gap:.6rem}
.ws li{display:grid;grid-template-columns:2.2rem 1fr;gap:.7rem;align-items:start}
.ws b{display:grid;place-items:center;width:2.2rem;height:2.2rem;border-radius:6px;background:var(--grid);font-size:.8rem}
.ws span{color:var(--muted)}
.ws strong{display:block;color:var(--fg)}
.decision{border-left:4px solid var(--blue);padding:.2rem 0 .2rem 1rem}
.opts{display:flex;flex-wrap:wrap;gap:.5rem;margin:.6rem 0}
.opts span{padding:.3rem .7rem;border-radius:6px;border:1px solid var(--line);font-weight:600;font-size:.85rem}
.opts span.chosen{background:var(--fg);color:var(--paper);border-color:var(--fg)}
.mailbtn{display:inline-block;margin-top:.5rem;padding:.7rem 1.1rem;border-radius:8px;font-weight:700;text-decoration:none;min-height:44px}
.mailbtn{background:var(--fg);color:var(--paper)}
footer{max-width:72rem;margin:0 auto;padding:1rem;color:var(--muted);font-size:.88rem}
@media (max-width:40rem){td.num{white-space:normal}th,td{padding:.5rem .35rem}.sheet{padding:1rem}.titlebar{grid-template-columns:auto 1fr}.status{grid-column:1/-1;text-align:left}}
"""

BARS = [  # label, sub, start (year, month), end (year, month inclusive), cls, text
    ("Associate Consultant", "Finyx Consulting", (2009, 3), (2023, 6), "b1", "14 yrs 4 mos"),
    ("Programme Manager", "easyJet", (2023, 9), (2024, 12), "b2", ""),
    ("Separation Consultant", "Tessiant, client HX", (2025, 2), (2025, 6), "b3", ""),
    ("Senior Project Manager", "London Gatwick", (2026, 1), (2026, 8), "b4", ""),
]


def col(y, m):
    return 2 + (y - 2009) * 12 + (m - 1)


MON = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]


def page():
    years = "".join(f'<div class="yr{' odd' if y % 2 == 0 else ''}" style="grid-column:{col(y,1)-1}/span 12">{y}</div>' for y in range(2009, 2027))
    rows = [f'<div class="grow head" aria-hidden="true"><div class="lbl"></div><div class="track yrs">{years}</div></div>']
    for l, s_, a, b, c, t in BARS:
        when = f"{MON[a[1]-1]} {a[0]} to {MON[b[1]-1]} {b[0]}" if c != "bnext" else "as his profile says"
        rows.append(f'<div class="grow"><div class="lbl">{l}<small>{s_} · {when}</small></div><div class="track" aria-hidden="true"><div class="bar {c}" style="--s:{col(*a)-1};--e:{col(*b)}"><span>{t}</span></div></div></div>')
    gantt = "\n".join(rows)
    return head("Ben Fung: programme plan", "/designs/programme-plan/", STYLE, "Ben Fung's career as a programme highlight report: a plan on a page from 2009 to 2026, the figures from his profile and what he wants next.", card="card-programme-plan.jpg") + f"""{switcher("plan")}
<main id="main">
<header class="sheet titlebar">
  <img src="/assets/img/ben-fung-400.jpg" width="400" height="400" alt="Ben Fung">
  <div>
    <p class="doc">Career programme · highlight report</p>
    <h1>Ben Fung</h1>
    <p>Technology project and programme manager. Enterprise applications, cloud and cyber security; business separation and project recovery.</p>
  </div>
  <div class="status"><span class="pill">Next role</span><span>London and one other location · hybrid or remote</span>{mail_button()}</div>
</header>

<section class="sheet" aria-labelledby="summary">
  <h2 id="summary">Programme summary</h2>
  <dl class="kv">
    <div><dt>In technology</dt><dd>25+ yrs</dd></div>
    <div><dt>Delivery leadership</dt><dd>~20 yrs</dd></div>
    <div><dt>Project budget, Gatwick</dt><dd>~£2m</dd></div>
    <div><dt>Forecast spend avoided</dt><dd>£1m</dd></div>
    <div><dt>Extra licensing avoided</dt><dd>£50k/yr</dd></div>
  </dl>
</section>

<section class="sheet" aria-labelledby="plan">
  <h2 id="plan">Plan on a page, 2009 to 2026</h2>
  <div class="gantt">
{gantt}
  </div>
  <p class="note">Bars run from the first to the last month of each role as listed on his profile. Other client assignments (Direct Line Group, HMRC, Credit Suisse, LSEG) are listed below without dates.</p>
</section>

<div class="cols">
<section class="sheet" aria-labelledby="benefits">
  <h2 id="benefits">Figures from his profile</h2>
  <table>
    <thead><tr><th scope="col">Engagement</th><th scope="col">Result</th><th scope="col">Measure</th></tr></thead>
    <tbody>
      <tr><td>London Gatwick</td><td>Uncommitted forecast implementation spend avoided</td><td class="num">£1m</td></tr>
      <tr><td>London Gatwick</td><td>Additional annual licensing avoided</td><td class="num">£50k a year</td></tr>
      <tr><td>London Gatwick</td><td>Remediation completed within budget, with formal operational and service-management acceptance</td><td class="num">Within budget</td></tr>
      <tr><td>Credit Suisse</td><td>ServiceNow provisioning automation: measured processing lead time, excluding business-owner approval waiting time</td><td class="num">~15 → 1 working days</td></tr>
    </tbody>
  </table>
</section>

<section class="sheet" aria-labelledby="workstreams">
  <h2 id="workstreams">Workstreams</h2>
  <ul class="ws">
    <li><b>01</b><div><strong>Project recovery</strong><span>Rebasing the plan with stakeholders while keeping scheduled deployments (London Gatwick).</span></div></li>
    <li><b>02</b><div><strong>Business separation</strong><span>Direct Line Group's separation from RBS; for client HX, Seaware ERP transition policies and master-data definition (Tessiant).</span></div></li>
    <li><b>03</b><div><strong>Enterprise applications and data-centre exit</strong><span>easyJet's Agresso/Unit4 SaaS ERP migration against a fixed exit deadline.</span></div></li>
    <li><b>04</b><div><strong>Cyber security</strong><span>Security orchestration and cyber forensic capabilities at London Stock Exchange Group.</span></div></li>
    <li><b>05</b><div><strong>Programmes and automation</strong><span>HMRC's Columbus programme; ServiceNow provisioning automation at Credit Suisse.</span></div></li>
  </ul>
</section>
</div>

<div class="cols">
<section class="sheet" aria-labelledby="decision">
  <h2 id="decision">Options presented: one example</h2>
  <div class="decision">
    <p>At London Gatwick, Ben assessed a proposed monitoring consolidation investment and presented three options.</p>
    <div class="opts" role="list"><span role="listitem">Proceed</span><span role="listitem">Retender</span><span role="listitem" class="chosen">Cancel (the outcome)</span></div>
    <p>The resulting cancellation avoided £1m of uncommitted forecast implementation expenditure and £50k in additional annual licensing costs.</p>
  </div>
</section>

<section class="sheet" aria-labelledby="resourcing">
  <h2 id="resourcing">Resourcing request</h2>
  <table>
    <tbody>
      <tr><th scope="row">Roles</th><td>Senior Technology Project Manager · Programme Manager · Technology Delivery Lead</td></tr>
      <tr><th scope="row">Basis</th><td>Permanent preferred; selective consulting assignments</td></tr>
      <tr><th scope="row">Certified</th><td>PRINCE2 Practitioner · ITIL v3 (PeopleCert)</td></tr>
      <tr><th scope="row">Contact</th><td>{mail_button()}</td></tr>
    </tbody>
  </table>
</section>
</div>
</main>
<footer>
{site_links()}
{credit_line()}
</footer>
""" + END
