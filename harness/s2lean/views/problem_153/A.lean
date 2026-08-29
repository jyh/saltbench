import Imports.AllImports

/--
function_signature: "def Strongest_Extension(class_name: String, extensions: List[String]) -> String"
docstring: |
    You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters
    in the extension's name, the strength is given by the fraction CAP - SM.
    You should find the strongest extension and return a string in this
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension
    (its strength is -1).
test_cases:
  - input: ['my_class', ['AA', 'Be', 'CC']]
    expected_output: 'my_class.AA'
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: String → List String → String)
-- inputs
(class_name: String)
(extensions: List String) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
