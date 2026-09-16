# AMENDMENT — agy LANE **LEVEL 6**: the twelve conditions the harness can express today, FROZEN BEFORE ITS FIRST CALL
## bench (SaltBench lead), 2026-09-16. Desk row **MR**. Released by council 2026-09-16 ③a: *"yes, accept all recs"* —
## (a) **discriminating conditions go into the DESIGN targets** for levels 6-8, the arXiv-update gate unchanged;
## (b) the Claude-lane worker stays on HC stage 1; (c) level 7's brownfield re-fires authorised (level 7's own freeze).
## A runner seat `gemini` is the HAND; **bench is lead — design, caps, scoring rules, amendments.**
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** No cell fires on this file before that signature is appended below.

---

## §H0 · ⚖️ THE INPUTS, IN ONE BLOCK SO THE HAND NEEDS NOTHING ELSE
```
  1  MODEL IDs      gemini-3.1-pro-high (Pro conditions) · gemini-3.8-flash-high (Flash conditions)
                    Both listed by `agy models` on the run box, 2026-09-16. Re-assert served at launch;
                    a served-model mismatch VOIDS (§H6 row 1).
  2  n              3 per condition.
  3  POPULATION     12 conditions, 36 cells (§H1). Nothing is added, dropped or substituted.
  4  EXPORT         any single harness sha whose tree is IDENTICAL to master `eacb9ec` under
                    tasks/systems-v3/{LZW,LRU,Paxos}/ and that carries the any-503 supervisor
                    (gemini_canary_wave_v1.sh). Measured: `e5f7126` differs from `eacb9ec` under those
                    task dirs ONLY in LZW/brownfield/solution.rs, which no level-6 condition builds.
                    ⛔ AND the export MUST carry the launcher's P-DELIVERY repair (§H4.5): the token is never
                    written to ctl/launch.log, and the uniqueness walk re-runs immediately before the client
                    spawns. No sha without it qualifies. One sha for all 36 cells, recorded.
  5  FIRE ORDER     by expected discrimination (§H2), under the council's any-503 rule.
  6  USAGE          `gemini` reads agy /usage at each fire and bank (council 09-16 ③b); bench consumes it.
```

---

## §H1 · THE POPULATION — 12 CONDITIONS, 36 CELLS
```
  block  problem   field        arms                                     models          conditions   cells
  S      LZW       greenfield   plain-stmt · salt-stmt                   Pro · Flash          4          12
  B      LRU·Paxos brownfield   plain-bare · salt-bare                   Flash                4          12
  G      LZW       greenfield   plain-bare · salt-bare                   Pro · Flash          4          12
                                                                                    TOTAL   12          36
```
**WHY THESE TWELVE:** they are every owed agy-lane condition in the matrix census that the harness expresses
**today** with givens not in doubt. Brownfield FreeList/LZW/Crc32, brownfield × statement, and greenfield
spec-change are levels 7 and 8, each gated on a delivery this level does not need. **Pro's brownfield LRU/Paxos
conditions are DONE** (level 4) and are not re-run.
📌 **Pro's LZW cells from 2026-09-10/11 are NOT counted DONE by the census** (§C4: LZW was excluded from the bare pair and
held at n = 1 under desk HC), so blocks S and G run Pro too. **Those earlier cells enter this level ONLY as priors (§H2).**

**ARM → FLAGS** (`cell_build.py --client agy --budgets pricing`):
```
  plain-bare   --arm plain     --field greenfield                    (block G)
  salt-bare    --arm salt-diet --field greenfield                    (block G)
  plain-stmt   --arm plain     --field greenfield --statement        (block S)
  salt-stmt    --arm salt-diet --field greenfield --statement        (block S)
  plain-bare   --arm plain     --field brownfield --phase 1          (block B)
  salt-bare    --arm salt-diet --field brownfield --phase 1          (block B)
```
⛔ **`--arm salt-diet`, NEVER `--arm salt`.** ⛔ **`--hint` is not used.**

---

