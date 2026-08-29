import Imports.AllImports

/--
function_signature: "def sum_squares(lst: List[int]) -> int"
docstring: |
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.
test_cases:
  - input: [1, 2, 3]
    expected_output: 6
  - input: []
    expected_output: 0
  - input: [-1, -5, 2, -1, -5]
    expected_output: -126
-/

-- start_def problem_spec
def problem_spec
-- function signature
(impl: List Int → Int)
-- inputs
(lst : List Int) :=
-- spec
let spec (result : Int) :=
let last := lst.length-1;
(lst = [] → result = 0) ∧
(lst ≠ [] ∧ last % 3 = 0 → result = lst[last]! ^ 2 + impl (lst.take last)) ∧
(lst ≠ [] ∧ last % 4 = 0 ∧ last % 3 != 0 → result = lst[last]! ^ 3 + impl (lst.take last)) ∧
(lst ≠ [] ∧ last % 3 != 0 ∧ last % 4 != 0 → result = lst[last]! + impl (lst.take last))
-- program termination
∃ result, impl lst = result ∧
-- return value satisfies spec
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (lst : List Int) : Int :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation [1, 2, 3] = 6
#test implementation [] = 0
#test implementation [-1, -5, 2, -1, -5] = -126
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(lst : List Int)
: problem_spec implementation lst :=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
