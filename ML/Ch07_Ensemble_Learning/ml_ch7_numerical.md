# 🔢 Ch7 — Ensemble Learning: NUMERICAL
### *Rules first → then solve. Mind-friendly. Every step shown.*

> **Nav:** [← INDEX](./ml_ch7_index.md) | [📖 THEORY](./ml_ch7_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](./ml_ch7_practice.md)

---

## 📦 ALL FORMULAS — Read This First!

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. VOTING ERROR (Binomial)                                      │
│    P(k wrong out of n) = C(n,k) · pᵏ · (1-p)^(n-k)           │
│    Ensemble error = P(majority wrong) = Σ P(k) for k > n/2    │
│    C(n,k) = n! / (k! · (n-k)!)                                 │
├─────────────────────────────────────────────────────────────────┤
│ 2. ADABOOST                                                     │
│    Error rate:  r = (Σ wᵢ for wrong points) / (Σ all wᵢ)     │
│    Clf weight:  α = η · ln((1-r)/r)     [η=learning rate]     │
│    Update rule: wrong → wᵢ × exp(+α)   ← gets bigger         │
│                 right → wᵢ × exp(-α)   ← gets smaller        │
│    Normalize:   divide all wᵢ so they sum to 1                │
│    Final pred:  ŷ = sign( Σ αₜ · hₜ(x) )                     │
├─────────────────────────────────────────────────────────────────┤
│ 3. GRADIENT BOOSTING                                            │
│    Start:    ŷ₀ = mean(y)                                      │
│    Residual: r = y - ŷ_current                                 │
│    Update:   ŷ_new = ŷ_old + η · h_new(x)   [h fits r]       │
│    MSE:      mean( (y - ŷ)² )                                  │
├─────────────────────────────────────────────────────────────────┤
│ 4. OOB (Out-of-Bag)                                             │
│    P(point NOT picked in one draw) = 1 - 1/n                   │
│    P(never picked in n draws) = (1-1/n)ⁿ → 1/e ≈ 0.368       │
│    So ~63.2% points train each tree, ~36.8% are OOB            │
├─────────────────────────────────────────────────────────────────┤
│ 5. SOFT VOTING                                                  │
│    avg_prob[class] = (p₁ + p₂ + p₃) / 3                      │
│    Predict class with highest average probability              │
├─────────────────────────────────────────────────────────────────┤
│ 6. GINI IMPORTANCE (one split)                                  │
│    = (nₚ/n)·Gₚ − (nₗ/n)·Gₗ − (nᵣ/n)·Gᵣ                    │
│    nₚ=parent count, nₗ=left, nᵣ=right, G=Gini score          │
└─────────────────────────────────────────────────────────────────┘
```

> 💡 **Gini reminder:** Gini = 1 − Σ pᵢ²  (0 = pure, 0.5 = worst for 2 classes)
> 💡 **ln vs log:** AdaBoost uses natural log (ln). ln(1)=0, ln(2)≈0.693, ln(e)=1

---

## P1 — Voting: Does Ensemble Beat Individual?

**Given:** 5 classifiers, each 70% accurate (error p=0.30). Majority vote. Find ensemble error.

```
👶 Think: 5 friends voting. Wrong only if 3+ friends are wrong.

FORMULA: P(k wrong) = C(5,k) × 0.30ᵏ × 0.70^(5-k)

C(5,3) = 5!/(3!·2!) = 10
C(5,4) = 5!/(4!·1!) = 5
C(5,5) = 1

k=3: 10 × 0.30³ × 0.70²  =  10 × 0.027 × 0.49  = 0.1323
k=4:  5 × 0.30⁴ × 0.70¹  =   5 × 0.0081 × 0.70 = 0.0284
k=5:  1 × 0.30⁵ × 0.70⁰  =   1 × 0.00243 × 1   = 0.0024

Ensemble error = 0.1323 + 0.0284 + 0.0024 = 0.163 = 16.3%

