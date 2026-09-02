# AMENDMENT 15 — **S2-RUST ON VeruSAGE-Bench**: THE ARM, THE GRADER, AND STAGE 0

**FROZEN 2026-09-01 21:5x PDT — THIS COMMIT IS THE AUTHORIZATION (F2).** Seat `bench`.
Registered under desk row **DD**, discharged by the helm on the bus 09/01 21:35:05, whose post names this
seat's gate in its own words: *"WHAT bench DOES NEXT (its gate): freeze the AMENDMENT from the commission,
then stage 0 per its §5."*

**Sources, in precedence order.** (1) the fleet's wave commission for S2-Rust (2026-09-01, in the private record)
(the wave commission; its **§11 binds the body where they disagree**). (2)
the fleet's arm-and-grader commission (2026-09-01, in the private record; the arm+grader design,
one refuter, two CONFIRMED-FATAL folded) — hereafter **DD**. (3) `S2-RUST-SCOUT-2026-09-02.md`,
`S2-SOURCE-READ-2026-08-29.md`. The S2-Lean harness at `15cfdc2` is the port's parent.

⛔ **NO S2-RUST MODEL CALL HAS BEEN MADE. THIS AMENDMENT SPENDS ZERO MODEL TOKENS AND SO DID EVERY
MEASUREMENT IN IT.** Stage 0 is by construction model-free; §9 names the one control that is not, and
sequences it out of stage 0 rather than smuggling it in.

⚖️ **HOW THIS AMENDMENT TREATS ITS OWN COMMISSION.** Amendment 11's rule carries: *every number is re-derived
at the artifact, and where the commission stated one I say whether my measurement reproduced it.* Eight
reproduced. **Six did not survive contact, two of them fatally** (§3, §4, §7). This is not a complaint about
the brief — the helm's §7 already names the habit that produced them, and the refuter that caught five more
was the helm's own. It is the reason the freeze happens **after** the object was reached, not before.

---

## §1 · THE QUESTION

Does the salt arm `a2` raise the rate at which a coding agent produces a **verifier-accepted proof** for a
**fixed specification and fixed executable code**, against the plain arm `a0`, with the placebo `a1`
controlling for prompt length? Read exactly as amendment 11 reads it: `b` = `a0`-only passes, `c` = `a2`-only
passes, separation on the drawn population, registered before the first call.

⛔ **THE REFEREE IS MACHINE-CHECKED, NOT KERNEL-CHECKED.** Verus emits no proof object and there is no
independent re-check. Wherever S2-Lean said "kernel" this protocol says "the referee accepted". The tombstoned
S2-Lean classes `KERNEL_REJECTED`, `AXIOMS_FAIL` and `PROVENANCE` have no successor of that kind: their work is
done by §6's three integrity layers, which are *text and AST* checks, and the protocol says so in those words.

## §2 · THE SUBSTRATE, MEASURED

Every line here was measured today at the object, on the seat, from a fresh clone.

| fact | commission | **measured** | verdict |
|---|---|---|---|
| `microsoft/verus-proof-synthesis` pin | `cbf9c0c6337b…` | `cbf9c0c6337b224fd8e5b7cb4e01ae65c0f98bc1` **= today's HEAD** | ✅ reproduces |
| `tasks.jsonl` size | 58,418,193 B | **58,418,193 B** | ✅ reproduces |
| `tasks.jsonl` sha256 | — | `d9b23ed7066ea6a7d782b98d3660f1fee514633b6a3e12b2801c3691f1cf689a` | new pin |
| records / `tasks/` files | 849 | **849 / 849** | ✅ reproduces |
| `NR` | NRKernel, 204 | **NRKernel, 204** | ✅ reproduces |
| `AC` | "Anvil Controller", 63 | **`Anvil-Advanced`, 63** | ⚠️ count right, **name wrong** |
| `AL` | Anvil, 104 | **`Anvil`, 104** | ✅ reproduces |
| `OS` | ATMO, 157 | **`ATMO`, 157** | ✅ reproduces |
| §11.1's NR misread trap | NR ≠ Node-Replication | **`NO` = `Node-Replication` = 29, distinct** | ✅ trap is real, resolution correct |
| population `AC ∪ NR` | 267 | **267** | ✅ reproduces |

⚠️ **`AC` is `Anvil-Advanced`, not "Anvil Controller".** The count 63 and the Table-6 row are right; the prose
name is not, and `AL`/`Anvil` (104) is a *different project* sitting one letter away. Recorded because §11.1
already had to correct one project-name misread on this benchmark, and this is a second of the same shape.

