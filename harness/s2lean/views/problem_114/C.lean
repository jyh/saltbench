import Imports.AllImports

/--
function_signature: "def minSubArraySum(nums : list[int]) -> int"
docstring: |
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
test_cases:
  - input: [2, 3, 4, 1, 2, 4]
    expected_output: 1
  - input: [-1, -2, -3]
    expected_output: -6
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: List Int → Int)
-- inputs
(nums: List Int) :=
-- spec
let spec (result : Int) :=
  (∀ subarray ∈ nums.sublists,
    subarray.length > 0 →
    result ≤ subarray.sum) ∧
  (∃ subarray ∈ nums.sublists,
    subarray.length > 0 ∧
    result = subarray.sum)
-- program termination
∃ result,
  implementation nums = result ∧
  spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (nums: List Int) : Int :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation [2, 3, 4, 1, 2, 4] = 1
#test implementation [-1, -2, -3] = -6
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(nums: List Int)
: problem_spec implementation nums
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
