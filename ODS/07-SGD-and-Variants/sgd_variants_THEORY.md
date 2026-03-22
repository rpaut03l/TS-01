# SGD, Momentum, Adam — Theory
### ODS Topic 07 · Lectures 6-7

> **Nav:** [← INDEX](./sgd_variants_INDEX.md) · [→ PRACTICE](./sgd_variants_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

---

## 7.1 Why SGD?

Batch GD computes: ∇F(w) = (1/n) Σᵢ ∇fᵢ(w). When n = 10⁶, this is SLOW.

**SGD:** Pick random iₜ, use ∇f_{iₜ}(w) instead. One sample gradient!

```
SGD Update:
  w_{t+1} = wₜ - ηₜ ∇f_{iₜ}(wₜ)

Key property: E[∇f_{iₜ}(w)] = ∇F(w)  (UNBIASED estimator!)
```

## 7.2 Convergence of SGD

For convex, L-smooth F with bounded variance σ²:
```
E[F(w̄_T) - F(w*)] ≤ O(1/√T)    (slower than BGD's O(1/T))
```

Robbins-Monro conditions for learning rate: Σ ηₜ = ∞ and Σ ηₜ² < ∞.
Common choice: ηₜ = O(1/t).

## 7.3 Mini-Batch GD

Sample batch Bₜ of size b:
```
w_{t+1} = wₜ - (ηₜ/b) Σ_{i∈Bₜ} ∇fᵢ(wₜ)

Variance reduction: Var = σ²/b
```

## 7.4 Momentum (Polyak's Heavy Ball)

```
vₜ₊₁ = β vₜ + ∇F(wₜ)           ← accumulate velocity
wₜ₊₁ = wₜ - η vₜ₊₁             ← update with momentum

β ∈ [0,1) is the momentum coefficient (typically 0.9)
```

Dampens oscillations, accelerates along consistent gradient directions.

## 7.5 Nesterov Accelerated Gradient (NAG)

```
vₜ₊₁ = β vₜ + η ∇F(wₜ - β vₜ)   ← "look-ahead" gradient
wₜ₊₁ = wₜ - vₜ₊₁

Optimal rate for L-smooth convex: F(wₜ) - F(w*) ≤ O(1/T²)
```

## 7.6 AdaGrad, RMSProp, Adam (Mentioned)

Per-parameter learning rates for sparse features:
- **AdaGrad:** Accumulates squared gradients, decreases LR for frequent features
- **RMSProp:** Exponential moving average of squared gradients
- **Adam:** RMSProp + Momentum, the DEFAULT in deep learning

```
  COMPARISON DIAGRAM:
  
  GD ──→ Add momentum ──→ Heavy Ball / NAG
   │
   └──→ Use 1 sample ──→ SGD ──→ Mini-batch SGD
   │
   └──→ Per-param LR ──→ AdaGrad ──→ RMSProp ──→ Adam
                                       (combines all ideas!)
```

---

> [→ PRACTICE](./sgd_variants_PRACTICE.md) · [↑ Hub](../ODS_Master_INDEX.md)

[Back to Top](#sgd-momentum-adam--theory)
