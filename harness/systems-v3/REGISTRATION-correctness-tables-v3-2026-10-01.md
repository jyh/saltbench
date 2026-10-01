# REGISTRATION: FOUR CORRECTNESS TABLES OVER THE COMPLETE PILOT MATRIX (arXiv v3), DECLARED POST HOC
## bench (SaltBench lead), 2026-10-01, written before any pass count is computed. Council 2026-10-01, item 1, the Captain's words on v3:
## *"Yes, it looks good. But I don't see why we don't check correctness, even post-hoc is fine."* and *"yes (a)"* (the reading folds into
## v3 before submission; submission stays his). P1–P4 mirror `REGISTRATION-descriptive-tables-v2-2026-09-27.md`'s T1–T4.

⛔ **THIS READING IS POST HOC, AND IT IS DECLARED AS SUCH.** Every one of the 181 DONE conditions has a result of record, and every one of
those results already prints its cells' suite verdicts. The lead has read many of them. What is fixed here, before the instrument runs, is
the METHOD: what counts as a pass in each task form, how a halt is read, how a condition's cell is summarised, and how the signs are formed.
⛔ **IT IS DESCRIPTIVE.** No test, no p-value, no verdict on the arms. The registered tests remain §4's.

## §P1 · THE POPULATION
The descriptive tables' §D1, unchanged: `CENSUS-full-matrix-2026-09-14.md` at its current head, **DONE 181 · INEXPR 16 · DECLARED 3 = 200**,
each condition's cells being the cells its result of record names (pooled cells where the record pools them). No cell is added, dropped,
re-fired or re-scored for this reading.

## §P2 · THE CELL VERDICT: THE ONE THE RESULT OF RECORD PRINTS
- **Source.** The suite verdict the condition's result of record prints for the cell, AS AMENDED by any dated addendum to that same file.
  The withheld suite is the grader. A cell's own landing claim is never read as a pass (a self-graded landing is an upper bound, this
  repository's CLAUDE.md).
- **What PASS means, per task form, each as the condition's own freeze registered it:**
  ```
    greenfield (bare · statement)   the withheld G/ suite FULL PASS (every test passes)
    brownfield (bare · statement)   the brownfield suite FULL PASS on the end state
    spec-change                     the phase-2 B/ suite FULL PASS: every test passes, REGRESSIONS 0, CLAUSE_TESTS 0
  ```
  For salt-diet cells that the freeze also gates on a TARGET or axiom check, the pass is the SUITE's. The proof's verdict is printed beside it
  in the result file and never folded into it: the matrix's pass must mean the same thing in both arms.
- **Four classes, and only four:**
  ```
    PASS        the definition above
    FAIL        the suite ran on the cell's end state and did not pass (a failing test, a BUILD-FAIL the runner names as a build failure)
    CENSORED    the cell HALTED at a registered budget (CAP-COST, CAP-TOKENS, CAP-WALL, a turn or wall DEADLINE, MEM-CAP) and its end state did
                not pass. ⛔ A HALT IS NEVER A FAILURE (his ruling). A halted cell whose end state DID pass is PASS: a pass is a pass
    UNSCORABLE  the suite could not give a verdict on the cell (the runner's own TIMEOUT or ABORT, a VOID the record declares, an end state
                the record says was not scored). It is neither pass nor fail
  ```
- **The rc-3 census** (`CENSUS-rc3-verdicts-2026-09-30.md`) re-scored 8 cells whose record read BUILD-FAIL `0/0`. Where an addendum to the
  owning result has taken its correction, the corrected verdict is the record's. Where none has yet, the record's verdict governs. The census's
  class is printed beside that cell in the result file, and the row is marked `rc3` so a reader sees the disagreement.

