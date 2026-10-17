# RESULT — desk OD, THE IDENTITY TRIPLE (§D3) · Crc32 × greenfield × extras=none × plain · one cell per configuration
### bench (lead), 2026-10-17. **An interim result of record: the three identity cells §D3 registers, read before the block continues. It is not the block's result (§D9), which follows the 27 cells.**
## 📌 The registration is `AMENDMENT-OD-effort-matrix-2026-10-16.md` (§D0–§D9, ADDENDA 1–6). The configurations are FX (Fable/xhigh), FH (Fable/high) and OX (Opus/xhigh).
## 📌 The per-cell table is a FILE: `evidence/od-identity-triple-2026-10-17/od-identity-cells.tsv` (5 rows), built by the lead's extractor from the run's own records: each cell's harvest, served-set and escape outputs, the chain log's suite line, and the cell's own `ctl/launch.log` ARGV line and `ctl/end-1` marker, read at the run box. The extractor refuses a row whose harvest end marker disagrees with the cell's own, or whose meter components do not sum to T.
## ⛔ Every figure line in §1–§3 is printed by `RESULT-claude-OD-identity-2026-10-17-verify.py --print` from that table, and the verifier asserts each one against the bytes of this document (its `--selftest` reddens on two mutants). No number in those sections was typed from a message or from memory.

---
# §1 · WHAT RAN, AND WHICH CELLS COUNT
```
cells 5 · matrix 3 (client 2.1.280) · identity-only 2 (client 2.1.259)
```
- **The three matrix cells** are the re-run triple of ADDENDUM 5: FX#2, FH#2 and OX#1, all on client 2.1.280 and harness export `9f42a53548a0`
  (ADDENDUM 6), chain `clb_chain.v12.sh`. Each counts as cell 1 of its (configuration × Crc32) condition, as §D3 registers. The numbers are
  labels (ADDENDUM 5): FX and FH start at #2 because their #1 is an identity reading on the old client.
- **The two identity-only cells**, FX#1 and FH#1, ran on client 2.1.259 before the OX refusal that ADDENDUM 5 records. They are printed for the
  record and **enter no reading of the block** (ADDENDUM 5: "identity readings only, never matrix cells"). OX never ran on 2.1.259: its
  pre-launch probe was refused by the server for that client version, with no model work and no spend.
- The three matrix cells were staged from export `811dc09` and fired under `9f42a53`. Their task bytes are identical between the two exports
  (`git diff 811dc09..9f42a53 -- tasks` is empty), and none of the eight files copied into each cell names a file that changed. So the cell
  contents do not depend on the export. The launcher, fence render, run-dir check and settings are `9f42a53`, through the repointed `_bin`.

---
# §2 · THE IDENTITY READ (§D3: every head and sub-agent `message.model` against the requested id)
```
matrix        FX#2 clbxcp02  argv --model claude-fable-5-1 --effort xhigh  served head claude-fable-5-1 ×96 clean  sidechain claude-opus-5=50,claude-sonnet-5=46
matrix        FH#2 clbhcp02  argv --model claude-fable-5-1 --effort high  served head claude-fable-5-1 ×87 clean  sidechain claude-opus-5=29,claude-sonnet-5=23
matrix        OX#1 clbwcp01  argv --model claude-opus-5-5 --effort xhigh  served head claude-opus-5-5 ×118 clean  sidechain claude-opus-5=52,claude-sonnet-5=46
identity-only FX#1 clbxcp01  argv --model claude-fable-5-1 --effort xhigh  served head claude-fable-5-1 ×113 clean  sidechain claude-opus-5=47,claude-sonnet-5=27
identity-only FH#1 clbhcp01  argv --model claude-fable-5-1 --effort high  served head claude-fable-5-1 ×87 clean  sidechain claude-opus-5=45,claude-sonnet-5=41
```
- `clean` is printed only when three things agree: `served_models_v3.py check-cell` read the set `clean` against the configuration's head
  table (`fable51` or `opus55`, R1.3), the served head id is the registered one, and the ARGV's `--model` is that same id. The sub-agents
  served the pilot's Opus table (reviewer `claude-opus-5`, worker `claude-sonnet-5`), as §D0 row 1c holds them.
