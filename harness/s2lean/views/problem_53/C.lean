import Imports.AllImports

/--
function_signature: "def add(x: Int, y: Int) -> Int"
docstring: Add two numbers x and y
test_cases:
  - input: [2, 3]
    expected_output: 5
  - input: [5, 7]
    expected_output: 12
-/

-- start_def problem_spec
def problem_spec
-- function signature
(impl: Int → Int → Int)
-- inputs
(x y: Int) :=
-- spec
let spec (res: Int) :=
  res - x - y = 0
-- program terminates
∃ result, impl x y = result ∧
-- return value satisfies spec
spec result
-- if result then spec else ¬spec
-- end_def problem_spec

-- start_def implementation_signature
def implementation (x y: Int) : Int :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation 2 3 = 5
#test implementation 5 7 = 12
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(x y: Int)
: problem_spec implementation x y  :=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
