import Imports.AllImports

/--
function_signature: "def find_closest_elements(numbers: List[float]) -> Tuple[float, float]"
docstring: |
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
test_cases:
  - input: [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
    expected_output: (2.0, 2.2)
  - input: [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
    expected_output: (2.0, 2.0)
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: List Rat → (Rat × Rat))
-- inputs
(numbers: List Rat) :=
-- spec
let spec (result: (Rat × Rat)) :=
2 ≤ numbers.length →
(let (smaller, larger) := result;
let abs_diff := |larger - smaller|;
smaller ≤ larger ∧
smaller ∈ numbers ∧
larger ∈ numbers ∧
(∀ x y, x ∈ numbers → y ∈ numbers → x ≠ y → abs_diff ≤ |x - y|) ∧
(smaller = larger → 2 ≤ (numbers.filter (fun z => z = smaller)).length));
-- program termination
∃ result, implementation numbers = result ∧
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (numbers: List Rat): (Rat × Rat) :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation [1.0, 2.0, 3.0, 4.0, 5.0, 2.2] = (2.0, 2.2)
#test implementation [1.0, 2.0, 3.0, 4.0, 5.0, 2.0] = (2.0, 2.0)
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(numbers: List Rat)
: problem_spec implementation numbers
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
