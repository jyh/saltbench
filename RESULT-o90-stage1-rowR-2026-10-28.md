# RESULT — O90 stage 1, row R: the U1 and U2 reads (AMENDMENT-O90-stage1 ADDENDUM 2 A2.3–A2.10, ADDENDUM 6) — set halted 2026-10-28

Every figure below is copied from `harness/s2lean/o90-2026-10-23/rowR-2026-10-28/score.out`. That file is the output of
`harness/s2lean/o90-2026-10-23/o90_rowr_score.py` (blob f4475d918b5d) over the set's frozen reads, which are copied into the same
directory and hashed in its `SHA256SUMS.evidence`. Nothing is retyped from a message. Writing this file cost no model call.

**Every U1 and U2 accuracy in this file is "by one reader mechanism (Gemini)"** (A2.8 rider 2), and the reader is not blind to
the arm (A2.7).

⛔ **Stage 1 is INCOMPLETE** (A2.8 rider 1). This file records what row R scored. It is not a stage-1 verdict. The truth axis
has its own record, `RESULT-o90-stage1-truth-axis-2026-10-31.md`, and this file does not combine the two.

## The set: HALTED at 319 of 323 (A2.6)

```
HALTED: 319 of 323 reads, reported at the n it reached (A2.6); HALT: 2026-10-28T14:35:17Z spend 12pt > 11.0pt
NOT READ (declared missing): seq 320 U2 p92-a5-def-1 a5 · seq 321 U2 p112-a0-def-0 a0 · seq 322 U2 p149-a5-theorem-0 a5 · seq 323 U2 p146-a0-def-0 a0
```

The set stopped on A2.6's spend halt at A6.7's resume dial of 11 points. A2.6 says a halted set is reported at the n it
reached, so every figure below is at n = 319. All 138 U1 reads ran. 181 of 185 U2 reads ran. The four unread seqs are all
U2, two per arm. `read-320` finished but the harness never wrote it to `reads.tsv`. It is not scored, it is not copied here,
and its verdict has not been opened. The lead ruled on 10-28 (bus @91,462,713): no cap extension, and no DONE written.

