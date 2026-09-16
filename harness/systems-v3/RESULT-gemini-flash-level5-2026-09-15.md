# RESULT — LEVEL 5, THE GEMINI **FLASH** GREENFIELD WAVE: **HALTED AT 21 OF 42; SCORES RECOVERED, 15 OF 20**
## bench (lead and hand), 2026-09-15. Freeze: `AMENDMENT-gemini-flash-level5-2026-09-14.md` §F0–§F6 + ADDENDA 1–4.
## Authorised by council 2026-09-14 ⑫(i). Fired 2026-09-15T01:29:52Z. Halted 12:13Z on a PRE-REGISTERED criterion.
## ⛔ **READ ADDENDUM 1 BEFORE §4. §4 SAYS THE SCORES ARE VOID AND ADDENDUM 1 SUPERSEDES IT:
## THEY ARE RECOVERED AND THEY ARE 15 OF 20.** §4 is left standing, unrewritten, as the honest record of
## what was known — **the route out changed, not the measurement.** ⚠️ This file's TITLE said `ITS SCORES
## ARE VOID` until 2026-09-15 16:2x, one line above an addendum of its own that says they are not.
## ⇒ 🔑 ***A TITLE IS NAVIGATION, NOT RECORD. LEAVING A SUPERSEDED SECTION STANDING IS HONEST; LEAVING A
## SUPERSEDED TITLE STANDING IS A TRAP, BECAUSE THE TITLE IS WHAT GETS QUOTED AND IT IS READ FIRST.***
## The same defect, in the same shift, in the sibling census file (§C5), by the same author — there the
## superseded block was quoted as the answer and a false finding was routed to the whole fleet.

## 1 · WHAT RAN
```
  population          §F1's 14 conditions x n3 = 42 cells, level 1's population mirrored exactly
  FIRED               21 cells (7 conditions)         NEVER FIRED  21 cells (7 conditions)
  LANDED              20        NOT-LANDED  1         built-but-unfired at the halt: 3 (zero spend)
  model               gemini-3.8-flash-high, model_requested read back FROM EACH CELL'S OWN RECEIPT
                      and asserted per condition; ZERO substitutions
  export              saltbench-systems-v3-export-9f650a3 (client_sha256 in every receipt, ⑫(1))
  containment         level 1's, unchanged — srt, p_exposure sensitive=3/10 (§4 of the 09-14 bus ruling)
```

## 2 · THE PER-CELL TABLE — `clean_s` IS THE COST FIGURE, NOT `cum`
`clean_s` sums the per-turn deltas of **SUCCESS turns only**; `cum` is the terminal `duration_seconds`.
They are equal exactly when a cell took no error turns. ⛔ **`cum` on an error-hit cell is capacity retry,
not model work** — the instrument that made this visible is in §5.
```
cell    condition           arm       SUC ERR  clean_s     cum            T   ok/run  end
l5cp01  crc32-plain         plain        3   0      278     278    3,993,025     1/33  LANDED
l5cp02  crc32-plain         plain        4   0      203     203    3,389,253     0/24  LANDED
l5cp03  crc32-plain         plain        3   0      311     311    5,838,876    24/48  LANDED
l5cs01  crc32-saltdiet      salt-diet    4   0      481     481   12,112,123    10/45  LANDED
l5cs02  crc32-saltdiet      salt-diet    4   0      513     513   11,452,788    15/49  LANDED
l5cs03  crc32-saltdiet      salt-diet    5   0     2090    2090   12,283,790    16/63  LANDED
l5fp01  freelist-plain      plain        4   0      371     371    4,850,397     7/24  LANDED
l5fp02  freelist-plain      plain        3   0      412     412    6,495,950     2/24  LANDED
l5fp03  freelist-plain      plain        4   0      349     349    6,748,970     0/22  LANDED
l5fs01  freelist-saltdiet   salt-diet    5   0      608     608   11,901,071    14/37  LANDED
l5fs02  freelist-saltdiet   salt-diet    6   0     5108    5108   57,655,873   60/183  LANDED
l5fs03  freelist-saltdiet   salt-diet    4   0      982     982   24,187,669    33/64  LANDED
l5lp01  lru-plain           plain        3   0      390     390    6,709,167     1/35  LANDED
l5lp02  lru-plain           plain        3   0      399     399    5,413,078    19/38  LANDED
l5lp03  lru-plain           plain        5   0      270     270    3,390,887     2/23  LANDED
l5ls01  lru-saltdiet        salt-diet    1   1       23     479    5,363,915    34/84  NOT-LANDED
l5ls02  lru-saltdiet        salt-diet    1   4       65    3586   24,067,847    16/47  LANDED
l5ls03  lru-saltdiet        salt-diet    0   5        0    3906   15,944,363    13/45  LANDED
l5pp01  paxos-plain         plain        1   3      226    1499    4,693,808     3/18  LANDED
l5pp02  paxos-plain         plain        3   0     1607    1607    5,954,935    10/28  LANDED
l5pp03  paxos-plain         plain        1   3      107    1654    5,566,217     1/23  LANDED
```
⚠️ **`T` CARRIES ITS COMPOSITION OR IT IS NOT A COST: 85–88 % CACHE READ, UNDER 1 % OUTPUT** (measured).
⚠️ **`ok/run` is PROVEN-OK COMMANDS of commands run** — see §6, it is not a pass rate.

