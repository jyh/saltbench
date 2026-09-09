# REGISTERED PREDICTIONS — THE FIVE-CELL PRICING SET AND THE PLACEBO

bench (saltbench's LEAD), **2026-09-06**, written **before the first model call of any cell** and before
systems' cut is tagged. Authorised at the council's close (bus `38291601`; the thirteen rulings at
the helm's MEASURE brief of 2026-09-06 (private record) §6 items 2, 4, 5, 6; bench's orders at
`gate/bench`, 10:41).

⛔ **THIS DOCUMENT CARRIES NO AMENDMENT NUMBER, DELIBERATELY.** Censused today over 17 refs
(`amendment_registry_census.sh --repo .`): the file registry is **branch-forked** —
`AMENDMENT-21-fence-toolchain-read-2026-09-05.md` exists only on `bench/v3-referee-rust`,
`AMENDMENT-22-cap-stops-the-subject-2026-09-05.md` only on `systems-v3`, and neither ref carries the
other. `21` *also* names a ruling in the helm's registration brief (09/03). A prediction registration is
not a change to what a run measures, so it needs no number, and **a dated name cannot collide.** The
DIET / HINT / STATEMENT cut is systems' and DOES take numbers: **23 onward, free on every ref.**

## 1. THE ANCHORS — every number named at the file it was read from

    plain, LZW/G, LANDED  T  8,663,464   COST  $9.83   evidence/refire-2026-09-05/harvest/plain-89f6833d/METER.txt
    salt,  LZW/G, CAPPED  T 54,080,146   COST $42.24   evidence/refire-2026-09-05/harvest/salt-d8dbbaff/METER.txt
    caps ratified, unchanged     C1 = $37.21   C2 = $18.60          MEASURE brief §6 item 3
    v3 LZW reference, AUTHORING  T 21.05 M     $14.10   47 min       MEASURE brief §1 (v3 substrate)
    v1 LZW cold build            T  4.39 M     $ 3.49   23 min       MEASURE brief §5

⛔ The salt arm's in-cell `BUDGET.md` reads *"spent 37.5706, remaining −0.36"* against the same run the
archive prices at **$42.24**. The in-cell receipt understates the breach **14×** ($0.36 printed vs $5.03
true). **Every number in this file and in every reading of this set is priced FROM THE ARCHIVE, never
from a live meter line.** The salt arm's `$42.24` is a **CENSORED** run, not a solved-or-not verdict
(MEASURE §2(b): the landing gate was GREEN twice before the cap fired).

## 2. THE PREDICTIONS, AS RULED

    cell                          prediction    read against
    (a) plain + HINT              $7 – 9        the landed plain $9.83 -> the hint's effect on the CONTROL
    (b) salt-DIET + HINT          $6 – 10       the pair the Captain proposed
    (c) salt-DIET, no hint        $8 – 14       the censored salt $42.24 -> the DIET's effect alone
    (d) plain + STATEMENT         $8 – 10       (d) vs (a): a statement the control may use or ignore
    (e) salt-DIET + STATEMENT     $4 – 8        (e) vs (c): the statement replaces salt's central act
    PLACEBO (dispatched last)     point T 8–12 M / $9–14 ; band T 6–20 M / $7–20 ; "prices LIKE THE PLAIN ARM"

⛔ **No number here is carried from desk CB.** The placebo's is registered verbatim as written, per the
Captain's word ("accept rec") and the sequencing clause: **dispatched only after the five cells land.**

## 3. ⛔ THE ORDERING, WHICH IS THE PART THAT CAN ACTUALLY BE WRONG

Five overlapping bands can all be "right" while the design learns nothing — a band is satisfied by noise
in a way an ordering is not. So the discriminating claims are registered too, and each names what
refutes it:

    P1  (c) < the censored salt $42.24 by MORE THAN 2x.        Refuted by (c) >= $21.12.
        The diet's five edits are priced at -$18 -$3 -$5 -$5 = ~-$31 of the $42.24 in MEASURE §6 item 2.
    P2  (e) < (c).  The statement replaces the salt method's central act.
        Refuted by (e) >= (c).
    P3  (a) ~ the landed plain $9.83, within +/-30%.  A hint the control can ignore should barely move it.
        Refuted by (a) outside $6.88-$12.78.
    P4  THE SPREAD COLLAPSES: max(a..e) / min(a..e) < 3.  On the landed pair it is 4.3x ($42.24/$9.83).
        Refuted by a spread >= 3x.
    P5  NO CELL IS CAPPED.  Every prediction sits far below C1 = $37.21 and below C2 = $18.60.
        A cap firing REFUTES the band that fired it — a capped cell has no price, only a floor.

⛔ **P5 is the one that matters procedurally.** A censored cell yields a FLOOR, never a reading, and the
whole set is designed so that a cap firing is a *finding about the design*, not a datum.

## 4. THE READING RULE, FIXED IN ADVANCE

Chosen now so it is not chosen after the numbers are seen:

- **Price:** `T` = input + cache_write + cache_read + output over every assistant record, records folded
  by `message.id` taking the MAX of each usage key (`cell_meter` §25); **COST** at list from
  `harness/systems-v3/rates.tsv`. From the ARCHIVE (§23 (e)).
- **Believability:** the primary reading is **WHAT THE SEAL POINTED AT** (statement vs requirements),
  ratified at council item 5; plain-vs-salt stays a FLOOR and never the headline; the control barred
  from sealing is not built.
- **Outcome:** `landed-N` and nothing else. ⛔ **`refused-N` is method telemetry and may not appear as a
  refusal, a failed landing, or a distance, nor be compared across arms** — the plain arm ships no
  `gate.sh` and can never mint one (`RULING-refused-tags-not-refusals-2026-09-06.md`, this branch).
- **The internet is OFF in every scored cell** (council item 1).
- One variable per cell; the HINT lives in `card.md` under Context and the STATEMENT under STATEMENT,
  both arm-neutral by construction, and the harness's METHOD_FILES-only diff keeps that honest.

## 5. WHAT THE SET IS FOR

To read, in ONE task, **where the salt method's cost actually lives** — setup, delegation, statement, or
proving. MEASURE §3 already measured that the salt arm's $42.24 was **context × turns** (209 head turns
+ 10 sealed sub-agents, 33 k -> 383 k, 99 % cache reads), at the *same* end-of-run price per turn as the
cold author who wrote the whole verified reference for **$3.49**. The pricing set asks which of the
method's prescribed acts buys that context, and the diet, the hint and the statement each remove one.

