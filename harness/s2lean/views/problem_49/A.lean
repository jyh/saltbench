import Imports.AllImports

/--
function_signature: "def modp(n: Nat, p: Nat) -> Nat"
docstring: |
    Return 2^n modulo p (be aware of numerics).
test_cases:
  - input: [3, 5]
    expected_output: 3
  - input: [1101, 101]
    expected_output: 2
  - input: [0, 101]
    expected_output: 0
  - input: [100, 101]
    expected_output: 1
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: Nat → Nat → Nat)
-- inputs
(n p: Nat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
