# AMENDMENT 16 — THE VERUSAGE STAGE-0 REGIME BOUNDARY, AS ONE CHANGE

**Date:** 2026-09-02 · **Seat:** `bench` · **Authorization:** the helm's word on the bus, 09/01 23:12:39
(*"RELEASED NOW on OWED item 2 (the regime-boundary bundle as ONE change, AV + CO ripening in it)"*).
**Model tokens spent: ZERO.** Every number below is a run of the referee, the fence or a gate.

Rows **AV** and **CO** ripen here, as the helm ruled: **one regime change, not three.**

---

## §1 · WHAT THE BUNDLE CONTAINED, AND WHAT EACH ITEM TURNED OUT TO BE

| item | commissioned as | what it actually was |
|---|---|---|
| the z3 fence widening | widen `sandbox_check.sb` for z3 | **the referee was not fenced at all**, and the exec set is **four** binaries, not z3 |
| Studio provisioning | install verus + z3 + lynette + 1.88.0 | done by **transport from the seat**, verified by content, 22 s |
| a toolchain-mismatch smoke gate | refuse on mismatch | built; refuses the exact release amendment 15 rejected |
| merge `HASHES-S2RUST.txt` into `hashes.sh` | bookkeeping | **the two tables collide on `base.md` and `rt.template`** |
| row AV | state the `native_decide` rule | **17 of 29 refusal rules were unstated**, and the gap is arm-relevant |
| row CO | derive `denyRead` from `$BENCH` | done, with the paired arm the desk row asked for |

**Suite: 74 arms → 97 arms, 0 failed.** New gates: `selftest_fence_verus.py` (18) ·
`selftest_prompt_coverage.py` (5). New files: `sandbox_verus.sb` · `provision_studio.sh` ·
`smoke_toolchain_verus.sh`. Evidence: `evidence/amend16-regime-boundary-2026-09-02/`.

---

## §2 · THE FENCE — AND THE HEADER THAT WAS FALSE FROM THE DAY IT WAS WRITTEN

`check_verus.py`'s docstring has said, since it was created:

> *Runs on the Studio, no model, under sandbox-exec, in its OWN PROCESS GROUP, with a PER-INVOCATION belt.*

A grep of the file for `SANDBOX` / `sandbox-exec` / `killpg` / `belt` returned **nothing but that comment**.
The referee ran in a bare `subprocess.run`, unfenced, with no profile, no process-group kill and no belt.
Of the paragraph's three claims exactly one (`start_new_session=True`) was implemented. It was inherited
verbatim from `s2lean/check.py`, **where every clause of it is true.**

> 🔑 **A DOCSTRING COPIED FROM A FILE WHERE IT WAS TRUE IS AN ASSERTION ABOUT THE FILE IT CAME FROM.** It
> reads as a receipt, it survives review because it is accurate prose about a real design, and it describes
> another program. Nothing caught it because nothing ever **asked the running program** whether it was fenced.
> That question is now arm **A13**.

### 2.1 The exec set is FOUR binaries, and open question (ii) is answered NO

Amendment 15 §8 listed *"(ii) Verus execs only z3"* as unmeasured. **It is false.** `verus` is a shim that
resolves the pinned Rust toolchain by **running `rustup`**, which execs `rust_verify`, which execs `z3`.
Established by a ladder in which **each arm's own error names the next binary** — so every member is proven
NECESSARY, not merely listed:

```
allow {verus}                       -> error: failed to execute rust_verify (PermissionDenied)
allow {verus,rustup}                -> error: command failed: '.../rust_verify': Operation not permitted
allow {verus,rustup,rust_verify}    -> error: could not execute z3 process (Operation not permitted)
allow {verus,rustup,rust_verify,z3} -> verification results:: 1 verified, 0 errors
```

⛔ **`rustup` is the one member OUTSIDE the pinned release** — it lives on the user's PATH and is
user-writable — so it is now pinned by sha (`rustup-sha`) alongside the other three. *A binary admitted to a
fence must be pinned by the same instrument that pins the ones it stands next to.*

