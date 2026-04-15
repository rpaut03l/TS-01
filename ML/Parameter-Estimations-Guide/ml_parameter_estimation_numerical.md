# 🔢 ML Parameter Estimation: NUMERICAL

### *Rules first → then solve. Every step shown.*

> **Nav:** [← INDEX](../ml_master_gap_index.md) | [📖 THEORY](ml_parameter_estimation_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_parameter_estimation_practice.md)

---

## 📦 ALL FORMULAS

```
┌──────────────────────────────────────────────────────────────────┐
│ MLE BERNOULLI:   θ̂ = k / n                                       │
│ MLE GAUSSIAN μ:  μ̂ = (1/n) Σ xᵢ                                  │
│ MLE GAUSSIAN σ²: σ̂² = (1/n) Σ (xᵢ − x̄)²       (biased)           │
│ UNBIASED σ²:     s² = (1/(n−1)) Σ (xᵢ − x̄)²                      │
│ MLE POISSON:     λ̂ = x̄                                           │
│ MLE EXPONENTIAL: λ̂ = 1 / x̄                                       │
│                                                                  │
│ BAYES:           p(θ|D) ∝ p(D|θ) · p(θ)                          │
│ MAP:             θ̂ = argmax [ log p(D|θ) + log p(θ) ]            │
│                                                                  │
│ BETA POSTERIOR:  Beta(α, β) + k/n  →  Beta(α+k, β+n−k)           │
│ BETA MEAN:       α / (α + β)                                     │
│ BETA MODE:       (α − 1) / (α + β − 2)                           │
│                                                                  │
│ GAUSSIAN-GAUSSIAN POSTERIOR (σ² known):                          │
│   μ_post = (σ²·μ₀ + σ₀²·Σxᵢ) / (σ² + n·σ₀²)                      │
│   σ²_post = (σ²·σ₀²) / (σ² + n·σ₀²)                              │
└──────────────────────────────────────────────────────────────────┘
```

---

## P1: MLE of Bernoulli — Coin Flips

```
DATA: 10 flips, observe H,H,T,H,T,H,H,T,H,H  →  k = 7, n = 10

RULE:  θ̂_MLE = k / n

STEP 1 — Likelihood
  L(θ) = θ⁷ · (1−θ)³

STEP 2 — Log-likelihood
  ℓ(θ) = 7 log θ + 3 log(1−θ)

STEP 3 — Differentiate and set to 0
  dℓ/dθ = 7/θ − 3/(1−θ) = 0
  7(1−θ) = 3θ
  7 − 7θ = 3θ
  7 = 10θ
  θ̂_MLE = 0.7 ✓
```

