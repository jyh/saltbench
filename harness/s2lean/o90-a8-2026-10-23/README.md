# O90 inputs from AMENDMENT 8's run: the a2/a0 token-ratio spread [F11c] and calls-to-first-green [H3]

Two read-only measurements over the 60 episodes of SCOUT-S2LEAN-STAGE0.md "### Amendment 8" (U15, `claude-opus-5`,
arms `a0` and `a2`, stages A and B). They feed the O90 test design's §4: the noise floor for the cost axis's 1.5
threshold and the U3 tokens clause's 0.8 threshold ([F11c]), and whether the harness keeps a per-call build trace that
the `calls-to-proof` clause can run on ([H3]). Nothing here was spent: no model call, no episode, no write to the run box.

**Source.** The run's state root on the run box, `~/bench-a8/state/ep-*/` (60 episode dirs) and
`~/bench-a8/logs/s2-landings.log`, copied read-only to a local scratch directory (`canonical.olean` excluded). Neither
tool types a problem id or an episode id: both derive the population from the manifests.

**Reproduce.**

```
python3 -I spread.py         --state <copy>/state --landings <copy>/logs/s2-landings.log [--json spread.json]
python3 -I spread.py         --state <copy>/state --landings <copy>/logs/s2-landings.log --selfcheck
python3 -I calls_to_green.py --state <copy>/state [--json calls_to_green.json]
python3 -I calls_to_green.py --selftest
```

The outputs of exactly those commands are committed beside the tools: `spread.out.txt`, `spread.json`,
`spread.selfcheck.txt`, `calls_to_green.out.txt`, `calls_to_green.json`, `calls_to_green.selftest.txt`.

---

## 1. `spread.py`: the per-problem a2/a0 token ratio [F11c]

### Definitions and the field used

- **Tokens** `T` = manifest field **`metered_sum_governing`**: the CLI's own `modelUsage` sum for the episode, which
  the meter cross-checks against the transcript (`meter.json` → `crosscheck.metered_sum_governing`). It includes the
  CLI's small side-model usage (`claude-haiku-4-5` in every `modelUsage`; governing − `metered_sum` is 1,017–1,027 tokens
  in each of the 60). The
  transcript-only main-model field `metered_sum` is printed beside it.
- **Population** = the problems where **both** `a0` and `a2` have manifest `passed = true` at stage B. Derived: **n = 9**
  (16, 31, 38, 54, 73, 74, 141, 142, 146), which is the amendment's `9 both-proved at Opus` (10/15 each,
  `a0`-only {112}, `a2`-only {4}).
- `r_B = T(a2, B) / T(a0, B)`; `r_AB = (T(a2, A) + T(a2, B)) / (T(a0, A) + T(a0, B))`, on the same nine problems.

### The 26,104,403 reproduction

| field | stage A | stage B | A + B | the amendment text |
|---|---|---|---|---|
| `metered_sum` | 5,952,298 | 20,090,848 | 26,043,146 | **does not** reproduce |
| **`metered_sum_governing`** | **5,982,892** | **20,121,511** | **26,104,403** | **reproduces exactly**, and both stage figures too ("Stage A 5,982,892 · stage B 20,121,511") |

The tool parses the figure from the amendment text itself, never from this README. A second, independent match: the
aggregate `sum a2 / sum a0` at stage B over the nine is **1.5055**, the amendment's "+50.6 %" for the 9 both-passed at
Opus.

### Readings (from `spread.out.txt`)

| problem | a0 B | a2 B | **r_B** | a0 A+B | a2 A+B | **r_AB** |
|---|---|---|---|---|---|---|
| 16 | 384,790 | 427,296 | 1.110 | 452,015 | 749,972 | 1.659 |
| 31 | 140,498 | 209,150 | 1.489 | 207,864 | 368,028 | 1.771 |
| 38 | 605,836 | 1,190,213 | 1.965 | 705,686 | 1,478,689 | 2.095 |
| 54 | 54,768 | 106,640 | 1.947 | 156,966 | 304,767 | 1.942 |
| 73 | 832,471 | 664,691 | 0.798 | 938,865 | 1,023,940 | 1.091 |
| 74 | 154,982 | 225,320 | 1.454 | 241,073 | 368,562 | 1.529 |
| 141 | 180,396 | 424,885 | 2.355 | 484,340 | 731,976 | 1.511 |
| 142 | 400,478 | 477,673 | 1.193 | 525,907 | 763,902 | 1.453 |
| 146 | 967,038 | 1,876,634 | 1.941 | 1,064,075 | 2,614,511 | 2.457 |

