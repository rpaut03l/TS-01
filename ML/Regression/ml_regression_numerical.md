# 🔢 ML Regression: NUMERICAL

### *Rules first → then solve. Every step shown.*

> **Nav:** [← INDEX](../ml_master_gap_index.md) | [📖 THEORY](ml_regression_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_regression_practice.md)

---

## 📦 ALL FORMULAS

```
┌──────────────────────────────────────────────────────────────┐
│ SLR:   β̂₁ = Σ(xᵢ−x̄)(yᵢ−ȳ) / Σ(xᵢ−x̄)²                        │
│        β̂₀ = ȳ − β̂₁ x̄                                         │
│                                                               │
│ MLR:   β̂  = (Xᵀ X)⁻¹ Xᵀ y                                    │
│ RIDGE: β̂  = (Xᵀ X + λ I)⁻¹ Xᵀ y                              │
│                                                               │
│ MSE  = (1/n) Σ (yᵢ − ŷᵢ)²                                    │
│ RMSE = √MSE                                                   │
│ MAE  = (1/n) Σ |yᵢ − ŷᵢ|                                     │
│ R²   = 1 − SS_res / SS_tot                                    │
│          SS_res = Σ (yᵢ − ŷᵢ)²                                │
│          SS_tot = Σ (yᵢ − ȳ)²                                │
│                                                               │
│ LOGISTIC: σ(z) = 1 / (1 + e^(−z))                            │
│        log-odds  = log(p/(1−p)) = wᵀx + b                    │
│        log loss  = −(1/n) Σ [y log p̂ + (1−y) log(1−p̂)]       │
└──────────────────────────────────────────────────────────────┘
```

---

## P1: Simple Linear Regression — Hand Fit

```
DATA
  x = [1, 2, 3, 4, 5]
  y = [2, 4, 5, 4, 5]

STEP 1 — Means
  x̄ = 15/5 = 3
  ȳ = 20/5 = 4

STEP 2 — Deviations and products
  xᵢ − x̄ : −2 −1  0  1  2
  yᵢ − ȳ : −2  0  1  0  1
  (xᵢ−x̄)(yᵢ−ȳ) :  4   0   0   0   2    Σ = 6
  (xᵢ−x̄)²      :  4   1   0   1   4    Σ = 10

STEP 3 — Slope and intercept
  β̂₁ = 6 / 10 = 0.60
  β̂₀ = 4 − 0.60·3 = 4 − 1.8 = 2.20

MODEL:   ŷ = 2.2 + 0.6 x

STEP 4 — R²
  ŷ : 2.8  3.4  4.0  4.6  5.2
  SS_res = (2−2.8)² + (4−3.4)² + (5−4.0)² + (4−4.6)² + (5−5.2)²
         = 0.64 + 0.36 + 1.00 + 0.36 + 0.04 = 2.40
  SS_tot = (2−4)² + (4−4)² + (5−4)² + (4−4)² + (5−4)²
         =  4 + 0 + 1 + 0 + 1 = 6
  R² = 1 − 2.4/6 = 1 − 0.4 = 0.60
```

