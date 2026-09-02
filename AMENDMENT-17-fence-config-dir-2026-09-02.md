# AMENDMENT 17 — THE AGENT FENCE MUST DENY THE CONFIG DIR IT RUNS ON

**2026-09-02, seat `bench`.** Rides under `AMENDMENT-16-regime-boundary-2026-09-02.md`.
Authorization: council 09/02 (`DT both arms at Sonnet`) and the helm's 09:00 word — *"the halt was RIGHT and
the repair is yours, REPAIR-THEN-RESUME"*, with six numbered requirements. This document is the registration;
`RESULT-DT-sonnet-probe-2026-09-02.md` will carry the read that follows it.

---

## §1 · THE DEFECT, AND HOW IT WAS FOUND

The row-DT Sonnet probe was launched at 15:32 UTC. Its **first episode** — `ep-c392a7ac`, draw rank 1,
`a0`, `claude-sonnet-5` — landed:

```
termination  VOID(ESCAPE:ROUNDS_EXHAUSTED)
void         true          void_reasons ["ESCAPE"]
escape_unblocked  ["Read file_path=$CFG/projects/<slug>/memory/MEMORY.md -> ..."]
escape_attempts_blocked ["Bash ls $CFG/projects/<slug>/memory/ && cat .../MEMORY.md"]
```

**The agent asked for one path two ways. The `Bash` form was BLOCKED by the PreToolUse hook; the `Read` form
was SERVED.** The reason is in `check_verus.py`:

```python
DENY_READ = ["~/.claude-bench", "~/.claude", "~/.ssh", ...]     # a STATIC list
def deny_read_paths(bench=None):
    paths = [expanduser(p) for p in DENY_READ]
    if root: paths.append(realpath(root))                        # $BENCH — DERIVED (row CO)
    return paths
```

Row CO derived the **state root** and left the **config dir** a literal. That literal is `~/.claude-bench` —
**S2-Lean's** config dir. S2-Rust episodes run on `~/.claude-bench-rust`, which is a **sibling**: the names
share a prefix, the paths do not nest. So the agent's own config directory — **the directory holding
`.credentials.json`** — was outside the filesystem fence for the entire S2-Rust wave.

### The laws this pays for

> 🔑 **A REPAIR THAT DERIVES ONE OF TWO PATHS LEAVES THE OTHER NAMED**, and the docstring explaining the
> derivation reads, to every later reviewer, as though everything is derived. I read that docstring the same
> morning and believed the fence was derived. It is half derived.

> 🔑 **SIBLING PATHS WHOSE NAMES SHARE A PREFIX ARE THE WORST CASE**: a `startswith` test answers *covered*
> where path containment answers *not covered*. ⛔ **My own first check made exactly that error** and printed
> `credentials path readable? False`. I caught it only because the episode's audit log contradicted my test.

> 🔑 **A SECOND LAYER THAT COVERS A SUBSET OF THE TOOLS CANNOT BE READ AS EVIDENCE THE FIRST LAYER HOLDS.**
> The PreToolUse hook matches `Bash|Monitor`. It will pass exactly the probes written in the language it
> matches, and the filesystem fence — the only layer that applies to every tool — must be complete on its own.

## §2 · SCOPE, STATED WITHOUT INFLATION

| | |
|---|---|
| **PROVEN** | the episode's config **directory** is readable by the `Read` tool; `.credentials.json` sits in it |
| **NOT MEASURED** | whether Claude Code independently special-cases the filename `.credentials.json`. The agent read `memory/MEMORY.md`, not the credential file. **A directory outside the fence is reported; a credential read is not claimed.** |
| **NO EXFILTRATION PATH** | `sandbox.network.allowedDomains: []`, `strictAllowlist: true`, `url_mentions = 0`. Defence in depth held at the second layer — an argument for calm, not for leaving it. |
| **NO CROSS-EPISODE LEAK** | the episode archives and RESETS `$CFG` to its keep-list after itself, so `memory/` cannot survive into the next episode. |
| **THE OPUS READ IS UNAFFECTED** | all 15 landed S2-Rust Opus episodes: `void=False`, `escape_unblocked=0` (one BLOCKED attempt). **`P0 = 9 of 10` STANDS**, measured, not assumed. |

