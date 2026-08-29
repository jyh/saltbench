import Imports.AllImports

/--
function_signature: "def parse_music(music_string: str) -> List[int]"
docstring: |
    Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat
test_cases:
  - input: "o o| .| o| o| .| .| .| .| o o"
    expected_output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
-/

-- start_def generated_spec
def generated_spec
-- function signature
(implementation: String → List Nat)
-- inputs
(string: String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
