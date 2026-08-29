import Imports.AllImports

/--
function_signature: "def truncate_number(number: float) -> float"
docstring: |
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
test_cases:
  - input: 3.5
    expected_output: 0.5
-/

-- start_def problem_spec
def problem_spec
-- function signature
(impl: Rat → Rat)
-- inputs
(number: Rat) :=
-- spec
let spec (res) :=
number > 0 →
0 ≤ res ∧
res < 1 ∧
number.floor + res = number;
-- program terminates
∃ result, impl number = result ∧
-- return value satisfies spec
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (number: Rat) : Rat :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation 3.5 = 0.5
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(number: Rat)
: problem_spec implementation number :=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
