import Imports.AllImports

/--
function_signature: "def bf(planet1: str, planet2: str) -> List[str]"
docstring: |
    There are eight planets in our solar system: the closest to the Sun
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn,
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2.
    The function should return a tuple containing all planets whose orbits are
    located between the orbit of planet1 and the orbit of planet2, sorted by
    the proximity to the sun.
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names.
test_cases:
  - input: ("Jupiter", "Neptune")
    expected_output: ("Saturn", "Uranus")
  - input: ("Earth", "Mercury")
    expected_output: ("Venus")
  - input: ("Mercury", "Uranus")
    expected_output: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: String → String → List String)
-- inputs
(planet1: String)
(planet2: String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