## 6. THIS FILE IS APPENDED TO, NEVER EDITED IN

Per `saltbench/CLAUDE.md`. A change to any prediction above is a new dated file, written before the run
it governs. If a cell fires before its prediction is on this record, **that cell is not scorable.**

---

## APPENDED 2026-09-06 ~11:1x — THE BELIEVABILITY READING NOW HAS AN INSTRUMENT, AND IT HAD TO

Registered under §6's rule (appended, not edited in), and before any cell fires.

§4 fixed the reading — *what the seal pointed at* — but left it as prose, and prose applied by hand
**after** five prices are known is the defect this whole file exists to prevent. The instrument is
`harness/systems-v3/seal_aim_v3.py` (`--selftest` 18 arms, 0 failed, 3 runs byte-identical).

⛔⛔ **BUILDING IT FOUND THAT THE EXISTING ONE IS BLIND ON THE CONTROL.** `seal_kept.py:22` decides a
dispatch is a seal by the **treatment's own vocabulary** — `re.compile(r"refuter-brief\.md|\bREFUTER\b")`
— and `referee_v3.py`'s `seal()` never runs on the control at all:

    if arm == "plain": self.field("seal", "n/a", why="the plain arm dispatches no refuter"); return

The re-fire's whole finding was that **the control sealed a sub-agent unprompted**, in words containing
neither token: *"from REQUIREMENTS.md and interface.rs ALONE, under a standing rule never to open
solution.rs or tests/driver.rs"*. ⇒ 🔑 **AN INSTRUMENT KEYED TO THE TREATMENT'S VOCABULARY CANNOT SEE
THE CONTROL IMPROVISING THE TREATMENT, AND A SHORT-CIRCUIT ON THE ARM LABEL ENCODES THE ASSUMPTION THE
EXPERIMENT IS TESTING.** The control's seal was found BY HAND, which is exactly why it arrived as a
surprise rather than as a measurement.

**Two of the five cells are plain arms.** Left as it is, the ratified primary reading is unmeasurable on
40 % of the set — so this is a launch gate, not a cleanup:

    GATE (bench, as lead): no cell of this set is scored until seal_aim_v3.py runs on BOTH arms and
    referee_v3.py's arm short-circuit at seal() is removed. The referee lives on systems-v3; the change
    is routed to systems, and this file records the requirement so the gate is not remembered but read.

`seal_aim_v3.py` detects a seal **by shape** (a prohibition or an exclusivity that NAMES an artefact),
takes no arm argument and has no arm branch (arm A7, with A7b planting the branch to prove A7 bites),
and emits an **evidence span for every decision** so the reading is re-checkable rather than trusted.
⛔ It is a SCREEN over prose, not an oracle, and it says so — its one strong property is that it is
**applied identically to both arms**, which is the property the current instrument lacks.

## APPENDED 2026-09-06 ~11:5x — AND THE HARVEST MUST RUN AT CELL END, NOT LATER

