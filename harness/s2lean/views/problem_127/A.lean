import Imports.AllImports

/--
function_signature: "def intersection(interval1: Tuple[Int, Int], interval2: Tuple[Int, Int]) -> str"
docstring: |
    You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".
test_cases:
  - input: [(1, 2), (2, 3)]
    expected_output: "NO"
  - input: [(-1, 1), (0, 4)]
    expected_output: "NO"
  - input: [(-3, -1), (-5, 5)]
    expected_output: "YES"
-/

-- start_def generated_spec
def generated_spec
-- function signature
(impl: Int × Int → Int × Int → String)
-- inputs
(interval1: Int × Int)
(interval2: Int × Int) : Prop :=
-- end_def generated_spec
-- start_def generated_spec_body
sorry
-- end_def generated_spec_body
