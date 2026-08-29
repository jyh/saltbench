import Imports.AllImports

/--
function_signature: "def get_closest_vowel(s : str) -> str"
docstring: |
    You are given a word. Your task is to find the closest vowel that stands between
    two consonants from the right side of the word (case sensitive).

    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition.

    You may assume that the given string contains English letter only.
    Note: The "closest" is interpreted as the closest to the end of the word, not the closest to the consonants.
test_cases:
  - input: "yogurt"
    expected_output: "u"
  - input: "FULL"
    expected_output: "U"
  - input: "quick"
    expected_output: "i"
  - input: "ab"
    expected_output: ""
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: String → String)
-- inputs
(s: String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
