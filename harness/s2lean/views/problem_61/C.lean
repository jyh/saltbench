import Imports.AllImports

/--
function_signature: "def correct_bracketing(brackets: str) -> Bool"
docstring: |
    brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.
test_cases:
  - input: "("
    expected_output: False
  - input: "()"
    expected_output: True
  - input: "(()())"
    expected_output: True
  - input: ")(()"
    expected_output: False
-/

-- start_def problem_spec
def problem_spec
-- function signature
(impl: String → Bool)
-- inputs
(brackets: String) :=
-- spec
let spec (result: Bool) :=
  brackets.data.all (fun c => c = '(' ∨ c = ')') →
  (result ↔ balanced_paren_non_computable brackets '(' ')')
-- program terminates
∃ result, impl brackets = result ∧
-- return value satisfies spec
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (paren_string: String) : Bool :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation "(" = false
#test implementation "()" = true
#test implementation "(()())" = true
#test implementation ")(()" = false
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(brackets: String)
: problem_spec implementation brackets :=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
