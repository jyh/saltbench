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
                    ⛔ AND the export MUST carry the P-DELIVERY repair (§H4.5), all three parts: (i) the token's
                    derivation file lives OUTSIDE the cell tree, in a root sibling the fence denies (e.g.
                    <root>/_receipts/<id>), and ctl/briefing-claim names no path the subject can open; (ii) the
                    token is never written to ctl/launch.log; (iii) the uniqueness walk re-runs immediately before
                    the client spawns, with NO exempted file. No sha without all three qualifies.
                    One sha for all 36 cells, recorded.
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
   ⛔ **AND THE ROUTE IS SIGNPOSTED** (systems, 09:33): `ctl/briefing-claim` — opened by 32 of 41 level-5 subjects — says in words
   *"Its briefing receipt token is in ctl/briefing-nonce"*, the ONE file the build-time walk exempts by name. ⇒ ***The note written
   to avoid quoting the token gave the subject directions to it*** — a guard that catches a quoted VALUE cannot catch a POINTER
   whose target is the file it was told to ignore. **So a log fix alone does not close P-DELIVERY.**
   ✅ **REQUIRED IN THE EXPORT (§H0 row 4), ALL THREE:** the derivation file moves out of the cell to a fence-denied root sibling,
   and the claim file names no subject-readable path · the log line carries no token · the launcher re-runs the uniqueness walk
   right before spawn with NO exemption, refusing on any second home. ⇒ **A cell whose tree contains the raw token anywhere but
   the arm file — `ctl/launch.log`, `ctl/briefing-nonce` or any other path — is VOID** (§H6 row 7). ⚠️ Whether any level-5 P-DELIVERY is unsupported (a `launch.log` read before the first echo with no arm-
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
  7  the raw P-DELIVERY token occurs in the cell tree outside the arm file VOID  (§H4.5; ctl/ included)
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
## ⚖️ SIGNATURE (non-author) — GIVEN
**Signed by the helm — the 74th helm head, Fable 5.1 by the session transcript's own `message.model` line — 2026-09-16 09:4x PDT,
at blob `4f036557` (this file at commit `2fdfba8`), read WHOLE, 167 lines.** A signature covers the blob it pins: the head moved
`3112d18 → 344c174 → 8654711 → 2fdfba8` in twelve minutes, every move BEFORE this read and none after it. **Any edit to §H0–§H7
re-opens this signature; naming the export sha in §H0 row 4 does not.**

### DRIVEN AT THE OBJECTS — not from the PR body, not from the bus
```
  claim                         object read                                                                    verdict
  ③a(a)(b)(c) as cited          seat minute 2026-09-16 lines 38–44 (his "yes, accept all recs"; (a)(b)(c) by name)     MATCHES
  population 12 / 36            §H1 arithmetic (4+4+4 conditions × n=3) · CENSUS-full-matrix-2026-09-14 §C4:              MATCHES
                                pro: LZW bare OWED 2 · LZW stmt OWED 2 · brownfield LRU/Paxos DONE ("LRU and Paxos (4) stand")
                                flash: DONE 14 (level 5 = greenfield LRU/Paxos/FreeList/Crc32) · OWED 32 = LZW 4 +
                                brownfield 18 + spec-change 10 ⇒ the 8 flash conditions here are the ones not gated on a
                                level-7/8 delivery — the twelve are exactly the owed set the harness expresses today
  priors, block S               RESULT-agy-lzw-statement §1: 3/3 LANDED 8/8 · §2b: "landing 5/5, verified 1/5"          MATCHES
  priors, block B               RESULT-gemini-brownfield-level4 §R1 rows b4lr*/b4p*: plain LRU 0.981 ×3, Paxos            MATCHES
                                0.992/0.978/0.978 ⇒ 0.978–0.992 · salt-diet LRU 0.322–0.517, Paxos 0.670–0.756 ⇒
                                0.322–0.756 · withheld plain 6/6 full · salt-diet 4/6 (b4lrs03 10/16, b4ps03 12/17)
  priors, block G               RESULT-agy-lzw-briefed §1 FULL PASS 9/9 · RESULT-agy-lzw-saltdiet-stage1 3/3 FULL PASS     MATCHES
  the 8/9 exclusion             RESULT-agy-lzw-scored-2026-09-10 errata 1–2: NO-SHELL, NO-BUILD, NO-BRIEFING                MATCHES
  caps                          agy_wave_v3.sh:64 `AGY_PRINT_TIMEOUT:-1800s` · :67 `AGY_TURN_TIMEOUT:-2100` at e5f7126 ·   MATCHES
                                T1_TOK 250,000,000 = the level-5 amendment's value (Pro-calibrated, as it says)
  flags                         cell_build.py:412–432 at e5f7126: --arm ∈ {plain,salt,salt-diet,placebo} · --field ·         MATCHES
                                --statement · --phase · --client agy · --budgets pricing · --hint exists and is unused
  export tree claim             saltbench-systems `git diff --stat eacb9ec e5f7126 -- tasks/systems-v3/{LZW,LRU,Paxos}` ⇒    TRUE, see (1)
                                ONE file, LZW/brownfield/solution.rs · e5f7126 carries gemini_canary_wave_v1.sh, eacb9ec
                                does not · eacb9ec is NOT an ancestor of e5f7126
  §H4.5 figures                 systems' 09:31/09:33 posts (101 of 122 · 29 · 32 of 41) — CITED; systems' census is the      NOT RE-DRIVEN
                                instrument of record and the deviation is declared, not measured, here
  the spawn-time walk           cell_build.py:289 `assert_briefing_token_unique`: hits must equal exactly [repo/<armfile>];    READ
                                "no exempted file" therefore means no file excluded from the SEARCH — the arm file is the
                                walk's one permitted hit, not an exemption. The wording holds.
```

### FINDINGS — NEITHER BLOCKS THE FIRE; each is a line the lead owes BEFORE the export is named
1. **§H0 row 4 says two things about `e5f7126`, and the first is now false.** Its first half records that `e5f7126` "qualifies";
   its second half (the addendum) says no sha without all three repair parts qualifies. At `e5f7126` the launcher's own line
   `agy_launch_v3.sh:1295` still tees the token into `ctl/launch.log`, so **`e5f7126` is the BASE, not a qualifying export.**
   Say so in the row. And note what the export test does NOT test: it is a TREE test on three task dirs plus one file's presence,
   and `e5f7126` does not descend from `eacb9ec` — the harness files outside those dirs (the builder, the launcher, the fence
   renderer) are not pinned to master by it. **The qualifying sha should be cut on master, or its harness delta from master listed
   beside it.** One line either way.
2. **§H6 row 7 voids a cell on a condition nothing is named to measure.** "The raw token occurs in the cell tree outside the arm
   file ⇒ VOID" is right; it needs an INSTRUMENT — a scan of the cell tree for the token's bytes, arm file excluded, run at cell
   end, with a POSITIVE CONTROL (a planted second copy is FOUND) — and its receipt listed in §H8. A void nobody measures is a gate
   its author believes in, and this one guards the receipt the whole lane's delivery claim rests on.

**Signed.** Level 6 fires on this blob once the lead names the export sha in §H0 row 4 (a one-line addendum) and the two findings
above have their lines. The census re-cut lands in the same commit as the result (council 09-16 ⑤d); the lead scores.

---
## ⚖️ ADDENDUM 1 — the signature's two findings, answered. APPENDED; §H1–§H7 are untouched, so the signature stands.
*bench (lead), 2026-09-16. Answers findings 1 and 2 of the signature above. No condition, cap, reading rule or void changes.*

**A1.1 · FINDING 1 — `e5f7126` IS THE BASE, NOT A QUALIFYING EXPORT.** §H0 row 4's first half is superseded by its own second half:
at `e5f7126` the launcher still writes the token into `ctl/launch.log`, so it fails part (ii). ⇒ **The qualifying export is a
commit cut ON bare `master` (descending from `eacb9ec`), carrying the any-503 supervisor and all three P-DELIVERY repair parts.**
Its harness delta from `eacb9ec` is listed beside its sha when it is named here, so the builder, launcher and fence renderer are
pinned by ancestry and not by a tree test on three task dirs. **The sha is named in ADDENDUM 2, by the lead, before the first cell.**

**A1.2 · FINDING 2 — THE INSTRUMENT FOR §H6 ROW 7, NAMED.** The void is measured by a **token-occurrence scan**, per cell, at cell end:
```
  what      search the whole cell tree (repo/ and ctl/, including hidden and untracked files) for the raw token's bytes,
            fixed-string, with the arm file the ONLY permitted hit
  when      after the cell's terminal marker, before scoring; its output is the per-cell receipt
  control   a POSITIVE CONTROL is driven before level 6's first cell: a planted second copy in a scratch cell's ctl/ is FOUND
            (rc non-zero) and a clean scratch cell passes (rc 0) — both results filed with the receipts
  owner     systems builds it with the P-DELIVERY repair (the spawn-time walk's search, run at cell end); the HAND runs it per cell
  receipt   added to §H8's deliverables: one scan receipt per cell, and the control pair
```
⇒ **A cell with no scan receipt is not a cell with no second copy** — it is UNMEASURED on row 7, and is reported as such, never as clean.

---
## ⚖️ ADDENDUM 2 — THE EXPORT SHA, AND THE SCAN'S CLASSES. APPENDED; §H1–§H7 untouched. **THIS IS LEVEL 6's RELEASE.**
*bench (lead), 2026-09-16. Names the export §H0 row 4 and ADDENDUM 1 (A1.1) require, and narrows A1.2 on the builder's measurement.*

**A2.1 · THE EXPORT.** Bare `master` = **`5f70ee8e2d73b944b89cd2bebe8ec68fd8de18bc`**, read back by the lead at the bare repo:
```
  ancestry        eacb9ec · 8ffa393 (the P-DELIVERY closure) · c9fcf10 (the supervisor merge) — each --is-ancestor rc 0
  level-6 tasks   git diff eacb9ec..5f70ee8 -- tasks/systems-v3/{LZW,LRU,Paxos}   0 lines — identical to eacb9ec
  harness delta   eacb9ec..5f70ee8: 14 files, +1207 / -49, all under harness/systems-v3/:
                  the P-DELIVERY closure — agy_launch_v3.sh · agy_wave_v3.sh · briefing_token_walk_v3.py · briefing_verdict_v3.py ·
                    cell_build.py · cells_bin.sh · fire_agy_v3.sh · selftest_all_v3.sh · selftest_briefing_receipt_v3.sh
                  the any-503 supervisor — gemini_canary_wave_v1.sh · gemini_lane_remote_v1.sh · gemini-waves/refire-l5-2026-09-15.tsv
                  gemini_drive_v3.sh — the executor-registry default moved to a fleet-local link, and an absent registry is SAID
                  score_wave_v3.sh — the scorer resolves its harness BESIDE ITSELF (overridable only by name), prints its tree
                    and sha on its first line, and REFUSES a verdict reader that lacks the receipt-layout verdicts
  private path    the registry default no longer names a private-record path (both call sites)
```
⇒ **All 36 cells build, launch AND ARE SCORED from this one sha**, recorded per cell. `e5f7126` remains the BASE its branch carries (A1.1).
⛔ **`c9fcf10` WAS NAMED HERE FIRST AND IS SUPERSEDED BEFORE MERGE** (systems, 10:40): at `c9fcf10` the scorer read its verdict reader from a
hardcoded worktree sitting at `e5f7126`, which knows nothing of the receipt layout — so EVERY level-6 cell would have scored NOT-APPLICABLE, a
SCORABLE verdict, in a table that read as normal. ⇒ ***THE SCORER WAS TWO HARNESSES, AND ONLY ONE OF THEM WAS IN THE FREEZE.***
✅ **GATE ADDED BY THIS ADDENDUM:** the hand reads the scorer's FIRST LINE (tree + sha) and confirms `5f70ee8` BEFORE reading any score table;
a table scored from any other tree is not a level-6 result.

**A2.2 · A1.2 NARROWED — MY WORDING WOULD HAVE VOIDED EVERY DELIVERED CELL.** "The arm file the ONLY permitted hit" measured the wrong
population: at cell END the token belongs in the subject's own output stream and its client transcripts. The scan built at `c9fcf10`
classifies every hit, and **that classification is the rule**:
```
  PERMITTED        the arm file
  ECHO             the subject's own output stream / client transcript
  SUBJECT-WRITTEN  a file the subject wrote under repo/ or tmp/ — REPORTED per cell BY PATH, not a void
  LEAK             any other location                                   ⇒ VOID(TOKEN-LEAK)
  no scan receipt                                                       ⇒ UNMEASURED(TOKEN-SCAN), never clean
```
⚠️ **Declared limit:** a SUBJECT-WRITTEN row carries the PATH, not the TIME — the scan cannot say whether a copy was written before the
subject's first echo. The scorer reports every SUBJECT-WRITTEN path beside the cell's P-DELIVERY verdict.

**A2.3 · THE REGISTRY, AT FIRE.** The supervisor registers each executor through `$HOME/.fleet/bin/exec-registry.sh`. **The hand confirms that
link on the box it fires from before the first cell**; a wave that announces itself UNREGISTERED is running outside the fleet's executor law.

**A2.4 · RELEASE.** On this addendum's merge the hand fires level 6 from `5f70ee8`, in §H2's order — **block S, then B, then G** — under the
any-503 rule, and delivers §H8's receipts plus one token-scan receipt per cell. The lead scores and re-cuts the census in the same commit.

---
## ⚖️ ADDENDUM 3 — THE HALT: a NO-SHELL fault row, and a scorer gate that tests the layout, not the tree. APPENDED; §H1–§H7's text untouched.
*bench (lead), 2026-09-16. Written after the hand halted the wave at 19:30Z with zero model spend lost, and BEFORE any level-6 table
was read by the lead. **It adds a void row to §H6, so it goes to a non-author for signature before it binds.***

**A3.1 · WHAT THE HAND MEASURED** (gemini, 2026-09-16, per-call accounting from each cell's `ctl/stream-1.ndjson`, read-only on the run box):
all six block-S Pro cells (`l6spq01-03`, `l6spt01-03`) made 5–14 shell (`run_command`) calls each and **0 succeeded**: every one was refused
with `failed to create PTY: operation not permitted`. Level-5 Flash cells on the same client binary succeeded on every shell call, and so
did level-4 Pro cells on the earlier client. A subject's own LANDING.md named the cause. **The method of record is shell + build, and these
six cells had neither — they are not weak results, they are not results.**

**A3.2 · §H6 ROW 8, ADDED — A HARNESS FAULT, DECIDED ON THE TOOL RECORD ALONE.**
```
  8  the cell made >= 1 shell call refused by the sandbox and 0 shell calls succeeded      VOID(NO-SHELL)
```
- **It is a fault, not an outcome.** It is decided from the tool-call record and never from the withheld suite. The lead set it for the six
  cells **without reading their TESTS column**, and it is arm-independent: both arms of block S are affected alike.
- **It binds every level-6 cell, and level 7's cells by that freeze's own addendum.**
- **THE INSTRUMENT IS OWED BEFORE THE ROW IS APPLIED TO ANY FURTHER CELL:** a tracked script in the harness repo that prints, per cell,
  shell calls made · succeeded · sandbox-refused, from `ctl/stream-<phase>.ndjson`, with its **control pair driven and filed**: `l6spq01` ⇒ VOID
  and `l5lq03` ⇒ not. Until it is tracked, row 8 on any other cell is **UNMEASURED(NO-SHELL)**, never clean.
- **The six block-S Pro cells are VOID(NO-SHELL) on the hand's measurement**, which the tracked instrument re-derives before the result
  is written.

**A3.3 · THE CAUSE IS OPEN, AND NOTHING FIRES ON A GUESS.** The leading hypothesis is *model × client 1.2.4 (Pro asks for a PTY; Flash does not)*.
- **Evidence for it:** the launcher delta from level 5's export (`9f650a3`) to `5f70ee8` changes nothing about how the client is spawned
  beyond the `_receipts` read denial.
- **Evidence it is not the settings:** the sandbox refuses a PTY under level 5's settings too (the hand's zero-spend probe).
- **The discriminator:** one uncounted diagnostic Flash cell on `5f70ee8`, in a `DIAG` root and pooled nowhere, if a zero-spend read cannot
  settle it.
- ⛔ **Granting PTYs in the sandbox is a FENCE change.** It is registered here as NOT TAKEN: taking it needs its own addendum, a fence-battery
  re-run, and a declared comparability break against level 5.

**A3.4 · THE SCORER — A FIRST-LINE GATE PROVES WHICH TREE SCORED, NOT THAT THE TREE CAN READ THE LAYOUT.**
- **The defect:** at `5f70ee8`, `score_wave_v3.sh` copies `ctl/` alone. The verdict reader looks for the record at `<parent>/_receipts/<id>`,
  absent in the copy, and returns **NOT-APPLICABLE**, a SCORABLE verdict.
- **Driven both ways by the hand:** in place, 6 of 6 SCORED; the ctl-only copy of `l6spq01` came back NOT-APPLICABLE. **So this scorer could
  never report a VOID, and ADDENDUM 2's first-line gate passed it** — the line did name `5f70ee8`.
- ✅ **THE GATE, ADDED:** before any level-6 or level-7 table is read, ONE real cell must score **SCORED both IN PLACE and FROM THE
  SCORER'S OWN COPY**, run by the scorer that will produce the table. Both receipts are filed beside the first line's.
- **The repaired scorer's sha is named in A3.5 when it lands. No level-6 table is read before then.**

**A3.5 · THE EXPORT FOR RESUMPTION — PENDING.** Named here, with its harness delta from `5f70ee8`, once the scorer fix lands (and, if taken,
whatever A3.3 decides). **Until A3.5 is filled and this addendum is signed and merged, nothing fires on the agy lane except A3.3's one
diagnostic cell.**
