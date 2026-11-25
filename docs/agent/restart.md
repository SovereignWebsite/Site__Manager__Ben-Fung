# Restart: how a new session takes over Ben Fung's site

For cl-4.ben-fung@SovereignWebsite.dinis (account D) or Ben's own agent.

1. Attach the repository SovereignWebsite/Site__Manager__Ben-Fung, branch `dev`. Pull before work (the factory bot refreshes `.github/ci` and `tools`).
2. Read, in order: `CLAUDE.md`, `docs/handover.md`, `docs/agent/now.md`, `site/policy/abp.json`, `docs/for-ben.md`.
3. Make your own signing key (`ssh-keygen -t ecdsa -b 256`, as `site/llms.txt` describes, or `tools/setup-signing.sh`). First commit: only `site/keys/<your-name>.json`. Every commit signed, with `Agent:` and `Claude-Session:` trailers; push to `dev` only. Add yourself to `site/data/agents.json`.
4. Before every push: `bash tools/check.sh`; also check 390px width and dark mode. To change all pages, use `docs/generator/` (`python3 docs/generator/gen.py`).
5. Report each pushed version to whoever looks after the site (a.factory's successor); ask the owner the open questions in `docs/agent/now.md`.
6. No wake schedule is needed: the site changes only when the owner asks.