## §H2 · ⚖️ THE DISCRIMINATING TARGET — COUNCIL ③a(a), APPLIED PER CONDITION, BEFORE ANY DATA
The ruling puts discrimination into the DESIGN, not the gate: **every condition carries a registered expectation of
whether its primary instrument can vary, and the wave fires in that order**, so a halt on capacity leaves the most
informative conditions done. **Each expectation below cites a result of record; none is a prediction of an arm
contrast.**
```
  order  block  expectation        prior (result of record)
  1      S      VARIES             Pro LZW plain+statement 3/3 at 8/8; salt-diet+statement VERIFIED 1/5 while
                                   LANDING 5/5 — the treated cells decline to ship unproven code
                                   (RESULT-agy-lzw-statement-2026-09-11.md §2b).
  2      B      VARIES (retention) Pro level 4: withheld suite plain 6/6 full, salt-diet 4/6 full; RETAINED plain
                                   0.978-0.992, salt-diet 0.322-0.756 (RESULT-gemini-brownfield-level4-2026-09-14.md
                                   §R1). Flash has never run brownfield.
  3      G      AT CEILING         Pro LZW plain-bare 9/9 FULL PASS (RESULT-agy-lzw-briefed-2026-09-11.md §1);
                                   salt-diet bare 3/3 FULL PASS (RESULT-agy-lzw-saltdiet-stage1-2026-09-11.md §1).
```
⛔ **NOT THE 8/9 OF `RESULT-agy-lzw-scored-2026-09-10.md`.** That file's own errata banner says its nine cells ran with
NO SHELL, NO BUILD and NO BRIEFING and are not a plain-arm datum; it points to the briefed wave, which is cited above.
The first draft of this row cited the 8/9 — caught against that file's header before freeze.
⚠️ **THESE ARE PRIORS FROM PRO.** Whether Flash reproduces them is what the Flash cells measure; a different Flash
shape is a result about the Flash-on-this-lane pair, never a failed prediction.
⛔ **A CEILING IS NOT PARITY.** A condition whose cells all pass is recorded **UNRESOLVED-BY-CEILING** on pass rate —
the level-5 statement lesson (18 of 18), registered here before the first call so a full row cannot read as a result.
⛔ **LANDED IS NOT VERIFIED.** Block S's prior is the case where a landing rate reads 5/5 and the withheld suite reads
1/5. **Every rate this level publishes is scored against the withheld suite; a self-graded landing is never quoted.**

---

## §H3 · CAPS — CARRIED, NOT RE-DERIVED, AND THEIR INCIDENCE IS REPORTED
```
  token cap       T1_TOK 250,000,000 — the level-5 value, unchanged; the lane has no USD pricing
  per-turn        AGY_PRINT_TIMEOUT 1800s · controller patience AGY_TURN_TIMEOUT 2100s (agy_wave_v3.sh's declared values)
  reporting       CAP-TOKENS, CELL-KILLED and TURNS-CUT are REPORTED per arm, never a void
```
⛔ **WHICH ARM TRIPS A CAP MORE:** every TURNS-CUT measured on this lane so far is a treatment cell. A cap that binds one
arm is a treatment; it is held constant here so its incidence is readable, and it is reported as a split by arm.

---

## §H4 · ⛔⛔ THE CONFOUNDS — REGISTERED, AND THEY TRAVEL WITH EVERY TABLE
1. **TIER + GENERATION** (level 5 §F3): Pro-3.1 vs Flash-3.8 moves both. Any Pro↔Flash difference in blocks S and G
   names both axes, every time; it is never a tier result.
2. **DATE AND EXPORT versus the Pro priors in §H2**: those ran on earlier exports on other days. §H2 uses them to ORDER
   the wave, never as the other arm of a contrast.
3. **Block B has no Pro pair at this level** — its Pro cells are level 4's, on export `ecd3924`. A Flash-vs-Pro
   brownfield reading carries confounds 1 and 2 together.
4. ⛔ **A KNOWN FENCE DEVIATION, DECLARED BEFORE THE FIRE RATHER THAN DISCOVERED AFTER IT** (systems, phase-2 scope census,
   2026-09-16): **the agy fence lets the subject read and write its own `ctl/`.** In level 5, 41 of 185 cells listed or opened
   `ctl/` — all Flash — and 15 opened `briefing-nonce`; one ran `tail` on the arm file and then read the nonce. ⇒ **P-DELIVERY on
   this lane proves the arm FILE was opened, not that the METHOD was read.** `ctl/` holds no withheld test and no other arm's
   material, and both arms are equally exposed. **This level fires on the same fence**, because the fix is its own fence
   freeze; the per-cell `ctl/` read census is a REPORTED column (§H8), and no delivery claim is made from P-DELIVERY alone.
