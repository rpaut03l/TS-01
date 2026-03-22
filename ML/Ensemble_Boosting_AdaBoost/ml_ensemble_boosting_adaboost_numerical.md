# 🔢 Ensemble Boosting & AdaBoost Deep-Dive: NUMERICAL

### *Rules first → then solve. Every step shown. Mind-friendly.*

> **Nav:** [← INDEX](ml_ensemble_boosting_adaboost_index.md) | [📖 THEORY](ml_ensemble_boosting_adaboost_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_ensemble_boosting_adaboost_practice.md)
>
> 🔗 **Related:** [Ch7 NUMERICAL (Géron)](https://github.com/rpaut03l/TS-01/blob/main/ML/Ch07_Ensemble_Learning/ml_ch7_numerical.md)

---

## 📦 ALL FORMULAS — Read This First!

```
┌─────────────────────────────────────────────────────────────────────┐
│ 1. ADABOOST — CORE FORMULAS                                         │
│                                                                     │
│    Initial weights:  wᵢ = 1/n  (n = number of samples)              │
│                                                                     │
│    Weighted error:   rₜ = Σ wᵢ·I(hₜ(xᵢ)≠yᵢ) / Σ wᵢ                   │
│                      (sum of weights of wrong points / total)       │
│                                                                     │
│    Amount of say:    αₜ = ½ × ln((1 − rₜ) / rₜ)                       │
│                      (with learning rate η: αₜ = η × ln(...) )       │
│                                                                     │
│    Weight update:    WRONG →  wᵢ_new = wᵢ × exp(+αₜ)                 │
│                      RIGHT →  wᵢ_new = wᵢ × exp(−αₜ)                 │
│                                                                     │
│    Normalize:        wᵢ = wᵢ / Σⱼ wⱼ                                │
│                                                                     │
│    Final clf:        H(x) = sign( Σₜ αₜ · hₜ(x) )                     │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ 2. ENSEMBLE VOTING ERROR (Binomial)                                 │
│                                                                     │
│    P(ensemble wrong) = Σ_{k > n/2} C(n,k) · pᵏ · (1−p)^(n−k)        │
│    where p = individual error rate, n = number of classifiers       │
│    C(n,k) = n! / (k!(n−k)!)                                         │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ 3. BOOTSTRAP SAMPLING                                               │
│                                                                     │
│    P(point NOT picked in 1 draw)  = (n−1)/n                         │
│    P(point NOT picked in n draws) = ((n−1)/n)^n → e⁻¹ ≈ 0.368       │
│    P(point picked at least once)  ≈ 1 − 0.368 = 0.632 (63.2%)       │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ 4. GMM — BASIC FORMULAS                                             │
│                                                                     │
│    Model:     P(x) = Σₖ πₖ · N(x | μₖ, Σₖ)                            │
│    Gaussian:  N(x|μ,Σ) = 1/√(2π|Σ|) × exp(−½(x−μ)ᵀΣ⁻¹(x−μ))         │
│    Mixing:    Σ πₖ = 1,  πₖ > 0                                      │
│    E-step:    γᵢₖ = πₖ·N(xᵢ|μₖ,Σₖ) / Σⱼ πⱼ·N(xᵢ|μⱼ,Σⱼ)                │
│               (responsibility: how much cluster k "owns" point i)   │
│    M-step:    μₖ = Σᵢ γᵢₖ·xᵢ / Σᵢ γᵢₖ                                │
│               Σₖ = Σᵢ γᵢₖ(xᵢ−μₖ)(xᵢ−μₖ)ᵀ / Σᵢ γᵢₖ                     │
│               πₖ = (Σᵢ γᵢₖ) / n                                      │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ 5. USEFUL CONSTANTS                                                 │
│    ln(2) = 0.693    ln(3) = 1.099    ln(4) = 1.386                  │
│    ln(9) = 2.197    e⁰·⁵ = 1.649    e⁻⁰·⁵ = 0.607                   │
│    e¹·⁰ = 2.718    e⁻¹·⁰ = 0.368    e⁰ = 1                          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🗺️ Problem Index

| # | Problem | Key Concept | Difficulty |
|---|---------|-------------|------------|
| P1 | Bagging vs Boosting comparison | Conceptual | ⭐ |
| P2 | Compute α from error rate | Amount of Say | ⭐⭐ |
| P3 | Decision stump on chest pain data | Find best stump + error | ⭐⭐ |
| P4 | Full AdaBoost Round 1 (5 samples) | Complete pipeline | ⭐⭐⭐ |
| P5 | AdaBoost Round 2 (continuation) | Weight update + new stump | ⭐⭐⭐ |
| P6 | GMM responsibility calculation | E-step basics | ⭐⭐ |

---

## P1: Bagging vs Boosting — When Does Each Shine?

### Problem

You have a model with high variance (overfitting). Another model has high bias (underfitting). Which ensemble method helps each?

### Solution

```
STEP 1: Identify the problem type

  High VARIANCE (overfitting):
    Model memorizes training data, fails on new data
    Predictions change wildly with different training sets
    → Need to STABILIZE predictions

  High BIAS (underfitting):
    Model is too simple, misses patterns
    Predictions are consistently wrong in the same direction
    → Need to IMPROVE accuracy on hard examples

STEP 2: Match to ensemble method

  High VARIANCE → BAGGING
    WHY: Each bag sees different 63.2% of data
         Averaging many different models cancels out noise
         Result: smoother, more stable predictions
    EXAMPLE: Random Forest (bagging of trees)

  High BIAS → BOOSTING
    WHY: Each new model focuses on MISTAKES of previous ones
         Progressively reduces systematic errors
         Result: stronger model that captures harder patterns
    EXAMPLE: AdaBoost, Gradient Boosting

ANSWER:
  Overfitting → Bagging (reduces variance)
  Underfitting → Boosting (reduces bias)
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-numerical)

