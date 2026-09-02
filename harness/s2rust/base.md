# Working notes
- The file to complete is `__EP__/repo/task.rs`. Write ONLY inside the two marked regions:
  `// start_def proof … // end_def proof` is the body of the target proof function, and
  `// start_def helpers … // end_def helpers` is where you may add new `proof fn` lemmas.
  The statements, the executable code and everything outside those two regions are fixed, and the checker
  discards edits to them.
- Check your work with `__EP__/rt verus task.rs`. That is the only command this wrapper accepts, and its
  flags are fixed — it is the same invocation the checker uses.
- The checker refuses `assume`, `admit`, `assume_specification`, `#[verifier::external_body]`,
  `#[verifier::external`, `#[verifier::assume_termination]`, `exec_allows_no_decreases_clause` and any added
  `axiom fn`. The context lemmas this file already stubs with `external_body` are the benchmark's own and
  their count must not change.
- Every item in the helpers region must be a `proof fn`. A `spec fn`, an `exec fn`, an `impl`, a `trait`, a
  `const` or a `broadcast proof` there is refused.
- **The two regions are proof text, not a module.** The checker refuses a new `use` import inside them —
  only `broadcast use <group>;` is allowed. It also refuses `mod`, `fn main`, `extern`, `unsafe`,
  `macro_rules`, `include!`, `include_str!`, `std::process`, `#[cfg`, `#[test]`, `todo!` and
  `unimplemented!`.
- Attributes inside the regions: `#[verifier::` is allowed only for `rlimit`, `integer_ring`, `memoize`,
  `loop_isolation` and `spinoff_prover`; any other one is refused. The only inner attribute forms accepted
  are `#![trigger …]`, `#![auto]` and `#![all_triggers]` — every other inner attribute is refused.
- There is no network, no cargo, no rustup and no git. Do not try to install or update anything.
