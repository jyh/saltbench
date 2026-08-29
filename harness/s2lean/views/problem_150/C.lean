import Imports.AllImports

/--
function_signature: "def x_or_y(int n, int x, int y) -> int"
docstring: |
    A simple program which should return the value of x if n is
    a prime number and should return the value of y otherwise.
test_cases:
  - input: [7, 34, 12]
    expected_output: 34
  - input: [15, 8, 5]
    expected_output: 5
-/

-- start_def problem_spec
def problem_spec
-- function signature
(impl: Int → Int → Int → Int)
-- inputs
(n x y: Int) :=
-- spec
let spec (result: Int) :=
(result = x ↔ Nat.Prime n.toNat) ∧
(result = y ↔ (¬ Nat.Prime n.toNat ∨ n ≤ 1))
-- program terminates
∃ result, impl n x y = result ∧
-- return value satisfies spec
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (n x y: Int) : Int :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation 7 34 12 = 34
#test implementation 15 8 5 = 5
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(n x y: Int)
: problem_spec implementation n x y :=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
