Complete the proof of `__TARGET__` in `__EP__/repo/task.rs`: write the body inside the `proof` section so that
Verus verifies the whole file. You may add helper `proof fn` lemmas inside the `helpers` section.

Do not change the function's signature, its `requires`/`ensures`, or anything outside the two sections.

Do not use `assume`, `admit`, `assume_specification`, `#[verifier::external_body]`,
`#[verifier::assume_termination]` or a new `axiom fn`: the checker refuses them.

`assert(…) by (nonlinear_arith)`, `by (bit_vector)`, `by (compute)`, `#[trigger]` / `#![trigger …]` /
`#![auto]` / `#![all_triggers]` annotations, `reveal(…)`, `broadcast use …` and `decreases` are normal Verus
proof, not placeholders, and are fine.

When `verus` reports `0 errors` and you are satisfied, stop; the file is your answer.
