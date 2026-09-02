# Working notes
- The file to complete is `__EP__/repo/task.rs`. Write ONLY inside the two marked regions:
  `// start_def proof … // end_def proof` is the body of the target proof function, and
  `// start_def helpers … // end_def helpers` is where you may add new `proof fn` lemmas.
  The statements, the executable code and everything outside those two regions are fixed, and the checker
  discards edits to them.
- Check your work with `__EP__/rt verus task.rs`. That is the only command this wrapper accepts, and its
  flags are fixed — it is the same invocation the checker uses.
- The checker refuses `assume`, `admit`, `assume_specification`, `#[verifier::external_body]`,
  `#[verifier::assume_termination]` and any added `axiom fn`. The context lemmas this file already stubs with
  `external_body` are the benchmark's own and their count must not change.
- Every item in the helpers region must be a `proof fn`. A `spec fn`, an `exec fn`, an `impl` or a `const`
  there is refused.
- There is no network, no cargo, no rustup and no git. Do not try to install or update anything.
