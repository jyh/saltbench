# AMENDMENT — O37 BLOCK TA: BLOCK N's SIX PROBLEMS × `statement`, GREENFIELD, agy LANE. FROZEN BEFORE THE FIRST CALL
## bench (SaltBench lead), 2026-11-17. This is block T's sibling freeze (`AMENDMENT-O37-statement-six-claude-2026-11-11.md`, cited as
## "block T", §T1: "the agy lane's 24 statement conditions are a sibling freeze"). The lane form is block WA's
## (`AMENDMENT-O37-wht-ntt-greenfield-agy-2026-11-13.md`, signed, ADDENDA 1–6, cited as "WA"), which carries block NA's
## (`AMENDMENT-O37-nine-greenfield-agy-2026-09-25.md`, cited as "NA") by citation; the statement arm is the pilot's
## (`AMENDMENT-statement-arm-pilot-2026-09-09.md`, cited as "the statement arm"). A clause that differs from any of them says so and why.
## Authority: block T's and WA's (the Captain's council word of 2026-09-25: the remaining problems run on bench at P3), and his read of the
## six statements, council 2026-11-14 ruling 6 ("O37 accepted").
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** ⛔ **NO CELL FIRES BEFORE §TA2's ITEMS ARE DRIVEN AND A RELEASE ADDENDUM NAMES THE EXPORT
## SHA, THE CLIENT, AND EACH §TA2 RECEIPT AS MET.** Signature and release are two acts, as in WA.

**Why now.** The agy lane has had no fireable work since WA Pro ended on 2026-11-15. Of O37's 216 conditions, these 24 are the agy half of
block T's 48 statement conditions on the six; block T (the Claude half) is released to build and waits only on its pool.

---

