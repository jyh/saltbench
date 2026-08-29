import Imports.AllImports

/--
function_signature: "def even_odd_count(num: int) -> Tuple[int, int]"
docstring: |
    Given an integer. return a tuple that has the number of even and odd digits respectively.
test_cases:
  - input: -12
    expected_output: [1, 1]
  - input: 123
    expected_output: [1, 2]
-/

-- start_def problem_spec
def problem_spec
-- function signature
(impl: Int → Int × Int)
-- inputs
(num: Int) :=
-- spec
let spec (result: Int × Int) :=
  let (even_count, odd_count) := result;
  let numAbs := |num|.toNat;
  let numBy10 := numAbs/10;
  let (even_count', odd_count') := impl numBy10;
  (result = impl numAbs) ∧
  (0 ≤ num → (Even num ↔ 1 + even_count' = even_count) ∧ (Odd num ↔ even_count' = even_count)) ∧
  (0 ≤ num → (Odd num ↔ 1 + odd_count' = odd_count) ∧ (Even num ↔ odd_count' = odd_count));
-- program terminates
∃ result, impl num = result ∧
-- return value satisfies spec
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (num: Int) : Int × Int :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation -12 = (1, 1)
#test implementation 123 = (1, 2)
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(num: Int)
: problem_spec implementation num :=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
