# 🔢 ML Bayesian Decision Theory: NUMERICAL

### *Rules first → then solve. Every step shown.*

> **Nav:** [← INDEX](../ml_master_gap_index.md) | [📖 THEORY](ml_bdt_theory.md) | 🔢 **NUMERICAL** | [💻 Practice Problems →](bayesian-practice-problems.md) | [📘 Detailed Guide](bayesian_becision_theory_guide.md)

---

## 📦 ALL FORMULAS

```
┌──────────────────────────────────────────────────────────────┐
│ BAYES:       p(ωⱼ|x) = p(x|ωⱼ) p(ωⱼ) / p(x)                  │
│ EVIDENCE:    p(x)    = Σⱼ p(x|ωⱼ) p(ωⱼ)                      │
│                                                              │
│ MAP RULE:    pick ωⱼ that maximizes p(ωⱼ|x)                  │
│              ⟺ maximizes p(x|ωⱼ) p(ωⱼ)                      │
│                                                              │
│ CONDITIONAL RISK:                                            │
│    R(αᵢ|x) = Σⱼ λ(αᵢ|ωⱼ) p(ωⱼ|x)                             │
│    optimal: argmin R(αᵢ|x)                                   │
│                                                              │
│ GAUSSIAN CLASS-COND:                                         │
│    p(x|ωⱼ) = (2π|Σⱼ|)^(−1/2) · exp(−½(x−μⱼ)ᵀΣⱼ⁻¹(x−μⱼ))      │
│                                                              │
│ LOG DISCRIMINANT:                                            │
│    gⱼ(x) = −½(x−μⱼ)ᵀΣⱼ⁻¹(x−μⱼ) − ½ log|Σⱼ| + log p(ωⱼ)       │
│                                                              │
│ LIKELIHOOD RATIO:                                            │
│    L(x) = p(x|ω₁) / p(x|ω₂)                                  │
│    threshold for 0-1 loss: L(x) > p(ω₂)/p(ω₁)                │
│                                                              │
│ BAYES ERROR:  P(e|x) = 1 − max_i p(ωᵢ|x)                     │
└──────────────────────────────────────────────────────────────┘
```

---

## P1: Compute the posterior from prior + likelihood

```
GIVEN: two classes ω₁, ω₂.
  Priors:       p(ω₁) = 0.3,  p(ω₂) = 0.7
  Likelihoods:  p(x|ω₁) = 0.6,  p(x|ω₂) = 0.2

STEP 1 — Joint
  p(x, ω₁) = 0.6 · 0.3 = 0.18
  p(x, ω₂) = 0.2 · 0.7 = 0.14

STEP 2 — Evidence
  p(x) = 0.18 + 0.14 = 0.32

STEP 3 — Posterior
  p(ω₁ | x) = 0.18 / 0.32 = 0.5625
  p(ω₂ | x) = 0.14 / 0.32 = 0.4375

DECISION (0-1 loss): argmax posterior → ω₁  ✓
Note: ω₂ had the larger prior, but the big likelihood flip (0.6 vs 0.2)
was enough to override it.
```

