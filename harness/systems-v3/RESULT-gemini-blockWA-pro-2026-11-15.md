# RESULT — O37 block WA, PRO HALF · the agy lane × greenfield × extras=none × WHT and NTT · n = 3 · gemini-4-argon-high
### bench (lead), 2026-11-15, on the hand's files (gemini; its deliveries on the bus at offsets 103,432,031 for WHT and 103,491,289 for NTT). **4 conditions, 12 cells. §WA6: "a result of record per model": this is argon's, under ADDENDUM 2's MODEL SEAM.**
## 📌 The registration is `AMENDMENT-O37-wht-ntt-greenfield-agy-2026-11-13.md` (§WA0–§WA6, signed; ADDENDUM 2 re-registered the Pro slot on `gemini-4-argon-high`; ADDENDA 3–5 released it; ADDENDUM 6, in this commit, records the NTT price re-cut and a name correction).
## 📌 The per-cell table of record is `evidence/blockWA-pro-2026-11-15/cells.tsv`, built by `wa_pro_cells_gen.py` beside it from the hand's score receipts (`score_wave_v3.sh`, one per cell, in the three run dirs the generator names) and `cell_facts.json` (`wa_facts.py`, read on the run box from each cell's own `ctl/`). The generator is the Flash half's, changed only as its docstring lists.
## ⛔ Every figure line below is printed by `wa_pro_cells_gen.py --summary`, and `wa_pro_cells_gen.py --check` on this file asserts each one occurs here verbatim. Bus offsets and clock times in the prose are citations, not measurements.

---
# §1 · WHAT RAN, AND ON WHAT
```
cells 12 · scored 12 · receipts read 12
requested_model gemini-4-argon-high=12
init_model gemini-4-argon-high=12
client_sha256 fad3628ad91fe861=12
export_sha 3fd5edf1ffa4=12
done_reason LANDED=12
```
- **One export for all 12 cells: `3fd5edf1`** (saltbench-systems), as ADDENDUM 5 released it. It carries the per-cell environment fix of
  ADDENDUM 3 and the client setting `agentMode ""` of ADDENDUM 5, which switches the client's own sandbox off.
- **One client, agy, binary hash `fad3628ad91fe861` in every cell**, the same binary as the Flash half. The hand reports 0 `exit 71`, 0
  `sandbox_apply`, 0 exebox and 0 `BypassSandbox` events in all 12 cells (its delivery posts; the counter is the export's
  `agy_shell_count_v3.py`). The lead did not re-count these.
- **The model column says less than a served set**, as in the Flash half: `requested_model` is what the harness asked for and
  `init_model` is what the client's `init` event reports. Both read `gemini-4-argon-high` in all 12.
- **WHICH 12.** `T-WA-P` is `wawas1r201` (WHT salt-diet #1), the re-fire ADDENDUM 5 released (its text called the id `wawas1r02`;
  ADDENDUM 6 corrects the name). `wawas101` is NOT-SCORED(HARNESS) (ADDENDUM 3) and `wawas1r01` is reported, not of record (ADDENDUM 5);
  neither is in this table, and the generator does not read their run dirs.
- **The order** was ADDENDUM 2's: `T-WA-P` first, read by the lead (bus offset 103,291,990), then WHT's other five cells, then the NTT
  price re-cut from WHT's walls (bus offset 103,435,747; ADDENDUM 6), then NTT's six, all serial.
- **THE BOX WAS SHARED for 8 of the 12 cells.** Another seat's long Lean run (on the run box from 12:49Z, still live at NTT's end) ran
  beside `wawap301` and `wawas301` wholly, the last ~15 minutes of `wawas201`, and all six NTT cells. Walls are reported as measured;
  none is corrected, and nothing here measures the sharing's effect.

---
# §2 · gemini-4-argon-high — THE RESULT OF RECORD
```
WHT plain: FULL PASS 3 of 3 scored, of 3 fired [11/11 11/11 11/11] · cut turns 0 of 9 sent · truncated 0 · interface 89f1f28cf0773154
WHT salt-diet: FULL PASS 3 of 3 scored, of 3 fired [11/11 11/11 11/11] · cut turns 6 of 11 sent · truncated 2 · interface 89f1f28cf0773154
NTT plain: FULL PASS 3 of 3 scored, of 3 fired [11/11 11/11 11/11] · cut turns 0 of 9 sent · truncated 0 · interface 3d2d201dbe94cf64
NTT salt-diet: FULL PASS 3 of 3 scored, of 3 fired [11/11 11/11 11/11] · cut turns 6 of 10 sent · truncated 2 · interface 3d2d201dbe94cf64
end-1 kinds: LANDED=11 PERSIST-INDETERMINATE=1
```
- **Every cell passes the withheld suite in full, on both problems and both arms.** Both conditions of each problem are at CEILING, so
  this block can say nothing about a difference between the arms in pass rate.
- **FOUR SALT-DIET CELLS WERE TRUNCATED and no plain cell was.** A truncated cell had turns cut by the per-turn deadline. Its pass stands
  as a FLOOR (it passed with less than the registered turn budget), and its token, turn and wall figures are NOT POOLABLE and enter no
  premium (helm ruling 2026-09-11). The four are `wawas1r201`, `wawas201`, `wanas101` and `wanas301`.