### 2.2 ⛔ THE COMPLETENESS CLAIM ALMOST WENT OUT ON ONE FIXTURE

My first green arm ran a **1.3 kB proof-only file**, and it passed the four-binary fence. That would have
been the receipt. It is worthless: a proof-only file **never reaches Verus's lifetime/borrow driver**, and
the existence of a fifth exec point (`lifetime rustc`) was revealed *by the RED arm's error text* — the
`(deny process-fork)` arm panicked at `rust_verify/src/lifetime.rs:333`, naming a binary the green arm had
never provoked.

> 🔑 **A WHITELIST IS COMPLETE ONLY OVER THE SHAPES IT WAS MEASURED ON**, and a green arm on one fixture
> measures the fixture. **The red arm reached further into the program than the green arm did.**

So completeness was re-established over a **population**: the **fence differential** — every reference file
run FENCED and UNFENCED, verdicts compared. Seeded sample (seed `20260902`) of **61** files from the
drawable population `AC ∪ NR`, plus the 4 rarest-shape records forced in: **61/61 agree, 0 differ.** A fifth
binary would have turned some fenced run into `COMPILE`.

📌 And the sample itself had to be re-taken: my first cut's stratifier matched **all 849** records, so it
silently measured 20 near-identical files from one module. *A stratifier that does not discriminate is a
`head -20`.*

### 2.3 The fence is WIDER than S2-Lean's, in exactly one respect, and it is forced

S2-Lean denies `process-fork` outright. **Verus cannot run under that rule** — it is a driver, not a
verifier (arm A5 measures this). So the fork is allowed and the entire weight rests on `process-exec*`.
Every leg is proven live by a **positive control** on the production profile text with **one declared
difference** (a shell admitted so a probe can reach legs Verus never touches): network denied · unlisted
exec denied · write outside the workdir denied *and no such file on disk afterwards* · credential trees
denied — **while a non-denied path stays readable**, so the leg bites without being blanket.

### 2.4 The gate is proven by mutation, deterministically

Five mutations, each turning exactly the right arm red, and the clean tree green ×3, the mutant red ×3:

| mutation | arm that went red |
|---|---|
| remove `(deny network*)` | A9 |
| remove `(deny file-write*)` | A7 |
| `fenced=False` by default | A13 |
| unset `$BENCH` falls back to `~/bench` | A11c |
| remove `(deny process-exec*)` | A1, A2, A3, A5, A10a |

⛔ **And the M2 run exposed a defect in my own gate.** A7's probe file survived onto disk, so A7 then stayed
red on a *clean* tree with the fence working. *An arm that leaves its own evidence on disk stops measuring
the fence and starts measuring its own history — a false red that outlives its cause is worse to debug than
a false green, because the tree it accuses is clean.* Fixed: removed before and after.

---

## §3 · ROW CO — THE FENCE DERIVES FROM `$BENCH`

`deny_read_paths()` appends the run's own state root, taken from `$BENCH`, to the static credential trees.
⛔ An **unset** `$BENCH` contributes **no root**, never a guessed `~/bench`: falling back would silently
reinstate the exact defect this repairs (arm A11c).

The desk row asked for *"a driven refusal arm (a GT file planted in a sibling root ⇒ RED)"*. It is arms
**A11d/A11e**, and they are a **pair**: a real `gt.json` planted in a real sibling root is **DENIED** when
`$BENCH` names that root, and the **same file is READABLE** when `$BENCH` names somewhere else — because a
fence that denied everything would pass the first arm alone.

⛔ **`settings.s2.json` (the AGENT fence) is deliberately UNTOUCHED.** It is pinned, asserted per episode,
and **201 landed episodes ran under it**; stage C's dispatch window is still open against the harness frozen
at `15cfdc2`. The S2-Rust regime gets its agent fence built derived-from-the-start when its episode driver
lands; the S2-Lean one moves at *its* regime boundary, after stage C. *Spend comparability only when a run
needs it.*

---

## §4 · ROW AV — WHAT THE CHECKER REFUSES, THE AGENT MUST HAVE BEEN TOLD

