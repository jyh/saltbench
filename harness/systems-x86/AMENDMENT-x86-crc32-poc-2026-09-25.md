# AMENDMENT — THE x86 LANE's PROOF OF CONCEPT: CRC-32 IN SCALAR x86-64, TWO ROWS, FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-09-25. The Captain, council 2026-09-16: *"we need to develop x86 saltbench soon"* · *"CRC32 sounds like a
## good choice for a PoC … it might make sense to produce a proposal with CRC32 x86 saltbench as the target."* Council 2026-09-25, on the
## run box's points: *"#1 the x86 lane on both sides (paris's proposal …; gemini's side commences)"*. The slice is paris's proposal v1 §5
## (S7), mirrored for the agy lane as gemini proposed (X4). bench is lead; the Claude row's hand is bench, the agy row's is `gemini`.
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES BEFORE THE RELEASE ADDENDUM (§X9) NAMES THE EXPORT AND EVERY
## RELEASE CONDITION READS MET.** Signature and release are two acts.

---

## §X0 · THE INPUTS
```
  1  ROWS / MODELS   CLAUDE row  claude-opus-5 (the pilot's; the served set per condition as lane B §Q0 row 1)
                     AGY row     gemini-3.1-pro-high (the pilot's; re-asserted served at launch; a mismatch VOIDS)
                     A newer model is not substituted, for block N §N0 row 1's reason: the x86 lane is a new substrate,
                     and a model change on top of it would leave two variables and no contrast.
  2  PROBLEM         Crc32, scalar x86-64, the card at saltbench-systems tasks/systems-x86/Crc32/ (card S4, bench).
  3  ARMS            plain · salt-diet, each an arm TEXT (CLAUDE.md for the Claude row, AGENTS.md for the agy row, same bytes)
  4  EXTRAS          none · statement (the statement arm delivers paris's Lean statement FILE, pinned BY BLOB; plain + statement
                     receives the same bytes as salt-diet + statement, which is v3's neutrality rule)
  5  n               SMOKE PAIR first, per row: plain·none + salt-diet·none at n = 1. These are PLUMBING, never pooled.
                     Then the SLICE: n = 3 per condition.
  6  POPULATION      per row 1 problem × 2 arms × 2 extras = 4 conditions, 12 cells; two rows = 8 conditions, 24 cells (§X1)
  7  x86lean         pinned 1f9ad9b, vendored STRIPPED (vendor_x86lean.py; 16 raw treatment-word hits → 0, controls fired),
                     Lean v4.27.0 (the harness pin, proposal v1 §2 — NOT x86lean's own v4.32.0-rc1).
  8  REFEREE         check_x86.py: executor (a) native under Rosetta, executor (b) the Lean model, AGREEMENT required per input,
                     TARGET for salt-diet (three standard axioms only; `bv_decide`'s native axiom is refused here).
                     WITHHELD SET: 82 inputs from gen_hidden.py (expected values from zlib, cross-checked bit-serial).
                     FUEL: F = 2 (§X4).
  9  CAPS            CLAUDE row: lane B §Q4, unchanged (C1_USD $37.21, W1_SEC 144,000; CAP-COST and CAP-WALL armed).
                     AGY row: level 6 §H3, unchanged (T1_TOK 250,000,000; AGY_PRINT_TIMEOUT 1800 s; AGY_TURN_TIMEOUT 2100 s).
 10  ACCOUNT         CLAUDE row: the run box's pool per block N §N0 row 8 and ADDENDUM 2 §A2.3 (a dedicated dir, the account check
                     AND one authenticated read before the first cell, the check per cell); after that pool retires, a P1-capacity
                     pool named per cell. AGY row: the agy subscription.
 11  PRECEDENCE      O4 is first on the run box's points (council 2026-09-25). This lane's cells go BEFORE O37's (blocks N and NA).
```

---

## §X1 · THE POPULATION
```
  row     model                 field        arms                 extras             conditions   cells
  CLAUDE  claude-opus-5         greenfield   plain · salt-diet    none · statement        4          12   (+ 2 smoke)
  AGY     gemini-3.1-pro-high   greenfield   plain · salt-diet    none · statement        4          12   (+ 2 smoke)
```
Not proposed here: brownfield, spec-change (the card has no phase 2), other models, LZW (U1 first), the vector add-on (after P2).

## §X2 · THE ORDER
Per row: smoke plain·none → smoke salt-diet·none → READ BOTH (§X3) → the slice, cells in the order none plain#1 · salt-diet#1 · #2 ·
#3, then statement the same. The agy row may fire before the Claude row: the Claude row's pool waits on the Captain's login (desk YG),
and the agy row does not.

