# 📖 NN Advanced: Weight Initialization & Universal Approximation

### *Why init is life-or-death · Xavier · He · LeCun · Orthogonal · UAT*

> **Nav:** [← advanced README](README.md) | [NN Theory basics](../ml_nn_mlp_bp_theory.md) | [Optimizers →](ml_nn_adv_optimizers.md)

---

## 🧠 MNEMONIC: **"SLICE"**

> **S**cale · **L**ayer-by-layer · **I**nput/output fan · **C**onsistent variance · **E**qual gradient flow

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Why Initialization Matters | [§1](#1-why-initialization-matters) |
| 2 | The Forward-Variance Argument | [§2](#2-the-forward-variance-argument) |
| 3 | The Backward-Variance Argument | [§3](#3-the-backward-variance-argument) |
| 4 | Xavier / Glorot Init | [§4](#4-xavier--glorot-init) |
| 5 | He / Kaiming Init (for ReLU) | [§5](#5-he--kaiming-init-for-relu) |
| 6 | LeCun Init (for SELU / tanh) | [§6](#6-lecun-init) |
| 7 | Orthogonal Init | [§7](#7-orthogonal-init) |
| 8 | Biases, BatchNorm, and "Init doesn't matter anymore" | [§8](#8-biases-batchnorm) |
| 9 | Universal Approximation Theorem | [§9](#9-universal-approximation-theorem) |
| 10 | Cheat Sheet | [§10](#10-cheat-sheet--exam-hacks) |

---

## 1. Why Initialization Matters

### 👶 Easy Story
You stack 20 layers. Every weight is a tiny Gaussian. You feed an image and run `loss.backward()`. Nothing happens — the loss is flat, gradients are ~10⁻¹⁵ at the first layer. What went wrong?

Or the opposite: every weight is 1.0. After 5 layers the activations are 10⁸ and the loss is NaN.

**The scale of the weights determines whether the signal survives the forward pass AND whether gradients survive the backward pass.** Init is not cosmetic; it's a correctness issue for deep nets.

```
TOO SMALL weights   →  activations shrink  →  gradients vanish  →  no learning
TOO LARGE weights   →  activations explode →  NaN loss          →  no learning
JUST RIGHT          →  activations/gradients keep ~constant variance
```

[↑ Back to Top](#-nn-advanced-weight-initialization--universal-approximation)

---

## 2. The Forward-Variance Argument

Assume one layer: **y = Wx + b**, W ∈ ℝ^(n_out × n_in), x has zero mean and variance σ²_x per coordinate, W entries are iid zero-mean with variance σ²_W. Then each output is a sum of **n_in** products:

```
Var(y_j) = n_in · Var(W_ji · x_i)
         = n_in · σ²_W · σ²_x       (independence)
```

If we want **Var(y) = Var(x)** (signal preserved layer after layer):

> **σ²_W = 1 / n_in**

This is **LeCun init** for linear / tanh-type activations.

[↑ Back to Top](#-nn-advanced-weight-initialization--universal-approximation)

---

## 3. The Backward-Variance Argument

During backprop, gradients flow the other way: **∂L/∂x = Wᵀ · ∂L/∂y**. By the symmetric argument, to keep gradient variance constant we need:

> **σ²_W = 1 / n_out**

**Two competing constraints**, one from the forward pass (1/n_in) and one from the backward pass (1/n_out). Xavier/Glorot splits the difference.

[↑ Back to Top](#-nn-advanced-weight-initialization--universal-approximation)

---

## 4. Xavier / Glorot Init

Glorot & Bengio (2010) derived an init that balances forward and backward variance:

### Formulas
```
Normal:    W ~ N(0, 2 / (n_in + n_out))
Uniform:   W ~ U( −√(6 / (n_in + n_out)),  +√(6 / (n_in + n_out)) )
```

### When to use
- **tanh** or **sigmoid** activations (symmetric around 0)
- Shallow-to-moderate depth
- Default in many frameworks before He became standard

### Why it fails for ReLU
ReLU zeroes out half the activations on average. The forward-variance calculation loses a factor of 2, so Xavier under-initializes — gradients still vanish in deep ReLU nets.

[↑ Back to Top](#-nn-advanced-weight-initialization--universal-approximation)

---

## 5. He / Kaiming Init (for ReLU)

He et al. (2015) fixed the ReLU problem by doubling the variance:

### Formulas
```
Normal:    W ~ N(0, 2 / n_in)
Uniform:   W ~ U( −√(6 / n_in), +√(6 / n_in) )
```

The extra factor of 2 compensates for the half of inputs that ReLU kills.

### When to use
- **Any ReLU-family** activation (ReLU, LeakyReLU, PReLU)
- **Default for modern CNNs and most fully-connected nets**
- This is what PyTorch's `nn.Linear` uses by default with `kaiming_uniform_`

### PyTorch one-liner
```python
torch.nn.init.kaiming_normal_(layer.weight, mode='fan_in', nonlinearity='relu')
```

- `fan_in` preserves forward variance (standard).
- `fan_out` preserves backward variance (use if you train only partial layers).

[↑ Back to Top](#-nn-advanced-weight-initialization--universal-approximation)

---

## 6. LeCun Init

Original LeCun proposal (1998), revived with SELU:

### Formula
```
Normal:  W ~ N(0, 1 / n_in)
```

### When to use
- **SELU** activation — LeCun init + SELU is the "self-normalizing network" recipe (Klambauer et al. 2017).
- **tanh** shallow networks.
- Otherwise prefer Xavier or He.

[↑ Back to Top](#-nn-advanced-weight-initialization--universal-approximation)

---

## 7. Orthogonal Init

Saxe et al. (2014): initialize **W** as an orthogonal matrix (WᵀW = I) scaled by a gain factor.

### Why
- Preserves vector norms exactly (not just in expectation).
- Very stable for **RNNs** — stops the iterated state transition from exploding or vanishing.
- Less sensitive to depth.

### PyTorch
```python
torch.nn.init.orthogonal_(layer.weight, gain=torch.nn.init.calculate_gain('relu'))
```

### When to use
- RNNs (LSTMs, GRUs), especially the hidden-to-hidden matrix.
- Very deep fully-connected nets without normalization.

[↑ Back to Top](#-nn-advanced-weight-initialization--universal-approximation)

---

## 8. Biases, BatchNorm

### Biases
Almost always initialized to **0**. Non-zero bias init only matters in niches:
- **Forget-gate bias = 1** in LSTMs — helps information flow at the start.
- **Output layer bias = log(prior)** for heavily imbalanced classification.

### BatchNorm and "does init still matter?"
With BatchNorm, each layer's activations are normalized anyway, so the network is remarkably insensitive to weight init. **But** the first layer before BN still matters, and during early training (first ~100 steps) before BN stats stabilize, bad init can still cause divergence.

Short answer: **modern architectures with BN + proper He init are very robust.** Transformers without BN but with LayerNorm rely MORE on init than you might think.

[↑ Back to Top](#-nn-advanced-weight-initialization--universal-approximation)

---

## 9. Universal Approximation Theorem

### Statement (informal)
> A feedforward network with **one hidden layer** and a **non-polynomial** activation function (e.g. sigmoid, tanh, ReLU) can approximate **any continuous function** on a compact subset of ℝⁿ to **arbitrary precision** — given **enough hidden units**.

### What it does NOT say
- It says **nothing** about how to *find* the right weights.
- It says **nothing** about generalization.
- It says **nothing** about sample efficiency.
- "Enough hidden units" can mean exponentially many.

### Why depth helps (the modern counterpart)
Depth separations: there are functions representable by a **deep** ReLU net of size **O(n)** that require **O(2ⁿ)** units to represent with a single hidden layer (Telgarsky 2016, Eldan & Shamir 2016). Depth isn't just convenient — it's provably more **parameter-efficient** for some function classes.

### Takeaway
UAT justifies why neural nets *could* work. Depth + SGD + modern init + BN + tricks explain why they *actually* work.

[↑ Back to Top](#-nn-advanced-weight-initialization--universal-approximation)

---

## 10. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  INITIALIZATION ONE-LINERS                                   ║
╠══════════════════════════════════════════════════════════════╣
║  LeCun:   Var(W) = 1 / n_in          (SELU, tanh)           ║
║  Xavier:  Var(W) = 2 / (n_in+n_out)  (sigmoid, tanh)        ║
║  He:      Var(W) = 2 / n_in          (ReLU family)          ║
║  Orth:    W orthogonal · gain        (RNNs, deep FC)        ║
║                                                              ║
║  Biases → 0 (usually), except LSTM forget-bias = 1          ║
║  UAT: 1 hidden layer + non-poly activation → universal     ║
║  Depth lets you approximate with exponentially fewer units  ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Why does Xavier fail for ReLU?"** — ReLU kills half the inputs on average, so forward-variance loses a factor of 2 → use He (which doubles the variance).
2. **"What's the difference between fan_in and fan_out?"** — fan_in preserves forward-pass variance, fan_out preserves backward-pass variance; Xavier uses the average of both.
3. **"Why init biases to 0?"** — symmetry breaking is already handled by the random weights; non-zero biases only matter in special cases (LSTM forget gate, imbalanced output bias).
4. **"What does UAT say / not say?"** — says arbitrarily good approximation is possible with one hidden layer; says nothing about how to find the weights or how many you need.
5. **"Does BatchNorm make init irrelevant?"** — mostly yes, but not completely — BN needs good stats to kick in, and the very first layer still matters.

[↑ Back to Top](#-nn-advanced-weight-initialization--universal-approximation)

---

### 💻 Quick Code

```python
import torch
import torch.nn as nn

class Block(nn.Module):
    def __init__(self, in_dim, out_dim, activation="relu"):
        super().__init__()
        self.fc = nn.Linear(in_dim, out_dim)
        if activation == "relu":
            nn.init.kaiming_normal_(self.fc.weight, nonlinearity="relu")
        elif activation == "tanh":
            nn.init.xavier_normal_(self.fc.weight, gain=nn.init.calculate_gain("tanh"))
        elif activation == "selu":
            nn.init.kaiming_normal_(self.fc.weight, nonlinearity="linear")  # LeCun normal equivalent
        nn.init.zeros_(self.fc.bias)
```

---

> **Next:** [Optimizers →](ml_nn_adv_optimizers.md)
>
> *ML · Neural Networks Advanced · github.com/rpaut03l/TS-01*