## 3 · THE THREE BLOCKS, AND THEY ARE NOT COMPARABLE TO EACH OTHER
```
  CONDITIONS 1–5   15 cells   ZERO error turns on every cell; cum == clean_s        ✅ CLEAN
  CONDITION 6       3 cells   ALL THREE capacity-hit. l5ls03 LANDED with 0 SUCCESS turns
                              and clean_s = 0; l5ls02 landed on 65 s of 3,586.
                              l5ls01 ended NOT-LANDED on INVALID_ARGUMENT (400).    ⛔ CONTAMINATED
  CONDITION 7       3 cells   SPLIT: 2 majority-error (503), 1 wholly clean          ⚠️ MIXED
```
⇒ 🔑 ***A CELL CAN LAND HAVING DONE NO WORK AT ALL.*** `l5ls03`'s end marker reads `LANDED` and its five
turns are five `UNAVAILABLE (503)`. **This is the campaign's own landing caveat at its limit case, measured.**
⛔ **§F5's void list does not cover it** (its faults are: wrong served model · meter-blind · build wedge ·
fence fail · wrong field). **The freeze is NOT amended** — post-first-call, an amendment would be post-data.
The cells are reported as outcomes with their errors quoted, and the reading rules handle them at scoring.

## 4 · ⛔⛔⛔ THE SCORES ARE **VOID**, AND THE POSITIVE CONTROL IS WHY THIS FILE SAYS SO
The score stage completed cleanly — 7 conditions, rc 0, 20 cells, POOLABLE, zero fetch failures — and
reported **FULL PASS 0 of 3 on every condition; every cell `BUILD-FAIL`, `TESTS 0/0`.**
✅ **CONTROL, DRIVEN BEFORE ANY OF IT WAS BELIEVED:** the same scorer, run the same minute, on a **LEVEL-1
(Pro)** condition whose result of record reads `crc32-plain 3 of 3 FULL PASS, 6/6 tests each`:
```
  s3cp01 · s3cp02 · s3cp03   ->   BUILD-FAIL   TESTS 0/0      ⇒ it fails cells KNOWN to pass
```
⇒ **THE INSTRUMENT, NOT THE SUBJECT.** Root cause, reproduced by hand with the harness's own toolchain env:
```
  error: linking with `cc` failed: exit status: 69
  note: You have not agreed to the Xcode license agreements. Please run 'sudo xcodebuild -license'
  ⇒ proc-macro2 and indexmap BUILD SCRIPTS fail ⇒ nothing links ⇒ every cell reads BUILD-FAIL
  the SCORING box cc  -> REFUSES (the scorer builds here)   the RUN box cc -> CLEAN (the cells ran here)
  and each cell's own battery at run time: "cargo-build expected=pass got=pass rc=0 out=BUILT"
```
⇒ ***THE SUBJECTS' CODE BUILT SUCCESSFULLY ON THE RUN BOX. THE FAILURE IS ENTIRELY IN THE LOCAL SCORING
STEP.*** ⭐ **NO PASS/FAIL NUMBER FROM THIS WAVE MAY BE QUOTED**, and none appears in this file.
📌 **The block is `paris`'s registered Xcode-licence wall, whose scope was bounded to the LEAN toolchain.
It also voids SaltBench's RUST scoring path — a second campaign, a different language, the same `cc`, and
it fails with a GREEN rc.** Release: `sudo xcodebuild -license` on the scoring box — interactive, needs
sudo, **no seat can do it.** ✅ **Every artefact is intact; the 21 cells re-score unchanged once it lifts.**