**Resolve from the jsonl, never the docs** — confirmed: `benchmark-stats.csv` still disagrees with the jsonl
(AL 106 vs 104, OS 160 vs 157, Σ 854 vs 849). The jsonl is the authority and its sha is pinned above.

**Contamination floor is unquantifiable and this amendment does not pretend otherwise**: all 849 solutions have
been public since Dec 2025 and the eight upstream projects are public repositories. No held-out set exists.

## §3 · THE POPULATION OF THIS WAVE — **207, NOT 267, AND NOT 163**

DD §3.1 restricts the wave to **proof-fn targets** and requires the refusals be *counted and published with the
draw*. Done, over all 267, by an item-level brace-matching parser applying **lynette's own target rule**
(`utils.rs` `fn_body_is_target`; `additions.rs:539–542`): the unique item named `target_function` whose body
does **not** contain `unimplemented!()`.

| class | n | share |
|---|---|---|
| **unique `proof fn` target, body EMPTY modulo whitespace** ⇒ **THE WAVE POPULATION** | **207** | 77.5 % |
| — of which the body is literally `{\n}` | 163 | |
| — of which the body is `{\n    }`, `{\n\n}` etc. (**whitespace only**) | **44** | |
| unique `proof fn` target whose stripped body carries CONTENT (placeholder / `// TODO`) | 17 | 6.4 % |
| target not present as a `proof fn` declaration (absent, `spec fn`, `broadcast proof fn`, name-prefix) | 24 | 9.0 % |
| target is an EXEC fn (`exec fn` or bare `fn`) ⇒ `EXEC_TARGET` | **15** | **5.6 %** |
| target ambiguous under lynette's rule (≥2 surviving candidates) ⇒ `TARGET_AMBIGUOUS` | 4 | 1.5 % |

**Two of DD's numbers do not survive this census, in opposite directions.**

1. ⛔ **DD §3.2's "assert the stripped body is exactly `{\n}`" throws away 44 tasks — 21 % of the recoverable
   population — over WHITESPACE.** The rule was priced on 20 sampled files in which every proof target
   happened to be `{\n}`; across all 267 the stripped body is also `{\n    }` (38), `{\n\n}` (3) and other
   pure-whitespace spellings (3). **REPAIR (registered): the shape predicate is `body.strip_braces().strip()
   == ""`** — empty modulo whitespace — and the *literal* spelling is recorded per task, not gated on.
   ⇒ 163 → **207**.
2. ⛔ **DD §3.1's "a quarter of the targets are EXEC fns" does not transfer**: 5/20 in the sample, **15/267 =
   5.6 %** on `AC ∪ NR`. The exec exclusion is far cheaper than the design feared. It is still taken (the
   two-region model cannot express ghost insertions inside an exec body) and still counted.

**A FIFTH REFUSE CLASS THE DESIGN DOES NOT HAVE.** DD §5 registers four (`EXEC_TARGET · TARGET_AMBIGUOUS ·
SHAPE · UNFAITHFUL`). The census turns up **24 records (9.0 %) whose `target_function` is not a `proof fn`
declaration in the task at all** — 12 in which the name does not occur even as a substring (e.g.
`AC__…__spec__invariant_is_stable`, whose target appears in neither the task nor the ground truth), and 12 in
which it occurs only as a `spec fn`, a `broadcast proof fn`, or a prefix of a longer name. This is **not**
ambiguity (0 candidates, not ≥2) and its cause is different, so it gets its own class: **`TARGET_ABSENT`**,
counted and published with the draw. A record that names a target the file does not contain is a defect in the
*benchmark's* record, and calling it "ambiguous" would have hidden that.

📌 **THE PRIOR DOES NOT TRANSFER TO THIS SUBPOPULATION, AND §7 SAYS SO.** §11.1's 65.2 % (AC 23/63 · NR
151/204) is measured over *all* tasks of AC∪NR, including the 60 this wave refuses. It is registered as a prior
from a different agent+tool regime **and now also from a different population**; the wave's plain-arm
expectation is §11's `bench §7(i)` prediction after the stage-0 controls, never this number.

## §4 · ⛔⛔ THE FATAL: DD §3.2's SECOND SELF-TEST CLAUSE REFUSES 85 % OF THE POPULATION

DD §3.2 requires, per drawn task, two round-trips, and refuses the task (`UNFAITHFUL`) if either fails:

