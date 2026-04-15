# 📖 NN Advanced: Gradients & Modern Activations

### *Vanishing/exploding · ReLU → GELU → Swish → Mish · Clipping · Skip connections*

> **Nav:** [← Regularization](ml_nn_adv_regularization.md) | [advanced README](README.md) | [Losses →](ml_nn_adv_losses.md)

---

## 🧠 MNEMONIC: **"GRACES"**

> **G**radient flow · **R**eLU family · **A**ctivations · **C**lipping · **E**xploding · **S**kip connections

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | The Vanishing Gradient Problem | [§1](#1-the-vanishing-gradient-problem) |
| 2 | The Exploding Gradient Problem | [§2](#2-the-exploding-gradient-problem) |
| 3 | Gradient Clipping | [§3](#3-gradient-clipping) |
| 4 | Sigmoid & Tanh (and why they fail) | [§4](#4-sigmoid--tanh) |
| 5 | ReLU and Dead Neurons | [§5](#5-relu-and-dead-neurons) |
| 6 | LeakyReLU · PReLU · ELU · SELU | [§6](#6-leakyrelu--prelu--elu--selu) |
| 7 | GELU · Swish · Mish | [§7](#7-gelu--swish--mish) |
| 8 | Skip Connections — the Real Fix | [§8](#8-skip-connections) |
| 9 | Activation Cheat Comparison | [§9](#9-activation-comparison) |
| 10 | Cheat Sheet | [§10](#10-cheat-sheet--exam-hacks) |

---

## 1. The Vanishing Gradient Problem

Consider backprop through L layers. By the chain rule:

```
∂L/∂θ_1  =  ∂L/∂a_L · ∂a_L/∂a_{L-1} · ... · ∂a_2/∂a_1 · ∂a_1/∂θ_1
                      └─────── L − 1 layer Jacobians ───────┘
```

If each Jacobian's operator norm is **< 1**, the product shrinks **exponentially**:
```
‖∂L/∂θ_1‖ ~ c^L   →   0   for L large
```

Result: **early layers get essentially zero gradient**, they never update, and the network can't learn long-range or hierarchical features.

### Why sigmoid/tanh cause it
sigmoid'(x) peaks at **0.25**, tanh'(x) peaks at **1.0** but is mostly well below 1. For 20 stacked layers, (0.25)^20 ≈ 10^−13.

### Symptoms
- Loss plateaus early.
- First-layer weights don't change.
- Gradient magnitudes tiny at bottom, OK at top.

[↑ Back to Top](#-nn-advanced-gradients--modern-activations)

---

## 2. The Exploding Gradient Problem

Symmetric: if each Jacobian's norm is **> 1**, the product grows exponentially. Result: **NaN loss**, sudden huge updates, training diverges.

### Common in
- **RNNs** — the same transition matrix is applied at every time step. If it has an eigenvalue > 1, gradients explode in time.
- **Poorly initialized deep nets** — a bad init can push you straight into the exploding regime.

### Symptoms
- Loss is OK then suddenly NaN.
- Gradient magnitudes blow up (check `torch.norm(p.grad)` during training).
- Weights become huge.

[↑ Back to Top](#-nn-advanced-gradients--modern-activations)

---

## 3. Gradient Clipping

The brute-force fix for exploding gradients: **cap** the gradient norm before the optimizer step.

### Clip by global norm
```
g_total = concat(all gradients)
if ‖g_total‖ > c:
    g_total ← g_total · (c / ‖g_total‖)
```

### Clip by value
```
g ← clip(g, −c, +c)        (element-wise)
```

### Which to use
- **Clip by norm** (c = 1.0) is the default for transformers and LLMs.
- **Clip by value** rarely — it destroys gradient direction.

### PyTorch
```python
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
optimizer.step()
```

### Why it works
Clipping caps the "oomph" of any single step so the optimizer can't wander off into never-never land when it hits a cliff in the loss landscape.

[↑ Back to Top](#-nn-advanced-gradients--modern-activations)

---

## 4. Sigmoid & Tanh

```
σ(x) = 1 / (1 + e^(−x))     →  (0, 1)
σ'(x) = σ(x)(1 − σ(x))      →  max at x=0, σ'(0) = 0.25

tanh(x) = (eˣ − e⁻ˣ)/(eˣ + e⁻ˣ)  →  (−1, 1)
tanh'(x) = 1 − tanh²(x)          →  max at x=0, tanh'(0) = 1
```

### Problems
1. **Saturating** — for |x| > 5, gradient is essentially 0 → neuron is "stuck."
2. **Non-zero-centered (sigmoid)** — gradients always have the same sign → zig-zag optimization.
3. **Exp is expensive** — minor but real.

### Still useful for
- **Output layers** — sigmoid for binary probabilities, tanh for bounded outputs.
- **Gates in LSTMs/GRUs** — gating naturally needs (0, 1).

[↑ Back to Top](#-nn-advanced-gradients--modern-activations)

---

## 5. ReLU and Dead Neurons

```
ReLU(x) = max(0, x)
ReLU'(x) = 1 if x > 0, else 0
```

### Why ReLU dominates
- **Cheap** — just a comparison.
- **Non-saturating for x > 0** — gradient is 1, so products of Jacobians don't shrink.
- **Sparse** — half the activations are 0 on average.
- **Gradients flow** — no vanishing in deep nets (within reason).

### Dead ReLU Problem
If a neuron's pre-activation is negative for every training example (due to bad luck, huge negative bias, or a large gradient step), its gradient is **always 0** → it never updates → **dead for the rest of training**.

Typical symptoms:
- Some fraction of ReLU neurons always output 0.
- Validation accuracy plateaus.

### Fixes
- **Lower learning rate** (big LR can kill neurons on one bad step).
- **He init** (correct scale).
- **LeakyReLU / PReLU / ELU** — small nonzero slope for x < 0.

[↑ Back to Top](#-nn-advanced-gradients--modern-activations)

---

## 6. LeakyReLU · PReLU · ELU · SELU

### LeakyReLU
```
LReLU(x) = x       if x > 0
         = α · x   if x ≤ 0        (α = 0.01 typically)
```
Small negative slope → dead-neuron fix, gradient can flow for x < 0.

### PReLU (Parametric ReLU)
Like LeakyReLU but **α is learned** per channel. More flexible, slightly more params.

### ELU (Exponential Linear Unit)
```
ELU(x) = x                 if x > 0
       = α · (eˣ − 1)      if x ≤ 0
```
Smooth at 0, negative values push mean activation toward 0 → batch-norm-like effect without BN.

### SELU (Scaled ELU)
Klambauer et al. (2017). SELU with LeCun init + specific α, λ constants gives **self-normalizing** networks — activations keep zero mean and unit variance through depth **without BatchNorm**.

```
SELU(x) = λ · ELU(x)
λ ≈ 1.0507,  α ≈ 1.6733        (magic constants)
```

### When to use
- **ReLU:** default, most networks, CNNs.
- **LeakyReLU:** GANs (prevents mode collapse).
- **ELU / SELU:** deep fully-connected nets without BN.

[↑ Back to Top](#-nn-advanced-gradients--modern-activations)

---

## 7. GELU · Swish · Mish

### GELU (Gaussian Error Linear Unit)
Hendrycks & Gimpel (2016). **Standard in transformers** (BERT, GPT, ViT).

```
GELU(x) = x · Φ(x)         (Φ = CDF of standard Normal)
        ≈ 0.5 x · (1 + tanh(√(2/π) · (x + 0.044715 x³)))
```

Think of it as ReLU + smoothness. Performs ~1% better than ReLU on transformers.

### Swish / SiLU
Ramachandran et al. (2017). Discovered via neural architecture search.

```
Swish(x) = x · σ(x)         (σ = sigmoid)
```

- Smooth, non-monotonic — has a dip for slightly negative x.
- Works well in deep CNNs (EfficientNet uses it).
- Roughly equivalent to GELU, easier to compute.

### Mish
Misra (2019). Smooth self-gated variant:
```
Mish(x) = x · tanh(softplus(x)) = x · tanh(ln(1 + eˣ))
```
Slightly better than Swish on some benchmarks. Used in YOLOv4.

### Bottom line
- **ReLU** — most nets, default.
- **GELU** — transformers.
- **Swish / SiLU** — efficient CNNs.

[↑ Back to Top](#-nn-advanced-gradients--modern-activations)

---

## 8. Skip Connections

The **actual solution** to deep-network gradient problems wasn't a better activation — it was the **residual connection**.

### Residual block (He et al. 2015)
```
y = F(x) + x
```
where F is a small sub-network (e.g., two conv layers).

### Why it helps gradients
The backward pass now has an **identity path**:
```
∂y/∂x = ∂F/∂x + I
```
Even if ∂F/∂x is tiny (vanishing), the identity term guarantees gradient flows. This turned out to be the key that enabled 100+ layer CNNs.

### Dense connections (DenseNet, Huang et al. 2017)
Each layer receives feature maps from **all previous layers**, concatenated:
```
x_l = H_l([x_0, x_1, ..., x_{l-1}])
```

### Transformer residuals
Every sub-layer in a transformer block is wrapped in:
```
x + Dropout(SubLayer(LayerNorm(x)))
```
(Pre-norm variant. Post-norm puts LN after addition but is less stable.)

### Why skip connections are a regularizer too
They let the network learn an **identity mapping** easily by just pushing F → 0. The network can "turn off" any block that isn't helping.

[↑ Back to Top](#-nn-advanced-gradients--modern-activations)

---

## 9. Activation Comparison

```
┌──────────┬────────────────┬──────────┬────────────┬──────────────────────┐
│ Name     │ Formula        │ Deriv    │ Saturates? │ Typical use          │
├──────────┼────────────────┼──────────┼────────────┼──────────────────────┤
│ Sigmoid  │ 1/(1+e⁻ˣ)      │ σ(1−σ)   │ Yes ±      │ output binary, gates │
│ Tanh     │ (eˣ−e⁻ˣ)/...   │ 1−tanh²  │ Yes ±      │ output [-1,1], RNN   │
│ ReLU     │ max(0,x)       │ 0 / 1    │ Left       │ default CNN/FC       │
│ LReLU    │ x / αx         │ 1 / α    │ No         │ GANs                 │
│ ELU      │ x / α(eˣ−1)    │ 1 / αeˣ  │ Left soft  │ deep FC w/o BN       │
│ SELU     │ λ·ELU(x)       │ λ·ELU'   │No(self-norm)│ deep FC w/o BN      │
│ GELU     │ x·Φ(x)         │ complex  │ No         │ transformers         │
│ Swish    │ x·σ(x)         │ σ+xσ(1−σ)│ No         │ efficient CNNs       │
│ Mish     │ x·tanh(sp(x))  │ complex  │ No         │ some CV models       │
└──────────┴────────────────┴──────────┴────────────┴──────────────────────┘
```

[↑ Back to Top](#-nn-advanced-gradients--modern-activations)

---

## 10. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  VANISHING / EXPLODING GRADIENT FIXES                        ║
╠══════════════════════════════════════════════════════════════╣
║  Vanishing  →  ReLU family + He init + Skip connections      ║
║              + BatchNorm / LayerNorm                         ║
║  Exploding  →  Gradient clipping + orthogonal init (RNNs)    ║
║              + careful LR                                    ║
║                                                              ║
║  Sigmoid/tanh saturate → use only at outputs or gates        ║
║  Dead ReLU → lower LR, He init, LeakyReLU                    ║
║  Skip connections are the real fix: identity path            ║
║     keeps gradient alive regardless of depth                 ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Why does ReLU prevent vanishing gradients in positive region?"** — gradient is exactly 1 for x > 0, so products of Jacobians don't shrink.
2. **"How does ResNet enable very deep networks?"** — residual (identity) connections give gradients an alternate path that never vanishes.
3. **"What is a dead ReLU?"** — a neuron whose pre-activation is always negative on the training set → always outputs 0 → gradient always 0 → stuck forever.
4. **"Gradient clipping — by norm or by value?"** — by norm preserves direction; by value destroys it (use norm).
5. **"Why GELU in transformers?"** — smooth, non-monotonic, works slightly better than ReLU in practice, differentiable everywhere.
6. **"SELU alone gives you BatchNorm?"** — approximately yes: SELU + LeCun init + ALPHA dropout → self-normalizing network without BN.

[↑ Back to Top](#-nn-advanced-gradients--modern-activations)

---

### 💻 Quick Code

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

# Activations
F.relu(x)
F.leaky_relu(x, negative_slope=0.01)
F.elu(x, alpha=1.0)
F.selu(x)
F.gelu(x)
F.silu(x)             # == Swish
F.mish(x)             # PyTorch ≥ 1.9

# Gradient clipping
optimizer.zero_grad()
loss.backward()
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
optimizer.step()

# Residual block
class ResBlock(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, dim), nn.GELU(),
            nn.Linear(dim, dim),
        )
    def forward(self, x):
        return x + self.net(x)        # identity skip
```

---

> **Next:** [Losses →](ml_nn_adv_losses.md)
>
> *ML · Neural Networks Advanced · github.com/rpaut03l/TS-01*
