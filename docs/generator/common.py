HOST = "https://ben-fung.manager.sovereignweb.site"
EMAIL = "ben@riskmandate.ai"
LINKEDIN = None  # waiting for Dinis: take it from the LinkedIn PDF, never guess
REPO = "https://github.com/SovereignWebsite/Site__Manager__Ben-Fung"
DESC = "Ben Fung leads technology change across aviation, financial services and government: enterprise migrations, business separation, cybersecurity delivery and operational resilience."

DESIGNS = [
    ("/", "Career path", "path"),
    ("/designs/departures/", "Departures board", "departures"),
    ("/designs/programme-plan/", "Programme plan", "plan"),
    ("/designs/line-map/", "Line map", "line"),
    ("/designs/broadsheet/", "Broadsheet", "broadsheet"),
]

FAMILY = """<details class="family-credit">
  <summary>Sovereign Website</summary>
  <ul>
    <li><a href="/start/">Start here</a></li>
    <li><a href="/agents/">Use with your AI</a></li>
    <li class="family-gap"><a href="/admin/">How this site was made</a></li>
    <li><a href="https://sovereignwebsite.ai/">Sovereign Website</a></li>
    <li><a href="https://sovereignwebsite.org/">Principles</a></li>
    <li><a href="https://sovereignwebsite.site/">Hosted</a></li>
    <li><a href="https://hub.sovereignweb.site/">Hub</a></li>
    <li><a href="https://agents.sovereignweb.site/">Agents</a></li>
    <li><a href="https://vault.sovereignwebsite.site/">Vault</a></li>
    <li><a href="https://agenticcells.ai/">AgentiCCells</a></li>
    <li><a href="https://riskmandate.ai/">RiskMandate</a></li>
    <li><a href="https://newsroom.sgit.ai/">Newsroom</a></li>
  </ul>
</details>"""


def head(title, path, style, desc=DESC, card="card-1200x630.jpg", alt=None):
    url = HOST + path
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Ben Fung">
<meta property="og:locale" content="en_GB">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{HOST}/assets/share/{card}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Ben Fung: technology programme and project delivery across aviation, financial services and government.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{HOST}/assets/share/{card}">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="/assets/site.css">
<style>
{style.strip()}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{FAMILY}
"""


THUMB = {"path": "career-path", "departures": "departures", "plan": "programme-plan", "line": "line-map", "broadsheet": "broadsheet"}


def switcher(current):
    names = {k: n for _, n, k in DESIGNS}
    here = f'<span class="here">this is {names[current]}</span>' if current in names else ""
    out = ['<nav class="designs" aria-label="Five designs of this page">', '<details>', f'  <summary><span class="lbl">Five designs</span>{here}</summary>', '  <ul class="dcards">']
    for i, (href, name, key) in enumerate(DESIGNS, 1):
        cur = ' aria-current="page"' if key == current else ""
        out.append(f'    <li><a href="{href}"{cur}><img src="/assets/designs/{THUMB[key]}-phone.jpg" width="300" height="400" alt=""><span>{i}. {name}</span></a></li>')
    out.append('  </ul>')
    out.append('  <p class="all"><a href="/designs/">See all five side by side</a></p>')
    out.append('</details>')
    out.append("</nav>")
    return "\n".join(out)


def site_links():
    return """<nav class="site-links" aria-label="About this site">
  <a href="/start/">Start here</a>
  <a href="/agents/">Use with your AI</a>
  <a href="/admin/">How this site was made</a>
  <a href="/policy/">How this site is governed</a>
  <a href="/progress/">How this site grew</a>
</nav>"""


def credit_line():
    return f'A sovereign website, made with the <a href="https://sovereignwebsite.org/">open pattern</a>. Source: <a href="{REPO}">github.com/SovereignWebsite/Site__Manager__Ben-Fung</a>.'


def contact_links(cls=""):
    c = f' class="{cls}"' if cls else ""
    out = [f'<a{c} href="mailto:{EMAIL}">{EMAIL}</a>']
    if LINKEDIN:
        out.append(f'<a{c} href="{LINKEDIN}">LinkedIn profile</a>')
    return out


END = "</body>\n</html>\n"


def mail_button(cls="mailbtn"):
    return f'<a class="{cls}" href="mailto:{EMAIL}">Email Ben · {EMAIL}</a>'