Measured before any repair: the screen enforces **29** refusal rules; the S2-Rust prompts named **12**.
**17 were unstated**, including `todo!` / `unimplemented!` and — the one that matters — **a new `use`
import**, since only `broadcast use` is allowed.

⛔⛔ **AND THE UNSTATED SURFACE IS ARM-RELEVANT.** The `use` rule bites in the **helpers region**, and `a2`
is the arm that **encourages helper lemmas**. This is amendment 15's FATAL 3 in different clothes: *an
instrument that penalises the treatment for applying the treatment manufactures the opposite effect.*

**The repair is a gate, not prose.** Prose fixes today and rots tomorrow — the next rule added to `RULES`
would be unstated again and nothing would notice. `screen_verus.PROMPT_COVERAGE` makes the prompt a
**consumer of the rule set**, and `selftest_prompt_coverage.py` refuses a rule with no entry (B1/B4) and an
entry whose phrase is absent from the prompt (B2/B5). Arm B2 immediately caught a real miss: my phrase
spanned a line wrap.

📌 The arm files (`arms/*.md`) are deliberately **excluded** from the prompt surface: a rule that only the
salt arm is told about is precisely the arm-correlated instrument this row exists to prevent.

⛔ **S2-Lean's `native_decide` line is NOT written here.** Row AV names `base.md`, `prompt_B.md` and
`a2.md` — S2-Lean files — and editing them now would change the regime under which stage C runs. It lands
at the S2-Lean boundary, after stage C. **`harness/s2lean/` is byte-untouched by this amendment.**

---

## §5 · THE HASHES MERGE — NOT THE BOOKKEEPING IT LOOKED LIKE

⛔⛔ **THE TWO TABLES SHARE KEYS WITH DIFFERENT VALUES.** Measured before merging:

| key | `HASHES.txt` | `HASHES-S2RUST.txt` |
|---|---|---|
| `base.md` | `9ada9241…` | `7e543ff6…` |
| `rt.template` | `c46e59af…` | `5db37bbe…` |
| `arms/a2.md` | `36ec05fc…` | `36ec05fc…` (identical by design) |

Every consumer resolves a key with `grep … | head -1`. A naive concatenation would have put **two `base.md`
lines** in the table and made one of them **silently authoritative** — the exact P2C2-01 defect
`sync_studio.sh`'s own comment warns about, re-created by the merge meant to be bookkeeping.

> 🔑 **TWO TABLES THAT WERE NEVER COMPARED CAN EACH BE CORRECT AND STILL COLLIDE — A MERGE IS A MEASUREMENT,
> NOT AN APPEND.**

**Repairs:** S2-Rust file keys are namespaced `s2rust/…` · the redundant `arms/a2.md` line is dropped (*a
duplicate whose two values agree today is a duplicate that stops agreeing silently*) · **`hashes.sh` now
REFUSES any table containing a duplicate key at all**, so this cannot recur · `hashes_s2rust.sh` becomes an
**emit-only** tool (*a retired artifact whose generator survives is not retired*) and remains the single
implementation, called by `hashes.sh` (*a checksum defined twice is two checksums*).

⛔ **My first cut of the duplicate gate was itself wrong.** It keyed on field 1, but the table carries two
line shapes — `<key> <value>` and `<kind> <subject> <value>` — which is exactly why `episode_s2.sh` has both
`pin2` and `pin3`. It reported `frozen`, `frozenA` and `prompt-canonical` as duplicates on a well-formed
table: **3 false positives out of 4 hits**, and it would have blocked every regeneration. *A uniqueness gate
must key on what the CONSUMER resolves on* — the same proxy-naming mistake, in miniature, as the family this
campaign keeps finding.

### 5.1 THE MERGE IS PROVEN ADDITIONS-ONLY

`HASHES.txt` regenerated and diffed against the committed table:
**changed or removed lines = 0 · added = 37.** Every pre-existing key is byte-identical, so **stage C's
per-episode assertions are untouched**. `views-set-sha256` reproduces `8c41b6d911ebeb36… count=207`.

