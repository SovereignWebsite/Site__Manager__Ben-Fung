from common import *
STYLE = r"""
:root{--bg:#f6f6f4;--fg:#18181b;--muted:#52525b;--line:#dedcd6;--sw-fg:#3f3f46;--sw-line:#d4d4d8;--sw-on-bg:#18181b;--sw-on-fg:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#121214;--fg:#f4f4f5;--muted:#b4b4bb;--line:#2a2a2e;--sw-fg:#d4d4d8;--sw-line:#3f3f46;--sw-on-bg:#f4f4f5;--sw-on-fg:#121214;--family-fg:#c8c8cc;--family-fg-strong:#fff;--family-bg:#1c1c1c}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.55 Inter,system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:70rem;margin:0 auto;padding:1rem 1.25rem 2rem}
h1{font-size:clamp(2rem,5vw,3rem);letter-spacing:-.02em;line-height:1.1;margin:1rem 0 .5rem}
.sub{color:var(--muted);max-width:44rem;margin:0 0 2rem}
.cards{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(19rem,1fr));gap:1.25rem}
.cards a{display:block;text-decoration:none;color:inherit;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--bg);height:100%}
.cards a:hover,.cards a:focus-visible{outline:3px solid var(--fg);outline-offset:2px}
.sw{height:9rem;display:grid;place-items:center;font-weight:800;font-size:1.6rem;letter-spacing:-.01em}
.s1{background:#f7f5f0;color:#0f6b58;border-bottom:3px solid #0f6b58}
.s2{background:#0b0c0e;color:#ffc23d;font-family:"JetBrains Mono",ui-monospace,monospace;letter-spacing:.2em}
.s3{background:#eef1f5;color:#14213d;background-image:linear-gradient(90deg,#6d28d9 0 55%,transparent 55%),linear-gradient(90deg,transparent 60%,#c2410c 60% 80%,transparent 80%),linear-gradient(90deg,transparent 84%,#0f766e 84% 89%,transparent 89%),linear-gradient(90deg,transparent 92%,#1d4ed8 92%);background-size:100% 10px;background-repeat:no-repeat;background-position:0 20%,0 40%,0 60%,0 80%}
.s3 span{background:#eef1f5;padding:.1rem .5rem}
.s4{background:#f4f1ea;color:#1b1b1f;background-image:linear-gradient(#00796b,#00796b);background-size:100% 12px;background-repeat:no-repeat;background-position:0 50%}
.s4 span{background:#f4f1ea;border:6px solid #00796b;border-radius:999px;padding:.2rem 1rem}
.s5{background:#f3efe6;color:#141414;font-family:"Bitstream Charter",Charter,Georgia,serif;border-bottom:4px double #141414}
.shot{display:block;width:100%;height:auto;border-bottom:1px solid var(--line)}
.txt{padding:1rem 1.2rem}
.txt h2{margin:0 0 .3rem;font-size:1.2rem}.txt p{margin:0;color:var(--muted);font-size:.95rem}
footer{max-width:70rem;margin:0 auto;padding:1rem 1.25rem;color:var(--muted);font-size:.88rem}
footer a{color:var(--fg)}
"""
CARDS = [
 ("/", "s1", "Ben Fung", "1. Career path", "An editorial timeline of his roles from Finyx Consulting to London Gatwick, with the numbers that matter."),
 ("/designs/departures/", "s2", "DEPARTURES", "2. Departures board", "Each role is a departure on a split-flap board. The top row is the role he wants next."),
 ("/designs/programme-plan/", "s3", "<span>Plan on a page</span>", "3. Programme plan", "A highlight report: a Gantt chart of 2009 to 2026, the figures from his profile and the options he presented at Gatwick."),
 ("/designs/line-map/", "s4", "<span>The Ben Fung Line</span>", "4. Line map", "His career as a transit line, with an interchange for the client assignments loop."),
 ("/designs/broadsheet/", "s5", "The Delivery Record", "5. Broadsheet", "A newspaper front page: the profile, the numbers and a classified for the next role."),
]
def page():
    TH = {"s1":"career-path","s2":"departures","s3":"programme-plan","s4":"line-map","s5":"broadsheet"}
    cards = "\n".join(f'<li><a href="{h}"><img class="shot" src="/assets/designs/{TH[c]}.jpg" width="640" height="400" alt="" loading="lazy"><div class="txt"><h2>{t}</h2><p>{d}</p></div></a></li>' for h,c,art,t,d in CARDS)
    return head("Ben Fung: five designs", "/designs/", STYLE, "One career, five designs: the same facts about Ben Fung, technology project and programme manager, told five ways.") + f"""{switcher("")}
<main id="main">
<h1>One career, five designs</h1>
<p class="sub">The same facts about Ben Fung, told five very different ways. Each one is a full page; pick the one that fits the reader.</p>
<ul class="cards">
{cards}
</ul>
</main>
<footer>
{site_links()}
{credit_line()}
</footer>
""" + END