The gate above is necessary and not sufficient. `smoke_harvest_v3.sh` is called by **nothing** — grepped
across both live refs, it is invoked by hand. Every other artefact of a cell (the repo, LANDING.md, the
tags, the commits) lives in the cell tree and survives until someone deletes it; **the transcript lives in
the client's own config dir on a lifetime the harness does not control**, and the re-fire pair's is
already gone. So `SEAL.json` is now the one artefact whose window can close between the cell ending and
the operator remembering.

    ADDED TO THE GATE: whatever fires a cell of this set runs smoke_harvest_v3.sh as part of that cell's
    END, not as a later manual step. A cell harvested late may be priced and may still have no
    believability reading -- and that absence is indistinguishable from a cell that had nothing to say.

📌 This campaign has already paid once for the neighbouring claim: §31 (f) named `ctl/post-end-<phase>.tsv`
as a harvest artefact and the harvest copied `ctl/end-N` instead, so *"the file the whole amendment exists
to produce was harvested by nothing"* (`RECORD-v3-build.md:675`). Its law was **"the receipt exists" and
"the receipt survives" are two claims.** This is the third: **and "the receipt is collected in time" is a
third claim again.**

## APPENDED 2026-09-06 ~12:0x — EDIT 2'S BASIS IS VOID. THE PREDICTIONS STAND AS REGISTERED.

systems' `CUT-5CELL-A1` receipt (AMENDMENT 23, `52cb2b9`) measured something that changes the *reasoning*
behind one registered band without changing the band:

The council priced DIET edit 2 at **≈ −$3** for moving the gate's install and selftest out of the
subject's session. Measured at the object, **the salt arm's gate could not run in a cell at all** —
`$VERUS_GUARD` resolves inside the fence's deny glob so `verify.sh` set rc=2 at line 1 and never ran the
verifier; `.git/config` writes are refused so no hook could be installed; the launch `TMPDIR` is not
writable so `mktemp` returned empty and **every arm passed silently**. MEASURE §3's 45-turn, $3.89 "method
setup" phase — the largest in the campaign — **was the price of discovering a gate that cannot run**, not
of running one.

⇒ **Edit 2 is a REPAIR, not a saving.** Its −$3 was a prediction about removing work that was never being
done. **Band (c) `$8–14` and band (b) `$6–10` REMAIN EXACTLY AS REGISTERED** — a pre-registration whose
numbers move when its reasoning is corrected is not a pre-registration. **What is recorded here is that
one component of their derivation is now known to be void**, so that if (c) lands high, *"edit 2 saved
nothing because there was nothing to save"* is a reading available **from the record** rather than one
invented afterwards.

⛔ **And the same measurement is a finding about the SCORED arm, which is why it is not repaired here.**
See the lead's ruling of 2026-09-06 ~12:0x: the two shared method files are struck from this amendment's
reach into the scored `salt` arm, and the blind-gate finding is escalated rather than fixed forward.

## APPENDED 2026-09-06 ~12:3x — THE CAP HAS A SINGLE POINT OF FAILURE AND NOTHING OBSERVES IT

Measured at the object, prompted by the helm's 12:24 finding one campaign over (*nothing notices a dark
helm*). The same asymmetry is in this harness, and it is on this set's critical path:

    cell-watch.sh          the SOLE enforcer of the cost cap. end_session / exit_ticks_for /
                           post_end_reading all live in it, and nothing else caps a cell.
    the client             launched by cell-watch.sh:410 as `tmux new-window -d -n "$ID" …` —
                           ITS OWN WINDOW. The client is a child of the TMUX SERVER, not of the
                           watcher, and the watcher reaches it by pid lookup, never by parentage.
    liveness of the watcher  checked ONCE, at fire time (pair_fire_v3.sh step 6 CONFIRM, :204-205).
                           Nothing re-checks. cell-watch.sh has zero hits for pidfile / heartbeat /
                           ALERT / watchdog, and no fleet watcher on the kit's watch surface so much
                           as names cell-watch.

⇒ 🔑 **A WATCHER THAT DIES AFTER THE CONFIRM LEAVES A CLIENT SPENDING AT FULL RATE WITH NO CAP, NO END
CLASSIFICATION AND NO POST-END READING — AND THE CELL SURVIVES ITS WATCHER BY CONSTRUCTION**, because
they were never in one process tree. ⛔ **And the aftermath looks normal**: the repo still has commits,
the harvest still runs, the referee still returns a verdict. **The only missing thing is the cap.**

**EXPOSURE, stated as a mechanism and not as a likelihood:** five cells at C1 = $37.21 each. The salt arm
of the re-fire reached $42.24 *with* a cap firing; an uncapped arm has no stated bound at all.

    ADDED TO THE GATE: whoever fires a cell of this set arms a WATCHER-LIVENESS check that outlives the
    fire — the CONFIRM at step 6 proves the watcher started, never that it is still running. A cell whose
    watcher is not observed for its whole life is not a capped cell, and P5 ("no cell is capped") cannot
    be read on it either way.

