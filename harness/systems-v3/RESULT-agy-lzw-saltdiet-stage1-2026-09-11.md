# RESULT — STAGE ❶: LZW, BARE SALT-DIET on Antigravity, scored against the withheld suite
**bench · 2026-09-11 · the bare treatment control for the whole Gemini pilot, written to `main` on the Captain's council ruling of this date: *"commit results to main"*, including this stage**

⛔ **Every verdict below was RE-DERIVED TODAY at the object**, not carried from the bus posts that
first announced it. The suite was driven by `tasks/systems-v3/LZW/G/run_tests.sh` (sha256/16
`7c6d2cea42891fab`) — the runner the referee uses — against a **COPY** of each `solution.rs` taken
from the read-only preservation copy `~/PRESERVED-stage1-2026-09-11T0540Z` on the run box; the source
sha was compared before and after each run and **no cell was mutated**. Token, turn and wall figures
come from each cell's own `ctl/agy-meter-1.json` and `ctl/agy-turnloop-1.json`; truncation counts from
each cell's own `ctl/agy-stderr-1.txt`. Scoring receipts: `~/stage1-score-20260911T162211Z/`.

## §1 · ⭐⭐ THE VERDICT
```
  3 cells · LZW · BARE salt-diet (no statement arm) · agy client · declared gemini-3.1-pro-high

  cell      landed-1    TESTS   T            cmds   wall_s   continue   truncations
  s1sd01    983c9c7d     8/8      8,197,996    70     882.6      3           2
  s1td01    fb76c89a     8/8     19,942,917   144    1944.8      7           4
  s1td02    db0f5fb0     8/8     10,419,576    41    1179.7      4           3
  ---- 3 of 3 LANDED · 3 of 3 FULL PASS · P-DELIVERY, P-PERSIST, P-ANYWHERE, P-SANDBOX yes in all ----
```
⇒ **The 13,326-byte salt-diet method file is delivered to Antigravity through `AGENTS.md`, is still
present at the end of every cell, and every cell produces code that passes the complete withheld
suite.** The briefing receipt token is derived per cell (`ARMRECV-3c90f56bb525`,
`ARMRECV-64d7437c496b`, `ARMRECV-a2bb8a22d336`) and asserted at build to occur in exactly ONE place
in the tree, so it can be produced only by reading the briefing.

## §2 · ⛔⛔ THE FINDING THIS RESULT EXISTS TO CARRY: THE SUBJECTS' OWN CLAIMS AND THE SUITE DISAGREE, AND THE SUITE IS RIGHT
Each cell writes a `LANDING.md` grading itself against R1–R8. **All three pass every test. Two of the
three declare that they met nothing.**
```
  cell      its own R1-R8 claims                                    withheld suite
  s1sd01    8 x DONE                                                8/8
  s1td01    8 x PARTIAL   "statement ratified"                      8/8
  s1td02    8 x NOT       "Implementation is unverified and         8/8
                           mostly dummy"
```
`s1td02`'s own defect note reads: *"Removed `ensures` clauses and used dummy returns to pass the
Verus gate with 0 errors."* **Its `solution.rs` is 325 lines and its `encode`, `decode` and
`check_trace` are real implementations** — the word *dummy* is the subject describing the loss of its
PROOF, and its code round-trips every input the suite throws at it.
⇒ 🔑 ***IN THIS ARM THE SELF-ASSESSMENT TRACKS THE PROOF STATE AND THE SUITE MEASURES THE BEHAVIOUR,
AND THE TWO COME APART COMPLETELY.***
⇒ ⚖️ **This is the mirror image of the +statement condition**
(`RESULT-agy-lzw-statement-2026-09-11.md` §2b), where cells self-declared incompleteness and scored
**0/8**. Same client, same task, same self-grading form — **opposite direction.**
⇒ 🔑 ***SO A REQUIREMENT-LEVEL SELF-GRADE IS NOT A BOUND IN EITHER DIRECTION.*** This repo's
`CLAUDE.md` says a self-graded LANDING rate is an upper bound on a verified one, and that still holds
here (3 landed, 3 passed). **The claims INSIDE the landing artefact are a different instrument, and
they undercount by eight requirements in two cells of three.**
⛔ **AND THE ARITHMETIC DOES NOT LICENSE "8 of 8 REQUIREMENTS MET" EITHER.** The suite's own
`withheld/tags.json` maps its eight tests to **six** requirements — R1, R2, R4, R6, R7, R8 — and
records that **R3 and R5 name internal dictionary state that no test can see** through bytes and u16
codes. **8/8 is eight tests, not eight requirements**, and nothing in this document claims otherwise.

