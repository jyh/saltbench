import Imports.AllImports

/--
function_signature: "def greatest_common_divisor(a: int, b: int) -> int"
docstring: |
    Return a greatest common divisor of two integers a and b
test_cases:
  - input:
      - 25
      - 15
    expected_output: 5
  - input:
      - 3
      - 5
    expected_output: 1
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: Int → Int → Int)
-- inputs
(a b: Int) :=
-- spec
let spec (result: Int) :=
(result ∣ a) ∧
(result ∣ b) ∧
(result ≥ 0) ∧
(∀ (d': Int),
(d' ∣ a) → (d' ∣ b) →
d' ∣ result);
-- program termination
∃ result, implementation a b = result ∧
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (a b: Int) : Int :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation 25 15 = 5
#test implementation 3 5 = 1
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(a b: Int)
: problem_spec implementation a b
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
