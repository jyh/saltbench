# RESULT — P1 spec-change across the pilot five at Opus, 19 cells, phase 2 on reused landings
**bench · 2026-09-10 · fired 18:59:09Z, harvested and scored 21:5xZ**

⛔ **Every number comes from `RESULT-p1-specchange-2026-09-10.tsv`**, which names the `METER.txt` each
row was read from; the analysis is `RESULT-p1-specchange-analysis-2026-09-10.txt`. Verdicts are from
each task's `B/run_tests.sh` — **the post-change suite, the runner the referee uses** — driven against
copies, every archive hash-checked before and after and byte-unchanged. **Nothing is retyped.**

## §1 · ⭐⭐ THE VERDICT, AND THE TWO HEADLINE NUMBERS DISAGREE ABOUT WHICH CELLS
```
  19 cells · 5 tasks · 2 arms · claude-opus-5 verified at message.model in every transcript
  LANDED     16/19          FULL PASS  16/19          <- the SAME number
  plain      landed 8/9     full pass 8/9
  salt-diet  landed 8/10    full pass 8/10
```
⇒ ⛔⛔ **AND THEY ARE NOT THE SAME SIXTEEN.**
```
  landed but NOT a full pass   f33c7e65  FreeList salt-diet  LANDED    8/9
  full pass but NOT landed     9e6c8d4d  Paxos    salt-diet  CAP-COST  24/24
```
⇒ 🔑 ***A CAMPAIGN REPORTING ONLY THE LANDING RATE WOULD HAVE HAD THE RIGHT NUMBER AND THE WRONG
CELLS.*** This is ADDENDUM 10 replicated **inside a single wave**, in both directions, having been
written hours earlier from two separate ones: a cell declared done with a failing test, and a cell
stopped on budget whose code is correct.

## §2 · EVERY CELL THAT IS NOT A FULL PASS, NAMED RATHER THAN AGGREGATED AWAY
```
  b22d1000  Paxos     salt-diet  CAP-COST  0/0     >= $19.56  CENSORED   does not build
  f6462d47  Paxos     plain      CAP-COST  23/24   >= $19.78  CENSORED
  f33c7e65  FreeList  salt-diet  LANDED     8/9       $14.81
```

## §3 · BY TASK — NOT POOLED, BECAUSE POOLING ACROSS TASKS IS A CONFOUND THIS CAMPAIGN CARDS
```
  Crc32     plain 3/3   salt-diet 3/3        LRU    plain 2/2  salt-diet 3/3
  FreeList  plain 2/2   salt-diet 0/1        LZW    salt-diet 1/1
  Paxos     plain 1/2   salt-diet 1/2
```
⇒ **The arms are level on every task except FreeList and Paxos**, and those are exactly the tasks with
the thinnest cells — `FreeList salt-diet` is **n=1** here because its reusable phase-1 pool was short.
**A 0/1 is not a rate.**

## §4 · COST AND TOKENS, BOTH (the Captain's ruling, H7-ter)
```
  arm          n  median $   median T   median output    $/M-T   $/M-output
  plain        8     13.52   15,213,405     162,557      0.901      80.73
  salt-diet    8      9.99   11,087,020     111,675      0.864      89.58
  wave totals: T 284,599,552 · cache_read 275,776,507 (96.9 %) · output 2,954,679 (1.04 %) · $250.93
```
⇒ **The reversal holds in direction**: cheaper per token of traffic, dearer per token produced —
consistent with the four other roots in `../systems-v3-analysis/`.
⛔ **BUT THE MEDIANS EXCLUDE THE THREE CENSORED CELLS AND THE EXCLUSION IS ARM-CORRELATED** — 2 of 10
salt-diet against 1 of 9 plain, and all three are among the most expensive cells in the wave. ⇒ **The
absolute medians must not be read as an arm cost comparison.** The `$/M` rates include every cell and
are therefore **FLOORS** wherever a censored cell contributes.

## §5 · WHAT THIS DOES NOT SUPPORT
n = 9 and 10, five tasks, **one model**, greenfield-then-spec-change only. No p-value, no interval, and
no claim that either arm is better: **on the measurement that matters the two arms are 8/9 and 8/10,
and the difference is one cell that does not build.**
⛔⛔ **AND IT IS NOT COMPARABLE TO THE GEMINI RESULT** (`RESULT-agy-lzw-scored-2026-09-10.md`), for a
structural reason `systems` measured today and not merely a difference of degree: **Claude cells launch
with `--dangerously-skip-permissions`; agy cells REFUSE that flag by construction**, so on agy the
client allowlist *is* the command fence. **The two arms are not equally fenced by design.** Any
cross-vendor number taken across that boundary compares two different experiments.

## §6 · PROVENANCE — THREE RUNS, AND THE TWO THAT WERE DISCARDED ARE IN THE RECORD
Run 1 (18:44Z) died on inherited `settings.json` pointing at another wave's `_bin`, then on a fence
sealed before those settings were repaired — **16 held boots, zero model spend**, every refusal landing
before the client started. Run 2 is this run. ⇒ **A fresh cells root needs `settings` → `fence` →
`trust`, in that order, because the fence render reads `settings.json`;** the fire script now refuses
before the first launch unless all three hold for that root, driven RED before it was trusted.
📌 **Zero spurious `landing-1` declarations across all 19 cells**, against 4 of 4 in the pilot's voided
run, which is the marker gate working.
