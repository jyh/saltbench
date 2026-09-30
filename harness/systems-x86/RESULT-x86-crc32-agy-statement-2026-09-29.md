# RESULT — x86 PoC, AGY ROW, `statement` × {plain, salt-diet} AT n = 3 (CRC-32, scalar x86-64)

## gemini (the agy row's hand), 2026-09-29. Registered design: `harness/systems-x86/AMENDMENT-x86-crc32-poc-2026-09-25.md` (PR #267,
## helm-signed as non-author), with its ADDENDA 1–16. plain and cell #1 of salt-diet ran on cut 5 = `ec67091` (ADDENDUM 13); salt-diet
## cells #2 and #3 ran on cut 6 = `3e9289c` under a memory ceiling (ADDENDA 14–16). Referee `referee_x86.sh` blob `8cfbf8113196`.

> ## ⛔ READ THIS BEFORE ANY NUMBER BELOW
> **This is ONE problem at n = 3 per arm. It carries NO effect size and NO premium** (§X8). **plain: 3/3 PASS** (AGREE=82), and a plain
> PASS says nothing about the statement, which plain cannot import (§1). **salt-diet: no cell landed a refereed pass.** Cell #1 was
> killed for box safety (CELL-KILLED, no ceiling). Cells #2 and #3 were ended by the memory ceiling (MEM-CAP). **Their END STATES,
> refereed under the same ceiling (§4), all agree with the executor on 82 of 82 inputs; #2 and #3 read CLASS SCREEN (a `sorry`), and
> #1's proof stage was killed at 8,000 MB.** An end-state verdict is printed BESIDE the cell's class, never as it (ADDENDA 14, 16). **The three salt-diet
> cells ran under TWO cap regimes and are never pooled** (ADDENDUM 14). **Each MEM-CAP cell's `ctl/end-1` reads `NO-SUBJECT-RAN`, which
> is FALSE** (§3, ADDENDUM 16).
> ⚠️ **Time order (ADDENDA 12–15):** plain ran first on 2026-09-26; salt-diet #1 followed it that day; salt-diet #2 and #3 ran three days
> later, on 2026-09-29. Every drift over that span falls on salt-diet alone, and its sign is not registered.

---

## 0 · PROVENANCE OF EVERY NUMBER IN THIS FILE

```
  end_marker, verbatim         each cell's own ctl/end-1, on the run box
  done_reason · turns · wall_s · false_done · mem_peak_mb
                               each cell's own ctl/agy-turnloop-1.json (done_reason, turns_sent, wall_seconds, false_done_claims,
                               mem_tree_peak_mb, which exists only where the ceiling was on, else "n/a")
  mem_cap_mb                   each cell's own ctl/caps.tsv, written at its launch (its `mem_cap_mb` row, or "none" where it has none)
  T_tokens · vendor_tokens · served · meter_verdict
                               each cell's own ctl/agy-meter-1.json (T, vendor_total_tokens, served_models, verdict), written by
                               agy_meter_v3.py from the client's stream at the cell's end
  class · tests · agreement · spec_strength · target · axioms · cell_translation
                               referee_x86.sh's out.json, per cell, run on the BUILD box on a hash-checked COPY of the cell's repo/,
                               with HARNESS = a clean worktree at the cell's own cut (ec67091 · 3e9289c; harness/systems-x86 and
                               tasks/ are byte-identical between them). For the three salt-diet END STATES, the referee's whole
                               process tree ran under an 8,000 MB kill (§4); where that kill stopped it before out.json was
                               written, `agreement` is the referee's own work/agree.out SUMMARY line, labelled so
  fire / clean times           the canary's ledger.tsv per wave, on the build box
  replay peaks (§3)            the systems branch's evidence-memcap-2026-09-29/memprobe.tsv and its curve files (commit 077ce5f)
```
The table in §2 was produced by one script over those files and is pasted here **verbatim, not typed**. The script is retained on the
build box and is not tracked here, because it names the run box; §7 says exactly what it reads. A missing source prints `MISSING`.
⚠️ **Declared gap:** the cells and the referee's out.json live on the run box and the build box, not in this repository, because they
carry host and account paths. A reader reproduces the table by re-running the referee and the meter against the cells.

