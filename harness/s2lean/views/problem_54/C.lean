import Imports.AllImports

/--
function_signature: "def same_chars(s0: string, s1: string) -> Bool"
docstring: Check if two words have the same characters.
test_cases:
  - input: ['eabcdzzzz', 'dddzzzzzzzddeddabc']
    expected_output: True
  - input: ['eabcd', 'dddddddabc']
    expected_output: False
-/

-- start_def problem_spec
def problem_spec
-- function signature
(impl: String → String → Bool)
-- inputs
(s0 s1: String) :=
-- spec
let spec (res: Bool) :=
  res ↔ (∀ c : Char, c ∈ s0.toList ↔ c ∈ s1.toList)
-- program terminates
∃ result, impl s0 s1 = result ∧
-- return value satisfies spec
spec result
-- if result then spec else ¬spec
-- end_def problem_spec

-- start_def implementation_signature
def implementation (s0 s1: String) : Bool :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation 'eabcdzzzz' 'dddzzzzzzzddeddabc' = true
#test implementation 'abcd' 'dddddddabc' = true
#test implementation 'dddddddabc' 'abcd' = true
#test implementation 'eabcd' 'dddddddabc' = false
#test implementation 'abcd' 'dddddddabce' = false
#test implementation 'eabcdzzzz' 'dddzzzzzzzddddabc' = false
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(s0 s1: String)
: problem_spec implementation s0 s1  :=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
