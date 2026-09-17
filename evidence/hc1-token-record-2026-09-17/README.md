# ⑯ — the HC stage 1 lane record in TOKENS, and the control that validates it

bench, 2026-09-17. Council ⑯: *"what we really want is the token cost, borken down if possible. Dollars are
secondary."* The PM declared this table a **VOID** in its schedule re-cut (*"TOKENS (VOID on this box)"*) and
refused to divide a dollar to get it. **That refusal was right, and this discharges it.**

| file | what it is |
|---|---|
| `drive.sh.txt` | the driver, fed to the run box on **stdin** so nothing was written there. Enumerates the population, **excludes two quarantine directories BY NAME**, and runs `scripts/cell_tokens.py` per cell. |
| `hc1-45-cells-tokens.txt` | the capture: 45 cells, role × model × five directions, `rc 0`, **0 refusals**. |
| `derive_lane.py` | produces **every figure** quoted from the capture's bytes, and **REFUSES (rc 1)** if the population is not 45 cells / 15 conditions or if any published median fails to re-derive. |

## The population, declared rather than globbed
**45 cells** = 5 problems × {placebo, plain, salt-diet} × n=3 — **43 LANDED + 2 CAP-COST**.
**2 directories are NOT cells** and are excluded by name, stated rather than silently skipped: a `FAILED-BUILD`
quarantine (no arm, no end marker) and a `NO-RUN` quarantine (staged, never ran).

## The positive control — and it is the point of the whole exercise
`RESULT-HC1-stage1-2026-09-16.md` §1 publishes fifteen USD medians and five premiums, computed independently
weeks earlier. **All fifteen medians and all five premiums re-derive from this token capture, to the published
cent and the published third decimal.** The lane's tokens and the lane's published dollars are the same cells.

## ⛔ The error the control caught, before anything was published
A first pass priced **every bucket at the Opus row** and over-stated **11 of 15 medians by 2–9 %, all in the
same direction.** **30 of the 45 cells carry SONNET subagent records inside an OPUS cell**, and Sonnet's row is
0.40× Opus's on every column.
⇒ ***A RATE APPLIED TO A TOKEN COUNT THAT IS NOT THAT MODEL'S*** — the same error the PM withdrew the same
afternoon on a different object, committed here by the seat that had just named it.
⇒ 🔑 ***THE SYSTEMATIC ONE-DIRECTIONAL DEVIATION IS WHAT EXPOSED IT. A SCATTER WOULD HAVE READ AS NOISE, AND
"CLOSE ENOUGH" WOULD HAVE SHIPPED.*** The control was built to validate the pipeline and it refuted it first.

## ⛔ And a defect it found in `cell_tokens.py`, merged an hour earlier
The reader **merged `cache_creation`** and dropped the meter's `(5m/1h)` split. Those are **two directions at
different rates** (6.25 vs 10.00 per M on the Opus row), so **a merged `cache_creation` cannot be priced** — the
first control could only produce a bracket. The split is now carried, with a self-test arm that moves tokens
**between** the TTLs without changing `T` and requires the report to change: **a merged column could not tell
those two cells apart.**

## What is new here, and what is not
⛔ **NOT new: that the salt-diet arm costs more.** That is published, per problem, with medians, bands and
verdicts, and this capture reproduces it exactly.
✅ **New: the record exists in the unit of record** — per cell, by role, by direction, by phase.
✅ **New and load-bearing: the premium's SIZE depends on the unit, and it is LARGER in tokens.**
Median premium **$1.818× vs T 2.168×**; on FreeList, the one problem HC1 registered as RESOLVED, **2.385× in
dollars and 3.440× in tokens.** The mechanism is arithmetic and measured: output is priced **50× cache_read**,
plain's output share of `T` is the higher one, so **plain is 26.9 % dearer per token** and the dollar ratio is
compressed. ✅ **And the output premium is only 1.324×** — the arm's cost is dominated by **re-reading context**,
not by producing more.
⚠️ **Every figure is a LOWER BOUND:** 2 salt-diet cells stopped at the USD cost cap and 10 cells carry an
interrupted turn, so the premiums **understate** the gap.
