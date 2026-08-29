import Imports.AllImports

/--
function_signature: "def parse_nested_parens(paren_string: str) -> List[int]"
docstring: |
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
test_cases:
  - input: "(()()) ((())) () ((())()())"
    expected_output: [2, 3, 1, 3]
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: String → List Nat)
-- inputs
(paren_string: String)
:=
-- spec
let spec (result: List Nat) :=
let paren_space_split := paren_string.splitToList (fun x => x = ' ');
result.length = paren_space_split.length ∧
∀ i, i < result.length →
let group := paren_space_split[i]!;
balanced_paren_non_computable group '(' ')' →
count_max_paren_depth group = result[i]!;
-- program termination
∃ result, implementation paren_string = result ∧
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (paren_string: String) : List Nat :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation "(()()) ((())) () ((())()())" = [2, 3, 1, 3]
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(paren_string: String)
: problem_spec implementation paren_string
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
