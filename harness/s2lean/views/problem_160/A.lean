import Imports.AllImports

/--
function_signature: "def do_algebra(operator: List String, operand: List Nat) -> Int"
docstring: |
    Given two lists operator, and operand. The first list has basic algebra operations, and
    the second list is a list of integers. Use the two given lists to build the algebric
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + )
    Subtraction ( - )
    Multiplication ( * )
    Floor division ( // )
    Exponentiation ( ** )

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
test_cases:
  - input: [['+', '*', '-'], [2, 3, 4, 5]]
    expected_output: 9
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: List String → List Nat → Int)
-- inputs
(operator : List String)
(operand : List Nat) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
