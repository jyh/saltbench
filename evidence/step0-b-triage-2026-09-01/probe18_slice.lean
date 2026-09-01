import Imports.AllImports

-- 1. What ARE String.drop / String.take in this toolchain?
#check @String.drop
#check @String.take

-- 2. The exact occurrence condition from problem_18's problem_spec.
example : Prop := (("aaaa":String).drop 1).take ("aa":String).length = ("aa":String)

-- 3. Is that equality REFUTABLE for a real occurrence?  ("aaaa","aa") at i=1 is a genuine hit.
theorem probe_occurrence_at_1_is_false :
    ¬ ((("aaaa":String).drop 1).take ("aa":String).length = ("aa":String)) := by
  intro h
  have h2 : ("aaaa" : String) = "aa" := congrArg String.Slice.str h
  exact absurd h2 (by decide)

-- 4. Therefore the occurrence SET for ("aaaa","aa") is empty ...
theorem probe_occurrence_set_empty :
    {i ∈ {i : Nat | i < ("aaaa":String).length - ("aa":String).length + 1} |
      (("aaaa":String).drop i).take ("aa":String).length = ("aa":String)} = (∅ : Set Nat) := by
  ext i
  simp only [Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false, not_and]
  intro _ h
  have h2 : ("aaaa" : String) = "aa" := congrArg String.Slice.str h
  exact absurd h2 (by decide)
