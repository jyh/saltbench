import Imports.AllImports

/--
function_signature: "def check_dict_case(s : dict[str, str]) -> bool"
docstring: |
    Given a dictionary, return True if all keys are strings in lower
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Note(George): Modified the problem to use strings only for both keys and values.
test_cases:
  - input: {"a":"apple", "b":"banana"}
    expected_output: True
  - input: {"a":"apple", "A":"banana", "B":"banana"}
    expected_output: False
  - input: {"a":"apple", "b":"banana", "a":"apple"}
    expected_output: False
  - input: {"Name":"John", "Age":"36", "City":"Houston"}
    expected_output: False
  - input: {"STATE":"NC", "ZIP":"12345" }
    expected_output: True
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: Std.HashMap String String → Bool)
-- inputs
(D: Std.HashMap String String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
