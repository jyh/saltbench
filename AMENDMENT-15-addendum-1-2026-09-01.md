# AMENDMENT 15 — ADDENDUM 1: WHAT DRIVING THE CODE FOUND THAT READING THE DESIGN DID NOT

**2026-09-01 22:1x PDT, seat `bench`. Appended to `AMENDMENT-15-s2rust-2026-09-01.md` (frozen `e09e6a1`),
never edited into it.** Zero model tokens. Stage 0's code was written from the frozen protocol and then
DRIVEN; this addendum is what the driving returned. **Three repairs, one of them a third fatal — and it is
the most dangerous defect found on this substrate, because it is ARM-CORRELATED.**

---

## §A1 · ⛔⛔ FATAL 3 — THE HELPERS REGION, AS PLACED, IS REFUSED BY LAYER 4 AS *CHEATING*

**The design's placement** (DD §3.2, carried into amendment 15 §8.1): the helpers region sits *at top level,
immediately before the item that encloses the target* — never inside the `impl`, because a non-trait item in a
trait impl is rustc `E0407`.

**Measured**: with any helper present, `lynette additions` returns rc 1 and
`Disallowed changes made to Verus macros in the original files.` ⇒ `check_verus.py` classifies the episode
**`STATEMENT_ALTERED`** — a **cheating** class — **for doing exactly what `prompt_P.md` invites**
(*"You may add helper `proof fn` lemmas inside the `helpers` section"*).

**The cause, read at lynette's source rather than inferred.** `check_items` (`additions.rs:340-532`) walks the
original and changed item lists **in lockstep**. An added `proof fn` is tolerated in exactly one place — the
`(Item::Fn, Item::Fn)` arm at `:420-436`, which advances only `idx_changed`. A helper placed immediately
before the enclosing `impl` is compared against an `Item::Impl`, falls through every typed arm to the
catch-all `(_, _)` at `:517`, and returns `false`. **47 of our 207 views (23 %) are impl-enclosed.**

⇒ 📌 **DD §4.4's "§4.4's UNMEASURED (iv) is SETTLED: helpers are accepted; no blanking contingency" is TRUE
OF THE FUNCTION AND FALSE OF THE PLACEMENT.** The refuter read `additions.rs:421-432` correctly — added proof
fns *are* accepted — and the design then placed them at the one offset where that arm never fires. Two
correct readings of two files, and the defect lives in the space between them.

⚠️ **WHY THIS ONE MATTERS MORE THAN ITS SIZE.** The salt arm `a2`'s practices explicitly encourage writing and
reusing helper lemmas. Under the shipped design, **the more an arm followed the salt method, the more often it
would be scored as having ALTERED THE STATEMENT.** The instrument would have manufactured a negative salt
effect and reported it as cheating. ⇒ 🔑 ***AN INSTRUMENT THAT PENALISES THE TREATMENT FOR APPLYING THE
TREATMENT DOES NOT MEASURE A SMALL EFFECT BADLY — IT MANUFACTURES THE OPPOSITE ONE. Ask of every gate: which
arm is more likely to trip it, and why?***

**THE REPAIR: the helpers region moves to the END of the `verus!` block, after every original item.** The same
loop that refuses the old placement makes this one safe: it is
`while idx_orig < original_items.len() && idx_changed < changed_items.len()`, so items appended past the end of
the original list are never examined, and the closing `return idx_orig == original_items.len()` holds. The
placement satisfies **both** constraints at once — outside every `impl` (no `E0407`) and past the lockstep
window (accepted). Rust item order does not affect name resolution, so a target may call a helper declared
after it.

**RED-FIRST, AND DETERMINISTIC — the amendment-14 standard (*a gate must fail on the broken version EVERY
time*):**

> helpers placement **BROKEN** → lynette `['REFUSED', 'REFUSED', 'REFUSED']`
> helpers placement **FIXED** → lynette `['accepted', 'accepted', 'accepted']`

**AND ITS PERMANENT GATE**, without which the repair would rot silently: fixture arm
**`clean body PLUS a valid helper` → `PASS`**. Before the repair that arm returned `STATEMENT_ALTERED`.