| spread measure (n = 9) | r_B | r_AB |
|---|---|---|
| median r · geometric mean | 1.489 · 1.507 | 1.659 · 1.682 |
| r > 1 · r > 1.5 · r < 0.8 | 8 · 4 · 1 of 9 | 9 · 7 · 0 of 9 |
| median \|r − 1\| | 48.9 % | 65.9 % |
| IQR(r) (Q1, Q3) | 0.754 (1.193, 1.947) | 0.430 (1.511, 1.942) |
| min · max · max/min | 0.798 · 2.355 · 2.95 | 1.091 · 2.457 · 2.25 |
| **exp(MAD of ln r)**, dispersion about its own centre | **1.308 (±30.8 %; 1/1.308 = 0.765)** | 1.142 (±14.2 %; 0.876) |
| exp(median \|ln r\|) | 1.489 | 1.659 |

### Which spread to use, and why

**Recommended: `exp(MAD of ln r)` on r_B = 1.308**, read as a multiplicative band of ×1.308 up and ×0.765 down.

- **It removes the arm shift.** `a2` and `a0` are different arms: `a2` is the dearer arm at Opus (median r_B 1.49,
  amendment 8's failed prediction 3). Measures centred on 1 (`median |r − 1|`, `median |ln r|`) are dominated by
  that shift (48.9 % is mostly the 1.49 centre, not dispersion), so they measure the arm difference and not the
  instrument. Centring on the sample's own median leaves the problem-to-problem dispersion.
- **It is symmetric for ratios**, so one number serves the 1.5 threshold above 1 and the 0.8 threshold below it.
  `IQR(r)` is on the linear scale and is not symmetric about a ratio.
- **It is robust at n = 9.** `max/min` is set by two problems (73 and 141) and the IQR by four order statistics.
- **Stage B, not A+B**, because the O90 cost axis compares stage-B proving and the P+U paragraph changes `prompt_B.md`
  only, so stage A is the same instruction in both O90 arms. The A+B figure is tighter (1.142) because stage A's
  `a2`/`a0` overhead (amendment 8 addendum 3: 2.44) is a near-constant shift that pulls every r_AB the same way.

**What it says for §4.** The 1.5 cost margin sits above the ×1.308 band, but not by much (1.5 / 1.308 ≈ 1.15). The
U3 tokens clause [H2] replaces 0.8 by "(1 − spread) if that spread exceeds 20 %". This spread is 30.8 %, so the rule
fires: on the linear form 1 − 0.308 = 0.692, on the log-symmetric form 1/1.308 = 0.765. Choosing between them is
the design's call. The second is the one consistent with treating the spread as a ratio band.

### Limits (these apply to every figure above)

- ⛔ **a2/a0 IS AN ARM DIFFERENCE PLUS NOISE, NOT NOISE.** Amendment 8 ran each (problem, arm) once, so the run holds
  no same-arm replicate and cannot isolate run-to-run noise. Centring removes the arm's average shift but not its
  interaction with the problem (the salt arm may cost more on some problems than on others), so the 1.308 is
  **arm × problem interaction plus noise**. As a noise floor it is probably an **over**-estimate, which makes the
  margin conservative. Its size is unmeasured. Measuring pure noise needs same-arm repeats, which this run does not
  contain.
- n = 9, and the 1.308 is itself uncertain at that n (no interval is computed here).
- Conditioned on both arms passing ([F11b]): the hardest problems (112, 4) are excluded.
- One model, one tier (`claude-opus-5`, effort `high`), one run.

### Self-check, and the mutants driven red (`spread.selfcheck.txt`)

Each invariant is checked against a source other than the computing path:
**I1** the 60-episode sum of the field equals the figure parsed from the amendment text ·
**I2** the population equals the both-passed set derived independently from each episode's `check.json` `passed` ·
**I3** each r_B equals the ratio recomputed from the landings log (the driver's own record, with its own arm and stage
labels).

| run | rc | which invariant fired |
|---|---|---|
| pristine | 0 | none (I1 I2 I3 hold) |
| `--mutant swap` (a0 ↔ a2) | **1** | I3: every r_B inverted against the landings |
| `--mutant allprob` (filter dropped, 15 problems) | **1** | I2: the population is not the both-passed set |
| `--mutant field` (`metered_sum`) | **1** | I1: 26,043,146 ≠ 26,104,403. I3 also fires, which shows the landings column is the governing field |

---

## 2. `calls_to_green.py`: calls up to the first green compile of the task file [H3]

### Definitions

- **Tool call**: each assistant `tool_use` on the main thread, in transcript order, numbered from 1. **API call**: a
  distinct assistant `message.id`.
- **Compile call**: a Bash tool call whose command runs `[lake env] lean [-flags] [path/]task.lean`, directly or
  through the episode's `rt` wrapper (`./rt`, `../rt`, `<ep>/rt`; `harness/s2lean/rt.template`). Lean on any other
  file (scratch files, or a copy such as `task.check.lean`) is not a compile call.
- **rt rc**: `rt.template` logs `START`/`END rc=N` for every invocation to `.rt.log`, which `episode_s2.sh` moves to
  `<state>/rt.log`. Each START is assigned to the last tool call whose timestamp, floored to the second, is ≤ the
  START second. Lean exits non-zero on an error. A `sorry` is a warning only and exits 0.
- **Diagnostics** in the call's `tool_result` text, for the task file only. Errors are counted in both forms,
  `task.lean:L:C: error:` and `task.lean:L:C: error(lean.xxx):`, plus lake's marker-first form
  `error: …task.lean:L:C:` and any bare line-initial `error:`. Sorry is
  `task.lean:L:C: warning: declaration uses 'sorry'`.
- **Visibility** of the lean output in the result. The pipeline after the lean invocation is classified as one of:
  - **OPAQUE**: a stdout redirect; `grep -c`, `grep -q` or `wc`; a `grep -v` or positive `grep` that would hide an
    error line or the sorry line (tested against sample lines); or an unrecognised stage.
  - **TRUNC(N)**: `head`, `tail` or `sed -n 1,Np`. This counts as transparent only if the result has fewer than N
    lines.
  - **CLEAR**: anything else.
- **Verdict**:
  - **RED**: a task-file error or sorry diagnostic is visible, or a task-file rt rc is not 0.
  - **GREEN**: an rt END with rc=0 for the task file, no diagnostic, and CLEAR output.
  - **GREEN_NORT**: the same without any rt record (a direct `lake env lean`), which is weaker because nothing proves
    the compile ran.
  - **UNDET**: no diagnostic is visible, but the output was opaque or may have been truncated.
- **First green**: the index of the first GREEN or GREEN_NORT compile call. `1st_maybe`, the first GREEN, GREEN_NORT
  or UNDET call, is an optimistic bound. Where the two differ, the episode's reading is ambiguous.

### Is the transcript a per-call build trace? Measured over all 30 stage-B episodes

| property | reading |
|---|---|
| tool results present | every tool call has its `tool_result` (0 missing) |
| subagent sidechains | **none**: 0 `isSidechain` lines, every episode's `configdir-projects` holds exactly 1 `.jsonl` and 0 `subagents/` dirs (the harness denies `Agent`/`Task` and voids an episode with a subagent) |
| transcript API calls vs manifest `calls` | equal in **30 of 30** |
| tool calls per API call | one in every episode (no parallel tool calls) |
| results the CLI cut | 1 (`<persisted-output>`, problem 146 / `a2`, call 7, a `find` listing, **not** a compile call) |
| rt records | every rt START assigned to a tool call (0 unassigned). One episode (73 / `a0`) never used `rt` and compiled with a direct `PATH=… lake env lean`, so it has no `rt.log` and its greens are GREEN_NORT |
| ambiguous episodes | 0 (first green = first maybe in all 30) |

⇒ **Yes, with limits.** The transcript plus `rt.log` gives an ordered, complete per-call record of every compile the
agent ran on the task file, its rc (when through `rt`) and its visible diagnostics. It records only compiles that
**the agent chose to run**. It is not a harness-side replay of the file after each edit, so the clause measures "the
first time the agent saw its task file compile clean" and not "the first call after which the file would have
passed". The two differ whenever the agent edits and does not recompile.

### Readings (`calls_to_green.out.txt`), all 30 stage-B episodes

| problem | arm | passed | class | tool calls | compiles | **first green** | kind | last compile |
|---|---|---|---|---|---|---|---|---|
| 0 | a0 | F | AXIOMS_FAIL | 8 | 1 | – | | RED |
| 0 | a2 | F | AXIOMS_FAIL | 17 | 4 | – | | RED |
| 4 | a0 | F | AXIOMS_FAIL | 18 | 5 | – | | RED |
| 4 | a2 | T | PASS | 8 | 2 | 4 | GREEN | GREEN |
| 16 | a0 | T | PASS | 18 | 2 | 16 | GREEN | GREEN |
| 16 | a2 | T | PASS | 17 | 1 | 15 | GREEN | GREEN |
| 18 | a0 | F | KERNEL_REJECTED | 27 | 1 | – | | RED |
| 18 | a2 | F | AXIOMS_FAIL | 16 | 2 | – | | RED |
| 31 | a0 | T | PASS | 7 | 2 | 6 | GREEN | GREEN |
| 31 | a2 | T | PASS | 9 | 2 | 4 | GREEN | GREEN |
| 38 | a0 | T | PASS | 18 | 1 | 15 | GREEN | GREEN |
| 38 | a2 | T | PASS | 27 | 3 | 19 | GREEN | GREEN |
| 54 | a0 | T | PASS | 3 | 2 | 3 | GREEN | GREEN |
| 54 | a2 | T | PASS | 6 | 2 | 3 | GREEN | GREEN |
| 73 | a0 | T | PASS | 28 | 4 | 25 | GREEN_NORT | GREEN_NORT |
| 73 | a2 | T | PASS | 22 | 5 | 17 | GREEN | GREEN |
| 74 | a0 | T | PASS | 7 | 3 | 6 | GREEN | GREEN |
| 74 | a2 | T | PASS | 9 | 3 | 5 | GREEN | UNDET |
| 96 | a0 | F | AXIOMS_FAIL | 14 | 3 | – | | RED |
| 96 | a2 | F | AXIOMS_FAIL | 15 | 3 | – | | RED |
| 112 | a0 | T | PASS | 55 | 11 | 50 | GREEN | UNDET |
| 112 | a2 | F | **SCREEN** | 55 | 4 | **47** | GREEN | GREEN |
| 127 | a0 | F | AXIOMS_FAIL | 8 | 1 | – | | RED |
| 127 | a2 | F | AXIOMS_FAIL | 10 | 1 | – | | RED |
| 141 | a0 | T | PASS | 8 | 1 | 8 | GREEN | GREEN |
| 141 | a2 | T | PASS | 16 | 3 | 10 | GREEN | UNDET |
| 142 | a0 | T | PASS | 11 | 2 | 8 | GREEN | GREEN |
| 142 | a2 | T | PASS | 16 | 2 | 11 | GREEN | GREEN |
| 146 | a0 | T | PASS | 26 | 2 | 25 | GREEN | GREEN |
| 146 | a2 | T | PASS | 34 | 3 | 29 | GREEN | GREEN |

(The API-call index at the first green equals the tool-call index in every episode, because each API call issued one
tool call.)

**Cross-check.** **20 of 20** passed episodes have a first green, so there are no exceptions. **1 of 10** failed
episodes has one: **112 / `a2`, class SCREEN**, the cell amendment 8 records as never compiled by the checker (the
screen refused `set_option linter.deprecated false`). The agent's own compile of that file was clean at call 47. This
agrees with amendment 9's later finding that the refused cell would have passed the checker (its §9.4 diagnostic). The other nine failures (8 `AXIOMS_FAIL`,
1 `KERNEL_REJECTED`) never compiled clean: every compile was RED, on a sorry or an error.

