# RESULT — ARM-LEVEL COVERAGE OF THE WITHHELD SUITES, FIVE PRICING TASKS (2026-09-10)
**The test × mutant matrix systems offered twice and nobody took.** Built by
`harness/systems-v3/arm_coverage.py`; every figure below is rendered from its `--json` output by
`harness/systems-v3/arm_coverage_report.py`, so **no number in this file is typed.** Zero model tokens.

## §0 · THE QUESTION, AND WHY NO EXISTING RECEIPT ANSWERS IT
`test_strength.py` points the withheld mutants at the **seat's** suite. Nothing pointed them at the
**referee's own** withheld suite. And `EXECUTOR-BRIEF-v3.md` §3 requires each mutant be rejected with
the *"first failing line quoted"* — **whichever arm happened to fail first, which reads like attribution
and is not.** So no receipt in this campaign has ever shown that a given arm tests the thing it was
built for. On the one task where anyone looked (the Liveness port), an arm fired against **zero**
mutants while every protocol receipt read green.

## §1 · THE MATRIX — every withheld arm × every withheld mutant, on the five pricing tasks
```
  task       arms  mutants  dead arms  margin-1  survivors
  Crc32         6        5          1         0          0
  LRU          16        4          4         0          0
  LZW           8        4          0         0          0
  FreeList      7        5          0         1          0
  Paxos        17        4          8         1          0
  TOTAL        54       22         13         2          0
```

## §2 · DEAD ARMS — an arm that fails on NO mutant
* **Crc32** — 1 dead: `repeatable_and_stateless`
* **LRU** — 4 dead: `capacity_and_empty_start`, `keeps_everything_below_capacity`, `miss_returns_none`, `observers_do_not_disturb`
* **Paxos** — 8 dead: `duplicate_accept_after_choice`, `init_nothing_chosen`, `neg_accept_from_initial`, `neg_promise_without_prepare`, `neg_propose_empty_quorum`, `own_value_proposal_is_proposed`, `plain_run_chooses_0`, `plain_run_chooses_1`

## §3 · MARGIN — how many arms each mutant's death rests on
A mutant killed by exactly ONE arm is one deletion away from surviving. The kill RATE cannot
see this: it counts mutants, and a margin-1 mutant is a full point in the numerator.
* **FreeList / `free_leaks`** — killed only by `exhaust_and_recover`
* **Paxos / `own_value`** — killed only by `exploration_agreement_and_validity`

## §4 · SURVIVORS — a mutant no arm kills
**NONE.** Every measured mutant is killed by at least one arm in its suite.

## §5 · WHAT THIS DOES AND DOES NOT ESTABLISH
✅ It replaces the protocol's *first failing line* — which reads like attribution and is not —
with the full set of arms that fail on each mutant. **Attribution is now measured.**
⛔ It does NOT show any suite is strong. Every arm here is scored against a mutant set the
same author wrote; a mutant set and a suite that share an author share their blind spots.
⛔ And a task's `TESTS p/t` denominator is unchanged by any of this: a dead arm would still
count toward `p` and toward `t` on every submission, in every receipt.

## §6 · ⛔ WHAT A DEAD ARM IS A STATEMENT ABOUT, AND IT IS NOT THE ARM
**A dead arm is a claim about the MUTANT SET first.** `repeatable_and_stateless` (Crc32) and
`miss_returns_none` (LRU) are not weak arms; they check properties **no mutant in their set attacks.**
⇒ **The reading is not "13 arms are useless." It is "13 arms are UNEXERCISED, and until a mutant
attacks each one, no receipt in this campaign distinguishes a live arm from a dead one."**
⭐ **The Liveness precedent is exactly this shape and it resolved the other way:** there, the arm was
dead because a *saturation* effect made the mutant behave like a pure function by the time the arm ran.
**Same reading, opposite cause** — which is why the matrix reports and does not rule.

⚠️ **ONE OBSERVATION, AT n = 5, ON ONE TASK, STATED WITH ITS DENOMINATOR BECAUSE IT WILL BE MISREAD.**
Paxos is the only task whose arms carry a `neg_` prefix (a refusal check: an illegal step must be
REFUSED). **3 of its 5 refusal arms are dead, against 5 of its 12 others.** ⛔ **This is one task and
five arms.** The prefix does not exist on the other four tasks, so there is **no campaign-wide split to
compute** and none is reported here. It is a hypothesis for whoever writes the next mutant set — that
mutant sets attack the accepting path and under-attack the refusing one — **and it is not evidence.**

## §7 · ⛔⛔ THE INSTRUMENT'S OWN FIRST READING WAS WRONG, AND IT WAS WRONG IN THE FLATTERING DIRECTION
The first sweep reported **27 dead arms and 9 survivors**, including Crc32 and Paxos at 100 % dead.
**None of it was real.** A `FAIL` line carries trailing detail a `PASS` line does not, the name regex
captured to end-of-line, and every kill looked up as `None` rather than `False`.
⇒ 🔑 ***AN INSTRUMENT THAT REPORTS ABSENCE FAILS TOWARD ABSENCE:*** a name that fails to match reads as
*"this arm killed nothing"*, which is **byte-identical to the finding the tool exists to produce.**
✅ **Only the positive control separated them** — a deliberately wrecked reference must FAIL, and on
Paxos it gave `TESTS 3/17` while all four of its mutants read as surviving. A suite that discriminates
and kills nothing is a contradiction, and that contradiction is the whole of the catch.
⛔ **The root is that the five withheld drivers do not share a FAIL contract.** `println!("PASS {}")` is
uniform in 5 of 5; the FAIL form is bare in three tasks, `"FAIL {}{}"` in Crc32, and **seven distinct
`"FAIL {} — …"` shapes in Paxos.** ⇒ ***THE REFERENCE RUN — THE VALIDITY CHECK EVERY TASK PASSES —
EXERCISES ONLY THE `PASS` PATH, WHICH IS THE ONE SHAPE THAT IS UNIFORM.*** A parser sanity-checked
against the reference is checked against the half that could not have told it anything.

## §8 · PROVENANCE
```
  tool        harness/systems-v3/arm_coverage.py        --selftest: 8 arms, 0 failed
              two of those arms fire RED on the pre-fix regex, verified by planting it back
  renderer    harness/systems-v3/arm_coverage_report.py  (this file's numbers come from the JSON)
  raw matrix  arm-coverage-2026-09-09.json  (kept on the run box beside the referee tree)
  suites      the withheld drivers and mutants of the posthoc referee tree, backup/systems-v3 ebe686c
  reference   every task's withheld reference passes its own suite (validity), 5 of 5
  control     a wrecked reference must FAIL -- driven on Paxos, TESTS 3/17, rc 1
```