Individual: 30% error → Ensemble: 16.3% ✅ (nearly halved!)
```

---

## P2 — AdaBoost: Weight Update by Hand

**Given:** 6 points, all start with w = 1/6 ≈ 0.167. After classifier 1: points 3 & 5 are wrong. η=1.

```
👶 Think: wrong students get MORE homework (higher weight). Right ones get a break.

STEP 1 — Error rate r:
  r = (w₃ + w₅) / total = (0.167 + 0.167) / 1.0 = 0.333

STEP 2 — Classifier weight α:
  α = ln((1-r)/r) = ln(0.667/0.333) = ln(2) = 0.693

STEP 3 — exp values:
  exp(+0.693) = 2.0  ← multiply wrong points by this
  exp(-0.693) = 0.5  ← multiply correct points by this

STEP 4 — New weights:
  Point 1: ✅  0.167 × 0.5 = 0.0835
  Point 2: ✅  0.167 × 0.5 = 0.0835
  Point 3: ❌  0.167 × 2.0 = 0.334   ← doubled!
  Point 4: ✅  0.167 × 0.5 = 0.0835
  Point 5: ❌  0.167 × 2.0 = 0.334   ← doubled!
  Point 6: ✅  0.167 × 0.5 = 0.0835
  Total = 0.0835×4 + 0.334×2 = 0.334 + 0.668 = 1.002 ≈ 1

STEP 5 — Normalize (/1.002):
  Correct points:    0.083 each
  Wrong points (3,5): 0.333 each ← 4× heavier than correct ones

WHY? Next classifier will focus hard on points 3 & 5 ✅
```

---

## P3 — AdaBoost: Final Prediction

**Given:** 3 classifiers with α₁=0.693, α₂=0.5, α₃=0.3. For test point x: h₁=+1, h₂=−1, h₃=+1.

```
👶 Think: weighted vote. Higher α = louder voice.

FORMULA: ŷ = sign( α₁·h₁ + α₂·h₂ + α₃·h₃ )

= sign( 0.693×(+1) + 0.5×(−1) + 0.3×(+1) )
= sign( 0.693 − 0.5 + 0.3 )
= sign( 0.493 )
= +1   → Predict Class 1 ✅

Class 1 total weight: 0.693 + 0.3 = 0.993
Class 0 total weight: 0.5
Class 1 wins by 0.493 margin
```

---

## P4 — Gradient Boosting: Residuals by Hand

**Given:** y = [3, 5, 4, 7]. Learning rate η = 0.5. Start: ŷ₀ = mean(y).

```
👶 Think: each tree ONLY fixes the mistakes of the previous prediction.

START:
  ŷ₀ = (3+5+4+7)/4 = 19/4 = 4.75  (just the mean)

ROUND 1 — compute residuals (what we got wrong):
  r₁ = y − ŷ₀ = [3−4.75, 5−4.75, 4−4.75, 7−4.75]
             = [−1.75,   +0.25,  −0.75,  +2.25]

Tree h₂ fits r₁ perfectly → h₂ predicts [−1.75, +0.25, −0.75, +2.25]

Update: ŷ₁ = ŷ₀ + η·h₂
            = 4.75 + 0.5×[−1.75, +0.25, −0.75, +2.25]
            = [4.75−0.875, 4.75+0.125, 4.75−0.375, 4.75+1.125]
            = [3.875, 4.875, 4.375, 5.875]

ROUND 2 — new residuals:
  r₂ = y − ŷ₁ = [3−3.875, 5−4.875, 4−4.375, 7−5.875]
              = [−0.875, +0.125, −0.375, +1.125]

KEY: residuals shrink each round by factor η = 0.5 ✅

MSE check:
  After ŷ₀: (1.75²+0.25²+0.75²+2.25²)/4 = 8.75/4 = 2.1875
  After ŷ₁: (0.875²+0.125²+0.375²+1.125²)/4 = 2.1875/4 = 0.547  ← 4× better!
```

---

## P5 — OOB Fraction

**Given:** 1000 training points. Bootstrap sample of 1000 (with replacement). What fraction is OOB?

```
👶 Think: drawing 1000 names from a hat (putting each back). Some never get drawn.

