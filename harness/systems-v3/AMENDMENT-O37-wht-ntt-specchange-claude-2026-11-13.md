# AMENDMENT — O37 BLOCK WC: WHT AND NTT × SPEC-CHANGE, CLAUDE LANE, B-CONTINUATION ON COPIES. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-11-13. The form is block NC's (`AMENDMENT-O37-blockNC-specchange-claude-2026-11-13.md`, signed, with its
## ADDENDUM 1, cited as "NC"), which is step g's B-CONTINUATION under the taskshape rule (§A3 as amended by B3). This block carries NC BY
## CITATION. Its sources are block W's cells (`AMENDMENT-O37-wht-ntt-greenfield-claude-2026-11-11.md`, cited as "block W"). A clause below
## that differs from NC says so, and says why. The authority is block N's: the Captain's council word of 2026-09-25 (P3, quota no
## higher-priority work needs) and his objective "fill out the 14 problems (greenfield only)".
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO BASELINE IS RUN BEFORE BLOCK W's RESULT OF RECORD EXISTS AND THIS FILE IS SIGNED.**
## ⛔ **NO CELL FIRES BEFORE §WC3's ITEMS ARE DRIVEN AND A RELEASE ADDENDUM NAMES THE EXPORT SHA, THE POOL AND EACH RECEIPT.**

**Why now.** NC §C1 left out WHT and NTT × spec-change because no greenfield landing of either existed. Both now have a `B/` rung with both
halves (saltbench-systems, WHT 36417e31 and NTT 7573e701, each read by a non-author), and block W, which produces their landings, is
signed with §W2 items 1–3 met (the account check and zero-cell probe wait on its pool). Registering the source rule now, before block W fires, puts the rule before every datum it selects on,
including the phase-1 landings themselves.

---

## §WC0 · THE INPUTS (NC §C0, row by row)
```
  1  MODEL IDs     claude-opus-5 · claude-sonnet-5, NC row 1 unchanged; the release re-measures both with the zero-cell probe.
  2  n             3 per condition.
  3  POPULATION    8 conditions, 24 cells (§WC1). Nothing is added, dropped or substituted.
  4  EXPORT        ⚖️ THE CHANGE FROM NC: ONE bare sha of saltbench-systems that carries the WHT and NTT trees, G and B halves, at the hashes
                   §WC3 item 1 drives, and the block-NC stager or its successor extended to this block. Block W's export (candidate
                   0916ef9a) already carries both B/ trees (WHT 17d0b93b, NTT c5cdaed5), so the release may name the same sha block W
                   fired on, or a descendant whose task trees are identical. Recorded per cell.
  5  CLIENT PIN    NC row 5. If it differs from the version that ran a source's phase 1, the pair is reported with both.
  6  TASK TREE     the EXPORT's tasks/systems-v3/<T>/B for phase 2, and <T>/G for any fresh phase 1.
  7  CAPS          NC row 7: phase 2 C2_USD $18.60 on the copy's own slug; fresh phase 1 C1_USD $37.21, W1_SEC 144,000. No cap is raised.
  8  ACCOUNT       NC row 8: P3, a pool the PM names at release, `cells_account_check.sh --expect` OK before each fire.
  9  FIRE ORDER    §WC4.
```

## §WC1 · THE POPULATION — 8 CONDITIONS, 24 CELLS
```
  problems   NTT · WHT                       the two with a v3 B/ rung (both halves, read) and a greenfield block (block W)
  models     claude-opus-5 · claude-sonnet-5
  arms       plain · salt-diet         field greenfield → spec-change         extras none
  ⇒ 2 × 2 × 2 = 8 conditions · × n 3 = 24 cells
```
**NOT in this block:** WHT and NTT × statement (no `## Statement` section exists), and the agy lane's WHT/NTT spec-change (a sibling freeze,
which would continue block WA's landings).

