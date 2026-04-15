# 📖 NN Advanced: Optimizers & Learning-Rate Schedules

### *SGD · Momentum · Nesterov · AdaGrad · RMSProp · Adam · AdamW · Schedules*

> **Nav:** [← Initialization](ml_nn_adv_initialization.md) | [advanced README](README.md) | [Regularization →](ml_nn_adv_regularization.md)

---

## 🧠 MNEMONIC: **"SMNARA-A"**

> **S**GD · **M**omentum · **N**esterov · **A**daGrad · **R**MSProp · **A**dam · **A**damW

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | The Optimization Problem | [§1](#1-the-optimization-problem) |
| 2 | Plain SGD | [§2](#2-plain-sgd) |
| 3 | Momentum | [§3](#3-momentum) |
| 4 | Nesterov Accelerated Gradient | [§4](#4-nesterov-accelerated-gradient) |
| 5 | AdaGrad | [§5](#5-adagrad) |
| 6 | RMSProp | [§6](#6-rmsprop) |
| 7 | Adam | [§7](#7-adam) |
| 8 | AdamW — Decoupled Weight Decay | [§8](#8-adamw) |
| 9 | Learning-Rate Schedules | [§9](#9-learning-rate-schedules) |
| 10 | Side-by-Side Comparison | [§10](#10-side-by-side-comparison) |
| 11 | Cheat Sheet | [§11](#11-cheat-sheet--exam-hacks) |

---

## 1. The Optimization Problem

Training a neural net means solving:

> **θ* = argmin_θ  L(θ) = (1/N) Σᵢ ℓ(f_θ(xᵢ), yᵢ)**

- **θ** — all network parameters (millions to billions)
- **L** — non-convex, high-dimensional, expensive to evaluate exactly
- **Gradient** ∇L(θ) is cheap (backprop) and unbiased-on-minibatch

All optimizers are variations of **gradient descent** with tricks to handle:
1. **Stochastic noise** (we only see minibatches, not full-batch gradients)
2. **Curvature** (the loss surface is an ill-conditioned elongated valley)
3. **Non-convexity** (local minima, saddle points, plateaus)

[↑ Back to Top](#-nn-advanced-optimizers--learning-rate-schedules)

---

## 2. Plain SGD

```
UPDATE:   θ_{t+1} = θ_t − η · ∇L(θ_t)
```

- **η** (learning rate) is the *only* hyperparameter.
- **Pros:** simple, works, well-understood convergence theory, good for large datasets (one update per minibatch).
- **Cons:** oscillates in narrow valleys, slow in flat regions, gets stuck on plateaus.

### Why pure SGD still wins sometimes
On image classification (ResNet-on-ImageNet), **SGD + momentum often generalizes *better* than Adam** because SGD's noise acts as an implicit regularizer and Adam can settle into sharp minima that don't transfer well.

[↑ Back to Top](#-nn-advanced-optimizers--learning-rate-schedules)

---

## 3. Momentum

Accelerate in directions of consistent gradient; damp oscillation.

```
v_{t+1} = β · v_t + ∇L(θ_t)
θ_{t+1} = θ_t − η · v_{t+1}
```

- **β** (typically 0.9) — how much of the previous velocity to keep.
- Think "rolling ball with inertia."
- **Effective learning rate** in steady state = η / (1 − β), which is why β=0.9 makes the effective step 10× bigger than plain SGD.

### Intuition
If you're in an elongated valley (ill-conditioning), the plain SGD bounces between walls. Momentum cancels the perpendicular bouncing (the gradients flip sign every step) and reinforces the forward motion along the valley floor (the gradients agree).

[↑ Back to Top](#-nn-advanced-optimizers--learning-rate-schedules)

---

## 4. Nesterov Accelerated Gradient

A "look-ahead" momentum variant (Nesterov 1983, Sutskever et al. 2013):

```
θ̃     = θ_t − η · β · v_t          (look ahead)
v_{t+1} = β · v_t + ∇L(θ̃)
θ_{t+1} = θ_t − η · v_{t+1}
```

- Compute the gradient **at the look-ahead point**, not the current point.
- Gives a slightly better convergence rate for convex problems.
- In practice, Nesterov vs plain momentum is a ~1% tweak.

[↑ Back to Top](#-nn-advanced-optimizers--learning-rate-schedules)

---

## 5. AdaGrad

Duchi et al. (2011). Adapt the learning rate **per parameter** based on historical gradient magnitudes.

```
G_t    = G_{t-1} + (∇L(θ_t))²         (element-wise accumulator)
θ_{t+1} = θ_t − (η / √(G_t + ε)) · ∇L(θ_t)
```

- **Big gradients** get **smaller** steps (learning rate shrinks).
- **Small gradients** get **larger** steps (sparse features get attention).
- **Fatal flaw:** G_t grows forever ⇒ effective learning rate → 0 ⇒ training stalls.

Good for convex problems (original use case: text). Not used much for deep nets today.

[↑ Back to Top](#-nn-advanced-optimizers--learning-rate-schedules)

---

## 6. RMSProp

Hinton (Coursera lecture, 2012). Fix AdaGrad's dying learning rate by **exponentially averaging** the squared gradients:

```
v_t     = β · v_{t-1} + (1 − β) · (∇L(θ_t))²
θ_{t+1} = θ_t − (η / √(v_t + ε)) · ∇L(θ_t)
```

- **β ≈ 0.9 or 0.99** — "how much history to remember."
- The accumulator decays, so the learning rate doesn't monotonically shrink.
- Great for RNNs where gradient magnitudes vary wildly across parameters.

[↑ Back to Top](#-nn-advanced-optimizers--learning-rate-schedules)

---

## 7. Adam

Kingma & Ba (2014). **Momentum + RMSProp** combined, with bias-correction.

```
m_t = β₁ · m_{t-1} + (1 − β₁) · g_t               (1st moment — mean)
v_t = β₂ · v_{t-1} + (1 − β₂) · g_t²              (2nd moment — variance)

m̂_t = m_t / (1 − β₁^t)                             (bias correction)
v̂_t = v_t / (1 − β₂^t)

θ_{t+1} = θ_t − η · m̂_t / (√v̂_t + ε)
```

### Default hyperparameters (don't change them unless you know why)
- **β₁ = 0.9**, **β₂ = 0.999**, **ε = 1e−8**, **η ∈ [1e−4, 1e−3]**.

### Why bias correction?
m_0 and v_0 are initialized to 0, so early in training they're biased toward 0. Dividing by (1 − β^t) unbiases them — important in the first ~100 steps.

### Why Adam wins most tasks
- Works **out of the box** — very little LR tuning.
- **Handles sparse gradients** (NLP, recommender systems).
- **Fast initial progress** (crucial when you have a compute budget).

### Where Adam loses to SGD
- **CNN image classification with good data augmentation** — SGD + momentum + cosine schedule often beats Adam.
- **Very large models with weight decay** — plain Adam's weight decay is broken (see AdamW).

[↑ Back to Top](#-nn-advanced-optimizers--learning-rate-schedules)

---

## 8. AdamW

Loshchilov & Hutter (2017). Fix the **weight-decay bug** in Adam.

### The bug
Plain Adam with L2 regularization adds **λ · θ** to the gradient:
```
g_t ← g_t + λ · θ_t
```
But then Adam divides by √v̂_t — so the **effective** weight decay depends on the adaptive learning rate. Parameters with large historical gradients get much less regularization than parameters with small historical gradients. That's not what you want.

### The fix — decouple it
Apply weight decay **directly** to the parameters, outside of the gradient:
```
θ_{t+1} = θ_t − η · ( m̂_t / (√v̂_t + ε)  +  λ · θ_t )
```
Now every parameter gets the same relative decay. AdamW is the **default optimizer for transformers** and modern vision backbones.

### PyTorch
```python
torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.01)
```

[↑ Back to Top](#-nn-advanced-optimizers--learning-rate-schedules)

---

## 9. Learning-Rate Schedules

The LR is by far the most important hyperparameter. Common schedules:

### Step decay
```
η_t = η_0 · γ^⌊t / step⌋          γ ~ 0.1–0.5
```
Drop by 10× every 30 epochs. Works, but brittle.

### Exponential decay
```
η_t = η_0 · γ^t
```
Smooth, but needs tuning.

### Cosine annealing
```
η_t = η_min + ½ (η_max − η_min) · (1 + cos(π · t / T))
```
- Popular for image classification.
- Often combined with **warm restarts** (SGDR, Loshchilov 2016) — restart the cosine schedule periodically.

### Warmup + cosine decay (transformer standard)
```
Steps 0 .. W         : linear from 0 → η_peak
Steps W .. T         : cosine from η_peak → η_min
```
- **Warmup** (first ~1-10% of training) prevents huge early updates when the loss gradient is chaotic.
- **Cosine decay** for the rest.

### One-cycle (Smith 2018)
```
First half:  LR ↑ from η_min to η_max;  momentum ↓ from 0.95 to 0.85
Second half: LR ↓ back to η_min / 100;   momentum ↑ back to 0.95
```
Fast convergence for image tasks. Works surprisingly well.

### PyTorch hooks
```python
from torch.optim.lr_scheduler import CosineAnnealingLR, OneCycleLR, LambdaLR

# Cosine
scheduler = CosineAnnealingLR(optimizer, T_max=epochs)

# Linear warmup + cosine
def lr_lambda(step):
    if step < warmup_steps:
        return step / warmup_steps
    progress = (step - warmup_steps) / (total_steps - warmup_steps)
    return 0.5 * (1.0 + math.cos(math.pi * progress))
scheduler = LambdaLR(optimizer, lr_lambda=lr_lambda)
```

[↑ Back to Top](#-nn-advanced-optimizers--learning-rate-schedules)

---

## 10. Side-by-Side Comparison

```
┌──────────┬─────────┬─────────┬─────────────┬──────────────────────┐
│ OPTIMIZER│ Params  │ Momentum│ Per-param η │ Best for             │
├──────────┼─────────┼─────────┼─────────────┼──────────────────────┤
│ SGD      │ θ       │ ❌      │ ❌          │ large well-tuned CV  │
│ SGD+mom  │ θ, v    │ ✅      │ ❌          │ default baseline     │
│ Nesterov │ θ, v    │ ✅      │ ❌          │ ~1% over momentum    │
│ AdaGrad  │ θ, G    │ ❌      │ ✅ (shrink) │ sparse feats         │
│ RMSProp  │ θ, v    │ ❌      │ ✅          │ RNNs                 │
│ Adam     │ θ, m, v │ ✅      │ ✅          │ default for NLP/most │
│ AdamW    │ θ, m, v │ ✅      │ ✅          │ transformers, modern │
└──────────┴─────────┴─────────┴─────────────┴──────────────────────┘
```

> **Rule of thumb:** start with **AdamW** + cosine schedule + warmup. Switch to **SGD + momentum + cosine** if Adam is overfitting or generalizing poorly.

[↑ Back to Top](#-nn-advanced-optimizers--learning-rate-schedules)

---

## 11. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  OPTIMIZER EQUATIONS                                         ║
╠══════════════════════════════════════════════════════════════╣
║  SGD:       θ ← θ − η g                                      ║
║  Momentum:  v ← βv + g; θ ← θ − ηv    (β≈0.9)                ║
║  Nesterov:  g at look-ahead θ − ηβv                         ║
║  AdaGrad:   G += g²; θ ← θ − η g / √G                       ║
║  RMSProp:   v ← βv + (1−β)g²; θ ← θ − η g / √v              ║
║  Adam:      m, v updates + bias correction                   ║
║  AdamW:     Adam + weight decay applied OUTSIDE the update  ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Why bias-correct in Adam?"** — m and v start at 0, so they're biased toward 0 early in training. Dividing by (1 − β^t) removes the bias.
2. **"Why does AdaGrad die?"** — G monotonically accumulates ⇒ effective LR → 0 ⇒ training stalls. RMSProp uses exponential averaging so v doesn't grow without bound.
3. **"Adam vs AdamW?"** — Adam's weight decay is entangled with the adaptive LR (parameters with big gradients get too little regularization). AdamW decouples them.
4. **"When does SGD beat Adam?"** — vision tasks with good augmentation — SGD's noise is an implicit regularizer, Adam can find sharp minima that don't generalize.
5. **"Why warmup?"** — the first few steps of training have chaotic gradients (loss surface still shaped mostly by init); low LR prevents huge corrupting updates.
6. **"Why cosine decay?"** — matches the "explore early, refine late" intuition; works well empirically and has no hyperparameters besides max LR.

[↑ Back to Top](#-nn-advanced-optimizers--learning-rate-schedules)

---

### 💻 Quick Code — all the optimizers in 10 lines

```python
import torch
p = [torch.randn(3, requires_grad=True)]

torch.optim.SGD(p, lr=1e-2)
torch.optim.SGD(p, lr=1e-2, momentum=0.9)
torch.optim.SGD(p, lr=1e-2, momentum=0.9, nesterov=True)
torch.optim.Adagrad(p, lr=1e-2)
torch.optim.RMSprop(p, lr=1e-3, alpha=0.99)
torch.optim.Adam(p, lr=1e-3, betas=(0.9, 0.999))
torch.optim.AdamW(p, lr=3e-4, weight_decay=0.01)
```

---

> **Next:** [Regularization →](ml_nn_adv_regularization.md)
>
> *ML · Neural Networks Advanced · github.com/rpaut03l/TS-01*
