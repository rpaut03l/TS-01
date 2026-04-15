# 📖 ML Bayesian Decision Theory (BDT): THEORY

### *Bayes rule · Loss & risk · Min-error classification · Gaussian discriminants*

> **Nav:** [← ML Master Index](../ml_master_gap_index.md) | **BDT** | [🔢 NUMERICAL](ml_bdt_numerical.md) | [💻 Practice Problems](bayesian-practice-problems.md) | [📘 Detailed Guide](bayesian_becision_theory_guide.md)
>

---

## 🧠 MNEMONIC: **"PLER-G"**

> **P**osterior · **L**ikelihood · **E**vidence · **R**isk minimization · **G**aussian discriminants

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Why Bayesian Decision Theory? | [§1](#1-why-bayesian-decision-theory) |
| 2 | Bayes' Rule Refresher | [§2](#2-bayes-rule-refresher) |
| 3 | Minimum-Error-Rate Classification | [§3](#3-minimum-error-rate-classification) |
| 4 | General Loss & Conditional Risk | [§4](#4-general-loss--conditional-risk) |
| 5 | Discriminant Functions | [§5](#5-discriminant-functions) |
| 6 | Gaussian Class-Conditional Densities | [§6](#6-gaussian-class-conditional-densities) |
| 7 | LDA vs QDA vs Naive Bayes — from BDT | [§7](#7-lda-vs-qda-vs-naive-bayes) |
| 8 | Bayes Error (the lower bound) | [§8](#8-bayes-error) |
| 9 | Cheat Sheet & Exam Hacks | [§9](#9-cheat-sheet--exam-hacks) |

---

## 1. Why Bayesian Decision Theory?

### 👶 Easy Story
A doctor sees a patient and wants to decide: "is this cancer or not?" She has:
- How common cancer is in general (**prior**).
- How the test results *look like* in each case (**likelihood**).
- A cost for being wrong — false negatives can kill, false positives cost a biopsy (**loss**).

Bayesian Decision Theory is the **optimal framework** for decisions of this shape: combine prior + likelihood into a posterior, then pick the action that minimizes expected loss.

### The Framework
```
┌───────────────────────────────────────────────┐
│  PRIOR       p(ωⱼ)        how frequent each   │
│                            class is           │
│  LIKELIHOOD  p(x|ωⱼ)      how data looks in   │
│                            each class         │
│  POSTERIOR   p(ωⱼ|x)      what Bayes says     │
│  LOSS        λ(αᵢ|ωⱼ)     cost of action αᵢ   │
│                            when truth is ωⱼ   │
│  DECISION    pick αᵢ that minimizes           │
│              EXPECTED LOSS                    │
└───────────────────────────────────────────────┘
```

> 🔑 BDT is **optimal** — under its assumptions, no classifier can beat it. Other classifiers are just approximations to the Bayes classifier.

[↑ Back to Top](#-ml-bayesian-decision-theory-bdt-theory)

---

## 2. Bayes' Rule Refresher

```
                    p(x | ωⱼ) · p(ωⱼ)
     p(ωⱼ | x) = ──────────────────────
                         p(x)

     p(x) = Σⱼ p(x | ωⱼ) · p(ωⱼ)        (evidence, normalizer)
```

| Symbol | Name | Role |
|---|---|---|
| p(ωⱼ) | **prior** | base rate of class j |
| p(x \| ωⱼ) | **likelihood** (class-conditional density) | how x is distributed inside class j |
| p(x) | **evidence** | P of seeing x at all |
| p(ωⱼ \| x) | **posterior** | belief about class j AFTER seeing x |

Because p(x) is a positive constant across classes, for decisions we can compare **p(x\|ωⱼ)·p(ωⱼ)** across j and skip the normalization.

[↑ Back to Top](#-ml-bayesian-decision-theory-bdt-theory)

---

## 3. Minimum-Error-Rate Classification

If our loss is **0-1 loss** (1 for wrong, 0 for right), then minimizing expected loss = **maximizing posterior**:

> **Decide ωⱼ** if   **p(ωⱼ | x) > p(ωₖ | x)** for all k ≠ j
>
> equivalently   **p(x | ωⱼ) p(ωⱼ) > p(x | ωₖ) p(ωₖ)**

This is called the **MAP rule** (maximum a posteriori) and gives the **minimum possible error rate** — the **Bayes error**.

### Special cases
- **Equal priors:** decision depends only on likelihood → **maximum-likelihood** rule.
- **Equal class-conditional densities:** decision depends only on priors → always predict the most frequent class.

[↑ Back to Top](#-ml-bayesian-decision-theory-bdt-theory)

---

## 4. General Loss & Conditional Risk

When wrong answers have **different costs**, 0-1 loss is wrong. Define:

> **λ(αᵢ | ωⱼ)** = cost of taking action αᵢ when the true class is ωⱼ

**Conditional risk** of action αᵢ given observation x:

```
R(αᵢ | x) = Σⱼ λ(αᵢ | ωⱼ) · p(ωⱼ | x)
```

**Bayes decision rule (general):**
> **Pick α* = argmin_{αᵢ}  R(αᵢ | x)**

### Example — asymmetric medical test
```
Actions:  α₁ = "predict cancer",  α₂ = "predict healthy"
Truths:   ω₁ = "cancer",          ω₂ = "healthy"

Loss matrix:
                 true ω₁   true ω₂
  predict α₁  [    0         1    ]   ← false alarm: cost 1
  predict α₂  [   10         0    ]   ← missed cancer: cost 10

R(α₁ | x) = 0 · p(ω₁|x) + 1 · p(ω₂|x) = p(ω₂ | x)
R(α₂ | x) = 10 · p(ω₁|x) + 0 · p(ω₂|x) = 10 · p(ω₁|x)

Decide α₁ (cancer) when R(α₁|x) < R(α₂|x)
     ⟹ p(ω₂|x) < 10·p(ω₁|x)
     ⟹ p(ω₁|x) / p(ω₂|x) > 1/10
     ⟹ we predict cancer even at only 10% posterior!
```

This is why asymmetric costs push decision boundaries — missing cancer is **much** more costly than a false alarm.

[↑ Back to Top](#-ml-bayesian-decision-theory-bdt-theory)

---

## 5. Discriminant Functions

A **discriminant function** gᵢ(x) is any function whose comparison encodes the Bayes decision:

> **Decide ωᵢ** iff   **gᵢ(x) > gⱼ(x)** for all j ≠ i

Any monotonic transform of the posterior works. Common choices:

```
gᵢ(x) = p(ωᵢ | x)                  ← direct posterior
gᵢ(x) = p(x | ωᵢ) · p(ωᵢ)          ← skip normalization
gᵢ(x) = ln p(x | ωᵢ) + ln p(ωᵢ)    ← log for numerical stability
```

Log form is preferred because products of densities underflow quickly.

[↑ Back to Top](#-ml-bayesian-decision-theory-bdt-theory)

---

## 6. Gaussian Class-Conditional Densities

When each class is Gaussian, **p(x | ωᵢ) = N(x | μᵢ, Σᵢ)**:

```
p(x | ωᵢ) = (1 / ((2π)^(d/2) |Σᵢ|^(1/2))) · exp( −½(x−μᵢ)ᵀΣᵢ⁻¹(x−μᵢ) )
```

Taking logs:

```
gᵢ(x) = −½ (x−μᵢ)ᵀ Σᵢ⁻¹ (x−μᵢ)  −  ½ log|Σᵢ|  +  log p(ωᵢ)  +  const
```

### Case 1 — Σᵢ = σ² I (same isotropic covariance, equal priors)
The quadratic term collapses:
```
gᵢ(x) = −‖x − μᵢ‖² / (2σ²)   ⟹   pick class with NEAREST mean
```
This is a **minimum-distance (Euclidean) classifier**.

### Case 2 — Σᵢ = Σ (shared, not necessarily isotropic)
Quadratic terms are the same for all i and cancel when comparing:
```
gᵢ(x) = wᵢᵀ x + bᵢ   ← LINEAR discriminant!
   wᵢ = Σ⁻¹ μᵢ
   bᵢ = −½ μᵢᵀ Σ⁻¹ μᵢ + log p(ωᵢ)
```
Decision boundaries are **hyperplanes** → this is **LDA**.

### Case 3 — Σᵢ different per class
Quadratic terms survive:
```
gᵢ(x) = −½ xᵀ Σᵢ⁻¹ x + wᵢᵀ x + const
```
Decision boundaries are **quadratic** → this is **QDA**.

[↑ Back to Top](#-ml-bayesian-decision-theory-bdt-theory)

---

## 7. LDA vs QDA vs Naive Bayes

All three are **Gaussian Bayes classifiers**, differing in what they assume about Σ:

```
┌──────────────────┬─────────────────────┬────────────────┬───────────────┐
│ METHOD           │ Σ assumption        │ Boundary       │ Parameters    │
├──────────────────┼─────────────────────┼────────────────┼───────────────┤
│ Naive Bayes      │ diagonal, per class │ quadratic      │ Cd + Cd       │
│ LDA              │ Σ shared across     │ linear         │ Cd + d(d+1)/2 │
│                  │ classes             │                │               │
│ QDA              │ Σᵢ per class        │ quadratic      │Cd + C·d(d+1)/2│
│ Gaussian Bayes   │ same as QDA         │ quadratic      │ same          │
└──────────────────┴─────────────────────┴────────────────┴───────────────┘
```

> All three are **special cases of the Bayes-optimal classifier** under different Gaussian assumptions. Deciding which one to use is a bias/variance trade-off: more assumptions = less variance = better on small data, worse if the assumption is wrong.

[↑ Back to Top](#-ml-bayesian-decision-theory-bdt-theory)

---

## 8. Bayes Error

The **Bayes error** is the error rate of the Bayes classifier — the theoretical **lower bound** on any classifier's error given the true distributions:

```
P(error) = ∫ P(error | x) · p(x) dx
P(error | x) = 1 − max_i p(ωᵢ | x)
```

For two classes with known Gaussian densities and a computable boundary, this integral can be evaluated exactly (see numerical P4).

> ⚠️ **You can't beat the Bayes error.** Any real classifier's error will be ≥ Bayes error. If you're close to it, trying harder on the model won't help — you need better features.

[↑ Back to Top](#-ml-bayesian-decision-theory-bdt-theory)

---

## 9. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  BAYESIAN DECISION THEORY ONE-LINERS                         ║
╠══════════════════════════════════════════════════════════════╣
║  Posterior  ∝  likelihood · prior                            ║
║  0-1 loss + argmax posterior = MAP classifier                ║
║  General loss: pick min expected risk R(αᵢ|x)                ║
║  Log-discriminants for numerical stability                   ║
║  Gaussian shared Σ  →  LDA  (linear boundary)                ║
║  Gaussian per-class Σ →  QDA (quadratic boundary)            ║
║  Naive Bayes = diagonal Σ, features independent              ║
║  Bayes error is the theoretical floor; features matter       ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Derive MAP from Bayes rule"** — p(ωⱼ|x) ∝ p(x|ωⱼ)p(ωⱼ); argmax doesn't depend on p(x); done.
2. **"What if priors are equal?"** — Bayes rule reduces to **ML rule** (pick argmax likelihood).
3. **"Why log-discriminants?"** — products of densities underflow; logs turn them into sums.
4. **"When does the Bayes classifier reduce to a linear boundary?"** — when class-conditional densities are Gaussian with the **same Σ** → LDA.
5. **"Why does Naive Bayes work despite its independence assumption?"** — because for classification you only need the **argmax** of the posterior, not its exact value. Even if joint probabilities are wrong, the relative ordering can be right.
6. **"Loss matrix with asymmetric costs"** — the boundary **shifts**; you predict the more costly class even when you're not sure.
7. **"What is the Bayes error?"** — expected error rate of the best possible classifier — the theoretical lower bound.

[↑ Back to Top](#-ml-bayesian-decision-theory-bdt-theory)

---

> **Next:** [🔢 NUMERICAL](ml_bdt_numerical.md) · [💻 Practice Problems](bayesian-practice-problems.md) · [Parameter Estimation](../Parameter-Estimations-Guide/ml_parameter_estimation_theory.md) · [LDA](../LDA/ml_lda_theory.md)
>
> *ML · Bayesian Decision Theory · github.com/rpaut03l/TS-01*
