import Imports.AllImports

/--
function_signature: "def fibfib(n: int)"
docstring: |
    The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
Note(Meghana): While the specification asks for an efficient computation of fibfib, we cannot enforce this constraint currently.
test_cases:
  - input: 1
    output: 0
  - input: 5
    output: 4
  - input: 8
    output: 24
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: Nat → Nat)
-- inputs
(x : Nat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
