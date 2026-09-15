# AUDIT — the §3b budget-read column was inoperative, and is corrected before the cell it could flatter

**Date:** 2026-09-15. **Scope:** HC stage 1, the disambiguating column registered in
`PREDICTIONS-HC-stage1-2026-09-13.md` §3b. **Status of the pre-registration: UNCHANGED.** No amendment
is taken and none is owed; see "What this is not", below.

**Why this is written now rather than with the result.** The wave stands at 11 cells fired of 45. The
next cell in firing order is the **first of the six predicted cap-outs** (§3a), and therefore the first
landing at which §3b's NEAR-CAP band can occur at all. A correction to a scoring instrument is credible
in proportion to its being recorded *before* the observation it governs, which is the same reason §3a
and §3b were themselves registered before the first cell fired.

## 1. What §3b registers

§3b establishes that the cost cap is visible to the subject — `BUDGET.md` sits in the subject's working
directory and is rewritten every tick — so a landing just under the cap is **pacing, not evidence**. It
defines a NEAR-CAP band of `[0.95 × C1, C1)` = `[$35.35, $37.21)` and rules it **its own outcome**:
neither a cap-out nor a falsification of one. It then requires a per-cell column:

> "for every stage-1 cell, **whether its transcript shows the subject reading `BUDGET.md`** — the file
> is in its cwd and **a read is a tool call**, so this is observable rather than argued."

## 2. The defect

The registered criterion is broad and correct: *a read is a tool call*. Two operational restatements of
it — one in the wave's fire order, one in the harvester's own output — narrowed it to **"a `Read` tool
call"**. The subjects do not read `BUDGET.md` with the `Read` tool. They read it with `cat`, inside a
`Bash` tool call, as part of an orientation command issued early in the episode.

Measured over every HC stage 1 session transcript in existence at this date (11 cells: the nine Crc32
cells, plus FreeList plain n=1 and FreeList placebo n=1):

| how the column was computed | result |
| --- | --- |
| a naive substring count of `BUDGET.md` | 3 per cell (two are not reads) |
| the restatement: a `Read` tool call | **0 of 11** |
| what the harvester in fact counted: mentions in the cell's `ctl/*.log` | **0 of 11** |
| the registered criterion: a **tool call** that reads the file | **11 of 11** |

Three distinct quantities, two of them zero by different mechanisms, and the column that disambiguates
the NEAR-CAP band would have read `NO-READ` for every cell of the wave. This is an inversion, not a
miscount. The two non-read occurrences per cell are the arm's own statement text describing budgets, and
a harness source file naming `BUDGET.md` in a skip list — so a loose needle over-counts and a strict
needle under-counts, in opposite directions, and neither is the registered quantity.

Representative evidence, FreeList plain n=1: a single `Bash` tool call at transcript record 37 whose
command contains `cat BUDGET.md 2>/dev/null`; zero `Read` tool calls naming the file anywhere in 143
records.

## 3. The direction of the error, which is the part that matters

The error is **arm-correlated and it favours this campaign's own prediction.** §3a predicts that the
`salt-bare` arm caps out on FreeList and Paxos. Under-counting budget reads moves a NEAR-CAP landing out
of "the subject paced itself to a countdown it can read" and into "the subject genuinely capped out" —
which is precisely the reading under which §3a's prediction appears confirmed.

§3b exists because "the harness's own disclosure could 'refute' the two sharpest predictions in this
file, and the refutation would be the instrument talking." An inoperative column would have let the same
instrument talk in the **opposite** direction, silently, with no refutation to notice. **The correction
therefore cuts against the campaign's own sharpest prediction**, and that is the principal reason to
trust it rather than to trust the reading it replaces.

## 4. What is corrected, and what is not

- **Corrected:** the column is now computed per cell by a dedicated instrument, invoked automatically by
  the wave's harvester. It reports each route separately — `Read` tool call · `Bash` call applying a read
  verb to the file · search tool targeting it · and, counted apart as *not* reads, mention-only-in-a-Bash
  command, mention inside another tool's payload, tool results, assistant prose, and statement text. It
  **refuses to collapse these to a boolean**, because collapsing routes is the act that produced the
  original defect. A write to `BUDGET.md` is reported separately again, as its own finding, never as a read.
- **Not corrected, because it is not wrong:** `PREDICTIONS-HC-stage1-2026-09-13.md`. The registered text
  says "a tool call" and has always been satisfiable. Nothing registered is edited, widened, or re-scoped.

## 5. No landed verdict changes

The NEAR-CAP band begins at `$35.35`. The most expensive cell landed to date is `$14.53`
(Crc32 salt-diet n=1). No cell yet landed is in or near the band, so **no scored verdict is affected by
this correction**, and the column becomes load-bearing for the first time on the next cell fired.

## 6. An error in the correcting instrument, recorded because it is the same class

The instrument's first draft folded "any other tool call carrying the string" into its read count, and
so scored Crc32 salt-diet n=3 as **2 reads** where the truth is **1** — because a `Write` to the
subject's own memory file *mentioned* `BUDGET.md` in its payload. The discriminator is the **target of
the call**, not the presence of the string. This was caught and fixed before the figure was quoted
anywhere, and it is recorded here because an instrument built to fix an over-counting-and-under-counting
defect reproduced the over-counting half on its first run.

## What this is not

This is not an amendment, and it does not change what any run measures. It records that an instrument
did not implement a registered criterion, corrects the instrument, and states the direction of the bias
the defect would have introduced. The pre-registration stands as written and as dated.