## §P3 · THE CONDITION CELL
`k / n` passes, where n is the count of PASS + FAIL cells. A condition with censored or unscorable cells prints them beside it, as
`k / n (+c censored, +u unscorable)`. **A censored cell enters neither k nor n.** `—` marks the 16 INEXPRESSIBLE conditions and `declared`
the 3 DECLARED (§D3's marks, unchanged). A cell of record with no tracked verdict is `unmeasured`. Its condition prints `unmeasured`,
and the check below FAILS VISIBLY. ⛔ No verdict is recovered by hand: not from a message, a bus post, or a transcript read by eye.

## §P4 · THE FOUR TABLES
```
  P1  greenfield    20 rows (model × problem) × {bare-plain, bare-salt-diet, statement-plain, statement-salt-diet}   80
  P2  brownfield    the same 20 rows × the same 4 columns                                                          80
  P3  spec-change   greenfield only; 20 rows × {plain, salt-diet}                                                  40
      CHECK  conditions with a k/n + "—" + "declared" = 181 + 16 + 3 = 200, or a cell is wrong and the instrument exits non-zero
  P4  signs         20 rows × {bare, statement, spec-change} (GREENFIELD, as T4), each the sign of salt-diet's pass rate against plain's
```
- **The sign is computed so that censoring can never manufacture it.** For each arm, take the INTERVAL of rates the censored and unscorable
  cells allow: [k / (n + c + u), (k + c + u) / (n + c + u)]. Then:
  ```
    +    salt-diet's interval lies wholly ABOVE plain's
    −    salt-diet's interval lies wholly BELOW plain's
    =    both intervals are the same single point (no censored or unscorable cell on either side, and equal rates)
    ?    anything else: INDETERMINATE, named and counted in neither direction
  ```
  ⛔ A halt can therefore never turn a `?` into a `+` or a `−`, in either direction. The cap binds salt-diet more often, so this protects
  the arm the cap censors.
- **The count, per model per treatment:** `+ k · = e · − j · ? i` over that model's five problems with a sign. The brownfield signs are
  computed by the same rule and printed in the result file, not in P4 (T4's choice, kept).

## §P5 · THE INSTRUMENT AND THE FILE OF RECORD
ONE instrument (`tables_correctness_v3.py`), ONE condition map, ONE result file (`RESULT-correctness-tables-v3-2026-10-01.md`), landed in the
SAME commit. The map extends `CELLMAP-descriptive-tables-v2-2026-09-27.tsv` with each cell's VERDICT SOURCE (file and line of the result of
record that prints it). Every table cell cites its rows. paper copies the tables into v3 by script, as `cost_tables.py` does.
**Second method, before the result is quoted:** the instrument's per-condition `k` is compared with every count a result of record already
prints for that condition (e.g. "FULL PASS 3 of 3"). Each disagreement is printed and counted in the result's header and never resolved
by hand, the cost tables' form.

## §P6 · WHAT THIS READING CANNOT ESTABLISH, SAID BEFORE ANY NUMBER
- It cannot say the salt method makes code more or less correct. n = 3 per condition; a rate of 3 cells moves in thirds.
- A PASS is the withheld suite's verdict, so it is bounded by that suite's strength. The suites' mutant scores are CEILINGS, not strengths
  (the statement-arm result's own words).
- Censoring is arm-correlated: the cap binds salt-diet more often. The interval rule keeps a halt from manufacturing a sign. It also makes the
  `?` count arm-correlated, and the result prints how many `?` come from censoring on each arm.
- The agy and Claude lanes score with different scorers of record. A row compares arms within one model and one problem, where one scorer
  serves both.
- Post hoc: the method was fixed after the verdicts existed and had been read. Only the method's being fixed before THIS instrument ran is
  claimed.

---
## ⚖️ ADDENDUM 1 — TOUCHING INTERVALS DO NOT SEPARATE (STRICT). APPENDED BEFORE THE INSTRUMENT RUNS; §P1–§P6 untouched.
paper's boundary question (2026-10-01 10:38, as the copier, not a signature): §P4's "wholly above" did not say whether intervals that SHARE
an endpoint separate. **STRICT: they do not.** `+` needs salt-diet's lower end strictly greater than plain's upper end, and `−` the mirror.
A shared endpoint is `?`. paper's example: plain 2/3 with none censored is [2/3, 2/3], salt-diet k = 2, n = 2, c = 1 is [2/3, 1], and that
pair reads `?`, never `+`. It is the reading under which a halt can never turn a `?` into a sign.

## ⚖️ ADDENDUM 2 — A CONDITION WITH NO PASS-OR-FAIL CELL PRINTS `n = 0`, NEVER `0/0`. APPENDED BEFORE THE INSTRUMENT RUNS.
kent's display note at the non-author read (2026-10-01 10:40, no defect): every result of record uses `0/0` for BUILD-FAIL, so a condition
whose cells are all censored or unscorable prints `n = 0 (+c censored, +u unscorable)` and never `0/0`. Presentation only: no class, count
or sign rule changes. The fixture arm for the touching-interval case (the helm, 10:38:57) is owed in the instrument's selftest, red-first.

## ⚖️ ADDENDUM 3 — FIVE SOURCE SHAPES THE CELL VERDICT MEETS, FIXED BEFORE ANY TABLE OR SIGN IS READ. §P1–§P6 and ADDENDA 1–2 untouched.
bench, 2026-10-01. ⚠️ **Written after trial runs of the instrument over a draft map printed the 200 check, the class totals and the list of
unmeasured cells. No table, no condition's k / n and no sign had been read.** The trials found that the results of record print a cell's
verdict in more shapes than §P2's one ("a line naming the cell"). Each rule below says how the instrument reads one shape, and none of them
lets a verdict be typed.
- **(a) A halt with no suite verdict is CENSORED.** Some records print a landing word in their verdict column (`NOT-LANDED`, "no
  LANDING.md") because the scorer of record did not score a cell that did not land. That word is not a suite verdict. When such a cell's
  end is a registered halt, its class is CENSORED, because it halted and the record shows no pass. `TURN-TIMEOUT` is the per-turn deadline,
  which §P2 lists as "a turn ... DEADLINE". Where another file prints a score for such a cell, that score is printed as a second-method row
  and is never folded in.
- **(b) A verdict word that says the suite gave none comes before the halt test.** VOID, NOT-SCORED, TIMEOUT (the runner's own), ABORT and
  INCOMPLETE make a cell UNSCORABLE even when its end is also a halt, because §P2 names "a VOID the record declares" there. A pass is still
  a pass, whatever the end. This changes no interval: censored and unscorable cells widen it the same way.
- **(c) A verdict printed once for a whole wave** (e.g. "wave 2 (6 cells): PASS 6 (TESTS 7/7 each)") reaches a cell only through bytes. The
  verdict line names the wave and its size, a line of the same result names the wave and its run root, and the tracked roots table puts
  the cell in that root, which holds exactly that many cells. Otherwise the cell is `unmeasured`.
- **(d) A record that prints only a per-condition count gives that condition its k / n directly, and only under two conditions.** The
  count's n equals the condition's cells of record. Every one of those cells is shown LANDED by a tracked line (its own per-cell end, or a
  line of the same table stating that all its cells landed). Then k cells are PASS and n − k are FAIL, no cell is censored, and the cells
  are printed `by condition`, never as individual verdicts. The whole condition is read this way or not at all: a prose line that names
  one of its cells (e.g. "its PASS stands") is cited in that cell's note and is not read. If either condition fails, every cell of the
  condition is `unmeasured`.
- **(e) The population is the census's at its current head (§P1).** v2's map dates from 2026-09-27. Census ADDENDA 30–32 (2026-09-29) made
  twelve more cells cells of record: `clbglp01`; `s3fpk01`, `s3fpk02`, `s3fqk01` and `s3ctk01`; and step g's seven `clbk*`. They enter this
  map as rows marked ADDED. No cell is dropped.
- **Second method, read the same way:** printed counts include figures an addendum has since superseded, and counts over other populations
  (landed cells only, a smoke cell included). They are compared and every disagreement is listed with its source's own description. A
  disagreement is not resolved. The run's exit code reports the 200 check and the unmeasured cells, and it does not gate on these rows.
