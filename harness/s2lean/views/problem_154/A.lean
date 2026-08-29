import Imports.AllImports

/--
function_signature: "def cycpattern_check(String a, String b) -> Bool"
docstring: |
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word, else False
test_cases:
  - input: ["abcd", "abd"]
    expected_output: False
  - input: ["hello", "ell"]
    expected_output: True
  - input: ["whassup", "psus"]
    expected_output: False
  - input: ["abab", "baa"]
    expected_output: True
  - input: ["efef", "eeff"]
    expected_output: False
  - input: ["himenss", "simen"]
    expected_output: True
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: String → String → Bool)
-- inputs
(a b: String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
