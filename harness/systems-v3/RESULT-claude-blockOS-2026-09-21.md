# RESULT — block OS · `claude-opus-5` × brownfield × extras=statement · n=22
### bench, 2026-09-21. **7 conditions DONE, 1 held at n=1. ⭐ AND IT IS THE ONLY BLOCK WITH *NO CAP BINDING ANYWHERE*, WHICH MAKES ITS COST RATIO A MEASUREMENT RATHER THAN A BOUND.**
## 📌 The per-cell table is a FILE: `evidence/claude-lane-blocks-2026-09-21/blockOS-cells.tsv` (22 rows, 25 columns).
## ⛔ Every figure below is derived from that table by `RESULT-claude-blockOS-2026-09-21-verify.py`.

---
# §1 · WHAT RAN, AND THE ONE CONDITION THAT IS **NOT** COMPLETE
`claude-opus-5` × **brownfield** × **statement** × {Crc32, FreeList, LRU, LZW} × {plain, salt-diet}. ⛔ **Paxos × statement is INEXPRESSIBLE (§C4).**
```
  run_state   ENDED: LANDED 22 · ENDED: CAP-COST 0 — nothing capped, truncated or refused
  suite       PASS 22 of 22          w1_fenced  COVERED 22 of 22
  model       claude-opus-5, 22 of 22, derived per cell from its own served-*.out
```
⛔⛔ **`Crc32 × plain` STANDS AT n=1 AND IS **NOT** CLAIMED DONE.** Its reps 02 and 03 (`clbtcp02`, `clbtcp03`) are **FLAGGED**, blocked on a lane pool credential that was blanked in place at `2026-09-21T01:17:19Z`. **Seven conditions here are complete at n=3; the eighth is one cell and stays `OWED`.**
⇒ **This is the SAME single condition named as class (b) in the 2026-09-21 partition of the 75** — *"blocked on the blanked credential: 1 condition, 2 cells"* — and it arrives here as the same fact from the other side. ⚠️ **It is held rather than reported at n=1, because a condition resting on one cell is not a weaker measurement, it is a different one.**

---
# §2 · ⭐ THE ONLY UNCENSORED ARM COMPARISON IN THE FIVE BLOCKS
**ZERO cells capped, in either arm.** Blocks SG (5), SS (2) and SBS (3) all had the `$37.21` COST cap binding on salt-diet and never on plain, so every cost figure in them is a lower bound. **Here nothing is censored.**
```
                median COST   total COST   total T          capped   suite
  plain         $12.08        $136.81      135,274,575      0 of 10   10 of 10 PASS
  salt-diet     $14.80        $213.46      250,019,763      0 of 12   12 of 12 PASS
  ratio         1.23x         1.56x         1.85x
```
⇒ 🔑 ***WHERE NOTHING IS CENSORED, THE MEDIAN COST RATIO IS 1.23× — AGAINST 8.27× (SG), 5.32× (SS) AND 4.71× (SBS), EVERY ONE OF WHICH IS A LOWER BOUND TAKEN WHILE A CAP WAS CUTTING THE SALT-DIET ARM.***
⚠️ **AND THIS BLOCK CANNOT EXPLAIN THAT GAP, BECAUSE MORE THAN ONE THING DIFFERS.** OS is Opus where SG/SS/SBS are Sonnet, and its cells simply **cost more in both arms** (plain median $12.08 against SBS's $1.54), so the cap was never reached by either. **Whether the low ratio is an Opus property, a consequence of an uncensored measurement, or both, is not decidable from these blocks** — it is the question they raise, not one they answer.

---
# §3 · RETENTION — THE SHAPE REPEATS A FOURTH TIME, AND HERE `retained` SEPARATES BY A HAIR
```
                      retained               surv (OVERLAPPING)     growth (DISJOINT)    end_lines
  plain      n=10     0.186 .. 0.583         0.300 .. 0.951         1.66x ..  3.46x      115 ..  664
  salt-diet  n=12     0.054 .. 0.182         0.360 .. 0.873         5.68x .. 13.85x      284 .. 2,659
```
⇒ **`retained` is disjoint by 0.004** (plain's floor 0.186 against salt-diet's ceiling 0.182) — **the narrowest separation in any of the four brownfield blocks**, while `growth` is disjoint by a wide margin and `surv` overlaps heavily.
⇒ 🔑 ***A SEPARATOR THAT HOLDS BY FOUR THOUSANDTHS IS ONE SAMPLE FROM NOT HOLDING, AND `growth` — WHICH IS WHAT IT IS ACTUALLY READING — IS NOWHERE NEAR ITS BOUNDARY.*** ⇒ **Do not build a threshold on `retained`.** This is the fourth block (with SB, O, SBS) in which the primary separator tracks growth rather than survival.
⛔ **`class` FOLLOWS `retained`:** salt-diet is 12/12 `REPLACED`; **plain carries one `REPLACED` too** (REPAIRED 9 · REPLACED 1) — the first plain cell in any of these blocks to be classed that way, and it sits next to the 0.004 margin above.

---
# §4 · ⛔ WHAT THIS DOES **NOT** SAY
1. **It does not explain §2's ratio gap.** Model and cost scale differ together; see §2's own limit.
2. **`Crc32 × plain` is NOT a result.** n=1, held, and named in §1.
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
