import Imports.AllImports

/--
function_signature: "def select_words(s : str, n : int) -> list[str]"
docstring: |
    Given a string s and a natural number n, you have been tasked to implement
    a function that returns a list of all words from string s that contain exactly
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
test_cases:
  - input: ("Mary had a little lamb", 4)
    expected_output: ["little"]
  - input: ("Mary had a little lamb", 3)
    expected_output: ["Mary", "lamb"]
  - input: ("simple white space", 2)
    expected_output: []
  - input: ("Hello world", 4)
    expected_output: ["world"]
  - input: ("Uncle sam", 3)
    expected_output: ["Uncle"]
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: String → Nat → List String)
-- inputs
(s: String)
(n: Nat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
