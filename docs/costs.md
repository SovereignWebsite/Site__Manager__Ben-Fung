# Costs of creating Ben Fung's site

As of 24 November 2026, 15:36 UTC. Tokens and time only, not money. Source: the session ledger (figures as reported by the harness when each agent run finished), the review folders and git. Anything not recorded is marked "not measured".

## Round 1

| Agent | Model | Tokens | Tool uses | Seconds |
|---|---|---:|---:|---:|
| recruiter | Sonnet | 78,733 | 7 | 44.9 |
| CIO | Sonnet | 83,166 | 8 | 52.4 |
| peer | Sonnet | 91,127 | 13 | 66.1 |
| accessibility | Sonnet | 84,817 | 9 | 92.3 |
| sceptic | Sonnet | 95,376 | 8 | 95.1 |
| design | Opus | 151,529 | 20 | 219.4 |
| **Round total** | | **584,748** | 65 (measured only) | **570.2** |

## Round 2

| Agent | Model | Tokens | Tool uses | Seconds |
|---|---|---:|---:|---:|
| CIO | Sonnet | 94,612 | not measured | 35.4 |
| recruiter | Sonnet | 87,576 | not measured | 37.7 |
| sceptic | Sonnet | 109,531 | not measured | 54.7 |
| peer | Sonnet | 105,225 | not measured | 59.0 |
| accessibility | Sonnet | 96,314 | not measured | 71.5 |
| reporter | Sonnet | 94,642 | 13 | 107.7 |
| design | Opus | 197,192 | 18 | 156.8 |
| **Round total** | | **785,092** | 31 (measured only) | **522.8** |

## Round 3

| Agent | Model | Tokens | Tool uses | Seconds |
|---|---|---:|---:|---:|
| CIO | Sonnet | 103,662 | not measured | 32.3 |
| recruiter | Sonnet | 95,400 | not measured | 35.7 |
| peer | Sonnet | 116,793 | not measured | 52.8 |
| sceptic | Sonnet | 134,797 | not measured | 74.5 |
| accessibility | Sonnet | 106,757 | not measured | 85.6 |
| design | Opus | 230,140 | not measured | 148.8 |
| **Round total** | | **787,549** | 0 (measured only) | **429.7** |

The reporter run (round 2 table) was a single pass on the /progress/ page, not a reviewer.

## Totals by model

| Model | Runs | Tokens | Agent-seconds |
|---|---:|---:|---:|
| Opus | 3 | 578,861 | 525.0 |
| Sonnet | 16 | 1,578,528 | 997.7 |
| **All** | 19 | **2,157,389** | **1522.7** |

Opus ran the design agent only (three runs). Sonnet ran the five simulated users in three rounds and the reporter. The keeper (Opus) is not in these totals.

## Cost per review round

| Round | Tokens | Agent-seconds | Wall-clock |
|---|---:|---:|---|
| 1 | 584,748 | 570.2 | about 3 min |
| 2 | 785,092 | 522.8 | about 4 min |
| 3 | 787,549 | 429.7 | about 3 min |

Round 2 includes the reporter run (94,642 tokens, 107.7 s), which was not a review. Without it, round 2 is 690,450 tokens and 415.1 agent-seconds.

## Wall-clock against agent time

- Seed commit (13:06:19 UTC) to last ledger entry (15:36): 2h29m41s (8,981 s).
- Of that, about 1h59m passed before the keeper started (~15:05), with no recorded activity.
- Keeper active: about 31 minutes (~15:05 to 15:36), approximate.
- Agent time summed over all 19 recorded runs: 1522.7 s (about 25.4 min). This is more than the review wall-clock (about 10 min across three rounds) because the six reviewers in each round ran in parallel.

## Keeper (main agent) usage, harness-reported, separate basis

At 15:35:03 UTC the harness reported cumulative usage for the keeper session: Opus 320 input, 140,261 output, 469,032 cache-creation and 27,426,135 cache-read tokens (32,534 thinking). A Sonnet line (176 input, 84,417 output, 614,624 cache-creation, 5,769,241 cache-read) and a tiny Haiku line (1,228 input, 22 output) also appear. It is not stated whether these include subagent runs, and the basis differs from the ledger's subagent_tokens, so they are not added to the totals above.

## Not measured

- Keeper (main agent, Opus) tokens: not in the ledger; harness cumulative figures are given separately under keeper_harness_usage, on a different basis, and are not added to totals.
- Accountant (this run, Sonnet): tokens, tool uses and seconds not measured, because the harness reports them only after the run ends.
- Tool uses not measured for all round 2 and round 3 simulated users and for the round 3 design agent (ledger gives tokens and seconds only). Round 2 design (18) and reporter (13) are recorded.
- Per-agent token split between input and output is not measured (ledger gives one subagent_tokens figure per run).
- Keeper's own elapsed time is only approximate: the ledger says '~15:05' for its start; its hours of thinking time versus waiting is not measured.
- Time between the seed commit (13:06) and the keeper start (~15:05) is not measured as work: it is elapsed time with no recorded activity.
- Reporter run timing is placed in round 2 from its 15:31 ledger entry; it was not part of a review round.
- Money cost: not measured and not stated (tokens, not money).
- Time spent by Dinis Cruz (providing materials, reading) is not measured.

## Notes

- Agents ran in parallel within each round, so agent-seconds exceed wall-clock time.
- Ledger times are UTC and given to the minute; durations are as the harness reported when each run finished.
- The keeper has committed nothing (signing blocked), so git shows only the seed commit fbfb222.
- Totals cover only runs recorded in the ledger (19 runs: 18 reviewer runs across 3 rounds plus 1 reporter run).
- Tool-use totals are sums of the measured values only and understate the real count.