## 1 · WHAT RAN
- **plain ×3 (`xaps01`–`03`)** and **salt-diet #1 (`xass201`)**, one wave from cut 5, by condition (ADDENDUM 13), 2026-09-26. Every view
  carried the statement hand-out asserted against its pinned blobs (statement `630a37ba2545`, spec `b336720df2e1`), with
  `ctl/statement=yes`. BATTERY GREEN, TMPDIR row OK, `a503=0` on every cell.
  **plain + statement is a DOCUMENT:** its `import Crc32X86Interface` resolves only in the salt-diet overlay, and a plain arm is refereed
  on its code alone, so these PASSes say nothing about the statement (the lead's ruling of 2026-09-26, as the Claude row carries it).
- **salt-diet #1, `xass201`, was ended by the operators at 15:08 PDT on 2026-09-26** with the run box at 27.4 of 28.7 GB swap (ADDENDUM 14).
  Its supervisor was stopped (rc 143), so the wave's cells #2 and #3 never started. It wrote no end marker, loop summary or meter, which
  is why its row reads `MISSING` in every column but `mem_cap_mb` (from its `caps.tsv`: none) and `agreement` (§4). Class: **CELL-KILLED** (level 6 §H6 row 6, not void). Its repo carries `LANDING.md`, added in
  commit `531b460` at 14:55:07 PDT, and the landing commit `e689590` ("landing 1") at 14:56:51 PDT. The first TERM of the stop was
  22:07:25Z = 15:07:25 PDT, so 12 min 18 s after the first and 10 min 34 s after the second. That fact is printed beside the class, never in
  place of it (ADDENDUM 15). Its tokens are UNMEASURED.
- **salt-diet #2 and #3, `xass301` and `xass302`,** fired from cut 6 under `AGY_MEM_CAP_MB=8000` (ADDENDUM 15), one supervisor, into a
  fresh staged root. Ledger: FIRE 14:57:48Z, CONDITION-CLEAN 15:33:55Z, `a503=0` on both. Each cell's `caps.tsv` carried
  `mem_cap_mb 8000`, and its loop printed `MEM-CAP ON` at launch. The ids are the condition's cells #2 and #3, which ADDENDUM 14 called
  xass202 and xass203.

## 2 · THE TABLE (verbatim output; tokens from each cell's own meter)

```
id	arm	n	end_marker	done_reason	turns	wall_s	false_done	T_tokens	vendor_tokens	served	meter_verdict	mem_cap_mb	mem_peak_mb	class	tests	agreement	spec_strength	target	axioms	cell_translation
xaps01	plain	1	2026-09-26T20:39:15Z LANDED landing-1 29dac11771fa	LANDED	3	199.2	0	1088001	156992	gemini-3.1-pro-high	OK	none	n/a	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
xaps02	plain	2	2026-09-26T21:19:20Z LANDED landing-1 b0890798501f	LANDED	3	217.0	0	1472654	192471	gemini-3.1-pro-high	OK	none	n/a	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
xaps03	plain	3	2026-09-26T21:23:28Z LANDED landing-1 10d68821dbcd	LANDED	3	214.5	0	854258	122395	gemini-3.1-pro-high	OK	none	n/a	PASS	PASS	AGREE=82	n/a	n/a	n/a	n/a
xass201	salt-diet	1	MISSING	MISSING	MISSING	MISSING	MISSING	MISSING	MISSING	MISSING	MISSING	none	MISSING	MISSING	MISSING	AGREE=82 (work/agree.out; out.json not written)	MISSING	MISSING	MISSING	MISSING
xass301	salt-diet	2	2026-09-29T15:14:22Z NO-SUBJECT-RAN phase-1 no turn and no tokens: no model was reached and NOTHING WAS SPENT. Infrastructure, not a statement about the arm (check the vendor credential window first)	MEM-CAP	2	925.5	0	0	0		VOID(NO-MODEL)	8000	8159	SCREEN	PASS	AGREE=82	None	n/a	n/a	n/a
xass302	salt-diet	3	2026-09-29T15:33:50Z NO-SUBJECT-RAN phase-1 no turn and no tokens: no model was reached and NOTHING WAS SPENT. Infrastructure, not a statement about the arm (check the vendor credential window first)	MEM-CAP	2	1122.1	0	0	0		VOID(NO-MODEL)	8000	8083	SCREEN	PASS	AGREE=82	None	n/a	n/a	n/a
```

**Reading the columns.** plain's `class PASS` is the referee's pass. For the salt-diet rows the referee columns are an END-STATE
verdict, printed BESIDE the cell's class (CELL-KILLED or MEM-CAP) and never as it. `xass201` has no end marker, loop summary or meter
(§1); its referee was killed at the proof stage before writing out.json, so only its agreement is printed, from `work/agree.out`.
`SCREEN` is a failure at the proof screen (§4); `spec_strength None` is the referee's own null for a cell stopped there. **For xass301 and xass302, `end_marker` and
`meter_verdict` are FALSE readings, printed verbatim as ADDENDUM 16 (3) requires:** the class is `done_reason MEM-CAP`, and their `T_tokens 0`
is not a zero (§3). `served` is empty for them because the meter found no result record to read a model from. `mem_peak_mb` is the
loop's own tree peak, which is the trip sample.

## 3 · THE TWO CEILING TRIPS, AND WHY THEIR END MARKERS ARE FALSE (ADDENDUM 16)
```
  cell     tripped at   tree peak   processes   largest process   results   stream step records   commands (meter)
  xass301  925.4 s      8,159 MB    8           5,703 MB          0         189                   23
  xass302  1,121.9 s    8,083 MB    7           5,223 MB          0         259 (last step 156)   34
```
Both trips came **inside the subject's first turn**, before the client wrote any result record. (`turns 2` in the table is the
opening's two sends: each cell's turns file has three lines, the loop sends all but the last up front, and holds the last, the
P-PERSIST probe, for the end. No continue turn had been sent.) The subject ran in both: it wrote and
tested `crc32.s`, ran the method's translation script, and (xass302) elaborated `Submission/Proof.lean` four times (steps 129–148).
**The launcher's P-RAN gate and the meter both read "no result record" as "no subject"**, and wrote `NO-SUBJECT-RAN … NOTHING WAS SPENT`
and `VOID(NO-MODEL)`, T 0. Both statements are false at the object. **Class `MEM-CAP` (ADDENDUM 16 (1)); price UNMEASURED (ADDENDUM 16 (2)),
never 0.** The client's own log carries no usage line, so nothing is printed in its place. The run box's free memory read 84 % at both
trips. The harness fix (P-RAN consults the loop's `done_reason`) is approved for a later cut only, and is not in this wave.
**Was it the pathology, or a heavy build the ceiling cut short?** Measured by replaying each cell's own final file ALONE, on a copy,
with the ceiling's own instrument and a 12 GB kill of its own:
```
  xass302  lake env lean Submission/Proof.lean        2,172 MB @22 s · 5,670 @65 s · 6,281 @86 s · 9,571 @108 s · KILLED 12,114 MB @115.8 s
  xass301  lake env lean Submission/TableEqTest.lean  2,201 MB @22 s · 5,753 @65 s · 6,231 @86 s · 10,617 @108 s · KILLED 12,170 MB @112.7 s
  xass201  lake build Submission.TableMatch           1,364 MB @16 s · 4,204 @48 s · 6,058 @81 s · 10,391 @113 s · KILLED 12,074 MB @118.6 s
  normal   lake build Submission, 9 landed cells      175 – 1,080 MB (agy none ×3, Claude none ×3, Claude statement ×3;
                                                      one, xasn01, is a failing build, rc 1, peak 176 MB like its siblings)
```
**In all three salt-diet cells, the subject's own table proof runs away when elaborated alone, along one curve shape** (a plateau near
6.2 GB around 86 s, then a climb). Each passes 11× the highest normal build. What the replay cannot say: which process held 5.2–5.7 GB
at each trip (they were dead before they could be measured), and whether the live run would have finished.

