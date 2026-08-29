import Imports.AllImports

/--
function_signature: "def total_match(lst1: List[str], lst2: List[str]) -> List[str]"
docstring: |
  Write a function that accepts two lists of strings and returns the list that has
  total number of chars in the all strings of the list less than the other list.
  If the two lists have the same number of chars, return the first list.
test_cases:
  - input: ([], [])
    expected_output: []
  - input: (['hi', 'admin'], ['hI', 'Hi'])
    expected_output: ['hI', 'Hi']
  - input: (['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
    expected_output: ['hi', 'admin']
  - input: (['hi', 'admin'], ['hI', 'hi', 'hi'])
    expected_output: ['hI', 'hi', 'hi']
  - input: (['4'], ['1', '2', '3', '4', '5'])
    expected_output: ['4']
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: List String → List String → List String)
-- inputs
(lst1: List String) (lst2: List String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
