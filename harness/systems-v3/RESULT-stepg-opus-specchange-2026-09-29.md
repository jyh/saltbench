# RESULT — STEP g: SEVEN OPUS SPEC-CHANGE CELLS; SIX CONDITIONS REACH n = 3 OF RECORD, EACH WITH ITS PHASE-1 REACH BESIDE IT
**bench · 2026-09-29 · fired 18:29Z → last end 23:00:52Z · registered by `AMENDMENT-stepg-opus-specchange-2026-09-29.md` (signed; ADDENDA 1–2)**

⛔ **Every figure in the code blocks below is rendered from `evidence/stepg-2026-09-29/cells.tsv` and `reach.tsv` by
`RESULT-stepg-opus-specchange-2026-09-29-verify.py`, which asserts each block is present in this file's bytes.** Those tables were produced
by `evidence/stepg-2026-09-29/stepg-derive.sh`, reading each cell on the run box: `ctl/end-2`, `ctl/post-end-2.tsv`, the served receipt
(`served_models_v3.py check-cell`), the transcripts' client version, `ctl/copied-from.tsv` and `ctl/parent`. It also runs each task's
`B/run_tests.sh` (the post-change suite, the runner the P1 wave used) over a copy of the cell's `solution.rs` at HEAD. **Nothing is retyped.**
⚠️ **The verifier's coverage is the seven new cells and the reach table.** The older cells of each condition (§3) are cited from their own
results of record by file and line, and it does not re-derive them.

## §1 · THE SEVEN CELLS
```
  cell      task      arm        end-2     suite     tests  regr   clause  phase-2 $   served head        source
  clbkzp01  LZW       plain      LANDED    PASS      15/15  0/8    0/7     18.96      claude-opus-5=155  cells-matrix1/c34012e0
  clbklp01  LRU       plain      LANDED    PASS      23/23  0/16   0/7     9.58       claude-opus-5=176  cells-gf-topup-1/61d2fda3
  clbkfp01  FreeList  plain      LANDED    PASS      9/9    0/7    0/2     17.46      claude-opus-5=187  cells-gf-topup-1/db0847aa
  clbkpp01  Paxos     plain      CAP-COST  PASS      24/24  0/16   0/8     18.80      claude-opus-5=161  cells-gf-topup-1/bc7997bd
  clbkps01  Paxos     salt-diet  LANDED    TIMEOUT   0/0    -      -       18.72      claude-opus-5=223  cells-gf-topup-1/d9998c97
  clbkfs01  FreeList  salt-diet  LANDED    PASS      9/9    0/7    0/2     12.44      claude-opus-5=195  cells-gf-topup-1/c17630f0
  clbkfs02  FreeList  salt-diet  LANDED    PASS      9/9    0/7    0/2     9.69       claude-opus-5=159  cells-gf-topup-1/783df512
```
SUITES: PASS 6 · TIMEOUT 1 · SERVED: head claude-opus-5 in 7 of 7 · verdict clean · client 2.1.259
SPEND: 7 cells, phase 2 only, $105.64 in all  =  2.95 – 3.35 pt
- Every cell is a COPY of its §G1 source, with phase 2 dispatched onto the copy (tag P1). The C2 cap ($18.60) meters the copy's own slug,
  so the phase-2 dollars above are phase 2 alone, never the source's phase 1.
- **`clbkpp01` is CAP-COST and passes 24/24.** Under lane B §CLB-R.2 clause 2 it is a cell of record at its suite result, and the cap is the
  selector. The P1 wave's `f6462d47` (Paxos plain) also capped, at 23/24.
- ⛔ **`clbkps01` LANDED and its suite is TIMEOUT.** The driver ran 23 tests to PASS, then the next test ran on CPU until the runner's 600 s
  alarm. That was reproduced on a second run by itself (9 m 56 s user time), so it is not box load. The runner prints `TESTS 0/0` on a timeout, and the
  23 is an observation from its log, not a score. **A self-graded landing whose code does not pass is the case this repository's CLAUDE.md
  warns about.** It counts as a non-pass at its end kind.
- ⚠️ **Instrument note:** the runner's rc 3 means "did not build, aborted, or timed out", and the runner prints which. The derivation's first
  version mapped every rc 3 to BUILD-FAIL. It was corrected to read the printed reason before any table was written (§5).

