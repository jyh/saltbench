import Imports.AllImports

/--
function_signature: "def change_base(x: Nat, base: Nat) -> String"
docstring: |
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
test_cases:
  - input: (8, 3)
    expected_output: '22'
  - input: (8, 2)
    expected_output: '1000'
  - input: (7, 2)
    expected_output: '111'
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: Nat → Nat → String)
-- inputs
(x base: Nat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