## 4 · THE THREE SALT-DIET END STATES, REFEREED UNDER THE CONDITION'S CEILING, 8,000 MB (the lead's ruling, 2026-09-29)
The referee runs TRANSLATE and both executors, which score tests and agreement, before its SCREEN and COMPILE/TARGET stages build any
Lean. Each end state was refereed on a hash-checked copy (digest equal before, after, and to the cell's own on the run box), inside
the fleet's one-heavy-job lock (the referee's Lean goes through saltbuild), with the whole referee tree under an 8,000 MB kill: the
condition's ceiling, the same for all three and never more. xass201's cell itself ran without one (§1).
```
  cell     referee end-state verdict                           tests   agreement   steps   referee tree peak   kill
  xass201  proof stage KILLED at the ceiling; no out.json      —       AGREE=82    82/82   8,023 MB            8,000 MB
  xass301  CLASS SCREEN · Submission/TableEqTest.lean:27 sorry  PASS    AGREE=82    82/82   1,189 MB            none
  xass302  CLASS SCREEN · Submission/Proof.lean:34 sorry        PASS    AGREE=82    82/82   1,183 MB            none
```
xass201's agreement and steps are from its `work/agree.out` (`SUMMARY AGREE=82`, `STEPS a+1==b on 82 of 82`), written at 08:44:19 PDT,
before the kill. **No tests verdict is printed for it**, because the referee wrote none.
⚠️ **A LIMIT OF THIS TABLE'S INSTRUMENT:** the wrapper also carried a 3,600 s wall cap, and that wall counted the time the referee
spent queued on the fleet lock (xass201's queued behind two other builds for most of its 1,915.9 s). A wall kill would therefore have
measured the queue, not the submission. **No row here was ended by the wall:** xass201 was killed by MEMORY (`killed mem`, 8,023 MB), and
xass301/302 finished in 266.3 s and 60.0 s. The stage that ran into the kill is the proof
stage (a Lean process after both executors), which the referee did not name, since it wrote no out.json.
⇒ **All three salt-diet routines agree with the harness's executor on all 82 withheld inputs (tests PASS for the two whose referee wrote
a tests verdict); none carries a proof the referee accepts.** Two
stop at a `sorry`, and the third's proof build is killed at the ceiling. Each cell's CLASS is unchanged: CELL-KILLED, MEM-CAP, MEM-CAP.

