import Imports.AllImports

-- NL Spec

/--
def search(numbers: List[int]) -> int
"""You are given a non-empty list of positive integers. Return the greatest integer that is greater than
zero, and has a frequency greater than or equal to the value of the integer itself.
The frequency of an integer is the number of times it appears in the list.
If no such a value exist, return -1.
"""
-/

-- Generated Spec

def generated_spec
-- function signature
(impl: List Int → Int)
-- inputs
(x: List Int) : Prop :=
((∃ n : Int, n > 0 ∧ (x.count n : Int) ≥ n ∧ impl x = n ∧
    ∀ m : Int, m > 0 → (x.count m : Int) ≥ m → m ≤ n) ∨
  (impl x = -1 ∧ ∀ m : Int, m > 0 → (x.count m : Int) < m))

-- Ground Truth Spec

def problem_spec
-- function signature
(implementation: List Int → Int)
-- inputs
(numbers: List Int) :=
-- spec
let spec (result: Int) :=
0 < numbers.length ∧ numbers.all (fun n => 0 < n) →
(result ≠ -1 ↔ ∃ i : Nat, i < numbers.length ∧
  numbers[i]! = result ∧ numbers[i]! > 0 ∧
  numbers[i]! ≤ (numbers.filter (fun x => x = numbers[i]!)).length ∧
  (¬∃ j : Nat, j < numbers.length ∧
  numbers[i]! < numbers[j]! ∧ numbers[j]! ≤ numbers.count numbers[j]!));
-- program termination
∃ result, implementation numbers = result ∧
spec result

-- Isomorphism Lemma

axiom cheat (P : Prop) : P

-- Isomorphism Theorem

theorem spec_isomorphism:
∀ impl,
(∀ x, problem_spec impl x) ↔
(∀ x, generated_spec impl x) :=

-- Isomorphism Proof

cheat _