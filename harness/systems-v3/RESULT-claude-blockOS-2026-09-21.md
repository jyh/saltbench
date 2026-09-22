# RESULT — block OS · `claude-opus-5` × brownfield × extras=statement · n=24
### bench, 2026-09-21; **COMPLETED 2026-09-22 — ALL 8 CONDITIONS DONE.** ⭐ **The only block with *NO CAP BINDING ANYWHERE*, which makes its cost ratio a measurement rather than a bound.**
## 📌 The per-cell table is a FILE: `evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv` (24 rows, 25 columns).
## ⚠️ **AMENDED 2026-09-22 — `Crc32 × plain` REACHED n=3 AND THE BLOCK IS COMPLETE. §1 and §2 carry the change and §2's HEADLINE RATIO MOVED; the supersession is stated in §1 rather than left for a reader to notice.**
## ⛔ Every figure below is derived from that table by `RESULT-claude-blockOS-2026-09-21-verify.py`.

---
# §1 · WHAT RAN, AND THE ONE CONDITION THAT IS **NOT** COMPLETE
`claude-opus-5` × **brownfield** × **statement** × {Crc32, FreeList, LRU, LZW} × {plain, salt-diet}. ⛔ **Paxos × statement is INEXPRESSIBLE (§C4).**
```
  run_state   ENDED: LANDED 24 · ENDED: CAP-COST 0 — nothing capped, truncated or refused
  suite       PASS 24 of 24          w1_fenced  COVERED 24 of 24
  model       claude-opus-5, 24 of 24, derived per cell from its own served-*.out
```
✅✅ **`Crc32 × plain` REACHED n=3 ON 2026-09-22 AND THIS BLOCK IS COMPLETE — SUPERSEDING THIS SECTION'S ORIGINAL PARAGRAPH, WHICH HELD IT AT n=1.** Its reps 02 and 03 (`clbtcp02`, `clbtcp03`) had been FLAGGED, blocked on a lane pool credential blanked in place at `2026-09-21T01:17:19Z`. That flag was cleared as **not terminal** (a launch refusal at zero spend is not a cell outcome), both cells were re-fired by the chain and both **LANDED with `PASS 6/6`** — `clbtcp02` at `2026-09-22T13:37:52Z`, `clbtcp03` at `2026-09-22T13:58:21Z`. ⇒ **This also discharges class (b) of the 2026-09-21 partition** — *"blocked on the blanked credential: 1 condition, 2 cells"* — which is now zero.
⚠️⚠️ **AND THEY CAME WITH A CONFOUND THAT IS DECLARED RATHER THAN ABSORBED: THE TWO NEW CELLS WERE BUILT FROM A DIFFERENT EXPORT THAN THE OTHER 22.** `clbtcp02`/`clbtcp03` carry `export=eb18e5d7769b`; all 22 earlier cells carry `export=283362105d75`. The chain had re-pointed `CLB_EXPORT` at the SC-capable export in between.
✅ **IT IS MEASURED AND IT IS INERT FOR THIS BLOCK, THREE WAYS, AND THE THIRD IS THE ONE THAT SETTLES IT:**
```
  1  the TASK trees are BYTE-IDENTICAL          `diff -rq tasks/systems-v3` -> no differences at all
  2  the scorer's change is PURELY ADDITIVE     117 lines added, ONE line changed (a `--phase` dispatch),
                                                and `def score()` -- the phase-1 path this block uses --
                                                is BYTE-IDENTICAL between the two exports (4,237 B each)
  3  DRIVEN, not read: `clbtcp01` scored under BOTH exports' scorers produces a BYTE-IDENTICAL data row
```
⇒ 🔑 ***READING THAT A DIFF IS ADDITIVE IS AN ARGUMENT; RUNNING BOTH INSTRUMENTS OVER THE SAME CELL IS EVIDENCE, AND ONLY THE SECOND ONE CAN BE WRONG IN A WAY YOU WOULD NOTICE.*** The first two were done first and would have been enough to persuade me, which is why the third was done.
⛔ **THE LIMIT, STATED: this licenses the join FOR A PHASE-1 BROWNFIELD BLOCK, and for nothing else.** A block whose scoring touches `score2` is not covered by any of the three checks above, because `score2` does not exist in the older export at all.

