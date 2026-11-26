from common import *
from facts import RECENT, PHASES, when

STYLE = r"""
:root{--bg:#fbfbfd;--paper:#fff;--fg:#16141f;--muted:#4e4a5c;--main:#5b2d8e;--branch:#b34700;--line:#dcd8e6;
  --sw-fg:#3b3747;--sw-line:#d3cfe0;--sw-on-bg:#5b2d8e;--sw-on-fg:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#100e18;--paper:#1a1724;--fg:#f1eef8;--muted:#b7b1c8;--main:#b48cff;--branch:#ffa057;--line:#2f2a3d;
  --sw-fg:#d9d4e6;--sw-line:#3a3449;--sw-on-bg:#b48cff;--sw-on-fg:#100e18;--family-fg:#cbc6d6;--family-fg-strong:#fff;--family-bg:#1c1c1c}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg) radial-gradient(var(--line) 1px,transparent 1.5px) 0 0/22px 22px;color:var(--fg);font:17px/1.55 "Inter",system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:var(--main)}
main{max-width:66rem;margin:0 auto;padding:.5rem 1.25rem 2rem}
.mast{display:flex;flex-wrap:wrap;align-items:center;gap:1.2rem;padding:1.5rem 0 1rem;border-bottom:6px solid var(--main);margin-bottom:2rem}
.badge{display:grid;place-items:center;width:4.4rem;height:4.4rem;border-radius:50%;border:9px solid var(--main);background:var(--paper);font-weight:800;font-size:1.05rem;color:var(--fg)}
.mast h1{margin:0;font-size:clamp(2rem,6vw,3.2rem);letter-spacing:-.02em;line-height:1.05}
.mast p{margin:.2rem 0 0;color:var(--muted)}
.key{display:flex;flex-wrap:wrap;gap:1rem 2rem;font-size:.85rem;color:var(--muted);margin:0 0 2rem;padding:.8rem 1rem;background:var(--paper);border:1px solid var(--line);border-radius:8px}
.key span{display:inline-flex;align-items:center;gap:.5rem}
.key i{display:inline-block;width:2rem;height:6px;border-radius:3px}
.key i.m{background:var(--main)}.key i.b{background:var(--branch)}
.key i.x{width:14px;height:14px;border-radius:50%;border:4px solid var(--fg);background:var(--paper)}
.line{list-style:none;margin:0;padding:0;position:relative}
.stop{position:relative;padding:0 0 2.2rem 4.2rem;min-height:3rem}
.stop::before{content:"";position:absolute;left:1.35rem;top:0;bottom:0;width:12px;background:var(--main)}
.stop:first-child::before{top:.9rem}
.stop.end::before{bottom:auto;height:1rem}
.stop::after{content:"";position:absolute;left:.85rem;top:.2rem;width:1.6rem;height:1.6rem;border-radius:50%;background:var(--paper);border:5px solid var(--fg)}
.stop.term::after{border-radius:4px;width:1.9rem;left:.7rem;background:var(--main);border-color:var(--main)}
.zone{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);font-weight:700}
.stop h3{margin:.1rem 0 .1rem;font:800 1.35rem/1.2 "Inter Display",Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.02em}
.stop .role{margin:0 0 .5rem;font-weight:600;color:var(--main)}
.stop p{margin:0 0 .5rem;color:var(--muted);max-width:40rem}
.zonehead{font-size:1.3rem;margin:2rem 0 .3rem}.zonenote{color:var(--muted);margin:0 0 1rem}
.loophead{font-size:1.45rem;margin:0 0 .3rem}.loopnote{color:var(--muted);margin:0 0 .5rem}
.branch{list-style:none;margin:.9rem 0 .4rem;padding:.9rem 1rem .4rem;border:1px solid var(--line);border-left:8px solid var(--branch);border-radius:8px;background:var(--paper)}
.branch li{position:relative;padding:0 0 .7rem 1.6rem}
.branch li::before{content:"";position:absolute;left:0;top:.35rem;width:.85rem;height:.85rem;border-radius:50%;border:3px solid var(--branch);background:var(--paper)}
.branch b{display:block}.branch span{color:var(--muted)}
.branch .title{padding-left:0;font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--branch)}
.branch .title::before{display:none}
.facts{display:flex;flex-wrap:wrap;gap:.4rem;margin:.4rem 0 0;padding:0;list-style:none}
.facts li{font-size:.8rem;padding:.15rem .55rem;border:1px solid var(--line);border-radius:4px;background:var(--paper)}
.map{display:block;width:100%;height:auto;margin:0 0 2rem;background:var(--paper);border:1px solid var(--line);border-radius:12px}
.map .m{stroke:var(--main)}.map .b{stroke:var(--branch)}.map .st{fill:var(--paper);stroke:var(--fg)}.map .bst{fill:var(--paper);stroke:var(--branch)}
.map .nm{fill:var(--fg);font:800 15px "Inter Display",Inter,sans-serif;text-transform:uppercase;letter-spacing:.04em}
.map .zn{fill:var(--muted);font:600 13px Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase}
.map .bn{fill:var(--fg);font:700 14px Inter,sans-serif}
.map .lab{font:800 13px Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase}
@media (max-width:48rem){.map{display:none}.key{display:none}}
@media (min-width:48.01rem){
  .key{display:none}
  .line{align-items:start}
  .stop::after{display:none}
  .stop .zone::before{content:"";display:inline-block;width:.7rem;height:.7rem;border-radius:50%;border:3px solid var(--fg);margin-right:.45rem;vertical-align:-1px}
  .stop.term .zone::before{border-color:var(--paper);border-radius:2px}
  .line{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-bottom:2rem}
  .stop{padding:1.1rem 1.2rem 1rem;background:var(--paper);border:1px solid var(--line);border-top:10px solid var(--main);border-radius:10px;min-height:0}
  .stop::before{display:none}
  .stop::after{left:auto;right:1rem;top:-1.05rem;width:1.5rem;height:1.5rem;border-width:5px}
  .stop.term{background:var(--main);color:var(--paper);border-color:var(--main)}
  .stop.term .facts li{color:var(--main)}.stop.term h3,.stop.term .role,.stop.term p,.stop.term .zone{color:var(--paper)}
  .stop.term::after{display:none}
}
.ticket{display:flex;flex-wrap:wrap;gap:1.2rem;align-items:center;margin:1rem 0 2rem;padding:1.3rem;border-radius:12px;background:var(--main);color:var(--paper)}
.ticket img{width:6rem;height:6rem;border-radius:50%;object-fit:cover;border:4px solid var(--paper)}
.mailbtn{display:inline-block;margin-top:.5rem;padding:.7rem 1.1rem;border-radius:8px;font-weight:700;text-decoration:none;min-height:44px}
.ticket .mailbtn{background:var(--paper);color:var(--main)}
.mast .mailbtn{background:var(--main);color:var(--paper);padding:.45rem .9rem;margin:.3rem 0 0}
.next-top{font-weight:600;color:var(--fg)!important}
.ticket h2{margin:0 0 .3rem}.ticket p{margin:0 0 .3rem}
.ticket a{color:var(--paper);font-weight:700}
@media (prefers-color-scheme:dark){.ticket{color:#0d0e10}.ticket a{color:#0d0e10}.ticket img{border-color:#0d0e10}}
footer{max-width:66rem;margin:0 auto;padding:1rem 1.25rem;color:var(--muted);font-size:.88rem}
"""