## §2 · THE MANDATORY REACH COLUMN — PHASE-1 LANDED / PHASE-1 CELLS WITH AN END, PER CONDITION
The helm's ruling on the freeze (§G5.1 departs from §CLB-R.2 clause 5): every source of every spec-change cell is a phase 1 that LANDED,
so the selection is printed beside every n. The population is every Opus greenfield × `none` (card extras none) phase-1 cell with an
`end-1` in the three source roots (cells-matrix1 · cells-n3-topup · cells-gf-topup-1), 40 cells (`phase1-population.tsv`):
```
  task      arm        phase-1 landed / with end-1   not landed
  LZW       plain      3 / 3                          -
  LRU       plain      4 / 5                          FAILED-BOOTS=1
  FreeList  plain      4 / 4                          -
  Paxos     plain      4 / 4                          -
  Paxos     salt-diet  3 / 5                          FAILED-BOOTS=1 CAP-COST=1
  FreeList  salt-diet  3 / 6                          FAILED-BOOTS=1 CAP-COST=2
```
⇒ **On FreeList and Paxos, the salt-diet phase 1 landed 3 of 6 and 3 of 5 times, against 4 of 4 for the plain phase 1 on the same tasks.**
Every n = 3 below is drawn from those landings. FAILED-BOOTS cells are counted because they carry an end. Whether they made any model call
is not measured here.

## §3 · THE SIX CONDITIONS AT n = 3 OF RECORD (claude-opus-5 · greenfield · spec-change)
```
  condition               cells of record (suite on the post-change runner)                                full passes   reach
  FreeList × plain        188f422b 9/9 · 9cb8ce96 9/9 · clbkfp01 9/9                                        3 of 3        4 / 4
  FreeList × salt-diet    f33c7e65 LANDED 8/9 · clbkfs01 9/9 · clbkfs02 9/9                                 2 of 3        3 / 6
  LRU × plain             3bdcbcbd 23/23 · 69e8c2c4 23/23 · clbklp01 23/23                                  3 of 3        4 / 5
  LZW × plain             93323249 15/15 · 22ee7d33 15/15 (a plain-STATEMENT phase 1) · clbkzp01 15/15      3 of 3        3 / 3
  Paxos × plain           60a056e6 24/24 · f6462d47 CAP-COST 23/24 · clbkpp01 CAP-COST 24/24                2 of 3        4 / 4
  Paxos × salt-diet       9e6c8d4d CAP-COST 24/24 · b22d1000 CAP-COST (see §4) · clbkps01 LANDED TIMEOUT    1 or 2 of 3   3 / 5
```
Older cells as published: `RESULT-p1-specchange-2026-09-10.tsv` rows for 188f422b · 9cb8ce96 · f33c7e65 · 3bdcbcbd · 69e8c2c4 ·
60a056e6 · f6462d47 · 9e6c8d4d · b22d1000, and `RESULT-specchange-1-2026-09-10.md:74` for 93323249 · 22ee7d33. LZW's composition (one
statement-built phase 1) is inherited and declared (freeze §G5.5).

## §4 · ⛔ `b22d1000`: TWO VERDICTS, BOTH NAMED, NEITHER EDITED HERE
```
  published   RESULT-p1-specchange-2026-09-10.md §2: CAP-COST 0/0, "does not build"
  re-score    today, B runner sha16 b154a6f7557b68c1: PASS 24/24 (rc 0), at the cell's HEAD and in its working tree
  the code    solution.rs sha256/16 121ec765779f83ae, byte-identical to the 09-10 harvest's
```
The code did not change, so the difference is the scoring run. The 09-10 runner output is not tracked, so which of rc 3's three causes
produced "0/0" is UNMEASURED. **This RESULT reports the condition both ways, 1 of 3 on the published verdict and 2 of 3 on the re-score,
and it moves nothing.** On the helm's order, a census of every rc-3 verdict of record comes before any correction addendum to the P1 result.

## §5 · PROVENANCE AND INSTRUMENT HISTORY
- Pooling: the B trees are byte-identical to the P1 wave's export, and the pooling control re-scored one P1-wave cell per task to its
  published verdict (freeze ADDENDUM 1). Client 2.1.259 on every cell, and every source's transcripts carry the same version.
- The derivation script's own defects, each found before a file was written: rc 3 read as BUILD-FAIL (§1), and a source column that pasted a
  tab-separated file and shifted every later column. Both were fixed in the script, and the tables were re-derived from the cells.
- Pool: the Claude pool the ruling names, on its run-box dir, with the account check OK and a red control RED before every cell.

## §6 · WHAT THIS RESULT DOES NOT SUPPORT
n = 3 per condition, one model, four tasks, spec-change only. **No arm comparison is licensed.** The arms differ in phase-1 reach (§2), and
every n is conditioned on a landing. There is no p-value, no pooling across tasks, and no claim about the salt method. A DONE here is
"a merged result of record at n = 3", never a verdict on the arms.

---
## ADDENDUM A (2026-09-30, bench) — §4's `b22d1000` is settled by the census; Paxos × salt-diet reads 2 of 3. The blocks above are unchanged.
`CENSUS-rc3-verdicts-2026-09-30.md` (read and merged) and `RESULT-p1-specchange-2026-09-10.md` ADDENDUM A record `b22d1000` at PASS 24/24. §3's
Paxos × salt-diet row "1 or 2 of 3" is therefore **2 of 3** (`9e6c8d4d` CAP-COST 24/24 · `b22d1000` CAP-COST 24/24 · `clbkps01` LANDED
TIMEOUT). Its reach (3 / 5) and every other row stand.
