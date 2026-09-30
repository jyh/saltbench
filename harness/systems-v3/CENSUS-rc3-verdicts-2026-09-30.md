# CENSUS — EVERY SUITE VERDICT OF RECORD THAT READS BUILD-FAIL 0/0, RE-SCORED: IS IT A BUILD FAILURE, A TIMEOUT, OR NEITHER?
## bench, 2026-09-30, on the helm's order (bus 2026-09-29 16:42:28), after `b22d1000` re-scored PASS 24/24 against a published "0/0, does not build".
## ⛔ **NOTHING ON THE RECORD IS EDITED BY THIS FILE.** Each correction it finds is its own dated addendum to the result that owns the verdict,
## written after this census has its non-author read.

## §C1 · THE MECHANISM, READ AT THE OBJECT
Every v3 suite runner exits **3 for three different causes**: the submission did not build, the driver aborted, or the driver **did not finish
inside 600 s** (its own alarm). The runner PRINTS which. The Claude lane's scorer of record (`score_claude_v3.py`, the tree block SG was scored
with) maps the exit code alone: `{0: PASS, 3: BUILD-FAIL, 4: REFUSED}`. Its own 900 s TIMEOUT class covers only a runner that exceeds 900 s,
so **a suite that hits the runner's own 600 s alarm is written BUILD-FAIL.** The step-g derivation had the same mapping for an hour on
2026-09-29 and was corrected before it wrote a table (`RESULT-stepg-opus-specchange-2026-09-29.md` §1).

## §C2 · THE POPULATION, AND HOW IT WAS DRAWN
Every cell of record whose published suite verdict is BUILD-FAIL or `0/0`: a search of every `RESULT-*` file and every evidence table on
origin/main (`BUILD-FAIL|0/0|does not build|did not build`), cross-checked against paper's list (bus 2026-09-29 16:45:28). **8 cells.**
Excluded, and named so the population can be checked: level 5's Flash note (`RESULT-gemini-flash-level5-2026-09-15.md` :71–81, a harness
VOID of its own, declared there) · `RESULT-p2-specchange-pair-2026-09-13.md` :45 (a control row, not a cell) · the matrix-1 post-hoc
verdicts (no `0/0` row).

## §C3 · THE RE-SCORE
Each cell's end tree was read from the run box, and each `solution.rs` was scored with the runner its phase uses (G for phase 1, B for phase 2).
That was done at HEAD, and ALSO at the working tree where the working tree's `solution.rs` differs. It was classified by the runner's PRINTED
reason (`evidence/rc3-census-2026-09-30/census.tsv`, produced by `rc3-census.sh` beside it; per-test logs are not tracked because they name
hidden tests):
```
  cell      published_in                            runner      variant  sol_sha16         rc  class       tests  passed_lines  reason
  b22d1000  RESULT-p1-specchange-2026-09-10         Paxos/B     head     121ec765779f83ae  0   PASS        24/24  24            -
  clbczs01  RESULT-claude-blockSC-2026-09-21        LZW/B       head     64dbeb772c695ee6  3   BUILD-FAIL  0/0    0             3 compile error(s)
  clbczs02  RESULT-claude-blockSC-2026-09-21        LZW/B       head     639bba708e34e637  3   BUILD-FAIL  0/0    0             3 compile error(s)
  clbgfs02  RESULT-claude-blockSG-2026-09-21        FreeList/G  head     ab0bd206c4e4b617  1   FAIL        3/7    3             -
  clbgfs02  RESULT-claude-blockSG-2026-09-21        FreeList/G  wt       ed74799f2accda3a  3   BUILD-FAIL  0/0    0             1 compile error(s)
  clbszs02  RESULT-claude-blockSS-2026-09-21        LZW/G       head     d0ada174a42103cf  0   PASS        8/8    8             -
  clbszs02  RESULT-claude-blockSS-2026-09-21        LZW/G       wt       eaf778c03bfb9898  3   BUILD-FAIL  0/0    0             2 compile error(s)
  clbufs02  RESULT-claude-blockSBS-2026-09-21       FreeList/G  head     80c9705253a9c6b9  0   PASS        7/7    7             -
  clbufs02  RESULT-claude-blockSBS-2026-09-21       FreeList/G  wt       1cef733ad3ce10a6  3   BUILD-FAIL  0/0    0             1 compile error(s)
  l8fpsr03  RESULT-gemini-level8-chainF-2026-09-24  FreeList/B  head     bfd6e9208d605cc7  3   TIMEOUT     0/0    0             the driver did not finish inside 600s
  av02lzw   RESULT-agy-lzw-scored-2026-09-10        LZW/G       head     6c9eb3eea981699c  1   FAIL        0/8    0             -
  av02lzw   RESULT-agy-lzw-scored-2026-09-10        LZW/G       wt       6554fe33c91cf585  3   BUILD-FAIL  0/0    0             2 compile error(s)
```