**Paired, both arms passed (n = 9):** `a2` needs more calls to its first green than `a0` in **4**, fewer in **4**,
and the same in **1**. The median a2/a0 ratio of first-green indices is **1.000**. Total tool calls are higher for
`a2` in 7 of 9 (from the same table). On this run the arms differ more in total calls than in calls to the first
green, which is the separation [H3] exists to make. This is a reading of one run, not a test.

### Selftest, and the mutants driven red (`calls_to_green.selftest.txt`)

There are five synthetic fixtures, built by the tool in a temp dir: a sorry then a clean compile; a tagged
`error(lean.unknownIdentifier)` on a direct (no-rt) compile; the wrapper's bound (rc 124) with clean-looking output; a
`grep -v sorry` filter; and a scratch-file compile plus a `task.lean.bak` mention. Each detector is removed by a
mutant, and the suite must go red:

| mutant | result |
|---|---|
| none | PASS 5/5 |
| `nosorry` (sorry warning ignored) | **RED**: the sorry fixture's first green moves 3 → 2 |
| `noerrtag` (tagged `error(…)` form not counted) | **RED**: the errtag fixture's first green moves 2 → 1 |
| `norc` (rt rc ignored) | **RED**: the rc-124 fixture's first green moves 2 → 1 |
| `nofilter` (visibility analysis off) | **RED**: the filter fixture's first green moves 2 → 1 |

### Limits

- **Agent-run compiles only** (above). An episode that never compiles its final task file can still PASS the checker
  and would show no first green. That case did not occur here (20 of 20).
- **A copy is not counted.** 112 / `a2` also compiled `task.check.lean` (a copy). A green on a copy is invisible to
  this definition.
- **GREEN_NORT is weaker.** In 73 / `a0`, nothing but the clean output shows the compile ran. Its commands echoed
  `EXIT:0`, but that is the pipeline's last stage and was not used as evidence.
- **Visibility is a classifier over shell text.** It recognises `grep`/`grep -v`/`head`/`tail`/`sed -n`/redirects.
  Anything else is OPAQUE (so UNDET, never GREEN). Any first green that was UNDET would show as ambiguous, and none
  was.
- **The in-session green is not the checker's verdict.** The checker re-assembles the scored bodies, screens them and
  audits axioms and statements (see 112 / `a2`). The in-session green also does not verify that the agent left the
  frozen statements unaltered.
- **One run.** The first-green indices carry the same no-replicate limit as §1.
