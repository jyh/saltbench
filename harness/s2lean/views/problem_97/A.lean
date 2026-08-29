import Imports.AllImports

/--
function_signature: "def multiply(a : Int, b : Int) -> Int"
docstring: |
    Complete the function that takes two integers and returns
    the product of their unit digits.
    Assume the input is always valid.
    -- Note(George): I'm finding it hard to not leak the implementation here, so I opted to make the spec more convoluted.
test_cases:
  - input: 148, 412
    expected_output: 16
  - input: 19, 28
    expected_output: 72
  - input: 2020, 1851
    expected_output: 0
  - input: 14, -15
    expected_output: 20
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: Int → Int → Int)
-- inputs
(a b: Int) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