---

## P2: Compute Amount of Say (α)

### Problem

Three weak classifiers have error rates: r₁ = 0.1, r₂ = 0.3, r₃ = 0.5. Compute the amount of say (α) for each. Learning rate η = 1 (default).

### Solution

```
FORMULA: αₜ = ½ × ln((1 − rₜ) / rₜ)

CLASSIFIER 1 (r₁ = 0.1):
─────────────────────────
  α₁ = ½ × ln((1 − 0.1) / 0.1)
     = ½ × ln(0.9 / 0.1)
     = ½ × ln(9)
     = ½ × 2.197
     = 1.099 ✅

  MEANING: High say! Low error → this classifier is trusted a lot.

CLASSIFIER 2 (r₂ = 0.3):
─────────────────────────
  α₂ = ½ × ln((1 − 0.3) / 0.3)
     = ½ × ln(0.7 / 0.3)
     = ½ × ln(2.333)
     = ½ × 0.847
     = 0.424 ✅

  MEANING: Moderate say. Some errors, but still useful.

CLASSIFIER 3 (r₃ = 0.5):
─────────────────────────
  α₃ = ½ × ln((1 − 0.5) / 0.5)
     = ½ × ln(0.5 / 0.5)
     = ½ × ln(1)
     = ½ × 0
     = 0.000 ✅

  MEANING: ZERO say! Error = 50% = random coin flip → ignored!

SUMMARY TABLE:
  ┌────────┬──────────┬──────────┬───────────────────────┐
  │  Clf   │ Error rₜ │    αₜ    │ Interpretation         │
  ├────────┼──────────┼──────────┼───────────────────────┤
  │   1    │  0.10    │  1.099   │ Strong voice          │
  │   2    │  0.30    │  0.424   │ Moderate voice        │
  │   3    │  0.50    │  0.000   │ Ignored (random)      │
  └────────┴──────────┴──────────┴───────────────────────┘
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-numerical)

---

## P3: Decision Stump on Chest Pain Data

### Problem

Given the dataset below, find the best decision stump and its error.

| Patient | Chest Pain | Weight | Blocked Arteries | Label (Heart Disease?) |
|---------|-----------|--------|-----------------|----------------------|
| 1 | Yes | 205 | Yes | Yes (+1) |
| 2 | No | 180 | Yes | Yes (+1) |
| 3 | Yes | 210 | No | Yes (+1) |
| 4 | Yes | 167 | Yes | Yes (+1) |
| 5 | No | 156 | No | No (-1) |
| 6 | No | 125 | No | No (-1) |
| 7 | Yes | 220 | No | No (-1) |
| 8 | No | 145 | No | No (-1) |

Initial weights: wᵢ = 1/8 = 0.125 each.

### Solution

```
STEP 1: Try each feature as a stump and count errors

