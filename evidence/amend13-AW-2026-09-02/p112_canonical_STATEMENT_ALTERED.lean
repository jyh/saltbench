import Imports.AllImports

/--
function_signature: "def reverse_delete(s : str, c : str) -> (str, bool)"
docstring: |
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    -- Note: We assume the deletions preserve the order of the remaining characters.
test_cases:
  - input: ["abcde", "ae"]
    expected_output: ("bcd", False)
  - input: ["abcdef", "b"]
    expected_output: ("acdef", False)
  - input: ["abcdedcba", "ab"]
    expected_output: ('cdedc', True)
-/

def generated_spec
-- function signature
(impl: String → String → (String × Bool))
-- inputs
(s: String)
(c: String) : Prop :=
let spec (result: (String × Bool)) :=
  let (result_str, result_palindrome) := result;
  -- the characters of s that occur in c are dropped, the rest keep their order
  result_str.toList = s.toList.filter (fun ch => !c.contains ch) ∧
  (result_palindrome ↔ is_palindrome result_str)
∃ result, impl s c = result ∧ spec result

def problem_spec
-- function signature
(implementation: String → String → (String × Bool))
-- inputs
(s: String)
(c: String) :=
-- spec
let spec (result : String × Bool) :=
  let (result_str, result_bool) := result
  result_bool = (List.Palindrome result_str.data) ∧
  (c.data.length = 0 → result_str = s) ∧
  (c.data.length > 0 →
    result_str =
    (implementation
      (String.join ((s.data.filter (fun x => x ≠ c.data.head!)).map (fun c => String.mk [c])))
      (c.drop 1).toString).fst)

-- program termination
∃ result,
  implementation s c = result ∧
  spec result



theorem spec_isomorphism:
∀ impl,
(∀ s c, problem_spec impl s c) ↔
(∀ s c, generated_spec impl s c) :=
by sorry
