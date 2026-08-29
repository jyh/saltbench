import Imports.AllImports

/--
function_signature: "def words_string(s: string) -> List[string]"
docstring: |
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
test_cases:
  - input: "Hi, my name is John"
    expected_output: ["Hi", "my", "name", "is", "John"]
  - input: "One, two, three, four, five, six"
    expected_output: ["One", "two", "three", "four", "five", "six"]
-/

-- start_def problem_spec
def problem_spec
-- function signature
(implementation: String → List String)
-- inputs
(s: String) :=
-- spec
let spec (result: List String) :=
  let chars := s.toList;
  let trimmed := String.mk (chars.dropWhile (fun c => c = ' ' ∨ c = ','));
  let first := (trimmed.takeWhile (fun c => c ≠ ',' ∧ c ≠ ' ')).toString;
  (result = [] ↔ (∀ x ∈ chars, x = ' ' ∨ x = ',') ∨ s = "") ∧
  (result ≠ [] ↔ result = [first] ++ (implementation (trimmed.drop (first.length + 1)).toString))

-- program termination
∃ result, implementation s = result ∧
spec result
-- end_def problem_spec

-- start_def implementation_signature
def implementation (s: String) : List String :=
-- end_def implementation_signature
-- start_def implementation
sorry
-- end_def implementation

-- start_def test_cases
#test implementation "Hi, my name is John" = ["Hi", "my", "name", "is", "John"]
#test implementation "One, two, three, four, five, six" = ["One", "two", "three", "four", "five", "six"]
#test implementation "Hi, my name" = ["Hi", "my", "name"]
#test implementation "One,, two, three, four, five, six," = ["One", "two", "three", "four", "five", "six"]
#test implementation "" = []
#test implementation "ahmed     , gamal" = ["ahmed", "gamal"]
-- end_def test_cases

-- start_def correctness_helper_lemmas
-- end_def correctness_helper_lemmas

-- start_def correctness_definition
theorem correctness
(s: String)
: problem_spec implementation s
:=
-- end_def correctness_definition
-- start_def correctness_proof
by sorry
-- end_def correctness_proof