> (a) `assemble(frozen, {})` minus the marker lines reproduces the original task text byte-for-byte;
> (b) `assemble(frozen, {proof: <ground_truth body>})` reproduces the `ground_truth` text byte-for-byte.

**Clause (b) fails on 176 of the 207 survivors. Only 31 round-trip.** Measured by splicing each task's
ground-truth target body into its own task skeleton at the exact byte span and comparing to `ground_truth`.

**The cause is not our scaffold. `ground_truth` is not `task` with the body filled in.** It is a
*separately assembled* single-file rendering of the same multi-file project, and it differs from `task`
**outside the target body**: whole context blocks are reordered and added. Specimen
`AC__vreplicaset_controller__proof__liveness__spec__invariant_is_stable` — task 4,316 lines, gt 4,322 lines,
and the *entire* diff is one 90-line block that sits at line 3849 in the ground truth and at the file's tail in
the task. Not one byte of the difference is in a proof body.

⇒ **APPLIED AS WRITTEN, THE DRAWABLE POPULATION IS 31 — below §2's ~80-paired-problem floor. The wave would
have died at its own faithfulness gate, and the gate would have blamed the benchmark.**

**REPAIR (registered, and the fork is stated in §7).** Clause (a) is **KEPT UNCHANGED and is the whole
scaffold test** — it is a statement about *our* assembler and it must be byte-exact. Clause (b) is
**REPLACED** by the semantic test that was already in the design one section later:

> (b′) `check_verus.py` on `{proof: <ground_truth body>, helpers: ""}` **PASSES the referee** — DD §4.6's
> ground-truth pass.

**Why (b′) is the right test and (b) never was.** (b) asserts a property of the *benchmark's file assembly*;
(b′) asserts the property we actually need — that a correct body, dropped into our scaffold, verifies. A
byte-comparison against a differently-ordered file tests nothing about us. ⇒ 🔑 ***A ROUND-TRIP TEST MUST
COMPARE AGAINST AN ARTIFACT OUR OWN CODE PRODUCED. COMPARING AGAINST SOMEONE ELSE'S ASSEMBLY OF THE SAME
CONTENT MEASURES THEIR BUILD, NOT OUR FIDELITY.***

⚠️ **AND THE CONFOUND (b′) INTRODUCES, CLOSED HERE RATHER THAN LATER.** (b′) makes `task_dead` and "our
scaffold is broken" the same observation. **The differential that separates them is cheap and is REGISTERED as
part of the ground-truth pass:** when a reference body fails inside our scaffold, the checker ALSO runs the
benchmark's own `ground_truth` file **as-is**. Reference file PASSES standalone but FAILS in our scaffold ⇒
`SCAFFOLD_DEFECT`, loud, blocking, posted. Fails **both** ways ⇒ genuinely `task_dead`. Two more `check.json`
fields: `gt_standalone_pass`, `gt_in_scaffold_pass`.

## §5 · THE TOOLCHAIN — ⛔ §3.5's CHOICE IS REFUTED BY ITS OWN 5 % RULE

§3.5 rules: *today's release binary … if `task_dead` under it exceeds 5 % of the draw, fall back to the
benchmark pin and re-run §3.3.* **Measured, and the rule fires by a factor of 6.6.**

**Ground-truth pass, seeded sample of 15 drawn from the 207 (seed 20260902), at
`release/0.2026.08.30.b432e82`, `--crate-type=lib --rlimit 250 --smt-option smt.random_seed=0`:**

> **PASS 10 / 15 = 67 %.** ⇒ apparent `task_dead` **33 %**.

⛔ **AND THE FIVE FAILURES ARE NOT DEAD PROOFS. THEY ARE RUSTC FRONT-END ERRORS**, in every case, with **no
`verification results::` line emitted at all**: `error: zero-sized fields in repr(transparent) cannot contain
external types with private fields` (5/5) and `error[E0308]: mismatched types` (3/5). These are
`COMPILE`-class, and they are a **toolchain incompatibility** between the benchmark's 2025 pin and an Aug-2026
release — *not* a property of the tasks.

⇒ 🔑 ***A FRONT-END ERROR ON A REFERENCE FILE INDICTS THE TOOLCHAIN, NEVER THE TASK.*** Had the ground-truth
pass folded `COMPILE` into `task_dead` — which is exactly what a "does the reference verify?" gate does by
default — the wave would have **pre-registered a third of its population as dead and blamed the benchmark for
our own pin.** `check_verus.py` therefore keeps `COMPILE` **separate from `VERIFY_FAIL` and separate from
`task_dead`**, and a non-zero `COMPILE` count on *reference* bodies is a **BLOCKING** condition, never a
`task_dead` entry.