## 5 · THE HALT — A PRE-REGISTERED CRITERION, AND THE CELL THAT PROVED WHY IT WAS WRITTEN DOWN
Registered before condition 7 had any data: *halt if ≥2 of 3 cells are majority-error.*
```
  l5pp01  1 SUCC / 3 ERR   YES        l5pp02  3 SUCC / 0 ERR   no        l5pp03  1 SUCC / 3 ERR   YES
  ⇒ 2 of 3  ⇒  FIRED
```
⭐ **`l5pp03` READ CLEAN MID-RUN** (`SUCCESS=1 ERROR=0 clean_s=107`) **AND THEN TOOK THREE 503s.** ⇒ ***HAD
I JUDGED ON THE SNAPSHOT I WOULD HAVE CONCLUDED "CAPACITY RECOVERED" AND CONTINUED.*** The criterion's own
wording — *"condition 7 RETURNS"* — is what stopped that. **A snapshot is not a verdict.**
**Halt executed by PID at both ends, verified dead, run box checked after; condition 8 was BUILT and
UNFIRED — zero model spend.** `exec-registry`: `HALTED-BY-REGISTERED-CRITERION`.

## 6 · WHAT THE WAVE DOES ESTABLISH, ALL OF IT ARM-FREE OR SIGN-ONLY
1. **Capacity boundary, sharp:** clean through **06:17Z**, degraded by **07:10Z**, still degraded at 12:13Z
   with one clean cell inside it. **Two error classes: `UNAVAILABLE (503)` and, once, `INVALID_ARGUMENT (400)`
   — the second is NOT the registered capacity risk and is unexplained (n=1).**
2. **Flash segments an episode exactly as Pro does** — 3–6 turns per cell, results spread through the
   stream. ADDENDUM 3's refutation now holds on 21 cells rather than the 1 it was built on.
3. ⚖️ **SIGN ONLY (freeze rule 1): salt-diet costs more than plain on both axes, on both problems with a
   clean pair** (Crc32, FreeList). **No magnitude and no ratio is published.**
4. **Cap incidence:** largest clean cell `l5fs02` at 57,655,873 T = **4.34× under the 250 M cap**. ⛔ Not
   compared to §F2's 9.96 % prior, which is **level 4 = BROWNFIELD**; this wave is greenfield, and that
   comparison would move model and field together.
5. **Proven-ok commands are NOT a pass rate and are reported as their own quantity:** 6 of 9 plain cells
   in conditions 1–5 landed having proven **≤2** commands worked. ⛔ **Not an arm claim** — volume and
   reverse causality are both live and the registered per-command-type instrument is unrun.

## 7 · WHAT IS OWED, AND BY WHOM
```
  the licence wall        the Captain's hand (sudo + interactive). NOT a seat act.
  re-score the 21         bench, the moment the wall lifts. Manifest builder and frozen harness ready.
  the 21 unfired cells    a SPEND: the helm's, then his. NOT re-fired on a seat's initiative.
  condition 6's re-fire   the same. Recommendation on the bus is AGAINST it.
  §F5's gap               a reading-rules question at scoring, NOT a post-data amendment.
```

---

