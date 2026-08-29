import Imports.AllImports

/--
function_signature: "def starts_one_ends(n: int) -> int"
docstring: |
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    Note: For reviewer, I believe this is the most straightforward spec, and I am relying on Set cardianlity not being computable in general. The point of this problem is really to privide a formula.
    Note: But I guess a program that goes through each number and adds 1 will be the same as a program that computes in O(1) under this view.
test_cases:
  - input: 1
    output: 1
  - input: 2
    output: 18
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: Nat → Nat)
-- inputs
(n: Nat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
