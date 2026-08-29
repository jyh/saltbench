import Imports.AllImports

/--
function_signature: "def max_element(l: list)"
docstring: |
    Return maximum element in the list.
test_cases:
  - input: [1, 2, 3]
    output: 3
  - input: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    output: 123
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: List Int → Int)
-- inputs
(l: List Int) :=
-- spec
let spec (result: Int) :=
  l.length > 0 →
  ((∀ i, i < l.length → l[i]! ≤ result) ∧
  (∃ i, i < l.length ∧ l[i]! = result));
-- program termination
∃ result, implementation l = result ∧
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (l: List Int) : Int :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation [1, 2, 3] = 3
#test implementation [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10] = 123
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(l: List Int)
: problem_spec implementation l
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
