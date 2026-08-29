import Imports.AllImports

/--
function_signature: "def is_sorted(lst: List[int]) -> Bool"
docstring: |
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
test_cases:
  - input: [5]
    expected_output: True
  - input: [1, 2, 3, 4, 5]
    expected_output: True
  - input: [1, 3, 2, 4, 5]
    expected_output: False
  - input: [1, 2, 3, 4, 5, 6]
    expected_outupt: True
  - input: [1, 2, 3, 4, 5, 6, 7]
    expected_output: True
  - input: [1, 3, 2, 4, 5, 6, 7]
    expected_output: False
  - input: [1, 2, 2, 3, 3, 4]
    expected_output: True
  - input: [1, 2, 2, 2, 3, 4]
    expected_output: False
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: List Int → Bool)
-- inputs
(lst: List Int) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