**THE PIN, RE-DERIVED.** The commission calls the benchmark's pin `ddc66116…` "(Dec 2025)". **It is dated
2025-09-11** (`Signed division and modulus in bit-vector mode (#1887)`) — a third commission date corrected at
the object. The benchmark builds Verus from source at that commit (`README.md:130`, `Dockerfile:51-57`); there
is no released binary for the commit itself. **Measured**: `release/0.2025.09.12.bb1f342` is **1 commit ahead
of `ddc66116` and 0 behind** (GitHub compare: `status=ahead, ahead_by=1, behind_by=0`) and **ships an
arm64-macos zip**. ⇒ it is the benchmark's pinned Verus, in binary, for the Studio's architecture, with no
source build and no cargo anywhere in the pipeline.

**✅ REGISTERED CHOICE, AND IT IS MEASURED, NOT ARGUED: `verus-release = release/0.2025.09.12.bb1f342`**
(arm64-macos zip, 115,494,871 B, sha256 `95c5d5a5c52e348c334a0d74c6661bc035109dd0ba275a9a4c31eb4f07bc6933`).
**The same seeded 15, same `--rlimit 250 --smt-option smt.random_seed=0`, re-run under it:**

| binary | GT PASS | reference `COMPILE` |
|---|---|---|
| `release/0.2026.08.30.b432e82` (§3.5's choice) | **10 / 15 = 67 %** | **5** |
| `release/0.2025.09.12.bb1f342` (the benchmark's pin) | **15 / 15 = 100 %** | **0** |

⇒ **`task_dead` on this sample is ZERO. All five "dead" tasks were the pin, and nothing but the pin.** Every
one of the five now passes, three of them emitting 24, 40, 42 and 46 verified obligations where the newer
binary could not get past rustc. Today's release is retained as the **specimen** of the incompatibility, and
`no_cheating_pristine` and this table are the two standing receipts of §5 and §7.

⚠️ **AND A PROVISIONING FACT NEITHER COMMISSION HAS, FOUND BY RUNNING THE BINARY RATHER THAN UNPACKING IT:
a Verus release zip does not stand alone — it demands a matching `rustup` toolchain ON THE HOST**, and the two
releases demand *different* ones (`1.97.1` for 08.30, **`1.88.0` for the pin**; the pin binary exits 1 with
`required rust toolchain 1.88.0-aarch64-apple-darwin not found` until it is installed). ⇒ **`rust-channel` is
not a documentation pin, it is a Studio PREREQUISITE**: `1.88.0-aarch64-apple-darwin` must be installed on the
Studio and recorded in `HASHES.txt`, and `smoke_s2.sh`'s Verus analogue must REFUSE a root whose toolchain does
not match. Unpacking the zip proves nothing; the version banner is the gate.

✅ **§5(i) SETTLED — the arm64-macos zip bundles everything.** `libvstd.rlib`, `vstd.vir`, `vstd/`, **and
`z3` (Z3 4.16.0)**, plus `rust_verify`, the builtin rlib and the two macro dylibs. No `rustup`, no `cargo`, no
network at episode time. Pins: `verus-sha`, `z3-sha`, `vstd-sha` computed from the unpacked release.

🚧 **FIREWALL NOTE.** A Verus build already exists on this machine at `~/opt/verus-arm64-macos` (v0.2026.08.15,
built 08/14). **It was not used and will not be**: saltbench downloads its own release zip from the public
GitHub release and pins it by sha256, which is what the protocol requires anyway. Recorded so that no future
head "saves a download" by reaching for a binary whose provenance this seat has not established.

## §6 · THE GRADER `check_verus.py` — THREE INTEGRITY LAYERS AND THE REFEREE

Ported from DD §4 with the repairs below. Runs on the Studio, no model, under `sandbox-exec`, in its own
process group, with `check.py`'s discipline — **fresh `cwork`, and a PER-INVOCATION `pgrep` belt**
(amendment 14 repair 4: a sweep whose pattern names a shared file cleans up after everybody).

**ORDER:** `SCREEN → SCAFFOLD_DAMAGED → CHEAT_FAIL → STATEMENT_ALTERED → TIMEOUT | RLIMIT | COMPILE |
VERIFY_FAIL → PASS`; `HARNESS` anywhere the checker cannot run. **A screened or cheating body is never handed
to the referee.**

1. **SCREEN** — `screen.py` with DD §4.1's Verus set, verbatim, including its three anchored repairs: the bare
   substring `axiom` is **not** refused (`axiom_max_phyaddr_width_facts();` is a legitimate context call),
   `#![trigger …]` / `#![auto` are **allowed**, and `broadcast use <group>;` is **allowed** while a line-start
   `use` not preceded by `broadcast` is refused. `#[verifier::…]` allowed only for lynette's own `is_proof_attr`
   set (`rlimit`, `integer_ring`, `memoize`, `loop_isolation`, `spinoff_prover`). Helpers region: every item
   must be a `proof fn` / `pub proof fn` at top level.
2. **SCAFFOLD_DAMAGED** — `_present` on both marker pairs, at amendment 14's placement, a marker-pair fact and
   never a content fact. ⚠️ Amendment 14's law binds this layer by name: **it is measured on the file the AGENT
   wrote (`task.rs`), never on the assembled canonical.**
3. **THE COUNT GUARD** — the benchmark's own rule (`verusage/utils.py`
   `proof_completion_code_change_is_safe`), **ported by hand as four lines and never called through
   `utils.py`**, so that the module global `DEBUG_SAFE_CODE_CHANGE` (which returns True and skips checking) is
   **out of the path by construction**. Six counts, canonical vs original task text, any difference ⇒
   `CHEAT_FAIL`: `admit()`, `assume(`, `#[verifier::external_body]`, `#[verifier::admit]`, **plus
   `#[verifier(external_body)]` (the old spelling, present in the corpus) and `assume_specification`** — the
   upstream four-count guard misses both.
4. **THE AST COMPARE** — `lynette additions <original task.rs> <canonical.rs>`, which is what the benchmark's
   own evaluator runs. **Not `compare -t`**, which deghosts both files (deleting every `proof fn`) before
   comparing and is therefore structurally blind to an altered `requires`/`ensures` on a proof-fn target. rc
   handling **stricter than upstream**: `0` = clean · `1` **with** `Disallowed changes detected` on stdout =
   `STATEMENT_ALTERED` · **any other rc, or `1` without the string, = `HARNESS_ERROR`** — never `CHEAT_FAIL`,
   never a pass (upstream squashes them to False). Because §6 layer 0 froze the statements *by assembly*, an
   "altered" verdict on a file our assembler built is **also a finding about the assembler** and is posted as
   one.
5. **THE REFEREE** — `verus --crate-type=lib --rlimit <R> --smt-option smt.random_seed=<S> task.rs`, fenced,
   flag-for-flag identical to the in-episode `rt` invocation. `R`, `S` from `HASHES.txt`.
   **`PASS` iff exit 0 AND the results line PARSES as `verification results:: N verified, M errors` with
   `M = 0`, `N ≥ 1`, and no `(partial verification …)` suffix.** ✅ **Confirmed at the object today**: the line
   is emitted in exactly that form, `1 errors` is ungrammatical (parse, never substring-match), and on 16
   referee runs **exit 0 ⇔ `M = 0`** held without exception — §5(iii) settled, and the predicate stays
   conjunctive so the tie is not load-bearing. **`RLIMIT`** is its own class, keyed on
   `Resource limit (rlimit) exceeded`, **never folded into `VERIFY_FAIL`** where it would be charged to the
   arm. **`COMPILE`** likewise (see §5). Exit 0 with no results line ⇒ `HARNESS`.
6. ⛔ **`--no-cheating` IS RETIRED, AND THE RETIREMENT IS NOW MEASURED, NOT ARGUED — SEE §7.**

**`check.json` gains:** `verus_sha256`, `z3_sha256`, `vstd_sha256`, `lynette_sha256`, `rlimit`, `seed`,
`verified_count`, `error_count`, `results_line`, `rlimit_exceeded`, `compile_error`, `count_guard` (six
counts), `lynette_rc`, `lynette_tail`, `no_cheating_pristine` (non-gating diagnostic), `gt_standalone_pass`,
`gt_in_scaffold_pass`; `checker_sha256` extended.

## §7 · ⚖️ THE CONFLICT BETWEEN THE TWO BINDING DOCUMENTS, AND HOW THIS SEAT RESOLVED IT

The wave commission's §11 says, in two places, that `--no-cheating` is mandatory:
**§11.1 (ruling r.7)** — *"in-episode, every arm may invoke the pinned `verus --no-cheating --rlimit <R> …`"*;
**§11.2(a)** — *"the referee runs `--no-cheating` at both the in-episode and the check-time invocation."*
**DD §2.2 and §4.5 RETIRE it** on the refuter's reading of `vir/well_formed.rs`. And the commission's own
header says: **where DD and §11 disagree, §11 binds.** By the letter, `--no-cheating` is mandatory.

**⚖️ THE FORK, POSTED WITH A RECOMMENDATION AND PROCEEDED ON (§9 governance).**
**Arm A** — obey §11's letter: `--no-cheating` in both invocations.
**Arm B** — DD's retirement: three integrity layers + the referee, `--no-cheating` as a **non-gating
diagnostic** recorded in `check.json`.
**RECOMMENDATION AND THE ARM TAKEN: B**, because Arm A is **not a design choice this seat may make — it is
factually impossible, and it is now measured rather than reasoned:**

> Pristine benchmark file `NR__spec_t__os_invariant__lemma_map_insert_values_equality` (536 B, 1
> `external_body` context stub), **unmodified, no agent involved**, under
> `release/0.2026.08.30.b432e82`:
> **without `--no-cheating`** → 1 error (`postcondition not satisfied`).
> **with `--no-cheating`** → 2 errors, the extra one being
> **`error: external_body/assume_specification not allowed with --no-cheating`.**

The benchmark ships its context lemmas as `external_body` stubs (18 of 20 sampled; the guard's own baseline
count is 1–29 per file). `--no-cheating` refuses them. ⇒ **under Arm A every episode of every arm fails on the
scaffold the benchmark itself supplies, `task_dead` empties the population, and the flag keeps none of the
promise the prompt makes to the agent.** §11's binding clause governs *design* disagreements; here §11's
premise is refuted at the object by the thing it legislates about.

📌 **The measurement is kept as a permanent non-gating diagnostic (`no_cheating_pristine`) precisely so that
this resolution can be re-checked by anyone, at any time, from the record rather than from this paragraph.**

⚠️ **A SECOND, SMALLER §11 ITEM, NOT DROPPED SILENTLY.** §11.2(c) names `build.rs` and proc macros among the
residue screen keywords. **They are unreachable by construction** — the canonical is assembled from the two
regions only, so a `build.rs` the agent creates never reaches the referee. They are therefore **tombstoned
with that reason** rather than screened, and a fixture (§8.6-l) plants a `build.rs` in the episode tree and
asserts it does not appear in the canonical. The other three (`std::process`, `include_str!`,
`#[verifier::external]`) **are** in the screen set and are driven red.

## §8 · STAGE 0 — WHAT MUST BE TRUE BEFORE ONE SCORED EPISODE

Zero model tokens. Every gate driven **RED FIRST**. Nothing below is inherited; each line ends in a receipt.

1. **The view builder** `build_views_verus.py` — lynette's target rule, §3's repaired shape predicate, the
   **five** counted refuse classes (`EXEC_TARGET · TARGET_AMBIGUOUS · TARGET_ABSENT · SHAPE · UNFAITHFUL`),
   helpers region **at top level before the enclosing item** (a non-trait item inside a trait impl is rustc
   `E0407`), markers as `//` line comments. Self-test = §4 clause (a), byte-exact, on every drawn task.
2. **`extract_verus.py` · `assemble_verus.py`** — the S2-Lean regex with `//`,
   `WANT = {"P": ["proof","helpers"]}`, `_present` as today. ⛔ The assembler **never** emits
   `unimplemented!()` (lynette identifies the target by its absence).
3. **`check_verus.py`** — §6, with `controls_gate.py` re-pointed at the LIVE checker shas (amendment 12's law:
   a gate that reads a summary cannot tell a result from a memory of one).
4. **THE PIN GATE (§5) — ✅ PASSED ON THE SAMPLE TODAY (15/15, reference `COMPILE` = 0), STILL OWED OVER THE
   WHOLE DRAW.** Then the ground-truth pass across all 207, with the §4 (b′) differential and `task_dead.json`
   pre-registered in the `c_dead` shape. ⛔ Plus the toolchain prerequisite of §5: `1.88.0-aarch64-apple-darwin`
   installed on the Studio, pinned, and refused-on-mismatch by the smoke gate.
5. **THE RLIMIT CURVE** — `R ∈ {10, 50, 250}` on the drawn ground truths; publish the PASS count per `R`;
   **the pin is INDICTED if the curve is still climbing at 250.** Plus **one ×3 repeat at `R = 250` as the
   determinism control** (§11.3: expected 0 flips; nonzero indicts the *pin*, not the solver, and BLOCKS).
6. **THE FIXTURE KIT — 11 RED + 3 GREEN + 1, each verdict PREDICTED and REGISTERED BEFORE IT IS RUN**
   (DD §4.7 (a)–(k), the three green screen controls, plus **(l)** the `build.rs` unreachability fixture of
   §7). ⚠️ Amendment 14's law binds the kit: **a gate must fail on the broken version EVERY time —
   reproducing a defect is not gating it.**
7. **THE FENCE** — `sandbox_check.sb` widened by the narrowest rule admitting the pinned `z3` **as Verus's
   child only**, after confirming at the object that Verus execs nothing else; profile sha in every manifest;
   `hook-deny-network.sh` unchanged; `meter.py --neutral` re-pointed at the Verus install.
   ⛔ **Row CO ripens here** (this is the VeruSAGE stage-0 regime boundary the helm named): the Seatbelt
   `denyRead` fence names `~/bench` statically and does not cover the sibling state roots. **Row AV ripens
   here too**, as the helm ruled — **one amendment, one regime change.**
8. **GROUND TRUTH NEVER REACHES THE STUDIO** — the split happens on the seat; `task.rs` and `frozen.json`
   carry no `ground_truth`; `gt.json` stays here; the Studio sync excludes `tasks.jsonl` **and** the `tasks/`
   directory. Stated as an **arm**: a fixture planting a `ground_truth` key on the Studio must turn the fence
   RED.
9. **CONTROLS** — the S2-Lean stage-0 control protocol re-run on this substrate, green, before any scored
   episode.
10. ⛔ **A STUDIO FACT THIS PORT MUST NOT REDISCOVER THE HARD WAY:** `~/bench-aw/harness` and
    `~/bench-c/harness` are **symlinks to `~/bench/harness`** — there is exactly ONE harness on that machine.
    Every "local" edit to a run root's harness is a global one, in both directions.

**UNMEASURED, in the order stage 0 settles them:** ~~(i) `vstd`/`z3` in the release zip~~ **SETTLED §5** ·
(ii) Verus execs only z3 · ~~(iii) the results-line/exit-code tie~~ **SETTLED §6.5** · (iv) the rlimit curve
and the pin gate · (v) per-episode wall, tokens **and turns** at Opus — `MAX_TURNS 40` is UNMEASURED on this
substrate and **the population makes that pointed**: measured task sizes on `AC ∪ NR` are **min 180 B, median
32,979 B, mean 65,432 B, max 223,425 B**, and referee wall on 16 real runs spanned **0.2 s to 84.7 s** at
`rlimit 250`. Reading alone can exhaust a turn budget priced on CLEVER · (vi) whether any reference body uses
a `#[verifier::…]` attribute outside the allowed five (§6.1's own control).

## §9 · THE GATE, AND ONE SEQUENCING CORRECTION

The gate is §11.6's: **the fixed separation of 5 is REJECTED**; the threshold is derived from a **registered
null** — the rerun-variance prior (11.8 % of failures flip, arXiv:2512.18436v1 §5.7), re-derived at the drawn
`n` as `z·sd(b−c)` with **z = 2.5** registered. The **REGISTERED-POPULATION line** is printed by the
instrument, which **derives** the population rather than trusting this document's prose (amendment 12's law:
a denominator typed into an amendment is a claim; one computed by the tool is a measurement).

⚠️ **THE SEQUENCING CORRECTION, AND IT IS THIS SEAT'S, NOT THE COMMISSION'S.** §11.6 puts *"ONE a0-vs-a0 rerun
on a registered subset of the draw (≥30 tasks)"* **inside stage 0**, which §3 defines as **zero model tokens**.
An `a0`-vs-`a0` rerun is **60 scored episodes of model spend**. It cannot be in a model-free stage.

⇒ **REGISTERED: the null-measurement rerun is `STAGE 0.5`** — a separately budgeted, separately dispatched
run that happens **after** stage 0's receipts and **before** the first scored comparison, under §10's ceiling
with its own HALT stops and its own dry. Stage 0 stays model-free and its "complete" is honest.
🔑 ***A CONTROL THAT COSTS MODEL TOKENS CANNOT LIVE INSIDE A STAGE DEFINED AS MODEL-FREE — one of the two
labels is a lie, and it is always the cheap-sounding one.***

If the measured null makes the registered threshold unreachable at the affordable `n`, **the wave HOLDS at
that seam** (§10) and the debt is restated on the record.

## §10 · REGIME, BUDGET, PREDICTIONS

**Arms** `a0 / a1 / a2` at **`claude-opus-5`**. `a2` = `harness/arms/a2.md`, **byte-identical to S2-Lean**,
**1,913 B, sha256 `36ec05fc…` (HASHES.txt:26)** — the substrate-independence claim is tested by the identical
text, and the Verus disambiguation lives in `prompt_P.md`, never in `a2.md` (amending `a2.md` would move
`rendered-s2-a2`, under which S2-Lean's landed stage-B data sits: **spend comparability only when a run needs
it**). `a1` = `placebo.md` unchanged, length-matched re-verified at the rendered sha (F3-02/03). `base.md`
re-spelled for Verus — the only arm-side text that changes. **One rung `P`**, so no `--a-bodies`, no
`bc_gate`, no `PROVENANCE`.
`WALL_S 5400`; `TOKEN_CEILING 8000000` **non-binding** (amendment 8's law: the ceiling is now LIVE and every
`a0` row of U15 ran with it DEAD, so `R` and `WALL` stay the binders). **`MAX_TURNS` is UNMEASURED and is
priced by the stage-0 controls, not inherited** (§8(v)).
**The per-episode TOKEN STOP = 4 × the governing regime's p90, a HALT never a FAIL, DERIVED and printed by the
morning line** (amendment 14's registered rider) — **and this is the run that wires it into the driver, under
this run's own dry.**
**Budget:** the helm's ceiling for the wave's scored episodes is **60 M tokens** before a re-price on the
record; the $7.76 / 11.6 min per-task anchor is Sonnet 4.5 hands-off and **Opus in the fence is UNMEASURED**.
**Predictions to register before the first call** (§7 of the commission, three minimum): (i) the plain-arm
count band at the drawn `n`, from the stage-0 controls' metered distribution — **not** from the 65.2 % prior,
which §3 shows is over a different population; (ii) the `a2 − a0` direction and the separation reach;
(iii) the flip count under §8.5 (registered at **0**, then measured).

## §11 · NOT IN SCOPE

Exec-fn targets (a later wave, with lynette `additions` as its structural layer and a region model admitting
ghost insertions) · the 17 content-bodied and 24 `TARGET_ABSENT` records · stage A/B analogues · the no-lemma
track · Vericoding Verus · R6 · the organisation arms and every multi-agent surface (§11.8) · any change to
`a2.md`.

## §12 · WHAT THIS AMENDMENT CHANGED IN ITS OWN COMMISSION, IN ONE LIST

Reproduced: the repo pin (**= today's HEAD**), the jsonl size, 849/849, NR = NRKernel = 204, AC = 63,
AL = 104, OS = 157, AC∪NR = 267, §11.1's misread trap.
**Corrected at the object:** `AC` is `Anvil-Advanced`, not "Anvil Controller" · the benchmark's Verus pin is
dated **2025-09-11**, not December 2025 · exec targets are **5.6 %**, not a quarter · the `{\n}` shape literal
costs **44** tasks to whitespace · **`--no-cheating` fails the pristine file** (§7) · **today's release fails
5/15 reference proofs at the RUSTC FRONT END, and the benchmark's pin passes 15/15** (§5).
**Two things added the record did not have:** a Verus release needs a matching host `rustup` toolchain, and
the two candidate releases need different ones (§5) · `AC∪NR` task sizes and referee wall (§8(v)).
**Two fatals repaired:** the `UNFAITHFUL` clause (85 % refusal → the semantic test plus a scaffold/dead
differential, §4) and the toolchain pin (§5).
**Two things added the design did not have:** the `TARGET_ABSENT` class (§3) and `STAGE 0.5` (§9).

**LAWS THIS AMENDMENT ADDS.** A round-trip test must compare against an artifact our own code produced —
comparing against someone else's assembly of the same content measures their build, not our fidelity · a
front-end error on a reference file indicts the toolchain, never the task — and the cheapest way to tell a
dead task from a bad pin is to run the SAME sample under BOTH binaries · a control that costs model tokens
cannot live inside a stage defined as model-free · a shape assertion copied from a sample is a whitespace
literal until it is counted over the population · when a binding document's premise is refuted at the object,
the binding clause governs the design, not the fact — and the refutation is kept as a standing diagnostic so
the resolution can be re-checked from the record rather than from the prose.
