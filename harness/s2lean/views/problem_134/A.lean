import Imports.AllImports

/--
function_signature: "def check_if_last_char_is_a_letter(txt: str) -> Bool"
docstring: |
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.
test_cases:
  - input: "apple pie"
    expected_output: False
  - input: "apple pi e"
    expected_output: True
  - input: "apple pi e "
    expected_output: False
  - input: ""
    expected_output: False
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: String → Bool)
-- inputs
(txt: String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
