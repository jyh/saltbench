import Imports.AllImports

/--
function_signature: "def remove_duplicates(numbers: List[int]) -> List[int]"
docstring: |
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
test_cases:
  - input: [1, 2, 3, 2, 4]
    expected_output: [1, 3, 4]
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: List Int → List Int)
-- inputs
(numbers: List Int) :=
-- spec
let spec (result: List Int) :=
(∀ i: Int, i ∈ result → numbers.count i = 1) ∧
(∀ i: Int, i ∈ numbers → numbers.count i = 1 → i ∈ result) ∧
(∀ i j : Nat, i < result.length → j < result.length → i < j →
∃ ip jp : Nat, ip < jp ∧ result[i]! = numbers[ip]! ∧ result[j]! = numbers[jp]!)
-- program termination
∃ result, implementation numbers = result ∧
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (numbers: List Int) : List Int :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation [1, 2, 3, 2, 4] = [1, 3, 4]
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
