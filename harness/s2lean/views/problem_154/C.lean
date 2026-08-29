import Imports.AllImports

/--
function_signature: "def cycpattern_check(String a, String b) -> Bool"
docstring: |
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word, else False
test_cases:
  - input: ["abcd", "abd"]
    expected_output: False
  - input: ["hello", "ell"]
    expected_output: True
  - input: ["whassup", "psus"]
    expected_output: False
  - input: ["abab", "baa"]
    expected_output: True
  - input: ["efef", "eeff"]
    expected_output: False
  - input: ["himenss", "simen"]
    expected_output: True
-/

-- start_def problem_spec
def problem_spec
-- function signature
(impl: String → String → Bool)
-- inputs
(a b: String) :=
-- spec
let spec (result: Bool) :=
(b.length = 0 → result) ∧
(0 < b.length →
result ↔ ((b.length ≤ a.length) ∧
  (∃ i : Nat, i < b.length ∧
  let b_rotation := (b.drop i).toString ++ (b.take i).toString;
  a.containsSubstr b_rotation)));
-- program terminates
∃ result, impl a b = result ∧
-- return value satisfies spec
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (a b: String) : Bool :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation "abcd" "abd" = False
#test implementation "hello" "ell" = True
#test implementation "whassup" "psus" = False
#test implementation "abab" "baa" = True
#test implementation "efef" "eeff" = False
#test implementation "himenss" "simen" = True
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(a b: String)
: problem_spec implementation a b :=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