## 5 · THE REGISTERED PREDICTIONS (§X5), READ
- **(i) salt-diet's cap incidence ≥ plain's (TURNS-CUT or CAP-TOKENS on this row):** no cell hit either registered cap (plain's most
  turns 3 of 40; salt-diet's measured T is 0 by the meter's false reading, so its T is UNMEASURED). **The only caps that ended cells are
  ones §X5 did not name:** the operators' kill (xass201) and the memory ceiling (xass301, xass302), which bind salt-diet alone. §X5 (i)
  holds trivially on its own caps, and the file says that this is not the interesting reading.
- **(ii) every salt-diet cell that reaches TARGET reads the three standard axioms or is refused at AXIOMS:** NOT EXERCISED. No salt-diet
  end state got past SCREEN or the proof stage (§4).
- **(iii) no plain cell reads `cell_translation=differs`:** HOLDS, 3 of 3 (plain ships no Lean).

## 6 · WHAT THIS CANNOT ESTABLISH (§X8, registered before any data)
**No effect size and no premium** at n = 3 on one problem, and **nothing about models, other problems, or cross-lane**. **No contrast
between `none` and `statement`** is claimed: they ran on different cuts by design, and the pairing was never registered. **No contrast
between cap regimes** is claimed either: xass201 ran without the ceiling and xass301/302 with it, and they are never pooled
(ADDENDUM 14). 3/3 PASS against 0/3 refereed passes is not an arm result: the salt-diet cells were asked to write and prove a Lean
TARGET, and in each one the subject's own table proof ran away when elaborated (§3). **The ceiling is ARM-ASYMMETRIC by construction** (ADDENDUM 14),
and here it bound two of the three salt-diet cells. That asymmetry is the harness's, and it is printed beside the column it touches.

## 7 · HOW THE TABLE WAS PRODUCED (the retained script, described)
For each cell id, it reads, by one ssh per cell and read-only, the run box's `ctl/end-1`, `ctl/agy-turnloop-1.json` and
`ctl/agy-meter-1.json`. It then reads the build box's referee `out.json`. A condition split over two roots is numbered on, never
restarted (xass201 = n 1, xass301 = n 2, xass302 = n 3). Where out.json is absent, the agreement column reads the referee's own
`work/agree.out` SUMMARY line and says so; no other column is ever filled from a partial run. A missing source prints `MISSING` and is
never filled. It printed MISSING on one row, xass201, whose end marker, loop summary, meter and out.json do not exist (§1, §4). The
`mem_cap_mb` column is read from each cell's `ctl/caps.tsv`, which every cell has, xass201 included.
