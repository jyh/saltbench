import Imports.AllImports

/--
function_signature: "def get_positive(l: list)"
docstring: |
    Return only positive numbers in the list.
test_cases:
  - input: [-1, 2, -4, 5, 6]
    expected_output: [2, 5, 6]
  - input: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected_output: [5, 3, 2, 3, 9, 123, 1]
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: List Int → List Int)
-- inputs
(numbers: List Int) :=
-- spec
let spec (result: List Int) :=
  result.all (λ x => x > 0 ∧ x ∈ numbers) ∧
  numbers.all (λ x => x > 0 → x ∈ result) ∧
  result.all (λ x => result.count x = numbers.count x);
-- program termination
∃ result,
  implementation numbers = result ∧
  spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (numbers: List Int): List Int :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation [(-1), 2, (-4), 5, 6] = [2, 5, 6]
#test implementation [5, 3, (-5), 2, (-3), 3, 9, 0, 123, 1, (-10)] = [5, 3, 2, 3, 9, 123, 1]
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(numbers: List Int)
: problem_spec implementation numbers
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