STUMP A: "Chest Pain = Yes → +1, No → -1"
─────────────────────────────────────────
  Patient 1: Chest=Yes → predict +1, actual +1  ✓
  Patient 2: Chest=No  → predict -1, actual +1  ✗ (wrong!)
  Patient 3: Chest=Yes → predict +1, actual +1  ✓
  Patient 4: Chest=Yes → predict +1, actual +1  ✓
  Patient 5: Chest=No  → predict -1, actual -1  ✓
  Patient 6: Chest=No  → predict -1, actual -1  ✓
  Patient 7: Chest=Yes → predict +1, actual -1  ✗ (wrong!)
  Patient 8: Chest=No  → predict -1, actual -1  ✓

  Wrong: Patient 2, Patient 7
  Weighted error = (0.125 + 0.125) / 1.0 = 0.250


STUMP B: "Blocked Arteries = Yes → +1, No → -1"
─────────────────────────────────────────
  Patient 1: Blocked=Yes → +1, actual +1  ✓
  Patient 2: Blocked=Yes → +1, actual +1  ✓
  Patient 3: Blocked=No  → -1, actual +1  ✗
  Patient 4: Blocked=Yes → +1, actual +1  ✓
  Patient 5: Blocked=No  → -1, actual -1  ✓
  Patient 6: Blocked=No  → -1, actual -1  ✓
  Patient 7: Blocked=No  → -1, actual -1  ✓
  Patient 8: Blocked=No  → -1, actual -1  ✓

  Wrong: Patient 3
  Weighted error = 0.125 / 1.0 = 0.125


STUMP C: "Weight > 170 → +1, ≤ 170 → -1"  (try a threshold)
─────────────────────────────────────────
  P1: 205>170 → +1, actual +1  ✓
  P2: 180>170 → +1, actual +1  ✓
  P3: 210>170 → +1, actual +1  ✓
  P4: 167≤170 → -1, actual +1  ✗
  P5: 156≤170 → -1, actual -1  ✓
  P6: 125≤170 → -1, actual -1  ✓
  P7: 220>170 → +1, actual -1  ✗
  P8: 145≤170 → -1, actual -1  ✓

  Wrong: Patient 4, Patient 7
  Weighted error = (0.125 + 0.125) / 1.0 = 0.250


STEP 2: PICK BEST STUMP (lowest error)

  ┌──────────────────┬────────────────┐
  │ Stump            │ Weighted Error │
  ├──────────────────┼────────────────┤
  │ Chest Pain       │ 0.250          │
  │ Blocked Arteries │ 0.125  ← BEST  │
  │ Weight > 170     │ 0.250          │
  └──────────────────┴────────────────┘

  WINNER: Stump B (Blocked Arteries), error = 0.125

STEP 3: Compute α for winning stump

  α = ½ × ln((1 − 0.125) / 0.125)
    = ½ × ln(0.875 / 0.125)
    = ½ × ln(7)
    = ½ × 1.946
    = 0.973 ✅

  This stump has a HIGH amount of say (error was low).
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-numerical)

