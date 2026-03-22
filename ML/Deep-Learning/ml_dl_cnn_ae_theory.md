# 📖 Deep Learning Foundations: DNN · CNN · Autoencoders

### *Deep Neural Networks · Convolutions · Pooling · Autoencoders*

> **Nav:** [← Neural Networks](../Neural-Networks/ml_nn_mlp_bp_theory.md) | **Deep Learning** | [← ML Master Index](../ml_master_gap_index.md)

---

## 🧠 MNEMONIC: **"CAPS-DAB"**

> **C**onvolution · **A**utoencoder · **P**ooling · **S**tride · **D**ropout · **A**rchitecture · **B**atch normalization

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | DNN — Going Deep | [§1](#1-dnn--going-deep) |
| 2 | CNN Architecture | [§2](#2-cnn--convolutional-neural-networks) |
| 3 | Convolution Operation | [§3](#3-convolution-operation) |
| 4 | Pooling | [§4](#4-pooling) |
| 5 | CNN Architectures | [§5](#5-famous-cnn-architectures) |
| 6 | Autoencoders | [§6](#6-autoencoders) |
| 7 | Training Deep Networks | [§7](#7-training-deep-networks) |
| 8 | Numericals | [§8](#8-numericals) |
| 9 | Cheat Sheet | [§9](#9-cheat-sheet--exam-hacks) |

---

## 1. DNN — Going Deep

### 👶 Easy Story
An MLP with 1-2 hidden layers is like recognizing a dog by checking "has fur? has legs?" A DEEP neural network (many layers) is like: Layer 1 detects edges, Layer 2 detects shapes (circles, lines), Layer 3 detects parts (ears, nose, tail), Layer 4 detects the whole dog. Each layer builds on the previous one — like building blocks!

```
DEEP = many hidden layers (typically 3+, can be 100+)

  Shallow (1-2 layers):          Deep (many layers):
  Input → [Hidden] → Output     Input → [H1] → [H2] → [H3] → ... → Output
                                          ↑      ↑      ↑
                                        edges  shapes  objects

CHALLENGES OF GOING DEEP:
  1. Vanishing gradients: gradients shrink to ~0 in early layers
     Fix: ReLU, ResNet skip connections, batch normalization
  2. Exploding gradients: gradients blow up to infinity
     Fix: gradient clipping, proper initialization (Xavier/He)
  3. Overfitting: too many parameters
     Fix: dropout, L2 regularization, data augmentation, early stopping
  4. Computation: slow training
     Fix: GPU/TPU, mini-batch SGD, Adam optimizer

KEY IDEAS:
  Xavier init:  W ~ N(0, 1/n_in)          (for sigmoid/tanh)
  He init:      W ~ N(0, 2/n_in)          (for ReLU)
  Batch Norm:   normalize activations per mini-batch → stable training
  Dropout:      randomly set p% of neurons to 0 during training → regularization
  Skip connections: add input of layer to output (ResNet: x + F(x))
```

[↑ Back to Top](#-deep-learning-foundations-dnn--cnn--autoencoders)

---

## 2. CNN — Convolutional Neural Networks

### 👶 Easy Story
When you look at a photo, your eyes don't scan every pixel independently. You look at SMALL patches: "this patch has an edge," "this patch has a colour," "this patch has an eye." CNNs do the same — they slide a small window (filter/kernel) across the image, detecting local patterns!

```
CNN ARCHITECTURE:
━━━━━━━━━━━━━━━━
  INPUT IMAGE → [CONV → ReLU → POOL] × N → FLATTEN → FC → OUTPUT
  
  CONV:    detect local features (edges, textures, shapes)
  ReLU:    activation (non-linearity)
  POOL:    downsample (reduce size, keep important info)
  FLATTEN: reshape 2D feature maps → 1D vector
  FC:      fully connected layer(s) for final classification

  IMAGE (32×32×3)
    ↓
  [Conv 5×5, 32 filters] → 28×28×32
    ↓ ReLU
  [MaxPool 2×2] → 14×14×32
    ↓
  [Conv 5×5, 64 filters] → 10×10×64
    ↓ ReLU
  [MaxPool 2×2] → 5×5×64
    ↓ Flatten
  [1600] → [FC 256] → [FC 10] → Softmax → 10 classes

KEY: Parameter sharing! One filter scans the ENTIRE image.
  MLP on 32×32×3 image: 3072 × hidden_size weights
  CNN 5×5 filter: only 5×5×3 + 1 = 76 weights! (MUCH fewer)
```

[↑ Back to Top](#-deep-learning-foundations-dnn--cnn--autoencoders)

---

## 3. Convolution Operation

```
CONVOLUTION (2D):
━━━━━━━━━━━━━━━━
  Input image I (H × W), Filter/Kernel K (f × f)
  Output: O[i,j] = Σₘ Σₙ I[i+m, j+n] × K[m, n]
  
  Slide the filter across the image, multiply-and-sum at each position.

EXAMPLE (3×3 filter on 5×5 input, stride=1, no padding):
  Input:           Filter:        Output:
  [1 2 3 0 1]     [1 0 1]        [? ? ?]
  [0 1 2 3 1]     [0 1 0]        [? ? ?]
  [1 0 1 2 0]     [1 0 1]        [? ? ?]
  [2 1 0 1 3]
  [1 0 2 1 0]

  O[0,0] = 1×1+2×0+3×1 + 0×0+1×1+2×0 + 1×1+0×0+1×1
         = 1+0+3 + 0+1+0 + 1+0+1 = 7

OUTPUT SIZE FORMULA:
  O = (I - K + 2P) / S + 1
  where I=input size, K=kernel size, P=padding, S=stride

  Example: I=32, K=5, P=0, S=1 → O = (32-5+0)/1 + 1 = 28

PADDING:
  "valid":  no padding → output smaller than input
  "same":   pad so output = same size as input (P = (K-1)/2)

STRIDE:
  S=1: move filter 1 pixel at a time (default)
  S=2: move 2 pixels → output half the size (downsamples)
```

[↑ Back to Top](#-deep-learning-foundations-dnn--cnn--autoencoders)

---

## 4. Pooling

```
POOLING = downsample feature maps (reduce spatial size)

MAX POOLING (most common):
  Take the MAX value in each window

  Input (4×4):        MaxPool 2×2, stride 2:
  [1 3 | 2 1]         [3  3]
  [2 1 | 3 2]   →     [4  5]
  [4 2 | 1 0]
  [0 1 | 5 3]

  Window [1,3,2,1] → max=3
  Window [2,1,3,2] → max=3
  etc.

AVERAGE POOLING:
  Take the AVERAGE in each window (less common)

GLOBAL AVERAGE POOLING:
  Average the ENTIRE feature map to 1 number
  → Used before final FC layer in modern architectures

WHY POOL?
  1. Reduces parameters → less overfitting
  2. Makes features invariant to small translations
  3. Increases receptive field (each later neuron "sees" more of input)
```

[↑ Back to Top](#-deep-learning-foundations-dnn--cnn--autoencoders)

---

## 5. Famous CNN Architectures

```
┌──────────────┬───────┬──────────────────────────────────────────┐
│ Architecture │ Year  │ Key Idea                                 │
├──────────────┼───────┼──────────────────────────────────────────┤
│ LeNet-5      │ 1998  │ First successful CNN (handwritten digits)│
│ AlexNet      │ 2012  │ Deep CNN + ReLU + dropout + GPU          │
│ VGGNet       │ 2014  │ Very deep (16-19 layers), small 3×3      │
│ GoogLeNet    │ 2014  │ Inception modules (parallel filters)     │
│ ResNet       │ 2015  │ Skip connections (solve vanishing grad)  │
│ DenseNet     │ 2017  │ Connect every layer to every other       │
│ EfficientNet │ 2019  │ Compound scaling (width+depth+resolution)│
└──────────────┴───────┴──────────────────────────────────────────┘

RESNET SKIP CONNECTION:
  Input x → [Conv → BN → ReLU → Conv → BN] → output + x → ReLU
                                                     ↑
                                              skip connection!
  F(x) + x  instead of just F(x)
  → Gradient flows directly through the skip → no vanishing gradient!
```

[↑ Back to Top](#-deep-learning-foundations-dnn--cnn--autoencoders)

---

## 6. Autoencoders

### 👶 Easy Story
Imagine summarizing a 100-page book into 5 sentences (encoder), then trying to rewrite the entire book from just those 5 sentences (decoder). If the rewrite is close to the original, those 5 sentences captured the ESSENCE of the book. An autoencoder compresses data into a small "bottleneck" and then reconstructs it!

```
AUTOENCODER ARCHITECTURE:
━━━━━━━━━━━━━━━━━━━━━━━━
  x ─→ [Encoder] ─→ z (latent/code) ─→ [Decoder] ─→ x̂ ≈ x
  
  d dims        k dims (k << d)           d dims
  (input)       (compressed!)              (reconstruction)

  LOSS: L = ||x - x̂||²  (reconstruction error)
  GOAL: minimize L → learn z that captures the MOST important info

  Input (784) → [256] → [64] → [32] → [64] → [256] → Output (784)
                 encoder         ↑       decoder
                           bottleneck (latent space)

TYPES:
  Undercomplete:  k < d (bottleneck smaller than input → compression)
  Overcomplete:   k > d (need regularization: sparse/denoising)
  Sparse:         add L1 penalty on z → most latent dims = 0
  Denoising:      add noise to input, train to reconstruct clean version
  Variational:    z is a DISTRIBUTION, not a point → generative model

APPLICATIONS:
  1. Dimensionality reduction (like non-linear PCA!)
  2. Anomaly detection (high reconstruction error = anomaly)
  3. Denoising (remove noise from images)
  4. Generative models (VAE can generate new data)
  5. Pre-training (encoder features → fine-tune for classification)

AUTOENCODER vs PCA:
  PCA: linear compression, closed-form solution
  AE:  non-linear compression (deep nets), gradient-based
  If AE has linear activations + MSE loss + 1 hidden layer → identical to PCA!
```

[↑ Back to Top](#-deep-learning-foundations-dnn--cnn--autoencoders)

---

## 7. Training Deep Networks

```
OPTIMIZERS:
  SGD:         W ← W - α∇L           (vanilla, can be slow)
  Momentum:    v ← βv + α∇L; W ← W - v  (accelerates in consistent direction)
  Adam:        adaptive learning rate per parameter (default choice!)
    m ← β₁m + (1-β₁)∇L       (1st moment)
    v ← β₂v + (1-β₂)(∇L)²    (2nd moment)
    W ← W - α × m̂/(√v̂ + ε)   (adaptive step)

REGULARIZATION:
  L2 (weight decay): add λ||W||² to loss
  Dropout: randomly zero-out p% of neurons per batch
  Batch Norm: normalize activations → faster, more stable
  Data augmentation: flip/rotate/crop images → more effective data
  Early stopping: stop when validation loss starts increasing
```

[↑ Back to Top](#-deep-learning-foundations-dnn--cnn--autoencoders)

---

## 8. Numericals

### N1: Conv Output Size

```
Input: 28×28, Kernel: 5×5, Padding: 2, Stride: 1
  O = (28 - 5 + 2×2)/1 + 1 = (28-5+4)/1 + 1 = 27+1 = 28
  (same size because padding=2 compensates for kernel=5!)

After MaxPool 2×2, stride 2:
  O = 28/2 = 14×14

Parameters:
  Conv: 5×5×1 filters × 16 + 16 bias = 416
  (if input has 3 channels: 5×5×3×16 + 16 = 1216)
```

### N2: Total Parameters in CNN

```
Architecture:
  Input: 32×32×3
  Conv1: 16 filters of 3×3, stride 1, padding 1 → 32×32×16
  Pool1: 2×2 → 16×16×16
  Conv2: 32 filters of 3×3 → 14×14×32
  Pool2: 2×2 → 7×7×32
  FC: 7×7×32 = 1568 → 128 → 10

Parameters:
  Conv1: 3×3×3×16 + 16 = 448
  Conv2: 3×3×16×32 + 32 = 4,640
  FC1: 1568×128 + 128 = 200,832
  FC2: 128×10 + 10 = 1,290
  TOTAL: 207,210

  NOTE: Most params are in FC layers! Conv layers are efficient.
```

### N3: Autoencoder Reconstruction

```
Encoder: x=[1,2,3,4] → z=Wx+b with W=[0.5,0.5,0,0; 0,0,0.5,0.5], b=[0,0]
  z = [0.5×1+0.5×2, 0.5×3+0.5×4] = [1.5, 3.5]  (compressed 4D → 2D)

Decoder: z=[1.5, 3.5] → x̂=W'd+b' with W'=[0.5,0; 0.5,0; 0,0.5; 0,0.5]
  x̂ = [0.5×1.5, 0.5×1.5, 0.5×3.5, 0.5×3.5] = [0.75, 0.75, 1.75, 1.75]

  Loss = ||x - x̂||² = (1-0.75)² + (2-0.75)² + (3-1.75)² + (4-1.75)²
       = 0.0625 + 1.5625 + 1.5625 + 5.0625 = 8.25
  
  (High loss → this autoencoder needs more training!)
```

[↑ Back to Top](#-deep-learning-foundations-dnn--cnn--autoencoders)

---

## 9. Cheat Sheet & Exam Hacks

```
┌────────────────────────────────────────────────────────────────┐
│           DEEP LEARNING CHEAT SHEET                            │
├──────────────────┬─────────────────────────────────────────────┤
│ Conv output size │ O = (I - K + 2P)/S + 1                      │
│ Conv parameters  │ K × K × C_in × C_out + C_out (bias)         │
│ MaxPool          │ Take max in each window, no parameters      │
│ Receptive field  │ Grows with depth (deeper = sees more)       │
│ ResNet           │ F(x) + x skip connection → no vanishing grad│
│ Autoencoder      │ Encoder → bottleneck → Decoder, min ||x-x̂||²│
│ VAE              │ Autoencoder + latent = distribution         │
│ Sparse AE        │ L1 on bottleneck → most dims inactive       │
│ Denoising AE     │ Input=noisy, Target=clean                   │
│ Dropout          │ Zero p% of neurons per batch (regularize)   │
│ Batch Norm       │ Normalize per mini-batch (faster training)  │
│ Adam optimizer   │ Adaptive lr per param (default choice)      │
│ Xavier/He init   │ Proper init prevents vanishing/exploding    │
│ CNN vs MLP       │ CNN: param sharing, spatial structure       │
│ AE vs PCA        │ AE non-linear, PCA linear; same if linear AE│
└──────────────────┴─────────────────────────────────────────────┘

🧪 EXAM HACKS:
💡 Conv output size: O = (I-K+2P)/S + 1 — memorize this!
💡 Conv params: K²×C_in×C_out + C_out — way fewer than FC
💡 ResNet: residual = F(x) + x. Gradient flows through + directly.
💡 Autoencoder loss = reconstruction error = ||x - x̂||²
💡 If AE is linear + MSE → same as PCA (this is an exam favourite!)
💡 Dropout at test time: NO dropout, but scale weights by (1-p)
💡 In exam: draw architecture diagram, show output sizes per layer
💡 CNN for images, RNN for sequences, Transformer for everything modern
```

---

> **Nav:** [← Neural Networks](../Neural-Networks/ml_nn_mlp_bp_theory.md) | **Deep Learning** | [← ML Master Index](../ml_master_gap_index.md)

[↑ Back to Top](#-deep-learning-foundations-dnn--cnn--autoencoders)

---

*AI · ML · github.com/rpaut03l/TS-01*