The scorer exits 4 (HALTED). It accepts the HALT line only after checking it against the record: the dial must be 12 or 11
(systems' read of #413).

## U1 (A2.3, A2.10 Q3): yes/no against the kernel's key, `cannot tell` scored wrong

```
U1 ALL: 12 problems 2 4 16 31 35 52 59 73 74 82 141 148
  a0: reads 69 · scored 68 · correct 68 · accuracy 100.0% · cannot-tell 0 (scored wrong) · accuracy over answered 100.0% (68) · UNSCORED 1 · spec_recoverable yes 0 partial 2 no 10
  a5: reads 69 · scored 69 · correct 69 · accuracy 100.0% · cannot-tell 0 (scored wrong) · accuracy over answered 100.0% (69) · UNSCORED 0 · spec_recoverable yes 6 partial 2 no 4
  paired items 68: both right 68 · a5 only 0 · a0 only 0 · neither 0
  a5 − a0 accuracy +0.0 points (by one reader mechanism (Gemini))
U1 NEITHER-YES: 6 problems 2 4 16 35 74 141
  a0: reads 42 · scored 42 · correct 42 · accuracy 100.0% · cannot-tell 0 (scored wrong) · accuracy over answered 100.0% (42) · UNSCORED 0 · spec_recoverable yes 0 partial 2 no 4
  a5: reads 42 · scored 42 · correct 42 · accuracy 100.0% · cannot-tell 0 (scored wrong) · accuracy over answered 100.0% (42) · UNSCORED 0 · spec_recoverable yes 0 partial 2 no 4
  paired items 42: both right 42 · a5 only 0 · a0 only 0 · neither 0
  a5 − a0 accuracy +0.0 points (by one reader mechanism (Gemini))
U1 ROUTE (a reading of A2.10 (b)/(c), deciding no VOID by itself): +10 not reached on ALL: the U1 route condition is NOT MET — HALTED set, reported at the n it reached (A2.6)
```

**The U1 route is NOT MET.** a5 − a0 is +0.0 points on ALL and on NEITHER-YES, against A2.10's +10. Both arms score 100 %, so
at this reader U1 cannot tell the arms apart in either direction. NOT MET here means U1 is at ceiling. It does not mean the
two arms were measured as equally understood. The route reading decides no VOID by itself.

## U2 (A2.4): per option against `frozen/u2/items.tsv`

```
U2 a0: artifacts read 23 (21 with a scored option) · options scored 441 · UNSCORED options 264 · POOLED accuracy 97.3% · MEAN of per-artifact accuracy 97.9% over 21 (by one reader mechanism (Gemini))
U2 a5: artifacts read 24 (24 with a scored option) · options scored 532 · UNSCORED options 200 · POOLED accuracy 97.7% · MEAN of per-artifact accuracy 97.9% over 24 (by one reader mechanism (Gemini))
```

`score.out` prints each artifact's figure. Two a0 artifacts (ep-26a7ef9e and ep-558aedfa) have no scored option, because
every option in them is UNSCORED.

**U2-theorem, with A6.8's bounds** (a timed-out option is counted as wrong for one bound and as right for the other):

```
U2-theorem a0: options scored 164 · correct 160 · observed 97.6% · timed-out options 128 · bound WRONG 54.8% · bound RIGHT 98.6% (A6.8)
U2-theorem a5: options scored 212 · correct 205 · observed 96.7% · timed-out options 88 · bound WRONG 68.3% · bound RIGHT 97.7% (A6.8)
U2-theorem a5 vs a0: observed a5 < a0 · a5-worst/a0-best a5 < a0 · a5-best/a0-worst a5 > a0 ⇒ UNDECIDED (the two bounds do not share one strict direction), beside the observed figure (A6.8)
```

**The U2-theorem comparison is UNDECIDED.** The observed figure puts a5 below a0, but the two bounds point in opposite
directions, and A6.8 decides by the bounds.

## UNSCORED reads, counted and never guessed (A2.3, A2.4, A6.3, A6.5)

```
UNSCORED reads by cause × kind × arm (A6.3): parse U1 a0 1 · parse U2-def a0 6 · parse U2-def a5 4 · parse U2-theorem a0 8 · parse U2-theorem a5 8 · print timeout U2-def a0 3 · print timeout U2-def a5 2 · print timeout U2-theorem a0 16 · print timeout U2-theorem a5 11
Reads with a print-timeout attempt, rescued (answered later) / all, by kind × arm (A6.5 condition): U2-def a0 1/7 · U2-def a5 2/6 · U2-theorem a0 2/21 · U2-theorem a5 1/18
```

The reader asked the lead for no VOID, and no read row was voided.

## Spend (A6.7, A6.10, A6.11)

```
POOL readings of the set (A6.11): 07:14 START 88% · 11:25 START 87% · 11:34 START 88% · 12:39 START 87% · 16:55 POOL 86% · 22:19 POOL 86% · 02:57 POOL 85% · 08:21 POOL 84% · 14:47 POOL 84% · 18:02 POOL 83% · 20:33 POOL 82% · 02:15 POOL 81% · 06:17 POOL 80% · 12:10 POOL 80% · 17:27 POOL 78% · 22:25 POOL 78% · 03:36 POOL 78% · 09:11 POOL 76% · 14:35 POOL 75% ⇒ S (sum of drops; the halt) 14 · D (net, 88 − 75; A6.5) 13
A6.5 named reading 2026-10-25T22:19:58Z: n 57 · D 2 · 323·x/n = 11.33 ⇒ (B) is NOT available; (A) stands to the end of row R
```

The Gemini pool fell from 88 % to 75 % across the set. S, the sum of drops and an upper bound, is 14 points. D, the net, is
13. A2.6's cap is 12. The halt fired when the reading crossed the dial (A6.7). The `spend 12pt` in the HALT line is the
last process's own count, from its START at 87 % (`run.log`, 2026-10-25T12:39:25Z) to 75 % (`run.log:450`,
`spent_across_set=12pt`), and that is the count A6.7's dial of 11 is measured against. S and D are the set's spend, which A6.7
says is reported "never one process's figure" (systems' N1 on #422). `score.out` lists all 19 pool readings.

## The record

`harness/s2lean/o90-2026-10-23/rowR-2026-10-28/` holds the scorer's inputs, copied from the reader's set directory
(`gemini.runs/o90-stage1-rowR`, on the reader's box):

| file | what it is |
|---|---|
| `reads.tsv` | 319 read rows (sha256/16 4cffadd5e14dd2be, as `score.out`'s inputs line prints) |
| `u2-options.tsv` · `draw.tsv` · `frozen-specrec.tsv` | the per-option rows, the draw, and the spec-recoverable key |
| `frozen/SHA256SUMS` · `frozen/u1/drawn.tsv` · `frozen/u2/items.tsv` | the frozen keys; the scorer refuses unless they match the registered hashes |
| `HALT` · `run.log` | the halt line, and the log that carries the pool readings |
| `out/read-*.FAIL-*.json` | the failed-attempt records (137), from which the scorer reads UNSCORED causes |
| `score.out` | the scorer's output (rc 4) |
| `SHA256SUMS.evidence` | sha256 of every file above |

The scorer was re-run on this copy and its output is byte-identical (`cmp`) to its output over the reader's own directory.
The reader's other files (prompts, rendered views, the harness's own `score.txt`) are not copied. On 10-28 the harness's own
`--score` (`run-rowR.py`) agreed with this scorer on every figure (bus @91,462,713). That is a second scorer over the same
input, not a second reader.

## Limits (they ride with the figures)

1. **One reader mechanism (Gemini), and it is not blind to the arm** (A2.7, A2.8 rider 2).
2. **U1 is at ceiling in both arms.** At this reader U1 cannot separate the arms, so NOT MET means "could not see a
   difference", not "no difference".
3. **The set is 4 U2 reads short** of the 323 drawn (seqs 320–323, two per arm). It is reported at n = 319 (A2.6).
4. **The set ran under two counting rules** (A6.6): A2.6 as fixed by A6.1 up to ADDENDUM 6's merge, and A6.4 after it. A6.4
   is a stopping rule chosen after the set began.
5. **Timeout missingness depends on the arm**: print-timeout UNSCORED reads are a0 19 · a5 13. That is why A6.8's bounds, not the
   observed figure, decide the theorem comparison.
6. **Stage 1 is INCOMPLETE** (A2.8 rider 1). This file reports row R only. If §10's registration later changes how a row-R
   figure may be cited, the change goes in a dated addendum and this file is not rewritten.
7. This RESULT makes no claim about the salt method's effect. It reports what the registered row-R reads scored.
