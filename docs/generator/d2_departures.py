from common import *

STYLE = r"""
:root{--page:#e9e6dd;--page-fg:#1d1d1b;--page-link:#7a4b00;--bg:#0b0c0e;--board:#15171b;--cell:#1f2228;--amber:#ffc23d;--white:#f3f1ea;--dim:#b9b4a6;--green:#5fe08f;--line:#2b2f36;
  --sw-fg:#e8e4d8;--sw-line:#3a3e46;--sw-on-bg:#ffc23d;--sw-on-fg:#111;--family-fg:#cfcabd;--family-fg-strong:#fff;--family-bg:#1c1c1c}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--white);font:16px/1.55 "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;min-height:100vh}
a{color:var(--amber)}
main{max-width:68rem;margin:0 auto;padding:1rem 1rem 2rem}
.board{background:var(--board);border:1px solid var(--line);border-radius:12px;box-shadow:0 30px 80px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.04);padding:1.5rem;margin-bottom:1.5rem}
.boardhead{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:1rem;border-bottom:2px solid var(--amber);padding-bottom:1rem;margin-bottom:1rem}
.kicker{color:var(--amber);letter-spacing:.3em;font-size:.8rem;margin:0 0 .6rem;text-transform:uppercase}
h1{margin:0;font-size:0;line-height:1}
.flap{display:inline-flex;flex-wrap:wrap;gap:4px}
.flap span{display:inline-grid;place-items:center;width:clamp(1.9rem,6vw,3.4rem);height:clamp(2.6rem,8vw,4.6rem);font-size:clamp(1.5rem,5vw,2.9rem);font-weight:700;color:var(--white);
  background:linear-gradient(#262a31 0 49%,#0b0c0e 49% 51%,#1d2026 51% 100%);border-radius:5px;box-shadow:inset 0 -2px 0 rgba(0,0,0,.4)}
@media (prefers-reduced-motion:no-preference){.flap span:not(.gap){animation:flip .5s cubic-bezier(.3,1.4,.5,1) both;transform-origin:50% 50%}
  @keyframes flip{0%{transform:rotateX(90deg)}60%{color:var(--amber)}100%{transform:rotateX(0)}}}
.flap span.gap{background:none;box-shadow:none;width:.8rem}
.clock{text-align:right;color:var(--dim);font-size:.85rem}
.clock b{display:block;color:var(--amber);font-size:1.6rem;letter-spacing:.05em}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.scroll{overflow-x:auto}
table{width:100%;border-collapse:separate;border-spacing:0 6px}
caption{text-align:left;color:var(--dim);font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;padding-bottom:.3rem}
th{color:var(--dim);font-weight:500;text-align:left;font-size:.75rem;letter-spacing:.18em;text-transform:uppercase;padding:.2rem .8rem}
td{background:var(--cell);padding:.8rem;vertical-align:top;text-transform:uppercase;letter-spacing:.04em}
td:first-child{border-radius:6px 0 0 6px;color:var(--amber);font-weight:700;font-size:1.15rem;white-space:nowrap}
td:last-child{border-radius:0 6px 6px 0}
td.dest{font-weight:700;font-size:1.05rem;color:var(--white)}
td .role{display:block;text-transform:none;letter-spacing:0;color:var(--dim);font-weight:400;font-size:.85rem;margin-top:.2rem}
.st{white-space:nowrap;display:inline-block;padding:.15rem .5rem;border-radius:3px;font-weight:700;font-size:.8rem}
.st.done{color:var(--dim);border:1px solid #4a4e57}
.st.board-now{background:var(--green);color:#06210f}
.gate{display:inline-block;margin-top:.4rem;color:var(--amber);font-weight:700;text-transform:none;letter-spacing:0;min-height:24px}
@media (prefers-reduced-motion:no-preference){.st.board-now{animation:pulse 2.4s ease-in-out infinite}@keyframes pulse{50%{box-shadow:0 0 0 6px rgba(95,224,143,.18)}}}
tr.next td{background:#22261c}
.panels{display:grid;grid-template-columns:repeat(auto-fit,minmax(18rem,1fr));gap:1.5rem}
.panel{background:var(--board);border:1px solid var(--line);border-radius:12px;padding:1.3rem 1.4rem}
h2{margin:0 0 .9rem;color:var(--amber);font-size:.95rem;letter-spacing:.2em;text-transform:uppercase}
.panel ul{list-style:none;margin:0;padding:0}
.panel li{padding:.55rem 0;border-top:1px dashed var(--line)}
.panel li:first-child{border-top:0}
.panel b{color:var(--white)}
.panel p,.panel li span{color:var(--dim)}
.panel ul,.panel p{font-family:Inter,system-ui,sans-serif;font-size:.98rem;letter-spacing:0}
.panel p{margin:0 0 .6rem}
@media (prefers-color-scheme:dark){.ticket{background:#d9d4c6}}
.ticket{display:grid;grid-template-columns:auto 1fr;gap:1.4rem;align-items:center;background:var(--white);color:#16181c;border-radius:14px;padding:1.4rem;position:relative;margin-top:1.5rem}
.ticket::before,.ticket::after{content:"";position:absolute;left:9.2rem;width:1.4rem;height:1.4rem;border-radius:50%;background:var(--page)}
@media (prefers-color-scheme:dark){.ticket::before,.ticket::after{background:var(--bg)}}
.ticket{box-shadow:0 0 0 1px rgba(0,0,0,.15)}
.ticket::before{top:-.7rem}.ticket::after{bottom:-.7rem}
.ticket img{width:7.5rem;height:7.5rem;border-radius:10px;object-fit:cover;filter:saturate(.9)}
.ticket h2{color:#7a4b00}
.ticket p{margin:.2rem 0;color:#2d3036}
.ticket a{color:#16181c;font-weight:700}
.mailbtn{display:inline-block;margin-top:.5rem;padding:.7rem 1.1rem;border-radius:8px;font-weight:700;text-decoration:none;min-height:44px}
.ticket .mailbtn{background:#16181c;color:#ffc23d}
footer{max-width:68rem;margin:0 auto;padding:1rem;color:var(--page-fg);font-size:.85rem}
footer a{color:var(--page-link)}
.designs{--sw-fg:#2d2b26;--sw-line:#b9b3a3;--sw-on-bg:#16181c;--sw-on-fg:#ffc23d}
.family-credit{--family-fg:#3f3d38;--family-fg-strong:#000;--family-bg:#fff}
@media (prefers-color-scheme:dark){body{background:radial-gradient(1200px 500px at 50% -10%,#232731 0,var(--bg) 60%)}footer{color:var(--dim)}footer a{color:var(--amber)}.designs{--sw-fg:#e8e4d8;--sw-line:#3a3e46;--sw-on-bg:#ffc23d;--sw-on-fg:#111}.family-credit{--family-fg:#cfcabd;--family-fg-strong:#fff;--family-bg:#1c1c1c}}
@media (max-width:40rem){.ticket{grid-template-columns:1fr}.ticket::before,.ticket::after{display:none}
  .flap span{width:2.3rem;height:3.1rem;font-size:1.75rem}.flap{gap:3px}.clock b{font-size:1.3rem}
  .board{padding:1rem .75rem}table,tbody,tr{display:block}thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}caption{display:block}tr{display:grid;grid-template-columns:3.6rem 1fr;margin-bottom:6px;background:var(--cell);border-radius:6px}tr.next{background:#22261c}td,tr.next td{background:none}td:last-child{grid-column:2;padding-top:0}td{padding:.6rem .5rem;font-size:.85rem}td:first-child{font-size:.95rem}td.dest{font-size:.92rem}th{padding:.2rem .5rem}.st{font-size:.7rem}.clock{text-align:left}}
"""