[↑ Back to Top](#-ml-bayesian-decision-theory-numerical)

---

## P2: Equal priors → ML rule

```
Priors: p(ω₁) = p(ω₂) = 0.5
Likelihoods: p(x | ω₁) = 0.4, p(x | ω₂) = 0.6

Because priors are equal, the prior factor cancels:
  argmax p(ωⱼ | x)  =  argmax p(x | ωⱼ)

p(x|ω₁) = 0.4  <  p(x|ω₂) = 0.6  ⟹  decide ω₂.

This is the MAXIMUM LIKELIHOOD rule — a special case of MAP.
```

[↑ Back to Top](#-ml-bayesian-decision-theory-numerical)

---

## P3: Asymmetric loss shifts the boundary

```
Two classes: ω₁ = cancer (rare), ω₂ = healthy (common)
Priors:  p(ω₁) = 0.01, p(ω₂) = 0.99

Loss matrix:
                 ω₁ (cancer)   ω₂ (healthy)
  α₁ = "cancer"   [    0             1      ]
  α₂ = "healthy"  [  100             0      ]

SUPPOSE posterior at x:
  p(ω₁|x) = 0.05,  p(ω₂|x) = 0.95

RISKS
  R(α₁|x) = 0 · 0.05 + 1 · 0.95 = 0.95
  R(α₂|x) = 100 · 0.05 + 0 · 0.95 = 5.00

DECISION: argmin → α₁ "cancer", even though p(ω₁|x) = 5% !

REASON: missing cancer costs 100× as much as a false alarm, so we
flip to "cancer" as soon as p(ω₁|x) > 1/101 ≈ 0.0099.
```

[↑ Back to Top](#-ml-bayesian-decision-theory-numerical)

---

## P4: Likelihood ratio threshold — two Gaussians

```
Two classes, 1-D Gaussian:
  ω₁: N(0, 1)
  ω₂: N(2, 1)
  equal priors, 0-1 loss.

RULE (MAP): decide ω₁ iff  p(x|ω₁) > p(x|ω₂)
            iff  (x−0)² < (x−2)²
            iff  x² < x² − 4x + 4
            iff  4x < 4
            iff  x < 1

So the decision boundary is x = 1 — the midpoint between the means, as expected for equal priors and equal variances.

CLASSIFY x = 1.4:
  p(x|ω₁) = (1/√(2π)) · exp(−½·1.4²) = 0.1497
  p(x|ω₂) = (1/√(2π)) · exp(−½·0.6²) = 0.3332
  ⟹ pick ω₂ ✓

LIKELIHOOD RATIO:
  L = 0.1497 / 0.3332 = 0.449
  Threshold for 0-1 loss: p(ω₂)/p(ω₁) = 1
  L < 1 ⟹ decide ω₂ ✓
```

[↑ Back to Top](#-ml-bayesian-decision-theory-numerical)

---

## P5: Bayes error of the 1D two-Gaussian setup

```
Same classes as P4:  ω₁ = N(0,1), ω₂ = N(2,1), equal priors.

By symmetry the optimal boundary is x = 1.
P(error) = P(class1 & x>1) + P(class2 & x<1)
         = 0.5 · P(X>1 | X ~ N(0,1)) + 0.5 · P(X<1 | X ~ N(2,1))

P(X > 1 | N(0,1)) = 1 − Φ(1) = 1 − 0.8413 = 0.1587
P(X < 1 | N(2,1)) = Φ((1−2)/1) = Φ(−1) = 0.1587

P(error) = 0.5·0.1587 + 0.5·0.1587 = 0.1587

BAYES ERROR = 15.87%.
No classifier can do better on this problem, no matter how fancy.
```

[↑ Back to Top](#-ml-bayesian-decision-theory-numerical)

---

## P6: Two-class Gaussian, unequal priors (boundary shift)

```
Same likelihoods: ω₁ = N(0, 1), ω₂ = N(2, 1)
NEW priors:       p(ω₁) = 0.8, p(ω₂) = 0.2

MAP rule: decide ω₁ iff  p(x|ω₁) p(ω₁) > p(x|ω₂) p(ω₂)
Taking logs and simplifying (shared variance cancels the quadratic):

  (x − 0)² − (x − 2)²  <  2 log( p(ω₁)/p(ω₂) )
  4x − 4               <  2 log(4)
  4x                   <  4 + 2·1.386
  4x                   <  6.773
  x                    <  1.693

So the boundary shifts from 1.0 → 1.693 (to the right) because we
BELIEVE more strongly in ω₁ a priori.
```

[↑ Back to Top](#-ml-bayesian-decision-theory-numerical)

---

## P7: Naive Bayes on a small text-style example

```
Spam vs Ham, simplified features (word presence 0/1):
  "free", "deal", "meeting"

TRAINING COUNTS (with Laplace smoothing):
  Spam: 40 emails. "free" in 30, "deal" in 20, "meeting" in 2.
  Ham:  60 emails. "free" in 5,  "deal" in 10, "meeting" in 45.

ESTIMATED PROBABILITIES  p(word | class):
  p(free | spam)    = (30+1)/(40+2) = 31/42 ≈ 0.738
  p(deal | spam)    = (20+1)/(40+2) = 21/42 = 0.500
  p(meeting | spam) = (2+1)/(40+2)  =  3/42 ≈ 0.071
  p(free | ham)     = (5+1)/(60+2)  =  6/62 ≈ 0.097
  p(deal | ham)     = (10+1)/(60+2) = 11/62 ≈ 0.177
  p(meeting | ham)  = (45+1)/(60+2) = 46/62 ≈ 0.742

PRIORS:  p(spam) = 40/100 = 0.4,  p(ham) = 0.6

TEST EMAIL: "free deal" (no "meeting")
Use log-probs to avoid underflow:

  log p(spam) + log p(free|spam) + log p(deal|spam) + log(1 − p(meeting|spam))
  = log 0.4 + log 0.738 + log 0.500 + log(1 − 0.071)
  = −0.916 + −0.304 + −0.693 + −0.074
  = −1.987

  log p(ham)  + log p(free|ham)  + log p(deal|ham)  + log(1 − p(meeting|ham))
  = log 0.6 + log 0.097 + log 0.177 + log(1 − 0.742)
  = −0.511 + −2.334 + −1.731 + −1.354
  = −5.930

−1.987 > −5.930  →  predict SPAM ✓
```

[↑ Back to Top](#-ml-bayesian-decision-theory-numerical)

---

## P8: Minimum distance classifier (Gaussian, Σ = σ² I)

```
GIVEN: 3 classes, equal priors, Σⱼ = σ² I for all j.
  μ₁ = (1, 2),  μ₂ = (3, 2),  μ₃ = (2, 5)

Discriminant collapses (as shown in §6 Case 1):
  gⱼ(x) = −‖x − μⱼ‖²       (ignoring the 2σ² constant)

CLASSIFY x = (2, 3):
  ‖x−μ₁‖² = (2−1)² + (3−2)² = 1 + 1 = 2
  ‖x−μ₂‖² = (2−3)² + (3−2)² = 1 + 1 = 2    ← tie
  ‖x−μ₃‖² = (2−2)² + (3−5)² = 0 + 4 = 4

Ties between classes 1 and 2; tie-break using priors (all equal here)
or any consistent rule. In practice sklearn picks the first class encountered.

Classify x = (2, 1):
  ‖x−μ₁‖² = 1+1 = 2
  ‖x−μ₂‖² = 1+1 = 2     ← tie again
  ‖x−μ₃‖² = 0+16 = 16

OBSERVATION: in this isotropic-Σ case, the decision boundaries are
the PERPENDICULAR BISECTORS between pairs of means — i.e. a Voronoi
diagram of {μ₁, μ₂, μ₃}.
```

[↑ Back to Top](#-ml-bayesian-decision-theory-numerical)

---

> **Next:** [📖 THEORY](ml_bdt_theory.md) · [💻 Practice Problems](bayesian-practice-problems.md)
>
> *ML · Bayesian Decision Theory · github.com/rpaut03l/TS-01*