📌 To regenerate at all, the three `leanproj-*` pin SOURCES had to come from the Studio (the CLEVER clone is
not on the seat). They were fetched and **verified to reproduce the committed pins exactly** before being
used — the fetch proves itself.

---

## §6 · THE STUDIO, PROVISIONED

By **transport from the seat**, not `curl | sh`: the wave's firewall line is *no binary of unestablished
provenance*, and a fresh network install would have put binaries nothing in this campaign has ever hashed
onto the machine that runs the episodes. The seat's copies are already pinned, so the Studio's toolchain is
a byte-identical copy of the one every stage-0 number was measured on.

```
OK verus / rust_verify / z3 / vstd / lynette / rustup   (sha256, both ends)
OK toolchain  01f12bacb2890fae (tree set-hash, 1.2 GB)
OK harness    no toolchain file under ~/bench/harness
smoke: verification results:: 1 verified, 0 errors        PROVISION OK  (22.6 s)
```

⛔ **Nothing was placed under `~/bench/harness`** — the ONE harness on that machine, which the state roots
reach by symlink and which is frozen at stage C's freeze commit. The toolchain lives in `~/verus-pin`, and
the script **asserts** the harness is clean afterwards rather than intending it.

📌 My first cut verified the 1.2 GB tree with `find -exec shasum {} \;` — one process per file, on both
ends. *A correct measurement that is too slow to run gets skipped, and a skipped gate is an absent one.*
Batched: many minutes → **22 s**.

---

## §7 · THE SMOKE GATE

`smoke_toolchain_verus.sh`, no model, run before the first episode. **T1** identity (every pinned binary;
an ABSENT pin is a FAILURE, never a skip) · **T2** the rust channel demanded AND installed · **T3**
capability · **T4** the profile sha · **T5** the referee's flags.

⭐ **T3 exists because identity is not capability.** Every sha can match while the toolchain cannot execute —
a missing channel, a half-copied tree. *A gate that checks only identity certifies a museum piece.*

**Driven red**, including against the actual specimen amendment 15 kept:

```
the REJECTED 0.2026.08.30 release -> DRIFT on verus/rust_verify/z3/vstd, and
   rust-channel  binary wants '1.97.1-…', pin says '1.88.0-…'
```

That is the toolchain that failed **5 of 15 reference proofs at the rustc front end**. **This gate would
have caught it before the first episode.** Also driven red on: a drifted z3 sha · a wrong channel · a
missing `verus-sha` pin · a drifted profile sha · missing rlimit/seed pins. Green on the seat **and on the
Studio**, against the merged table.

---

## §8 · WHAT THIS AMENDMENT DOES NOT DO

1. **`sync_studio.sh` has NOT been run.** It would overwrite the Studio harness that stage C is frozen
   against, and **the 09/02 window is still open**. The smoke gate was proven on the Studio from a scratch
   path (`~/s2rust-smoke`) instead. **This is the one item a future head must not mistake for done.**
2. **S2-Lean's `native_decide` line** (row AV's literal subject) and **`settings.s2.json`** (row CO's)
   remain untouched, for the same reason. Both land at the S2-Lean boundary, after stage C.
3. **No episode driver, no `settings.s2rust.json`.** Those belong to the arm design, not this bundle.
4. **Stage 0.5 is not started.** It is authorized *behind* this item; it is priced and posted before it runs.

---

## §9 · LAWS THIS AMENDMENT ADDS

- A docstring copied from a file where it was true is an assertion about the file it came from.
- A whitelist is complete only over the shapes it was measured on — and the red arm can reach further into
  the program than the green one does.
- A stratifier that does not discriminate is a `head -n`.
- An arm that leaves its own evidence on disk measures its own history, not its subject.
- Two tables that were never compared can each be correct and still collide: a merge is a measurement.
- A uniqueness gate must key on what the consumer resolves on.
- A retired artifact whose generator survives is not retired.
- Identity and capability are two claims; a toolchain gate must make both.
- A correct measurement that is too slow to run gets skipped, and a skipped gate is an absent one.
- A binary admitted to a fence must be pinned by the same instrument that pins the ones it stands next to.