⚠️ **BUT IT IS TIER-CORRELATED IN EFFECT, WHICH IS WHY IT BLOCKS THIS READ.** Fifteen Opus episodes, zero
unblocked escapes; the *first* Sonnet episode, one. If the lower tier is likelier to inspect its own config
dir, the Sonnet arm VOIDs more often — and a VOID is unscorable, so the defect eats the **lower tier's
denominator**. *Ask of every gate which arm is likelier to trip it; here, ask which tier.*

## §3 · THE REPAIR

1. **`deny_read_paths(bench, cfg)` derives TWO roots** — the state root from `$BENCH` and the agent config dir
   from `$CFG` — and the remaining literals are re-named `FOREIGN_CREDENTIAL_TREES`, **each with its reason
   written beside it**, so no literal can be misread as this run's own.
2. **`cfg` is an ARGUMENT, never an environment lookup** (unlike `bench`, which keeps its `$BENCH` fallback for
   existing callers). The harness renders this profile under its own environment while the agent is launched
   under `env -i`: a fence that reads its own scope from the ambient environment is *measured under one
   environment and runs under another*.
3. **`render_settings_verus.render()` REFUSES an unset cfg.** A default is how the config dir came to be
   another run's for a whole read.
4. **`episode_s2rust.sh` passes `--cfg "$CFG"`**, and its header now records the two-layer structure and the
   hook's `Bash|Monitor` coverage limit (helm requirement 4).

📌 **A DELIBERATE DIVERGENCE FROM THE HELM'S WORD, STATED SO IT CAN BE OVERRULED IN ONE WORD.** The instruction
was *"no literal config path remains in DENY_READ"*. Deleting `~/.claude-bench` outright would open a **new
hole in the same shape**: an S2-Rust agent could then read S2-Lean's credential tree. The defect was never that
a literal existed — it was that a literal was **mistaken for** the run's own config dir. The literals therefore
stay, under a name that cannot be misread, and arm **A14d** proves they are still denied.

## §4 · THE ARMS — RED FIRST, AND ONE OF THEM CAUGHT A DEFECT THE OTHERS MISSED

`selftest_fence_verus.py` **20 → 26 arms, 0 failed**; `selftest_settings_verus.py` 11, 0 failed.

| arm | what it holds |
|---|---|
| A14a | the credentials path IS covered by the rendered deny set — **by `Path.is_relative_to`, never `startswith`** |
| A14b | **RED**: without cfg it is NOT covered — proves A14a is not vacuous |
| A14c | **the string test lies**: `startswith` says covered where path containment says not — the incident kept as a permanent arm |
| A14d | the foreign trees are still denied — the repair did not trade one hole for another |
| A14e | the renderer **REFUSES** an unset cfg |
| A14f | the rendered agent fence carries it |
| A14g | **the CLI argv, as the episode calls it** |
| A14h | the CLI REFUSES without `--cfg` |

**Driven against the shipped code** (`git show HEAD:`): A14a, A14e and A14f **all FAIL** on the pre-repair
files. Red-first satisfied.

⛔ **AND A14g EXISTS BECAUSE A14a–f WERE ALL GREEN WHILE THE PRODUCTION PATH WAS BROKEN.** Those six call
`render()` directly. `main()` had no `--cfg` option at all, so the episode's own invocation would have REFUSED
on every task — six green arms over a program the caller never runs.
> 🔑 **A SELF-TEST THAT NEVER MAKES THE CALL ITS CALLER MAKES IS A SELF-TEST OF A DIFFERENT PROGRAM** —
> banked 08/30, re-earned today inside the arms written to prove a fence.

## §5 · A THIRD DEFECT, FOUND BY THE RE-PINNING

