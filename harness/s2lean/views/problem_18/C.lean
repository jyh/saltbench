import Imports.AllImports

/--
function_signature: "def how_many_times(string: str, substring: str) -> int"
docstring: |
  Find how many times a given substring can be found in the original string. Count overlaping cases.
test_cases:
  - input:
      - ""
      - "a"
    expected_output: 0
  - input:
      - "aaa"
      - "a"
    expected_output: 3
  - input:
      - "aaaa"
      - "aa"
    expected_output: 3
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: String → String → Nat)
-- inputs
(string substring: String) :=
-- spec
let spec (result: Nat) :=
(substring.length = 0 → result = string.length)
∧
(substring.length ≠ 0 →
(string.length < substring.length → result = 0)
∧
(string.length = substring.length →
((string = substring ↔ result = 1) ∧
(substring ≠ string ↔ result = 0)))
∧
(substring.length < string.length  →
let substring_start_idx := {i: Nat | i < string.length - substring.length + 1};
let substring_occurrences := {i ∈ substring_start_idx | (string.drop i).take substring.length = substring };
result = substring_occurrences.toFinset.card));
-- program termination
∃ result, implementation string substring = result ∧
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (string: String) (substring: String) : Nat :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation "aaa" "a" = 3
#test implementation "aaaa" "aa" = 3
#test implementation "" "a" = 0
#test implementation "a" "" = 1
#test implementation "a" "a" = 1
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(string: String)
(substring: String)
: problem_spec implementation string substring
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