P(one point NOT drawn in single pick) = 1 − 1/1000 = 0.999
P(NOT drawn in ANY of 1000 picks)     = 0.999¹⁰⁰⁰ = (1−1/n)ⁿ

As n→∞: (1−1/n)ⁿ → 1/e = 0.368

So:
  ~36.8% of points are OOB per tree  (never seen = free validation)
  ~63.2% of points train each tree

For n=1000:  ~368 OOB points per tree
             each tree validated on those 368 it never saw
             → exactly like leave-one-out cross-validation, but FREE ✅
```

---

## P6 — Soft vs Hard Voting Difference

**Given:** 3 classifiers. P(class=1) scores: A=0.51, B=0.51, C=0.02.

```
👶 Think: A and B are barely guessing. C is VERY confident for class 0.

HARD VOTING (just looks at label):
  A: 0.51 > 0.5 → votes class 1
  B: 0.51 > 0.5 → votes class 1
  C: 0.02 < 0.5 → votes class 0
  Result: 2 vs 1 → class 1  ← WRONG! A and B barely confident

SOFT VOTING (uses probabilities):
  avg P(class=1) = (0.51 + 0.51 + 0.02) / 3 = 1.04/3 = 0.347
  0.347 < 0.5 → class 0  ✅ ← correctly trusts C's strong 98% confidence

LESSON: Soft voting is smarter — it uses HOW confident each classifier is.
```

---

## P7 — Gini Feature Importance

**Given:** 1 split on Feature X. Root: 50 samples, Gini=0.5. Left: 30 samples, Gini=0.1. Right: 20 samples, Gini=0.4.

```
👶 Think: how much did this split CLEAN UP the mess (reduce impurity)?

FORMULA: Importance = (nₚ/n)·Gₚ − (nₗ/n)·Gₗ − (nᵣ/n)·Gᵣ

= (50/50)×0.5 − (30/50)×0.1 − (20/50)×0.4
=    1.0×0.5  −    0.6×0.1  −    0.4×0.4
=      0.5    −     0.06    −     0.16
= 0.28

Feature X reduced impurity by 0.28 ← its raw importance

In Random Forest:
  1. Average 0.28-style scores across ALL splits on X, across ALL trees
  2. Divide by total importance of all features → sum to 1.0
  → rf.feature_importances_[X_index]
```

---

## 🃏 FORMULA CARD (Tear-Out)

```
VOTING ERROR:     P(k wrong) = C(n,k)·pᵏ·(1-p)^(n-k); sum for k > n/2
ADABOOST r:       r = Σwᵢ[wrong] / Σwᵢ
ADABOOST α:       α = ln((1-r)/r)
ADABOOST update:  wrong×exp(+α), right×exp(−α), normalize
ADABOOST predict: sign(Σ α·h(x))
GBM residual:     r = y − ŷ_current
GBM update:       ŷ_new = ŷ_old + η·h(x)   where h fits r
OOB fraction:     (1−1/n)ⁿ → 1/e ≈ 0.368
SOFT VOTE:        avg(predict_proba) → argmax
GINI IMPORT:      (nₚ/n)Gₚ − (nₗ/n)Gₗ − (nᵣ/n)Gᵣ
```

---

## 🧪 EXAM HACKS

```
💡 Ensemble error → Binomial sum for k > n/2
💡 AdaBoost wrong → weight × 2 if α≈0.693 (r=0.333 case)
💡 GBM 2nd tree always fits RESIDUALS, not original y
💡 OOB fraction always ≈ 36.8% regardless of n (as long as n is large)
💡 Soft voting beats hard when one classifier is very confident vs others barely
💡 Gini importance = weighted impurity DROP at each split
```

---

> **Nav:** [← INDEX](./ml_ch7_index.md) | [📖 THEORY](./ml_ch7_theory.md) | 🔢 NUMERICAL | [💻 PRACTICE →](./ml_ch7_practice.md)

* AI · ML · github.com/rpaut03l/TS-01*
