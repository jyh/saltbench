# AMENDMENT — O37 BLOCK WCA: WHT AND NTT × SPEC-CHANGE, agy LANE, PHASE 2 ON COPIES OF WA's CELLS. FROZEN BEFORE THE FIRST BASELINE
## bench (SaltBench lead), 2026-11-23, from gemini's draft (the hand; saltbench-systems branch `gemini/o37-nca-wca-registration-drafts-2026-11-22`
## at 098430ec, backup only), beside block NCA (`AMENDMENT-O37-blockNCA-specchange-agy-2026-11-23.md`, cited as "NCA"). It carries NCA BY
## CITATION, exactly as block WC (`AMENDMENT-O37-wht-ntt-specchange-claude-2026-11-13.md`, "WC") carries NC. Its sources are block WA's cells
## of record (`AMENDMENT-O37-wht-ntt-greenfield-agy-2026-11-13.md`, "WA", ADDENDA 1–6). A clause that differs from NCA says so and why.
## ⛔ **UNSIGNED UNTIL A NON-AUTHOR SIGNS IT.** No baseline before the signature. No cell fires before a release addendum (NCA's rule), and
## NCA §NCA9 (§H-CLIENT) and §NCA10 (§H-CLIENT-NOISE) bind this block whole, by citation.

**Why now.** WA is a result of record on both models (census ADDENDA 40 and 44), WC holds WHT/NTT × spec-change on the Claude lane (census
ADDENDUM 45), and census ADDENDUM 46 §AQ2 lists "WHT and NTT … x spec-change, agy lane: in no block". This block is those 8 conditions.

---

## §WCA0 · THE INPUTS (NCA §NCA0, row by row)
```
  1  MODEL IDs     gemini-3.8-flash-high · gemini-4-argon-high: WA's two, as WA A2 left them, with its MODEL SEAM. Re-measured at release.
  2  n             3 per condition.
  3  POPULATION    8 conditions, 24 phase-2 cells (§WCA1).
  4  EXPORT        ⚖️ THE CHANGE FROM NCA: NO OVERLAY. The agy production line already carries WC's driven task trees. MEASURED
                   2026-11-22 (`git rev-parse <sha>:tasks/systems-v3/<P>[/B|/G]`): WHT 44b92115 (B 17d0b93b, G f5a9dbe7) and NTT 77c64177
                   (B c5cdaed5, G b868747b) at 6413289d (WA Flash), 3fd5edf1 (WA argon), d16d1173 and 36ca596b alike; WC ADDENDUM 1 names
                   the same hashes at d55062a6. ⚖️ RE-POINTED AT LANDING: the release fires on the RELEASED agy export aa071afc (NCA row 4), whose
                   WHT and NTT trees are 44b92115 and 77c64177, equal to WA's and WC's by git rev-parse (gemini's §WCA3 item 1 receipt).
                   Its task delta from 3fd5edf1 is NCA's six-tree overlay and block TA's six cards before it; WHT and NTT are untouched.
  5  CLIENT        NCA row 5.
  6  CAPS          NCA row 6 (NA row 5 per phase; persistence probe 600 s). No cap is raised.
  7  QUOTA         NCA row 7.
  8  FIRE ORDER    §WCA4.
```

## §WCA1 · THE POPULATION — 8 CONDITIONS, 24 PHASE-2 CELLS
```
  problems   NTT · WHT                     the two with a driven B/ rung (WC ADDENDUM 1 item 1) and an agy greenfield block (WA)
  models     gemini-3.8-flash-high · gemini-4-argon-high
  arms       plain · salt-diet             field greenfield → spec-change         extras none
  ⇒ 2 × 2 × 2 = 8 conditions · × n 3 = 24 phase-2 cells
```

## §WCA2 · THE SOURCES — NCA §NCA2's FLASH RULE, FOR BOTH MODELS
⚖️ **THE CHANGE FROM NCA: both models have sources**, so both are COPIES (L8 §A9.4 form, `agy_cell_copy_v3.py`, root `<source root>-wcacp`,
same id, AGY_PHASES=2 through the §A9.2 and §M3 gates, customer, aside), and NCA §NCA7 fork 1 does not arise. Sources:
```
  Flash   evidence/blockWA-2026-11-14/cells.tsv, 12 cells (export 6413289d): all 12 LANDED, PASS 11/11, none truncated
  argon   evidence/blockWA-pro-2026-11-15/cells.tsv, 12 cells of record (export 3fd5edf1): all 12 LANDED, PASS 11/11, 4 truncated
          (wawas1r201, wawas201, wanas101, wanas301: each a FLOOR at WA). wawas101 (NOT-SCORED(HARNESS)) and wawas1r01 (not of record)
          are not sources (WA Pro RESULT §1).
```
The G-rung baseline on landed-1 (NC ADDENDUM 1; `gbase.sh`, one attempt, on a clone) decides eligibility for all 24; a shortfall is a fresh
cell in level 8's one-cell form (NC rule 4), never retried; a condition with no cell of record is DECLARED unreached (census ADDENDUM 46).
**None of the 24 is WEB-SERVED** (census ADDENDUM 47 §AR2: "blocks WA and TA were served nothing"), so NCA §NCA6 item 5 has nothing to
act on here, and a WCA phase 2 that is itself served a search is WEB-SERVED in its own right.