---

## P4: Full AdaBoost Round 1 (5 Samples)

### Problem

Train one round of AdaBoost on this tiny dataset:

| i | x₁ | x₂ | y |
|---|----|----|---|
| 1 | 1 | 2 | +1 |
| 2 | 2 | 1 | +1 |
| 3 | 3 | 3 | -1 |
| 4 | 4 | 2 | -1 |
| 5 | 5 | 4 | -1 |

Show all steps: initial weights, best stump, error, α, weight update.

### Solution

```
STEP 1: INITIAL WEIGHTS
────────────────────────
  n = 5, so wᵢ = 1/5 = 0.200 for all

  w = [0.200, 0.200, 0.200, 0.200, 0.200]

STEP 2: FIND BEST STUMP
────────────────────────
  Try stump: "x₁ ≤ 2.5 → +1, x₁ > 2.5 → -1"
    P1: x₁=1 ≤ 2.5 → +1, actual +1  ✓
    P2: x₁=2 ≤ 2.5 → +1, actual +1  ✓
    P3: x₁=3 > 2.5 → -1, actual -1  ✓
    P4: x₁=4 > 2.5 → -1, actual -1  ✓
    P5: x₁=5 > 2.5 → -1, actual -1  ✓
    Errors: 0
    Weighted error = 0/1.0 = 0.000 ← PERFECT!

  NOTE: In practice, if error = 0, AdaBoost stops early.
  For teaching, let's use a slightly imperfect stump instead.

  Try stump: "x₂ ≤ 2.5 → +1, x₂ > 2.5 → -1"
    P1: x₂=2 ≤ 2.5 → +1, actual +1  ✓
    P2: x₂=1 ≤ 2.5 → +1, actual +1  ✓
    P3: x₂=3 > 2.5 → -1, actual -1  ✓
    P4: x₂=2 ≤ 2.5 → +1, actual -1  ✗ ← WRONG!
    P5: x₂=4 > 2.5 → -1, actual -1  ✓
    Errors: P4
    Weighted error = 0.200 / 1.000 = 0.200

  USE STUMP: "x₂ ≤ 2.5 → +1, else -1" with r₁ = 0.200

STEP 3: COMPUTE α₁
────────────────────────
  α₁ = ½ × ln((1 − 0.200) / 0.200)
     = ½ × ln(0.8 / 0.2)
     = ½ × ln(4)
     = ½ × 1.386
     = 0.693 ✅

STEP 4: UPDATE WEIGHTS
────────────────────────
  exp(+α₁) = exp(0.693) = 2.000  (for WRONG points)
  exp(−α₁) = exp(-0.693) = 0.500 (for RIGHT points)

  P1: ✓ correct → 0.200 × 0.500 = 0.100
  P2: ✓ correct → 0.200 × 0.500 = 0.100
  P3: ✓ correct → 0.200 × 0.500 = 0.100
  P4: ✗ WRONG  → 0.200 × 2.000 = 0.400  ← DOUBLED!
  P5: ✓ correct → 0.200 × 0.500 = 0.100

  Before normalize: [0.100, 0.100, 0.100, 0.400, 0.100]
  Sum = 0.100 + 0.100 + 0.100 + 0.400 + 0.100 = 0.800

STEP 5: NORMALIZE
────────────────────────
  P1: 0.100 / 0.800 = 0.125
  P2: 0.100 / 0.800 = 0.125
  P3: 0.100 / 0.800 = 0.125
  P4: 0.400 / 0.800 = 0.500  ← 4× heavier than others!
  P5: 0.100 / 0.800 = 0.125

  Final weights: [0.125, 0.125, 0.125, 0.500, 0.125]
  Sum check: 0.125×4 + 0.500 = 1.000 ✅

SUMMARY:
  ┌────┬───────┬────────────┬────────────────┐
  │  i │  yᵢ   │ Prediction │ New weight wᵢ  │
  ├────┼───────┼────────────┼────────────────┤
  │  1 │  +1   │   +1  ✓    │ 0.125          │
  │  2 │  +1   │   +1  ✓    │ 0.125          │
  │  3 │  -1   │   -1  ✓    │ 0.125          │
  │  4 │  -1   │   +1  ✗    │ 0.500 ← focus! │
  │  5 │  -1   │   -1  ✓    │ 0.125          │
  └────┴───────┴────────────┴────────────────┘

  Stump 1: "x₂ ≤ 2.5 → +1", α₁ = 0.693
  Next round: the new stump MUST get P4 right
  (because P4 now has 50% of the total weight!)
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-numerical)

---

## P5: AdaBoost Round 2 (Continuation of P4)

### Problem

Continue from P4. With new weights [0.125, 0.125, 0.125, 0.500, 0.125], find the next best stump and update weights again.

### Solution

```
CURRENT WEIGHTS: [0.125, 0.125, 0.125, 0.500, 0.125]

