# U2 use probe: generator, frozen filter and first live readings (2026-10-23)

This is the O90 test design's U2 probe (the PM's draft 4, §1, row "U2 use", findings F2 and G3). A reader is asked
`which of these library facts does this proof use?`. The generator is `harness/s2lean/u2_gen.py`. **Lean computes
every key, and the script never types one.** The items in this directory come from amendment 8 artifacts. They test
the instrument. They are not O90 items, because no O90 artifact exists yet.

## What it computes

For one passed stage-B artifact (the archived `canonical.lean`: frozen statements plus the agent's
`spec_isomorphism_proof` and `iso_helper_lemmas` sections), the tool:

1. **Refuses** anything that is not a stage-B episode whose manifest says `passed: true`. It also refuses a file whose
   sha256 differs from `check.json`'s `canonical_sha256`, and bodies that `screen.py` flags. Agent text is
   re-elaborated outside check.py's sandbox, so only screened, passed artifacts are admitted.
2. **Re-elaborates** a copy of the file with a read-only probe appended: one `#eval` that defines nothing and writes
   one file. For every constant *defined in the file* (module index none), the probe records the constants its type
   and its value mention (`Expr.getUsedConstants`). The file's constants include the agent's helper declarations
   (private ones too), `generated_spec`, the frozen `problem_spec`, and every auxiliary the elaborator made, such as
   `spec_isomorphism._proof_1_3` and `_simp_1`. For every imported constant those mention, the probe records its
   kind, module, the instance, recursor, matcher, noConfusion and deprecated flags, its type hash and its type head.
3. **Closes transitively.** A worklist runs from the value of `spec_isomorphism` (its elaborated term, the root)
   through every constant defined in the file that it reaches, taking both the type and the value of each. Imported
   constants are the leaves. A derivation split into named helper declarations therefore reaches the same library
   facts as one inline term.
4. **Restricts to one population.** A leaf counts only if its module root is in `LIBRARY_ROOTS`: `Init Std Lean
   Mathlib Batteries Aesop Qq ProofWidgets Plausible ImportGraph LeanSearchClient`. The task's own `Imports.*`
   helpers are not library.
5. **Filters**, using the frozen list below. The filter applies to library leaves only. It never applies to the
   file's own constants, which are traversed and never dropped.
6. **Draws items.** Per artifact and per kind (`theorem`; `def`, where an `opaque` counts as a `def`), the used
   members of that kind are ordered by `sha256(seed|problem|arm|used|name)` and cut into chunks of k = 4. Up to 2
   items are made per kind. Each item gets m = 4 distractors. Distractor j is matched to used member j mod k (its
   **anchor**): it is the first untaken eligible constant, in `sha256(seed|problem|arm|pool|name)` order, that shares
   the anchor's namespace and module family (the first two module components). Failing that, it shares the namespace
   alone. Failing that, it is any eligible pool member (`pool`). The level is recorded in `items.tsv` column `match`.
   Options are presented in `sha256(seed|problem|arm|order:<item>|name)` order. An item that cannot get m
   distractors is not made.
   **Pool for a kind:** imported constants of that kind whose top-level namespace (`_root_` for a one-component name)
   is the namespace of some used member of that kind. Then the same filter, minus the used set, minus any constant
   whose type hash equals a used member's (rule `DUP-TYPE`: an `alias` is the same fact under another name).

The item asks `used by this proof`, never `needed`.

## The frozen filter (rules in order; a constant is counted under the first that fires)

| rule | drops |
|---|---|
| `NOT-LIBRARY` | module root not in `LIBRARY_ROOTS` |
| `INSTANCE` | tagged `[instance]` (Lean `Meta.isInstanceCore`) |
| `SYNTAX` | head of the type (after binders) is in `SYNTAX_TYPEHEADS`: `ParserDescr`, `TrailingParserDescr`, `Parser`, `Macro`, the elaborator, delaborator and unexpander types, simprocs, `MetaM`/`CoreM` code |
| `COMPILER-AUX` | Lean flags it as an auxiliary recursor, noConfusion, matcher or recursor, or its last component is in `AUX_LAST` (`rec recOn casesOn below ibelow brecOn binductionOn noConfusion noConfusionType ctorIdx toCtorIdx ctorElim ctorElimType inj injEq sizeOf_spec recAux casesAuxOn`) |
| `EQN-LEMMA` | last component `eq_N`, `eq_def`, `_unfold`, `_sunfold`, `eq_unfold` or `_eq_N` (equation auxiliaries) |
| `AUX-NUMBERED` | a component is `match_N` or `proof_N` |
| `AUX-NAME` | the name contains `_private`, `._` or `_auxLemma` |
| `TACTIC-INTERNAL` | the name starts with `Lean.Omega.`, `Mathlib.Tactic.`, `Mathlib.Meta.`, `Lean.Meta.`, `Lean.Elab.`, `Lean.Parser.`, `Lean.Grind.`, `Nat.Linear.`, `Nat.SOM.`, `Lean.Simp.`, `Aesop.`, `Qq.`, `Linarith.` or `Mathlib.Linarith.` (tactic certificate machinery) |
| `DEPRECATED` | tagged `@[deprecated]` |

