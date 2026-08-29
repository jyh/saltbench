import Imports.AllImports

/--
function_signature: "def filter_by_prefix(strings: List[str], prefix: str) -> List[str]"
docstring: |
    Filter an input list of strings only for ones that start with a given prefix.
test_cases:
  - input:
    - []
    - "a"
    expected_output: []
  - input:
    - ["abc", "bcd", "cde", "array"]
    - "a"
    expected_output: ["abc", "array"]
-/

-- start_def generated_spec
def generated_spec
-- function signature
(implementation: List String → String → List String)
-- inputs
(strings: List String)
(pref: String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