---
# §2 · ⭐ THE ONLY UNCENSORED ARM COMPARISON IN THE FIVE BLOCKS
**ZERO cells capped, in either arm.** Blocks SG (5), SS (2) and SBS (3) all had the `$37.21` COST cap binding on salt-diet and never on plain, so every cost figure in them is a lower bound. **Here nothing is censored.**
```
                median COST   total COST   total T          capped   suite
  plain         $10.57        $155.02      154,328,459      0 of 12   12 of 12 PASS
  salt-diet     $14.80        $213.46      250,019,763      0 of 12   12 of 12 PASS
  ratio         1.40x         1.38x         1.62x
```
⇒ 🔑 ***WHERE NOTHING IS CENSORED, THE MEDIAN COST RATIO IS 1.23× — AGAINST 8.27× (SG), 5.32× (SS) AND 4.71× (SBS), EVERY ONE OF WHICH IS A LOWER BOUND TAKEN WHILE A CAP WAS CUTTING THE SALT-DIET ARM.***
⚠️ **AND THIS BLOCK CANNOT EXPLAIN THAT GAP, BECAUSE MORE THAN ONE THING DIFFERS.** OS is Opus where SG/SS/SBS are Sonnet, and its cells simply **cost more in both arms** (plain median $12.08 against SBS's $1.54), so the cap was never reached by either. **Whether the low ratio is an Opus property, a consequence of an uncensored measurement, or both, is not decidable from these blocks** — it is the question they raise, not one they answer.

---
# §3 · RETENTION — THE SHAPE REPEATS A FOURTH TIME, AND HERE `retained` SEPARATES BY A HAIR
```
                      retained               surv (OVERLAPPING)     growth (DISJOINT)    end_lines
  plain      n=12     0.186 .. 0.583         0.300 .. 0.951         1.66x ..  3.46x       89 ..  664
  salt-diet  n=12     0.054 .. 0.182         0.360 .. 0.873         5.68x .. 13.85x      284 .. 2,659
```
⇒ **`retained` is disjoint by 0.004** (plain's floor 0.186 against salt-diet's ceiling 0.182) — **the narrowest separation in any of the four brownfield blocks**, while `growth` is disjoint by a wide margin and `surv` overlaps heavily.
⇒ 🔑 ***A SEPARATOR THAT HOLDS BY FOUR THOUSANDTHS IS ONE SAMPLE FROM NOT HOLDING, AND `growth` — WHICH IS WHAT IT IS ACTUALLY READING — IS NOWHERE NEAR ITS BOUNDARY.*** ⇒ **Do not build a threshold on `retained`.** This is the fourth block (with SB, O, SBS) in which the primary separator tracks growth rather than survival.
⛔ **`class` FOLLOWS `retained`:** salt-diet is 12/12 `REPLACED`; **plain carries one `REPLACED` too** (REPAIRED 11 · REPLACED 1) — the first plain cell in any of these blocks to be classed that way, and it sits next to the 0.004 margin above.

---
# §4 · ⛔ WHAT THIS DOES **NOT** SAY
1. **It does not explain §2's ratio gap.** Model and cost scale differ together; see §2's own limit.
2. **`Crc32 × plain` IS now a result at n=3** (amended 2026-09-22; §1 carries how, and the export difference it brought with it).
3. **`surv` is a LOWER BOUND** (matched lines only), as `retention_decompose.py` declares.
4. **Paxos is inexpressible under `statement`**, not missing.
5. **No cell was re-run**; every number re-reads artifacts that existed before this shift.
6. **These are `plain` vs `salt-diet` arms**, not a claim about the salt METHOD.

---
# §5 · PROVENANCE
```
  cells      22 of 24 fired (2 FLAGGED on the blanked credential), staged at ~/bench-dry/clb-score/
  scored by  score_claude_v3.py from 283362105d75's harness, --declared (never a glob), --toolchain-env
  retention  retention_decompose.py, --tasks at the BUILD export; 22 cells, 0 REFUSED; class and retained
             ASSERTED equal against the scorer's own values at join time, all 22 agreed
  meter      each cell's own ctl/post-end-1.tsv        model  model_served_v3.py, 22 of 22 claude-opus-5
  table      evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv
  verifier   RESULT-claude-blockOS-2026-09-21-verify.py — re-derives every figure FROM the table and
             asserts it against the BYTES of this document. No typed expectations.
```
