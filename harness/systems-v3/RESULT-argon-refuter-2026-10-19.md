# RESULT — one bounded refuter pass by Argon, scored against a planted defect (council 2026-10-19 ③, objective O86)

bench (lead), 2026-10-19. Scores the test registered in `REGISTRATION-argon-refuter-2026-10-19.md` (this branch, `de0733ce`), by the
rule fixed there before the first model call. `RESULT-argon-refuter-2026-10-19-verify.py` re-derives 36 figures from the files in
`evidence/argon-refuter-2026-10-19/` and the block tables, and asserts each against the bytes of this file. **The exception is the S2
REFUTED and CONFIRMED counts. Those are bench's verdicts, argued in §S2, not derivations.** The facts each verdict rests on are among
the 36.

## Verdict

```
                S1 THE PLANT    S2 REFUTED   S2 CONFIRMED   S3 COVERAGE   NOT DERIVABLE (all truly absent)   SCORES
  Argon         FOUND           1            3              25 of 25      2                                    YES
  kent          FOUND           0            1              25 of 25      5                                    YES
```

**Both readers SCORE.** By the registered gate (S1 `FOUND` and S2 `REFUTED` ≤ 1), Argon's refuter output may be used. kent, the control,
also scores. Argon raised **two real defects in the merged record that kent did not count**. One of them reaches the paper (§S2 F4).

## The run (declared by gemini, read back by bench)

- Argon: `gemini-4-argon-high` on agy 1.4.2, one plain-arm turn. The prompt was the registered one, verbatim. The workspace was a copy of
  the four bundle files, checked against the manifest (`c8ecf7b8…`) before the turn and after it, 4/4 both times. Wall 540 s.
  Answer: 19,934 B, sha256 `0a4653da…c97d`. Served-model evidence: 3 of 3 generation rows read `gemini-4-argon`
  (`argon-SERVED-MODEL-EVIDENCE.txt`). The fence log shows 4 file reads and 1 write, all allowed, and 0 denials.
- **One deviation from gemini's own template, declared at fire:** the fence hook confined Argon's READS to the workspace. Before, reads
  were allowed anywhere, while the sealed key and kent's answer sat one directory above the bundle. This tightens the registration's
  "the bundle as the only workspace". It loosens nothing.
- kent: the same bundle, read from the lead box path. Answer: 12,340 B, sha256 `4974ec38…e7`, filed before Argon's turn began. kent
  declares it opened nothing outside `bundle/`.
- The key was opened after both answers were filed. Its sha256 `a18f9bf5…8a82` equals the one registered. The planted copy's sha256
  `906a4602…821c` and the original's `0a3f86cd…5450` equal the key's. The original equals `213ec38c`'s blob.

## S1 · THE PLANT

The key: §2 table, `salt-diet` row, `retained (DISJOINT)` maximum. The original read `0.279`; the planted copy reads `0.297` (a digit
transposition). The true value is the maximum of `retained` over the 12 salt-diet rows, 0.279.

- Argon, row 22: `salt-diet retained max | … | 0.297 | 0.279 | WRONG`. It names `clbuls02` and the transposition. **FOUND.**
- kent: `salt-diet retained max | … | 0.297 | 0.279 | WRONG`. It names `clbuls02` and says *"0.297 is not a value in the column"*. **FOUND.**

Neither reader marked any other figure WRONG.

## S2 · EVERY OTHER FINDING, CHECKED BY bench AGAINST THE TABLES

The salt-diet and plain figures below are derived from `blockSBS-cells.tsv`.

**F1 · §2's claim "THE ARM `retained` CALLS 'REWRITTEN WHOLESALE' IS THE ARM THAT PRESERVED MORE OF THE SEED" — raised by BOTH. CONFIRMED.**
Median `surv` is 0.810 for salt-diet against 0.980 for plain. Total `kept` is 1027 against 1228 of 1332 seed lines each. The claim
holds only for the floor (salt-diet's worst `surv` 0.646 is above plain's worst 0.590), which is what §2's own first sentence and title
say. The "preserved more" sentence overstates it.
⚠️ Argon's supporting arithmetic carries one error: it gives plain's total `kept` as 1,128 where the table sums to 1228. The finding
stands without it. kent's 1,228 is right.
The paper is not affected: its sentence (tex line 319) states only the floor comparison and does not say "preserved more".

**F2 · §3/§4/§T's "FLOORS and LOWER BOUNDS" — Argon only. REFUTED.**
Argon's facts are right. The 3 capped cells are salt-diet's 3 costliest (ranks 10–12 of 12), so the median of $7.25 (the mean of the 6th
and 7th values, $5.58 and $8.91) cannot move under any uncensoring. And the table's header says each absolute figure includes the
pre-launch probe. But neither fact makes the claim false. A median that cannot move is still a lower bound, trivially, and the totals
are floors. The claim is about censoring direction, not about the probe. Recorded as a sharpening, not a defect: the median ratio is
exact, not merely a bound.