# Stations on the drawn map: (x, label, year, above?) per zone. Every stop below comes from facts.py.
MAP = [
    (60, "Westpac", "1997", True), (200, "MF Global", "2007", False),
    (300, "Direct Line", "2011", True), (390, "Credit Suisse", "2014", False), (470, "HMRC", "2015", True),
    (550, "Home Office", "2018", False), (630, "Met Police", "2019", True), (710, "Defra", "2022", False),
    (775, "LSEG", "2022", True), (835, "easyJet", "2023", False), (895, "HX", "2025", True),
]
ZONES = [(40, 250, "Zone 1 · 1997 to 2009"), (250, 510, "Zone 2 · 2009 to 2016"), (510, 745, "Zone 3 · 2018 to 2022"), (745, 975, "Zone 4 · 2022 to 2026")]
ARRW = {"consultancy": "consultancy", "contract": "contract", "unknown": "arrangement not stated"}


def svg():
    z = "".join(f'<text class="zn" x="{a + 6}" y="40">{lab}</text><line x1="{a}" y1="50" x2="{a}" y2="250" style="stroke:var(--line)" stroke-width="2" stroke-dasharray="4 6"/>' for a, b, lab in ZONES)
    st = []
    for x, n, y, up in MAP:
        ny, yy = (112, 132) if up else (196, 216)
        st.append(f'<circle class="st" cx="{x}" cy="155" r="11" stroke-width="5"/><text class="nm" x="{x}" y="{ny}" text-anchor="middle">{n}</text><text class="zn" x="{x}" y="{yy}" text-anchor="middle">{y}</text>')
    return f"""<svg class="map" viewBox="0 0 1000 300" role="img" aria-labelledby="map-t">
  <title id="map-t">Diagram of the Ben Fung Line across four zones, from Westpac in 1997 to the terminus at Gatwick Airport in 2026, with the Finyx Consulting line running alongside from 2009 to 2023. Every stop is listed below.</title>
  {z}
  <line class="m" x1="60" y1="155" x2="955" y2="155" stroke-width="12" stroke-linecap="round"/>
  {''.join(st)}
  <rect x="937" y="137" width="36" height="36" rx="6" style="fill:var(--main)"/><text class="nm" x="975" y="196" text-anchor="end">Gatwick</text><text class="zn" x="975" y="216" text-anchor="end">2026</text>
  <path class="b" d="M262 270 H800" stroke-width="8" stroke-linecap="round" fill="none"/>
  <circle class="bst" cx="262" cy="270" r="8" stroke-width="4"/><circle class="bst" cx="800" cy="270" r="8" stroke-width="4"/>
  <text class="bn" x="531" y="295" text-anchor="middle">Finyx Consulting, associate · Mar 2009 to Jun 2023</text>
</svg>"""


