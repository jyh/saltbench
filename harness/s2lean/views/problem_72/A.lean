import Imports.AllImports

/--
function_signature: "def will_it_fly(q: List[int], w: int) -> bool"
docstring: |
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is
    less than or equal the maximum possible weight w.
test_cases:
  - input: ([1, 2], 5)
    expected_output: False
  - input: ([3, 2, 3], 1)
    expected_output: False
  - input: ([3, 2, 3], 9)
    expected_output: True
  - input: ([3], 5)
    expected_output: True
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: List Int → Int → Bool)
-- inputs
(q: List Int) (w: Int) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
