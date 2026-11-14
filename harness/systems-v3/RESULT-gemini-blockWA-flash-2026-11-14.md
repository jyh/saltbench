# RESULT — O37 block WA, FLASH HALF · the agy lane × greenfield × extras=none × WHT and NTT · n = 3 · gemini-3.8-flash-high
### bench (lead), 2026-11-14, on the hand's files (gemini; its delivery on the bus at offset 102,297,116). **4 conditions, 12 cells. §WA6: "a result of record per model": this is Flash's. The Pro half is HELD (ADDENDUM 1) and has no result.**
## 📌 The registration is `AMENDMENT-O37-wht-ntt-greenfield-agy-2026-11-13.md` (§WA0–§WA6, signed; ADDENDUM 1 released Flash and held Pro).
## 📌 The per-cell table of record is `evidence/blockWA-2026-11-14/cells.tsv`, built by `evidence/blockWA-2026-11-14/wa_cells_gen.py` from two sources it names: the hand's score receipts (`score_wave_v3.sh`, one per cell) and `cell_facts.json`, read on the run box from each cell's own `ctl/` by `wa_facts.py` (which runs block NA's `cell_facts.py` unchanged and adds three columns).
## ⛔ Every figure line below is printed by `wa_cells_gen.py --summary`, and `wa_cells_gen.py --check` on this file asserts each one occurs here verbatim. Bus offsets and clock times in the prose are citations to where a reader can look, not measurements; the two git tree hashes are `git rev-parse <export>:tasks/systems-v3/<P>` in saltbench-systems.

---
# §1 · WHAT RAN, AND ON WHAT
```
cells 12 · scored 12 · receipts read 12
requested_model gemini-3.8-flash-high=12
init_model gemini-3.8-flash-high=12
client_sha256 fad3628ad91fe861=12
export_sha 6413289d608c=12
done_reason LANDED=12
```
- **One export for all 12 cells: `6413289d`** (saltbench-systems), as ADDENDUM 1 released. Its WHT and NTT task trees are byte-identical
  to block W's export `0916ef9a` (git tree `44b92115d240` for WHT and `77c641773103` for NTT at both), so the Claude and agy halves of
  WHT and NTT ran the same task bytes. Nothing here compares them (§WA5).
- **One client: agy 1.5.9**, its binary hashed at launch in every cell (`client_sha256` above). The hand read `/usage`, then the version
  and the hash, before every fire, and none differed (its chain log).
- **The model column says less than a served set.** `requested_model` is what the harness asked for; `init_model` is the model the
  client's own `init` event reports for the session. The agy stream carries no per-response model field that these tools read, so
  neither is a served-set reading in the Claude lane's sense. Block NA reported `requested_model` for the same reason.
- **The order** was §WA2's: the tripwire `T-WA-F` (Flash · WHT · salt-diet #1, `wawfs101`) first, read by the lead before Flash
  continued (bus offset 102,023,406), then the remaining 11 cells by one chain. The chain paused once, 08:28–08:30Z, for block W's
  roots window, at the lead's request.

---
# §2 · gemini-3.8-flash-high — THE RESULT OF RECORD
```
WHT plain: FULL PASS 3 of 3 scored, of 3 fired [11/11 11/11 11/11] · cut turns 0 of 9 sent · truncated 0 · interface 89f1f28cf0773154
WHT salt-diet: FULL PASS 3 of 3 scored, of 3 fired [11/11 11/11 11/11] · cut turns 0 of 9 sent · truncated 0 · interface 89f1f28cf0773154
NTT plain: FULL PASS 3 of 3 scored, of 3 fired [11/11 11/11 11/11] · cut turns 0 of 9 sent · truncated 0 · interface 3d2d201dbe94cf64
NTT salt-diet: FULL PASS 3 of 3 scored, of 3 fired [11/11 11/11 11/11] · cut turns 0 of 10 sent · truncated 0 · interface 3d2d201dbe94cf64
```
- **Every cell passes the withheld suite in full, on both problems and both arms.** Both conditions of each problem are at CEILING, so
  this block can say nothing about a difference between the arms in pass rate: there is no room for one.
- **Each condition sits on one interface hash**, the receipts' POOLABLE line.
- **Cut turns are counted across both client stderr files** (`cut_turns_all`); block NA's single-file count (`cut_turns`) is in the table
  beside it and is also 0 in every cell.

**The predictions (§WA3):**
- (i) within a condition, salt-diet's TURNS-CUT and CAP-TOKENS incidence is ≥ plain's: **holds, trivially, at 0 ≥ 0** in both problems.
  No cell was cut and none tripped a token cap, so (i) was not tested in the direction it was registered to watch.
- (iii) CELL-KILLED binds no cell outside a declared 503 episode: **holds.** No cell was killed and there was no 503 episode.

**Cost, as a sign only (n = 3 per condition, and §WA3 registers no premium):**
```
WHT T by rep (plain / salt-diet): #1 4725146 / 17043470 · #2 4352636 / 16486091 · #3 4302624 / 30073609 · salt-diet > plain in 3 of 3 pairs
WHT wall_s by rep (plain / salt-diet): #1 595.0 / 1487.2 · #2 587.2 / 1431.6 · #3 460.9 / 1694.1 · salt-diet > plain in 3 of 3 pairs
NTT T by rep (plain / salt-diet): #1 6403847 / 12621087 · #2 5210692 / 17448833 · #3 5270720 / 19905803 · salt-diet > plain in 3 of 3 pairs
NTT wall_s by rep (plain / salt-diet): #1 693.1 / 1989.0 · #2 580.0 / 1263.0 · #3 614.1 / 1207.8 · salt-diet > plain in 3 of 3 pairs
```
T is the agy meter's token total (input + output + cache read). The pool's own unit was read from `/usage` at each fire (§WA3: no dollar
figure is registered); the agy pool read at or near its ceiling throughout, so per-cell pool deltas are not measurable here.
**No magnitude is claimed.** The sign is the same in all six pairs on both columns.

**Observations the hand carried, kept here because they bear on reading the table:**
- the meter's `commands_failed` is a text heuristic; exit codes are the measure, and the hand counted those per cell;
- the hand reports that every cell's first command hit the vendor sandbox's certificate-path denial (its `ftr` column); the lead did not
  re-measure this;
- some cells carry a `landed-2` tag in phase 1 (the P-PERSIST turn); the end marker and the score read `end-1` only. Counted from each
  cell's repo (the hand's post said seven; the tags say eight):
```
landed-2 tag present in 8 of 12 cells: wawfp101 wawfp201 wawfp301 wawfs201 wanfp101 wanfp201 wanfs201 wanfs301
```

---
# §3 · THE PRO HALF
Not run. ADDENDUM 1 holds it: the registered id gemini-3.1-pro-high is not served by today's client, and substituting another id is the
Captain's word through the helm's pack. Its DEFAULT, if no word comes, is that Pro's 4 conditions are reported NOT-FIRED(MODEL) by a
census addendum. Nothing in this file is about any Pro model.

---
# §4 · WHAT THIS RESULT DOES NOT ESTABLISH
Block W §W8 items 1, 3 and 4 and §WA5, carried: no effect size; nothing about the 212 O37 conditions outside these 4; WHT and NTT are a
selection (the two of three judged feasible, and both new). Nothing Claude-versus-agy, and nothing about block NA's six problems
(§WA4 item 2: a different harness and client). §WA4 item 1 is carried too: one author built both tasks and leads this block, and NTT's
reference proves less than WHT's. With every cell at ceiling, nothing here says whether the salt method helps or hurts on these problems.
