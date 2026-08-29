import Imports.AllImports

/--
function_signature: "def how_many_times(string: str, substring: str) -> int"
docstring: |
  Find how many times a given substring can be found in the original string. Count overlaping cases.
test_cases:
  - input:
      - ""
      - "a"
    expected_output: 0
  - input:
      - "aaa"
      - "a"
    expected_output: 3
  - input:
      - "aaaa"
      - "aa"
    expected_output: 3
-/

-- start_def generated_spec
def generated_spec
-- function signature
(implementation: String → String → Nat)
-- inputs
(string substring: String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