# ✅✅ ADDENDUM 1 — **§4 IS SUPERSEDED: THE SCORES ARE NOT VOID. THEY ARE RECOVERED, AND THEY ARE 15 OF 20.**
## bench, 2026-09-15, ~1 h after this file was cut. **§4 above is left standing and NOT rewritten** — it
## is the honest record of what was known, and the route out of it is what changed, not the measurement.

## §A1 · THE ROUTE, AND IT CAME FROM THE HELM
`§4` reported the scores VOID because `cc` on the scoring box refuses on the Xcode licence wall. **The
helm had measured a route past it and my transcript showed I had never received it** (`DEVELOPER_DIR`:
0 occurrences against a control of 27):
```
  DEVELOPER_DIR=/Library/Developer/CommandLineTools
  the helm drove it on a real compile AND link: default cc rc 69 · CLT route rc 0 · a binary that runs
  ⛔ ITS STATED LIMIT: measured for `cc`, UNMEASURED for cargo's BUILD SCRIPTS — "drive it before you trust it"
```
✅ **I DROVE THE UNMEASURED CASE, ON THE KNOWN-GOOD CONTROL FIRST.** Level-1 cell `s3cp01`, whose result
of record reads `3 of 3 FULL PASS, 6/6 tests each`:
```
  DEVELOPER_DIR=… run_tests.sh  ->  rc 0 · PASS x5 · TESTS 6/6      ⇒ matches its record EXACTLY
```
⇒ **The limit is now measured: the CLT route carries cargo's build scripts.** The control that condemned
the scores is the same control that cleared them — **run in both directions, an hour apart.**

## §A2 · THE SCORES, RE-RUN WHOLE
```
  crc32-plain        3 of 3        crc32-saltdiet       3 of 3
  freelist-plain     1 of 3        freelist-saltdiet    0 of 3   (1 TRUNCATED)
  lru-plain          3 of 3        lru-saltdiet         2 of 2   (1 TRUNCATED)
  paxos-plain        3 of 3
                                                   ⇒ 15 of 20 FULL PASS
```
⚖️ **NO PASS-RATE COMPARISON BETWEEN ARMS IS PUBLISHED HERE, AND THE REASON IS LEVEL 1's, UNCHANGED:**
the denominators are not neutral (`lru-saltdiet` is 2, not 3 — its third cell is the one that ENDED
NOT-LANDED on the 400), and **every missing cell is salt-diet.** A rate over those denominators is
measured on a treatment arm with cells removed by a mechanism whose incidence is itself arm-correlated.
⛔ **And conditions 6–7 remain capacity-contaminated** (§3): `l5ls02` and `l5ls03` are in the `lru-saltdiet`
2 of 2 **having done 65 s and 0 s of model work respectively.** ⇒ ***A FULL PASS BY A CELL THAT DID NO
WORK IS A FACT ABOUT THE TASK, NOT ABOUT THE MODEL***, and it is flagged here rather than pooled away.

## §A3 · WHAT §4's FINDING BECOMES — SMALLER, BUT NOT WRONG
The wall was real, it did void the scores, and **the block's scope IS wider than registered** — it was
raised against the Lean toolchain and it silently voids this Rust scoring path, with a green rc. **What
changes is that it is BOUNDED and has a seat-level route**, not that it was imaginary.
⇒ 🔑 ***A BLOCK WITH A ROUTE NOBODY ROUTED TO THE BLOCKED PARTY IS INDISTINGUISHABLE, FROM INSIDE, FROM A
BLOCK WITH NO ROUTE AT ALL.*** I had measured the wall correctly, reported it correctly, and stopped —
and the thing I was missing was not a measurement but a message.

---

# ✅ ADDENDUM 2 — **THE LICENCE IS DISCHARGED AT SOURCE, AND THE SCORES REPRODUCE WITHOUT THE WORKAROUND.**
## bench, 2026-09-15, council close. The Captain accepted the Xcode licence at the table; ADDENDUM 1's
## `DEVELOPER_DIR` route is no longer needed, and this addendum exists because I re-ran it rather than
## assuming the discharge.
```
  PLAIN scorer, DEVELOPER_DIR explicitly UNSET     FULL PASS 15 of 20
  CLT route (ADDENDUM 1)                           FULL PASS 15 of 20
  ⇒ IDENTICAL, condition for condition
```
⇒ **Two independent routes, one answer.** ⭐ **Why this is worth a paragraph rather than a silent edit:**
the discharge was reported to me, and a reported fix is a claim about a box I can check. **Re-running the
PLAIN scorer tests the claim; quoting ADDENDUM 1's numbers would only have re-quoted my own.**
📌 **Operationally: conditions 6–8 and the 21 unfired cells need NO toolchain workaround when they are
re-fired** — the scoring path is clean at source.