[↑ Back to Top](#-ml-parameter-estimation-numerical)

---

## P2: MLE of Gaussian μ and σ²

```
DATA: X = [2, 4, 4, 4, 5, 5, 7, 9]   (n = 8)

STEP 1 — Sample mean
  x̄ = (2+4+4+4+5+5+7+9)/8 = 40/8 = 5
  ⟹ μ̂_MLE = 5

STEP 2 — Sample variance (MLE, ÷ n)
  (xᵢ − x̄)² :  9, 1, 1, 1, 0, 0, 4, 16
  Σ = 32
  σ̂²_MLE = 32 / 8 = 4
  σ̂_MLE  = 2

STEP 3 — Unbiased variance (÷ n−1)
  s² = 32 / 7 ≈ 4.571
  s  ≈ 2.138

DIFFERENCE: the MLE UNDER-estimates σ² because it uses the estimated
mean instead of the true mean. The ÷(n−1) version is unbiased.
```

[↑ Back to Top](#-ml-parameter-estimation-numerical)

---

## P3: MAP of Bernoulli with Beta(α, β) Prior

```
DATA: n = 10 flips, k = 7 heads
PRIOR: θ ~ Beta(α=2, β=2)   ← weakly biased toward 0.5

RULE:  Posterior = Beta(α + k, β + n − k)
       MAP = mode of Beta = (α − 1) / (α + β − 2)

POSTERIOR
  Beta(2+7, 2+10−7) = Beta(9, 5)

MAP (mode of Beta(9,5))
  θ̂_MAP = (9 − 1) / (9 + 5 − 2) = 8 / 12 = 0.667

MLE for comparison
  θ̂_MLE = 7 / 10 = 0.700

INTERPRETATION
  Prior pulls estimate from 0.700 toward 0.500 → lands at 0.667.
  Equivalent to adding (α−1)=1 fake head and (β−1)=1 fake tail.
```

[↑ Back to Top](#-ml-parameter-estimation-numerical)

---

## P4: Full Bayesian Posterior (Beta) — Compute Mean & Mode

```
PRIOR:  Beta(3, 7)   (biased toward ~0.3)
DATA:   n = 20 flips, k = 12 heads

POSTERIOR:  Beta(3+12, 7+20−12) = Beta(15, 15)

POSTERIOR MEAN:   α / (α+β) = 15 / 30 = 0.500
POSTERIOR MODE:   (α−1)/(α+β−2) = 14/28 = 0.500  (MAP)

MLE (for comparison):  12 / 20 = 0.600

NOTE: Beta(15,15) is symmetric around 0.5 → mean = mode = median.
      The data pulled the prior center (0.3) toward 0.5 but did
      not reach the MLE of 0.6 — the prior had effective sample
      size α+β = 10 to start.
```

[↑ Back to Top](#-ml-parameter-estimation-numerical)

---

## P5: Gaussian-Gaussian Posterior (σ² known)

```
PRIOR:   μ ~ N(μ₀=100, σ₀²=25)    (belief about test scores)
DATA:    n = 4 samples, x̄ = 110, population σ² = 16 known

POSTERIOR (closed form):
  μ_post   = (σ²·μ₀ + σ₀²·Σxᵢ) / (σ² + n·σ₀²)

Σxᵢ = n·x̄ = 4·110 = 440
  μ_post   = (16·100 + 25·440) / (16 + 4·25)
           = (1600 + 11000) / (16 + 100)
           = 12600 / 116
           ≈ 108.62

  σ²_post  = (σ²·σ₀²) / (σ² + n·σ₀²)
           = (16·25) / (16 + 100)
           = 400 / 116
           ≈ 3.45
  σ_post   ≈ 1.857

CHECK: posterior μ ≈ 108.6 lies BETWEEN prior mean (100) and sample
       mean (110), closer to the sample mean because n=4 is large
       enough to mostly swamp the prior of "effective size" σ²/σ₀² ≈ 0.64.
```

[↑ Back to Top](#-ml-parameter-estimation-numerical)

---

## P6: MLE of Poisson λ

```
DATA: Calls per hour = [2, 3, 1, 4, 0, 2, 3]   (n = 7)

RULE:  λ̂_MLE = x̄

STEP 1 — Likelihood
  L(λ) = Π  e^(−λ) · λ^(xᵢ) / xᵢ!
       ∝  e^(−nλ) · λ^(Σxᵢ)

STEP 2 — Log-likelihood
  ℓ(λ) = −nλ + (Σxᵢ) log λ   (+ const)

STEP 3 — Solve dℓ/dλ = 0
  −n + (Σxᵢ)/λ = 0
  λ̂ = Σxᵢ / n = x̄

STEP 4 — Compute
  Σxᵢ = 2+3+1+4+0+2+3 = 15
  λ̂_MLE = 15 / 7 ≈ 2.143 calls/hour
```

[↑ Back to Top](#-ml-parameter-estimation-numerical)

---

## P7: L2 Regularization = Gaussian Prior (Identity)

```
SHOW: MAP estimation of linear-regression weights with a
      Gaussian prior N(0, τ²I) is equivalent to Ridge.

Likelihood (Gaussian noise σ²):
  log p(D | w) = −(1/2σ²) Σ (yᵢ − wᵀxᵢ)²  + const

Prior (Gaussian w ~ N(0, τ²I)):
  log p(w) = −(1/2τ²) ‖w‖²  + const

MAP objective:
  ŵ_MAP = argmin_w  (1/2σ²) Σ (yᵢ − wᵀxᵢ)²  +  (1/2τ²) ‖w‖²

Multiply through by σ²:
  ŵ_MAP = argmin_w  Σ (yᵢ − wᵀxᵢ)²  +  (σ²/τ²) ‖w‖²

Let  λ = σ² / τ²   ⟹   RIDGE REGRESSION!

CONCLUSION:
  Smaller τ² (stronger prior) ⟺ larger λ (stronger regularization).
  Laplace prior would give L1 (Lasso) by the same derivation.
```

[↑ Back to Top](#-ml-parameter-estimation-numerical)

---

## P8: Bias of MLE σ² — Why ÷n is Wrong

```
TRUE MODEL:  xᵢ ~ N(μ, σ²), n samples
CLAIM:        E[σ̂²_MLE] = σ² · (n−1)/n   ≠ σ²

PROOF SKETCH
  σ̂²_MLE = (1/n) Σ (xᵢ − x̄)²

  Σ (xᵢ − x̄)² = Σ (xᵢ − μ)² − n(x̄ − μ)²     (algebra)

  E[Σ(xᵢ−μ)²] = n σ²
  E[n(x̄−μ)²] = n · Var(x̄) = n · σ²/n = σ²

  ⟹  E[Σ(xᵢ−x̄)²] = n σ² − σ² = (n−1) σ²
  ⟹  E[σ̂²_MLE]    = (n−1)/n · σ²       ← biased low

FIX: Divide by (n−1) instead of n  →  UNBIASED.
```

[↑ Back to Top](#-ml-parameter-estimation-numerical)

---

> **Next:** [📖 THEORY](ml_parameter_estimation_theory.md) · [💻 PRACTICE](ml_parameter_estimation_practice.md)
>
> *ML · Parameter Estimation · github.com/rpaut03l/TS-01*
