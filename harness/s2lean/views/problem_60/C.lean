import Imports.AllImports

/--
function_signature: "def sum_to_n(n: Nat) -> Nat"
docstring: |
    sum_to_n is a function that sums numbers from 1 to n.
test_cases:
  - input: 30
    expected_output: 465
  - input: 100
    expected_output: 4950
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: Nat → Nat)
-- inputs
(n : Nat) :=
-- spec
let spec (result: Nat) :=
  0 < n →
  (result = 1 ↔ n = 1) ∧
  (∀ i, implementation (i + 1) - (implementation i) = i + 1)
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
#test implementation 30 = 465
#test implementation 100 = 5050
#test implementation 5 = 15
#test implementation 10 = 55
#test implementation 1 = 1
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
