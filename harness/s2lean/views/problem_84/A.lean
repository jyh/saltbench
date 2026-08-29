import Imports.AllImports

/--
function_signature: "def solve(n: int) -> str"
docstring: |
    Given a positive integer N, return the total sum of its digits in binary.
test_cases:
  - input: 1000
    output: "1"
  - input: 150
    output: "110"
  - input: 147
    output: "1100"
Note: The spec formalization takes the result, makes it a list of 0/1s and then reverse it and uses Nat.ofDigits. The reversal is because ofDigits expects little-endian order.
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: Nat → String)
-- inputs
(n: Nat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
