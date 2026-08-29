import Imports.AllImports

/--
function_signature: "def max_fill_count(grid : list[list[int]], capacity : int) -> int"
docstring: |
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it,
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.
    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
test_cases:
  - input: ([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1)
    expected_output: 6
  - input: ([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2)
    expected_output: 5
  - input: ([[0,0,0], [0,0,0]], 5)
    expected_output: 0
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: List (List Nat) → Nat → Nat)
-- inputs
(grid: List (List Nat))
(capacity: Nat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