def stop(o, r, s, e, a, text, hl=None, term=False):
    facts = f'<ul class="facts">{"".join(f"<li>{h}</li>" for h in hl)}</ul>' if hl else ""
    how = f" · {ARRW[a]}"
    return f"""  <li class="stop{' term' if term else ''}">
    <p class="zone">{when(s, e)}</p>
    <h3>{o}</h3>
    <p class="role">{r}{how}</p>
    <p>{text}</p>{facts}
  </li>"""


TAGS = {"Gatwick Airport": ["&#163;2m budget", "&#163;1m avoided", "&#163;50k a year avoided"],
        "easyJet": ["Five project managers", "No components deferred", "No unplanned outages"],
        "London Stock Exchange Group": ["To schedule and budget", "Cyber forensics"],
        "HX / Hurtigruten Expeditions": ["Separation", "Seaware ERP"]}


def page():
    zones = []
    recent = [stop(o, r, s, e, a, " ".join([sc.split(" He also assessed")[0]] + [h for h in hl if "avoided" in h]), TAGS.get(o), term=(i == 0)) for i, (o, r, s, e, a, sc, hl) in enumerate(RECENT)]
    zones.append(("Zone 4 · 2022 to 2026", "Recent roles, the terminus first.", list(reversed(recent))[::-1]))
    for span, title, intro, rows in PHASES:
        zones.append((f"{span}: {title}", intro, [stop(o, r, s, e, a, d) for o, r, s, e, a, d in rows]))
    names = ["Zone 4", "Zone 3", "Zone 2", "Zone 1"]
    blocks = []
    for i, (h, intro, stops) in enumerate(zones):
        hid = f"z{4 - i}"
        head_ = h if i == 0 else f"{names[i]} · {h}"
        blocks.append(f'<section aria-labelledby="{hid}"><h2 id="{hid}" class="zonehead">{head_}</h2><p class="zonenote">{intro}</p>\n<ol class="line">\n' + "\n".join(stops) + "\n</ol></section>")
    return head("Ben Fung: line map", "/designs/line-map/", STYLE, "The Ben Fung Line: his career drawn as a transit map, from Westpac in 1997 to Gatwick Airport in 2026.", card="card-line-map.jpg") + f"""{switcher("line")}
<main id="main">
<header class="mast">
  <span class="badge" aria-hidden="true">BF</span>
  <div>
    <h1>The Ben Fung Line</h1>
    <p>Technology programme and project delivery across aviation, financial services and government. Change here for enterprise migrations, business separation, cybersecurity delivery and operational resilience.</p>
    <p>{mail_button()}</p>
  </div>
</header>

{svg()}

<div class="key" role="group" aria-label="Map key">
  <span><i class="m"></i>The main line: his roles, zone by zone</span>
  <span><i class="b"></i>The Finyx Consulting line: an associate relationship, 2009 to 2023</span>
  <span><i class="x"></i>A stop</span>
</div>

{chr(10).join(blocks)}

<section aria-labelledby="loop">
<h2 id="loop" class="loophead">The Finyx Consulting line</h2>
<p class="loopnote">Associate Consultant, Finyx Consulting, Mar 2009 to Jun 2023: an associate consultancy relationship that ran alongside the main line, spanning overlapping client assignments.</p>
</section>

<section class="ticket" aria-labelledby="travel">
  <img src="/assets/img/ben-fung-400.jpg" width="400" height="400" alt="Ben Fung, smiling, in a dark jacket and striped shirt">
  <div>
    <h2 id="travel">Travel information</h2>
    <p>PRINCE2 Practitioner and ITIL v3, achieved. Microsoft Certified: AI Transformation Leader (AB-731), in progress.</p>
    <p>{mail_button()}</p>
  </div>
</section>
</main>
<footer>
{site_links()}
{credit_line()}
</footer>
""" + END
