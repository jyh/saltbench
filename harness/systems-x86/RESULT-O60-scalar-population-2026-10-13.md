# RESULT — O60, THE x86 LANE's FIRST POPULATION: 20 SCALAR PRIMITIVES × {plain, salt-diet}, n = 1, claude-opus-5. THE 40 CELLS, SCORED
## bench (SaltBench lead), 2026-10-13. Registered in `REGISTRATION-O60-scalar-population-2026-10-01.md` (§Z0–§Z10, signed; ADDENDA 1–16 and its
## corrections). Every number below is read from `evidence/o60-batch-score-2026-10-13/`, never typed: the harvest table (`HARVEST.tsv`), the
## rates (`primary.log`), each cell's referee record facts (`referee-facts.tsv`) and each cell's last meter line (`meter-last.txt`).

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
- **(ii) every salt-diet cell reaching TARGET reads the three standard axioms, or is refused at AXIOMS — HOLDS:** the 7 salt-diet cells whose
  TARGET passed read exactly {propext, Classical.choice, Quot.sound}. No cell was refused at AXIOMS.
- **(iii) no plain cell reads a `cell_translation` line — HOLDS:** 0 of 20 plain records carry a target block.
- **(iv) every salt-diet cell reaching TARGET reports a spec_strength — HOLDS IN FORM, NOT IN VALUE:** every record carries the field, but a
  MEASURED value exists for 2 of the 7 (Adler32 agree 92 of 92 · BignumSub 156 of 156). The other 5, and 9 more salt-diet cells, read
  `frame_spec.py: REFUSE: the descriptor has no spec directive`. **That is a gap in the TASK DESCRIPTORS (18 of 20 lack the directive), not a
  property of the subjects,** and it is declared here as a limit on every salt-diet PASS: kernel-checked against the cell's OWN spec, whose
  strength was NOT measured for 5 of the 7.

## §R4 · VALIDITY ROWS (the helm's 17:56 CONCUR of 10-10, kent's line)
- **SETTING-EDITED:** 440 events over the 40 cells, each with one quarantine (counts equal per cell). **0 of the 5,268 quarantined files is
  non-empty**: every quarantine is the client's empty scaffold, and one (`clbps10`, quarantine 3) is an empty directory. The same command
  counts all 5,268 files, so the zero is a reading.
- **`.claude/` in a JUDGED tree: 0 of 40** (searched over every materialised judged tree). Positive control: a planted `.claude/settings.json`
  in a scratch tree is found by the same command.
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
- **The cells ended over four days, 2026-10-09 → 10-13 (5 · 19 · 12 · 4 cells; `chain-ended.tsv`, the chain's own end record), in four chains** that held on pool day lines
  between them (a 10-13 start first REFUSED, firing nothing, because the run box's tmux session had died, and was re-fired). The cells were
  fired one at a time, so no two shared a window.
- The referee's declared limits ride with every verdict above (`table.log`'s LIMITS block, printed by `classify_cell.py --limits`).