## §WCA3 · THE BUILD ITEMS — NCA §NCA3, with these differences
1. **B/ trees:** equal to WC's driven trees by hash (§WCA0 row 4), so WC ADDENDUM 1 item 1's non-builder drive (systems, bus offsets
   103,352,799 and 103,355,962: WHT B/ 50/50, NTT B/ 45/45) is cited; a release export whose trees differ re-drives.
2. **Referee on dry agy cells** on the B/ rung, both arms, one clause and one regression mutant per task, with counts.
3. **The 24 baselines.** 4. **The copy form on a dry agy cell, one per model** (the argon copy is the first argon copy on this lane).
5. **No leak** (the checker screens both B/withheld trees; WC ADDENDUM 1 drove it on d55062a6, re-driven on the release export).
6. **The lane-live battery**, P-SWARM and P-WEB DENIED (NCA item 6).

## §WCA4 · THE ORDER, THE TRIPWIRES
```
  models     Flash first, then argon.
  problems   NTT → WHT (ascending B/ reference size, WC ADDENDUM 1: NTT 1147 · WHT 1186; the release re-reads with its own wc -l).
  cells      plain#1 · salt-diet#1 · plain#2 · salt-diet#2 · plain#3 · salt-diet#3, through the canary wave supervisor.
```
Tripwires: `T-WCA-F` = Flash · NTT · salt-diet#1 · `T-WCA-A` = argon · NTT · salt-diet#1, each read by the lead before its model continues
(NCA §NCA4's reading list).

## §WCA5 · PREDICTIONS AND THE PRICE
NCA §NCA5 (i)–(iii) carried. ⛔ No prediction about pass rate or premium. Printed by `wca_price.py --saltbench <clone> --ref 9efec234e988`
(`evidence/blockWCA-2026-11-23/`, with its output `wca_price.out`; re-run at landing against saltbench 9efec234e988, `cmp` EQUAL):
```
  L8 phase2/phase1 wall, model letter f: n 29 median 0.809
  L8 phase2/phase1 wall, model letter p: n 28 median 0.844
  gemini-3.8-flash-high: sources not landed 0  · 12 phase-2 launches floor · 9596 s = 2.7 h
  gemini-4-argon-high: sources not landed 0  · 12 phase-2 launches floor · 14199 s = 3.9 h
  WCA total: 24 launches floor · 23794 s = 6.6 h of cell wall; agy pool points per cell UNMEASURED
```
LIMITS: NCA §NCA5 (a), (d), (e) carried; shortfalls are decided by the baselines (a FLOOR); argon's source walls were measured on a box
SHARED for 8 of its 12 cells (WA Pro RESULT §1), so its medians may run high.

## §WCA6 · CONFOUNDS — NCA §NCA6 items 1, 2, 4 carried; item 3 restated; one of this block's own
3. **TWO EXPORTS PER PAIR, AND FOR FLASH A SANDBOX SETTING THAT DIFFERS.** Flash's sources ran on 6413289d, before WA ADDENDUM 3's per-cell
   environment fix and ADDENDUM 5's `agentMode ""` (the client's own sandbox off); their phase 2 runs on the release export, which carries
   both. Argon's sources ran on 3fd5edf1 (both carried). Each pair records both exports and both client hashes; phase 2 starts about a week
   after phase 1. Nothing compares a Flash figure with an argon one (WA §WA5).
6. **ONE AUTHOR FOR BOTH TASKS AND BOTH B/ SUITES, WHO IS THE LEAD; NTT's reference proves less than WHT's** (WC §WC6 item 4, carried).

## §WCA7 · FORKS ON A DEFAULT
None of NCA's arises (both models have sources; no source is WEB-SERVED; no condition starts without a source). The draft adds none.

## §WCA8 · READING RULES, VOIDS, WHAT IT CANNOT ESTABLISH, DELIVERABLES
NCA §NCA8, §NCA9 and §NCA10 carried, for NTT and WHT: a result of record per model, the census O37 section re-cut in the same commit; nothing about
gemini-3.1-pro-high, nothing Flash-versus-argon or Claude-versus-agy. Any public sentence is the Captain's.

---
# ⚖️ ADDENDUM 1 (2026-11-23, bench) — RELEASE, ⛔ DRAFT: carried whole from NCA ADDENDUM 1 (export 88b63df9, client, signature, items
1–6, the replaced-hook gate, the quiet window, quota). WCA-specific: item 1 WHT 44b92115 · NTT 77c64177; item 2 harvest 8/8; item 3
Flash 12/12 · argon 12/12, no shortfall; item 4's argon drive (wanap101) is this lane's first argon copy. APPENDED.

---
# ⚖️ ADDENDUM 2 (2026-11-24, bench) — THE RELEASE, carried whole from NCA ADDENDUM 2 (item 6 MET at 88b63df9, both models; the quota named
# by the PM; every receipt MET; the three first-fire reads). Effective when it reaches `main` after a non-author read. APPENDED.
WCA's own population, order and sources are §WCA1–§WCA4 and ADDENDUM 1. Nothing in NCA ADDENDUM 2 is specific to block NA's six, so it
carries to NTT and WHT without change.

---
# ⚖️ ADDENDUM 3 (2026-11-24, bench) — carried whole from NCA ADDENDUM 3: the supervisor 81792dbe (its WCA copy form `^cells-wa-…-wcacp[1-3]$`
# at AGY_PHASES=2) and the copy root `<source root>-wcacp<k>`; both departures declared. WCA registers no fresh form (24/24 sources eligible),
# and the supervisor admits none (`cells-wca-` fresh refuses at R2). IN FORCE WITH NCA ADDENDUM 3. APPENDED.
