# AMENDMENT — O37 BLOCK TW: WHT AND NTT × `statement`, GREENFIELD, CLAUDE LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-11-22. The form is block T's, `AMENDMENT-O37-statement-six-claude-2026-11-11.md` (signed; ADDENDA 1–5;
## its result of record `RESULT-claude-blockT{O,S}-2026-11-22.md`), cited below as "block T", carried BY CITATION. The two problems are
## block W's, `AMENDMENT-O37-wht-ntt-greenfield-claude-2026-11-11.md` (signed; its result of record `RESULT-claude-blockW{O,S}-2026-11-15.md`),
## cited as "block W". A clause that differs from either says so and why.
## Authority: block N's (the Captain's council word of 2026-09-25: the remaining problems run on bench at P3), as block T's.
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL IS BUILT BEFORE THE CAPTAIN HAS READ THE TWO STATEMENTS** (the statement
## arm §2; his council 2026-11-14 ruling 6 read block T's six, not these two), **AND NO CELL FIRES BEFORE A RELEASE ADDENDUM NAMES THE
## EXPORT SHA, THE POOL, AND EACH §TW2 RECEIPT AS MET.**

---
## §TW0 · THE INPUTS (block T §T0, row by row)
```
  1  MODEL IDs   claude-opus-5 · claude-sonnet-5, block T row 1 unchanged. Re-measured served at release by a zero-cell probe.
  2  n           3 per condition.
  3  POPULATION  8 conditions, 24 cells (§TW1).
  4  EXPORT      ONE bare-master sha of saltbench-systems, cut by a studio_export.sh that writes the listing marker, carrying (i) the
                 WHT and NTT `## Statement` sections at the blobs §TW2 item 1 names, (ii) block T's export 7fe4ff7f as an ancestor,
                 (iii) the stager's export-marker check (saltbench-systems 6d852677, the lead's queue row 8, a non-author read owed),
                 and (iv) the watcher's exit-wait beat (systems' 1eba956e, row 9). A DEPARTURE from block T's export, declared: (iii)
                 and (iv) are harness changes since 7fe4ff7f; neither touches tasks/, the referee, the leak checker or the builder.
  5  CLIENT PIN  block T row 5, re-driven at release. ⚠️ A client past 2.1.259 sets "idleCompaction": false in cell settings (the lead's
                 ruling of 2026-11-20, bus offset 107,406,746): declared at release with its schema probe, if the pin moves.
  6  TASK TREE   the EXPORT's tasks/systems-v3, and nothing else. Every cell is built with `cell_build.py --statement`.
  7  CAPS        block T row 7 unchanged: C1_USD $37.21, W1_SEC 144,000; CAP-COST and CAP-WALL armed.
  8  ACCOUNT     P3: a pool the PM names at release, never ahead of P1/P2 work, `cells_account_check.sh` OK before each fire.
  9  FIRE ORDER  §TW3. Every fire through the lead's local gate (refuses in a sitting on the box where the helm sits).
```

## §TW1 · THE POPULATION — 8 CONDITIONS, 24 CELLS
```
  problems   WHT · NTT                                                         block W's two
  models     claude-opus-5 · claude-sonnet-5
  arms       plain+statement · salt-diet+statement                             the statement arm's (d) and (e)
  field      greenfield            extras   statement
  ⇒ 2 × 2 × 2 = 8 conditions · × n 3 = 24 cells
```
These are 8 of the 24 WHT/NTT conditions the census lists NOT DONE (`CENSUS-full-matrix-2026-09-14.md` ADDENDUM 49 §AT2: "x statement,
both lanes; x spec-change, agy lane"). The agy lane's 8 WHT/NTT statement conditions are a sibling's to freeze.

## §TW2 · ⛔⛔ THE ITEMS — EACH DRIVEN, WITH A CONTROL, BEFORE THE CELLS IT GATES
1. **THE SECTIONS REPRODUCE FROM THE TOOL** (block T §T2 item 1). Each section is the output of `extract_statement_v3.py <ref> --names
   <verify.names> --interface <interface.rs> --check --carry-consts` on the export's own reference. The release re-derives both and `cmp`s
   them against the cards. Measured on the T export candidate (7fe4ff7f) at this writing: neither section carries a constant, and the
   cards say the extractor with and without `--carry-consts` produces byte-identical output for both.
2. **THE CAPTAIN HAS READ BOTH** (the statement arm §2). ⛔ OPEN: his read of block T's six does not cover these. His word is recorded in
   the release.
3. **SIZES, RECORDED** (block T §T2 item 3). The section's own bytes (the `rust` block under the card's `## Statement`, T export candidate):
   ```
     WHT   card.md 11,620 B · section 3,466 B · 20 spec fns · contracts of wht, iwht, check_trace
     NTT   card.md 12,328 B · section 3,286 B · 18 spec fns · contracts of ntt, intt, cyclic, check_trace
   ```
   The rendered card's bytes before and after `--statement` are recorded at the release from the built view. Both sections are about a
   third the size of block T's smallest (MaxFlow's 4,140 B rust block) and carry no constant.
