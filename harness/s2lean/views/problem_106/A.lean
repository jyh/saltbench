import Imports.AllImports

/--
function_signature: "def f(n: int) -> List[int]"
docstring: |
    Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
test_cases:
  - input: 5
    expected_output: [1, 2, 6, 24, 15]
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: Int → List Int)
-- inputs
(n: Int) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