## §X3 · THE SMOKE PAIR IS THE TRIPWIRE, AND WHAT IT MUST SHOW
Read by the lead and posted before the slice fires. Each of these reads, or the row HOLDS:
the arm file present and the neutrality gate green in the built view · the fence sha with a probe receipt (a network-denial arm for the
Claude row; the battery for the agy row, whose TMPDIR-identity row is printed) · `bin/rt check: OK` at t0 on the stub · the client
pin or served model · at least ONE working shell call in the transcript (the agy lane has landed cells with zero working calls: the
shell proof, gemini's X3, folded into the smoke) · the end marker verbatim · the referee's verdict line, carrying the export sha,
`cell_translation`, and for salt-diet the TARGET line and `#print axioms`. **A smoke cell's pass or fail is NOT a result and is
never quoted;** only its PLUMBING is read.

## §X4 · THE FUEL FACTOR, F = 2, AND WHY
Executor (b) gets F × executor (a)'s retired-instruction count + 1 per input. The model and the native run agree exactly on a halting
routine (systems measured (b) = (a) + 1, the off-program fetch), and K10 drives F = 1 end to end. So F matters only where the two
DISAGREE, and there it is a harness finding (a model-native divergence), never a subject failure. F = 2 leaves that margin, and the
lead's referee drives (R1 PASS AGREE=82) ran at F = 2. **It binds neither arm more**, since both arms' routines run under the same
factor. A cell that exhausts it is reported as REFEREE-FUEL with the counts, and is not scored.

## §X5 · PREDICTIONS — REGISTERED BEFORE ANY DATA
(i) salt-diet's cap incidence (CAP-COST on the Claude row, TURNS-CUT or CAP-TOKENS on the agy row) is ≥ plain's, within each row and
extras; the proposal priced salt-diet up to $40 against a $37.21 cap, so **CAP-COST CENSORING OF THE CLAUDE ROW's salt-diet cells is
EXPECTED** and is reported as a floor, never raised; (ii) every salt-diet cell that reaches TARGET reads the three standard axioms or is
refused at AXIOMS; (iii) no plain cell reads a `cell_translation=differs` line (plain ships no Lean). ⛔ **No prediction about pass rate or
premium** at n = 3 on one problem.

## §X6 · CONFOUNDS — REGISTERED, AND THEY TRAVEL WITH EVERY TABLE
1. **ONE PROBLEM.** Everything here is about CRC-32 in scalar x86-64. Nothing generalises to "x86", let alone to the method.
2. **THE ARM IS A NEW TEXT.** The x86 salt-diet text is v3's with 26 target-forced changes and 13 method changes RESOLVED (reverted,
   justified or declared: the card's ARM-salt-diet-ACCOUNT.md). Its differences from v3 are part of the treatment on this lane.
3. **THE CAP IS THE PILOT'S** and is expected to bind salt-diet (§X5 (i)).
4. **TWO LANES, TWO ENVIRONMENTS:** the Claude row's cells carry the pilot's unusable TMPDIR (block N ADDENDUM 2 §A2.5), unless the
   release adopts systems' `CLAUDE_CODE_TMPDIR` fix for this new lane after its one client-in-loop turn (the lead's ruling, 2026-09-25).
   The agy row sets its own. The release says which, and it is never a contrast.
5. **Cross-row (Claude versus agy) is NOT a registered contrast.**

## §X7 · VOIDS (faults only)
Lane B §Q7 rows 1–5 and 8–10 (Claude row) · level 6 §H6 (agy row) · plus: `x86_cell_build.py` refuses (NON-EMPTY · TREATMENT ·
NEUTRALITY) → DO NOT FIRE · the smoke's working-shell count is 0 → the row HOLDS · REFEREE-FUEL → NOT-SCORED(HARNESS).

## §X8 · WHAT THIS CANNOT ESTABLISH
No effect size and no premium (n = 3, one problem) · nothing about models · nothing cross-lane · a PASS is behaviour on 82 withheld
inputs plus, for salt-diet, a kernel-checked TARGET, and says nothing about untested inputs for plain.

## §X9 · RELEASE CONDITIONS — each MET, with its receipt, in the release addendum before the first smoke cell
```
  R1  the export: ONE saltbench-systems sha carrying the harness (systems-x86: fence, declare (A), rt TMPDIR/bytecode fixes, the export
      route), gemini's agy client and launcher branch, the card with its withheld set, paris's statement file and R1 control
  R2  BOTH ARM TEXTS FROZEN: plain and salt-diet, each with a non-author read (salt-diet: its ACCOUNT's remaining items; plain: its own)
  R3  the x86 turn prompts FROZEN (the card's, bench's)
  R4  the Claude row: the dedicated dir, the account check, one authenticated read (desk YG); the agy row: /usage read
  R5  the referee re-driven AT THE PIN (v4.27.0 build of 1f9ad9b): R1 PASS with full agreement, the stub TESTS_FAIL
  R6  one dry cell per row end to end at zero spend (build → fence → battery or probe → referee on the stub)
```
