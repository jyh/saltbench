import Imports.AllImports

/--
function_signature: "def fizz_buzz(n: int)"
docstring: |
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
test_cases:
  - input: 50
    output: 0
  - input: 78
    output: 2
  - input: 79
    output: 3
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: Nat → Nat)
-- inputs
(n: Nat) :=
-- spec
let spec (result: Nat) :=
  (n = 0 → result = 0) ∧
  (0 < n → result = implementation (n - 1) →
    ((n - 1) % 11 ≠  0 ∧  (n - 1) % 13 ≠  0) ∨ (n - 1).repr.count '7' = 0) ∧
  (0 < n → result ≠ implementation (n - 1) →
    ((n - 1) % 11 = 0 ∨  (n - 1) % 13 = 0) ∧
    result - implementation (n - 1) = (n - 1).repr.count '7')
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
#test implementation 50 = 0
#test implementation 78 = 2
#test implementation 79 = 3
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
