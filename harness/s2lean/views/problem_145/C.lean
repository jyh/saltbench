import Imports.AllImports

/--
function_signature: "def order_by_points(nums: List[int]) -> List[int]"
docstring: |
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.
test_cases:
  - input: [1, 11, -1, -11, -12]
    expected_output: [-1, -11, 1, -12, 11]
  - input: []
    expected_output: []
-/

-- start_def problem_spec
def problem_spec
-- function signature
(impl: List Int → List Int)
-- inputs
(nums: List Int) :=
-- spec
let spec (result: List Int) :=
List.Perm nums result ∧
match result with
| [] => nums = []
| head::tail =>
  let head_sum := digit_sum head;
  (∀ num ∈ nums,
    let sum := digit_sum num;
    sum > head_sum ∨
   (sum = head_sum ∧ nums.idxOf num ≥ nums.idxOf head))
  ∧ impl (nums.erase head) = tail
-- program termination
∃ result, impl nums = result ∧
-- return value satisfies spec
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (nums: List Int) : List Int :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation [1, 11, -1, -11, -12] = [-1, -11, 1, -12, 11]
#test implementation [] = []
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(nums: List Int)
: problem_spec implementation nums :=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
