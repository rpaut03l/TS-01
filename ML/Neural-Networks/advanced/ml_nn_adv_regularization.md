# 📖 NN Advanced: Regularization — Dropout · BatchNorm · LayerNorm · Weight Decay

### *Why deep nets memorize, and the tricks that prevent it*

> **Nav:** [← Optimizers](ml_nn_adv_optimizers.md) | [advanced README](README.md) | [Gradients & Activations →](ml_nn_adv_gradients_activations.md)

---

## 🧠 MNEMONIC: **"DB-WELS"**

> **D**ropout · **B**atchNorm · **W**eight-decay · **E**arly-stopping · **L**abel-smoothing · **S**tochastic depth

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Why Regularize a Neural Net? | [§1](#1-why-regularize-a-neural-net) |
| 2 | Weight Decay / L2 | [§2](#2-weight-decay--l2) |
| 3 | Dropout | [§3](#3-dropout) |
| 4 | Batch Normalization | [§4](#4-batch-normalization) |
| 5 | Layer Normalization (and friends) | [§5](#5-layer-normalization-and-friends) |
| 6 | Early Stopping | [§6](#6-early-stopping) |
| 7 | Label Smoothing | [§7](#7-label-smoothing) |
| 8 | Stochastic Depth & Other Drop\* Variants | [§8](#8-stochastic-depth--other-drop-variants) |
| 9 | Regularizers as Priors (Bayesian view) | [§9](#9-regularizers-as-priors) |
| 10 | Cheat Sheet | [§10](#10-cheat-sheet--exam-hacks) |

---

## 1. Why Regularize a Neural Net?

A modern deep net has **more parameters than training examples**. It can (and will) memorize the training set if you don't prevent it.

```
TYPICAL SIGN OF OVERFIT
  train loss   ↓ ↓ ↓   (near 0)
  val loss     ↓ then ↑  (U-shape)
```

Regularization = anything that **reduces the effective capacity** (or the effective number of independent parameters) without reducing the model's ability to fit real patterns. The dream: **underfit slightly less than you would otherwise**, generalize better.

[↑ Back to Top](#-nn-advanced-regularization)

---

## 2. Weight Decay / L2

### Formula
Add a penalty to the loss:
```
L_reg = L_data + (λ/2) · ‖θ‖²
```
Equivalently, at each step:
```
θ ← θ − η · (∇L_data + λ · θ)
```

### Effect
- Pulls weights toward **zero** (unless the data supports them being larger).
- Reduces variance of the estimated weights.
- Corresponds to a **Gaussian prior** on θ (MAP view — see [Parameter Estimation](../../Parameter-Estimations-Guide/ml_parameter_estimation_theory.md)).

### Typical values
- **λ = 1e−4** for CNNs.
- **λ = 0.01 – 0.1** for transformers (larger because of AdamW decoupling).
- **λ = 0** is rarely a good default for deep nets.

### Gotcha with Adam
Plain Adam + L2 is broken — see [AdamW discussion](ml_nn_adv_optimizers.md#8-adamw). Use AdamW instead.

[↑ Back to Top](#-nn-advanced-regularization)

---

## 3. Dropout

Srivastava et al. (2014). At each training step, **randomly zero out** a fraction **p** of activations.

```
TRAIN   y = mask · x / (1 − p)        (mask ~ Bernoulli(1 − p))
EVAL    y = x
```

### Why it works (interpretations)
1. **Ensemble** — each minibatch trains a different subnetwork; inference averages them.
2. **Co-adaptation break** — prevents neurons from relying on specific other neurons.
3. **Noise injection** — adds stochastic regularization similar to Gaussian noise.

### Typical rates
- **p = 0.5** for fully-connected hidden layers (original paper).
- **p = 0.1 – 0.3** for convolutional layers (CNNs have their own regularization via weight sharing).
- **p = 0.1** inside transformers (standard BERT/GPT).
- **NEVER** on the input layer (rarely helps).
- **NEVER** on the output layer.

### Inverse scaling (the "/ (1 − p)" trick)
During training we divide by (1 − p) so that the expected magnitude of the output is unchanged. This means **no scaling is needed at eval time** — you just turn dropout off.

### When dropout hurts
- Small models (it actually pushes them to underfit).
- CNNs with BatchNorm (BN is already regularizing).
- Very large models trained with enough data — they might not need it.

[↑ Back to Top](#-nn-advanced-regularization)

---

## 4. Batch Normalization

Ioffe & Szegedy (2015). Normalize each **feature channel** across the **batch** dimension.

### Forward pass
```
For each feature j in layer:
  μ_B = (1/m) Σ x_ij                          (mean over batch)
  σ²_B = (1/m) Σ (x_ij − μ_B)²                (variance over batch)
  x̂_ij = (x_ij − μ_B) / √(σ²_B + ε)            (normalize)
  y_ij = γ_j · x̂_ij + β_j                     (scale + shift — learnable)
```

### At inference
Use **running averages** of μ and σ² accumulated during training (not the current mini-batch — that would make inference depend on batch composition).

### Why it works (official story vs reality)
- **Official story:** reduces "internal covariate shift" — the input distribution of each layer stays stationary.
- **Reality (Santurkar et al. 2018):** the real benefit is that BN **smooths the loss landscape**, allowing larger learning rates and faster convergence.

### Effects
1. **Allows higher learning rates** (5–10× larger).
2. **Acts as regularizer** (batch noise is a form of stochastic augmentation).
3. **Makes init less important.**
4. **Speeds up convergence.**

### Gotchas
- **Small batches (B < 8)** — BN stats are noisy → use LayerNorm or GroupNorm instead.
- **Distributed training** — sync BN across GPUs or use the local-batch approximation carefully.
- **Train/eval mismatch** — forgetting `model.eval()` means BN uses the current mini-batch stats at inference. Classic bug.
- **RNNs** — BN is awkward because the time dimension and the batch dimension interact.

[↑ Back to Top](#-nn-advanced-regularization)

---

## 5. Layer Normalization (and friends)

Ba et al. (2016). Normalize across the **feature** dimension within **each sample**, so the normalization is independent of batch composition.

### LayerNorm formula
```
For each sample i:
  μᵢ  = (1/d) Σ_j x_ij          (mean over features)
  σ²ᵢ = (1/d) Σ_j (x_ij − μᵢ)²
  x̂_ij = (x_ij − μᵢ) / √(σ²ᵢ + ε)
  y_ij = γ_j · x̂_ij + β_j
```

### Why transformers use LayerNorm (not BatchNorm)
- **Variable sequence length** — BN stats would be averaged over nonsense positions.
- **Small per-step batches** — BN with B = 1 makes no sense.
- **Recurrence** — LN works per-step; BN doesn't.

### GroupNorm (Wu & He 2018)
Split features into **G groups**, normalize within each group. Interpolates between LayerNorm (G=1) and InstanceNorm (G = channels). Works well for small-batch vision (e.g., detection, segmentation).

### InstanceNorm
Normalize each channel of each sample independently. Popular in **style transfer**.

### RMSNorm (Zhang & Sennrich 2019)
LayerNorm without the mean-subtraction step — just scale by RMS. Cheaper, works well, now used in **LLaMA / modern LLMs**.

```
RMS(x) = √( (1/d) Σ x_j² )
y = x / RMS(x) · γ
```

[↑ Back to Top](#-nn-advanced-regularization)

---

## 6. Early Stopping

The simplest, most effective regularizer.

```
ALGORITHM
  1. Monitor validation loss after each epoch.
  2. If val_loss stops improving for K epochs ("patience"), stop training.
  3. Return the weights from the best val-loss epoch, not the last epoch.
```

### Why it works
Training trajectory goes through a "sweet spot" where the model has learned signal but not yet memorized noise. Early stopping picks that spot automatically.

### Equivalence
Early stopping is **provably equivalent** to L2 regularization for linear models, and **approximately equivalent** for deep nets (Bishop 1995, Yao et al. 2007).

### Hyperparameters
- **Patience:** 5–20 epochs.
- **Min delta:** how much improvement counts (e.g., 1e−4).
- **Save best weights** — not the final ones.

[↑ Back to Top](#-nn-advanced-regularization)

---

## 7. Label Smoothing

Szegedy et al. (2016). Replace hard 1-hot labels with a softer distribution.

```
y_true = [0, 0, 1, 0, 0]        (standard 1-hot)
y_smooth = [ε/K, ε/K, 1−ε+ε/K, ε/K, ε/K]   (with ε = 0.1, K = 5 classes)
```

### Why
- Prevents the model from becoming **over-confident** (pushing logits to ±∞).
- **Calibrates** probabilities — predicted confidences match actual accuracies better.
- **Improves generalization** — forces the feature space to have non-trivial inter-class structure.
- Standard in **transformers** (GPT, ViT) and **modern CNNs**.

### Cross-entropy with label smoothing
```
L = − (1 − ε) · log p(y_true) − (ε / K) · Σ_k log p(k)
```

### Typical values
- **ε = 0.1** for image classification
- **ε = 0.1** for machine translation
- **ε = 0** for safety-critical tasks where you want sharp probabilities (rare)

[↑ Back to Top](#-nn-advanced-regularization)

---

## 8. Stochastic Depth & other Drop-* variants

| Name | What's dropped | Used in |
|---|---|---|
| **Dropout** | individual activations | FCs, transformers |
| **DropConnect** | individual weights | rarely |
| **Spatial dropout** | entire feature maps | CNNs |
| **Stochastic depth** | entire residual blocks | ResNet, EfficientNet |
| **DropPath** | residual connection output | ViT, ConvNeXt |
| **DropBlock** | contiguous regions of feature maps | detection |

### Stochastic depth
Huang et al. (2016). During training, randomly **skip** an entire residual block with probability p. At inference, always use it but scale down the residual by (1 − p).

```
TRAIN:  out = x + BernoulliMask(1 − p) · Block(x)
EVAL:   out = x + (1 − p) · Block(x)
```

Lets you train 1000-layer networks (Huang et al. 2016) and is a staple of modern vision backbones.

[↑ Back to Top](#-nn-advanced-regularization)

---

## 9. Regularizers as Priors

Bayesian view: **L_data = −log p(D|θ)**, **L_reg = −log p(θ)**.

| Regularizer | Equivalent prior |
|---|---|
| L2 (‖θ‖²) | Gaussian θ ~ N(0, 1/λ) |
| L1 (‖θ‖₁) | Laplace θ ~ Lap(0, 1/λ) |
| Dropout | Approximate Bayesian inference (Gal & Ghahramani 2016) |
| Weight decay on BN γ | Gaussian on scale factor |

Dropout being a kind of **approximate variational inference** is neat: you can interpret dropout at inference time (leaving it ON) as sampling from an approximate posterior → gives you **uncertainty estimates** for free.

[↑ Back to Top](#-nn-advanced-regularization)

---

## 10. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  WHICH REGULARIZER WHEN                                      ║
╠══════════════════════════════════════════════════════════════╣
║  Default stack:  AdamW (weight decay) + dropout + early stop ║
║  Images (CNN):   + BatchNorm + data aug + label smoothing    ║
║  Transformers:   + LayerNorm + dropout 0.1 + label smooth    ║
║  Tiny data:      stronger dropout, early stop, augmentation  ║
║  Tiny model:     LESS regularization                         ║
║  RNNs:           LayerNorm (not BatchNorm), dropout on non-  ║
║                  recurrent connections, gradient clipping    ║
║  Distillation:   label-smoothed teacher logits               ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Why use the (1−p) rescaling in dropout?"** — to keep the expected activation magnitude constant; inference can then use the raw values (no extra scaling).
2. **"Why not BatchNorm in transformers?"** — variable sequence length, small batches, and sample-level position dependence make LayerNorm more natural.
3. **"Why is Adam + L2 different from AdamW?"** — in Adam, L2 is scaled by the adaptive learning rate, so parameters with big gradients get too little regularization.
4. **"What's label smoothing doing?"** — preventing the logits from exploding to ±∞, calibrating probabilities, regularizing via a softer target distribution.
5. **"Early stopping ≈ L2?"** — yes, approximately; both reduce the effective number of gradient steps that pull toward the memorization region.
6. **"BatchNorm at eval time?"** — use the running averages, not current-batch stats. Forgetting `model.eval()` is a common bug.

[↑ Back to Top](#-nn-advanced-regularization)

---

### 💻 Quick Code

```python
import torch.nn as nn

# Typical CNN block
block = nn.Sequential(
    nn.Conv2d(64, 128, kernel_size=3, padding=1),
    nn.BatchNorm2d(128),
    nn.ReLU(inplace=True),
    nn.Dropout2d(p=0.1),
)

# Typical transformer block (partial)
tblock = nn.Sequential(
    nn.LayerNorm(768),
    nn.Linear(768, 3072),
    nn.GELU(),
    nn.Dropout(p=0.1),
    nn.Linear(3072, 768),
    nn.Dropout(p=0.1),
)

# Loss with label smoothing (PyTorch ≥ 1.10)
import torch.nn.functional as F
loss = F.cross_entropy(logits, targets, label_smoothing=0.1)
```

---

> **Next:** [Gradients & Activations →](ml_nn_adv_gradients_activations.md)
>
> *ML · Neural Networks Advanced · github.com/rpaut03l/TS-01*
