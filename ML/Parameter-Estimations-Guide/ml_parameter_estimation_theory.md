# 📖 ML Parameter Estimation: THEORY

### *MLE · MAP · Bayesian Parameter Estimation · Conjugate Priors*

> **Nav:** [← ML Master Index](../ml_master_gap_index.md) | **Parameter Estimation** | [🔢 NUMERICAL](ml_parameter_estimation_numerical.md) | [💻 PRACTICE](ml_parameter_estimation_practice.md)
>

---

## 🧠 MNEMONIC: **"MAP-B"**

> **M**LE (what data says) · **A**dd prior · **P**osterior · **B**ayesian avg

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Why Parameter Estimation? | [§1](#1-why-parameter-estimation) |
| 2 | Likelihood & Log-Likelihood | [§2](#2-likelihood--log-likelihood) |
| 3 | Maximum Likelihood Estimation (MLE) | [§3](#3-maximum-likelihood-estimation-mle) |
| 4 | Bayesian View — Prior · Posterior · Evidence | [§4](#4-bayesian-view) |
| 5 | MAP Estimation | [§5](#5-map-estimation) |
| 6 | Full Bayesian Estimation | [§6](#6-full-bayesian-estimation) |
| 7 | Conjugate Priors | [§7](#7-conjugate-priors) |
| 8 | MLE vs MAP vs Bayesian — Side-by-Side | [§8](#8-mle-vs-map-vs-bayesian) |
| 9 | Bias & Variance of Estimators | [§9](#9-bias--variance-of-estimators) |
| 10 | Cheat Sheet & Exam Hacks | [§10](#10-cheat-sheet--exam-hacks) |

---

## 1. Why Parameter Estimation?

### 👶 Easy Story
You have a coin. You want to know **P(heads) = θ**. You flip it 10 times and see 7 heads. What's θ?
- Your friend says "**θ = 0.7** — that's what the data shows!" → **MLE**
- Your grandma says "Coins are usually fair. **θ is near 0.5**." → **Prior**
- You combine both → "**θ ≈ 0.65**" → **MAP / Bayesian**

Parameter estimation is **how we turn data into model parameters**.

```
┌─────────────────────────────────────────────────┐
│ DATA  D = {x₁,...,xₙ}                           │
│              │                                  │
│              ▼                                  │
│ MODEL  p(x | θ)       ← assume family           │
│              │                                  │
│              ▼                                  │
│ GOAL:  find best θ̂                              │
│              │                                  │
│   ┌──────────┼──────────┐                       │
│   ▼          ▼          ▼                       │
│ MLE         MAP      BAYESIAN                   │
│ (data)   (+prior)   (full posterior)            │
└─────────────────────────────────────────────────┘
```

[↑ Back to Top](#-ml-parameter-estimation-theory)

---

## 2. Likelihood & Log-Likelihood

### Definition
Given i.i.d. data **D = {x₁,...,xₙ}** and a model **p(x | θ)**:

> **Likelihood:**   L(θ | D) = p(D | θ) = Π p(xᵢ | θ)

Because products of small numbers underflow, we always work with:

> **Log-Likelihood:**   ℓ(θ) = log L(θ) = Σ log p(xᵢ | θ)

### Why log?
1. **Numerical stability** — sums instead of products.
2. **Calculus-friendly** — derivative of sum = sum of derivatives.
3. **Monotonic** — argmax of L = argmax of log L.

```
LIKELIHOOD vs PROBABILITY
─────────────────────────
 p(x | θ)  fixed θ, function of x  → PROBABILITY (sums to 1 over x)
 L(θ | x)  fixed x, function of θ  → LIKELIHOOD  (does NOT sum to 1)
```

[↑ Back to Top](#-ml-parameter-estimation-theory)

---

## 3. Maximum Likelihood Estimation (MLE)

### The Rule
> **θ̂_MLE = argmax_θ  ℓ(θ)**

Pick the θ that makes the observed data **most probable**.

### Recipe (4 steps)
```
1. Write likelihood   L(θ) = Π p(xᵢ | θ)
2. Take log           ℓ(θ) = Σ log p(xᵢ | θ)
3. Differentiate      dℓ/dθ = 0
4. Solve for θ        → θ̂_MLE
   (check d²ℓ/dθ² < 0 for max)
```

### Classic Derivations

**Bernoulli (coin flip), n tosses, k heads:**
```
p(x|θ) = θˣ (1-θ)^(1-x),  x ∈ {0,1}
ℓ(θ) = k log θ + (n-k) log(1-θ)
dℓ/dθ = k/θ - (n-k)/(1-θ) = 0
⟹ θ̂_MLE = k / n          ← SAMPLE PROPORTION
```

**Gaussian (unknown μ, known σ²):**
```
ℓ(μ) = -½n log(2πσ²) - (1/2σ²) Σ(xᵢ - μ)²
dℓ/dμ = (1/σ²) Σ(xᵢ - μ) = 0
⟹ μ̂_MLE = (1/n) Σ xᵢ = x̄   ← SAMPLE MEAN
```

**Gaussian (unknown μ and σ²):**
```
μ̂_MLE = x̄
σ̂²_MLE = (1/n) Σ(xᵢ - x̄)²     ← BIASED! (should be 1/(n-1))
```

> ⚠️ **Famous gotcha:** MLE variance for Gaussian is **biased** — it divides by **n**, not **n−1**. The unbiased estimator is the one stats textbooks use.

[↑ Back to Top](#-ml-parameter-estimation-theory)

---

## 4. Bayesian View

### The Chain
```
     PRIOR × LIKELIHOOD         p(θ) · p(D | θ)
POSTERIOR = ───────────────  = ───────────────────
         EVIDENCE                    p(D)
```

> **p(θ | D)  ∝  p(D | θ) · p(θ)**

| Symbol | Name | Meaning |
|---|---|---|
| p(θ) | **Prior** | What we believed about θ BEFORE seeing data |
| p(D \| θ) | **Likelihood** | How well θ explains the data |
| p(D) | **Evidence** | Marginal p(D) = ∫ p(D\|θ) p(θ) dθ — normalizer |
| p(θ \| D) | **Posterior** | Updated belief AFTER data |

### Story
- **Prior** = grandma's "coins are fair"
- **Likelihood** = your 7/10 heads experiment
- **Posterior** = combined belief

More data ⟹ posterior shape dominated by likelihood ⟹ prior washes out.

[↑ Back to Top](#-ml-parameter-estimation-theory)

---

## 5. MAP Estimation

### The Rule
> **θ̂_MAP = argmax_θ  p(θ | D) = argmax_θ  [ p(D | θ) · p(θ) ]**

MAP = MLE **plus** a prior. You pick the peak of the posterior.

```
θ̂_MAP = argmax_θ  [ log p(D|θ)  +  log p(θ) ]
                    └─ likelihood ─┘  └─ prior ─┘
                    ↑                  ↑
                 same as MLE       regularization!
```

### Key Insight — MAP ≡ Regularized MLE
| Prior on θ | Equivalent penalty | Classical name |
|---|---|---|
| Gaussian  θ ~ N(0, τ²) | λ ‖θ‖² | **L2 / Ridge** |
| Laplace   θ ~ Lap(0, b) | λ ‖θ‖₁ | **L1 / Lasso** |
| Uniform | 0 | **Plain MLE** |

> 🔑 **This is why Bayesian stats and regularization are two sides of the same coin.**

### MAP vs MLE — Bernoulli with Beta(α,β) prior
```
Prior:     θ ~ Beta(α, β)
Data:      n flips, k heads
Posterior: θ | D ~ Beta(α + k, β + n − k)

θ̂_MAP = (α + k - 1) / (α + β + n - 2)     ← mode of Beta
θ̂_MLE =  k / n
```
- α = β = 1 (uniform prior) ⟹ MAP = MLE
- α, β large ⟹ prior dominates

[↑ Back to Top](#-ml-parameter-estimation-theory)

---

## 6. Full Bayesian Estimation

Instead of one point estimate, **use the entire posterior** when predicting new data:

> **p(x_new | D) = ∫ p(x_new | θ) · p(θ | D) dθ**

```
MLE / MAP →  "pick one θ, predict with it"
BAYESIAN  →  "average predictions over ALL θ, weighted by posterior"
```

### Why bother?
- **Captures uncertainty** in θ, not just in x.
- **More robust** with small data (heavy-tailed posterior protects you).
- **Cost:** integral is usually intractable → need MCMC / variational inference.

[↑ Back to Top](#-ml-parameter-estimation-theory)

---

## 7. Conjugate Priors

A prior is **conjugate** to a likelihood if the **posterior has the same family** as the prior — so Bayesian updates become simple parameter updates.

| Likelihood | Conjugate Prior | Posterior |
|---|---|---|
| Bernoulli(θ) | **Beta(α, β)** | Beta(α + k, β + n − k) |
| Binomial(n, θ) | **Beta(α, β)** | Beta(α + k, β + n − k) |
| Poisson(λ) | **Gamma(α, β)** | Gamma(α + Σxᵢ, β + n) |
| Normal(μ, σ² known) | **Normal(μ₀, σ₀²)** | Normal with updated μ, σ² |
| Normal(μ known, σ²) | **Inverse-Gamma** | Inverse-Gamma |
| Multinomial(θ) | **Dirichlet(α)** | Dirichlet(α + counts) |

### Why it matters
- **Closed-form updates** — no integration needed.
- **Sequential learning** — posterior after batch 1 becomes prior for batch 2.
- **Sanity check** — if your prior and likelihood are conjugate, you can check numerical results against a simple formula.

[↑ Back to Top](#-ml-parameter-estimation-theory)

---

## 8. MLE vs MAP vs Bayesian

```
┌───────────┬───────────────────────┬─────────────────────┬─────────────────────┐
│ PROPERTY  │ MLE                   │ MAP                 │ FULL BAYESIAN       │
├───────────┼───────────────────────┼─────────────────────┼─────────────────────┤
│ Output    │ point estimate        │ point estimate      │ full distribution   │
│ Uses prior│ ❌ No                  │ ✅ Yes (peak only)  │ ✅ Yes (entire)      │
│ Small n   │ ⚠️ Overfits            │ 👍 Regularized      │ 👍👍 Best            │
│ Large n   │ ✅ Converges           │ ✅ Same as MLE      │ ✅ Same as MLE       │
│ Cost      │ Cheap (closed-form)   │ Cheap               │ Expensive           │
│ Example   │ θ̂ = k/n                │ θ̂ = (k+α−1)/(n+α+β−2)│ p(θ|D) = Beta(·,·) │
└───────────┴───────────────────────┴─────────────────────┴─────────────────────┘
```

### Consistency (the punchline)
As **n → ∞**, all three converge to the **true θ** (if the model is correct and the prior is nonzero there). Prior only matters when data is scarce.

[↑ Back to Top](#-ml-parameter-estimation-theory)

---

## 9. Bias & Variance of Estimators

For an estimator θ̂(D):

```
BIAS(θ̂)     = E[θ̂] − θ
VARIANCE(θ̂) = E[(θ̂ − E[θ̂])²]
MSE(θ̂)      = BIAS² + VARIANCE
```

| Estimator | Bias | Variance | Notes |
|---|---|---|---|
| Sample mean (MLE of μ) | 0 (unbiased) | σ²/n | Best you can do for Gaussian μ |
| MLE of σ² (÷n) | −σ²/n (biased) | Lower | Divides by n |
| Unbiased σ² (÷n−1) | 0 | Slightly higher | Bessel's correction |
| MAP with strong prior | biased | low | Good trade for small n |

> 💡 Biased estimators are **often better** than unbiased ones when they reduce variance more than they add bias² (James-Stein phenomenon, ridge regression, etc.).

[↑ Back to Top](#-ml-parameter-estimation-theory)

---

## 10. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  KEY EQUATIONS                                               ║
╠══════════════════════════════════════════════════════════════╣
║  MLE:        θ̂ = argmax Σ log p(xᵢ | θ)                      ║
║  MAP:        θ̂ = argmax [ Σ log p(xᵢ|θ) + log p(θ) ]         ║
║  BAYES:      p(θ|D) ∝ p(D|θ) · p(θ)                          ║
║  PREDICT:    p(x*|D) = ∫ p(x*|θ) p(θ|D) dθ                   ║
╠══════════════════════════════════════════════════════════════╣
║  STANDARD MLEs                                               ║
╠══════════════════════════════════════════════════════════════╣
║  Bernoulli:  θ̂ = k/n                                         ║
║  Gaussian μ: μ̂ = x̄                                           ║
║  Gaussian σ²: σ̂² = (1/n) Σ(xᵢ-x̄)²    ← biased!               ║
║  Poisson λ:  λ̂ = x̄                                           ║
║  Exponential λ: λ̂ = 1/x̄                                      ║
╠══════════════════════════════════════════════════════════════╣
║  CONJUGATE QUICK-REFERENCE                                   ║
╠══════════════════════════════════════════════════════════════╣
║  Bern/Bin  ←→  Beta                                          ║
║  Poisson   ←→  Gamma                                         ║
║  Normal(μ) ←→  Normal                                        ║
║  Multinom. ←→  Dirichlet                                     ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Estimate θ from n i.i.d. samples"** → default to **MLE** unless prior is given.
2. **"Prior on θ is Beta/Normal/..."** → this is a **MAP/Bayes** problem.
3. **"Show that MAP = MLE when..."** → answer: **uniform prior** or **n → ∞**.
4. **"Why is σ̂²_MLE biased?"** → because we use **x̄** (itself estimated) instead of the true μ, losing 1 degree of freedom → should be 1/(n−1).
5. **"Which prior gives Ridge / Lasso?"** → **Gaussian → L2 (Ridge)**, **Laplace → L1 (Lasso)**.

[↑ Back to Top](#-ml-parameter-estimation-theory)

---

> **Next:** [🔢 NUMERICAL](ml_parameter_estimation_numerical.md) · [💻 PRACTICE](ml_parameter_estimation_practice.md)
>
> *ML · Parameter Estimation · github.com/rpaut03l/TS-01*
