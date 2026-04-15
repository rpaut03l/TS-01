# 📖 NN Advanced: Loss Functions

### *Cross-entropy · Focal · Huber · Contrastive · Triplet · InfoNCE*

> **Nav:** [← Gradients & Activations](ml_nn_adv_gradients_activations.md) | [advanced README](README.md) | [Deep Learning Advanced →](../../Deep-Learning/advanced/README.md)

---

## 🧠 MNEMONIC: **"CHF-CTI"**

> **C**E · **H**uber · **F**ocal · **C**ontrastive · **T**riplet · **I**nfoNCE

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Classification: Binary Cross-Entropy | [§1](#1-binary-cross-entropy) |
| 2 | Classification: Categorical Cross-Entropy | [§2](#2-categorical-cross-entropy) |
| 3 | Class Imbalance: Weighted CE & Focal Loss | [§3](#3-focal-loss) |
| 4 | Regression: MSE · MAE · Huber · Log-cosh | [§4](#4-regression-losses) |
| 5 | Margin Losses: Hinge | [§5](#5-hinge-loss) |
| 6 | Metric Learning: Contrastive | [§6](#6-contrastive-loss) |
| 7 | Metric Learning: Triplet | [§7](#7-triplet-loss) |
| 8 | Self-Supervised: InfoNCE | [§8](#8-infonce) |
| 9 | Cheat Sheet | [§9](#9-cheat-sheet--exam-hacks) |

---

## 1. Binary Cross-Entropy

```
BCE(y, p̂) = − [ y · log p̂  +  (1 − y) · log(1 − p̂) ]
```

- y ∈ {0, 1}, p̂ ∈ (0, 1).
- Penalizes confident wrong predictions heavily (log blows up at 0).
- **Equivalent to MLE** under a Bernoulli model of y given x.

### Numerical stability
Use **binary_cross_entropy_with_logits** (fused with sigmoid) instead of sigmoid → BCE — avoids log(0) at very confident predictions.

```python
loss = F.binary_cross_entropy_with_logits(logits, targets.float())
```

[↑ Back to Top](#-nn-advanced-loss-functions)

---

## 2. Categorical Cross-Entropy

```
CE(y, p̂) = − Σ_k  y_k · log p̂_k
```
where y is one-hot and p̂ is a softmax output.

If y is a class index j, this simplifies to:
```
CE = − log p̂_j
```

### Link to information theory
Cross-entropy = H(y, p̂) = E_y [− log p̂]. Minimizing it drives p̂ to match the true class distribution.

### Numerical stability
Use **cross_entropy** (fused with log_softmax):
```python
loss = F.cross_entropy(logits, targets)    # targets are class indices
```

### Label smoothing
See [regularization §7](ml_nn_adv_regularization.md#7-label-smoothing). Replaces the one-hot with (1 − ε) on the true class and ε/(K−1) elsewhere.

[↑ Back to Top](#-nn-advanced-loss-functions)

---

## 3. Focal Loss

Lin et al. (2017). Fixes the problem where easy negatives drown the loss signal in heavily imbalanced tasks (e.g., object detection: 99% of boxes are background).

### Standard CE
```
CE = − log(p_t),   where p_t = p̂ if y=1 else 1−p̂
```

### Focal loss
```
FL(p_t) = − (1 − p_t)^γ · log(p_t)
```

- **γ = 2** is the standard choice.
- When p_t is close to 1 (easy example), **(1 − p_t)^γ** drives the loss toward 0.
- Hard examples (p_t small) dominate the gradient.

### With α-balancing
```
FL(p_t) = − α_t · (1 − p_t)^γ · log(p_t)
```
α_t is a class-weight.

### When to use
- **Object detection** (originally RetinaNet).
- **Long-tail classification** (rare classes dwarfed by common ones).
- **Any heavy class imbalance** where plain CE plateaus at "predict majority."

### Plain weighted CE is often enough
If imbalance is moderate, class-weighted CE is simpler and often equivalent.

[↑ Back to Top](#-nn-advanced-loss-functions)

---

## 4. Regression Losses

### MSE (L2)
```
MSE = (1/n) Σ (y − ŷ)²
```
- Convex, differentiable, **MLE under Gaussian noise**.
- Quadratic penalty → **outliers dominate**.

### MAE (L1)
```
MAE = (1/n) Σ |y − ŷ|
```
- **Robust to outliers**.
- Non-differentiable at 0, so gradient-based optimizers need sub-gradients.
- **MLE under Laplace noise**.

### Huber Loss (Smooth L1)
The best of both — quadratic near 0, linear far from 0:
```
Huber_δ(e) = ½ e²              if |e| ≤ δ
           = δ · (|e| − ½ δ)   if |e| > δ
```
- δ is a threshold (often 1.0).
- Gradient bounded by δ → prevents one outlier from hijacking the update.
- Used in **regression heads for object detection** (box-coordinate regression).

### Log-cosh
```
Lcosh(e) = log(cosh(e))
```
- Smooth everywhere (unlike Huber's kink at δ).
- Behaves like ½e² near 0 and |e| − log 2 far from 0.
- Nice property: second derivative bounded.

### Which to use
| Situation | Use |
|---|---|
| Clean Gaussian noise | MSE |
| Heavy-tailed noise / outliers | MAE or Huber |
| Bounded outputs | Tanh + MSE, or sigmoid + BCE |
| Detection bbox regression | Smooth L1 / Huber |

[↑ Back to Top](#-nn-advanced-loss-functions)

---

## 5. Hinge Loss

The SVM loss, generalized to nets:
```
L = max(0, 1 − y · s)         y ∈ {−1, +1},  s = score
```

- Zero when y · s ≥ 1 (correct side of margin).
- Linear penalty otherwise.
- Sparse gradients (many examples contribute 0).

### Squared hinge
```
L = max(0, 1 − y · s)²
```
Smoother, differentiable everywhere except at s = 1/y.

### When
- Multi-class SVM heads (rare today).
- Margin-based ranking.
- Structured prediction (hinge is natural for max-margin).

[↑ Back to Top](#-nn-advanced-loss-functions)

---

## 6. Contrastive Loss

Hadsell et al. (2006). Learn an embedding where **similar pairs** are close and **dissimilar pairs** are at least a margin apart.

```
L(x_i, x_j, y) = y · d(f(x_i), f(x_j))²     (positive pair — pull together)
               + (1 − y) · max(0, m − d(f(x_i), f(x_j)))²  (negative — push apart)
```

- **y = 1** if pair is similar, 0 if dissimilar.
- **m** is a margin (e.g., 1.0).
- **d** is usually Euclidean.

### Use
- Face verification, signature verification (Siamese networks).
- Any task where "same / different" is the supervision.

[↑ Back to Top](#-nn-advanced-loss-functions)

---

## 7. Triplet Loss

Schroff et al. (2015) for FaceNet. Anchor (a), positive (p), negative (n):

```
L = max(0, d(a, p) − d(a, n) + margin)
```

- Pull anchor toward positive, push away from negative by at least `margin`.
- Only contributes loss when the negative is too close to the anchor.

### Hard mining
The loss is zero for "easy" triplets (already well-separated). You need to **mine hard triplets** — ones where the negative is actually confusable — to keep learning.

- **Offline mining** — find hard triplets before each epoch.
- **Batch-hard mining** — within each batch, pick the hardest positive and hardest negative for each anchor (Hermans et al. 2017).

### Use
- Face recognition (FaceNet).
- Person re-identification.
- Any "find images of the same thing" task.

[↑ Back to Top](#-nn-advanced-loss-functions)

---

## 8. InfoNCE

Contrastive Predictive Coding (Oord et al. 2018). Generalizes contrastive loss to K negatives at once via a softmax:

```
L_InfoNCE = − log [ exp(sim(q, k⁺) / τ)  /  Σ_i exp(sim(q, kᵢ) / τ) ]
```

- **q** = query embedding, **k⁺** = positive, **kᵢ** include **k⁺** and K − 1 negatives.
- **τ** = temperature (e.g., 0.07 for SimCLR).
- **sim** = cosine similarity (typically).

### Interpretation
Treat contrastive learning as **classification**: the query must pick its matching key out of K candidates. The cross-entropy of that K-way softmax is InfoNCE.

### Use
- **SimCLR, MoCo, BYOL, CLIP** — modern self-supervised vision.
- **CLIP** — contrastive image-text alignment with massive batches.
- **Dense prediction** — contrastive pretraining at the pixel level.

### Why big batches help
With N examples in a batch, each gets N − 1 negatives for free. **Larger batch → harder negatives → better representations.** CLIP used batches of 32,768.

[↑ Back to Top](#-nn-advanced-loss-functions)

---

## 9. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  LOSS FUNCTIONS AT A GLANCE                                  ║
╠══════════════════════════════════════════════════════════════╣
║  Binary clf:      BCE (use _with_logits)                     ║
║  Multi-class:     Cross-entropy + label smoothing            ║
║  Imbalanced clf:  Focal (γ=2) or weighted CE                 ║
║  Regression:      MSE (clean) / Huber (outliers)             ║
║  Detection bbox:  Smooth L1 / GIoU                           ║
║  Siamese same/diff: Contrastive                              ║
║  Face / identity: Triplet + hard mining                      ║
║  Self-supervised: InfoNCE with cosine sim + temperature      ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Why use _with_logits versions?"** — numerical stability: fused with log-sum-exp tricks, avoids log(0).
2. **"Focal loss: what does γ control?"** — how aggressively to down-weight easy examples; γ=0 recovers plain CE, γ=2 is standard.
3. **"MSE vs MAE?"** — MSE = MLE under Gaussian noise, quadratic in error, outlier-sensitive; MAE = MLE under Laplace, linear, outlier-robust.
4. **"Why Huber?"** — it's MSE near 0 (smooth gradient) and MAE far from 0 (robust) — best of both.
5. **"Triplet loss without hard mining?"** — it collapses: easy triplets give zero loss, so training signal dies.
6. **"Why does bigger batch help InfoNCE?"** — more negatives per anchor → harder discrimination task → better features. SimCLR and CLIP both paid for huge batches.

[↑ Back to Top](#-nn-advanced-loss-functions)

---

### 💻 Quick Code

```python
import torch
import torch.nn.functional as F

# Standard CE with label smoothing
loss = F.cross_entropy(logits, targets, label_smoothing=0.1)

# Binary CE (logits)
loss = F.binary_cross_entropy_with_logits(logits, targets.float())

# Focal loss (write your own)
def focal_loss(logits, targets, gamma=2.0, alpha=0.25):
    ce = F.binary_cross_entropy_with_logits(logits, targets.float(), reduction='none')
    p_t = torch.exp(-ce)                         # prob of the true class
    return (alpha * (1 - p_t) ** gamma * ce).mean()

# Huber
loss = F.smooth_l1_loss(pred, target, beta=1.0)

# Triplet
loss = F.triplet_margin_loss(anchor, positive, negative, margin=1.0)

# InfoNCE (simplified)
def info_nce(q, k, temperature=0.07):
    # q, k: [B, D], rows assumed to be positive pairs
    q = F.normalize(q, dim=-1)
    k = F.normalize(k, dim=-1)
    logits = q @ k.t() / temperature              # [B, B]
    labels = torch.arange(q.size(0), device=q.device)
    return F.cross_entropy(logits, labels)
```

---

> **Next:** [Deep Learning Advanced →](../../Deep-Learning/advanced/README.md)
>
> *ML · Neural Networks Advanced · github.com/rpaut03l/TS-01*
