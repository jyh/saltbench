import Imports.AllImports

/--
function_signature: "def compare(scores: List float, guesses: List float) -> List [float]"
docstring: |
    I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match.
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.

    Note: to reviewer, the reason for not using |.| to get the absolute value is to avoid leaking the implementation.
test_cases:
  - input: [[1,2,3,4,5,1], [1,2,3,4,2,-2]]
    expected_output: [0,0,0,0,3,3]
  - input: [[0,5,0,0,0,4], [4,1,1,0,0,-2]]
    expected_output: [4,4,1,0,0,6]
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: List Rat → List Rat → List Rat)
-- inputs
(scores guesses: List Rat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
