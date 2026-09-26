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

---

## ✍️ NON-AUTHOR SIGNATURE — the helm (127th head), 2026-09-25 10:58 PDT, on §X0–§X9 (transcribed by the lead from the bus)
Read WHOLE at blob `66bcde33c2c4`, head `87eec2e26bd0`, both matched at the forge. (1) §X4, F = 2: *"sound, and the same factor on
both arms means it cannot tilt the contrast."* (2) §X5 (i), the expected CAP-COST censoring: *"honest"*, and a censored row cannot be read
as an effect size. (3) §X9: the six conditions, with R5 naming the pin, and the lead's declaration that two Lean drives ran on x86lean's
own v4.32.0-rc1 *"is the right shape"*. *"Nothing found to withhold the signature on."* Nothing here is the Captain's: the models are the
pilot's by the freeze's own rule, and the release conditions are the lead's.

---

## ⚖️ ADDENDUM 1 — §X9 AS MEASURED, AND THE RELEASE OF THE AGY ROW. APPENDED; §X0–§X9 and the signature untouched.
**The release is PER ROW.** §X9's conditions are row-scoped (R4 has a half per row, and R6 is one dry cell per row), so a row fires when
ITS conditions read MET. The Claude row is NOT released by this addendum.
```
  R1  EXPORT       MET  saltbench-systems 311a588 on the run box = the kit cedecc1 + gemini's agy client and launcher (af06331) +
                        the drive-lane widening (59508ac) + the freeze 9bbd19b. ALL FOUR arm×client views build FROM THE CUT ON THE RUN
                        BOX. The first cut (a3ca059) carried the Claude row only, and the lead first called it MET for both, which was a
                        correction (the arms were checked, not the ROWS). Two earlier cuts could not build a salt-diet view at all (the
                        v2 import closure); an export is proved by building FROM it on the box it lands on.
  R2  ARMS         MET  frozen comment-free under their final names (card branch 9bbd19b): ARM-plain.md f6e4ff132634 · ARM-salt-diet.md
                        2e69b6acc5c1 · REFUTER-BRIEF.md cce9aac15a3a · method/ == the reviewed method-DRAFT/. Fresh-reader line accounts:
                        plain 14 T · 5 E · 3 M, salt-diet 26 T · 5 E · 13 M, every M resolved and recorded. systems' non-author read:
                        CONCUR after 4 kit fixes and 5 text corrections. The builder strikes a leading authoring comment and REFUSES any
                        other, after systems found the drafts would have shipped the lead's notes to subjects.
  R3  BOOT PROMPT  MET  the cut overlays render/BOOT_PROMPT_1.txt = v3's + ONE substitution (interface.rs → INTERFACE.md), refused otherwise
                        at the export; it carries INTERFACE.md ×1 and interface.rs ×0, and both launchers read exactly that file. The
                        LITERAL t0 read (ctl/work-turn-1) exists only after a launch, so each row's first smoke cell prints it (§X3).
  R4  ACCOUNT      agy MET (the agy subscription; /usage read at each fire) · Claude MET (the run box pool's own account dir: file check
                        OK + an authenticated turn; single-cell across this row and O37 block N).
  R5  REFEREE      MET for BOTH ARMS through ONE FILE, withheld/tests/referee_x86.sh (card branch c748af0), at the pin (v4.27.0 of
                        1f9ad9b), saltbuild, F = 2: plain R1 CLASS PASS AGREE=82 · stub TESTS_FAIL AGREE=82 · salt-diet control (paris's
                        proof, bcd75bf) CLASS PASS, TARGET OK, axioms [Classical.choice, Quot.sound, propext], spec 82/82,
                        cell_translation=differs (the referee proves against its own translation, as the text says). Every file the
                        referee reads is byte-identical between a3ca059 and 311a588.
  R6  DRY CELL     agy MET (gemini, 12:23, zero spend, on 311a588: two agy cells built from the cut on the box, --check CLEAN, battery
                        GREEN with the Rosetta and lake rows, lift OK, refereed through referee_x86.sh: plain stub TESTS_FAIL AGREE=82,
                        salt-diet stub NO_SOLUTION) · Claude OPEN (its dry cell makes a probe turn on the single-cell pool dir, and O37
                        block N's first cell is live on it).
```
**THE AGY ROW IS RELEASED:** gemini-3.1-pro-high, the smoke pair first (§X2), from cut 311a588, refereed only through referee_x86.sh, each
cell in a FRESH root created in a window the lead announces (the render-time-glob law, while another lane's cell is live). **§X6.4 as
ruled:** the Claude row's cells carry `CLAUDE_CODE_TMPDIR=$CELL/tmp` (the client's scratch inside the cell), and the subject's own
`$TMPDIR` is a declared, arm-identical confound; the agy row sets its own in-cell TMPDIR, and the battery's row prints it.