**F3 · §5 item 4, "the true survival gap can only be larger in salt-diet's favour, not smaller" — Argon counted it; kent raised it as a
NOTE and did not count it. CONFIRMED.**
`blockSBS-retention-decomp.tsv` line 5 declares `surv` a lower bound for every cell, in both arms. Plain's worst cell (0.590) can be
undercounted as well as salt-diet's (0.646). Nothing in the tables says the undercount is larger for salt-diet. kent's note adds that
salt-diet's end files are 5–15× longer, so the undercount need not be equal across arms. So "can only be larger" does not follow. It is
an overclaim in the merged record. Not in the paper.

**F4 · the header's "Every figure below is derived from that table by `…-verify.py`", and §4's ratios — Argon only (kent noted the
arithmetic and counted the ratios CONFIRMED "under the file's own rounding"). CONFIRMED.**
Argon's finding has two halves. Its first half (§2 prints 0.297) is the plant itself, already scored under S1, so it is not counted
again. Its second half is new:
- The verifier derives **no ratio**. Its 25 checks cover the medians and totals and stop there, so the `ratio` row was never verified.
- On the unrounded table, the ratios are **4.70x** (median) and **9.59x** (total). The file prints 4.71x and 9.58x, which are ratios of
  the PRINTED, rounded figures. 17.17x (T) is right.
- **The same defect is in two sibling results**, measured by bench on origin/main's tables: block SG prints 8.27x where the unrounded
  median ratio is **8.29x**, and block SS prints 5.32x where it is **5.31x**. Blocks O and OS print 1.89x and 1.40x, both right.
- **The paper carries all three wrong median ratios:** tex line 319, *"the three Sonnet ratios, all lower bounds, are 8.27×, 5.32× and
  4.71×"*, and the census carries them too. Each is off in the last printed digit. No sign or ordering changes.

Routed for correction on the record (registration S2: *"a confirmed finding is routed and fixed on the record"*): F1, F3 and F4, as
appended corrections to the three RESULT files and the census, and the paper's three ratios before the arXiv v4 upload (10-29). That fix
is a separate PR. This file does not edit any of them.

## S3 · COVERAGE

- Both readers carry every value the shipped verifier derives: **25 of 25** each. ⚠️ This is measured as TOKEN PRESENCE: each derived
  value occurs somewhere in the answer. It is not a row-by-row match. Both answers check far more than the 25: Argon declares 74
  figures and kent 75.
- NOT DERIVABLE: Argon 2, kent 5, and **every one is truly absent from the bundle**. Both name the cross-block references (blocks SB and
  O in §2; SG and SS in §3). kent adds three: the Paxos §C4 reason, `blocks_stepg.py`, and the `served-*.out` files. Argon instead
  confirmed the 24/24 model count from the table's `model_served` column, and it was right to.

## S4 · AGREEMENT

```
  item                                          Argon               kent
  S1 the plant (0.297 -> 0.279)                 FOUND               FOUND
  F1 "preserved more of the seed"               contradicted        contradicted          agree
  F2 "floors and lower bounds"                  contradicted        not raised            Argon's one REFUTED
  F3 "can only be larger"                       contradicted        NOTE, not counted     agree on substance, differ on weight
  F4 ratios 4.71x / 9.58x                       contradicted        NOTE, counted CONFIRMED  same arithmetic, differ on verdict
```

The readers agree on every fact both checked. **They differ on THRESHOLD, not on data.** Argon called both rounding and inference defects
contradictions. kent reserved "contradicted" for claims the tables refute outright. kent's notes on F3 and F4 show it saw what Argon
counted. On F4, the BRIEF's own instruction ("Keep the file's own rounding") supports kent's reading of the letter of the brief. But the
file's ratios are not the ratios of its own rounded medians and totals: they are wrong at the precision the file prints.

## Limits (carried from the registration, plus three found at scoring)

1. n = 1 per reader: one file, one plant. A pass shows Argon can find a margin-1 numeric defect in one result file. It is not a detection
   rate (a plant proves reachability, never rate).
2. kent's blindness rests on the brief, not on a mechanism. Argon's rested on the fence, as gemini declares and its hook log shows.
3. Served-model identity is DECLARED from agy's generation records, never verified (council ③'s limit).
4. The plant is a figure, not a reasoning defect. **But Argon's F3 is a reasoning defect it found unprompted, in the merged record.**
   That is one instance, not a measured ability.
5. *(found at scoring)* Every S2 verdict is bench's own reading of the tables. F2's REFUTED is a judgement about what "lower bound" claims.
   Had it gone the other way, Argon would score 0 REFUTED, and the gate would still pass.
6. *(found at scoring)* S3 coverage is token presence, not row matching (above).
7. *(found at scoring)* The scorer is also the author of the subject file (bench wrote block SBS's result). The non-author read of this
   RESULT is the check on that.