## §A2 · THE COST THE REPAIR CREATED, PAID IN THE SAME BREATH — `HELPERS_SHAPE`

Appending past the end of the original list means **lynette never examines the helpers region at all.** A new
`axiom fn` there — which `additions.rs` would otherwise refuse as `FnMode::ProofAxiom` — became invisible to
layer 4. Found because the fixture kit's registered prediction for *"new axiom fn, screen disabled"* was
`STATEMENT_ALTERED` and the run returned `VERIFY_FAIL` with `lynette_rc = 0`. **The prediction was right and
the world had changed under it; a kit without that arm would have reported the hole as a pass.**

⇒ **NEW STRUCTURAL LAYER `HELPERS_SHAPE`, between `SCAFFOLD_DAMAGED` and `CHEAT_FAIL`** — a **WHITELIST**:
every top-level item in the helpers region must be a `proof fn` / `pub proof fn` (attributes and doc comments
allowed before it). ⛔ **`--no-screen` does NOT disable it**: `--no-screen` exists to record token screening
for controls, while this is structural integrity for a region no other layer can see.
📌 It also repairs a silent weakening of my own: the design specified this check as a whitelist and my first
implementation made it a **blacklist** of named bad shapes. It passed every red arm I had written, because I
had written arms only for the shapes I had named. ⇒ 🔑 ***A BLACKLIST PASSES EXACTLY THE TESTS YOU THOUGHT TO
WRITE. THAT IS WHAT MAKES IT LOOK LIKE A WHITELIST.***

**REVISED ORDER:** `SCREEN → SCAFFOLD_DAMAGED → HELPERS_SHAPE → CHEAT_FAIL → STATEMENT_ALTERED →
TIMEOUT | RLIMIT | COMPILE | VERIFY_FAIL → PASS`.

## §A3 · §4'S DIFFERENTIAL IS A **THREE**-WAY, AND THE THIRD LEG IS WHAT EXONERATES US

§4 registered a two-way differential (reference file standalone vs. in our scaffold). Its first real run —
the seeded 15 — returned **12/15 in our scaffold against 15/15 standalone**, which the two-way reads as
**`SCAFFOLD_DEFECT`: ours, blocking**. It is not ours. The three failures are
`E0412 cannot find type RLbl`, `E0425 cannot find function is_in_mapped_region`, and
`cannot find macro assert_by_contradiction` — **missing definitions**, the same class as §4's finding that the
`ground_truth` carries context blocks the `task` does not.

**THE CONTROL THAT SETTLES IT, run rather than reasoned:** splice the reference body **straight into the
benchmark's own `task` file** — no markers, no scaffold, no reordering — and compare.

| task | direct splice | our scaffold | verdict |
|---|---|---|---|
| `NR__…__lemma_concurrent_trs_induct` | rc 1, `E0412 RLbl` | rc 1, `E0412 RLbl` | identical ⇒ exonerated |
| `NR__…__step_MemOp_refines` | rc 1, `E0425 is_in_mapped_region` | rc 1, same | identical ⇒ exonerated |
| `NR__…__next_step_preserves_inv_sbuf_facts` | rc 1, `cannot find macro` | rc 1, same | identical ⇒ exonerated |

⇒ **NEW CLASS `TASK_CONTEXT_INCOMPLETE`**: the record's `task` omits context its own `ground_truth` supplies,
so the task is **unsolvable by any agent** and is removed from the draw and pre-registered. On the seeded 15
it is **3/15**; the rate over all 207 is the full pass's to report.

**THE REGISTERED DECISION TABLE** (`gt_pass_verus.py`, three referee runs at most, the third only on failure):

| standalone | splice | scaffold | verdict |
|---|---|---|---|
| PASS | — | PASS | **LIVE** — drawable |
| PASS | FAIL | FAIL | **TASK_CONTEXT_INCOMPLETE** — the benchmark's record; removed, counted |
| PASS | PASS | FAIL | **SCAFFOLD_DEFECT** — ours. LOUD, BLOCKING |
| FAIL (`COMPILE`) | — | — | **PIN_DEFECT** — the toolchain (§5), BLOCKING |
| FAIL (other) | — | — | **TASK_DEAD** |

