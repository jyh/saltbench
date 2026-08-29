import Imports.AllImports

/--
function_signature: "def correct_bracketing(brackets: str) -> Bool"
docstring: |
    brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.
test_cases:
  - input: "("
    expected_output: False
  - input: "()"
    expected_output: True
  - input: "(()())"
    expected_output: True
  - input: ")(()"
    expected_output: False
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: String → Bool)
-- inputs
(x : String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
