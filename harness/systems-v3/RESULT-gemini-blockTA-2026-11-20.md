# RESULT — O37 block TA · the agy lane × block N's six problems × `statement` × greenfield · n = 3 · gemini-3.8-flash-high and gemini-4-argon-high
### gemini (the hand), 2026-11-20, on the hand's own files; the lead (bench) reads it before it is quoted (bench's assignment, bus offset 107,190,349). **24 conditions, 72 cells. §TA6: "a result of record per model": §2 is Flash's, §3 is argon's, never pooled.**
## 📌 The registration is `AMENDMENT-O37-statement-six-agy-2026-11-17.md` (§TA0–§TA6, signed by the helm 2026-11-17; ADDENDA 1–3 released it; ADDENDUM 4 the roots; ADDENDA 6–7 the client; ADDENDA 5 and 8 the price re-cuts).
## 📌 The per-cell table of record is `evidence/blockTA-result-2026-11-20/cells.tsv`, printed by `ta_result_gen.py` beside it from TRACKED copies of the hand's record (`ta_collect.py`: the two tallies, `cell_facts.json`, `receipts.tsv`, `meters.tsv`) and two read-only censuses taken on the run box (`events.tsv` by `ta_events.sh`, `swarm.tsv` by `ta_swarm_census.py`). The README there lists every input.
## ⛔ Every figure line in a code block below is printed by `ta_result_gen.py --summary`, and `ta_result_gen.py --check` on this file asserts each one occurs here verbatim. Bus offsets and clock times in the prose are citations, not measurements.
## ⚖️ §1.4's four cells (Claude workers inside Flash cells) are RULED by the lead, bus offset 107,197,659: COUNTED as PASS cells of record, flagged MODEL-SEAM, OUT of every Flash comparison by the truncation rule, cost a lower bound. The search the ruling made a condition is in §1.4.