4. **NEUTRALITY ON A BUILT VIEW PER PROBLEM AND ARM**: the cell build's own gate, re-driven at the export (4 dry cells), with a planted
   "theorem" in one section REFUSED as the control.
5. **THE ACCOUNT CHECK, NO LEAK INTO A VIEW, THE ZERO-CELL PROBE**: block T §T2 item 5, unchanged.
6. **THE STAGER REFUSES A NON-EXPORT** (new, from queue row 8): `export_marker_check.sh` reads OK on the release export, and the stager's
   selftest arm `export-marker` is green on the export's own harness. Control: the quarantined full-tree cut refused.

## §TW3 · THE ORDER, THE TRIPWIRES
Block W §W3's order (WHT → NTT; per problem plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3), models interleaved.
Tripwires: `TW-O` = Opus · WHT · salt-diet+statement#1 · `TW-S` = Sonnet · the same. Each is read and posted before its model continues,
the reading list block T §T3's, including the statement line (did the subject use, ignore, or contradict the statement), read in block
T's categories with USED checked by line position and the subject's own clean run.

## §TW4 · CAPS, PREDICTIONS AND THE PRICE — REGISTERED BEFORE ANY DATA
Caps: block T §T4. Predictions, per model, where a miss is a result: (i) within a condition, salt-diet+statement's CAP-COST incidence is ≥
plain+statement's; (ii) CAP-WALL binds no cell. No prediction about pass rate or premium.
**The price**, printed by `evidence/blockTW-2026-11-22/tw_price.py` (output `tw_price.out`) from three tracked tables, nothing typed:
block W's own metered spend on WHT/NTT (`extras = none`), scaled per model × arm by block T's metered spend on the six over block N's
(the statement arm against `extras = none` on the same six problems):
```
opus   plain     N six 18 cells $255.56 · T six 18 cells $276.02 · ratio 1.080 · W WHT/NTT 6 cells $49.36 -> $53.31
opus   salt-diet N six 18 cells $415.43 · T six 18 cells $404.63 · ratio 0.974 · W WHT/NTT 6 cells $177.69 -> $173.07
sonnet plain     N six 18 cells $68.10 · T six 18 cells $59.47 · ratio 0.873 · W WHT/NTT 6 cells $10.52 -> $9.19
sonnet salt-diet N six 18 cells $514.54 · T six 18 cells $381.61 · ratio 0.742 · W WHT/NTT 6 cells $181.99 -> $134.97
block TW estimate $370.54 for 24 cells · ceiling 24 x $37.21 = $893.04, plus each cell overrun past the cap
```
Control on the inputs: block N's sums reproduce block T §T4's registered price per model (Sonnet $582.64 exact; Opus $670.99 against
$671.00, a cent of rounding in the registration). ⚠️ The ratio is measured on six OTHER problems, months apart (block T §T8.3), and is an
estimate whose direction of error is unknown. The WHT triple of each model re-cuts it before NTT fires.

## §TW5 · CONFOUNDS — block T §T5 carried whole, block W §W5 carried whole
1. Block T §T5.1–2: the statement arm is a stronger treatment by construction (a specification extracted verbatim from the withheld
   reference); the refuter's catch and the planted-ambiguity instrument are off by construction.
2. Block W §W5.1: **the two problems' author is the lead**, who also extracted their statements. §TW2 item 1's re-derivation by the tool
   and the Captain's read are the controls. A defect in a task or a section is a HARNESS finding, never an arm effect.
3. Block W §W5.2: **NTT's reference proves less than WHT's** (its butterfly is not proved equal to the sums), so NTT's extracted statement
   states what the reference's checker states, nothing about the butterfly. It is printed beside any table that sets the two side by side.

