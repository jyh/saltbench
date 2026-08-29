import Imports.AllImports

/--
function_signature: "def pluck(numbers: List[Int]) -> List[Int]"
docstring: |
    Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smallest_value, its index ],
    If there are no even values or the given array is empty, return [].
test_cases:
  - input: [4, 2, 3]
    expected_output: [2, 1]
  - input: [1, 2, 3]
    expected_output: [2, 1]
  - input: []
    expected_output: []
  - input: [5, 0, 3, 0, 4, 2]
    expected_output: [0, 1]
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: List Nat → List Nat)
-- inputs
(x: List Nat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
