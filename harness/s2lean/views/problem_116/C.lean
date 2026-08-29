import Imports.AllImports

/--
function_signature: "def max_fill_count(grid : list[list[int]], capacity : int) -> int"
docstring: |
    Please write a function that sorts an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.
test_cases:
  - input: [1, 5, 2, 3, 4]
    expected_output: [1, 2, 3, 4, 5]
  - input: [1, 0, 2, 3, 4]
    expected_output: [0, 1, 2, 3, 4]
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: List Nat → List Nat)
-- inputs
(lst: List Nat) :=
-- spec
let spec (result : List Nat) :=
  ∀ x : Nat, lst.count x = result.count x ∧
  result.length = lst.length ∧
  (∀ i j : Nat, i < j → j < result.length →
    Nat.digits 2 (result[i]!) < Nat.digits 2 (result[j]!) ∨
    (Nat.digits 2 (result[i]!) = Nat.digits 2 (result[j]!) ∧ result[i]! < result[j]!))
-- program termination
∃ result,
  implementation lst = result ∧
  spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (lst: List Nat) : List Nat :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation [1, 5, 2, 3, 4] = [1, 2, 3, 4, 5]
#test implementation [1, 0, 2, 3, 4] = [0, 1, 2, 3, 4]
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(lst: List Nat)
: problem_spec implementation lst
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
