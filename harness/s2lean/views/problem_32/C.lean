import Imports.AllImports

/--
function_signature: "def find_zero(xs: list)"
docstring: |
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    Note(George): This problem has been modified from the original HumanEval spec because of Real is not a computable type, but a zero does not necessarily exist over the rationals.
test_cases:
  - input: [1, 2]
    output: -0.5
  - input: [-6, 11, -6, 1]
    output: 3.0
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: List Rat → Rat)
-- inputs
(xs: List Rat) :=
-- spec
let spec (result: Rat) :=
  let eps := (1: Rat) / 1000000;
  xs.length ≥ 1 → xs.length % 2 = 0 →
  ∀ poly : Polynomial Rat,
    poly.degree = some (xs.length - 1) →
    (∀ i, i ≤ xs.length - 1 → poly.coeff i = xs[i]!) →
    |poly.eval result| ≤ eps;
-- program termination
∃ result,
  implementation xs = result ∧
  spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (xs: List Rat) : Rat :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test |implementation [1, 2] - (-1/2)| ≤ 1/1000000
#test |implementation [-6, 11, -6, 1] - 1| ≤ 1/1000000 ∨ |implementation [-6, 11, -6, 1] - 2| ≤ 1/1000000 ∨ |implementation [-6, 11, -6, 1] - 3| ≤ 1/1000000
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(xs: List Rat)
: problem_spec implementation xs
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