---

# ✅✅ ADDENDUM 3 — **LEVEL 5 IS COMPLETE: 27 OF 27 CELLS LANDED AND SCORED, 25 FULL PASS**
## bench (lead), 2026-09-16. `gemini` was the hand; the wave ran 14 h 44 m unattended and ended rc=0.
## **Every figure below was re-read by the lead from the per-condition receipt files, not retyped from
## the hand's report.** The hand's report was correct in every figure checked.

## §C1 · THE NINE CONDITIONS
```
  condition                  attempt  FULL PASS   tests                 truncated
  lru-saltdiet   (re-fire)      3       3 of 3    16/16 x3                  0
  paxos-plain    (re-fire)      1       2 of 3    17/17, 17/17, 16/17       0
  paxos-saltdiet (re-fire)      2       2 of 3    17/17, 17/17, 16/17       1
  crc32-plain-stmt              1       3 of 3    6/6 x3                    0
  crc32-saltdiet-stmt           1       3 of 3    6/6 x3                    0
  freelist-plain-stmt           1       3 of 3    7/7 x3                    0
  freelist-saltdiet-stmt        1       3 of 3    7/7 x3                    0
  lru-plain-stmt                1       3 of 3    16/16 x3                  0
  lru-saltdiet-stmt             1       3 of 3    16/16 x3                  0
  -----------------------------------------------------------------------------------
  27 cells . 27 LANDED . 25 FULL PASS . 2 FAIL (both Paxos, both 16/17) . TRUNCATED 1
```
⛔ **THIS IS NOT A COLUMN TO SUM.** It holds two populations: three **re-fired** conditions that replace
503-contaminated conditions of this wave's first run, and six **new** statement conditions.

## §C2 · ⛔ THE STATEMENT ARM IS AT A CEILING, AND THAT IS A PROPERTY OF THE SCORED POPULATION
**18 of 18 statement cells passed every test**, with 0 truncations. ⇒ **The pass-rate instrument cannot
produce a difference between arms on these tasks.** A measurement with no variance is not a weak one but
an absent one, and no increase in n lifts it. The correct entry is therefore **not** "no difference
found" but **"this instrument cannot produce a difference"** — a limitation of the scored population.
⚠️ The controls that went red were drawn from other tasks. That proves the red path is live **in the run**;
it does not prove **these tasks** can go red. A task that has never failed is one whose difficulty is
unmeasured, not one shown to be passable.
⚠️ **A "margin" cannot rescue this from the pass side**: distance-to-failure is undefined for a cell at
n/n. The instrument that measures it is mutation analysis, which is a spend and not a re-read.

## §C3 · TRUNCATION, AS A COUNT
```
  plain       0 of 21 cells  (7 conditions)
  salt-diet   4 of 23 cells  (8 conditions)
```
All-treatment, zero-control, in every wave measured. **This is a COUNT and is not claimed as an effect.**
A per-turn deadline can only bind the arm whose turns run longer, so the two arms are not measured under
the same regime. For TOKENS the bias is conservative (a cut turn understates salt-diet's T, pushing any
premium down); for CORRECTNESS its sign is unmeasured. **It is owed a registration before the next wave,
so that it can be tested rather than accumulated.**

## §C4 · WHAT THIS ADDENDUM DOES NOT DO
1. **No arm contrast, ratio or premium is computed** (§F4 rule 1).
2. `l5psra202`'s cost figures remain **unpoolable** (truncated; its PASS stands as a floor).
3. `l5psr01` remains a **recorded set-aside**: citable, never tabled.
