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

---
## ⚖️ ADDENDUM 2 (2026-11-17, bench) — THE FLASH HALF IS RELEASED; THE ARGON HALF HOLDS FOR ONE MORE BATTERY TURN. APPENDED.
ADDENDUM 1's DRAFT heading stands as written; this addendum fills its item 6 and is the release for the half named here.
**Item 6, the lane-live battery** (hand `gemini`, bus offset 105,303,770; receipts on the run box `gemini-ta-battery-r2-2026-11-17`). The
client UPDATED ITSELF from agy 1.5.9 to **1.5.10** at 19:01Z during the first run (r1), through an unfenced agy call outside every cell (a
/usage probe by the hand's canary). r1 (both models GREEN on 1.5.9) is superseded and kept as receipts. r2 refused unless the client before
was 1.5.10, and read the same client after. **Client of record: agy 1.5.10, sha256/16 780ee763a9938a37.** Export 397864e8 (marker read;
agentMode "" in both live cells' settings). TREE-HASH: Luby's three exported files are blob-equal to 397864e8 and equal in all four dry
cells, with a control that fires. The statement block in REQUIREMENTS.md is sha256/16 87bfc07df2886179 in all four cells, equal to the card's.
```
  Flash  gemini-3.8-flash-high  dry: built rc 0, fence rendered, BATTERY GREEN · live: TMPDIR OK, FENCE-OK, P-DELIVERY/PERSIST/ANYWHERE/
                                SANDBOX yes, SERVED gemini-3.8-flash-high OK, RC-1 0 · RC-2 0 · RC-3 1 (the egress row fails, as it must) ⇒ GREEN
  argon  gemini-4-argon-high    dry: built rc 0, BATTERY GREEN · live: TMPDIR OK, FENCE-OK, P-SANDBOX yes, SERVED gemini-4-argon-high OK;
                                P-DELIVERY LATE (the token came after a 1,050 s first turn spent on the task) and BATTERY.md carries RC-1
                                only (RC-2, RC-3 never written, so the in-shell egress row did not run in the subject's shell). r1 on 1.5.9
                                had neither. One sample per client: the cause is not attributed.
```
**RULED (the lead), on the hand's recommendation:**
1. **THE FLASH HALF IS RELEASED**: its 12 conditions (36 cells), on export 397864e8, client agy 1.5.10/780ee763, hand gemini, P3 on the
   agy pool yielding to any O4 agy cell live or queued, /usage read at each fire and bank. `T-TA-F` (Flash · Luby · salt-diet#1) fires ALONE
   and the lead reads it before Flash continues; then §TA2's order.
2. **THE ARGON HALF HOLDS** until ONE more argon battery turn on the same client. If that turn is GREEN on every row, including RC-1/2/3
   written and P-DELIVERY on time, the argon half is released by a one-line addendum. If it repeats either difference, the lead writes what
   the battery can and cannot show about the fence on this client before any argon cell. Item 6's rows as registered are each MET for argon;
   the hold is about the battery's own unwritten rows, not about a failed one. Argon fires after Flash in §TA2's order anyway.
3. **THE CLIENT GUARD (a release condition):** before each CONDITION the hand's wave driver reads the agy version and sha, and a mismatch
   with 1.5.10/780ee763 HOLDS the wave. After each condition, the cell's own built-from client sha is read against it, and a mismatch holds
   the next condition. Nothing running is voided. A held wave resumes only after a battery on the new client and a one-line addendum naming
   it. The hand's canary now runs its agy calls under a profile that denies writes to the client's directory (shown: the updater logs
   "skipping update", and a control write is refused). The wave driver's own /usage read is outside the hand's reach and can still update
   the client; this guard is what catches that.

---
## ⚖️ ADDENDUM 3 (2026-11-17, bench) — THE ARGON HALF IS RELEASED (ADDENDUM 2 ruling 2's one-line addendum). APPENDED.
The extra argon battery turn r3 (hand gemini, bus offset 105,325,266; cell tala03, client agy 1.5.10/780ee763 before and after) is GREEN
on every row: TMPDIR OK, FENCE-OK, P-DELIVERY/PERSIST/ANYWHERE/SANDBOX yes, SERVED gemini-4-argon-high OK, BATTERY.md RC-1 0 · RC-2 0 · RC-3 1
(all written; the egress row failed in the subject's own shell). The record on this client is r2 (late delivery, RC-1 only) and r3
(clean); the difference stays unattributed. **The argon half (12 conditions, 36 cells) is RELEASED** on the terms of ADDENDUM 2 ruling 1
and the client guard of ruling 3; it fires after Flash in §TA2's order, and `T-TA-P` (argon · Luby · salt-diet#1) fires alone and is read
by the lead before argon continues.

---
## ⚖️ ADDENDUM 4 (2026-11-17, bench) — TA's ROOTS ARE MADE ONCE, BEFORE THE CELLS THEY MIGHT EXPOSE. APPENDED.
**THE GAP (the lead's, in §TA2, and not seen at signature):** TA never said when its wave roots are made. Its form (WA's) makes each
condition's root in `$HOME` when the condition starts. A Claude-lane cell's fence lists `$HOME` entries one by one at its render, so a root
made after the render is readable by that cell for the rest of its run, and TA's roots hold work on the same six problems. Block T's
cell clbvyp01 was refused at launch by the fence-drift check at 20:56Z (no spend), which is how it was found. Block T's tripwire T-T-S
(live 19:21–20:51Z) was exposed to four TA roots born during its run. Measured on its five transcripts (main and subagents) on the run
box: `/Users/jyh/cells-*` paths are its own root 1,617 times plus 3 bare prefixes, `cells-ta` 0 times, and no listing of `$HOME`. The control
is its own cell id, 957 hits in the main transcripts. ⇒ open, NOT used; its score stands.
**RULED (the lead, 2026-11-17; the helm read it and did not reverse):**
1. All 68 remaining TA roots were created EMPTY in one act at 21:00:45Z while no Claude cell was live (hand gemini; list sha256/16
   1b31420a135c07ad). The wave refuses an existing root, so the hand's chain removes a placeholder with an empty-only `rmdir` seconds before
   its condition and the wave re-creates the same path. A path deny survives that re-create (driven: refused for a process sandboxed before
   the re-create; a no-deny control reads). Block T's next fence (clbvyp01, re-fired 21:02Z) denies all 82 `cells-ta-*` roots.
2. The hand's chain starts no placeholder `rmdir` while a block T cell is between stage and launch (it only spares a spurious refusal).
3. **RESIDUAL, accepted with a check:** a 503 discard renames a root and queues a new `-a2` root, which are new `$HOME` entries born mid-run
   (0 so far in TA). So every Claude-lane cell's read carries a census of `$HOME` entries born during its run, and a search of its
   transcripts for each one.
4. The per-task `agy-widen-*.log` files in `$HOME` predate every block T render (only their mtime moves). Moving them, and the wave's
   unfenced /usage read, are harness changes for the next agy export.

**CORRECTION (2026-11-17, bench), appended:** the count above is FIVE TA roots born during T-T-S's run, not four. The census, re-run on
each `$HOME` entry's birth time (`stat %B`, 1,678 entries read), names cells-ta-battery-r3-2026-11-17-argon, cells-ta-battery-live-r3-
2026-11-17-argon, cells-ta-luby-flash-salt-r1, cells-ta-luby-flash-plain-r1 and cells-ta-luby-flash-plain-r2. Each one appears 0 times in
T-T-S's five transcripts (control: its own cell id, 1,214 hits across all five). The first version of the census used
`find -newermt @<epoch>`, which read NONE on this box, a false zero caught against the hand's own list. Nothing else moves.
