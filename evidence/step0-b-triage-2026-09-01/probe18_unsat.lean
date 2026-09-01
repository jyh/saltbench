import Imports.AllImports

def problem_spec
-- function signature
(implementation: String → String → Nat)
-- inputs
(string substring: String) :=
-- spec
let spec (result: Nat) :=
(substring.length = 0 → result = string.length)
∧
(substring.length ≠ 0 →
(string.length < substring.length → result = 0)
∧
(string.length = substring.length →
((string = substring ↔ result = 1) ∧
(substring ≠ string ↔ result = 0)))
∧
(substring.length < string.length  →
let substring_start_idx := {i: Nat | i < string.length - substring.length + 1};
let substring_occurrences := {i ∈ substring_start_idx | (string.drop i).take substring.length = substring };
result = substring_occurrences.toFinset.card));
-- program termination
∃ result, implementation string substring = result ∧
spec result

/-- The occurrence set of the docstring's own example is EMPTY, because in Lean v4.27
    `String.drop/take : String -> Nat -> String.Slice` and `Slice` equality is STRUCTURAL:
    it forces the base strings equal. -/
theorem occ_set_empty :
    {i : Nat | i ∈ {i : Nat | i < ("aaaa":String).length - ("aa":String).length + 1} ∧
      (("aaaa":String).drop i).take ("aa":String).length = ("aa":String).toSlice} = (∅ : Set Nat) := by
  ext i
  simp only [Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false, not_and]
  intro _ hh
  have h2 : ("aaaa" : String) = "aa" := congrArg String.Slice.str hh
  exact absurd h2 (by decide)

theorem occ_card_zero :
    ({i : Nat | i ∈ {i : Nat | i < ("aaaa":String).length - ("aa":String).length + 1} ∧
      (("aaaa":String).drop i).take ("aa":String).length = ("aa":String).toSlice} : Set Nat).toFinset.card = 0 := by
  rw [Finset.card_eq_zero, Set.toFinset_eq_empty]
  exact occ_set_empty

/-- The frozen `problem_spec` for problem_18, at the docstring's OWN example
    ("aaaa","aa"), forces the answer 0 -- while the C view's `#test` line demands 3. -/
theorem problem_spec_forces_zero_at_aaaa_aa
    (impl : String → String → Nat)
    (h : problem_spec impl "aaaa" "aa") : impl "aaaa" "aa" = 0 := by
  obtain ⟨r, hr, hspec⟩ := h
  have hne : ("aa":String).length ≠ 0 := by decide
  have hlt : ("aa":String).length < ("aaaa":String).length := by decide
  have h3 : r = ({i : Nat | i ∈ {i : Nat | i < ("aaaa":String).length - ("aa":String).length + 1} ∧
      (("aaaa":String).drop i).take ("aa":String).length = ("aa":String).toSlice} : Set Nat).toFinset.card :=
    (hspec.2 hne).2.2 hlt
  rw [occ_card_zero] at h3
  rw [hr, h3]

/-- Hence stage C for problem_18 is UNSATISFIABLE: no `implementation` can both satisfy
    `correctness` and pass the frozen `#test implementation "aaaa" "aa" = 3`. -/
theorem stageC_problem18_unsatisfiable :
    ¬ ∃ impl : String → String → Nat,
        (∀ s t, problem_spec impl s t) ∧ impl "aaaa" "aa" = 3 := by
  rintro ⟨impl, hcorrect, htest⟩
  have h := problem_spec_forces_zero_at_aaaa_aa impl (hcorrect "aaaa" "aa")
  omega

#print axioms occ_set_empty
#print axioms occ_card_zero
#print axioms problem_spec_forces_zero_at_aaaa_aa
#print axioms stageC_problem18_unsatisfiable
