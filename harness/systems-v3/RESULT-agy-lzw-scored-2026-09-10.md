# RESULT — the nine landed Gemini cells, SCORED against the withheld suite
**bench · 2026-09-10 · zero model tokens: no model of any kind was called for this table**

⛔ **Every number comes from `RESULT-agy-lzw-scored-2026-09-10.tsv`**, which names the `agy-meter-*.json`
each row was read from. The verdicts come from `tasks/systems-v3/LZW/G/run_tests.sh`
(sha `7c6d2cea4289`) — **the runner the referee uses**, driven per cell against a COPY of each
submission. The archive was hash-checked before and after every run and is byte-unchanged.

## §1 · ⭐⭐ THE VERDICT — 8 OF 9, AND IT IS A FLOOR
```
  av01 PASS 8/8   av02 BUILD-FAIL 0/0   av03 PASS 8/8
  av04 PASS 8/8   av05 PASS 8/8         av06 PASS 8/8
  av07 PASS 8/8   av08 PASS 8/8         av09 PASS 8/8
  ---- VERIFIED 8/9 · SELF-CLAIMED 9/9 ----
```
⇒ **Gemini (declared `gemini-3.1-pro-high`, see §4) solves LZW greenfield in at least 8 of 9 cells**,
each passing the complete hidden suite, **while denied 50.7 % of its tool calls.**
⇒ 🔑 ***A CONFOUND WHOSE SIGN IS KNOWN IS A BOUND, NOT A VOID.*** The fence denies the subject actions
and reports the denial to it as success; that can only make the subject perform **worse** than an
unfenced one. **8/9 is therefore a FLOOR under the true number, not an estimate of it.**

## §2 · ⛔⛔ A LANDING IS THE SUBJECT GRADING ITSELF, AND ONCE IN NINE IT WAS WRONG
All nine cells ended `LANDED` with `false_done_claims: 0`. **`av02lzw` claimed R1–R8 all `DONE:
tests/driver.rs` and its `solution.rs` does not compile** — `error: literal out of range for u16`.
⇒ **`false_done_claims` only means the subject did not claim done while the LOOP disagreed. The loop
cannot compile anything**, so this class is invisible to it by construction.
⇒ 🔑 ***NINE LANDINGS WERE NOT NINE RESULTS, AND THE GAP WAS EXACTLY ONE CELL — WHICH NOTHING IN THE
RUN RECORD COULD HAVE TOLD US.*** The withheld suite was the only party that had not been asked, and
asking it cost nothing. **A self-graded landing rate is an upper bound on a verified one.**

## §3 · THE TOKEN FIGURES BESIDE THE COST, PER THE STANDING ORDER
```
  turns 71 · denied-as-SUCCESS 36 (50.7 %, every cell affected, 2–6 per cell)
  T 9,169,972 · vendor_total_tokens 1,540,179 · thinking 125,308
```
⛔ **`turns`, `T` and every token total here are INFLATED by turns that did nothing**, non-uniformly
(2–6 per cell). ⇒ **These are the cost of a partly-blocked subject and must not be pooled with a Claude
arm.** The verdict in §1 survives that; a cost comparison does not.
📌 systems has established the denials are the subject invoking `bin/bus` and `bin/rt` — **the interface
this campaign handed it** — against a settings file allowing `command(*)` but nothing `unsandboxed`.
⇒ **FENCE-OVERREACH, not subject-reach.** It is being fixed, and a clean re-run is the comparable number.

## §4 · ⛔ MODEL IDENTITY — DECLARED, NOT VERIFIED
The pin is `gemini-3.1-pro-high`, enforced by a launcher that refuses an unpinned launch, consistent
across 46 records. **Antigravity's transcript carries no model field**, so what the vendor served
cannot be read back. ⛔ The meter's `requested_model` and `served_models` hold **the same value**, and
two agreeing columns read as corroboration while being one number printed twice. **This result carries
the declaration, never a verification**, and the fields should collapse to one whose name says so.

## §5 · WHAT THIS DOES NOT SUPPORT
n = 9, **one task** (LZW), one substrate, one declared model, greenfield only. No cross-vendor claim is
made here: the Claude arm ran under a different tool-permission regime, and comparing them would
compare two experiments. **This is a standalone floor for one vendor on one task, and it is offered as
exactly that.**