STEP 1: FIND BEST STUMP FOR ROUND 2
────────────────────────────────────
  Stump must get P4 right (it has weight 0.500 = half!)

  P4: x₁=4, x₂=2, y=-1

  Try: "x₁ > 3.5 → -1, x₁ ≤ 3.5 → +1"
    P1: x₁=1 ≤ 3.5 → +1, actual +1  ✓
    P2: x₁=2 ≤ 3.5 → +1, actual +1  ✓
    P3: x₁=3 ≤ 3.5 → +1, actual -1  ✗ (weight 0.125)
    P4: x₁=4 > 3.5 → -1, actual -1  ✓ (weight 0.500 → counted correct!)
    P5: x₁=5 > 3.5 → -1, actual -1  ✓

    Weighted error = w₃ / sum = 0.125 / 1.000 = 0.125

STEP 2: COMPUTE α₂
────────────────────
  α₂ = ½ × ln((1 − 0.125) / 0.125)
     = ½ × ln(7)
     = ½ × 1.946
     = 0.973 ✅

STEP 3: UPDATE WEIGHTS
───────────────────────
  exp(+α₂) = exp(0.973) = 2.646  (wrong)
  exp(−α₂) = exp(-0.973) = 0.378 (right)

  P1: ✓ → 0.125 × 0.378 = 0.047
  P2: ✓ → 0.125 × 0.378 = 0.047
  P3: ✗ → 0.125 × 2.646 = 0.331  ← now P3 is heavy!
  P4: ✓ → 0.500 × 0.378 = 0.189  ← went DOWN (fixed!)
  P5: ✓ → 0.125 × 0.378 = 0.047

  Sum = 0.047 + 0.047 + 0.331 + 0.189 + 0.047 = 0.661

STEP 4: NORMALIZE
──────────────────
  P1: 0.047 / 0.661 = 0.071
  P2: 0.047 / 0.661 = 0.071
  P3: 0.331 / 0.661 = 0.501  ← now P3 is the focus!
  P4: 0.189 / 0.661 = 0.286  ← still heavier than P1/P2/P5
  P5: 0.047 / 0.661 = 0.071

  Weights: [0.071, 0.071, 0.501, 0.286, 0.071]

STEP 5: COMBINED CLASSIFIER SO FAR
────────────────────────────────────
  H(x) = sign( 0.693 × h₁(x) + 0.973 × h₂(x) )

  For new point x = (3, 1):
    h₁: x₂=1 ≤ 2.5 → +1
    h₂: x₁=3 ≤ 3.5 → +1
    H = sign(0.693×(+1) + 0.973×(+1)) = sign(1.666) = +1

  For new point x = (4, 4):
    h₁: x₂=4 > 2.5 → -1
    h₂: x₁=4 > 3.5 → -1
    H = sign(0.693×(-1) + 0.973×(-1)) = sign(-1.666) = -1 ✅
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-numerical)