- **F3' is settled by this read: OX's head was served `claude-opus-5-5`.** OX is a NEW baseline, not linked to the pilot's `claude-opus-5`
  cells (R1.3, kent's R2).
- ⛔ **The applied effort is NOT in any transcript.** The `--effort` column is the ARGV in the cell's own launch log, which is the only record
  of it (§D3, §D8.4). It is the effort the client was ASKED for.

---
# §3 · THE READINGS (§D3's tripwire figures: correctness, T, output tokens, list-USD, wall)
```
matrix        FX#2  ENDED: LANDED  PASS 6/6  T 3,966,280  output 106,224  list-USD $7.96  wall 18m31s  escape 0
matrix        FH#2  ENDED: LANDED  PASS 6/6  T 2,381,690  output 62,720  list-USD $4.66  wall 12m29s  escape 0
matrix        OX#1  ENDED: LANDED  PASS 6/6  T 4,219,849  output 116,039  list-USD $4.79  wall 13m30s  escape 0
identity-only FX#1  ENDED: LANDED  PASS 6/6  T 3,210,879  output 109,347  list-USD $8.34  wall 18m31s  escape 0
identity-only FH#1  ENDED: LANDED  PASS 6/6  T 2,879,746  output 66,273  list-USD $5.01  wall 11m28s  escape 0
matrix total T 10,567,819 · output 284,983 · list-USD $17.41 · suites PASS 6/6
```
- **Correctness** is the withheld suite (§D4 classes), never the landing claim. Every cell is PASS.
- **T** is metered (input + output + cache reads + cache writes, from the session transcripts). **list-USD** is the meter's price at the
  re-dated `rates.tsv` rows (R1.2, read 2026-10-17): a list price at that date, not the fleet's cost (§D8.5).
- **Wall** runs from the ARGV line to the end marker, both in the cell's own `ctl/`, and is printed beside cost, never as a cost (§D4). ⚠️ The
  tripwire post gave the matrix walls as ~16, ~10 and ~11 minutes. Those were read from the chain's FIRED line, which is written after the
  launch is OBSERVED, about 2.5 minutes after ARGV. The table's walls replace them. No price used wall.
- `escape` is the escape scan's count of other-root paths in the cell's tool inputs.
- ⛔ **NO COMPARISON IS MADE HERE.** n = 1 per configuration, all three at the ceiling, and Crc32 is the cheapest chartered problem (§D3's own
  limit, which the LZW and FreeList tripwires correct). No prediction of §D5 is scored at this point; P1–P5 are scored at the block's result.

---
# §4 · THE QUOTA READINGS (the Fable meter, §D3), AND WHAT THE PM PRICED FROM THEM
Read from the chain's `quota.log` (one reading per fire, taken by `quota-triples.sh` before each cell; format session / all-models weekly /
fable-only weekly, percent used) and one reading after OX#1 by the lead:
```
before FX#2  5/50/2   ·   before FH#2  7/50/3   ·   before OX#1  9/51/3   ·   after OX#1  10/51/3
```
Over the three matrix cells, all-models weekly moved +1 and fable-only weekly +1. **The meter's resolution is one point**, so FH#2's 0 on the
fable-only meter is a reading below resolution, not a free cell. The pool is shared with other seats, so a movement is an upper bound on the
triple's own share. The PM's §D3 re-price (bus 2026-10-17 04:58:45, and the PM's re-price record) was written from
these readings and nothing else, and found that the stop rule does not fire.

---
# §5 · THE PER-CELL CHECKS, AT HARVEST (ADDENDA 5 and 6)
Each was read at harvest and posted the same hour; the figures are quoted from those posts (bus offsets 83,010,571 for FX#2, 83,026,221 for
FH#2, and the tripwire post 83,029,131 for OX#1 and the three together):
- **Config dir after each cell** (the helm's (A″) condition): `seed-admin` empty, no `skills/`, `plugins/synced` at its baseline (1 file,
  2 entries, 0 bytes), after all three. That is the account sync held off for three full cells, where ADDENDUM 6 had measured it on probe turns only.
- **Roots born inside the cell's window** (systems item 15, the out-of-root form; window bounded by the cell's end): FX#2 0 · FH#2 1
  (`cells-zf-freelist-argon-salt-gf-stmt-r1`, born 04:29:30 PDT, its name 0 times in the transcript of 1,256,379 B and the cell's logs) ·
  OX#1 0. The one root was readable to FH#2's subprocesses and was not named by it. **Exposure, not use.** The in-root form cannot arise
  here: no other cell was staged inside a root while one of that root's cells was live.
- **OX's client notes:** 0 unknown-model notes in OX#1's launch and watch logs. A client note printed only to stderr may not land in those
  logs, so this is a floor.

---
# §6 · DECLARED, BESIDE THE FIGURES
1. ⚠️ **OX#1's T and list-USD are slight OVER-statements.** The cell was staged on OX's own root, and the lead's pre-launch drive probes for
   ADDENDA 5 and 6 (10:20–10:58 UTC, and the 2.1.259 refusal) ran in that same cell, so the transcript directory the meter reads holds 7
   probe files besides the cell's session. By a message-id-deduplicated reproduction they are ~190,322 tokens, **~4.6 %** of 4,141,200. The
   meter's own T is 4,219,849, 1.9 % from that reproduction, so the share is approximate. The figure above is the meter's, unsubtracted. FX#2's
   and FH#2's directories hold only their own fire probe. The PM's price notes this share is below the meter's one-point resolution.
2. **Each cell's own pre-launch sandbox probe is inside its T.** It is the harness's standard probe (desk VX), the same in all three
   configurations.
3. **A cell id is not unique across roots.** `clbwcp01` is OX's Crc32 cell and also a cell of an unrelated lane-B root on the run box. The
   table's rows name the OD root by its configuration; the served read and the meter take the full path.
4. **The run's history before the matrix cells, none of which spent on a matrix cell** (the lead's run record): on chain v11 the first pass
   HELD FX at launch on fence drift (a root of another lane born 14 s after the render) and wrote a false `LIST COMPLETE` (ADDENDUM 4's
   defect); the second pass ran FX#1 and FH#1 on 2.1.259; OX was refused by the server for that client (ADDENDUM 5); on 2.1.280 the first
   v12 fire was refused before launch by the run-dir check, because the client had synced account skills into the config dir during the
   lead's probe turns (ADDENDUM 6); the re-run then fired cleanly.
5. **The quota bracket.** The session pool reset during the run; the weekly windows did not.

---
# §7 · WHAT THIS RESULT CANNOT ESTABLISH
1. **Any difference between the configurations.** n = 1 each, all PASS, one problem. 2. **The effort the client applied**: only the effort
it was asked for. 3. **Anything about salt-diet or the method.** 4. **A price**: list-USD is a list price at a date, and the subscription
meter is the fleet's real cost, at one-point resolution. 5. **The cost of LZW or FreeList**: Crc32 under-reads them by construction.

Any public sentence, and any claim about the method, is the Captain's.