## §TA0 · THE INPUTS (WA §WA0, row by row, as WA's ADDENDA 2 and 5 left it)
```
  1  MODEL IDs     gemini-3.8-flash-high · gemini-4-argon-high (WA ADDENDUM 2's Pro slot; today's client does not serve gemini-3.1-pro-high,
                   WA ADDENDUM 1). Re-measured served on the release's client by the lane-live battery; a served-model mismatch VOIDS.
  2  n             3 per condition.
  3  POPULATION    24 conditions, 72 cells (§TA1).
  4  EXPORT        ONE harness sha, named in the release. CANDIDATE: saltbench-systems 397864e8 (backup branch
                   bench/o37-TA-agy-export-candidate-2026-11-17) = WA Pro's export 3fd5edf1 with block N's six card.md files OVERLAID from
                   8bf04bdc, the cards the Captain read. Its harness tree equals 3fd5edf1's; outside the six card.md files the diff is empty;
                   every other file of the six task trees is already byte-identical between 3fd5edf1 and 8bf04bdc. For five cards the
                   overlay is the agy line's card plus the `## Statement` section; for LinearScan see §TA4 item 4.
  5  CLIENT        agy at the version and sha the release names. Settings carry `"agentMode": ""` (WA ADDENDUM 5, in 3fd5edf1's launcher).
  6  CAPS          WA row 5 unchanged (NA ADDENDUM 4's): T1_TOK 250,000,000 · AGY_PRINT_TIMEOUT 1800 s · AGY_TURN_TIMEOUT 2100 s; CAP-TOKENS,
                   CELL-KILLED and TURNS-CUT reported per arm, never a void; a truncated PASS is a FLOOR. No cap is raised.
  7  QUOTA         WA row 6 unchanged: P3, the agy pool, yielding to any O4 agy cell live or queued; /usage read at each fire and bank.
  8  TASK TREE     the EXPORT's tasks/systems-v3, and nothing else; every cell built with `cell_build.py --client agy --statement`.
```

## §TA1 · THE POPULATION — 24 CONDITIONS, 72 CELLS
```
  problems   Luby · AES · Liveness · MaxFlow · BinomialHeap · LinearScan     block N's six (block T's)
  models     gemini-3.8-flash-high · gemini-4-argon-high
  arms       plain+statement · salt-diet+statement                           the statement arm's (d) and (e); agy registers no `salt`
  field      greenfield            extras   statement
  ⇒ 6 × 2 × 2 = 24 conditions · × n 3 = 72 cells
```
Not in this block: spec-change on the six on the agy lane; anything on WHT or NTT.

## §TA2 · ⛔⛔ THE ITEMS, THE ORDER AND THE TRIPWIRES
**Items, each driven with a control before the cells it gates:**
1. **THE SECTIONS REPRODUCE FROM THE TOOL** (block T §T2 item 1): the six sections at the export `cmp` EQUAL to the output of the command each
   card names, run on the export's own references. Block T's release drove this at 7fe4ff7f (6/6 EQUAL, a one-byte control DIFFER); the
   six references and `verify.names`/`interface.rs` files are byte-identical between 7fe4ff7f, 8bf04bdc and 397864e8, so the release
   re-drives it on 397864e8 or cites block T's drive with that identity shown.
2. **HIS READ COVERS THESE BYTES.** The six sections are 8bf04bdc's byte for byte (the overlay copies the card files whole). The release
   shows the six blob identities beside ruling 6. ⚖️ **For the signer:** ruling 6 released BLOCK T; this block relies on the same read for
   the same bytes on the other lane. If the signer reads ruling 6 as not reaching the agy lane, the read is re-asked through the pack
   (DEFAULT: no TA cell fires until it is given), and nothing else here moves.
3. **SIZES:** block T §T2 item 3's table, unchanged (the same sections).
4. **NEUTRALITY ON A BUILT agy VIEW PER PROBLEM AND ARM.** Driven 2026-11-17 on the run box, dry, from a `studio_export.sh` cut of 397864e8
   into a scratch directory (387 files, 0 withheld-shaped names, required-ancestors 5/5): 12 cells built with `--client agy --statement`,
   all rc 0, "neutrality: zero hits" 12 of 12; Luby plain's REQUIREMENTS.md carries the section's ```rust block with sha256/16
   87bfc07df2886179, equal to the extractor's output. Control: a copy with one planted `// theorem: planted` line inside Luby's section
   REFUSED in both arms (2 hits, rc 4). Re-driven at the release's export.
5. **NO LEAK INTO A VIEW:** `check_withheld_leak_v3.py` over the export, every positive control firing.
6. **THE LANE IS LIVE ON THIS EXPORT** (WA §WA2 item 4 and ADDENDUM 2 condition 1): the agy battery on one dry cell PER MODEL on the
   release's client (credential window, served model, fence intact, TMPDIR identity, the TREE-HASH line), the client version and sha named.
**Order:**
```
  models     Flash first, then argon (NA §NA2's reason, as in WA)
  problems   block N §N3's: Luby → AES → Liveness → MaxFlow → BinomialHeap → LinearScan (block T §T3's)
  cells      per problem: plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3, through the wave supervisor
```
**Tripwires, each ONE cell, read by the lead before its model continues:** `T-TA-F` = Flash · Luby · salt-diet#1 · `T-TA-P` = argon · Luby ·
salt-diet#1. The reading list is WA's, plus block T's line: did the subject use, ignore or contradict the statement.

## §TA3 · PREDICTIONS AND THE PRICE — REGISTERED BEFORE ANY DATA
WA §WA3 carried: (i) within a condition, salt-diet+statement's TURNS-CUT and CAP-TOKENS incidence is ≥ plain+statement's; (iii) CELL-KILLED
binds no cell outside a declared 503 episode. ⛔ **No prediction about pass rate or premium.**
**The price**, in cell wall (WA ADDENDUM 2's unit; agy pool points per cell are UNMEASURED). Printed by
`evidence/blockTA-2026-11-17/ta_price.py` from three tracked files (block NA's cells table; WA Flash's and WA Pro's cells), output
`ta_price.out` beside it: Flash = 3 × NA's Flash median wall per problem and arm; argon = that × WA's argon/Flash median-wall ratio per arm
(plain 1.269, salt-diet 1.382; WHT and NTT pooled), because no argon cell has run on the six and NA's Pro cells were another model.
**Flash 41,439 s = 11.5 h · argon 56,276 s = 15.6 h · 72 cells 97,715 s = 27.1 h of cell wall.** LinearScan salt-diet alone is about a third
(`ta_price.out`, last line). Its direction is unknown: the statement may shorten salt-diet's specification work or lengthen plain's reading, and both bases are
`extras = none`. ⚠️ **A mode seam inside the price:** WA Flash ran in the client's Auto mode and WA Pro in Default (WA ADDENDUM 5 item 3),
so the ratio compares two modes; every TA cell runs in Default. The script's registered-n filter is live: a mutant without it
reads BinomialHeap salt-diet at n 4 (NA's one cell outside its registered n) and the total at 28.9 h. The Luby sextet of each model re-cuts the price before AES fires.

## §TA4 · CONFOUNDS — WA §WA4 and block T §T5, plus this block's own
1. **THE STATEMENT ARM IS A STRONGER TREATMENT BY CONSTRUCTION** (block T §T5 item 1), within which (d) and (e) are compared.
2. **THE REFUTER'S CATCH AND THE PLANTED-AMBIGUITY INSTRUMENT ARE OFF BY CONSTRUCTION** (block T §T5 item 2), and **CARRIED CONSTANTS**
   (block T §T5 item 3).
3. **THE MODEL SEAM** (WA ADDENDUM 2): an argon cell is never pooled, tabled beside or compared with a gemini-3.1-pro-high result, NA's
   included. **THE CLIENT SEAM** (WA ADDENDUM 1, 5): NA ran on clients older than 1.5.7, the version that made Auto mode the headless default; TA runs on the
   release's client, in Default mode by the setting.
4. **LINEARSCAN'S CARD SCOPE LINE.** The agy production line (0b783cf3, and 3fd5edf1 after it) carries LinearScan's pre-desk-YM scope line
   ("… AS A THEOREM IS NOT ASKED FOR. That is a compiler-verification project …"), which the neutrality gate refuses (bus 2026-09-26). NA's
   export 8ed8cb3 and 8bf04bdc carry the reworded line (23485e58). The overlay takes 8bf04bdc's card whole, so TA's LinearScan card equals the
   wording NA ran on, plus the section. Declared because the agy line's own card differs from it.
5. **A DIFFERENT HARNESS FROM NA's** (WA §WA4 item 2), carried.

## §TA5 · VOIDS, READING RULES, WHAT THIS BLOCK CANNOT ESTABLISH
Voids: WA's, plus block T §T7's row: **a cell built from a section that does not `cmp` equal to the tool's re-derivation is VOID.** Reading:
every premium is registered UNRESOLVED-UNDERPOWERED (block N §N6, as block T §T6). Cannot establish: no magnitude or effect size; nothing
Claude-versus-agy (level 6's cross-lane rule), so nothing block T versus TA; nothing Flash-versus-argon as models; nothing about the
statement arm versus `extras = none` across blocks (block T §T8 item 3: NA ran months earlier, on other exports, clients and a Pro model
that TA does not run).

## §TA6 · WHAT THE HAND DELIVERS
WA §WA6 unchanged (NA §NA6's list, the tree-hash line per cell, the O4 concurrency column, the cut columns), plus the per-cell answer to
§TA2's extra tripwire line. A result of record per model, O37's census section re-cut in the same commit. Any public sentence, and any
claim about the method, is the Captain's. The hand is named in the release (WA's was `gemini`).

---
## ✍️ NON-AUTHOR SIGNATURE — the helm (214th head), 2026-11-17 10:36 PST, bus offset 105,188,771 (transcribed by the lead)
Blob fe9b27a51916 at head b9eaf115f069, read whole (§TA0–§TA6), NO LOW. Checked at the objects: the candidate 397864e8 differs from 3fd5edf1
in exactly the six card.md files; each card is blob-equal to 8bf04bdc's; `ta_price.out` ends as §TA3 says. **§TA2 item 2, the helm's read
(reversible by the Captain with one word; on the 11-18 pack's ledger):** ruling 6's read REACHES the agy lane, because his read was of the
six statements' bytes and TA carries them unchanged, his 09-25 word is the authority for O37's remaining problems on bench's lanes, and block
T's own registration names these 24 conditions as its sibling freeze. Wrong if he says the release was for the Claude lane only. Not
measured by the signer: items 4 and 5 beyond the lead's post; item 6 (the lane battery) is the release's. Signature is not release.

---
## ⚖️ ADDENDUM 1 (2026-11-17, bench) — RELEASE, ⛔ DRAFT: NOT A RELEASE UNTIL ITEM 6 (THE LANE BATTERY PER MODEL) IS FILLED AND THE CLIENT IS NAMED
**Export: saltbench-systems `397864e8`**, the candidate §TA0 row 4 names, unchanged. On the run box by `studio_export.sh --no-toolchain
--unreferenced-dest` (a block T cell was live there, and the exporter refuses a referenced dest while a client runs; this dest is new and
nothing resolves into it): 387 files, listing sha256/16 4670ec729a6c3eb6, withheld-shaped names 0 in the listing and 0 on the host,
required-ancestors 5/5, marker written last.
**§TA2 receipts:**
1. MET BY CITATION, with the identity shown: block T's ADDENDUM 1 item 1 (6/6 EQUAL at 7fe4ff7f, a one-byte control DIFFER). For each of
   the six problems, `G/withheld/reference/solution.rs`, `verify.names` and `G/interface.rs` have the same git blob at 7fe4ff7f, 8bf04bdc
   and 397864e8 (18 of 18 compared), and each card is blob-equal to 8bf04bdc's (the signer's check (2)).
2. MET by the helm's read recorded above (ruling 6 reaches the agy lane; reversible; on the 11-18 pack's ledger).
3. Sizes: block T §T2 item 3's table, unchanged.
4. MET 2026-11-17 at this export on the run box: 12 cells built with `--client agy --statement` into a scratch cells root, all rc 0,
   "neutrality: zero hits" 12 of 12; the planted `// theorem: planted` copy REFUSED in both arms (2 hits, rc 4).
5. MET: `check_withheld_leak_v3.py` over 397864e8's tasks: CLEAN, 244 identifiers across 13 tasks, every positive control fired, 0 in any
   view.
6. ⛔ OPEN: the lane-live battery on one dry cell per model (gemini-3.8-flash-high, gemini-4-argon-high) on the release's client, by the
   hand, with the client version and sha, the credential window, the served model, fence, TMPDIR identity and the TREE-HASH line.
**Hand:** gemini (as WA), on its confirmation. **Pool:** the agy pool at P3, yielding to any O4 agy cell live or queued. **Order:** §TA2 as
registered (Flash first; Luby first; `T-TA-F` read by the lead before Flash continues). Nothing fires before this heading loses its DRAFT
mark.
