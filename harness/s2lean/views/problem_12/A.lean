import Imports.AllImports

/--
function_signature: "def longest(strings: List[str]) -> Optional[str]"
docstring: |
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
test_cases:
  - input: []
    expected_output: None
  - input: ["a", "b", "c"]
    expected_output: "a"
  - input: ["a", "bb", "ccc"]
    expected_output: "ccc"
-/

-- start_def generated_spec
def generated_spec
-- function signature
(implementation: List String → Option String)
-- inputs
(strings: List String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