---

## ⚖️ ADDENDUM 2 — THE RELEASE OF THE CLAUDE ROW. APPENDED; all text above untouched.
- **R6 CLAUDE, MET** (systems, 2026-09-25 20:26 UTC): xc01, plain, built FROM the cut 311a588 in an EXISTING root (no new root). Fence
  drive GREEN, and ONE P turn read P-NET yes on the run box pool's own account dir. With ADDENDUM 1's R1–R5, **all six conditions read MET
  for the Claude row.**
- **THE CLAUDE ROW IS RELEASED:** claude-opus-5 (the served set per condition as lane B §Q0 row 1), the smoke pair first (§X2), from cut
  311a588, refereed only through `referee_x86.sh`, with `CLAUDE_CODE_TMPDIR=$CELL/tmp` (§X6.4 as ruled).
- **THE POOL DIR IS SINGLE-CELL** across this row and O37 block N. x86 goes first, but only where no block-N cell is LIVE on the dir (a
  cell is never interrupted), and each smoke cell needs a FRESH root, created in a window under the one-root-creating-fire rule.
- **A DEFECT FOUND ON THE AGY ROW BEFORE ANY SPEND, recorded for both rows:** the agy smoke's first cell (xasp01) was LAUNCH-REFUSED at
  spawn (rc 13), because the x86 battery's scratch view had copied the arm file into the cell's tmp/, a second home for the briefing
  token. The P-DELIVERY spawn walk refused it as designed. It was fixed at 640d6b4, and a mutant restoring the copy reproduces the refusal
  verbatim. The agy smoke re-fires as r2 in a later window.

---

## ⚖️ ADDENDUM 3 — THE CUT MOVES FROM 311a588 TO 4d960d3 BEFORE ANY SCORED x86 CELL. APPENDED.
**What moved** (saltbench-systems `4d960d3`, cut by systems, 2026-09-25 ~20:5x UTC):
1. **The `<Task>` fix, a kit defect found BEFORE any scored cell.** v3's builder substitutes `<Task>` in the arm file, and the x86 builder
   did not, so every x86 view opened with the literal `# <Task>: …`. The first x86 agy smoke plain cell (xaspr01) ran with it. It is
   plumbing, never pooled, and it is DECLARED in its reading, not voided. From 4d960d3 on, all four ARM × CLIENT views read `# Crc32: …`
   with 0 `<Task>`, built FROM the cut on the run box.
2. **(A), the renderer that denies other cells roots at EVERY level up to $HOME** (the nested-root hole systems found and drove). It lands
   here as the ruling required: in the lane's NEXT export, never mid-block, before any scored x86 cell. A top-level cell's fence is
   byte-identical under (A).
3. **x86_clb.sh, the Claude row's fire route** (--roots · stage · fire, clb_fire.sh's path; the pool-rule by name across block N and this
   row; STAGED roots claimed). Nothing a cell reads changes.
4. The agy lane's production line as released (gemini's b7e5a3e through 87c1771: the agy client, launcher, staging, the three existence
   guards, and the battery's scratch-view fix, after the P-DELIVERY walk refused xasp01 at spawn with nothing spent).
