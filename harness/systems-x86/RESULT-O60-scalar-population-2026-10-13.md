# RESULT — O60, THE x86 LANE's FIRST POPULATION: 20 SCALAR PRIMITIVES × {plain, salt-diet}, n = 1, claude-opus-5. THE 40 CELLS, SCORED
## bench (SaltBench lead), 2026-10-13. Registered in `REGISTRATION-O60-scalar-population-2026-10-01.md` (§Z0–§Z10, signed; ADDENDA 1–16 and its
## corrections). Every number below is read from `evidence/o60-batch-score-2026-10-13/`, never typed: the harvest table (`HARVEST.tsv`), the
## rates (`primary.log`), each cell's referee record facts (`referee-facts.tsv`), each cell's last meter line (`meter-last.txt`) and the two
## §R4 censuses re-run over the run box's archive (`r4-*`). The one statement that is NOT in that directory is marked in place (§R6).

⛔ **A descriptive result, n = 1 per task, one model. No effect size, no premium, no p-value (§Z9).** Tasks are not exchangeable (§Z6.1), so
the per-task table comes first and the pooled rates sit beside it, never instead of it.

## §R0 · HOW IT WAS SCORED
`harvest_o60.py` (export `34a65d3f2a57`), run on the run box after the 40th cell ended (no cell live), task pair by task pair: fetch → the
task's reference CONTROL refereed first (it must read ACCEPTED, or the harvest stops) → each cell's JUDGED COMMIT, pinned by the harness
(`landing-N` from the end line for a landing, the watcher's `s<phase>` snapshot otherwise) → `referee_o60.sh` → `classify_cell.py`. All 20
controls read ACCEPTED (`score.log`, the CONTROL line before each pair). Scoring ran 2026-10-14 00:02–02:06 UTC. `table` over the 40-cell manifest rc 0. Then the score dir,
which carries the withheld tests, was deleted. The run box's withheld census reads 0 (the same command counted 1,063 in the score dir before
the delete).

## §R1 · PER TASK (the end the cell declared is in brackets)
| task | plain | salt-diet |
|---|---|---|
| Adler32 | ACCEPTED (LANDED) | ACCEPTED (LANDED) |
| BignumModN256Alt | ACCEPTED (LANDED) | HALTED (CAP-COST) |
| BignumModadd | ACCEPTED (LANDED) | ACCEPTED (CAP-COST) |
| BignumMul | ACCEPTED (LANDED) | HALTED (CAP-COST) |
| BignumMul4x8Alt | ACCEPTED (LANDED) | HALTED (CAP-COST) |
| BignumMulP25519Alt | ACCEPTED (LANDED) | HALTED (CAP-COST) |
| BignumSub | ACCEPTED (LANDED) | ACCEPTED (LANDED) |
| Blake2bUpdateMulti | ACCEPTED (LANDED) | REJECTED (LANDED) |
| Blake2sUpdateMulti | ACCEPTED (LANDED) | HALTED (CAP-COST) |
| Cswap2Vale | ACCEPTED (LANDED) | ACCEPTED (LANDED) |
| FsubVale | ACCEPTED (LANDED) | ACCEPTED (LANDED) |
| HalfSipHash | ACCEPTED (LANDED) | HALTED (CAP-COST) |
| Lookup3 | ACCEPTED (LANDED) | HALTED (CAP-COST) |
| Murmur3X64_128 | ACCEPTED (LANDED) | REJECTED (LANDED) |
| Murmur3X86_32 | ACCEPTED (LANDED) | HALTED (CAP-COST) |
| Poly1305Vale | ACCEPTED (LANDED) | HALTED (CAP-COST) |
| SipHash24 | ACCEPTED (LANDED) | HALTED (CAP-COST) |
| WordBytereverse | ACCEPTED (LANDED) | ACCEPTED (LANDED) |
| WordClz | ACCEPTED (LANDED) | ACCEPTED (LANDED) |
| Xxh64 | ACCEPTED (LANDED) | HALTED (CAP-COST) |