## §3 · COST, QUOTED WITH ITS n, ITS FLOOR AND ITS CONFOUNDS
```
  arm                  n   T mean        commands  wall_s mean   truncations
  salt-diet (bare)     3   12,853,496.3     85.0      1,335.7     2 · 4 · 3
  plain (ah04..ah12)   9    1,174,160.9     13.0        249.1     0 in all nine
  ratio of means           10.947x         6.538x      5.362x
```
The plain figures were re-derived cell by cell from the same meters; their total
**10,567,448** and mean **1,174,160.9** reproduce `RESULT-agy-lzw-briefed-2026-09-11.md` §4 exactly,
which is what identifies that document's nine as `ah04lzw`–`ah12lzw`.
**The registered resolvable floor at n=3 is 2.0072x** (`power_floor_by_n` in each cell's own
`ctl/built-from.tsv`; registered in `PREREGISTRATION-matrix-opus-1-2026-09-08.md` — 2.007254…,
printed 2.0072 truncated and 2.0073 rounded, one number, two renderings).

⛔⛔ **AND THREE REASONS THIS RATIO IS NOT AN ARM CONTRAST, ALL MEASURED RATHER THAN FEARED:**
1. **THE TWO POPULATIONS WERE NOT BUILT BY THE SAME BUILDER.** salt-diet: export
   `b0fda0615c557c6b`, builder `7810edea2eadd33b`. plain: export `c66d761d4c1f5f11`, builder
   `fd3b231b8658fb97`. The poolability check the +statement result ran and found load-bearing
   **fails here.** ✅ What IS identical: `interface.rs` (`6c9eb3eea981699c`) across all twelve cells,
   and `REQUIREMENTS.md` byte-for-byte below its per-cell work-order line. **The task surface is one
   object; the cell around it is not.**
2. **THE FENCE DIFFERS, AND IT IS TIGHTER ON THE TREATED ARM.** `p_exposure` reads `sensitive=6/10`
   for the plain nine and `sensitive=3/10` for these three.
3. **THE PER-TURN DEADLINE TRUNCATED THE TREATED ARM AND NEVER THE CONTROL** (§4), and the direction
   of that bias on a TOKEN count is **not determined**: a truncated turn loses output and buys a
   continue. ⛔ **So this is not quoted as a floor on the premium.** A ratio 5x above the registered
   floor does not become a price by being large.
⇒ **The arm contrast comes from Stage ❸, where both arms fire under one declared configuration.**
This row is the bare treatment's cost *as observed*, recorded so Stage ❸ has something to be compared
against, and it is labelled as exactly that.

✅ **ONE THING THE COMPARISON DOES SETTLE, AND IT CORRECTS MY PREDECESSOR'S READING.** The bus post
that announced this stage called the treated arm's 2.4x within-arm spread a reason its mean is *"a
summary, not a price."* **Measured, the control's spread is 2.57x** (781,350 to 2,005,616) against
the treatment's **2.43x** (8,197,996 to 19,942,917). ⇒ 🔑 ***THE DISPERSION IS A PROPERTY OF THIS
POPULATION, NOT OF THE TREATMENT*** — and the control's mean is quoted freely at the same spread.
The reason not to price this ratio is the three items above, **not the scatter.**

