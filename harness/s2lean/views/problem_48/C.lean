import Imports.AllImports

/--
function_signature: "def is_palindrome(string: str) -> Bool"
docstring: |
    Checks if given string is a palindrome
test_cases:
  - input: ""
    expected_output: True
  - input: "aba"
    expected_output: True
  - input: "aaaaa"
    expected_output: "True"
  - input: "zbcd"
    expected_output: "False"
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: String → Bool)
-- inputs
(string: String) :=
-- spec
let spec (result: Bool) :=
result ↔ is_palindrome string
-- program termination
∃ result, implementation string = result ∧
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (string: String) : Bool :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation "" = true
#test implementation "aba" = true
#test implementation "aaaaa" = true
#test implementation "zbcd" = false
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(s: String)
: problem_spec implementation s
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