## §R2 · POOLED, BESIDE THE TABLE (`primary.log`'s POOLED lines)
```
  plain      (i) landed cells accepted 20/20 · (ii) all cells accepted 20/20
  salt-diet  (i) landed cells accepted  6/8, plus 1 accepted from a CAP-COST snapshot (BignumModadd) · (ii) all cells accepted 7/20
```
**Two salt-diet cells CLAIMED a landing the withheld suite REJECTS** (Blake2bUpdateMulti, Murmur3X64_128; both "TARGET probe_rc=1 with no
positioned diagnostic"). That is why a landing is never quoted as a rate here (CLAUDE.md: a self-graded landing is an upper bound).

## §R3 · THE PREDICTIONS OF §Z5, EACH AGAINST THE RECORD
- **(i) salt-diet's CAP-COST incidence ≥ plain's — HOLDS:** 12 of 20 salt-diet cells ended CAP-COST, 0 of 20 plain. "Censoring of salt-diet on
  the largest tasks (8, 9)": task 8 (Blake2sUpdateMulti) was censored; **task 9 (Blake2bUpdateMulti) was NOT**: it landed under the cap and was
  REJECTED. So the prediction holds for 8 and not for 9. Censored cells are floors and are never raised.
- **"Reaching TARGET", defined, because the record and the prose can mean two things:** the referee record's own `target_reached` is True for
  **19** salt-diet cells (`referee-facts.tsv`): 7 whose TARGET PASSED, 9 that failed AT TARGET (no axiom set read), 2 SCREEN, 1 COMPILE.
  (ii) and (iv) below are scored on both readings.
- **(ii) every salt-diet cell reaching TARGET reads the three standard axioms, or is refused at AXIOMS — HOLDS FOR THE 7 WHOSE TARGET PASSED;
  NEITHER SHOWN NOR REFUTED FOR THE OTHER 12 OF THE 19:** the 7 read exactly {propext, Classical.choice, Quot.sound}. For the other 12 no
  axiom set exists and none was refused at AXIOMS, because the referee never reached that stage. No cell was refused at AXIOMS.
- **(iii) no plain cell reads a `cell_translation` line — HOLDS:** 0 of 20 plain records carry a target block.
- **(iv) every salt-diet cell reaching TARGET reports a spec_strength — HOLDS IN FORM, NOT IN VALUE, on either reading:** all 19 records with
  `target_reached` carry the field, but a MEASURED value exists for 2 of them, both among the 7 whose TARGET passed (Adler32 agree 92 of 92 ·
  BignumSub 156 of 156). The other 5 of the 7, and the 9 that failed at TARGET, read `frame_spec.py: REFUSE: the descriptor has no spec
  directive`; the 3 SCREEN/COMPILE cells read "the spec was not evaluated". **That is a gap in the TASK DESCRIPTORS (18 of 20 lack the directive), not a
  property of the subjects,** and it is declared here as a limit on every salt-diet PASS: kernel-checked against the cell's OWN spec, whose
  strength was NOT measured for 5 of the 7.

## §R4 · VALIDITY ROWS (the helm's 17:56 CONCUR of 10-10, kent's line)
- **SETTING-EDITED (`r4-quarantine-census.tsv`, by `r4_quarantine_census.py`):** 440 events over the 40 cells, each with one quarantine
  (counts equal per cell). **0 of the 5,268 quarantined files is non-empty**: every quarantine is the client's empty scaffold, and one
  quarantine of `clbps10` is an empty directory. The same command counts all 5,268 files, so the zero is a reading; positive control: one
  planted non-empty file in a copied quarantine reads `nonempty_files 1`.
- **`.claude/` in a JUDGED tree: 0 of 40 (`r4-judged-claude-census.tsv`, by `r4_judged_claude_census.sh`)**: each cell's repo at the harness's
  own judged pin (`HARVEST.tsv`'s `tree` column), all 40 pins resolved. Positive control: a scratch repo with a committed
  `.claude/settings.json` reads 1 through the same script.
- *Both censuses were first run on the run box before the score dir was deleted, and their output was not kept. They were RE-RUN on
  2026-10-13 over the run box's archive (the VM's cell roots, taken before its deletion, sha256 equal at both ends), read-only, and
  reproduce the first reading exactly.*
- **One observation, not a class:** `clbps03` (Murmur3X86_32, salt-diet, HALTED) reads `cell_translation: differs`, with `Submission.correct
  absent from the environment`. It is the only cell whose translation differs from the referee's. Its class is HALTED by the cap, so no verdict
  rests on it.

## §R5 · SPEND (`meter-last.txt`: each cell's last METER line)
```
  plain      20 cells · T   179,552,290 · $190.07
  salt-diet  20 cells · T   777,757,866 · $644.88        total $834.95   (§Z7: CENTRAL $808.94 · CEILING $1,520.86)
```
Dollars are the meter's list-price model on a subscription, not invoices. A cell's last METER line can trail its final record by one interval
(the IN-FLIGHT estimate is not added), so each figure is a floor by at most one interval. The CAP-COST cells' cell-cumulative cost is in their
end lines (`chain-ended.tsv`).

## §R6 · CONFOUNDS AND LIMITS — §Z6 and §Z9 carried whole, plus
- **The run moved to a native x86_64 host** (ADDENDUM 15: five Rosetta cells VOID), so §Z6.5's "Rosetta, not an x86 CPU" no longer holds:
  executor (a) is the host's CPU.
- **The cells ended over four days, 2026-10-09 → 10-13 (5 · 19 · 12 · 4 cells; `chain-ended.tsv`, the chain's own end record).** *Bench's
  reading, NOT in the record directory:* they ran in four chains that held on pool day lines between them, and a 10-13 start first REFUSED,
  firing nothing, because the run box's tmux session had died, and was re-fired. The cells were fired one at a time, so no two shared a
  window.
- The referee's declared limits ride with every verdict above (`table.log`'s LIMITS block, printed by `classify_cell.py --limits`).

---

## ADDENDUM 1 · 2026-10-16 · §R3 (iv) MEASURED IN VALUE: the spec-strength metric over the 16 salt-diet cells whose spec could be evaluated
*bench (SaltBench lead), on the helm's order of 2026-10-16 (O60 Step A, the campaign's own WRONG-IF; no model call, no cell re-run). Appended, never
an edit: every line above stands as the 10-13 record. Every number below is read from `evidence/o60-spec-rescore-2026-10-16/`, never typed.*