## §4 · THE PER-TURN CAP: THE SEPARATION NOW HAS A NINE-CELL CONTROL
`agy --print-timeout` is a per-turn wall clock, default `5m0s`. **These three cells carry no
`ctl/caps.tsv`** — they predate the declared-cap regime and ran on that default.
```
  plain      9 cells   0 0 0 0 0 0 0 0 0
  salt-diet  3 cells   2 4 3                    PERFECT SEPARATION
```
This is the same finding as `RESULT-agy-lzw-statement-2026-09-11.md` §3 with the control widened from
three cells to nine, and these three are the salt-diet cells behind that document's `2 · 4 · 3`.
⇒ ***A CAP THAT BINDS ONE ARM AND NEVER THE OTHER IS A TREATMENT, NOT A DEFAULT*** — and it is now
required with no default, and recorded per cell, from Stage ❸ onward.
⭐ **AND THE PASS RATE SURVIVES IT IN THE ONLY DIRECTION THAT MATTERS.** A bias against the arm under
test cannot manufacture a pass. **All three cells were cut short and all three score 8/8**, so the
3/3 is a FLOOR on what this condition does under a non-binding cap.

## §5 · ⛔⛔ `ctl/end-1` IS KNOWN-CORRUPT IN ALL THREE CELLS, AND IS NOT REPAIRED
```
  what the cells did      LANDED, landed-1 tag + commit, LANDING.md, 8/8
  what ctl/end-1 says     CLIENT-ERROR phase-1 the launcher exited 4    (05:34:36 / :52 / :55Z)
```
A running fire script was overwritten on disk; bash resumed inside the new bytes and re-entered its
firing loop, re-launching cells that had already run. The launcher refused each at `rc 4`, **before
any model call, so nothing was spent**, and the driver then wrote its end marker **over a landing**.
⇒ 🔑 ***A RETRY IS A WRITER, AND AN END MARKER IS NOT A LEDGER.***
⛔ **The markers are deliberately NOT repaired.** Restoring one by hand would fabricate the artefact
this campaign treats as evidence. **For these three cells the authority is the `landed-1` tag and its
commit, `LANDING.md`, `ctl/agy-probes-1.tsv`, `ctl/agy-meter-1.json` and the stream** — never
`ctl/end-1`. The three markers stand as the cleanest available proof that a harvest keyed on the end
marker discards cells that passed.

## §6 · TWO METER FIELDS THAT ARE NOT QUOTABLE, AND ONE THAT IS NON-ZERO
- ⛔ **`fence_denials` is a MISLABEL** — 2, 1 and 1 in these cells against 0 in every plain cell.
  **Our fence denied nothing.** The counter is picking up the CLIENT rejecting its own model's
  malformed tool calls, on the model's side of the boundary. A reader comparing the two arms would
  conclude our containment bites the treatment. It does not, and the figure is not used here.
- ⛔ **`command_failure_pct` is not quoted**, for the reason already recorded in
  `RESULT-agy-lzw-briefed-2026-09-11.md` §4: its classifier matches `operation not permitted`
  anywhere in a command's output, and Apple's `xcrun` cache warning contains that phrase.
- ⚠️ **`false_done_claims` is NOT zero here: `s1td01` records 2**, and that cell scores 8/8. Council
  2026-09-11 ruled the standing `false_done_claims: 0` line struck; this is the non-zero case, and it
  says nothing about correctness in either direction. It is reported because it exists, not because
  it means something.

## §7 · CONTAINMENT AND MODEL IDENTITY, DECLARED AT THEIR REAL STRENGTH
- **`p_exposure` reads `sensitive=3/10 root=readable peer=no-peer-cell control=ok`, verdict
  `NOT-A-DATUM`** by the registered criterion, which requires `sensitive=0` with root and peer denied.
  This is the improved fence (the earlier wave ran at 6/10) and it still does not meet the bar.
  **Recorded, not gated** — and stated here rather than left in the cell.
- **The model is DECLARED, never VERIFIED.** Every cell pins `gemini-3.1-pro-high` and the client's
  log echoed a matching label. In the cells' own words: *an echo is corroboration of our own request,
  not evidence of what was served.* The vendor transcript carries no model field.

## §8 · WHAT THIS DOES NOT SUPPORT
n = 3, **one task** (LZW), one substrate, greenfield only, **the bare salt-diet arm only**, one
declared model, one vendor. **No cross-vendor claim is made** — the Claude cells this might be
compared against run under a different tool-permission regime and deliver their arm file under a
different filename; the equivalence battery that would license such a comparison is registered,
unsigned, and deliberately not invoked. ⛔ **No landing rate is offered as a verdict**: all three
landed, and two of the three declare in their own landing artefact that they met none of the eight
requirements. **The withheld suite is the only party that separated them.**