## §TW6 · READING RULES, §TW7 · VOIDS, §TW8 · WHAT THIS BLOCK CANNOT ESTABLISH
§TW6 = block T §T6 (every premium registered UNRESOLVED-UNDERPOWERED). §TW7 = block T §T7 whole, the section-`cmp` VOID row included
(read per cell as block T's result did, by `t_section_cmp.py`'s method on the card as built).
§TW8: 1. No magnitude, no effect size. 2. Nothing about Opus versus Sonnet. 3. Nothing about the statement arm versus `extras = none` across
blocks (block W ran on another export and pool). 4. Nothing about the six problems of block T, or about LU (declared not feasible).

## §TW9 · WHAT THE HAND DELIVERS
Block T §T9: a result of record per model, the per-cell statement line, the census's O37 section re-cut in the same commit. Any public
sentence, and any claim about the method, is the Captain's.

---
# ✍️ SIGNED — the helm (221st head), 2026-11-22 14:00 PST, bus offset 108,838,766: blob e3f04cd9d68c at head 48379c5e26f2, read whole
(100 lines, 9,137 B), **1 LOW**. It checked that the form is block T's and that every departure is declared (§TW0 row 4). It checked
the gates (no build before his read; no fire before a release addendum names the export, the pool and each §TW2 receipt), the
predictions (registered before data, no pass-rate or premium claim), the confounds (carried whole) and §TW8–§TW9. It re-derived the
price by hand: ratios 1.080 · 0.974 · 0.873 · 0.7417, sum $370.54, ceiling $893.04. **The LOW** is §TW2 item 3's size comparison,
corrected in ADDENDUM 1 below. Also owed before release: the non-author read of saltbench-systems 6d852677 (§TW0 row 4 (iii)).

---
# ADDENDUM 1 (2026-11-22, bench) — §TW2 item 3's size comparison, CORRECTED. APPENDED; the signed text above is unchanged.
§TW2 item 3 says both sections are "about a third the size of block T's smallest (MaxFlow's 4,140 B rust block)". That ratio was typed,
not computed. Computed: WHT 3,466 / 4,140 = 0.837 and NTT 3,286 / 4,140 = 0.794, so each is **about four-fifths** of MaxFlow's, and the
smallest statements of either block. No gate turns on it.

---
# ⚖️ ADDENDUM 2 (2026-11-23, bench) — RELEASE, ⛔ DRAFT: NOT A RELEASE. BUILT AHEAD OF HIS READ (§TW2 item 2). APPENDED.
Every receipt that can be driven before his read, and without building a cell, is driven here on the export CANDIDATE. The rest are
marked OPEN. This heading loses its DRAFT mark only in a later addendum that records his word, names the export as cut and the pool, and
fills every OPEN row. Nothing in this addendum builds or fires a cell.
**Export candidate: saltbench-systems `6d7f398f`** (§TW0 row 4; backup branch `bench/o37-TW-export-candidate-2026-11-22`). The WHT and NTT
task trees there have git tree ids WHT 44b92115d240 · NTT 77c641773103, which are equal at WA Pro's export 3fd5edf1 and at the agy hook export
candidate aa071afc (block TWA's §TWA0 row 4 cites this).
**§TW2 receipts:**
1. **MET at the candidate, 2026-11-23, on the lead's workstation** (the files read by `git show 6d7f398f:<path>`, no export cut): `extract_statement_v3.py
   <ref> --names <verify.names> --interface <G/interface.rs> --check`, run with and without `--carry-consts`, rc 0 in all four runs. Each card's
   ```rust block under `## Statement` `cmp` EQUAL to the extractor's output: WHT 3,466 B (sha256/16 06099b2de83edec7) · NTT 3,286 B (sha256/16
   f4e431a069a515ce). With and without `--carry-consts` the output is byte-identical for both. Control: the WHT block with one line appended
   reads DIFFER. The release re-drives it on the export as cut, or cites this drive with the two tree ids shown equal there.
2. ⛔ OPEN: the Captain's read of both sections (the pack's ask 2). His word, with its minute line, is recorded in the release.
3. MET: the sizes above equal §TW2 item 3's table (3,466 B and 3,286 B), with ADDENDUM 1's correction.
4. ⛔ OPEN by the gate: neutrality is driven on BUILT views, and no cell is built before his read. At the release: 4 dry cells at the
   export as cut, with the planted-theorem control.