**The reviewer's decisions on this list, made by bench while building it and not set by the design:**
- `match_` and `proof_` are matched as **whole components** (`match_N`, `proof_N`), not as substrings. Read as
  substrings they would also drop real library facts such as `proof_irrel`. A self-test arm keeps `proof_irrel` and
  `eq_self`.
- **`recAux` and `casesAuxOn` were added on 2026-10-23 after the Lean fixture showed the need.** On Lean 4.27,
  `induction n` over `Nat` elaborates through `Nat.recAux`, Nat's custom eliminator. It is a plain `def` that no
  recursor flag marks, so without this entry it would have counted as a library fact. No O90 artifact existed when
  this change was made.
- **`SYNTAX` and `TACTIC-INTERNAL` were added on 2026-10-23 after the first live run, before any O90 artifact
  existed.** That run drew the notation `def` `«term∏'_,_»` as a distractor. It also showed that a derivation
  calling `omega` reaches dozens of `Lean.Omega.*` certificate facts (27 in ep-a1644525). `TACTIC-INTERNAL` is the
  rule most open to argument. It removes facts that are in the term but that no author chose. If it is struck,
  `omega`/`ring` derivations carry many more used facts, and the arms differ partly by tactic choice.
- `DEPRECATED` drops a deprecated fact from the used set even when the term really uses it (2 such drops in the
  live run).

## Seed and parameters

`--seed o90-u2-2026-10-23` (the default), `--k 4 --m 4 --items-per-kind 2`. Every draw is a pure function of
(seed, problem, arm, the Lean output).

## How to run

```
python3 harness/s2lean/u2_gen.py --selftest                              # pure arms + mutants, no Lean
SSH_HOST=<run box> python3 harness/s2lean/u2_gen.py lean-selftest --work DIR   # Lean fixtures + mutants
SSH_HOST=<run box> python3 harness/s2lean/u2_gen.py run --ep '~/<state>/ep-…' … --out DIR --work WDIR
python3 harness/s2lean/u2_gen.py summary --out DIR
```

One Lean run per artifact, about 30 s each. Runs are sequential, under the one-heavy-job convention. The probe writes
to a file under `REMOTE_DIR` (default `~/bench-dry/u2-2026-10-23/work`), and the tool copies it back to `WDIR`. The
probe files (40–120k pool rows, 6–13 MB) are not kept here. Their sha256 values are in `report.json`
(`probe_sha256`).

## Files

- `used.tsv`: per artifact, every used library constant (all kinds), with `via` (the file constant through which it
  was first reached; `spec_isomorphism` means it is in the root term itself) and `only_via_problem_spec` (1 means it
  is reachable only through the frozen human spec, which both arms share).
- `drops.tsv`: every library leaf the closure reached and the filter dropped, with its rule.
- `items.tsv`: one row per option (item, episode, problem, arm, kind, k, m, position, option, **key**, module, via,
  match, anchor). `key` is `used` or `not-used`.
- `report.json`: parameters, the filter as run, counts per artifact (pool candidates, eligible, drops by rule,
  `DUP-TYPE`, in-used), the canonical sha256 values, and the Lean project manifest hash now and at the run.
- `run.log`, `selftest.log`, `lean-selftest.log`: the output of the three commands, each with its `EXIT=` line.

## Checks of the instrument