## §WC2 · ⛔⛔ THE SOURCES — NC §C2's RULE, AS AMENDED BY NC ADDENDUM 1, APPLIED TO BLOCK W's CELLS
Each phase 2 continues a COPY of one of block W's cells of record of the SAME problem, model and arm (block W's roots, `cells-clb-w{o,s}-
<problem>-<arm>/`). NC §C2 steps 1–6 apply unchanged, with NC ADDENDUM 1's instrument: the P1 baseline is the export's `G/run_tests.sh` on
a CLONE of the source's `landed-1`; ELIGIBLE iff it exits 0 and passed == total > 0; anything else is UNMEASURED and NOT ELIGIBLE. Every
eligible cell is used once, in ascending cell-id order; each shortfall is ONE fresh phase 1 (greenfield × none at this block's export and
C1), recorded beside block W and never in its n; a fresh cell that does not land, or whose baseline fails, is a REACH LOSS.
⚖️ **THE CHANGE FROM NC: the sources do not exist yet.** The baselines run after block W's result of record and this file's signature, and
the release addendum writes the table of 24 (cell, baseline, eligible, or the fresh cell that fills it), as NC's ADDENDUM 1 evidence did.
A block-W cell that is VOIDED and re-fired is represented by its `r<k>` replacement, as in block W's record; the void is not a source.

## §WC3 · ⛔⛔ THE BUILD ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
1. **THE TWO B/ SUITES RE-DRIVEN BY A NON-BUILDER ON THE EXPORT'S BYTES** — NC §C3 item 1's form, unchanged. The lead built both. A task whose
   drive disagrees with its B/ README and RUN file is WITHDRAWN by name and its conditions reported NOT-FIRED(TASK).
2. **THE 24 BASELINES** (§WC2), after block W's result of record and the signature, on copies, read-only on the sources, with NC ADDENDUM
   1's control (`B/run_tests.sh` on one source must exit 3 with no REGRESSIONS line).
3. **THE COPY FORM ON A DRY CELL PER MODEL** — NC §C3 item 3, on a copy of one eligible block-W source.
4. **THE STAGER** — a freeze for this block (copy blocks for phase 2, fresh blocks for the shortfalls, a source table derived from item
   2), with a selftest that fails on the stager before it, as `clb_blockNC_selftest.sh` does.
5. **THE ACCOUNT CHECK**, **NO LEAK INTO A VIEW** (the checker screens both B/ withheld trees), and **THE ZERO-CELL PROBE** (NC §C3 items 4–5).

## §WC4 · THE ORDER, THE TRIPWIRES
```
  models     interleaved as block N ADDENDUM 10's form; Opus's tripwire first.
  problems   NTT → WHT (ascending B/ reference size, 1147 · 1186 lines at 0916ef9a; the release re-reads them with its own `wc -l`)
  cells      per condition pair: plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3; a fresh phase 1 runs immediately
             before the phase 2 it feeds, in the same pool dir.
```
Tripwires, each ONE phase-2 cell, read by the lead and posted before its model continues: `T-WC-O` = Opus · NTT · salt-diet#1, `T-WC-S` =
Sonnet · NTT · salt-diet#1. The reading list is NC's.

## §WC5 · CAPS, PREDICTIONS AND THE PRICE — REGISTERED BEFORE ANY DATA
Caps as NC §C5. Predictions, per model, where a miss is a result: NC §C5 (i)–(iii), carried. ⛔ No prediction about pass rate or premium.
**The price**, from NC's medians (the same two tables of record, NC's price script):
```
  estimate      12 × $13.36 + 12 × $2.515 = 160.32 + 30.18 = $190.50 for phase 2
  ceiling       24 × $18.60 = $446.40 for phase 2, plus $37.21 per shortfall (at most 24 × 37.21 = $893.04, if no block-W cell lands),
                plus each cell's overrun past its cap
```
The shortfall count is unknown until block W lands, so the release re-prices it from the baselines. The medians come from other problems,
and their direction of error is unknown.

## §WC6 · CONFOUNDS — NC §C6 items 1–3 carried; item 4 restated
4. **ONE AUTHOR FOR BOTH TASKS AND BOTH B/ SUITES, WHO IS THE LEAD.** §WC3 item 1 is the control. NTT's reference proves less than WHT's at
   G (block W §W5 item 2); the same limit is printed beside any table that sets the two side by side.

## §WC7 · READING RULES, VOIDS, WHAT THIS BLOCK CANNOT ESTABLISH, DELIVERABLES
NC §C8, unchanged, with "§C1" read as §WC1. A result of record per model, with the census's O37 section re-cut in the same commit. Any public
sentence, and any claim about the method, is the Captain's.