[↑ Back to Top](#-ml-regression-numerical)

---

## P2: Multiple Linear Regression via Normal Equation

```
PROBLEM: fit y ≈ β₀ + β₁ x₁ + β₂ x₂

DATA
       x₁  x₂   y
  i=1:  1   1   6
  i=2:  1   2   8
  i=3:  2   2  11
  i=4:  2   3  14

DESIGN MATRIX X (with intercept column of 1s):
      [1 1 1]
      [1 1 2]
      [1 2 2]
      [1 2 3]

STEP 1 — Compute Xᵀ X
  Xᵀ X = [ 4   6   8 ]
         [ 6  10  13 ]
         [ 8  13  18 ]

  (Row 1 = sums of 1·1, 1·x₁, 1·x₂ over i
   Row 2 = sums of x₁·1, x₁², x₁·x₂
   Row 3 = sums of x₂·1, x₁·x₂, x₂²)

STEP 2 — Compute Xᵀ y
  y = [6, 8, 11, 14]
  Xᵀ y = [ 39 ]
         [ 64 ]
         [ 86 ]

STEP 3 — Solve (Xᵀ X) β = Xᵀ y by elimination
  Augmented:
    [ 4   6   8 |  39 ]
    [ 6  10  13 |  64 ]
    [ 8  13  18 |  86 ]

  R2 ← R2 − (6/4)R1,  R3 ← R3 − (8/4)R1
    [ 4   6   8 | 39 ]
    [ 0   1   1 |  5.5 ]
    [ 0   1   2 |  8   ]

  R3 ← R3 − R2
    [ 4   6   8 | 39 ]
    [ 0   1   1 |  5.5 ]
    [ 0   0   1 |  2.5 ]

BACK-SUBSTITUTE:
  β₂ = 2.5
  β₁ = 5.5 − 2.5 = 3.0
  β₀ = (39 − 6·3.0 − 8·2.5) / 4 = (39 − 18 − 20) / 4 = 0.25

MODEL:   ŷ = 0.25 + 3.0 x₁ + 2.5 x₂

SANITY CHECK (predictions):
  i=1: 0.25 + 3 + 2.5 = 5.75   (actual 6)
  i=2: 0.25 + 3 + 5.0 = 8.25   (actual 8)
  i=3: 0.25 + 6 + 5.0 = 11.25  (actual 11)
  i=4: 0.25 + 6 + 7.5 = 13.75  (actual 14)
  Small residuals → good fit.
```

[↑ Back to Top](#-ml-regression-numerical)

---

## P3: Ridge vs OLS — one-feature sanity check

```
PROBLEM: fit y = wx (no intercept), n=3 points.
  x = [1, 2, 3],  y = [1, 2, 2]

OLS (λ = 0):
  ŵ = Σ xy / Σ x² = (1·1 + 2·2 + 3·2) / (1 + 4 + 9)
     = (1 + 4 + 6) / 14
     = 11 / 14  ≈ 0.786

RIDGE (λ = 5):
  ŵ = Σ xy / (Σ x² + λ) = 11 / (14 + 5) = 11 / 19 ≈ 0.579

OBSERVE: Ridge shrinks the coefficient toward 0. Larger λ → smaller ŵ.

SAME IDEA IN MATRIX FORM:
  (XᵀX + λI)⁻¹ XᵀY = scalar version above.
```

[↑ Back to Top](#-ml-regression-numerical)

---

## P4: Compute R², Adjusted R², MSE, MAE

```
y       = [10, 12, 14, 16, 18]
ŷ       = [11, 11, 15, 15, 19]
residuals (y − ŷ) : −1, +1, −1, +1, −1

STEP 1 — Residual sums
  Σ |e| = 1 + 1 + 1 + 1 + 1 = 5
  Σ e² = 1 + 1 + 1 + 1 + 1 = 5

STEP 2 — Mean of y
  ȳ = (10+12+14+16+18)/5 = 70/5 = 14

STEP 3 — SS_tot
  (y−ȳ)² : 16, 4, 0, 4, 16   → Σ = 40

STEP 4 — Metrics
  MSE  = 5 / 5 = 1.0
  RMSE = 1.0
  MAE  = 5 / 5 = 1.0
  R²   = 1 − 5/40 = 1 − 0.125 = 0.875

STEP 5 — Adjusted R² (assume p = 2 features)
  n = 5, p = 2
  Adj R² = 1 − (1 − 0.875) · (n−1) / (n−p−1)
         = 1 − 0.125 · 4 / 2
         = 1 − 0.25
         = 0.75
```

[↑ Back to Top](#-ml-regression-numerical)

---

## P5: Logistic Regression — hand forward pass

```
WEIGHTS (given):  w = [0.5, -1.0],  b = 0.2

INPUT:  x = [2, 1],  true label y = 1

STEP 1 — Linear combination
  z = wᵀx + b = 0.5·2 + (−1.0)·1 + 0.2 = 1.0 − 1.0 + 0.2 = 0.2

STEP 2 — Sigmoid
  σ(0.2) = 1 / (1 + e^(−0.2))
         = 1 / (1 + 0.8187)
         = 1 / 1.8187
         ≈ 0.5498
  ⟹ p̂ = 0.5498 (model thinks 55% chance of class 1)

STEP 3 — Log loss for this one example
  L = −[ y log p̂ + (1−y) log(1−p̂) ]
    = −[ 1·log(0.5498) + 0·log(0.4502) ]
    = −log(0.5498)
    = 0.5981

STEP 4 — Gradients
  ∂L/∂z = p̂ − y = 0.5498 − 1 = −0.4502
  ∂L/∂w = (p̂−y) · x = −0.4502·[2, 1] = [−0.9004, −0.4502]
  ∂L/∂b = (p̂−y) = −0.4502
```

[↑ Back to Top](#-ml-regression-numerical)

---

## P6: Interpreting a Logistic Coefficient (odds ratio)

```
Fitted model:  logit(p) = −2.0 + 0.8·age + 0.5·income

QUESTION: What does w_age = 0.8 mean?

ONE-UNIT INCREASE in age multiplies ODDS by:
  e^(0.8) ≈ 2.2255

INTERPRETATION:
  Each extra year of age → odds of positive class go up by ~123%.

If current p = 0.2 (odds = 0.25), after age += 1:
  new odds  = 0.25 · 2.2255 ≈ 0.556
  new p     = 0.556 / (1 + 0.556) ≈ 0.357
```

[↑ Back to Top](#-ml-regression-numerical)

---

## P7: VIF (multicollinearity detector)

```
REGRESS x_j on the OTHER predictors. Suppose R²_j = 0.93.

RULE:  VIF_j = 1 / (1 − R²_j)

VIF_j = 1 / (1 − 0.93) = 1 / 0.07 ≈ 14.3

INTERPRETATION:
  VIF > 10 → serious multicollinearity.
  Standard error of β̂_j is √14.3 ≈ 3.78 times larger than if x_j
  were uncorrelated with the rest. Drop the feature or use Ridge.
```

[↑ Back to Top](#-ml-regression-numerical)

---

## P8: Lasso zeroing out a feature by hand (soft-thresholding)

```
COORDINATE-WISE LASSO UPDATE (feature j, features standardized):

  w_j  ←  S(  (1/n) Σ xᵢⱼ rᵢ  ,  λ )

where S(z, λ) = sign(z) · max(|z| − λ, 0)     ← soft threshold
      rᵢ = yᵢ − Σ_{k≠j} w_k xᵢₖ   (partial residual)

EXAMPLE:
  Suppose the "unregularized" update gives  z = 0.3.
  λ = 0.1  →  w_j = sign(0.3) · (0.3 − 0.1) = 0.20
  λ = 0.25 →  w_j = sign(0.3) · (0.30 − 0.25) = 0.05
  λ = 0.40 →  |z| < λ  ⟹  w_j = 0   ← FEATURE KILLED
```

This is exactly why Lasso gives sparse solutions: any coordinate whose "desire" is less than λ gets clipped to exactly 0.

[↑ Back to Top](#-ml-regression-numerical)

---

> **Next:** [📖 THEORY](ml_regression_theory.md) · [💻 PRACTICE](ml_regression_practice.md)
>
> *ML · Regression · github.com/rpaut03l/TS-01*