Regenerating `HASHES.txt` **silently dropped `views-set-sha256`**. That pin is emitted behind
`if [ -n "${VIEWS_DIR:-}" ]` — the one conditional line in a generator whose own header says it *"FAILS LOUD
if one is missing: a HASHES file that silently omits a pin is worse than none."* `episode_s2rust.sh:133`
REFUSES on an empty `want_vs`, so it **fails closed** — no result could be wrong; it would simply have killed
the next paid-for run at its first episode.

> 🔑 **THE ONE CONDITIONAL LINE IN A FAIL-LOUD GENERATOR IS THE LINE THAT WILL GO MISSING.**

**Repaired:** `VIEWS_DIR` is now `:?`-required and fails loud (driven: `rc=1` with the message naming the
remedy). The views are a pure function of two pinned inputs, so a rebuild is always available: measured at
**3.0 s**, and the seat rebuild reproduces the Studio's live set-hash **byte-identically**
(`8c41b6d911ebeb36… count=207`) — *the reproduction is the check that the pin is honest.*

## §6 · WHAT MOVED, AND WHAT DID NOT

Six files re-pinned: `check_verus.py` · `episode_s2rust.sh` · `hashes_s2rust.sh` · `render_settings_verus.py` ·
`selftest_fence_verus.py` · `selftest_settings_verus.py` (plus `selftest_dry_s2rust.sh`, which the fenced-set
check caught unpinned on its first run — **the fence working on its author**).

✅ **`s2lean/*`, `rendered-s2-*`, `leanproj-*` and `clever-commit` rows are BYTE-IDENTICAL**, verified by diff:
**stage C's frozen table is undisturbed** and the three `leanproj-*` pins reproduced.

## §7 · MY OWN ERROR, WHICH IS WHY I HALTED AND WAS NOT WHY THE HALT WAS RIGHT

I read `calls = 80` against `max_turns = 40` and concluded the turn cap had failed for Sonnet. **It had not.**
Both tiers' `result.json` reads `subtype = error_max_turns`, `num_turns = 41`: the CLI enforced exactly 40
turns for both. `calls` in our manifest is **distinct `message.id`**, and at the same 40 turns Opus produced
40 and Sonnet 80.

> 🔑 **A CAP IN TURNS DOES NOT CAP API CALLS, AND THE CALLS-PER-TURN RATIO IS TIER-DEPENDENT.**

⛔ This seat banked *"a statistic is only a cap's price if it is in the cap's unit"* on **09/02 at 03:45**,
after a predecessor read "turn 70" off an episode capped at 40. **I read the brief carrying that law at 08:30
and made the same error, in the opposite direction, at 15:50.**
> 🔑 **A LAW YOU HAVE READ IS NOT A LAW YOU HAVE INSTALLED.**

**The halt was still right, for the VOID**: episode 1 is unscorable, the cause recurs by construction, and a
probe that VOIDs is not a cheaper probe — it is no probe.

### The one number the episode bought

First paired Sonnet/Opus observation on the same task under a cap that provably bound both at 40 turns:

| | turns | API calls | metered | wall | `rt_calls` |
|---|---|---|---|---|---|
| opus `ep-34aa0535` | 40 | 40 | 3,255,428 | 910 s | 6 |
| sonnet `ep-c392a7ac` | 40 | **80** | **9,367,589** | 1291 s | 1 |

**2.88× the tokens and 2.0× the API calls for the same turn budget.** ⇒ **P2′ (1.0–1.5×) is REFUTED and the
original registered P2 (≈4×, band 2–6×) was the better prediction.** I corrected a right answer into a wrong
one and published the correction with confidence; the escape clause I registered for P2′ is exactly what
happened, by a mechanism I had named as unlikely. **n=1 and VOID, so it prices nothing yet.**

## §8 · WHAT THE PROBE DOES NEXT (helm requirement 5)

`ep-c392a7ac` **stands in the record as VOID — unscorable, the detector's verdict, not a re-score.** The probe
RESUMES at **n = 3**, with a **fresh episode for draw rank 1**: replacing a VOID is not selection. The three
ids, the draw order, the registration and the gates G1/G2 are **unchanged**; only the instrument moved.
