import Imports.AllImports

/--
function_signature: "def int_to_mini_roman(num: Nat) -> String"
docstring: |
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000
test_cases:
  - input: 19
    expected_output: xix
  - input: 152
    expected_output: clii
  - input: 426
    expected_output: cdxxvi
-/

-- start_def problem_spec
def problem_spec
-- function signature
(impl: Nat → String)
-- inputs
(num: Nat) :=
-- spec
let spec (result: String) :=
1 ≤ num ∧ num ≤ 1000 ∧ (result.data.all (fun c => c.isLower)) →
isValidRoman result ∧ romanToDecimal result = num
-- program terminates
∃ result, impl num = result ∧
-- return value satisfies spec
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (num: Nat) : String :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation 19 = "xix"
#test implementation 152 = "clii"
#test implementation 426 = "cdxxvi"
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(num: Nat)
: problem_spec implementation num :=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