- **ONE END KIND IS PERSIST-INDETERMINATE: `wanas301`.** Its `end-1` reads that the subject gave no answer on the final turn, so the
  post-landing persistence probe could not be read. It LANDED by the record: `landed-1` is tagged, `wa_facts.py` reads `done_reason`
  LANDED, and the hand's run of `phase2_landed_gate_v3.py` reads LANDED with the tag equal to the receipt (its NTT post). **Ruled (the
  lead): it counts as a landed, scored cell of record**, with its end kind printed beside it. It is also TRUNCATED, so its pass is a floor.
  A reader who opens its score receipt meets `LANDED 0 · SCORABLE 1`: the receipt tallies END kinds, and this cell's is not LANDED. The
  count of landed cells here comes from the tag, the landed gate and `wa_facts.py`, not from that tally.
- **Each condition sits on one interface hash**, the receipts' POOLABLE line, and each equals the Flash half's for the same problem.

**The predictions (§WA3):**
- (i) within a condition, salt-diet's TURNS-CUT and CAP-TOKENS incidence is ≥ plain's: **holds, and is TESTED here** (unlike the Flash
  half, where it held at 0 ≥ 0): turns were cut in 2 of 3 salt-diet cells against 0 of 3 plain, in both problems. No cell tripped a
  token cap.
- (iii) CELL-KILLED binds no cell outside a declared 503 episode: **holds.** No cell was killed; the hand reports `a503 = 0` throughout.

**Cost, as a sign only (n = 3 per condition, §WA3 registers no premium, and a TRUNCATED cell's figures are not poolable):**
```
WHT T by rep (plain / salt-diet; (T) = TRUNCATED, not poolable): #1 2055806 / 11778076 (T) · #2 1238966 / 6845625 (T) · #3 1225379 / 4281863 · untruncated pairs 1 (#3)
WHT wall_s by rep (plain / salt-diet; (T) = TRUNCATED, not poolable): #1 704.0 / 2227.1 (T) · #2 728.7 / 2020.4 (T) · #3 760.5 / 1836.5 · untruncated pairs 1 (#3)
NTT T by rep (plain / salt-diet; (T) = TRUNCATED, not poolable): #1 1926854 / 7139885 (T) · #2 2810812 / 5397079 · #3 1681250 / 13302421 (T) · untruncated pairs 1 (#2)
NTT wall_s by rep (plain / salt-diet; (T) = TRUNCATED, not poolable): #1 740.0 / 2013.1 (T) · #2 1259.0 / 1450.8 · #3 847.6 / 2842.7 (T) · untruncated pairs 1 (#2)
```
T is the agy meter's token total. With four of six salt-diet cells truncated, ONE untruncated pair per problem is left (#3 for WHT, #2
for NTT). **No sign is claimed from one pair**, and none is printed. The cut cells are printed so a reader can see what was spent; they are
not a cost reading.

**Observations the hand carried, kept because they bear on reading the table:**
- `wanas301` carries 2 of 62 shell steps with an empty output and no exit line; the counter counts them as succeeded. The hand noted
  them and did not re-classify them, and neither does this file.
- the gap between a wave's span and the sum of its cell walls is the client's credential-window wait (1,941 s before `wanas201`, the case the hand named),
  outside every `wall_seconds` above;
- `landed-2` (the P-PERSIST turn's tag) is present in 6 cells; the end marker and the score read `end-1` only:
```
landed-2 tag present in 6 of 12 cells: wawap101 wawap201 wawap301 wawas301 wanap201 wanap301
```

---
# §3 · THE SEAMS
- **MODEL SEAM (ADDENDUM 2):** this is a result about `gemini-4-argon-high`. It is never pooled, tabled beside or compared with any
  `gemini-3.1-pro-high` result, and nothing here is Flash-versus-argon as models.
- **CLIENT-MODE SEAM (ADDENDUM 5 item 3):** the Flash half ran in the client's Auto mode (its own sandbox on); these 12 ran with it off.
- **ENVIRONMENT SEAM (ADDENDUM 3):** the Flash half's subjects ran with the shell `TMPDIR` at `/tmp/claude`, a path that did not
  exist; these 12 ran with it at the cell's own tmp.
- The Flash half's ADDENDA (`/tmp/claude` tool failures; Auto mode) describe the Flash cells; neither shape occurs in these 12 by the
  hand's counts (0 exebox, 0 `sandbox_apply`).

---
# §4 · WHAT THIS RESULT DOES NOT ESTABLISH
Block W §W8 items 1, 3 and 4 and §WA5, carried: no effect size; nothing about the 212 O37 conditions outside these 4; WHT and NTT are a
selection (the two of three judged feasible, and both new). Nothing Claude-versus-agy, nothing Flash-versus-argon, and nothing about
block NA's six problems. §WA4 item 1 is carried: one author built both tasks and leads this block, and NTT's reference proves less than
WHT's. With every cell at ceiling, nothing here says whether the salt method helps or hurts on these problems. The truncation pattern
(salt-diet 4 of 6, plain 0 of 6) is the registered prediction holding; it is not a measure of the method's cost.