5. ⛔⛔ **A THIRD ROUTE TO THE TOKEN, AND IT IS REPAIRED BEFORE THIS LEVEL FIRES, NOT DECLARED** (systems, 2026-09-16 09:31):
   the launcher's own line *"ack token … lives ONLY in the cell's briefing file"* tees the token into `ctl/launch.log` BEFORE the
   client starts — 101 of 122 file-mode cells carry it, and 29 level-5 subjects opened that log. The build-time uniqueness walk
   is correct when it runs; `launch.log` does not exist yet. ⇒ **The line asserting the token has one home was its second home.**
   ✅ **REQUIRED IN THE EXPORT (§H0 row 4):** the log line carries a hash of the token, never the token, and the launcher re-runs
   the uniqueness walk right before spawn, refusing on a second home. ⇒ **A cell whose `ctl/launch.log` contains the raw token
   is VOID** (§H6 row 7). ⚠️ Whether any level-5 P-DELIVERY is unsupported (a `launch.log` read before the first echo with no arm-
   file read) is a separate sizing for level 5's result of record, and is not decided here.

---

## §H5 · THE READING RULES — level 5 §F4, inherited in full, plus two
Rules 1-8 of level 5 §F4 apply unchanged (sign only · a TURNS-CUT pass is a floor and its costs are unpoolable ·
landing and passing are two rates · an arm-correlated cut is decided by its sign · `bugs_introduced` is a floor ·
export sha recorded · no USD · an unmetered cell is a row, not a smaller denominator).
**9  VERIFIED FIRST.** A condition's rate is withheld-suite passes over scorable cells; LANDED is a separate column.
   ⛔ **On this lane LANDED means `LANDING.md` EXISTS, not that the subject declared a landing** (systems, 2026-09-16: 13 of 146
   LANDED agy cells carry no `landed-N` tag, and three result-bearing cells' own `.seat` records say the subject gave up). The
   LANDED column therefore also carries `declared` (a `landed-N` tag present) beside it, and neither is ever a pass rate.
**10 RETENTION IS BLOCK B's PRIMARY SEPARATOR, AND IT IS A PROPERTY OF THE GIVEN.** It is reported per cell beside the
   withheld suite, never averaged across problems (LRU and Paxos seeds differ in size).

## §H6 · WHAT VOIDS A CELL (faults only — no expectation from §H2 appears here)
```
  1  the served model differs from the condition's model id             VOID
  2  the cell ends METER-BLIND / no readable T                            VOID(UNPRICED)
  3  ctl/field or ctl/card_extras differs from the condition's flags      VOID
  4  the fence battery does not pass for the cell's PATH                  DO NOT FIRE
  5  a 503 inside the cell                                                DISCARD per the council's any-503 rule
  6  CAP-TOKENS · CELL-KILLED · TURNS-CUT                                 NOT void: reported per arm
  7  ctl/launch.log contains the raw P-DELIVERY token (§H4.5)             VOID
```

## §H7 · WHAT THIS LEVEL CANNOT ESTABLISH, SAID BEFORE ANY DATA
1. **Anything about tier alone** (§H4.1). 2. **No magnitude** — sign only at n = 3. 3. **No cross-lane comparison** with
the Claude lane in dollars or tokens. 4. **A cost result and a pass-rate result are two results**, never joined by
"and therefore". 5. **A condition at ceiling says nothing about the arms** (§H2).

## §H8 · WHAT THE HAND DELIVERS, AND WHAT THE LEAD OWES AFTER
```
  one export sha across all 36 cells · per-condition score receipts as FILES · the per-cell table of record
  (arm · problem · model · T · wall · turns · done_reason · end · verdict · tests · retention for block B ·
  TURNS-CUT flag · declared (landed-N tag) · ctl/ read census · source receipt) · TURNS-CUT and CAP incidence as a
  SPLIT BY ARM · the /usage rows it logged
```
⇒ **The lead scores and writes the result of record, and RE-CUTS THE MATRIX CENSUS IN THE SAME COMMIT** (council
09-16 ⑤d). Any public sentence, and any claim about the method, is the Captain's.

---
## ⚖️ SIGNATURE (non-author) — NOT YET GIVEN