⇒ 🔑 ***A TWO-WAY DIFFERENTIAL ASSIGNS BLAME BETWEEN THE ONLY TWO CANDIDATES IT WAS GIVEN. Before trusting one
that indicts you — or that acquits you — ask whether a third party was ever on the list.*** Had I trusted the
two-way, I would have spent the next hours hunting a defect in an assembler that produces byte-identical
output to the benchmark's own file.

## §A4 · THE SCREEN'S OWN CONTROL FOUND A THIRD LEGITIMATE TRIGGER FORM

The registered control (§6.1: *a reference body the screen refuses is a SCREEN DEFECT, not a dead task*) run
over all **207 reference bodies** refused **2**, both on `#![all_triggers]` — a trigger form in neither
commission. **Widened by the NAMED token after censusing every inner attribute in the corpus**, rather than by
patching the two failures: across all of AC ∪ NR there are exactly three forms — `#![auto` (989 task / 63
reference), `#![trigger` (574 / 11), `#![all_triggers` (13 / 2). **The widening is therefore complete by
measurement, not by iteration**, and a red arm (`#![allow(dead_code)]` still refused) keeps it narrow.
**Control re-run: 0 screen defects over 207.**

## §A5 · RECEIPTS, EACH DRIVEN

- `build_views_verus.py` over `AC ∪ NR`: **built 207** · refused `TARGET_ABSENT` 24 · `SHAPE` 17 ·
  `EXEC_TARGET` 15 · `TARGET_AMBIGUOUS` 4 (**207 + 60 = 267** ✓), **`UNFAITHFUL` 0 · `PARSE` 0**, and the
  counts **independently reproduce** the §3 census written by a separately-authored parser.
- `screen_verus.py --selftest`: **29 arms, 0 failed** (14 red · 15 green — including a token inside a comment
  and inside a string, which must NOT trip it).
- `selftest_check_verus.py`: **19 arms, 0 failed** — 13 red, 5 green, 1 structural (an edit outside the two
  regions is absent from the canonical: statement immutability by assembly, driven not asserted).
- `helpers_shape` unit arms: 8, 0 failed.
- The grader end to end on a real task: reference body ⇒ `PASS` (`lynette_rc 0`,
  `10 verified, 0 errors`); empty body ⇒ `VERIFY_FAIL` (`9 verified, 1 errors`). **Both arms differ.**
- `lynette` built on the SEAT from the pinned repo (release profile) — no cargo on the Studio, sha to be
  pinned in `HASHES.txt` with the Verus and z3 shas.

## §A6 · STILL OWED BEFORE ONE SCORED EPISODE

The full three-way ground-truth pass over all 207 (running; it produces `task_dead.json` and the
`TASK_CONTEXT_INCOMPLETE` rate) · the rlimit curve `R ∈ {10, 50, 250}` and the ×3 determinism control ·
`hashes.sh` re-keyed and `controls_gate.py` re-pointed at the live checker shas · the fence widening for z3,
driven red-first, with rows **AV** and **CO** ripening in it · `rt`, `prompt_P.md`, `base.md` re-spelled ·
the Studio toolchain prerequisite (`1.88.0-aarch64-apple-darwin`) and a smoke gate that refuses a mismatch ·
the `ground_truth`-on-the-Studio fence fixture · **STAGE 0.5** (§9) · the token stop's driver wiring.

**LAWS THIS ADDENDUM ADDS.** An instrument that penalises the treatment for applying the treatment does not
measure a small effect badly, it manufactures the opposite one — ask of every gate which arm is more likely to
trip it · two correct readings of two files can still leave a defect in the space between them: a function's
behaviour and the position you call it from are separate facts · a blacklist passes exactly the tests you
thought to write, which is what makes it look like a whitelist · a two-way differential assigns blame between
the only two candidates it was given — before trusting one that acquits you, ask whether a third party was
ever on the list · a registered prediction that fails is worth more than one that passes, and worth most when
the code, not the prediction, turns out to have moved.
