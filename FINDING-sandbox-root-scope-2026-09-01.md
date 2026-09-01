# FINDING — THE SEATBELT `denyRead` FENCE NAMES `~/bench` STATICALLY AND DOES NOT COVER THE SIBLING STATE ROOTS

**Found 2026-09-01 22:3x while building `~/bench-aw` for amendment 13, BEFORE its stage B.**
**Nothing is applied. Nothing landed is invalidated. Routed to the desk.**

## THE FACT

`harness/settings.s2.json` — the agent's fence, pinned and verified per episode against
`settings_sha256` — declares:

    "filesystem": { "denyRead": [ "~/bench", "~/bench-dry", "~/.claude-bench", "~/.claude", … ] }

That list is **STATIC and names `~/bench`**. Since 08/31 this campaign has deliberately run each new regime in
its **own state root** — `~/bench-a8` (the Opus `a0`/`a2` comparison), `~/bench-c` (amendment 11 stage C),
`~/bench-aw` (amendment 13) — and **`/Users/jyh/bench-a8` is a SIBLING of `/Users/jyh/bench`, not a child of
it.** A subpath deny on `~/bench` does not reach it.

⇒ **THE LAW "A NEW REGIME GETS A NEW STATE ROOT" WAS ADOPTED WITHOUT THE FENCE FOLLOWING IT.** The
state-root split solved a real problem (nothing skipped, no prior artifact touched) and silently moved the
episodes' `state/` — landed `bodies.json`, `canonical.lean` — **outside the path the fence names.**

📌 **Why the GT was nevertheless protected in every landed run:** `~/bench-a8/s2views` and
`~/bench-c/s2views` are **SYMLINKS to `~/bench/s2views`**, so a read through them resolves INTO the denied
subpath. The ground truth was safe **by an accident of how the roots were built**, not by the fence naming it.
⛔ `~/bench-aw/s2views` is a **REAL DIRECTORY** (it had to be — stage A needs a GT-free tree and `ship A`
hangs), so that accident does not hold there.

## WHAT ACTUALLY DEFENDED, MEASURED RATHER THAN ASSUMED

The fence is not the only layer, and the other layer **does** cover the sibling roots — by a detail worth
naming: `hook-deny-network.sh`'s escape pattern contains

    /Users/[^ ]*/(bench|\.claude)([^A-Za-z0-9_]|$)

and `-` is inside `[^A-Za-z0-9_]`, so **`bench-a8`, `bench-c` and `bench-aw` all MATCH.** The hook is
`PreToolUse` on `Bash|Monitor` and **blocks**, it does not merely log.

**MEASURED OVER EVERY EPISODE OF BOTH RUNS:**

| run | episodes | `escape_attempts_blocked` | `url_mentions` |
|---|---|---|---|
| `~/bench-c` (stage C, a0, Opus) | 12 | **0 in all 12** | 0 |
| `~/bench-a8` (a0+a2, Opus, A+B) | 60 | **0 in 57, 1 in each of 3 — all BLOCKED** | 0 |

⇒ **No agent ever reached another root, and the three that pattern-matched were stopped.** The landed record
is not in question.

## WHY THIS IS NOT FIXED TODAY, AND THAT IS A DECISION RATHER THAN AN OVERSIGHT

`settings.s2.json` is **PINNED** (`HASHES.txt`) and its sha is asserted **per episode**
(`episode_s2.sh:57`, refusing on drift) and **recorded in every manifest**. Editing it changes the fence
under which **201 landed episodes** ran, for a run whose comparison arm (`~/bench-a8`) ran under the old one.
⇒ ***spend comparability only when a run needs it*** — this run does not need it, and amendment 13's whole
purpose is a comparison against a8.

**AND THE NARROWER REASON IT IS SAFE TO PROCEED WITH AW's STAGE B:** `frozen.json` is the only GT-class file
being added to the non-denied tree, and at **stage B its entire content is already in the agent's task file
by design** — `problem_spec` and `isomorphism_theorem` ARE the stage-B task (prove your generated spec
isomorphic to the human one), and `shipped_generated_spec_body` is the agent's own stage-A output.
**`C.lean` is deliberately NOT added** (only stage C requires it), so AW's stage B root is **strictly more
GT-free than a8's stage B root was**, not less.

## THE REPAIR, PRICED AND ROUTED

Make the deny **derive from `$BENCH`** instead of naming one path — i.e. render `settings.s2.json` per run
the way `check.py` already renders its sandbox profile (`render_profile`, `__WRITE_PATHS__`/`__DENY_READ__`
substitution), so the fence follows the root by construction. That is a **freeze-level change to the pinned
agent fence** and therefore its own dated amendment, with the pin regenerated and a driven refusal arm.
**Until it lands, the operating rule: a new state root is covered by the HOOK, not by the Seatbelt fence —
so never place ground truth in a sibling root except behind a symlink into `~/bench`.**

⇒ **THE LAW: A FENCE THAT NAMES A PATH INSTEAD OF DERIVING ONE STOPS PROTECTING THE DAY THE WORK MOVES —
and the move that broke it was a repair, adopted for good reasons, whose blast radius nobody re-measured.**
This is the fifth member of the family this seat has now found in five days (`ship BC` on a DONE line ·
`c_dead` on elaboration · the controls gate on a boolean · the F3 headline at a stage-C root · this) and its
shape is constant: **an instrument that names a proxy keeps answering after the thing it stood for moved.**
