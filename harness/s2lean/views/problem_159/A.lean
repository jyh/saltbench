import Imports.AllImports

/--
function_signature: "def eat(number: Nat, need: Nat, remaining: Nat) -> List Nat"
docstring: |
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.

    Variables:
      @number : integer
          the number of carrots that you have eaten.
      @need : integer
          the number of carrots that you need to eat.
      @remaining : integer
          the number of remaining carrots thet exist in stock

    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000
test_cases:
  - input: [5, 6, 10]
    expected_output: [11, 4]
  - input: [4, 8, 9]
    expected_output: [12, 1]
  - input: [1, 10, 10]
    expected_output: [11, 0]
  - input: [2, 11, 5]
    expected_output: [7, 0]
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: Nat → Nat → Nat → List Nat)
-- inputs
(a b c : Nat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
