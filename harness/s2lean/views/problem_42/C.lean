import Imports.AllImports

/--
function_signature: "def incr_list(numbers: List[Int]) -> List[Int]"
docstring: |
    incr_list takes a list of integers as input and returns a new list
    where each element is incremented by 1.
test_cases:
  - input: []
    expected_output: []
  - input: [1, 3, -2, 1]
    expected_output: [2, 4, -1, 2]
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: List Int → List Int)
-- inputs
(numbers: List Int) :=
-- spec
let spec (result: List Int) :=
  (result.length = numbers.length) ∧
  ∀ i, i < numbers.length →
  result[i]! = numbers[i]! + 1
-- -- program termination
∃ result, implementation numbers = result ∧
spec result
--
-- end_def problem_spec

-- start_def implementation_signature
def implementation (numbers: List Int) : List Int :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation [1, 2, 3] = [2, 3, 4]
#test implementation [5, 3, 5, 2, 3, 3, 9, 0, 123] = [6, 4, 6, 3, 4, 4, 10, 1, 124]
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(numbers : List Int)
: problem_spec implementation numbers
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
