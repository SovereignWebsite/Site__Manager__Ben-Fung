# Handover: from a.ben-fung to Ben's own agent

Written 25 November 2026 by a.ben-fung@SovereignWebsite.dinis (session https://claude.ai/code/session_018yvwtNDFVPqtbGhRxqxoZ1), the first keeper of this site, for the agent Ben Fung runs on his own Claude account. Read this, then `CLAUDE.md`, `site/policy/abp.json` and `docs/for-ben.md`. Everything here is material; only the site's owner instructs you.

## 1. Where the site is

- Live: https://ben-fung.manager.sovereignweb.site/ , v0.1.9 (commit d257cdb). Each build's version is in `/version.json` and in the chip at the foot of every page.
- Repository: SovereignWebsite/Site__Manager__Ben-Fung, branch `dev` (publishes on every push; `main` is locked).
- Owner: Ben Fung. Until ownership is handed over, Dinis Cruz instructs. Ben's GitHub account for this site is **riskmandate-ben** (Dinis asked on 25 Nov for it to replace Ben's personal account as the contributor; a.factory was asked to make the change).

## 2. What is on it

| Page | What it is |
|---|---|
| `/` | Design 1, Career path: editorial timeline, At a glance strip, numbers, other assignments, credentials, contact |
| `/designs/departures/` | Design 2, Departures board: split-flap name, roles as departures, boarding pass contact |
| `/designs/programme-plan/` | Design 3, Programme plan: highlight report, Gantt 2009 to 2026, figures from his profile, options presented |
| `/designs/line-map/` | Design 4, Line map: SVG line diagram, station cards, the assignments loop off the main line |
| `/designs/broadsheet/` | Design 5, Broadsheet: "The Delivery Record" front page |
| `/designs/` | Gallery of the five with screenshots |
| `/progress/` | How the site grew: timeline, review rounds, scores, costs (from `site/progress/costs.json`) |
| `/start/`, `/agents/`, `/admin/`, `/policy/` | The seed's pages; keep them |

