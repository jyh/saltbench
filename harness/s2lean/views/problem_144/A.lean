import Imports.AllImports

/--
function_signature: "def simplify(x: str, n: str) -> Bool"
docstring: |
    Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.
test_cases:
  - input: ["1/5", "5/1"]
    expected_output: True
  - input: ["1/6", "2/1"]
    expected_output: False
  - input: ["7/10", "10/2"]
    expected_output: False
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: String → String → Bool)
-- inputs
(x: String) (n: String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