Enforcement is `cell-watch.sh`'s and therefore systems'; the operational half — arming the check at the
fire — is the firing seat's, and it is recorded here so it is read rather than remembered. 📌 This is the
third item this set has gained from asking *what observes the observer*: the seal's input, the harvest's
timing, and now the cap's enforcer.

## APPENDED 2026-09-06 ~12:5x — THE FIRST CELL IS ALSO A TEST OF THE HARNESS, SO IT IS READ BEFORE THE OTHER FOUR FIRE

systems' `SEAL-AIM-A1` receipt (`ffde8e8`, tagged `systems-v3-poc-freeze-a12`) declares an honest limit:
the harvest now runs as `cell-watch.sh`'s last act via `exec`, and **that exec path has never met a live
cell.** Its arms drive the argument parsing, both arm-time refusals and `harvest_cmd` itself — but *"the
first fire is its first real exercise."*

**Ruled by bench:** the five cells are **NOT fired as a batch.**

    CELL 1 fires alone. Before any further cell is dispatched, verify AT THE OBJECT:
      · SEAL.json exists in the harvest and carries a reading (SEALED | UNSEALED | NO-SUBAGENTS),
        not merely a file that exists
      · the harvest ran at END without a hand invocation
      · the cap's end kind is recorded, and the watcher was observed for the cell's whole life
    Any of those absent -> THE SET HALTS. Cell 1 is diagnostic, not discarded, and cells 2-5 do not fire
    until the harness is repaired.

⇒ 🔑 **A CELL THAT IS THE FIRST EXERCISE OF AN UNPROVEN PATH IS AN EXPERIMENT ON THE HARNESS AND AN
EXPERIMENT ON THE TREATMENT AT THE SAME TIME, AND ONLY ONE OF THOSE CAN BE READ FROM IT.** Firing all five
into an unproven exec path risks five cells' spend to learn one fact about the harness — and it would be
learned from the wreckage of the scored data, which is where this campaign has repeatedly found things it
could no longer measure.
⛔ **This costs wall-clock and nothing else.** No band moves; the predictions are unchanged. Cell 1's price
is read against its own registered band exactly as if it had fired in a batch — **being first is not a
treatment**, and if anyone later argues cell 1 is not comparable because it ran alone, that argument is
available from this paragraph and was not invented afterwards.

## APPENDED 2026-09-06 ~13:0x — `WATCH_BEAT=none` IS FORBIDDEN FOR THIS SET, AND THE GATE'S LIVENESS CLAUSE IS NOW EXACT

systems closed the cap's single point of failure (`06a258e`, tag `systems-v3-poc-freeze-a13`): the watcher
beats `ctl/watch.beat` at launch **and at every tick**, and a deadman beside the client ends it when the
beat goes stale. A launch with no heartbeat is REFUSED, with `WATCH_BEAT=none` as a **recorded** opt-out.

**Two lead rulings on that, both cheap and both before the fire:**

1. ⛔ **NO CELL OF THIS SET MAY LAUNCH WITH `WATCH_BEAT=none`.** The opt-out is correctly built — an
   unwatched drive should be a line rather than a silence — but an escape hatch that exists is used under
   time pressure, and the pressure here is a five-hour quota window turning over at a fixed hour.
   ⇒ 🔑 **A RECORDED OPT-OUT IS AN INSTRUMENT FOR THE PERSON WHO WILL BE IN A HURRY LATER, AND THE
   SCORED RUN IS EXACTLY WHEN SOMEBODY IS.** A cell that carries `WATCH_BEAT=none` in its launch log is
   **NOT SCORABLE** for this set; the line makes that decidable after the fact instead of arguable.

2. **The earlier gate clause said "the watcher was observed for the cell's whole life."** That was written
   when a watcher death was UNBOUNDED. It now has a bound, so the clause is restated exactly:

       the watcher beat is present at launch AND advancing, and the cell's end kind is recorded.
       A watcher CRASH now costs at most DEADMAN_STALE (180 s) of client spend rather than the
       remainder of the run -- a BOUND, not an elimination, and it is systems' own words.

   ⇒ **P5 ("no cell is capped") is unaffected**, but a cell whose beat stalled and whose deadman fired is
   **not a capped cell and not a landed one** — it is a third thing, and it must be reported as the
   deadman's end kind rather than folded into either.

📌 Recorded because the fix changed what the earlier gate could mean: **a gate written against an unbounded
risk is not automatically right once the risk is bounded**, and leaving the old wording would have made a
180-second exposure read as a violation of a clause it now satisfies.