---
# §1 · WHAT RAN, AND ON WHAT
```
flash: cells 36 · scored 36 · PASS 36 · FULL PASS 36 · receipts 36
flash requested_model gemini-3.8-flash-high=36
flash served_models gemini-3.8-flash-high=36
flash export_sha 397864e860af=36
flash done_reason LANDED=36
argon: cells 36 · scored 36 · PASS 36 · FULL PASS 36 · receipts 36
argon requested_model gemini-4-argon-high=36
argon init_model gemini-4-argon-high=36
argon served_models gemini-4-argon-high=36
argon export_sha 397864e860af=36
argon done_reason LANDED=36
```
1. **ONE EXPORT FOR ALL 72 CELLS: saltbench-systems `397864e8`**, ADDENDUM 1's, built with `cell_build.py --client agy --statement`.
2. **THE CLIENTS.** agy's binary is hashed at each cell's launch (`client_sha256`, from the cell's own `built-from.tsv`):
```
flash client 62f2102784bb74b7: 13 cells
flash client 780ee763a9938a37: 22 cells
flash client ef265356c3e5d3c6: 1 cells (tamfs301)
argon client 62f2102784bb74b7: 36 cells
```
   - `780ee763` is agy 1.5.10, the release's client (ADDENDUM 2). It self-updated to 1.5.11 `62f21027` through the wave's own credential
     warm-up; ADDENDUM 6 made `62f21027` the client of record for every cell not yet fired. It self-updated again to 1.5.12 `ef265356`
     through the wave's `/usage` read; ADDENDUM 7 restored `62f21027` and made the client's directory unwritable for the rest of TA.
   - ⇒ **Flash carries a declared CLIENT SEAM**: Luby, AES and Liveness on `780ee763`; MaxFlow holds all three clients (4 cells on
     `780ee763`, `tamfp301` on `62f21027`, `tamfs301` on `ef265356`, which ADDENDUM 7 item 3 counts with its client declared);
     BinomialHeap and LinearScan on `62f21027`. **Argon is on one client, `62f21027`, in all 36.** Every per-condition line below names
     its clients.
3. **WHICH 72.** The tripwires are `talfs101` (T-TA-F, Flash · Luby · salt-diet#1) and `talas101` (T-TA-P, argon · Luby · salt-diet#1),
   each read by the lead before its model continued. One attempt was discarded on a 503 and re-queued under a new root, as the canary
   wave's rule says; it is not a cell of record, and `events.tsv`/`swarm.tsv` carry it so the census's population is visible:
```
cell dirs on the run box not of record: 1: tamfp201 cells-ta-maxflow-flash-plain-r2.DISCARDED-503-2026-11-18T05:06:38Z
```
   Its condition's cell of record is `tamfp2a201` (root `cells-ta-maxflow-flash-plain-r2-a2`).
4. **⚠️ CLAUDE WORKERS INSIDE FOUR FLASH CELLS (MODEL SEAM, ruled).** `init_model` is the set of `"model"` values in the cell's main
   stream (`wa_facts.py`), and it reads more than Flash in four Flash cells:
```
flash init_model claude-opus-5-5-high,claude-sonnet-5-5-high,gemini-3.8-flash-high=1 claude-opus-5-5-medium,claude-sonnet-5-5-medium,gemini-3.8-flash-high=1 claude-sonnet-5-5-high,gemini-3.8-flash-high=2 gemini-3.8-flash-high=32
flash swarm workers added in 4 of 36 cells (swarm.tsv read 36): talfs201=claude-sonnet-5-5-high,claude-opus-5-5-high tavfs301=claude-sonnet-5-5-high tabfs301=claude-sonnet-5-5-high tasfs301=claude-sonnet-5-5-medium,claude-opus-5-5-medium
argon swarm workers added in 0 of 36 cells (swarm.tsv read 36): -
```
   In each of the four the subject called the client's `swarm` tool, listed the models it offers, and ADDED workers on Claude models,
   which it later killed (`swarm.tsv`). The census covers every TA cell dir (73): 4 Flash salt-diet cells used the tool, and no argon cell did.
   **WHAT THE WORKERS DID, read from their own records** (`workers.txt`, `ta_worker_read.py`). The main stream does not carry a worker's
   turns, but the client keeps each worker's conversation in the cell's own agy home, under `brain/<worker id>/`, found by the ids in the
   `add` outputs. All six workers' records are present (searched: the cell dir, its root, and the client's global directory on the run
   box, where no worker id occurs). Their responses carry only the requested Claude model; each ran 1–2 minutes.
   - Every worker acted as the salt method's REFUTER (`worker-sonnet`) or REVIEWER (`reviewer`), briefed by the Flash subject.
   - Each refuter WROTE ONE TEST FILE under `tests/refute/` (`refute_a.rs`, `r1.rs`, `probe.rs`, `clobber.rs`), ran it, and posted a
     verdict to the swarm's board. All four files are in the cell's final tree, added by the subject's next commit after the worker's
     window. `tasfs301`'s reviewer also wrote `docs/reviews/review-1.md`, which the same commit added.
   - **No worker wrote `solution.rs`, `interface.rs` or `LANDING.md`.** Every argument naming one of them is a read (`cat`, `sed -n`,
     `grep`) or advice inside a post. No commit falls inside any worker's window.
   - So the scored solution is the Flash subject's text, but the subject READ Claude workers' refutations and reviews before committing
     it, and the cell's own test tree carries a file a Claude worker wrote. That influence is why the lead keeps the four out of every comparison.
   `meters.tsv`'s served set reads Flash in all 36 Flash cells, but the meter reads the main conversation only. The workers' tokens are in
   `workers.txt`. Which pool billed them is not in any record read, so it is UNMEASURED. The lead's ruling (bus offset 107,197,659) keeps the
   four as PASS cells of record, flagged, OUT of every Flash per-condition comparison, ratio and category tally read as "what Flash did",
   and their cost a lower bound. Arm (b), a void under §TA0 row 1, was rejected because that row was written for a served-id mismatch on the
   subject, and the subject is Flash in all four.
5. **THE MODEL COLUMN**, as in WA: `requested_model` is what the harness asked for, `served_models` is the meter's set from the main
   conversation, and `init_model` is the stream's model values. Neither is a served set in the Claude lane's sense.

---
# §2 · gemini-3.8-flash-high — THE RESULT OF RECORD (CLIENT SEAM declared, §1.2; four cells FLAGGED, §1.4)
```
flash Luby plain: PASS 3 of 3 [12/12 12/12 12/12] · truncated 0 (events 0; print-timeout lines 0) · interface 1bda4459679b1bf1 · clients 780ee763
flash Luby salt-diet: PASS 3 of 3 [12/12 12/12 12/12] · truncated 0 (events 0; print-timeout lines 0) · interface 1bda4459679b1bf1 · clients 780ee763
flash AES plain: PASS 3 of 3 [8/8 8/8 8/8] · truncated 0 (events 0; print-timeout lines 0) · interface dd4b759c2c3a60e7 · clients 780ee763
flash AES salt-diet: PASS 3 of 3 [8/8 8/8 8/8] · truncated 0 (events 0; print-timeout lines 0) · interface dd4b759c2c3a60e7 · clients 780ee763
flash Liveness plain: PASS 3 of 3 [11/11 11/11 11/11] · truncated 0 (events 0; print-timeout lines 0) · interface 87ecc3aa5a6eea59 · clients 780ee763
flash Liveness salt-diet: PASS 3 of 3 [11/11 11/11 11/11] · truncated 0 (events 0; print-timeout lines 0) · interface 87ecc3aa5a6eea59 · clients 780ee763
flash MaxFlow plain: PASS 3 of 3 [8/8 8/8 8/8] · truncated 0 (events 0; print-timeout lines 0) · interface 94fa3a69d109dd9b · clients 62f21027,780ee763
flash MaxFlow salt-diet: PASS 3 of 3 [8/8 8/8 8/8] · truncated 0 (events 0; print-timeout lines 0) · interface 94fa3a69d109dd9b · clients 780ee763,ef265356
flash BinomialHeap plain: PASS 3 of 3 [13/13 13/13 13/13] · truncated 0 (events 0; print-timeout lines 0) · interface e440fb9aa198280c · clients 62f21027
flash BinomialHeap salt-diet: PASS 3 of 3 [13/13 13/13 13/13] · truncated 3 (events 4; print-timeout lines 12) · interface e440fb9aa198280c · clients 62f21027
flash LinearScan plain: PASS 3 of 3 [9/9 9/9 9/9] · truncated 0 (events 0; print-timeout lines 0) · interface 6c675da1f3171e38 · clients 62f21027
flash LinearScan salt-diet: PASS 3 of 3 [9/9 9/9 9/9] · truncated 2 (events 2; print-timeout lines 6) · interface 6c675da1f3171e38 · clients 62f21027
```
- **Every Flash cell passes the withheld G suite in full**, on every problem and both arms (the referee's own runner at `397864e8`, on a
  copy). Every condition is at CEILING, so nothing here separates the arms by pass rate. No pass count turns on the four §1.4 cells:
```
flash salt-diet PASS, swarm cells OUT: 14 of 14
```
- **WHAT IS LEFT FOR A COMPARISON.** A truncated cell and a §1.4 cell keep their PASS and leave every per-arm comparison (the lead's rulings):
```
flash comparison n per condition, truncated and swarm cells OUT: Luby plain 3 · Luby salt-diet 2 · AES plain 3 · AES salt-diet 3 · Liveness plain 3 · Liveness salt-diet 2 · MaxFlow plain 3 · MaxFlow salt-diet 3 · BinomialHeap plain 3 · BinomialHeap salt-diet 0 · LinearScan plain 3 · LinearScan salt-diet 1
```
- **TRUNCATION.** A truncated cell had at least one turn cut by the registered 1800 s print deadline. Its PASS stands as a FLOOR; its
  token, turn and wall figures are NOT POOLABLE and are EXCLUDED, named, from every per-arm comparison (helm ruling 2026-09-11; the lead
  for TA at bus offsets 106,348,486 and 106,389,932):
```
flash truncated 5 cells, 6 events, 18 print-timeout lines (scorer figure 18): tabfs101=1/3 tabfs201=2/6 tabfs301=1/3 tasfs201=1/3 tasfs301=1/3
```
  Each pair is `events/lines`. **EVENTS** are `^AGY_ERROR` lines in the cell's `ctl/agy-stderr-1.txt`, one per timeout. **LINES** are
  `print timeout` lines in the same file, three per event; the scorer's `TRUNCATED` figure (`score_wave_v3.sh:281`) and `wa_facts.py`'s
  `cut_turns` both count LINES, so `tabfs201`'s scorer `6` is 2 cut turns. `events.tsv`'s population is every TA cell dir: 6 truncated
  cells across both models, 0 elsewhere.
- **THE STATEMENT LINE: did the subject use, ignore or contradict the statement (§TA2's extra tripwire line).** Categories as the lead
  ruled them (bus offsets 106,504,279, 106,539,735, 106,587,008; EXEC USE by THE LINE, 107,185,047), one per cell, read from the head of
  the tally's `statement` cell:
```
flash plain categories: EXEC USE 2 · EXEC USE (partial) 1 · TEST ORACLE 8 · TEST ORACLE (partial) 1 · WEAK TRACE 2 · NO TRACE 4
flash salt-diet categories: USED 15 · USED (partial) 2 · SPEC TRANSCRIBED, CONTRACT ABSENT 1
flash salt-diet categories, swarm cells OUT: USED 13 · SPEC TRANSCRIBED, CONTRACT ABSENT 1
```
  Both USED (partial) cells are §1.4 cells, each with a Claude reviewer; read as "what Flash did", salt-diet is the third line.
  - **USED**: every function the statement contracts is `ensures`-bound INSIDE `verus!` (position, `used-position2.py`), and the subject's
    own last Verus run reads "N verified, 0 errors". **USED (partial)**: k of n contracts bound (`talfs201`, `tasfs301`, 1 of 2 each).
    **USED (unverified)**: bound, never run.
  - **SPEC TRANSCRIBED, CONTRACT ABSENT** (`tasfs101`): all 51 statement spec fns transcribed as `open spec fn` inside `verus!`, the two
    contracted functions outside it with no `ensures`; its LANDING cites "solution.rs::allocate contract" and no such contract exists (the
    tally row says so). It PASSES the suite.
  - **EXEC USE**: the statement's checker clauses transcribed into the solution's executable `check_trace`, by name or clause-labelled
    inline; the task's own deliverable is NOT EXEC USE. **TEST ORACLE**: the statement's spec fns transcribed into the TESTS as an
    oracle. **WEAK TRACE**: a name in a comment, no transcription. **NO TRACE**: none found.
  - **Placements the lead has not ruled one by one** (each the hand's, posted, "your call"): `tavfp201` EXEC USE (partial); `tavfp301`
    TEST ORACLE (partial). The lead's acceptance of the census at bus offset 107,190,349 did not reverse them.
  - **The instrument's limits.** Plain cells were read by the census `stmt-names-in-tests.sh` (names DERIVED from REQUIREMENTS.md; matches
    NAME, `<p>_NAME`, `<p>_STEM`, bare STEM) AND by opening every test file's header and function list. Two rename shapes are NOT
    matched by the census: a reordered name (`spec_leaves_from` for `leaves_from_spec`) and a name with no stem in common; a plain cell's
    TEST ORACLE or WEAK/NO TRACE rests on the hand read for those. Three needle defects were found and corrected during the harvest
    (`taafp101/201/301`, `talfp201`: WEAK/NO TRACE → TEST ORACLE); the tally rows carry each correction.
- **COST, in cell wall (§TA3's unit), SPENT, never a premium:**
```
flash cell wall SPENT 34810.8 s against the registered 41439 s (x0.840) · a LOWER BOUND: 5 truncated cells, 4 with unmetered swarm workers
flash Luby sextet: SPENT 3622.9 s against the registered 4062 s
flash AES sextet: SPENT 3266.0 s against the registered 5034 s
flash Liveness sextet: SPENT 3336.8 s against the registered 4556 s
flash MaxFlow sextet: SPENT 3947.9 s against the registered 5041 s
flash BinomialHeap sextet: SPENT 11685.6 s against the registered 6992 s
flash LinearScan sextet: SPENT 8951.6 s against the registered 15754 s
```
  The total is a LOWER BOUND twice over: five truncated cells stopped turns at the deadline, so their walls are what was spent, not what
  the work needed; and the four §1.4 cells' workers are not in any meter (their tokens are in `workers.txt`). BinomialHeap is the one problem over its price, and all three of its salt-diet cells were truncated. The price was re-cut once
  after the Luby sextet (ADDENDUM 5: AES..LinearScan 34,459 s); the registered line is the one compared here.
- **Prediction (i)** (§TA3, from WA: within a condition, salt-diet's TURNS-CUT incidence is ≥ plain's):
```
flash prediction (i) holds in 6 of 6 problems · truncated cells plain 0, salt-diet 5
```
  It holds in every problem, but it is TESTED (a non-zero side) only in BinomialHeap and LinearScan; elsewhere it holds at 0 ≥ 0. No cell
  tripped a token cap. **Prediction (iii)** (CELL-KILLED binds no cell outside a declared 503 episode): holds; `done_reason` is LANDED in
  all 36, and the one 503 was a discarded attempt (§1.3).

---
# §3 · gemini-4-argon-high — THE RESULT OF RECORD (one client)
```
argon Luby plain: PASS 3 of 3 [12/12 12/12 12/12] · truncated 0 (events 0; print-timeout lines 0) · interface 1bda4459679b1bf1 · clients 62f21027
argon Luby salt-diet: PASS 3 of 3 [12/12 12/12 12/12] · truncated 0 (events 0; print-timeout lines 0) · interface 1bda4459679b1bf1 · clients 62f21027
argon AES plain: PASS 3 of 3 [8/8 8/8 8/8] · truncated 0 (events 0; print-timeout lines 0) · interface dd4b759c2c3a60e7 · clients 62f21027
argon AES salt-diet: PASS 3 of 3 [8/8 8/8 8/8] · truncated 0 (events 0; print-timeout lines 0) · interface dd4b759c2c3a60e7 · clients 62f21027
argon Liveness plain: PASS 3 of 3 [11/11 11/11 11/11] · truncated 0 (events 0; print-timeout lines 0) · interface 87ecc3aa5a6eea59 · clients 62f21027
argon Liveness salt-diet: PASS 3 of 3 [11/11 11/11 11/11] · truncated 0 (events 0; print-timeout lines 0) · interface 87ecc3aa5a6eea59 · clients 62f21027
argon MaxFlow plain: PASS 3 of 3 [8/8 8/8 8/8] · truncated 0 (events 0; print-timeout lines 0) · interface 94fa3a69d109dd9b · clients 62f21027
argon MaxFlow salt-diet: PASS 3 of 3 [8/8 8/8 8/8] · truncated 0 (events 0; print-timeout lines 0) · interface 94fa3a69d109dd9b · clients 62f21027
argon BinomialHeap plain: PASS 3 of 3 [13/13 13/13 13/13] · truncated 0 (events 0; print-timeout lines 0) · interface e440fb9aa198280c · clients 62f21027
argon BinomialHeap salt-diet: PASS 3 of 3 [13/13 13/13 13/13] · truncated 1 (events 1; print-timeout lines 3) · interface e440fb9aa198280c · clients 62f21027
argon LinearScan plain: PASS 3 of 3 [9/9 9/9 9/9] · truncated 0 (events 0; print-timeout lines 0) · interface 6c675da1f3171e38 · clients 62f21027
argon LinearScan salt-diet: PASS 3 of 3 [9/9 9/9 9/9] · truncated 0 (events 0; print-timeout lines 0) · interface 6c675da1f3171e38 · clients 62f21027
```
- **Every argon cell passes the withheld G suite in full.** Every condition is at CEILING. No argon cell used the `swarm` tool:
```
argon salt-diet PASS, swarm cells OUT: 18 of 18
argon comparison n per condition, truncated and swarm cells OUT: Luby plain 3 · Luby salt-diet 3 · AES plain 3 · AES salt-diet 3 · Liveness plain 3 · Liveness salt-diet 3 · MaxFlow plain 3 · MaxFlow salt-diet 3 · BinomialHeap plain 3 · BinomialHeap salt-diet 2 · LinearScan plain 3 · LinearScan salt-diet 3
argon salt-diet categories, swarm cells OUT: USED 18
```
- **TRUNCATION**, one cell, as ADDENDUM 8 declared the risk before AES:
```
argon truncated 1 cells, 1 events, 3 print-timeout lines (scorer figure 3): tabas101=1/3
```
- **THE STATEMENT LINE:**
```
argon plain categories: USED (unverified) 1 · EXEC USE 3 · TEST ORACLE 9 · TEST ORACLE (partial) 4 · WEAK TRACE 1
argon salt-diet categories: USED 18
```
  Every argon salt-diet cell is USED: all contracts bound inside `verus!` and the subject's own last run "N verified, 0 errors". The one
  USED (unverified) is plain `talap201` (the statement whole inside `verus!`, never run, no false claim). The THE LINE sweep moved
  `talap101`, `talap301` and `tasap301` to EXEC USE (`ct-sweep-2026-11-20.txt`, the lead's acceptance at bus offset 107,190,349).
  Placements the lead accepted by name: `tabap101`, `tabap301` TEST ORACLE (partial). Not ruled one by one: `taaap301`, `tavap201` TEST
  ORACLE (partial).
- **COST, SPENT:**
```
argon cell wall SPENT 37943.2 s against the registered 56276 s (x0.674) · a LOWER BOUND: 1 truncated cells, 0 with unmetered swarm workers
argon Luby sextet: SPENT 5636.6 s against the registered 5492 s
argon AES sextet: SPENT 5700.8 s against the registered 6815 s
argon Liveness sextet: SPENT 6160.0 s against the registered 6169 s
argon MaxFlow sextet: SPENT 6446.7 s against the registered 6811 s
argon BinomialHeap sextet: SPENT 6965.6 s against the registered 9521 s
argon LinearScan sextet: SPENT 7033.5 s against the registered 21468 s
argon AES..LinearScan SPENT 32306.6 s against ADDENDUM 8 re-cut 51512 s (x0.627; registered 50784 s)
```
  A LOWER BOUND (`tabas101`). ADDENDUM 8 re-cut AES..LinearScan from argon's Luby sextet (plain ×1.781, salt-diet ×0.832); the line against
  that re-cut is printed beside the registered one. LinearScan spent a third of its price: the registered line carried NA's LinearScan
  salt-diet median, 4,354.8 s per cell (`ta_price.out`).
- **Predictions:**
```
argon prediction (i) holds in 6 of 6 problems · truncated cells plain 0, salt-diet 1
```
  TESTED only in BinomialHeap. (iii) holds: LANDED in all 36, no 503.

---
# §4 · THE SEAMS AND WHAT THE TABLE DOES NOT CARRY
- **MODEL SEAM (§TA4 item 3):** §2 and §3 are two results; nothing here is Flash-versus-argon as models, and no argon cell is tabled beside
  a gemini-3.1-pro-high result.
- **CLIENT SEAM (ADDENDA 6–7):** Flash, three clients (§1.2). The updates came from the wave's own unfenced host calls, never from a cell;
  the next agy export moves them (ADDENDUM 4 item 4, ADDENDUM 7 item 4).
- **WORKER SEAM (§1.4):** four Flash cells, ruled. The next agy export denies the `swarm` tool (the lead's queue, bench row 10).
- **MODE:** every TA cell ran in Default mode (`agentMode ""`, §TA0 row 5); WA Flash's Auto mode is in §TA3's price ratio, not in a cell.
- **NOT IN THIS TABLE:** tokens beyond `T` (the meter's total) and any agy pool points per cell (UNMEASURED, §TA3); the `/usage` reads
  at fire and bank are on the bus, not here.

# §5 · WHAT THIS RESULT DOES NOT ESTABLISH
§TA5, carried: every premium is UNRESOLVED-UNDERPOWERED; no magnitude or effect size; nothing Claude-versus-agy, so nothing block T versus
TA; nothing Flash-versus-argon as models; nothing about the statement arm versus `extras = none` across blocks. With every condition at
ceiling in both models, nothing here says whether the salt method helps or hurts on these problems. The statement categories describe
what the subjects did with the statement; they are not a score. Any public sentence, and any claim about the method, is the Captain's.
