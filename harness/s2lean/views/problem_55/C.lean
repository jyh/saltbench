import Imports.AllImports

/--
function_signature: "def fib(n: int) -> int"
docstring: |
    Return n-th Fibonacci number.
test_cases:
  - input: 10
    expected_output: 55
  - input: 1
    expected_output: 1
  - input: 8
    expected_output: 21
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: Nat → Nat)
-- inputs
(n: Nat) :=
-- spec
let spec (result: Nat) :=
fibonacci_non_computable n result
-- program termination
∃ result, implementation n = result ∧
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (n: Nat) : Nat :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation 10 = 55
#test implementation 1 = 1
#test implementation 8 = 21
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(n: Nat)
: problem_spec implementation n
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
