import Imports.AllImports

/--
function_signature: "def match_parens(l : list[str]) -> str"
docstring: |
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
test_cases:
  - input: ['()(', ')']
    expected_output: "Yes"
  - input: [')', ')']
    expected_output: "No"
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: List String → String)
-- inputs
(l: List String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