ROWS = [
    ("NEXT", "Your programme", "Senior Technology Project Manager · Programme Manager · Technology Delivery Lead", "London and one other location · hybrid or remote", f'<span class="st board-now">Next</span> <a class="gate" href="mailto:{EMAIL}">Gate: email Ben</a>', ' class="next"'),
    ("2026", "London Gatwick", "Senior Project Manager · contract", "8 mos", '<span class="st done">Within budget</span>', ""),
    ("2025", "Tessiant / HX", "Separation Consultant, Policy and Process · contract", "5 mos", '<span class="st done">Contract</span>', ""),
    ("2023", "easyJet", "Programme Manager · contract", "1 yr 4 mos", '<span class="st done">Contract</span>', ""),
    ("2009", "Finyx Consulting", "Associate Consultant · contract", "14 yrs 4 mos", '<span class="st done">Contract</span>', ""),
]


def flap(word):
    return "".join('<span class="gap"></span>' if ch == " " else f'<span style="animation-delay:{i*50}ms">{ch}</span>' for i, ch in enumerate(word))


def page():
    rows = "\n".join(
        f'<tr{cls}><td>{y}</td><td class="dest">{d}<span class="role">{r} · {dur}</span></td><td>{st}</td></tr>'
        for y, d, r, dur, st, cls in ROWS)
    return head("Ben Fung: departures board", "/designs/departures/", STYLE, "Ben Fung's career as a departures board: London Gatwick, Tessiant, easyJet and Finyx Consulting. Next: your programme.", card="card-departures.jpg") + f"""{switcher("departures")}
<main id="main">
<section class="board" aria-labelledby="name">
  <div class="boardhead">
    <div>
      <p class="kicker">Departures · technology delivery</p>
      <h1 id="name"><span class="sr">Ben Fung</span><span class="flap" aria-hidden="true">{flap("BEN FUNG")}</span></h1>
    </div>
    <p class="clock"><b>25+ yrs</b>in technology · ~20 in project management and delivery leadership</p>
  </div>
  <table>
    <caption>Roles since 2009, newest first</caption>
    <thead><tr><th scope="col">Year</th><th scope="col">Destination</th><th scope="col">Remarks</th></tr></thead>
    <tbody>
{rows}
    </tbody>
  </table>
</section>

<div class="panels">
  <section class="panel" aria-labelledby="flight-notes">
    <h2 id="flight-notes">Flight notes</h2>
    <ul>
      <li><b>London Gatwick.</b> <span>Recovered master data management delivery with direct responsibility for an approximately £2m budget. He presented proceed, retender and cancel options on a monitoring consolidation investment; the resulting cancellation avoided £1m of uncommitted forecast implementation spend and £50k in additional annual licensing.</span></li>
      <li><b>Tessiant / HX.</b> <span>Client assignment for HX (Hurtigruten Expeditions): supported business separation through Seaware ERP transition policies and master-data definition.</span></li>
      <li><b>easyJet.</b> <span>Managed the Agresso/Unit4 SaaS ERP migration against a fixed data-centre exit deadline.</span></li>
    </ul>
  </section>
  <section class="panel" aria-labelledby="connections">
    <h2 id="connections">Other connections</h2>
    <ul>
      <li><b>Direct Line Group.</b> <span>Separation from RBS.</span></li>
      <li><b>HMRC.</b> <span>The Columbus programme.</span></li>
      <li><b>Credit Suisse.</b> <span>ServiceNow provisioning automation: processing lead time from approximately 15 working days to one, excluding business-owner approval waiting time.</span></li>
      <li><b>LSEG, through Finyx.</b> <span>A recent assignment: security orchestration and cyber forensic capabilities.</span></li>
    </ul>
  </section>
  <section class="panel" aria-labelledby="baggage">
    <h2 id="baggage">Carry-on</h2>
    <p><b>PRINCE2 Practitioner</b> and <b>ITIL v3</b>, both PeopleCert.</p>
    <p>An infrastructure engineering background, which helps him work effectively with technical specialists.</p>
    <p>Enterprise applications · infrastructure · cloud · cyber security · business separation.</p>
  </section>
</div>

<section class="ticket" aria-labelledby="gate">
  <img src="/assets/img/ben-fung-400.jpg" width="400" height="400" alt="Ben Fung">
  <div>
    <h2 id="gate">Boarding pass · Gate: inbox</h2>
    <p>Passenger: Ben Fung, technology project and programme manager.</p>
    <p>Destination: your next programme. Permanent roles preferred; selective consulting assignments.</p>
    <p>{mail_button()}</p>
  </div>
</section>
</main>
<footer>
{site_links()}
{credit_line()}
</footer>
""" + END
