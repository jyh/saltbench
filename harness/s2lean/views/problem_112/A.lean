import Imports.AllImports

/--
function_signature: "def reverse_delete(s : str, c : str) -> (str, bool)"
docstring: |
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    -- Note: We assume the deletions preserve the order of the remaining characters.
test_cases:
  - input: ["abcde", "ae"]
    expected_output: ("bcd", False)
  - input: ["abcdef", "b"]
    expected_output: ("acdef", False)
  - input: ["abcdedcba", "ab"]
    expected_output: ('cdedc', True)
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: String → String → (String × Bool))
-- inputs
(s: String)
(c: String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