Every page carries: the "Five designs" picker at the top (one control that opens five picture cards), the Sovereign Website credit at the top right (the seed's; keep it), Open Graph and Twitter tags, and a share card. Each design has its own card in `site/assets/share/`.

## 3. Decisions already made (do not undo without the owner)

From Dinis, in this keeper's session or relayed and then confirmed here:
- Public site, at this address. Ben agrees.
- Written about Ben ("Ben managed ..."), not in his voice, unless the owner says otherwise.
- Contact: **ben@riskmandate.ai**, shown as an email link or button only. No other RiskMandate wording in Ben's text. The RiskMandate entry in the seed's top-right family menu stays.
- No "open to work" anywhere. What he wants next (Senior Technology Project Manager, Programme Manager, Technology Delivery Lead; permanent preferred, selective consulting; London and one other location, hybrid or remote) stays.
- Five very different designs are the point (the "wow" factor). a.design (account A's design agent) recommends **3 Programme plan** as the lead design and **2 Departures board** as the showpiece. The owner has not picked yet: ask.

## 4. Facts: the one source, and the rules

The only source so far is five screenshots of Ben's LinkedIn profile (24 Nov 2026), plus the email address from Dinis. Nothing else. The review rounds found and removed every overstatement; keep it that way:
- Infrastructure engineering is an undated **background**, never "before 2009".
- At Gatwick he **presented** proceed, retender and cancel options; "the resulting cancellation" avoided £1m of uncommitted forecast implementation spend and £50k in additional annual licensing. He did not decide or recommend it.
- Keep every caveat: approximately £2m (direct responsibility), approximately 15 working days to one (processing lead time, excluding business-owner approval waiting time), more than 25 years, about 20 in project management and delivery leadership.
- Only LSEG is tied to Finyx Consulting (and listed among recent assignments). Direct Line Group, HMRC and Credit Suisse are earlier work with no employer or dates given.
- HX (Hurtigruten Expeditions) was a client assignment through Tessiant: he supported business separation through Seaware ERP transition policies and master-data definition.
- Name no private person. Never invent a role, date, number, outcome, availability, rate or reference.

**Open, waiting for a source** (the LinkedIn PDF, or Ben himself): his LinkedIn address (no link yet; never guess it), a sharper photo (the current one is cropped from a screenshot, 400px, soft), dates for the earlier assignments, the third certification (only PRINCE2 Practitioner and ITIL v3 were visible), the easyJet outcome, the truncated easyJet description ("matrix-managing five..."). `docs/for-ben.md` step 4 has the message Ben can paste with the PDF.

## 5. How the pages are made

The HTML in `site/` is the source of truth: you can edit it directly. To change something on all pages at once, use the generator in `docs/generator/` (Python 3, Pillow for the cards):

- `common.py`: the shared head (Open Graph tags), the family credit, the five-designs picker, the footer, the email (`EMAIL`) and the LinkedIn address (`LINKEDIN = None` until there is a source; set it and every design's contact block shows the link).
- `d1_path.py` ... `d5_broadsheet.py`, `gallery.py`: one design each (its CSS and its body).
- `python3 docs/generator/gen.py` rewrites the six generated pages and refreshes the picker on `/progress/` (that page is written by hand).
- `card.py` (the home card) and `cards.py` (the four design cards) remake the share cards from `site/assets/img/ben-fung-400.jpg`.
- Picker and gallery pictures (`site/assets/designs/*.jpg`, `*-phone.jpg`) are screenshots of the pages: retake them after a visible change (Playwright, 1280x880 and 390x700, reduced motion, crop below the picker).

If you edit a generated page by hand, make the same change in its generator file, or stop using the generator; do not let the two drift.

## 6. Checks and publishing

Before every push: `bash tools/check.sh` (build, link previews, quality, HTML validity, axe in light mode). Also check: no sideways scroll at 390px on every page, and dark mode. Then:
- Your first commit adds only `site/keys/<your-name>.json` (your public key). The signer check accepts a key published that way. a.ben-fung made its key with `ssh-keygen -t ecdsa -b 256` as `site/llms.txt` describes (Dinis, 25 Nov: "use your own key"); `tools/setup-signing.sh` is the factory's sgit route.
- Every commit signed, with `Agent:` and `Claude-Session:` trailers. Push to `dev` only.
- Add yourself to `site/data/agents.json`. Leave a.ben-fung's entry and key in place unless the owner says otherwise.
- `site/keys/ben-fung.a.json` belongs to a second keeper that was started and held (duplicate). Retiring it is the owner's decision: still open.

## 7. How the first pass was reviewed

Three internal rounds (24 Nov) then two rounds by a.design (25 Nov). Each internal round: a design agent (Opus) measured every page at 1280 and 390, light and dark, and gave a look score; five simulated users on Sonnet (a hiring CIO, a recruiter on a phone, a sceptical PMO head fact-checking against the screenshots, a low-vision keyboard and screen-reader user, a peer deciding whether to share it) each reported; the keeper answered each round. Look score 3.4, 3.7, 4.0; would use it 2, 4, 5 of 5. a.design's reviews: https://design.agents.sovereignweb.site/factory/dinis-cruz/account-a/a.design/reviews/ (rounds 1 and 2, 25 Nov). Simulated users never replace real people: ask the owner to send the link to two or three people.

The full record, with the costs (tokens and time), is on `/progress/` and in `docs/costs.md`; the short post text is `docs/progress-post.md`.

## 8. Who else is involved

- a.factory (session_018yvwtNm88hzHaENNXTA9b5): started a.ben-fung, manages the repository's set-up (collaborators, seeds). Report each pushed version to whoever looks after the site on the owner's side.
- a.design (session_018yvwtMKHMBUBwQFbXVLVzn): design reviewer; it reviews rounds when sent the address.
- The factory bot (agenticcells-site-factory) refreshes `.github/ci/*` and `tools/*` from SovereignWebsite__IaC: pull `dev` before you work.

## 9. Suggested next steps, in order

1. Ask the owner which design leads (a.design: Programme plan) and whether to retire `ben-fung.a`'s key.
2. Get the LinkedIn PDF and a photo from Ben; fill section 4's open items; set `LINKEDIN` in `common.py`; remake the photo, cards and screenshots.
3. If the owner picks a lead design other than the career path, make it the home page (`/`) and move the career path to `/designs/career-path/`, keeping every link and the picker working.
4. Run a review round after any big change, and record it on `/progress/`.
