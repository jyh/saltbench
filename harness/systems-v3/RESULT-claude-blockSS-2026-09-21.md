# RESULT — block SS · `claude-sonnet-5` × greenfield × extras=statement · n=24
### bench, 2026-09-21. **8 conditions. ⛔ THE ARM-CORRELATED COST CAP REPEATS — AND HERE THE SALT-DIET ARM HAS *NO UNCAPPED FAILURE AT ALL*.**
## 📌 The per-cell table is a FILE: `evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv` (24 rows, 15 columns).
## ⛔ Every figure below is derived from that table by `RESULT-claude-blockSS-2026-09-21-verify.py`.

---
# §1 · WHAT RAN
`claude-sonnet-5` × **greenfield** × **statement** × {Crc32, FreeList, LRU, LZW} × {plain, salt-diet} × 3 reps = **8 conditions / 24 cells**, every condition at full n=3.
⛔ **PAXOS IS ABSENT BY DESIGN, NOT BY LOSS:** `Paxos × statement` is **INEXPRESSIBLE** (§C4), which is why this block is 4 problems and not 5. **An absent problem that is inexpressible is not a missing measurement**, and it is stated here so nobody reads 4 as a shortfall.
```
  run_state   ENDED: LANDED 22 · ENDED: CAP-COST 2        model  claude-sonnet-5, 24 of 24, derived per cell
  suite       PASS 22 · FAIL 1 · BUILD-FAIL 1   (of 24; see §2 — BOTH non-PASS cells are CAPPED cells)
```
⚠️ **GREENFIELD SHAPE** — no seed, so no `class`/`retained`/`surv`/`growth`. Omitted, never blank (see block SG §1).

---
# §2 · ⛔⛔ THE CAP IS ARM-CORRELATED AGAIN, AND THIS TIME IT ACCOUNTS FOR *EVERY* SALT-DIET FAILURE
```
                cells    CAPPED at $37.21      suite
  plain         12       0  of 12              PASS 12 · FAIL 0 · BUILD-FAIL 0
  salt-diet     12       2  of 12              PASS 10 · FAIL 1 · BUILD-FAIL 1
  the two non-PASS cells, named — AND BOTH ARE CAPPED CELLS:
    clbsfs02  FreeList  salt-diet  FAIL        6/7   ENDED: CAP-COST   $37.46   CAPPED
    clbszs02  LZW       salt-diet  BUILD-FAIL  0/0   ENDED: CAP-COST   $37.31   CAPPED
```
⇒ 🔑 ***EVERY NON-PASS IN THIS BLOCK IS A CELL THAT HIT THE BUDGET. THERE IS NO UNCAPPED SALT-DIET FAILURE AND THERE IS NO PLAIN FAILURE OF ANY KIND.*** So the apparent correctness gap (12/12 against 10/12) **coincides exactly with the censoring**, and this block cannot separate *"the treatment produced worse code"* from *"the treatment ran out of money."*
⭐ **THE DIRECTION IS KNOWN, SO THIS IS A BOUND AND NOT A DOUBT:** the cap can only ever remove salt-diet work. ⇒ **salt-diet's 10/12 is a FLOOR and its costs are LOWER BOUNDS.**
⚠️ **`clbszs02`'s `0/0` IS THE SIGNATURE OF A SUITE THAT NEVER RAN**, not of one that ran and failed — the same read as block SG's `clbgfs02`. **It is in no correctness denominator.** `clbsfs02` did run its suite (6 of 7) and is counted.
⇒ **This is block SG's §2 finding repeating under a DIFFERENT TREATMENT** (`statement` rather than `none`), at the same model and field. **Two blocks, same direction, and the cap is the common cause rather than the treatment.**

---
# §3 · COST — BOUNDED, AND SMALLER THAN block SG's ON THE SAME FIELD AND MODEL
```
                median COST   total COST   total T          capped
  plain         $1.67         $21.64        38,901,865      0 of 12
  salt-diet     $8.88         $188.29      618,901,195      2 of 12
  ratio         5.32x         8.70x         15.91x           <- ALL THREE ARE LOWER BOUNDS
```
⭐ **THE COMPARISON WORTH RECORDING, AND IT IS AN OBSERVATION RATHER THAN AN EXPLANATION:** on block SG — the **same model, same field**, treatment `none` — the median ratio is **8.27×**; here under `statement` it is **5.32×**. **Exactly ONE thing differs between those two blocks (the treatment), which is the cleanest contrast this campaign has so far** — ⚠️ **and both figures are lower bounds censored by an arm-correlated cap, so the DIFFERENCE between them is not itself bounded in a known direction.** It is a pair of readings to be re-taken when the cap is not binding, not a result about the statement treatment.

---
# §4 · ⛔ WHAT THIS DOES **NOT** SAY
1. **It cannot separate a correctness effect from the cap.** §2 is the whole reason, and it is this block's headline.
2. **Nothing here reaches Opus, brownfield, or the spec-change treatment.**
3. **`clbszs02` is in no correctness denominator**; the block's 22/24 is over 23 scorable cells.
4. **Paxos is inexpressible under `statement`** and is not a missing measurement.
5. **No cell was re-run.** Every number re-reads artifacts that existed before this shift.
6. **These are `plain` vs `salt-diet` arms**, not a claim about the salt METHOD.

---
# §5 · PROVENANCE
```
  cells      24, staged at ~/bench-dry/clb-score/ and scored as they landed
  scored by  score_claude_v3.py from 283362105d75's harness, --declared (never a glob), --toolchain-env
  retention  NOT RUN, and not applicable: greenfield has no seed
  meter      each cell's own ctl/post-end-1.tsv        model  model_served_v3.py, 24 of 24 claude-sonnet-5
  table      evidence/claude-lane-blocks-2026-09-21/blockSS-cells.tsv
  verifier   RESULT-claude-blockSS-2026-09-21-verify.py — re-derives every figure FROM the table and
             asserts it against the BYTES of this document. No typed expectations.
```