- `--selftest`: **42 arms OK, 8 mutants, all RED** (`selftest.log`). The mutants are: M-SKIP-LOCALS (no traversal
  of the file's constants), M-FILTER-LOCALS (filter applied before the closure, which drops a `_private` helper),
  M-NO-FILTER, M-DRAW-NO-EXCLUDE, M-DRAW-NO-DUPTYPE, both of those together, M-DRAW-UNSEEDED and M-DRAW-NO-MODMATCH.
  Two mutants first came back not red. Both were faults in the arms, fixed as follows:
  - "No dropped name is in the used set" is vacuous when nothing is dropped. It now reads "no used name fires a
    filter rule".
  - The in-used exclusion is masked at the output by `DUP-TYPE`, because a used constant in the pool carries its own
    type hash. Its mutant now shows in the report counts, and only both guards off can break disjointness. The
    synthetic pool was shrunk to make that observable. At 40 members, the planted entries were never drawn.
- `lean-selftest`: **9 arms OK, 3 mutants, all RED** (`lean-selftest.log`), on four Lean fixtures in one file:
  - Direct: a root term naming `List.append_nil`.
  - Via: the same root through a public helper.
  - Priv: the same root through a `private` helper.
  - Aux: a root by `induction`.
  The expected set is **derived** from Direct's own root term by Lean (`congrArg`, `List.append_nil`); it is not
  typed. Two non-vacuity arms confirm that Via's and Priv's own root terms lack `List.append_nil`. M-SKIP-LOCALS
  turns Via and Priv red. M-FILTER-LOCALS turns Priv red. M-NO-FILTER lets an instance and `Nat.recAux` into the
  used set.
- **On real artifacts**, recomputed from the six saved probe files:
  - M-SKIP-LOCALS drops 7 to 17 used `theorem` constants per artifact (ep-e3da4a44: 19 → 2). The losses include
    constants under the elaborator's own `spec_isomorphism._proof_1_N` auxiliaries, so even an unsplit derivation
    needs the closure.
  - 0 of 96 distractors lie in the raw (pre-filter) closure.
  - Every key option is in `used.tsv`, and `used.tsv` equals the recomputed set.
  - A second, independent Lean run of ep-e3da4a44 gave a byte-identical probe file (sha256 `3206e03c902c…`), plus
    identical `items.tsv` and `used.tsv` rows. Another seed changes the items.

## Live readings (amendment 8, passed stage-B, both arms, three problems)

Lean 4.27.0. The project's `lake-manifest.json` sha256 is `75f31318f4fa…`, both now and in every episode's manifest,
so the re-elaboration uses the Mathlib the episode was checked against.

| episode | problem | arm | file consts | reached imported | dropped | used (all kinds) | used `theorem` | used `def` | in the root term directly | items |
|---|---|---|---|---|---|---|---|---|---|---|
| ep-a1644525 | 74 | a0 | 10 | 161 | 90 | 71 | 25 | 24 | 40 | 4 |
| ep-1a75f80f | 74 | a2 | 7 | 165 | 93 | 72 | 26 | 24 | 40 | 4 |
| ep-05b2f46c | 16 | a0 | 10 | 70 | 17 | 53 | 16 | 21 | 31 | 4 |
| ep-e3da4a44 | 16 | a2 | 11 | 72 | 16 | 56 | 19 | 21 | 12 | 4 |
| ep-e45d67b9 | 141 | a0 | 9 | 91 | 24 | 67 | 18 | 23 | 46 | 4 |
| ep-51311316 | 141 | a2 | 10 | 81 | 23 | 58 | 13 | 24 | 46 | 4 |

- **Drops (all six):** `INSTANCE` 167 · `TACTIC-INTERNAL` 53 · `COMPILER-AUX` 27 · `AUX-NAME` 14 · `DEPRECATED` 2.
- **Distractor match levels (96):** ns+module2 80 · ns 4 · pool 12. The `pool` level appears where an anchor is
  alone in its namespace, such as `HAdd.hAdd`.
- **Sample used `theorem` constants:**
  - ep-a1644525: `CharP.cast_eq_zero` `Decidable.byContradiction` `Eq.symm` `Eq.trans` `Int.add_one_le_of_lt` …
  - ep-e3da4a44: `Finset.ext` `Finset.mem_image` `Iff.mp` `Iff.symm` …
  - ep-51311316: `List.countP_eq_length_filter` `List.exists_cons_of_ne_nil` `String.toList_empty` …
- **Sample item** (`p16-a2-theorem-0`): key `Finset.mem_image`, `funext`, `Iff.symm`, `Iff.mp`. Distractors
  `Finset.attachFin_subset_attachFin_iff`, `imp_intro`, `Iff.refl`, `Iff.subst`.

All sources are under the run box's amendment 8 state directory.

## LIMITS

- **`used` is not `needed`.** The key says which constants appear in the elaborated term, not which ones the
  argument depends on. An item asks `used by this proof`, never `needed`.
- **The term is not the source.** `simp`, `omega`, `exact?`, `decide` and `norm_num` put constants in the term that
  the agent never wrote (`implies_congr`, `of_eq_true`, `eq_self`, `Decidable.byContradiction` …). A reader working
  from the source alone cannot always see them, and the two arms can differ by tactic choice as well as by
  understanding. `TACTIC-INTERNAL` removes only the certificate namespaces.
- **The closure goes through `problem_spec` and `generated_spec`.** Constants of the human spec's definition reached
  through the root are in both arms' sets. `only_via_problem_spec` marks the ones reachable only that way (0 or 1
  per artifact here, because these derivations unfold the spec and its constants enter the root term directly).
- **`def` items are dominated by notation projections** (`HAdd.hAdd`, `LE.le`, `OfNat.ofNat`, `dite`). A scorer
  may prefer the `theorem` items. Constructors, inductives and axioms are in `used.tsv` and are never itemised.
- **`DUP-TYPE` catches only exact aliases**, meaning a structurally equal type hash. A restatement with different
  binders or universe names is not caught.
- **The pool is matched by namespace and module family, not by difficulty.** Some distractors can be rejected
  without reading the artifact. 12 of 96 here fell back to the whole pool.
- **Re-elaboration is not the checked olean.** The tool re-elaborates `canonical.lean` in the project's current
  environment. The sha256 pin guarantees the source, and the manifest hash shows the same Mathlib, but the term is the
  one this elaboration produces. It does not run in check.py's sandbox; the admission rule (passed, sha-pinned,
  screened) is the guard.
- **The probe is a plain `#eval` appended after the agent's text.** An artifact that changes the environment in ways
  the screen does not catch could in principle affect the probe. Only screened, passed artifacts are admitted.
- **Six artifacts, three problems.** The readings validate the instrument. They are not a measure of either arm.
