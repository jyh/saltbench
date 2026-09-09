# RESULT — THE POST-HOC CORRECTNESS PASS OVER MATRIX #1
## Run 2026-09-09. **Every number here is derived from the verdicts table beside it, not retyped.**

⛔ **THIS IS A DECLARED POST-HOC MEASUREMENT.** The analysis was frozen at
`PRESPEC-posthoc-correctness-matrix1-2026-09-09.md`, commit `437ea70`, **14:57:28, before the first
suite touched any cell repo.** The author already knew the cost result and the pre-spec says so in its
own first section. It is not a pre-registered result and may never be presented as one.

## PROVENANCE
```
  referee        tasks/systems-v3/<problem>/G/run_tests.sh at backup/systems-v3 ebe686c
  toolchain      the six-name contract in ~/cells/toolchain.env, enforced by rust_env.sh
                 (VERUS_SHA256 checked against the binary — a wrong toolchain is REFUSED, not scored)
  runner         arm-blind by construction: "no arm detection: every submission is built the same way"
  staging        a fresh root outside every cell root; withheld material entered no readable tree
  spend          ZERO model tokens. 43 cells, 246s total, mean 5.7s/cell.
```

## §1 · CLASSES, WITH THE REGISTERED RULE APPLIED
```
  PASS           35
  FAILED-BOOT    4
  CAP-COST       3
  FAIL           1
```
⛔ **`CAP-COST` AND `FAILED-BOOT` ARE NEVER POOLED INTO `FAIL` (pre-spec §3 rule 1).** The runner
returns non-zero for a cell that never booted, so the raw tally read **5 FAIL**; the registered rule
gives **1**. ⇒ ***FOUR CELLS THAT PRODUCED NO SUBJECT BEHAVIOUR WOULD OTHERWISE HAVE BEEN PUBLISHED
AS CORRECTNESS FAILURES.*** The pre-spec's first job was catching the instrument, not constraining the author.

## §2 · THE REGISTERED READING — LANDED CELLS, BARE ARMS, PER PROBLEM
```
  problem     plain      salt-diet
  Crc32      3/3        3/3        tie
  FreeList   4/4        0/1        differs
  LRU        4/4        3/3        tie
  LZW        3/3        3/3        tie
  Paxos      4/4        2/2        tie
```
⇒ **4 ties, 1 informative pair. The cross-problem sign test cannot reach significance and does not try.**
⭐ **This outcome is registered in pre-spec §4 before any suite ran** — *"the instrument did not
separate the arms"* — together with an explicit refusal to run a second analysis. **There is none.**

## §3 · ⭐⭐ THE FINDING THE PASS WAS NOT LOOKING FOR: BUDGET STOPS ARE ARM-CORRELATED
```
  plain      FAILED-BOOTS 1  LANDED 18
  salt-diet  CAP-COST 3  FAILED-BOOTS 3  LANDED 12
```
⇒ 🔑 ***THE ARM THAT COSTS MORE IS SYSTEMATICALLY LESS LIKELY TO BE ASKED THE CORRECTNESS QUESTION.***
The cells dropped from the salt arm are the ones that ran long enough to hit a cap — **the hard ones** —
so the surviving salt sample is easier and **salt's pass rate is biased UP by construction.**
**This is a selection effect, it is arm-correlated, and it travels with any correctness number here.**

⭐ **AND A BUDGET STOP IS NOT A CORRECTNESS FAILURE — MEASURED:** both capped FreeList salt cells
scored **7/7**. Reporting `FreeList salt-diet 0/1` alone would mislead: of its priced cells, **two
passed completely**, one landed at 6/7, one never booted.

## §4 · WHAT A PASS DOES NOT MEAN
⛔ **A PASS IS NOT "CORRECT". IT IS "THE WITHHELD SUITE DID NOT FAIL IT."** The suites' measured
strength is 44 of 44 mutants killed — **a CEILING, not a strength**: authored beside the tests, seven
dying to a single test. ⇒ **No sentence may join the cost premium to correctness with "and therefore".**
