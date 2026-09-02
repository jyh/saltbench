# SCOUT DY — DeepSWE (Datacurve): THE VERUS-AMENABILITY CRITERION, REGISTERED BEFORE THE DATA

**2026-09-02, seat `bench`.** Desk row **DY**, cut at the 09/02 council (§2.4): *"SCOUT first, zero model
tokens: count Verus-amenable Rust tasks; ≥ 8 ⇒ proceeds as v2's second population; ~3 ⇒ no."*

⛔ **THIS FILE IS WRITTEN AND COMMITTED BEFORE THE DATASET IS FETCHED.** The commission's decision rule is a
threshold on a count, so whoever defines "amenable" after seeing the tasks decides the answer. The criterion
is fixed here, with its failure direction, and the census reports against it whatever it returns.

---

## §1 · WHY THIS SEAT DOES NOT TRUST ITS OWN CENSUS BY DEFAULT

The campaign has already been wrong at exactly this step. `saltbench-stage0-state`: *"Multilingual Rust **is**
43 and Multi-SWE-bench **is** 239 — our 08/29 census was wrong, from substring-vs-exact-key."* A count taken
with `in` where the consumer resolves on `==` is not a small error in a number; it is a different set.

⇒ **RULE 1 — EXACT KEYS ONLY.** Every field test is equality against a named field, never a substring of a
blob, and the census prints the field it keyed on and the distinct values it saw. If the schema does not
carry the field, the census REFUSES rather than guessing from prose.

⇒ **RULE 2 — THE SCREEN FAILS CLOSED.** A task that cannot be shown amenable is counted NOT amenable. The
threshold is a floor (≥ 8 proceeds), so every ambiguity resolved generously moves the answer toward "yes";
resolving them closed is the only direction that cannot manufacture the result the scout exists to test.

⇒ **RULE 3 — TWO COUNTS, BOTH REPORTED, NEITHER SUBSTITUTED.**
`n_rust` = tasks whose language field is exactly Rust. `n_amenable` = the subset passing §3.
**The verdict is read off `n_amenable`.** `n_rust` is reported so a reader can see the screen's attrition.

---

## §2 · WHAT "VERUS-AMENABLE" HAS TO MEAN HERE

The adaptation the council registered is **not** "prove the task correct". It is: *the agent states and
proves a Verus specification of what the hidden behavioural tests check; the tests are the non-vacuity
witness.* So amenability is a property of **the specification surface**, not of the whole repository:

> A task is **Verus-amenable** if the property its hidden tests check can be stated as a
> `requires`/`ensures` contract over the signatures the task's own change touches, and that region is
> inside the Rust subset Verus accepts.

Two things follow, and both matter for the count:
- A task in a large crate is not disqualified by the crate's size. Only the **touched region** must be in
  the subset — this is the same discipline S2-Rust already uses, where the episode sees one `task.rs`.
- A task whose test checks something **not functional** — timing, formatting, log text, CLI ergonomics,
  panics-as-behaviour — is disqualified even if its code is trivial, because there is no contract to state.

## §3 · THE SCREEN, IN ORDER; A TASK MUST PASS EVERY CLAUSE

| # | clause | disqualifies |
|---|---|---|
| S1 | the task's language field is **exactly** the Rust value used by the schema | every non-Rust task |
| S2 | the hidden test's property is **functional** — a relation between inputs and returned values/state | timing, formatting, log text, CLI ergonomics, flakiness, build-system-only changes |
| S3 | the touched region is **specifiable**: named functions with concrete signatures, not a trait-object or macro-generated surface | `dyn Trait` dispatch, proc-macro-generated bodies, blanket impls as the target |
| S4 | the touched region is inside the **Verus-supported subset**: no `async`, no `unsafe`, no FFI, no threads/interior mutability in the proof surface | anything Verus cannot elaborate |
| S5 | the property is expressible over **vstd**-representable data (integers, bools, sequences/maps/sets, plain structs/enums) | I/O handles, sockets, external crate types in the contract |
| S6 | the task is **self-contained enough to render** as one working file plus its context, as S2-Rust's `task.rs` is | changes spread over many crates with cross-crate invariants |

📌 **S2–S6 are judged from the task's own metadata and diff, never from running anything** — this scout is
zero model tokens and zero episodes by commission.
📌 **Every disqualification is recorded with its clause and one line of evidence.** A census that reports
only a total cannot be audited, and the S1 scar is precisely a total nobody could re-derive.

## §4 · WHAT IS REPORTED, WHATEVER THE ANSWER

1. The dataset identity: source URL, commit/revision, licence, task count, and the **schema field names**
   the census keyed on — so the count is reproducible from the record.
2. `n_rust` and `n_amenable`, with the per-clause attrition table (how many each of S2–S6 removed).
3. The verdict against the commission's rule: **≥ 8 ⇒ proceeds as v2's second population; ~3 ⇒ no**, and an
   explicit statement when the count lands between those two numbers, because **the commission names two
   points and not a boundary** — 4–7 is unruled and must be routed, not rounded.
4. ⚠️ Any clause that could not be evaluated from the available metadata, named, with what it would need.
   *An absence-list carries the same staleness as the presence-list it complements.*

## §5 · THE PREDICTION, REGISTERED BEFORE THE FETCH

**`n_rust` = 15–30 of 113** (five languages, roughly balanced, Rust one of them).
**`n_amenable` = 3–8**, point estimate **5** ⇒ **the likeliest outcome is the UNRULED middle**, and I expect
to be routing a fork rather than returning a clean yes/no.
⛔ **And a caution registered against my own record:** this seat has under-estimated five times in one
direction and then over-corrected once across a population boundary (P1 today, predicted 2 measured 0).
That history is about `a0`'s pass rate, not about corpus composition, so I am **not** applying a correction
to this estimate — *a correction for a bias inherits the population the bias was measured on.*
