# O37: web searches the agy client SERVED to subjects in 10 cells of record (2026-11-20)

**Finding.** The agy client's `search_web` tool returned a search summary to the subject on every call it was asked for:
96 calls in 12 cells on the run box, 96 served, 0 denied. Ten of the 12 cells are cells of record. `read_url_content` was
called 4 times and denied 4 times, by the client's permission layer ("permission check failed for read_url ... user denied
permission"). The canonical PreToolUse hook (`agy_web_deny_v3.sh`, registered in every one of these cells'
`.agyhome/.gemini/config/hooks.json`, deny list naming `search_web`) did not deny one call, and no record on the box shows it
ever denying one.

This makes two merged sentences false:
- level 6 ADDENDUM 6, A6.4 (and level 5 RESULT §D3, which quotes it): *"0 network-tool results were served"*, a census of the
  main streams; and A5.2's *"the builder reports 0 of the 48 served"*, by the same stream census;
- level 5 RESULT §D3: `l5psra202` *"carries 2 search_web CALL records and no result record, denied by the canonical hook"*.
  The two records are one call (ACTIVE, then DONE after 4.1 s). It was served.

**Why the stream census missed it.** The main stream (`ctl/stream-*.ndjson`) records a client-executed tool as a
`step_update` that goes ACTIVE then DONE and carries no result body, so a served call and a denied call look the same there.
The client's own conversation record (the "brain" transcript,
`<cell>/.agyhome/.gemini/antigravity-cli/brain/<conversation>/.system_generated/logs/transcript_full.jsonl`) records the call
in a PLANNER_RESPONSE step's `tool_calls` and its result in the next GENERIC step. For `l5psra202` that step reads
*"The search for ""verus" "failed this postcondition" forall exists" returned the following summary: The error message
**"failed this postcondition"** in Verus indicates ..."*.

**What this does to the record (the lead's ruling, bus 2026-11-20 00:29:42, helm-reversible).** No cell is voided: A5.2
registered that the fence *"does NOT claim the subject could not reach a web tool during a run"* and voids only FENCE-TAMPER.
Each cell of record below is declared **WEB-SERVED** in its RESULT. It keeps its verdict and **leaves every comparison**: an
input from outside the arm, of unknown sign. The table re-cuts, where a comparison loses a cell, are a separate change.

## Method

1. `web_brain_census.py` (run on the run box, read-only, zero spend) reads every brain transcript under `~/cells-*/` and, for each
   `search_web` / `read_url_content` call, classifies the next GENERIC step: SERVED (`returned the following summary`),
   DENIED (`permission check failed`, `denied permission`, `BLOCKED`), OTHER, or NO-RESULT. → `census.tsv`, one row per
   transcript and tool. `unserved.py` prints every non-served result in full → `unserved.txt` (the 4 denials).
2. `record_list.py` derives the agy cells of record from tracked files at the registration branch
   `bench/o37-statement-agy-registration-2026-11-17` (never typed) → `records.tsv`:
   MATRIX = `harness/systems-v3/CELLMAP-descriptive-tables-v2-2026-09-27.tsv`, gemini rows with status DONE (the 8 INEXPR rows
   carry no cell) · NA = `harness/systems-v3/RESULT-gemini-blockNA-2026-09-28-cells.tsv` · ZF = `evidence/zf-result/zf-cells.tsv`
   · WA = `evidence/blockWA-2026-11-14/cells.tsv` · WA-pro = `evidence/blockWA-pro-2026-11-15/cells.tsv` · TA =
   `evidence/blockTA-result-2026-11-20/cells.tsv`. 0 lines skipped.
3. `record_join.py` finds each cell of record on the run box (`<root>/<cell>` where the record names a root: NA, WA, TA; else
   by id over `~/cells-*`: MATRIX, ZF) and gives it one state: WEB-SERVED (at least one served result), CLEAN (at least one
   brain transcript read, none served), UNMEASURED (no brain transcript, or no directory). → `join.tsv`.

The tables below are printed by `python3 web_served_gen.py` from `join.tsv` and `census.tsv`; `--check` fails if this file
does not carry them verbatim.

```
  block    cells of record   WEB-SERVED   CLEAN   UNMEASURED
  MATRIX               272            3     269            0
  NA                    73            5      68            0
  ZF                   264            2     262            0
  WA                    12            0      12            0
  WA-pro                12            0      12            0
  TA                    72            0      72            0
  all                  705           10     695            0

  block    cell           model                   arm         search results served   network calls denied
  MATRIX   l5psra202      gemini-3.8-flash-high   salt-diet                        1                      0
  MATRIX   l6vbpp02       gemini-3.8-flash-high   plain                            1                      0
  MATRIX   l7npfs01       gemini-3.1-pro-high     salt-diet                        1                      0
  NA       nalsfp201      gemini-3.8-flash-high   plain                            7                      0
  NA       nalsfp202      gemini-3.8-flash-high   plain                           16                      1
  NA       nalsfp203      gemini-3.8-flash-high   plain                           22                      0
  NA       nalsfs202      gemini-3.8-flash-high   salt-diet                        3                      0
  NA       nalsfs203      gemini-3.8-flash-high   salt-diet                        3                      0
  ZF       zffpgns2a201   flash                   salt                             7                      1
  ZF       zffpbns101     flash                   salt                            19                      0
  served over the cells of record: 80
  #POPULATION transcripts=1775 unread=0 search_web:transcripts=12,calls=96,served=96,denied=0,other=0,no_result=0 read_url_content:transcripts=4,calls=4,served=0,denied=4,other=0,no_result=0
```

The other two cells with served searches, `l8zfps02` and `l8xfps03` (8 each), are not cells of record: they are in the
level-8 hidden-root wave (`evidence/l8-invalid-as-fired-2026-09-23/`) and in none of the files in step 2.
The first query of each cell of record is in `join.tsv`'s last column; among them, NA LinearScan's
*"Poletto" "Sarkar" "Linear scan register allocation" spill* names the algorithm's source paper, and ZF Paxos's
*"Paxos" "inductive invariant" verus OR dafny* names the proof the task asks for.

## Controls

- **Positive:** `l5psra202`, found by hand first, is in `census.tsv` at 1 call, 1 served.
- **The UNMEASURED state can fire:** two planted records (an id that exists nowhere, and a root that does not exist) read
  UNMEASURED 2 of 2. So the population's 0 UNMEASURED is not the join's default.
- **DENIED can fire:** the 4 `read_url_content` denials are classified DENIED, and `unserved.txt` prints their text.
- **The ambiguous ids:** 10 MATRIX ids exist in more than one cell family on the box (`s3cq01-03`, `s3ct01-02`, `l5cp01-03`,
  `l8cpss01`, `l8cpss03`); every family is read and all are CLEAN, so the state does not depend on which family is the record's.

## Copies of the false sentences (`copies_census.py`, flattened, at `origin/main`)

`copies-census.txt` is every window, over 805 tracked text files, that matches the web/deny needles in the script (hard wraps
undone first). 13 files hit, 23 windows, each read by hand:
- **Fall, corrected by addenda in this change:** level 5 RESULT §D3; level 6 AMENDMENT A5.2 ("0 of the 48 served") and A6.4.
- **Annotated in this change:** `PREDICTIONS-pricing-set-2026-09-06.md` "The internet is OFF in every scored cell" (false for
  the 10 agy cells of record above).
- **Stand, re-read:** level 6 AMENDMENT's DIAG-2 "0 web-class tool steps" and its "No web tool was called" (neither cell is in
  the 12); the Claude-lane receipts (a different client, not measured here); SCOUT and S2 hook text (other harnesses).