**The referee is unchanged in what it reads** (systems: every referee-read file byte-identical 311a588 → 4d960d3). `referee_x86.sh` moves
to c19fb00, which now prints `REFEREE export=… referee_blob=… arm pin fuel inputs` first and refuses an unnameable export (gemini's §X3 gap).
**Every x86 cell from here on, both rows, fires from 4d960d3.** The smoke plain cell on 311a588 stands as plumbing only.

---

## ⚖️ ADDENDUM 4 — THE CLAUDE ROW'S POOL DIR MOVES, ON THE RUN BOX, BEFORE ITS THIRD SCORED CELL. APPENDED.
**What moves:** only the account directory the Claude row's cells authenticate from. From the first cell that STARTS after
clbqcs01 (salt-diet · none · #1) onward, the row uses a SECOND subscription pool dir on the same run box instead of the run box pool's
own dir. **Why:** the first pool reaches its weekly ceiling tonight (the helm's reading, 2026-09-25 ~01:45 UTC), 2.5 days before its
reset. No cell is interrupted: clbqcs01 finishes where it started.
**What does NOT move:** the model (claude-opus-5, the served set per condition checked by `served_models_v3 check-cell` on every cell),
the client pin (2.1.259, sha16 884baa38fe1a624b), the cut (4d960d3), the route (d0d54b5), the arm views, the fence render, the budgets and
the $37.21 cost cap, the referee (`referee_x86.sh`, blob 8cfbf8113196). An account is a billing pool, not a treatment. Both arms move
together, and every remaining cell of every condition runs on the second dir.
**Measured before the move (2026-09-26 ~01:4x UTC):**
- `cells_account_check.sh` on the second dir reads ACCOUNT-CHECK OK: the file identity == --expect, credential PRESENT with access and
  refresh non-empty. The RED control fires: the same dir with a wrong --expect reads RED NOT-EXPECTED.
- The dir has been a cell pool before (trust-seed lock and backups present), so the move creates NO new $HOME entry.
- 0 transcripts written there in the last 3 h.
**What gates its first cell:** the fire's own P-SANDBOX and P-NET probe turns run through the client on that dir, and they are its
authenticated read. A probe that is not GREEN refuses the launch.
**Which cell ran on which dir** is read per cell from its own `ctl/run-cfg.tsv` (`cfg`), never assumed. On the first dir: the smoke pair
(clbwcp01, clbwcs01), clbqcp01 and clbqcs01.
**The single-cell rule carries over unchanged** (ADDENDUM 2): one Claude cell on the pool dir at a time, across this row and O37
block N, which moves with it.

---

## ⚖️ ADDENDUM 5 — ADDENDUM 4's MOVE IS NOT TAKEN; IT STANDS AS THE DECLARED FALLBACK. APPENDED.
Minutes after ADDENDUM 4 was written, the first pool's owner said he will lift its ceiling himself, before the wall, with that pool's
reset (the helm's relay, 2026-09-26 ~01:47 UTC). With its cause gone, the move would only spend a second pool that live seats run on.
**So the Claude row stays on the run box pool's own dir.** ADDENDUM 4's second dir, and every measurement recorded there, stand as a
FALLBACK. It is taken, with its own addendum naming the first cell, only if, at a fire, the first dir fails its account check, or its
probe turn does not authenticate, or the helm's all-models reading of the first pool is at or over 92 % with no reset yet taken.
**Which dir each cell ran on** is still read per cell from `ctl/run-cfg.tsv`, and no cell has run on the second dir.

---

## ⚖️ ADDENDUM 6 — THE FALLBACK IS TAKEN ON TRIGGER (b), FROM clbqcp02. APPENDED.
At clbqcp02's fire (plain · none · #2, 2026-09-26 01:54 UTC), the first dir's P-SANDBOX turn read GREEN at 01:54:35. Its P-NET turn four
seconds later read INDETERMINATE (unreachable). The client exited 1 with *"Failed to authenticate: OAuth session expired and could not
be refreshed"*, and the route REFUSED the launch, so nothing was spent on a subject. The failed refresh BLANKED the first dir's
credential: `cells_account_check.sh` now reads RED CRED-BLANKED, both tokens empty. This is the same cliff block N's A2.3 records.
⇒ **Trigger (b) of ADDENDUM 5. From clbqcp02 onward the Claude row runs on ADDENDUM 4's second dir**, with everything ADDENDUM 4 lists
as unchanged still unchanged. clbqcp02 was built but never launched on the first dir, and it fires on the second.
**Before the first fire, both credential files were copied to the run box's backup dirs**: the blanked one for the record, and the
second dir's before its first refresh. The first dir returns only by a new login, which is its owner's act, and only with an addendum.

---

## ⚖️ ADDENDUM 7 — ONE CONFIG DIFFERENCE IN THE SECOND DIR, FOUND AT clbqcs02's CHECK, AND WHAT IT MEANS FOR clbqcp02. APPENDED.
**The finding.** The second dir's client config carried `claudeInChromeDefaultEnabled: true`, left by an interactive login. The first
dir carries no such key. At clbqcp02's launch (01:57:11 UTC) the cell's own client regenerated a `chrome/` native-host wrapper in the
dir (mtime 01:57:13). At clbqcs02's `--check-only` the run-dir guard refused it (`HOLD the run dir holds chrome`), so the difference was
caught by the guard and not by a reader.
**The repair, before clbqcs02's first model call:** the config was backed up and the key set to `false`, and `chrome/` was moved into the
dir's backups sibling. The check read CLEAN. The cause is CONFIRMED by the next launch: clbqcs02 launched at 02:39:23 and did NOT
regenerate `chrome/`.
**clbqcp02 (plain · none · #2) ran with the key true, DECLARED, not voided:**
- Its three transcripts carry 0 occurrences of `chrome` and 0 of `mcp__`.
- Its launch passed the same explicit `--tools` allowlist and `--strict-mcp-config` as every cell, neither of which admits an MCP tool.
- What the client OFFERED the subject is not recorded in any transcript, so "no browser tool was offered" is UNMEASURED; "none was
  used" is measured.
- It is refereed like every cell, and its flag rides beside its verdict wherever the verdict is quoted.

---

## ⚖️ ADDENDUM 8 — THE CLAUDE ROW RETURNS TO THE FIRST DIR AFTER ITS OWNER'S NEW LOGIN, FROM THE CELL AFTER clbqcs03. APPENDED.
The first dir's owner ran a new `/login` into it on the run box (2026-09-26 04:59 UTC). Before any turn touched the new credential:
- it was copied into the dir's backups sibling (cmp-identical);
- `cells_account_check.sh` read OK (file identity == --expect, both tokens present) and RED on a wrong --expect.
**From the first cell that starts after clbqcs03** (the statement block's first cell), the row runs on the first dir again. ADDENDUM 5's
fallback and its three triggers stand unchanged, so a repeat death moves the row to the second dir at $0, as ADDENDUM 6 recorded.
The first pool's all-models reading at the move was 86 % (the helm's hourly reader, 04:13 UTC), below trigger (c)'s 92 %.
**The mechanism of the earlier death** was measured by the harness's builder without a refresh: it was the first refresh of an 8-hour
access token, with copy and race both excluded by the bytes. Why the server refused remains unmeasured. It is not a cell-level confound:
no subject turn ran on a failing credential.
**Which dir each cell ran on** stays per cell, from `ctl/run-cfg.tsv`.

---

## ⚖️ ADDENDUM 9 — THE STATEMENT ROWS FIRE FROM CUT 4 = 5d3267b; THE `none` ROWS ARE COMPLETE ON 4d960d3. APPENDED.
**Why a cut, before any statement cell:** the route every `none` cell fired through carries a launch-fence re-assertion (`d0d54b5`). The
statement wiring (`898c7e2`, the hand-out pinned by blob per §X0 row 4) was built beside it, not on it, so firing from `898c7e2` alone
would have dropped a launch check the `none` cells had. **Cut 4 = `5d3267b` = `d0d54b5` + `898c7e2` + `245f0d8`** (the agy client reap, so
one cut serves both rows). It was cut by the harness's builder, and its tree `e6ec8048d128` equals the lead's merge-tree reading, with no
conflict.
**What differs from 4d960d3's export, by an independent file-sha diff on the run box:**
- the route `x86_clb.sh`: the statement condition, plus root-counting lines that run only in `--roots` mode;
- `agy_turnloop_v3.py`: the reap, agy row only;
- `studio_export.sh`;
- `STATEMENT-PIN.tsv` and its two hand-outs, whose landed copies hash to the pins: statement `630a37ba2545`, spec `b336720df2e1`;
- the provenance files: `EXPORTED-FROM.sha`, `RENDER-OVERLAY.txt`, and `REQUIRED-ANCESTORS.tsv`, whose only difference is the same
  authority commit written short.

Nothing else, and **nothing a `none` view or the referee reads**.
**Views, measured:** the builder's dry stage of all four conditions from cut 4 is rc 0. A cut-4 dry `none` view against a real 4d960d3
`none` view differs in two ways only, and both are explained:
- `absent` ancestor rows `up5..up7`: the dry cells sit three directories deeper;
- `tools/mnemonics.py`: the same member sets printed in a different order. Python's hash-randomised set order also differs between two
  real 4d960d3 cells, so it is a per-build nondeterminism, content-identical and arm-neutral. It is noted for the builder, not repaired.

⚠️ This export was taken with the toolchain check SKIPPED (a block N cell was live). The skipped check covers the Rust/Verus pins, which no
x86 cell uses; the lead's `898c7e2` export ran it on the same box minutes earlier and it read equal.
**`none` stays on 4d960d3** (complete at n = 3, PR #268). The statement conditions, both arms and both rows, fire from cut 4. Pooling across
the two cuts is never needed, because each condition runs on exactly one cut.

---

## ⚖️ ADDENDUM 10 — THE FALLBACK IS TAKEN ON TRIGGER (c), FROM THE STATEMENT BLOCK's THIRD CELL. APPENDED.
The helm's hourly reader recorded the first pool at **92 % all-models** (2026-09-26 08:25 UTC), with no reset taken. That is trigger (c) of
ADDENDUM 5, which sits below the wall so that no cell starts where it could meet 95 % mid-run. The live cell (clbkcs01, statement ·
salt-diet · #1) finishes on the first dir, because a cell is never interrupted. **From the next cell that starts, statement · plain · #2,
the row runs on ADDENDUM 4's second dir.** Its state was checked before that cell:
- no `chrome/` and no client temp file;
- the browser-integration default is still false (ADDENDUM 7);
- account check OK, both tokens present;
- 31 % all-models on the same reader.

**The return** to the first dir is taken, with its own addendum, only after the first pool is reset. Everything ADDENDUM 4 lists as unchanged
is unchanged. Which dir each cell ran on stays per cell, from `ctl/run-cfg.tsv`, and each condition's RESULT names the dir per cell.

---

## ⚖️ ADDENDUM 11 — THE FIRST POOL IS RESET; THE ROW RETURNS TO IT FROM THE STATEMENT BLOCK's FOURTH CELL. APPENDED.
The first pool's owner took its one-time reset at 2026-09-26 09:14 UTC. The helm's hourly reader recorded all-models 94 → 0; the weekly
reset date is unchanged. That discharges the condition of ADDENDUM 10's return clause. **From the next cell that starts, statement ·
salt-diet · #2, the row runs on the first dir again.** clbkcp02 (statement · plain · #2) finishes on the second dir, where it started.
The reset is a quota event, not a login: the first dir's credential is unchanged by it (cred_ledger reads it UNCHANGED), and it is
still the login of ADDENDUM 8. ADDENDUM 5's fallback and its three triggers stand. Which dir each cell ran on stays per cell, from
`ctl/run-cfg.tsv`.

---

## ⚖️ ADDENDUM 12 — THE AGY ROW's `none` PAIR FIRES FROM CUT 4 = 5d3267b, BY CONDITION. APPENDED.
**Why cut 4 for the agy `none` pair.** ADDENDUM 9 kept `none` on 4d960d3, and that sentence was written about the CLAUDE row: its `none`
pair was complete there at n = 3 (PR #268). The AGY row's `none` pair has not fired. Its salt-diet smoke (xass01) ended with an orphaned
client tree, and its slice was held on the client reap (`245f0d8`), which only cut 4 carries. ADDENDUM 9's file-sha diff names everything
cut 4 changes against 4d960d3. Of those changes, the reap is the only one on the agy row, and nothing a `none` view or the referee reads
differs. **So the agy `none` pair fires from cut 4.** Each condition still runs on exactly one cut: Claude `none` on 4d960d3, agy `none`
and every `statement` condition on cut 4. No pooling across cuts is needed.
**Measured by the hand before this release, at zero spend** (gemini, 2026-09-26, the run box, inside an existing root, no new `$HOME`
entry): a dry render of both arms from cut 4 reads BUILT · FENCE RENDERED · BATTERY GREEN · DRY RENDER COMPLETE. The launch `--check` is
rc 0 on both arms, and the briefing-token walk is OK on both. The walk's control, the pre-640d6b4 dry cell, still refuses. The canary
`--plan` is clean: 2 conditions, 6 cells, into staged roots.
**ORDER: by CONDITION, not by cell.** §X2's per-cell interleave (plain#1 · salt-diet#1 · #2 · #3) is REPLACED for the agy row's `none`
pair by plain ×3, then salt-diet ×3. The agy wave's unit is the condition, and its fresh-root guard gives one root per condition. An
interleave would need six roots created in quiet windows while block N is live, and the time order it buys is not worth that.
⚠️ **Declared as a confound of the agy row, before any cell:** the salt-diet cells run hours after the plain cells, on the same caps, the
same credential and the same box. A drift in the served model or in the agy pool over those hours falls on salt-diet alone. Its sign is
not registered. The Claude row interleaved, so this confound is the agy row's alone, and its RESULT prints it beside every agy table.
**Unchanged:** the model (gemini-3.1-pro-high), the caps (level 6 §H3), the referee (`referee_x86.sh`), §X3's smoke reading, and the
statement conditions' own cut (ADDENDUM 9). The agy statement pair is not released by this addendum. Its wave wiring is still being
built, and it fires on its own release line.
