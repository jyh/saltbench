import Imports.AllImports

/--
function_signature: "def strange_sort_list(lst: List[int]) -> List[int]"
docstring: |
    Given list of integers, return list in strange order.
    Strange sorting is when you start with the minimum value,
    then the maximum of the remaining integers, then the minimum and so on.
test_cases:
  - input: [1, 2, 3, 4]
    expected_output: [1, 4, 2, 3]
  - input: [5, 5, 5, 5]
    expected_output: [5, 5, 5, 5]
  - input: []
    expected_output: []
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: List Int → List Int)
-- inputs
(lst: List Int) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