5. **MET at the candidate's task tree, 2026-11-23, on the lead's workstation** (a detached worktree of 6d7f398f, removed after the run):
   `check_withheld_leak_v3.py --tasks tasks/systems-v3` CLEAN: 343 identifiers across 13 tasks, every positive control fired, 1,372 view-file
   reads, 0 in any view (WHT 30 and NTT 28 identifiers screened). The release re-runs it on the export as cut.
6. ⛔ OPEN: `export_marker_check.sh` on the export as cut, and the stager's `export-marker` selftest arm on its own harness, with the
   quarantined full-tree cut refused as the control.
**Also OPEN at the release:** the pool (the PM names it, P3), the zero-cell served-model probe and the account check (§TW2 item 5), and the client pin (§TW0
row 5, with the `idleCompaction` declaration if the pin moves).
**Hand:** bench. **Order:** §TW3 as registered (`TW-O`, then `TW-S`, each read before its model continues).

---
# ⚖️ ADDENDUM 3 (2026-11-23, bench) — THE RELEASE. ADDENDUM 2's open items are filled here; this heading is the release. APPENDED.
The repo appends to a frozen file and never edits it, so ADDENDUM 2's heading keeps its DRAFT mark. Its condition is met by this addendum.
**§TW2 item 2, his read: MET.** Council 2026-11-23, ask 2 (the council minute of 2026-11-23, item 2, seat blob afbe23b67bcc):
after an English reading of both statements, his words were *"yes, readd and approved"*. That accepts NTT's weaker statement as registered
(§TW5.3). What he read is seat blob a859f1d2a31c. Its two ```rust blocks are byte-equal to the cards at the export below: WHT 3,466 B and
NTT 3,286 B, compared by script.
**CORRECTION TO ADDENDUM 2 item 1:** the two sha256/16 values there are attached to the wrong problems. Measured twice (a python parse and an awk
cut of each card's block at the export): **WHT 3,466 B is f4e431a069a515ce, NTT 3,286 B is 06099b2de83edec7.** The seat brief he read
(the seat brief at blob a859f1d2a31c, its WHT and NTT headings) has them right. The sizes and the `cmp` verdict in ADDENDUM 2 stand.
**Export: saltbench-systems `e4f786fe`** (backup branch `bench/o37-TW-stager-2026-11-23`) = the candidate 6d7f398f + ONE commit, the TW
stager. ⚖️ **A DEPARTURE FROM §TW0 row 4, DECLARED:** at 6d7f398f no block could stage a TW cell, because blocks TO/TS are freeze T and the scope
rule refuses W's problems there. e4f786fe adds blocks TWO (letter a, Opus) and TWS (letter p, Sonnet), greenfield × statement, freeze TW,
to clb_stage.sh, clb_fire.sh and clb_harvest.py, in the same shape as block T's 2505998e, plus the fixture `clb_blockTW_selftest.sh`. It
touches no tasks/, referee, leak checker, extractor, builder or neutrality grep: against 6d7f398f, `tasks/systems-v3` (tree e2cbc84cbfba),
`referee_v3.py`, `check_withheld_leak_v3.py`, `extract_statement_v3.py`, `cell_build.py` and `neutrality_grep.py` are byte-identical (git tree
and blob ids equal). The fixture: this tree 14/14 GREEN (lane B stage and fire parity on 870 combos; block W's WO/WS and block T's TO/TS
parity, 32 combos; 24 TW ids and 8 roots, none colliding; 44 cross combinations refuse naming this freeze; `--roots --freeze TW` = 8, 4 Opus
and 4 Sonnet). The 6d7f398f scripts go RED on exactly the 7 TW arms (b1–b4, c1, d2, d3). Its non-author read: systems, CONCUR, no logic fault (bus offset 109,827,304, 2026-11-23 10:52 PST). It reproduced 14/14 and ran three mutants: two were killed (the fire scope clause, the --freeze TW problems line). The third, TW's letters dropped from clb_harvest, SURVIVES: no fixture arm covers clb_harvest's table, so a missing letter would show only as a KeyError at harvest. That is declared LOW and owed to a later export, together with the pre-existing gap systems found (block G's letter k is absent from clb_harvest; the same at 6d7f398f). With TW the block letters a–z are all in use.
Cut on the run box by `studio_export.sh --no-toolchain`: 426 files, listing sha256/16 76b33cc7b5817107, withheld-shaped names 0 in the
listing and 0 on the host, marker written last.
**§TW2 receipts at the export as cut:**
1. MET by citation: the WHT and NTT task trees at e4f786fe are 44b92115d240 and 77c641773103, equal to 6d7f398f's, and the extractor blob is
   unchanged, so ADDENDUM 2's drive stands (with the correction above).
3. MET (ADDENDUM 2; the trees are unchanged).
4. MET 2026-11-23 18:32Z on the run box: 4 dry cells (WHT × Opus and NTT × Sonnet, × plain and salt-diet) built by the export's own stager
   (`clb_stage.sh … --dry`, so `cell_build.py --statement`) into a scratch cells parent under ~/bench-dry. All rc 0, each "card-extras
   statement". `ctl/neutrality.log` reads "neutrality: zero hits" in 4 of 4. REQUIREMENTS.md is identical across the two arms of each problem
   except the work-order nonce line, and carries one `## Statement`. Control: a copy of the export with one line `// theorem: planted`
   inside WHT's ```rust block REFUSED in both arms (neutrality 2 hits; the stager's rc 3).