**WHAT CHANGED, AND WHERE.** Two things in the private harness tree, at bench's commit `698612e` (on systems' Step A drive, `d525400`, whose parent
is the scoring export `34a65d3f2a57`):
- the 18 population descriptors that lacked a `spec` directive now carry one, each read from the task's own harness-owned interface (its
  `SpecShape` gives the argument types, its `Input` the order) and the descriptor's result order. The cell builder drops that line from every
  cell's view, so no cell, past or future, sees it.
- the metric's Lean generator carried a `dec` field only as a `Nat`, so a card whose parameter is a fixed-width word (Cswap2Vale's `bit`,
  HalfSipHash's and SipHash24's `outlen`) could not be evaluated at all: its metric would have read UNAVAILABLE by a type error, not by
  anything the cell wrote. It now carries the value to the parameter's own type.

**THE CHECKS, each with its file.**
- *The directives match the cards' signatures:* a stub spec of exactly each task's `SpecShape` is evaluated through each directive.
  Before the generator fix 16 of 20 are available and 3 fail on the type error named above (`shape-RED-frame_spec-at-d525400.txt`); after it,
  19 of 20 (`shape-at-698612e.txt`). The 20th, Poly1305Vale, is refused by design: its expected lines are per-input (`expect`), which this
  metric does not render, so it reads UNAVAILABLE and never 0. This check cannot see two arguments of ONE type given in the wrong order;
  the agreements below can.
