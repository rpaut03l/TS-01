# 📖 DL Advanced: Modern CNN Architectures & Vision Transformers

### *ResNet · DenseNet · MobileNet · EfficientNet · ViT · ConvNeXt*

> **Nav:** [← Generative](ml_dl_adv_generative.md) | [advanced README](README.md) | [Transfer & Training Tricks →](ml_dl_adv_transfer_tricks.md)

---

## 🧠 MNEMONIC: **"REMEV-C"**

> **R**esNet · **E**fficientNet · **M**obileNet · **E**volution of backbones · **V**iT · **C**onvNeXt

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Pre-Residual Era (Quick Recap) | [§1](#1-pre-residual-era) |
| 2 | ResNet — Skip Connections | [§2](#2-resnet--skip-connections) |
| 3 | DenseNet — Feature Reuse | [§3](#3-densenet--feature-reuse) |
| 4 | MobileNet — Depthwise Separable Conv | [§4](#4-mobilenet) |
| 5 | EfficientNet — Compound Scaling | [§5](#5-efficientnet) |
| 6 | Vision Transformer (ViT) | [§6](#6-vision-transformer-vit) |
| 7 | Hybrid & ConvNeXt | [§7](#7-hybrid--convnext) |
| 8 | Choosing an Architecture in 2026 | [§8](#8-choosing-an-architecture-in-2026) |
| 9 | Cheat Sheet | [§9](#9-cheat-sheet--exam-hacks) |

---

## 1. Pre-Residual Era

Quick recap of the history before ResNet:

- **LeNet-5** (1998) — 7 layers, MNIST.
- **AlexNet** (2012) — 8 layers, ReLU, dropout, GPUs, ImageNet breakthrough.
- **VGG-16/19** (2014) — stacks of 3×3 conv, very deep but no tricks.
- **GoogLeNet / Inception v1** (2014) — inception modules, 1×1 conv bottlenecks.
- **Inception v2/v3** — factorized convolutions, BatchNorm.

Stacking more layers naïvely (VGG-50) **hurt** accuracy. People assumed depth was hitting a limit. It wasn't — they just needed skip connections.

[↑ Back to Top](#-dl-advanced-modern-cnn-architectures--vision-transformers)

---

## 2. ResNet — Skip Connections

He et al. (2015). The paper that unlocked very deep networks.

### The residual block
```
y = F(x) + x
```
where F is a tiny sub-network (e.g., two 3×3 convs with BN + ReLU).

```
┌──────────────┐
│    x         │
│    ├────────────┐
│    ▼            │
│  3×3 conv       │
│  BN, ReLU       │
│  3×3 conv       │
│  BN             │
│    +────────────┘    (add x)
│  ReLU
└──────────────┘
```

### Why it works
- **Gradient flow** — identity path guarantees gradient reaches early layers.
- **Identity initialization** — if F is near 0 at init, the block is the identity → deeper networks never hurt.
- **Optimization landscape** is smoother.

### Bottleneck variant (ResNet-50+)
```
1×1 conv  (dim → dim/4)
3×3 conv  (dim/4 → dim/4)
1×1 conv  (dim/4 → dim)
```
Cheaper and deeper. ResNet-50, -101, -152 all use this.

### Variants
- **Pre-activation ResNet** — put BN/ReLU *before* the conv (He et al. 2016).
- **Wide ResNet** — fewer layers, wider — sometimes better accuracy/parameter ratio.
- **ResNeXt** — grouped convolutions inside the bottleneck.

### Staying power
ResNet-50 with modern training tricks is still competitive in 2026 for many tasks — a testament to how well skip connections scale.

[↑ Back to Top](#-dl-advanced-modern-cnn-architectures--vision-transformers)

---

## 3. DenseNet — Feature Reuse

Huang et al. (2017). Instead of adding x + F(x), **concatenate** all previous layers' outputs.

```
x_l = H_l([x_0, x_1, ..., x_{l-1}])
```

### Pros
- **Strong feature reuse** — parameters are more efficient.
- **Gradient flow** is even better than ResNet.
- **Smaller models** for similar accuracy.

### Cons
- **Memory-hungry** — every layer's output is kept around.
- **Implementation complex** in some frameworks.
- Less popular than ResNet in practice.

[↑ Back to Top](#-dl-advanced-modern-cnn-architectures--vision-transformers)

---

## 4. MobileNet

Howard et al. (2017). Designed for **mobile / edge** devices — trades a bit of accuracy for 8-10× fewer FLOPs.

### Depthwise separable convolution
Standard conv does **spatial filtering + channel mixing** in one operation. Depthwise separable splits them:
```
1. Depthwise:  apply one k×k filter PER CHANNEL  (no channel mixing)
2. Pointwise:  1×1 conv to mix channels
```
This cuts the cost from **k² · C_in · C_out** to **k² · C_in + C_in · C_out**. For a 3×3 conv, roughly **8-9× fewer multiplications**.

### MobileNet v2
Adds **inverted residuals** and **linear bottlenecks** — expand, depthwise, project back down.

### MobileNet v3
Adds **squeeze-and-excitation** blocks + **hard-swish** activation + neural architecture search.

### Use
- On-device inference (phones, embedded).
- Real-time applications with tight latency budgets.

[↑ Back to Top](#-dl-advanced-modern-cnn-architectures--vision-transformers)

---

## 5. EfficientNet

Tan & Le (2019). **Compound scaling**: instead of scaling depth, width, or resolution independently, scale all three together with a principled ratio.

### The formula
```
depth      = α^φ
width      = β^φ
resolution = γ^φ
subject to:  α · β² · γ² ≈ 2        (keeps compute roughly 2^φ)
```

- φ is a single **scaling coefficient** that controls the size of the model.
- EfficientNet-B0 through B7 are the same architecture at different scales.

### Base architecture
Built from **MBConv** blocks (mobile inverted bottleneck with SE) discovered via neural architecture search.

### Key result
At the same accuracy, EfficientNet-B7 uses **8× fewer parameters** and **6× fewer FLOPs** than comparable ResNets at the time of publication.

### EfficientNet v2
Tan & Le (2021). Uses fused MBConv early in the network (actual conv, not depthwise separable, when small), trains faster.

[↑ Back to Top](#-dl-advanced-modern-cnn-architectures--vision-transformers)

---

## 6. Vision Transformer (ViT)

Dosovitskiy et al. (2020). Take the transformer from NLP and apply it to image patches with minimal changes.

### The idea
Chop an image into **patches** (e.g., 16×16), flatten each, linearly project to an embedding, add **positional embeddings**, feed into a standard transformer encoder.

```
H×W image
  ─→ patches of 16×16 ─→ [N, 256]  where N = H·W/256
     linear project ─→ [N, d_model]
     + positional encoding
     + [CLS] token (optional)
  ─→ Transformer Encoder (L blocks)
  ─→ classification head on [CLS] token (or global average pool)
```

### Key findings
- **Beats ResNets** when pretrained on large datasets (JFT-300M).
- **Loses** to ResNets when trained from scratch on small datasets — ViT needs data to learn the locality inductive biases that conv nets get for free.
- Works best as a **pretrained backbone** (ImageNet or larger).

### DeiT (Touvron et al. 2020)
Shows ViT can be trained on ImageNet **alone** with:
- Strong data augmentation
- Knowledge distillation from a CNN teacher
- Specific training recipe (AdamW, cosine schedule, etc.)

### Swin Transformer (Liu et al. 2021)
**Hierarchical** ViT with **shifted windows**. Reintroduces some local inductive bias:
- Compute attention only within windows (not globally) → O(n) not O(n²) in image size.
- Shift windows between blocks to allow information flow across windows.
- Pyramidal feature maps (like a CNN) → good for dense prediction (detection, segmentation).

[↑ Back to Top](#-dl-advanced-modern-cnn-architectures--vision-transformers)

---

## 7. Hybrid & ConvNeXt

### The "CNN vs Transformer" debate (~2021)
Transformers were claimed to dominate vision. Then Liu et al. (2022, **ConvNeXt**) modernized a plain ResNet with:
- 7×7 depthwise convs (matching ViT's large receptive field)
- GELU instead of ReLU
- LayerNorm instead of BN
- Fewer activations per block
- Larger kernel, smaller stem
- Inverted bottleneck

The result: a **pure CNN** that matched Swin Transformer. The takeaway: **training recipe matters more than architecture family**.

### Hybrid architectures
Many modern backbones mix conv and attention:
- **CoAtNet** — conv early, attention late (for local vs global features).
- **MobileViT** — CNN backbone with ViT blocks in the middle.
- **EfficientFormer** — low-latency hybrid for mobile.

[↑ Back to Top](#-dl-advanced-modern-cnn-architectures--vision-transformers)

---

## 8. Choosing an Architecture in 2026

```
┌────────────────────────┬────────────────────────────────────┐
│ GOAL                   │ PICK                               │
├────────────────────────┼────────────────────────────────────┤
│ Baseline, transfer     │ ResNet-50 or ConvNeXt-Tiny         │
│ Tight compute          │ MobileNet v3 or EfficientNet-B0    │
│ Huge data + budget     │ ViT-L/16 or Swin-L, pretrained     │
│ Detection/segmentation │ Swin + Mask R-CNN / DETR           │
│ On-device realtime     │ MobileNet v3 + quantization        │
│ Self-supervised        │ ViT + MAE or DINO                  │
│ Small dataset fine-tune│ ImageNet ResNet-50 or ConvNeXt     │
└────────────────────────┴────────────────────────────────────┘
```

> **Rule:** pretrain on a big dataset first, then fine-tune on yours. The backbone family is usually a smaller effect than the pretraining corpus.

[↑ Back to Top](#-dl-advanced-modern-cnn-architectures--vision-transformers)

---

## 9. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  MODERN CNN / VISION BACKBONES                               ║
╠══════════════════════════════════════════════════════════════╣
║  ResNet:       y = F(x) + x    — identity skip               ║
║  DenseNet:     concat of all prev layers                     ║
║  MobileNet:    depthwise separable conv → 8-9× fewer FLOPs   ║
║  EfficientNet: compound scaling (α^φ · β^2φ · γ^2φ)          ║
║  ViT:          patches → transformer encoder → CLS token     ║
║  Swin:         window attention + shifted windows → O(n)     ║
║  ConvNeXt:     modernized ResNet matches ViT performance     ║
║                                                              ║
║  Best training recipe >> architecture family                 ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Why ResNet works?"** — identity skip gives gradient a clean path + starting-from-identity means extra layers never hurt.
2. **"Depthwise separable convolution — savings?"** — roughly (k²·C_in·C_out) → (k²·C_in + C_in·C_out); ~8-9× for 3×3.
3. **"Compound scaling?"** — scale depth, width, and input resolution together with a fixed ratio rather than tuning them independently.
4. **"Why does ViT need so much data?"** — it has no built-in locality inductive bias; CNNs get for free what ViT must learn from data.
5. **"Swin's key innovation?"** — window-local attention + shifted windows → linear complexity in image size + cross-window information flow.
6. **"ConvNeXt's main message?"** — with the right training recipe and small architectural tweaks, pure CNNs still match transformers.

[↑ Back to Top](#-dl-advanced-modern-cnn-architectures--vision-transformers)

---

### 💻 Quick Code

```python
import torch
import torchvision.models as models

# Pretrained backbones — pick one
resnet50 = models.resnet50(weights="IMAGENET1K_V2")
efficientnet_b0 = models.efficientnet_b0(weights="IMAGENET1K_V1")
mobilenet_v3 = models.mobilenet_v3_large(weights="IMAGENET1K_V2")
convnext_tiny = models.convnext_tiny(weights="IMAGENET1K_V1")
vit_b_16 = models.vit_b_16(weights="IMAGENET1K_SWAG_E2E_V1")
swin_t = models.swin_t(weights="IMAGENET1K_V1")

# Replace the classifier head for transfer learning
import torch.nn as nn
resnet50.fc = nn.Linear(resnet50.fc.in_features, num_classes=10)
```

---

> **Next:** [Transfer & Training Tricks →](ml_dl_adv_transfer_tricks.md)
>
> *ML · Deep Learning Advanced · github.com/rpaut03l/TS-01*