5. NO LEAK — MET 2026-11-23 at e4f786fe (a worktree on the lead's workstation): `check_withheld_leak_v3.py --tasks tasks/systems-v3` CLEAN, 343 identifiers across
   13 tasks, every positive control fired, 1,372 view-file reads, 0 in any view (WHT 30, NTT 28).
   THE ACCOUNT CHECK — MET 2026-11-23 18:33:39Z: `lane_identity.py --expect` against the pool's REGISTERED digest (the one block T's lane env for
   this pool carries) read IDENTITY OK, refresh token present. Control: a digest one character off returns rc 5.
   THE ZERO-CELL PROBE — MET 2026-11-23 18:33:44Z–18:33:51Z, block WC's form: pinned client 2.1.259 (sha256/16 884baa38fe1a624b, asserted),
   one `-p` turn per model. claude-opus-5: rc 0, reply `OK`, `message.model` set exactly {claude-opus-5}. claude-sonnet-5: rc 0, reply `OK`,
   set exactly {claude-sonnet-5}. Spend $0.1080 on the pool, outside every cell's meter. `modelUsage` lists a Haiku id on each turn, the
   client's own side call, which appears in no assistant message (as in T and WC).
6. MET 2026-11-23: `export_marker_check.sh` on the export as cut: OK (e4f786fe25c0, 426 files, listing 76b33cc7b5817107, withheld-shaped
   paths 0). The export-marker selftest is green on the same commit's harness, 19/19 (run on the lead's workstation worktree at e4f786fe, because the
   selftest re-exports from a git HEAD and an export carries no .git). Control: both quarantined T cuts (09516b81, 7fe4ff7f) REFUSED, rc 2.
**Client pin (§TW0 row 5):** 2.1.259 (sha256/16 884baa38fe1a624b), block T's, asserted by the stager at every stage ("CLIENT PIN OK"). The
pin did not move, so no `idleCompaction` declaration is owed.
**Pool: pool 1 (block T's Luby pool and block WC's), at P3.** The PM's report of 2026-11-23 (§1) names it in advance: block TW landing on
this pool this week "spends the slack, the intended outcome", with the pool on DRAIN to ~95 until its 18:59 PST reset that day. The PM's
seat is held to its 11-24 cut, so the helm reads this naming. Each launch runs under the fleet's day-line check for this pool. At 10:3x
PST it read LAUNCH, all 72 against 95. The lane env is block T's env for this pool with ONE line changed (the export).
**Roots:** created 2026-11-23 18:52:36Z on the run box in a quiet window (no client, watcher, fire, verus or cargo process): `clb_stage.sh
--roots --freeze TW` from the export, under this block's lane env, rc 0. There are 8 roots with `_bin` linked into e4f786fe, and each root's model
table was read back (4 Opus, 4 Sonnet, equal to the registered 8).
**Order:** §TW3 as registered. WHT first, models interleaved. `TW-O` = Opus · WHT · salt-diet+statement#1 fires first, and the lead reads it
before Opus continues (block T's reading list plus the statement line). `TW-S` = Sonnet · the same, likewise. The WHT triple of each model
re-cuts the price before NTT fires (§TW4).
