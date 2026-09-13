import re

with open('ScratchX.lean', 'r') as f:
    content = f.read()

# I will find the block starting with "let C := ... \n  clear_value C"
# and ending before "have h_logbK_pos : 0 \le Real.logb 2 K + 1"
# and replace it!

start_marker = "  clear_value C"
end_marker = "  have h_logbK_pos : 0 ≤ Real.logb 2 K + 1 := by"

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker)
    
    new_block = """

  let K := sealK k
  let N := 2 ^ Nat.log 2 (K * ⌈Real.sqrt (k : ℝ)⌉₊)
  let L := Real.log (2 * (k : ℝ))

  have hK : 2 ≤ K := sealK_ge_two k
  have hk_r : (2 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hL_pos : 0 < L := by refine Real.log_pos ?_; exact_mod_cast (by omega : 1 < 2 * k)

  have hE_pos : 0 ≤ E := le_trans (by norm_num) hE
  have h_sqrt_k : 2 ≤ ⌈Real.sqrt (k : ℝ)⌉₊ := by
    have h2 : 0 < ⌈Real.sqrt (k : ℝ)⌉₊ := by exact Nat.ceil_pos.mpr (by have := Real.one_le_sqrt hk_r; linarith)
    have h_ceil_le : (⌈Real.sqrt (k : ℝ)⌉₊ : ℝ) ≤ 2 * Real.sqrt (k : ℝ) := by
      have h1 : (⌈Real.sqrt (k : ℝ)⌉₊ : ℝ) < Real.sqrt (k : ℝ) + 1 := Nat.ceil_lt_add_one (Real.sqrt_nonneg _)
      have h2 : (1 : ℝ) ≤ Real.sqrt (k : ℝ) := Real.one_le_sqrt.mpr (by linarith)
      linarith
    have hk_ceil_pos : 0 < sealK k * ⌈Real.sqrt (k : ℝ)⌉₊ := by
      have h1 : 0 < sealK k := by exact_mod_cast (le_trans (by norm_num : 1 ≤ 2) hK)
      exact mul_pos h1 h2
    have hN1 : (2 ^ Nat.log 2 (sealK k * ⌈Real.sqrt (k : ℝ)⌉₊) : ℝ) ≤ (sealK k : ℝ) * (⌈Real.sqrt (k : ℝ)⌉₊ : ℝ) := by
      have := Nat.pow_log_le_self 2 (ne_of_gt hk_ceil_pos)
      exact_mod_cast this
    have h_N_le2 : (2 ^ Nat.log 2 (sealK k * ⌈Real.sqrt (k : ℝ)⌉₊) : ℝ) ≤ (sealK k : ℝ) * 2 * Real.sqrt (k : ℝ) := by
      calc (2 ^ Nat.log 2 (sealK k * ⌈Real.sqrt (k : ℝ)⌉₊) : ℝ) ≤ (sealK k : ℝ) * (⌈Real.sqrt (k : ℝ)⌉₊ : ℝ) := hN1
        _ ≤ (sealK k : ℝ) * (2 * Real.sqrt (k : ℝ)) := mul_le_mul_of_nonneg_left h_ceil_le (by positivity)
        _ = (sealK k : ℝ) * 2 * Real.sqrt (k : ℝ) := by ring
    have h_logN : Real.log (2 ^ Nat.log 2 (sealK k * ⌈Real.sqrt (k : ℝ)⌉₊)) ≤ Real.log ((sealK k : ℝ) * 2 * Real.sqrt (k : ℝ)) := Real.log_le_log (by positivity) h_N_le2
    have h_log_prod : Real.log ((sealK k : ℝ) * 2 * Real.sqrt (k : ℝ)) = Real.log (sealK k) + Real.log 2 + 1/2 * Real.log (k : ℝ) := by
      rw [Real.log_mul (by positivity) (by positivity), Real.log_mul (by positivity) (by positivity), Real.log_sqrt (by positivity)]
      ring
    have h_log_k : Real.log (k : ℝ) = Real.log (2 * (k : ℝ)) - Real.log 2 := by
      have h_prod : Real.log (2 * (k : ℝ)) = Real.log 2 + Real.log (k : ℝ) := Real.log_mul (by norm_num) (by positivity)
      linarith
    have h_logb_diff : Real.logb 2 (2 ^ Nat.log 2 (sealK k * ⌈Real.sqrt (k : ℝ)⌉₊)) - Real.logb 2 (sealK k) = (Real.log (2 ^ Nat.log 2 (sealK k * ⌈Real.sqrt (k : ℝ)⌉₊)) - Real.log (sealK k)) / Real.log 2 := by rw [Real.logb, Real.logb]; ring
    have h_log_diff_le : Real.log (2 ^ Nat.log 2 (sealK k * ⌈Real.sqrt (k : ℝ)⌉₊)) - Real.log (sealK k) ≤ Real.log 2 + 1/2 * (Real.log (2 * (k : ℝ)) - Real.log 2) := by linarith
    have h_div_le : (Real.log (2 ^ Nat.log 2 (sealK k * ⌈Real.sqrt (k : ℝ)⌉₊)) - Real.log (sealK k)) / Real.log 2 ≤ (Real.log 2 + 1/2 * (Real.log (2 * (k : ℝ)) - Real.log 2)) / Real.log 2 := div_le_div_of_nonneg_right h_log_diff_le (by linarith [Real.log_two_gt_d9])
    have ht2 : 1/2 * (Real.log (2 * (k : ℝ)) - Real.log 2) + 3 * Real.log 2 = 1/2 * (Real.log (2 * (k : ℝ)) + 5 * Real.log 2) := by ring
    have h1 : Real.log (2 * (k : ℝ)) + 5 * Real.log 2 ≤ 5772 / 1000 * Real.log (2 * (k : ℝ)) * Real.log 2 := by
      have ht : 2 * (693147 / 1000000) ≤ Real.log (2 * (k : ℝ)) := by
        have h2 : 6931471803 / 10000000000 ≤ Real.log 2 := by have h := Real.log_two_gt_d9; linarith
        have : Real.log 4 ≤ Real.log (2 * (k : ℝ)) := Real.log_le_log (by norm_num) (by exact_mod_cast (by omega : 4 ≤ 2 * k))
        have h4 : Real.log 4 = 2 * Real.log 2 := by rw [show (4:ℝ)=2^2 by norm_num, Real.log_pow]; norm_num
        linarith
      nlinarith [Real.log_two_gt_d9, Real.log_two_lt_d9]
    have ht3 : 1/2 * (Real.log (2 * (k : ℝ)) + 5 * Real.log 2) ≤ 1/2 * (5772 / 1000 * Real.log (2 * (k : ℝ)) * Real.log 2) := by linarith
    have ht4 : 1/2 * (5772 / 1000 * Real.log (2 * (k : ℝ)) * Real.log 2) = 2886 / 1000 * Real.log (2 * (k : ℝ)) * Real.log 2 := by ring
    have ht5 : 1/2 * (Real.log (2 * (k : ℝ)) - Real.log 2) + 3 * Real.log 2 ≤ 2886 / 1000 * Real.log (2 * (k : ℝ)) * Real.log 2 := by linarith
    have ht6 : (1/2 * (Real.log (2 * (k : ℝ)) - Real.log 2) + 3 * Real.log 2) / Real.log 2 ≤ (2886 / 1000 * Real.log (2 * (k : ℝ)) * Real.log 2) / Real.log 2 := div_le_div_of_nonneg_right ht5 (by linarith [Real.log_two_gt_d9])
    have ht7 : (1/2 * (Real.log (2 * (k : ℝ)) - Real.log 2) + 3 * Real.log 2) / Real.log 2 = (Real.log 2 + 1/2 * (Real.log (2 * (k : ℝ)) - Real.log 2)) / Real.log 2 + 2 := by
      have : Real.log 2 ≠ 0 := by positivity
      field_simp; ring
    have ht8 : (2886 / 1000 * Real.log (2 * (k : ℝ)) * Real.log 2) / Real.log 2 = 2886 / 1000 * Real.log (2 * (k : ℝ)) := by
      have : Real.log 2 ≠ 0 := by positivity
      field_simp; ring
    linarith
  have hk2 : 2 * 2 ≤ k := by linarith
  exact Nat.ceil_le_ceil (Real.sqrt_le_sqrt (by exact_mod_cast hk2)) |>.trans (by norm_num)

  have hN : K ≤ N := by
    have h1 : sealK k * 1 ≤ sealK k * ⌈Real.sqrt (k : ℝ)⌉₊ := Nat.mul_le_mul_left (sealK k) h_sqrt_k
    have h2 : sealK k ≤ 2 ^ Nat.log 2 (sealK k) := Nat.le_pow_log (by norm_num : 1 < 2) (by exact_mod_cast (le_trans (by norm_num : 0 ≤ 2) hK))
    have h3 : 2 ^ Nat.log 2 (sealK k) ≤ 2 ^ Nat.log 2 (sealK k * ⌈Real.sqrt (k : ℝ)⌉₊) := Nat.pow_le_pow_right (by norm_num : 0 < 2) (Nat.log_mono h1)
    linarith
  have hN_one : 1 ≤ N := le_trans (by omega) hN

  have h_logbK : Real.logb 2 K + 1 ≤ 2972 / 1000 * L := logbK_bound k hk
  have h_sqrt : Real.sqrt (2 * (1 + Real.log K)) ≤ 2915 / 1000 * L := sqrt_bound k hk
  have h_logbN_raw := logbN_bound k hk
  have h_logbN_cast : Real.logb 2 (N : ℝ) - Real.logb 2 (K : ℝ) + 2 ≤ 2886 / 1000 * Real.log (2 * (k : ℝ)) := by
    exact_mod_cast h_logbN_raw
  have h_logbN : Real.logb 2 N - Real.logb 2 K + 2 ≤ 2886 / 1000 * L := h_logbN_cast

"""

    with open('ScratchX.lean', 'w') as f:
        f.write(content[:start_idx] + new_block + content[end_idx:])
        
