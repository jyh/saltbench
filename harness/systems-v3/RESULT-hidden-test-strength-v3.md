# The hidden-test strength table — row 2's deliverable, over the five cards

Owner: bench. Date: **2026-09-04**. Box: **yukon**. 💵 **Zero model tokens — no model of any kind was
called.** No cell was run: this is the referee measuring **withheld tests against withheld mutants**,
squarely inside the gate's *build and receipt only*.

**Every number below names the file it came from:**
`results/hidden-test-strength-2026-09-04.json` (the raw readings) and
`results/hidden-test-strength-2026-09-04.txt` (the run's own output), produced by
`hidden_test_strength_table_v3.py` over `tasks/systems-v3/` at systems' Day-1 packet `1d77e6d`.

⛔ **It drives `run_tests.sh`, the runner the referee uses**, and not a cargo line of its own: a table
about the hidden tests must describe them as the referee runs them, and a second invocation is a
second instrument. ⇒ **MEASURE THE PROGRAM THE RUN WILL EXECUTE.**

---

## 1. The table

```
cell         reading   score   KILLED  SURVIVED  NOT MEASURED   reference
Crc32/G      measured  1.000     5        0          0          TESTS 6/6
Crc32/B      measured  1.000     2        0          0          TESTS 10/10  REGRESSIONS 0/6   CLAUSE_TESTS 0/4
LRU/G        measured  1.000     4        0          0          TESTS 16/16
LRU/B        measured  1.000     2        0          0          TESTS 23/23  REGRESSIONS 0/16  CLAUSE_TESTS 0/7
LZW/G        measured  1.000     4        0          0          TESTS 8/8
LZW/B        measured  1.000     5        0          0          TESTS 15/15  REGRESSIONS 0/8   CLAUSE_TESTS 0/7
FreeList/G   measured  1.000     5        0          0          TESTS 7/7
FreeList/B   measured  1.000     7        0          0          TESTS 9/9    REGRESSIONS 0/7   CLAUSE_TESTS 0/2
Paxos/G      measured  1.000     4        0          0          TESTS 17/17
Paxos/B      measured  1.000     6        0          0          TESTS 24/24  REGRESSIONS 0/16  CLAUSE_TESTS 0/8
                                ──       ──         ──
             10 cells            44        0          0          score 1.000 over the measured
```

**Every reference passes its own suite cleanly, no cell is ABSENT, VACUOUS, INVALID or NOT MEASURED,
and every one of the 44 withheld mutants was measured.** By §4.3 item 5 that is the bar: **no card is
disqualified before the run**, and a per-card difference in the pilot cannot be blamed on a dead
suite. `CLAUSE_TESTS 0/N` on every B reference is **expected** — the clause is the change request's
and the base does not implement it.

## 2. ⛔ AND A UNIFORM 1.000 IS THE LEAST INFORMATIVE THING THE INSTRUMENT CAN PRINT

A suite that kills every mutant it is handed tells you **the mutants are killable**, not that the
suite is strong — and the mutant set was authored alongside the tests, so this measures **internal
consistency**, not power against an implementation nobody has seen. ⇒ **AN ARM AT CEILING LEAVES NO
ROOM TO DISCRIMINATE**, and here the arm at ceiling is the *mutant set*.

**The signal is in the MARGIN, which the rate discards.** The margin is the number of hidden tests
that actually failed on the mutant — the evidence the kill rested on:

```
cell         score   min margin   the mutants at that margin
Crc32/G      1.000       5        all five (5 of 6 tests fail)
LRU/G        1.000       5        put_duplicates
LRU/B        1.000       5        peek_moves, peek_returns_none
LZW/G        1.000       5        dict_seeded_255
Crc32/B      1.000       3        StreamRestart
FreeList/B   1.000       2        free_leaks, free_stops_merging, merge_below_only
FreeList/G   1.000       1        free_leaks
LZW/B        1.000       1        clears_too_early, decoder_ignores_clear
Paxos/G      1.000       1        own_value
Paxos/B      1.000       1        own_value, reply_from_memory, restart_keeps_memory
```

⇒ 🔑 **A KILL RATE OF 1.000 SAYS THE SUITE CAN TELL; THE PARTIAL COUNT SAYS BY HOW MUCH, AND THE
MARGIN IS WHERE THE FRAGILITY IS.** This seat's row-DT law — *a partial count measures distance, a
zero measures nothing* — read forwards for once, before the run rather than after it.

⛔ **SEVEN MUTANTS ACROSS FOUR CELLS ARE KILLED BY A SINGLE TEST.** Three of them are Paxos/B, where
**one test out of twenty-four** is the entire difference between KILLED and SURVIVED — on the set's
hardest task. A seat whose implementation differs in a way that one test does not probe is reported
PASS. The same holds for `Paxos/G own_value`, `FreeList/G free_leaks` and two LZW/B mutants.

📌 The converse is equally worth reading: mutants failing **every** test (`FreeList header_past_end`
and `split_off_by_one`, `LZW/G encoder_extends_before_emitting`) are killed at maximum margin and
therefore say the **least** about suite strength — they are loud, not discriminating.

## 3. What this does and does not license

- **Does:** admit all five cards. Nothing is VACUOUS or INVALID; the instrument reads `measured` on
  10 of 10 with zero NOT MEASURED, so §4.3 item 5's gate is satisfied for the whole set.
- **Does not:** license reading 1.000 as "the hidden tests are strong". It is a ceiling on this
  mutant set, and the margins say the evidence is thin in four cells.
- **Recommendation (bench's, for the Q2/Q3 sitting; not bench's to rule):** print the **min margin
  beside the strength** in the result renderer, so no reader takes 1.000 for robustness; and consider
  whether Paxos's one-test margins want a mutant or two more before the pricing pair — an addition to
  the withheld set is systems', and it changes no card the seats see.

## 4. One defect of my own, caught before it reached the table

My first parser matched `TESTS\s+(\d+)/(\d+)` **anywhere** and took the last hit — so on the B rung,
which prints `TESTS` then `REGRESSIONS` then `CLAUSE_TESTS`, it matched the substring inside
`CLAUSE_TESTS` and reported the Crc32/B reference as **`0/4`** when its real reading is **`TESTS
10/10`**. The verdict was right (it comes from the exit code) and the number beside it was wrong.
⇒ 🔑 **A WRONG NUMBER UNDER A RIGHT VERDICT READS AS CORROBORATION**, and ⇒ **A LABEL THAT IS A SUFFIX
OF ANOTHER LABEL MUST BE MATCHED ANCHORED, NEVER BY SUBSTRING.** All three counters are now parsed by
their own anchored labels and all three are printed.
