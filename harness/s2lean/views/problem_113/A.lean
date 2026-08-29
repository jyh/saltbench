import Imports.AllImports

/--
function_signature: "def odd_count(lst : list[str]) -> list[str]"
docstring: |
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.
    Note(George): Found it hard to not leak the implementation, so I opted for a recursive statement.
test_cases:
  - input: ['1234567']
    expected_output: ["the number of odd elements 4n the str4ng 4 of the 4nput."]
  - input: ['3',"11111111"]
    expected_output: ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: List String → List String)
-- inputs
(lst: List String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
