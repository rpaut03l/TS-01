# 📖 DL Advanced: Transfer Learning & Training Tricks

### *Fine-tuning · LR schedules · Warmup · Mixed precision · Augmentation · Mixup · Gradient accumulation*

> **Nav:** [← Modern CNNs](ml_dl_adv_modern_cnns.md) | [advanced README](README.md) | [← ML Master Index](../../ml_master_gap_index.md)

---

## 🧠 MNEMONIC: **"TFLAG-M"**

> **T**ransfer learning · **F**ine-tuning · **L**R schedules · **A**ugmentation · **G**radient accumulation · **M**ixed precision

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Transfer Learning — Why It Works | [§1](#1-transfer-learning--why-it-works) |
| 2 | Fine-Tuning Strategies | [§2](#2-fine-tuning-strategies) |
| 3 | Discriminative Learning Rates | [§3](#3-discriminative-learning-rates) |
| 4 | LR Warmup & Schedules | [§4](#4-lr-warmup--schedules) |
| 5 | Mixed Precision (FP16 / BF16) | [§5](#5-mixed-precision-fp16--bf16) |
| 6 | Gradient Accumulation | [§6](#6-gradient-accumulation) |
| 7 | Data Augmentation (Basic to Advanced) | [§7](#7-data-augmentation) |
| 8 | Mixup & CutMix | [§8](#8-mixup--cutmix) |
| 9 | Gradient Checkpointing (memory saver) | [§9](#9-gradient-checkpointing) |
| 10 | Distributed Training Basics | [§10](#10-distributed-training-basics) |
| 11 | Cheat Sheet | [§11](#11-cheat-sheet--exam-hacks) |

---

## 1. Transfer Learning — Why It Works

> **Train a model on a huge dataset once. Reuse it on your small problem.**

Deep nets learn hierarchical features:
- **Early layers:** edges, textures, colors — generic.
- **Middle layers:** motifs, parts — semi-generic.
- **Late layers:** task-specific categories.

The generic features transfer well across many tasks. This is why ImageNet-pretrained backbones still dominate small-dataset problems.

### Typical wins
- **10-100× less training data** needed.
- **Faster convergence** (hours vs days).
- **Better final accuracy** unless you truly have millions of labeled examples.

[↑ Back to Top](#-dl-advanced-transfer-learning--training-tricks)

---

## 2. Fine-Tuning Strategies

### Strategy 1 — Linear probing (fastest)
Freeze the entire pretrained model. Train only a new classification head.
- Use when: tiny dataset, limited compute, want to check what the features can do.
- PyTorch: `for p in model.parameters(): p.requires_grad = False`, then replace the head.

### Strategy 2 — Fine-tune everything
Unfreeze all parameters and train with a **small learning rate**.
- Use when: moderate dataset, you want the best accuracy.
- Learning rate ~10-100× smaller than scratch training (`1e-4` with AdamW is typical).

### Strategy 3 — Progressive unfreeze
Train the head first, then gradually unfreeze layers from top to bottom.
- Helps avoid catastrophic destruction of the pretrained features early in training.
- Popular in fastai ("discriminative fine-tuning").

### Strategy 4 — Low-rank adaptation (LoRA, QLoRA, etc.)
Keep the pretrained weights **frozen**. Add small **rank-r adapter matrices** and train only those.
- Dramatically cheaper for LLM fine-tuning.
- `W_effective = W_pretrained + B · A` where B, A are low-rank trainables.

[↑ Back to Top](#-dl-advanced-transfer-learning--training-tricks)

---

## 3. Discriminative Learning Rates

Different layers need different learning rates.
- **Early layers** (generic features) — barely change, use a tiny LR (1e-5).
- **Middle layers** — medium LR (1e-4).
- **Head** (randomly initialized) — full LR (1e-3).

### PyTorch
```python
optimizer = torch.optim.AdamW([
    {"params": model.backbone.parameters(),  "lr": 1e-5},
    {"params": model.middle.parameters(),    "lr": 1e-4},
    {"params": model.head.parameters(),      "lr": 1e-3},
], weight_decay=0.01)
```

[↑ Back to Top](#-dl-advanced-transfer-learning--training-tricks)

---

## 4. LR Warmup & Schedules

Two big levers on top of the optimizer choice.

### Warmup
Start with a tiny learning rate, **linearly ramp up** to the target over the first N steps (or epochs).
- Prevents huge, destructive updates during the first few steps when the gradient landscape is chaotic.
- **Transformers essentially always use warmup** (5-10% of training).
- CNNs with BN sometimes skip it.

### Cosine schedule
See [optimizers §9](../../Neural-Networks/advanced/ml_nn_adv_optimizers.md#9-learning-rate-schedules). Smoothly decay LR from peak to near 0 along a cosine curve after warmup. De facto standard for vision and most NLP training from scratch.

### Step decay
```
epoch 0-29:  lr = 1e-3
epoch 30-59: lr = 1e-4
epoch 60+:   lr = 1e-5
```
Old-school but still competitive for CNNs.

### One-cycle
Smith (2018). LR goes up then down in a big triangle; momentum does the inverse. Often converges faster than constant or cosine.

[↑ Back to Top](#-dl-advanced-transfer-learning--training-tricks)

---

## 5. Mixed Precision (FP16 / BF16)

Train most of the network in **half precision** (16-bit) and a few critical operations in full **FP32**. Result: 2-3× speedup + half the memory, with almost no accuracy loss.

### FP16 pitfalls
- **Smaller dynamic range** — underflow in gradients, overflow in loss.
- Need **loss scaling** — multiply loss by 2^k before backward, divide gradients by 2^k — to keep small gradients from underflowing to 0.
- PyTorch's `torch.cuda.amp.GradScaler` handles this automatically.

### BF16
- Same dynamic range as FP32 (both have 8 exponent bits).
- Less precision in the mantissa (7 vs 23 bits).
- No loss scaling needed.
- **Default on modern GPUs (A100+)** and TPUs.

### PyTorch AMP boilerplate
```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()
for x, y in loader:
    optimizer.zero_grad()
    with autocast(dtype=torch.float16):          # or torch.bfloat16
        logits = model(x)
        loss = criterion(logits, y)
    scaler.scale(loss).backward()
    scaler.unscale_(optimizer)
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    scaler.step(optimizer)
    scaler.update()
```

[↑ Back to Top](#-dl-advanced-transfer-learning--training-tricks)

---

## 6. Gradient Accumulation

You want a large effective batch size but your GPU can only fit a small one. **Accumulate gradients** across several mini-batches before stepping the optimizer.

```python
accum_steps = 4
optimizer.zero_grad()
for i, (x, y) in enumerate(loader):
    loss = criterion(model(x), y) / accum_steps
    loss.backward()
    if (i + 1) % accum_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

Result: **effective batch size = micro_batch × accum_steps**, without needing more GPU memory (except for activations during one forward/backward pass).

### Gotchas
- **BatchNorm stats** are still computed on the micro-batch size → may be noisy. Use LayerNorm / GroupNorm or increase the micro-batch if possible.
- **Effective LR is the large-batch LR**, not the micro-batch LR.

[↑ Back to Top](#-dl-advanced-transfer-learning--training-tricks)

---

## 7. Data Augmentation

### Basic (always do these)
- **Random horizontal flip** (unless symmetry is meaningful in your task).
- **Random resize & crop** (RandomResizedCrop).
- **Color jitter** — brightness, contrast, saturation, hue.
- **Normalize** — subtract ImageNet mean/std.

### Stronger modern cocktails
- **AutoAugment** (Cubuk 2018) — augmentation policies learned via reinforcement learning.
- **RandAugment** (Cubuk 2019) — simpler variant, two hyperparameters (N, M). **Default strong baseline.**
- **TrivialAugment** — one random op, one random strength. Even simpler, competitive.
- **AugMix** — mixes multiple augmented versions to improve robustness.

### Advanced
- **Random erasing** — blank out random rectangular regions.
- **Cutout** — similar, simpler.

### Text augmentation
- **Back-translation** (translate to another language and back).
- **Synonym replacement.**
- **Dropout on input embeddings.**

[↑ Back to Top](#-dl-advanced-transfer-learning--training-tricks)

---

## 8. Mixup & CutMix

Train not on single examples but on **linear combinations** of examples and labels.

### Mixup (Zhang et al. 2017)
```
λ ~ Beta(α, α)      α typically 0.2–0.4
x' = λ·x_i + (1−λ)·x_j
y' = λ·y_i + (1−λ)·y_j
```
- Use the smoothed (x', y') as the training example.
- **Regularizes** by forcing the model to behave linearly between training points.
- **Improves calibration** — predicted confidence matches accuracy better.
- **Improves adversarial robustness.**

### CutMix (Yun et al. 2019)
Cut a random rectangle from image B and paste it into image A. Label becomes a weighted mix based on area ratio.
- Preserves more local structure than mixup.
- Especially good on images; default in many modern vision recipes.

### MixUp vs CutMix vs Label Smoothing
All three are "soften the targets" style regularizers that consistently improve generalization by ~0.5-2% on ImageNet classification. Usually combined.

[↑ Back to Top](#-dl-advanced-transfer-learning--training-tricks)

---

## 9. Gradient Checkpointing

Save activations only at a few **checkpoints** instead of every layer. Recompute them on the backward pass.

```
MEMORY: O(√N) instead of O(N)     (N = depth)
TIME:   ~30% slower
```

Useful when:
- You're training a huge model that doesn't fit.
- You want a bigger batch size.
- You're willing to trade compute for memory.

### PyTorch
```python
from torch.utils.checkpoint import checkpoint

def forward(x):
    x = checkpoint(block1, x)          # recompute activations on backward
    x = checkpoint(block2, x)
    return x
```

[↑ Back to Top](#-dl-advanced-transfer-learning--training-tricks)

---

## 10. Distributed Training Basics

### Data Parallel (DP / DDP)
- Each GPU has a **full copy** of the model.
- The batch is **split** across GPUs.
- Gradients are **averaged** across GPUs (via all-reduce).
- Linear scaling up to a point.
- **DDP** (DistributedDataParallel) is the correct choice; plain DP is slower.

### Model Parallel
- **Tensor parallel** — split a single matrix multiply across GPUs (Megatron).
- **Pipeline parallel** — put layers on different GPUs, run batches as a pipeline.
- Used when the model doesn't fit in one GPU.

### ZeRO / FSDP
Shard optimizer states, gradients, and parameters across GPUs. Enables trillion-parameter training with "DP-like" ergonomics.

### Sharded / Fully-Sharded Data Parallel (FSDP)
PyTorch's native answer to DeepSpeed ZeRO. Now standard for large-model training.

[↑ Back to Top](#-dl-advanced-transfer-learning--training-tricks)

---

## 11. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  THE MODERN TRAINING CHECKLIST                               ║
╠══════════════════════════════════════════════════════════════╣
║  ✅ Start from a pretrained backbone                         ║
║  ✅ AdamW + cosine schedule + linear warmup                  ║
║  ✅ Mixed precision (AMP / BF16)                             ║
║  ✅ Strong data augmentation (RandAugment)                   ║
║  ✅ Mixup / CutMix                                           ║
║  ✅ Label smoothing 0.1                                      ║
║  ✅ Weight decay 0.05 (vision) / 0.01 (NLP)                  ║
║  ✅ Gradient clipping max_norm = 1.0                         ║
║  ✅ Discriminative LRs for fine-tuning                       ║
║  ✅ Save best-validation checkpoint (early stopping-ish)     ║
║  ✅ Gradient checkpointing if memory is tight                ║
║  ✅ DDP (not DP) for multi-GPU                               ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Why warmup?"** — initial gradients are chaotic; small LR prevents destructive early updates.
2. **"FP16 vs BF16?"** — FP16 has higher precision but smaller range (needs loss scaling); BF16 has FP32 range but less precision (no loss scaling needed). BF16 is easier on modern hardware.
3. **"Gradient accumulation effect?"** — increases effective batch size without using more memory; LR should match the effective (large) batch, not the micro-batch.
4. **"Why mixup?"** — linearizes the model between training points, improves generalization, calibration, and adversarial robustness.
5. **"Discriminative LR for fine-tuning?"** — early layers (generic features) use a tiny LR; later layers and the new head use larger LRs to avoid destroying pretrained features.
6. **"LoRA — what's it for?"** — train only small low-rank adapter matrices while keeping the pretrained model frozen; dramatically cheaper for LLM fine-tuning.
7. **"DDP vs DP?"** — DDP uses separate processes per GPU with efficient all-reduce; DP uses one process with lots of Python-side overhead. Always use DDP.

[↑ Back to Top](#-dl-advanced-transfer-learning--training-tricks)

---

### 💻 Quick Code — minimal modern training loop

```python
import torch, torch.nn as nn
from torch.utils.data import DataLoader
from torch.optim.lr_scheduler import OneCycleLR
from torch.cuda.amp import autocast, GradScaler

model = ...            # pretrained backbone + new head
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=0.05)
scheduler = OneCycleLR(optimizer, max_lr=3e-4, total_steps=total_steps,
                       pct_start=0.1, anneal_strategy="cos")
criterion = nn.CrossEntropyLoss(label_smoothing=0.1)
scaler = GradScaler()

for x, y in loader:
    x, y = x.cuda(), y.cuda()
    optimizer.zero_grad()
    with autocast(dtype=torch.bfloat16):
        logits = model(x)
        loss = criterion(logits, y)
    scaler.scale(loss).backward()
    scaler.unscale_(optimizer)
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    scaler.step(optimizer)
    scaler.update()
    scheduler.step()
```

---

> **Back to:** [advanced README](README.md) · [← ML Master Index](../../ml_master_gap_index.md)
>
> *ML · Deep Learning Advanced · github.com/rpaut03l/TS-01*