- **Owed to the lead, not edited here:** the paper's abstract, "a wall probed before any scored run isolates the agent from the
  network, reference solutions and harness". The Gemini-lane cells above are the counterexample.

## Limits

- The population is the brain transcripts under `~/cells-*/` on the run box (1,775). No brain transcript exists outside it
  (`find ~/bench-dry`: 0). Every cell of record has at least one, so no cell of record is UNMEASURED; a cell with a transcript
  that the client wrote only in part would still read CLEAN.
- A served result is a search SUMMARY the client wrote for the subject; what the subject did with it is not measured, and no
  verdict or cost is re-read here.
- The NOT-SERVED classes are matched by text. A denial worded otherwise would read OTHER, and is printed in `unserved.txt`;
  there are none.
- Swarm worker conversations are in the population (they live under the same `.agyhome`); none of them called a web tool.
- The Claude lane is NOT measured here.
- The tracked copies of `census.tsv`, `join.tsv` and `unserved.txt` have the home directory written as `~/`
  (`sed 's|/Users/<user>/|~/|g'`); the run-box originals are `census2.tsv` sha256 `6a2b2c5279ebe85f…`, `join.tsv`
  `224211fc66f8fc60…`, `unserved.txt` `7b570290bcc32098…`, in `~/bench-dry/gemini-webcensus-2026-11-20/`.

## ⚖️ NOTE, 2026-11-25 (bench, lead): appended; everything above is unchanged
Step 1's census reads the brain transcripts its glob reaches (`cells-*/*/.agyhome/…/transcript_full.jsonl`). A two-phase
cell's phase-1 conversation lives under `<family>/_aside/<id>/`, which that glob does not reach: 213 transcripts in 108 cells
of record (MATRIX 60, ZF 48). Read on 2026-11-25 by `../o37-agy-ctl-read-census-2026-11-25/` (which walks the cell and its
aside), they hold 0 `search_web` and 0 `read_url_content` calls. **No figure above moves:** WEB-SERVED 10 and CLEAN 695 stand.
The sentence "reads every brain transcript" did not cover them, and this note records that.
