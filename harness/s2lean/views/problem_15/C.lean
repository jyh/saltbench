import Imports.AllImports

/--
function_signature: "def string_sequence(n: int) -> str"
docstring: |
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
test_cases:
  - input: 0
    expected_output: "0"
  - input: 5
    expected_output: "0 1 2 3 4 5"
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: Nat → String)
-- inputs
(n: Nat) :=
-- spec
let spec (result: String) :=
let result_nums := result.splitOn " ";
result_nums.length = n + 1 ∧
∀ i, i < n + 1 → result_nums[i]! = i.repr;
-- program termination
∃ result, implementation n = result ∧
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (n: Nat) : String :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation 0 = "0"
#test implementation 5 = "0 1 2 3 4 5"
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