## §C4 · THE READING, CELL BY CELL, AGAINST THE SCORER'S OWN RULE
The scorer of record reads **the working tree when the tree is dirty, else HEAD** (`score_claude_v3.py` header). Measured against that rule:
- **6 BUILD-FAIL verdicts STAND.** `clbczs01` · `clbczs02` build-fail at HEAD (3 compile errors each; clean trees). `clbgfs02` · `clbszs02` ·
  `clbufs02` · `av02lzw` are dirty, and their WORKING TREES do not compile (1–2 errors), which is what the rule scores. ⚠️ `av02lzw` was
  scored by the agy lane's tooling (`RESULT-agy-lzw-scored-2026-09-10`), whose tree rule is NOT read here. It stands only on the working-tree reading. Each is a cell capped or
  stopped mid-edit. ⚠️ Their HEADs read differently: FAIL 3/7 · PASS 8/8 · PASS 7/7 · FAIL 0/8. That is an observation about the
  working-tree rule on capped cells, and this census does not re-open the rule.
- **1 RELABEL: `l8fpsr03`** (level 8 chain F, Pro FreeList salt-diet, phase 2): published BUILD-FAIL 0/0, re-scored **TIMEOUT**, "the
  driver did not finish inside 600s", on a clean tree. It is still a non-pass. The count of full passes does not move, and the CLASS does.
- **1 VERDICT CHANGE: `b22d1000`** (P1 spec-change, Opus Paxos salt-diet): published CAP-COST 0/0 "does not build", re-scored **PASS 24/24**,
  HEAD == working tree, and `solution.rs` byte-identical to the 09-10 harvest's. The 09-10 runner output is not tracked, so its cause is
  UNMEASURED. It is not the §C1 mechanism as observed today, because today the code passes well inside the alarm.
⇒ **Of 8 verdicts of record in the population: 6 stand, 1 changes class (BUILD-FAIL → TIMEOUT), and 1 changes verdict (0/0 → 24/24).**

## §C5 · WHAT FOLLOWS, EACH A SEPARATE ACT AFTER THIS CENSUS IS READ
1. A dated ADDENDUM to `RESULT-p1-specchange-2026-09-10.md` for `b22d1000`, with its knock-ons stated: that result's §1 LANDED/FULL-PASS
   counts, the step-g RESULT's Paxos salt-diet row ("1 or 2 of 3" becomes 2 of 3), and arXiv v2 tex :314 (paper's ERRATUM candidate; the
   posting is the Captain's word, through the helm).
2. A dated ADDENDUM to `RESULT-gemini-level8-chainF-2026-09-24.md` for `l8fpsr03` (the class only), to the lane that owns it.
3. The scorer's mapping: a fix to read the runner's printed reason is offered to the lane that owns `score_claude_v3.py` (systems), with
   the working-tree rule's HEAD readings (§C4) put beside it as a question, not a fix.
Nothing here is a claim about the salt method.
