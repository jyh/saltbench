import Imports.AllImports

/--
function_signature: "def rescale_to_unit(numbers: List[float]) -> List[float]"
docstring: |
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
test_cases:
  - input: [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_output: [0.0, 0.25, 0.5, 0.75, 1.0]
-/

-- start_def generated_spec
def generated_spec
-- function signature
(implementation: List Rat → List Rat)
-- inputs
(numbers: List Rat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
