from common import *
from facts import RECENT, PHASES, when
import re

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
.track{display:grid;grid-template-columns:repeat(360,minmax(0,1fr));position:relative;min-height:1.9rem;
  background:repeating-linear-gradient(90deg,var(--grid) 0 1px,transparent 1px calc(100%/30));border-radius:4px}
.yrs{min-height:0;background:none}
.yr{font-size:.8rem;color:var(--muted);border-left:1px solid var(--line);padding:0 0 .2rem .2rem;font-variant-numeric:tabular-nums;grid-row:1}
.lbl{font-weight:600;line-height:1.25}
.lbl small{display:block;font-weight:400;color:var(--muted);font-size:.8rem}
.bar{grid-row:1;grid-column:var(--s)/var(--e);align-self:center;height:1.7rem;border-radius:5px;min-width:14px;color:#fff;font-weight:600;font-size:.75rem;display:flex;align-items:center;padding:0 .5rem;white-space:nowrap;overflow:hidden;min-width:6px}
@media (prefers-color-scheme:dark){.bar{color:#0b1220}}
.yr.odd{visibility:hidden}.grow.phase-h{margin-top:.6rem}.grow.phase-h .lbl{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
@media (max-width:40rem){.grow{grid-template-columns:1fr;gap:.25rem}.grow.head .lbl{display:none}.yr.m5{visibility:hidden}.yr{font-size:.65rem;padding-left:.1rem}.bar span{display:none}}
.bnext{background:repeating-linear-gradient(45deg,var(--now) 0 6px,transparent 6px 10px);border:2px solid var(--now)}
.bfin{background:repeating-linear-gradient(45deg,var(--grid) 0 6px,transparent 6px 10px);border:2px solid var(--violet);color:var(--fg)}.b1{background:var(--violet)}.b2{background:var(--orange)}.b3{background:var(--teal)}.b4{background:var(--blue)}
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

START = 1997


def col(ym):
    y, m = map(int, ym.split("-"))
    return 2 + (y - START) * 12 + (m - 1)


def end_col(ym):
    return col(ym) + 1


def plain(s):
    return re.sub(r"<small>.*?</small>", "", s)


# Oldest first, as a plan reads; each phase gets its own colour. Facts from facts.py only.
GROUPS = [
    ("1997 to 2009: infrastructure engineering to project leadership", "b1", list(reversed(PHASES[2][3]))),
    ("2009 to 2016: programme and project management", "b2", list(reversed(PHASES[1][3]))),
    ("2018 to 2022: security, procurement and resilience consulting", "b3", list(reversed(PHASES[0][3]))),
    ("2022 to 2026: recent roles", "b4", [(o, r, s, e, a, sc) for o, r, s, e, a, sc, _ in reversed(RECENT)]),
]
ARRW = {"consultancy": "consultancy", "contract": "contract", "unknown": "arrangement not stated"}


def page():
    years = "".join(f'<div class="yr{" odd" if y % 2 else ""}{"" if y % 5 == 0 else " m5"}" style="grid-column:{col(f"{y}-01")-1}/span 12">{y}</div>' for y in range(START, 2027))
    rows = [f'<div class="grow head" aria-hidden="true"><div class="lbl"></div><div class="track yrs">{years}</div></div>']
    for title, c, roles in GROUPS:
        rows.append(f'<div class="grow phase-h"><div class="lbl">{title}</div><div></div></div>')
        if c == "b2":
            rows.append(f'<div class="grow"><div class="lbl">Associate Consultant<small>Finyx Consulting · Mar 2009 to Jun 2023 · an associate relationship spanning overlapping client assignments</small></div><div class="track" aria-hidden="true"><div class="bar bfin" style="--s:{col("2009-03")-1};--e:{end_col("2023-06")-1}"><span>Finyx Consulting, associate</span></div></div></div>')
        for o, r, s, e, a, _ in roles:
            rows.append(f'<div class="grow"><div class="lbl">{plain(r)}<small>{o} · {when(s, e)} · {ARRW[a]}</small></div><div class="track" aria-hidden="true"><div class="bar {c}" style="--s:{col(s)-1};--e:{end_col(e)-1}"></div></div></div>')
    gantt = "\n".join(rows)
    return head("Ben Fung: programme plan", "/designs/programme-plan/", STYLE, "Ben Fung's career as a programme highlight report: every role on a plan from 1997 to 2026, the measured results and the recommendation he made at Gatwick.", card="card-programme-plan.jpg") + f"""{switcher("plan")}
<main id="main">
<header class="sheet titlebar">
  <img src="/assets/img/ben-fung-400.jpg" width="400" height="400" alt="Ben Fung, smiling, in a dark jacket and striped shirt">
  <div>
    <p class="doc">Career programme · highlight report</p>
    <h1>Ben Fung</h1>
    <p>Technology programme and project delivery across aviation, financial services and government: enterprise migrations, business separation, cybersecurity delivery and operational resilience.</p>
  </div>
  <div class="status"><span class="pill">Contact</span>{mail_button()}</div>
</header>

<section class="sheet" aria-labelledby="summary">
  <h2 id="summary">Programme summary</h2>
  <dl class="kv">
    <div><dt>In technology</dt><dd>Since 1997</dd></div>
    <div><dt>Gatwick MDM budget</dt><dd>&#163;2m</dd></div>
    <div><dt>Spend avoided, Gatwick</dt><dd>&#163;1m</dd></div>
    <div><dt>Licensing increase avoided</dt><dd>&#163;50k a year</dd></div>
    <div><dt>P1 defects at go-live, HMRC</dt><dd>0</dd></div>
  </dl>
</section>

<section class="sheet" aria-labelledby="plan">
  <h2 id="plan">Plan on a page, 1997 to 2026</h2>
  <div class="gantt">
{gantt}
  </div>
  <p class="note">Each bar runs from the first to the last month of a role, as given. Bars that overlap are engagements that ran at the same time. The striped bar is his associate relationship with Finyx Consulting.</p>
</section>

<div class="cols">
<section class="sheet" aria-labelledby="benefits">
  <h2 id="benefits">Measured results</h2>
  <table>
    <thead><tr><th scope="col">Engagement</th><th scope="col">Result</th><th scope="col">Measure</th></tr></thead>
    <tbody>
      <tr><td>Gatwick Airport</td><td>Implementation spend avoided through his recommendation to cancel the infrastructure monitoring project</td><td class="num">&#163;1m</td></tr>
      <tr><td>Gatwick Airport</td><td>Increase in licensing costs avoided through the same recommendation</td><td class="num">&#163;50k a year</td></tr>
      <tr><td>Gatwick Airport</td><td>Mobile Device Management project budget he was responsible for; remediation completed within budget and formally accepted</td><td class="num">&#163;2m</td></tr>
      <tr><td>easyJet</td><td>Unit4 ERP migration and required integrations by the fixed data-centre exit deadline, no components deferred</td><td class="num">On deadline</td></tr>
      <tr><td>easyJet</td><td>Servers decommissioned by the wider data-centre exit programme</td><td class="num">~150</td></tr>
      <tr><td>HMRC</td><td>Priority-one defects at go-live and through stabilisation, on his assigned migration delivery</td><td class="num">0</td></tr>
      <tr><td>Credit Suisse</td><td>Measured virtual-server provisioning processing time, excluding time waiting for business-owner approval</td><td class="num">~15 &#8594; 1 working days</td></tr>
      <tr><td>MF Global</td><td>Servers decommissioned by the VMware virtualisation project he led</td><td class="num">200+</td></tr>
    </tbody>
  </table>
</section>

<section class="sheet" aria-labelledby="workstreams">
  <h2 id="workstreams">Workstreams</h2>
  <ul class="ws">
    <li><b>01</b><div><strong>Enterprise migration</strong><span>easyJet's Unit4 ERP move to SaaS for the data-centre exit; HMRC's Columbus programme.</span></div></li>
    <li><b>02</b><div><strong>Business separation</strong><span>HX's Seaware ERP transition; Direct Line Group's separation from RBS; resilience for M&amp;G's separation from Prudential.</span></div></li>
    <li><b>03</b><div><strong>Cyber security and operating models</strong><span>Security orchestration and forensics at London Stock Exchange Group; the security target operating model for HMRC / Home Office.</span></div></li>
    <li><b>04</b><div><strong>Procurement and evaluation</strong><span>Scoring and evaluation for the Metropolitan Police Service and the National Crime Agency.</span></div></li>
    <li><b>05</b><div><strong>Commercial control and automation</strong><span>A &#163;2m budget at Gatwick; ServiceNow automation and portfolio scoring at Credit Suisse.</span></div></li>
    <li><b>06</b><div><strong>Infrastructure</strong><span>From server support at Westpac to leading VMware virtualisation at MF Global.</span></div></li>
  </ul>
</section>
</div>

<div class="cols">
<section class="sheet" aria-labelledby="decision">
  <h2 id="decision">Recommendation made: one example</h2>
  <div class="decision">
    <p>At Gatwick Airport, Ben assessed a proposed project to consolidate infrastructure monitoring tools and presented the options.</p>
    <div class="opts" role="list"><span role="listitem">Proceed</span><span role="listitem" class="chosen">Cancel (his recommendation)</span></div>
    <p>Through his recommendation, Gatwick avoided &#163;1m of implementation spend and an increase of &#163;50k a year in licensing costs.</p>
  </div>
</section>

<section class="sheet" aria-labelledby="resourcing">
  <h2 id="resourcing">Certifications and development</h2>
  <table>
    <tbody>
      <tr><th scope="row">PRINCE2 Practitioner</th><td>Achieved</td></tr>
      <tr><th scope="row">ITIL v3</th><td>Achieved</td></tr>
      <tr><th scope="row">Microsoft Certified: AI Transformation Leader (AB-731)</th><td>In progress</td></tr>
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