- *The fix moves no earlier reading:* systems' weak-spec drive reproduces its own numbers exactly (Adler32 88·83·37/92 · BignumSub
  132·143·142/156 · Crc32 0·2·0/82, separated 3/3; `drive-weakspec-at-698612e.txt`), and its mutant still goes red (separated 0/3, STOP-A fires;
  `drive-weakspec-mutant-at-698612e.txt`).
- *Each comparison can fail:* beside every row below, a spec of the card's type that answers `default` everywhere reads below of/of on that
  task (0 to 25 agreements; the rows' own files). A row whose control could not fail would make the tool exit 1. None did.

**THE 7 ACCEPTED salt-diet landings (`rescore-7-accepted.txt`): 7 of 7 read of/of.**
```
  Adler32 92/92 · BignumModadd 99/99 · BignumSub 156/156 · Cswap2Vale 34/34 · FsubVale 171/171 · WordBytereverse 108/108 · WordClz 200/200
```
Adler32 and BignumSub reproduce the two values the 10-13 record measured, which is the check that this path is the referee's.
⛔ **This half was expected and is a consistency reading, not a finding about the subjects.** Under today's target shape (a total function,
the exact result register and output regions, the precondition fixed by the harness), an ACCEPTED cell has a kernel-checked proof that the
routine computes its spec, and the routine passed the withheld tests. So its spec MUST agree on every withheld input that meets the
precondition. What the 7 rows add is that the measured values agree with that derivation.

**THE 9 cells that failed AT TARGET (`rescore-9-failed-at-target.txt`), separable from the commissioned 7 and declared as bench's addition:
9 of 9 read of/of.**
```
  Xxh64 146/146 · Murmur3X86_32 312/312 · Murmur3X64_128 333/333 · Lookup3 316/316 · HalfSipHash 176/176 · Blake2bUpdateMulti 48/48 ·
  BignumModN256Alt 57/57 · BignumMul4x8Alt 82/82 · BignumMulP25519Alt 79/79
```
These are the cells for which the metric is NOT forced: no proof bound the spec to the routine. Two of them are the landings the withheld suite
REJECTED (Murmur3X64_128, Blake2bUpdateMulti). In those two cells the **routine** was wrong, and the **spec** agrees with the reference on every
withheld input. In all 9, the salt-diet subject wrote a spec that matches the card on every withheld input,
and the cell failed in the routine or the proof.

**§R3 (iv), RE-READ.** On the 7-cell reading, it now HOLDS IN VALUE: 7 of 7 report a measured spec_strength, each of/of. On the 19-cell reading,
16 of 19 do. The other 3 are the SCREEN and COMPILE cells (Blake2sUpdateMulti, Poly1305Vale, SipHash24), which the referee never evaluated
and which are not re-scored here. Poly1305Vale's metric would read UNAVAILABLE in any case (`expect`).

**THE CAMPAIGN'S WRONG-IF does not fire.** No row needed a cell re-run: every judged `Submission/Spec.lean` imports nothing, which the tool
checks and refuses otherwise. Each one was evaluated from the text the referee judged, recorded by git blob and sha256 in `spec-lean-blobs.tsv`.

**LIMITS, which ride with every row above.**
- A finite hidden-input comparison. A spec that agrees on every withheld input reads of/of whether or not it is the card's function.
- The spec is evaluated INLINE from Spec.lean's text, not imported from the cell's built modules. This is the one part of the referee's path not
  exercised, and the same one systems' drive declares.
- The text evaluated is the referee's own copy of each judged tree, kept with the 10-13 scoring outputs. It was not re-derived from the cell
  repositories this time.
- Two of the 18 directives are exercised by no cell above: BignumMul's (its x and y are commutative) and SipHash24's (identical to HalfSipHash's,
  which the 176/176 row confirms). Each is checked only by the stub-shape check.
- n = 1 per task, one model. A spec agreeing with the card says nothing about the method's effect (§Z9 stands whole).
- **What this result does NOT say:** that a salt-diet spec cannot be weak. Under a target shape that leaves the result relational (a form
  under consideration, not registered), a proven spec need not pin every output, and this metric is the instrument that would see it.
