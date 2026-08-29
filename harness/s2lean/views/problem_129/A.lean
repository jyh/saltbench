import Imports.AllImports

/--
function_signature: "def split_words(txt)"
docstring: |
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
test_cases:
  - input: "Hello world!"
    expected_output: ["Hello", "world!"]
  - input: "Hello,world!"
    expected_output: ["Hello", "world!"]
  - input: "abcdef"
    expected_output: 3
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: String → Option (List String) × Option Nat)
-- inputs
(text: String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