---

## P6: GMM Responsibility Calculation (E-step)

### Problem

A 1D GMM has K=2 components:
- Component 1: μ₁=2, σ₁=1, π₁=0.5
- Component 2: μ₂=5, σ₂=1, π₂=0.5

Compute the responsibility of each component for point x=3.

### Solution

```
FORMULA (1D Gaussian):
  N(x|μ,σ) = (1/√(2πσ²)) × exp(−(x−μ)² / (2σ²))

STEP 1: Compute N(x=3 | μ₁=2, σ₁=1)
─────────────────────────────────────
  = (1/√(2π×1)) × exp(−(3−2)² / (2×1))
  = (1/√(6.283)) × exp(−1/2)
  = (1/2.507) × exp(−0.5)
  = 0.399 × 0.607
  = 0.242

STEP 2: Compute N(x=3 | μ₂=5, σ₂=1)
─────────────────────────────────────
  = (1/√(2π×1)) × exp(−(3−5)² / (2×1))
  = 0.399 × exp(−4/2)
  = 0.399 × exp(−2)
  = 0.399 × 0.135
  = 0.054

STEP 3: Compute responsibilities (E-step formula)
──────────────────────────────────────────────────
  γ₁ = π₁·N(x|μ₁,σ₁) / [π₁·N(x|μ₁,σ₁) + π₂·N(x|μ₂,σ₂)]
     = (0.5 × 0.242) / (0.5 × 0.242 + 0.5 × 0.054)
     = 0.121 / (0.121 + 0.027)
     = 0.121 / 0.148
     = 0.818 ✅

  γ₂ = π₂·N(x|μ₂,σ₂) / [same denominator]
     = 0.027 / 0.148
     = 0.182 ✅

  Check: γ₁ + γ₂ = 0.818 + 0.182 = 1.000 ✅

INTERPRETATION:
  Point x=3 is 81.8% likely from Component 1 (μ=2)
  and 18.2% likely from Component 2 (μ=5).
  Makes sense! x=3 is much closer to μ₁=2 than μ₂=5.

  This is "SOFT" assignment (vs K-Means which would say 100% Comp 1).
```

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-numerical)

---

## 📊 Quick Reference — Common Calculations

```
ERROR → ALPHA LOOKUP TABLE (α = ½ × ln((1-r)/r)):
─────────────────────────────────
  r = 0.01 → α = 2.298
  r = 0.05 → α = 1.472
  r = 0.10 → α = 1.099
  r = 0.15 → α = 0.867
  r = 0.20 → α = 0.693
  r = 0.25 → α = 0.549
  r = 0.30 → α = 0.424
  r = 0.35 → α = 0.310
  r = 0.40 → α = 0.203
  r = 0.45 → α = 0.100
  r = 0.50 → α = 0.000  ← random!
─────────────────────────────────

WEIGHT MULTIPLIER TABLE (exp(α)):
─────────────────────────────────
  α = 0.5  → exp(+α)=1.649, exp(-α)=0.607
  α = 0.7  → exp(+α)=2.014, exp(-α)=0.497
  α = 1.0  → exp(+α)=2.718, exp(-α)=0.368
  α = 1.1  → exp(+α)=3.004, exp(-α)=0.333
─────────────────────────────────
```

---

> **Nav:** [← INDEX](ml_ensemble_boosting_adaboost_index.md) | [📖 THEORY](ml_ensemble_boosting_adaboost_theory.md) | 🔢 NUMERICAL | [💻 PRACTICE →](ml_ensemble_boosting_adaboost_practice.md)

[↑ Back to Top](#-ensemble-boosting--adaboost-deep-dive-numerical)

---

*AI · ML · github.com/rpaut03l/TS-01-Pvt*
