import Imports.AllImports

/--
function_signature: "def is_nested(string: str) -> Bool"
docstring: |
    Create a function that takes a string as input which contains only parentheses.
    The function should return True if and only if there is a valid subsequence of parentheses
    where at least one parenthesis in the subsequence is nested.
test_cases:
  - input: '(())'
    expected_output: True
  - input: '()))))))((((()'
    expected_output: False
  - input: '()()'
    expected_output: False
  - input: '()'
    expected_output: False
  - input: '(()())'
    expected_output: True
  - input: '(())(('
    expected_output: True
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: String → Bool)
-- inputs
(lst: String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
