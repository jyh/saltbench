import Imports.AllImports

/--
function_signature: "def sort_array(lst : list(int)) -> list(int)"
docstring: |
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.
    Note(George): I have elected to ignore the copy part.
test_cases:
  - input: []
    output: []
  - input: [5]
    output: [5]
  - input: [2, 4, 3, 0, 1, 5]
    output: [0, 1, 2, 3, 4, 5]
  - input: [2, 4, 3, 0, 1, 5, 6]
    output: [6, 5, 4, 3, 2, 1, 0]
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: List Nat → List Nat)
-- inputs
(lst: List Nat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
