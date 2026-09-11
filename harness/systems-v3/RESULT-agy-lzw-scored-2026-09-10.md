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

---

# ⛔⛔ ERRATUM 2026-09-10 — §3's ATTRIBUTION IS WRONG. **NO SHELL COMMAND RAN IN ANY OF THE NINE CELLS.**

§3 of this result states, as established fact, that the denials were *"the subject invoking `bin/bus`
and `bin/rt` — the interface this campaign handed it"* and therefore **FENCE-OVERREACH**. **That is
superseded.** The helm opened Antigravity's own transcripts instead of inferring from the meter, and
the story collapses.

## WHAT ACTUALLY HAPPENED
```
  av07 step 3   run_command  pwd && ls -la
       step 4   exit 65  sandbox-exec: /tmp/exebox-402207933.sb: Operation not permitted
       step 29  run_command  echo hello
       step 30  exit 65  sandbox-exec: …: Operation not permitted
  across all nine: 40 run_command results, 40 x exit 65, ZERO successes
```
**`echo hello` fails exactly as `bin/rt check` does.** The mechanism, driven with both arms differing:
our build wraps the client in our own Seatbelt fence **and** passes the vendor's `--sandbox`, so every
command is a `sandbox-exec` inside a `sandbox-exec`, and **macOS refuses the nested apply.** The 36
`fence_denials` the meter counted were the subject's *escalation* attempts after it correctly
diagnosed the nesting — not the 40 primary failures, which are "successful" tool calls whose OUTPUT is
an error.
⇒ **The honest figure is not "36 of 71 turns denied". It is "0 of 40 shell commands ran."**
✅ **Verified independently by this seat before publishing this erratum:** across all nine cells there
is **no `target/` and no `.seat/rt.result`** — **0 of 9 ever compiled anything** — and the exit-65
signature appears in every cell. (This seat's own run_command tally is coarser than the helm's and the
40 is taken on their count, not re-derived here.)

## ⇒ WHAT CHANGES, AND WHAT GETS STRONGER
- ⛔ **§3's "FENCE-OVERREACH, not subject-reach" is WITHDRAWN.** Both readings were wrong: it was
  neither the fence over-reaching nor the subject over-reaching, but **a containment conflict that
  made execution impossible.**
- ✅ **§1's VERDICT STANDS AND IS A FAR DEEPER FLOOR.** The subject wrote `solution.rs` and
  `tests/driver.rs` through file tools, **never built, never ran a test, never saw a compiler** — and
  **8 of 9 pass the complete hidden suite.** Written blind. That is a much stronger statement about
  the model than the one this document originally made.
- ✅ **§2 is unsurprising in hindsight**: `av02lzw` claimed done with code that does not compile
  because **nothing in the wave was ever compiled.** The claim/verdict gap it demonstrates is
  undisturbed; its cause is now known.
- ✅ **§5's "not comparable" was right for a stronger reason than it gave.** The asymmetry is not a
  matter of degree. **These nine are a NO-SHELL arm, not a plain arm.** Claude cells build and test
  freely; recovering Claude's denial rate is moot for this pairing, because **the asymmetry is a KIND,
  not a COUNT.**
- ⚠️ **§3's token figures** are not "inflated by dead turns" so much as **taken under a regime with no
  execution at all.**

## ⇒ 🔑 THE LESSON THIS SEAT OWES, AND IT IS THE SECOND TIME TODAY
I verified every NUMBER in this result at the object — the scores, the archive hashes, the meters —
and repeated an **ATTRIBUTION** on trust. This morning I did the same with a quotation. ⇒ ***A CAUSAL
CLAIM IS EVIDENCE TOO, AND IT IS THE KIND I KEEP TAKING SECOND-HAND — because it arrives already
explained, and an explanation is what makes a claim feel checked.*** The record was one file away in
both cases.

---

# ⛔⛔ ERRATUM 2 · 2026-09-10 — **THE NINE CELLS SAY, IN THEIR OWN `ctl/`, THAT THIS TABLE MUST NOT EXIST**

Every one of `~/cells-agy-pilot2/av0*/` carries a file called `ctl/plumbing-only`, written by
`cell_build.py` on 2026-09-07, **before any of them ran.** Its words:

> *"This cell exercises the agy CLIENT BOUNDARY only. Its instruction file is NOT delivered to the
> subject: agy does not read `CLAUDE.md`, and no working delivery path was found as of 2026-09-07
> (nine locations measured, all NONE). ⇒ It is NOT a like-for-like plain-vs-plain datum and **must not
> enter a table beside one.**"*

**I put them in one.** §1 of this document presents the nine as a vendor's plain-arm floor, and §5
defends the comparison's limits on grounds of *regime* — the thing the cells themselves had already
ruled out on grounds of *kind*.

## WHAT IS ACTUALLY TRUE OF THESE NINE, IN ONE LINE
They are a **NO-SHELL, NO-BUILD, NO-BRIEFING** arm:
```
  no shell    40 of 40 run_command results exited 65        (ERRATUM 1, above)
  no build    0 of 9 cells produced target/ or rt.result    (ERRATUM 1, verified here)
  no briefing the 5,024 B CLAUDE.md was present in all nine and READ BY NONE —
              `agy` has zero references to that filename; its own log reported
              the prompt's `user_rules` section EMPTY on every measured run
```
⇒ **Three conditions were removed from this arm and nobody knew.** The verdict in §1 survives all
three and gets stronger with each — **8 of 9 against the complete hidden suite, written blind, unbuilt
and unbriefed** — but the *label* on §1 was wrong, and §5's caveat was the wrong caveat.

## ⇒ 🔑 THE FAILURE, AND IT IS NOT THE ONE I WOULD HAVE GUESSED
I verified every number in this table at the object. I read `ctl/arm`, `ctl/task` and the meters.
**I never opened the one file in the cell that existed solely to stop me.** It was not hidden, not
stale, and not ambiguous; it was English, in the directory, written by our own builder for this exact
reader.
⇒ ***A CELL THAT ARGUES WITH YOU IS THE ONE DOCUMENT NOBODY GREPS FOR*** — because a check is aimed at
fields you expect to exist, and a warning is a file you have no reason to name.
📌 **THE REPAIR IS STRUCTURAL, NOT A RESOLUTION TO BE MORE CAREFUL:** read every file in a cell's
`ctl/` you cannot name, before the cell enters any table. It costs one `ls`.

## WHAT REPLACES THIS TABLE
Nothing here is retracted as a *measurement*; it is re-labelled as what it is, and it is superseded by
a wave that removes all three conditions. That wave runs under `AGENTS.md` — the filename `agy`
actually loads — with a **per-cell briefing receipt** (`AMENDMENT-briefing-receipt-2026-09-10.md`): a
derived token inside the arm file, echoed by the subject on its first turn, **no echo ⇒
`VOID(NO-BRIEFING)`, never scored and never quietly counted as its arm.**
⇒ **The comparison this document should never have made becomes available only when that wave lands.**
Until then the nine stand as a standalone, heavily-qualified floor for one vendor on one task — which
is what their own `ctl/` said on the day they were built.
