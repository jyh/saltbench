import Imports.AllImports

/--
function_signature: "def iscube(a: int) -> bool"
docstring: |
    Write a function that takes an integer a and returns True if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
test_cases:
  - input: 1
    expected_output: True
  - input: 2
    expected_output: False
  - input: -1
    expected_output: True
  - input: 64
    expected_output: True
  - input: 0
    expected_output: True
  - input: 180
    expected_output: False
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: Int → Bool)
-- inputs
(a: Int) :=
-- spec
let spec (result: Bool) :=
  result ↔ exists n: Int, a = n^3
-- program termination
∃ result, implementation a = result ∧
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (a: Int) : Bool :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation 1 = True
#test implementation 2 = False
#test implementation -1 = True
#test implementation 64 = True
#test implementation 180 = False
#test implementation 1000 = True
#test implementation 0 = True
#test implementation 1729 = False
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(a: Int)
: problem_spec implementation a
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
