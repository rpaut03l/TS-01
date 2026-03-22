# 📖 Neural Networks: MLP · Backpropagation · RBF-Net

### *Perceptron · MLP · Forward/Backward Pass · Activations · RBF Networks*

> **Nav:** [← SVM](../SVM-Kernels/ml_svm_kernels_theory.md) | **Neural Networks** | [Deep Learning →](../Deep-Learning/ml_dl_cnn_ae_theory.md)

---

## 🧠 MNEMONIC: **"FLAME-BR"**

> **F**orward pass · **L**ayers · **A**ctivation functions · **M**LP · **E**rror backprop · **B**ias · **R**BF networks

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Perceptron | [§1](#1-perceptron) |
| 2 | MLP Architecture | [§2](#2-multi-layer-perceptron-mlp) |
| 3 | Activation Functions | [§3](#3-activation-functions) |
| 4 | Forward Propagation | [§4](#4-forward-propagation) |
| 5 | Backpropagation | [§5](#5-backpropagation) |
| 6 | RBF Networks | [§6](#6-rbf-networks) |
| 7 | Numericals | [§7](#7-numericals) |
| 8 | Cheat Sheet | [§8](#8-cheat-sheet--exam-hacks) |

---

## 1. Perceptron

### 👶 Easy Story
A perceptron is like a simple voting machine. Each input casts a WEIGHTED vote. If the total votes exceed a threshold, the answer is YES (+1), otherwise NO (-1). It's the simplest "neuron"!

```
PERCEPTRON:
━━━━━━━━━━
  x₁ ──(w₁)──┐
  x₂ ──(w₂)──┼──→ Σ(wᵢxᵢ + b) ──→ step(z) ──→ ŷ ∈ {-1, +1}
  x₃ ──(w₃)──┘

  Output: ŷ = sign(wᵀx + b) = sign(Σ wᵢxᵢ + b)
  
  If wᵀx + b > 0 → predict +1
  If wᵀx + b ≤ 0 → predict -1

LEARNING RULE:
  If misclassified: w_new = w_old + η × yᵢ × xᵢ
                    b_new = b_old + η × yᵢ
  If correct: do nothing

LIMITATION: Can ONLY learn linearly separable patterns
  ✅ AND, OR   ✗ XOR (this killed perceptrons in 1969!)
  → Solution: Multi-Layer Perceptron (MLP) with hidden layers!
```

[↑ Back to Top](#-neural-networks-mlp--backpropagation--rbf-net)

---

## 2. Multi-Layer Perceptron (MLP)

```
ARCHITECTURE:
━━━━━━━━━━━━
  INPUT          HIDDEN LAYER(s)          OUTPUT
  LAYER          (the "brain")            LAYER

  x₁ ○───────○ h₁                    ○ ŷ₁
               ╲  ╱ ╲
  x₂ ○─────── ○ h₂  ○──────────────○ ŷ₂
               ╱  ╲ ╱
  x₃ ○───────○ h₃
  
  d inputs     L hidden neurons        C outputs
              (can have multiple        (1 for regression,
               hidden layers)           C for classification)

EACH NEURON COMPUTES:
  z = wᵀx + b           ← linear combination (pre-activation)
  a = f(z)               ← activation function (non-linearity)

NOTATION:
  W⁽ˡ⁾ = weight matrix for layer l    (size: nˡ × nˡ⁻¹)
  b⁽ˡ⁾ = bias vector for layer l      (size: nˡ × 1)
  z⁽ˡ⁾ = W⁽ˡ⁾a⁽ˡ⁻¹⁾ + b⁽ˡ⁾           (pre-activation)
  a⁽ˡ⁾ = f(z⁽ˡ⁾)                      (activation)
  a⁽⁰⁾ = x                            (input layer)

UNIVERSAL APPROXIMATION THEOREM:
  An MLP with 1 hidden layer + enough neurons + non-linear activation
  can approximate ANY continuous function to arbitrary accuracy!
  → Neural nets are universal function approximators!
```

[↑ Back to Top](#-neural-networks-mlp--backpropagation--rbf-net)

---

## 3. Activation Functions

```
┌────────────────┬──────────────────────┬──────────────────────┬─────────────────┐
│ Function       │ Formula              │ Derivative           │ Range           │
├────────────────┼──────────────────────┼──────────────────────┼─────────────────┤
│ Sigmoid (σ)    │ 1/(1+e⁻ᶻ)            │ σ(z)(1-σ(z))         │ (0, 1)          │
│ Tanh           │ (eᶻ-e⁻ᶻ)/(eᶻ+e⁻ᶻ)    │ 1 - tanh²(z)         │ (-1, 1)         │
│ ReLU           │ max(0, z)            │ 1 if z>0, 0 if z≤0   │ [0, ∞)          │
│ Leaky ReLU     │ max(αz, z), α=0.01   │ 1 if z>0, α if z≤0   │ (-∞, ∞)         │
│ Softmax        │ eᶻⁱ / Σⱼeᶻʲ          │ (complex)            │ (0,1), sum=1    │
└────────────────┴──────────────────────┴──────────────────────┴─────────────────┘

SIGMOID:                TANH:                ReLU:
  1 │    ────           1│    ────           │      ╱
    │  ╱                 │  ╱                │    ╱
 .5 │╱                 0 │╱                  │  ╱
    │                  -1│                   │╱_________
  0 │                    │                   0

WHEN TO USE:
  Hidden layers:  ReLU (default) or Leaky ReLU
  Output (binary): Sigmoid
  Output (multi-class): Softmax
  Output (regression): Linear (no activation)
  AVOID: Sigmoid/Tanh in hidden layers (vanishing gradient!)
```

[↑ Back to Top](#-neural-networks-mlp--backpropagation--rbf-net)

---

## 4. Forward Propagation

```
LAYER-BY-LAYER COMPUTATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━
  Input:   a⁽⁰⁾ = x
  
  For each layer l = 1, 2, ..., L:
    z⁽ˡ⁾ = W⁽ˡ⁾ a⁽ˡ⁻¹⁾ + b⁽ˡ⁾      ← matrix multiply + bias
    a⁽ˡ⁾ = f(z⁽ˡ⁾)                   ← apply activation
  
  Output:  ŷ = a⁽ᴸ⁾

LOSS FUNCTIONS:
  Regression:       L = ½ Σ(yᵢ - ŷᵢ)²           (MSE)
  Binary clf:       L = -[y log(ŷ) + (1-y)log(1-ŷ)]  (Binary CE)
  Multi-class clf:  L = -Σₖ yₖ log(ŷₖ)           (Categorical CE)
```

[↑ Back to Top](#-neural-networks-mlp--backpropagation--rbf-net)

---

## 5. Backpropagation

### 👶 Easy Story
You take a test. You get 60%. The teacher says "you lost 10% on question 3 and 30% on question 5." That feedback flows BACKWARDS — from the final score, to each question, to each concept you got wrong. Backprop does the same: compute the error at the output, then flow it backwards through each layer to figure out how much each weight contributed to the error.

```
BACKPROPAGATION ALGORITHM:
━━━━━━━━━━━━━━━━━━━━━━━━━
  1. FORWARD PASS: compute all z⁽ˡ⁾, a⁽ˡ⁾, and Loss L
  2. BACKWARD PASS: compute gradients layer by layer

  OUTPUT LAYER error:
    δ⁽ᴸ⁾ = ∂L/∂z⁽ᴸ⁾ = (a⁽ᴸ⁾ - y) ⊙ f'(z⁽ᴸ⁾)
    (for MSE + sigmoid: δ⁽ᴸ⁾ = (ŷ - y) × σ'(z))
  
  HIDDEN LAYER error (propagate backward):
    δ⁽ˡ⁾ = (W⁽ˡ⁺¹⁾ᵀ δ⁽ˡ⁺¹⁾) ⊙ f'(z⁽ˡ⁾)
    
    ⊙ = element-wise multiplication

  GRADIENTS:
    ∂L/∂W⁽ˡ⁾ = δ⁽ˡ⁾ (a⁽ˡ⁻¹⁾)ᵀ     ← gradient for weights
    ∂L/∂b⁽ˡ⁾ = δ⁽ˡ⁾                 ← gradient for biases

  WEIGHT UPDATE (gradient descent):
    W⁽ˡ⁾ ← W⁽ˡ⁾ - α × ∂L/∂W⁽ˡ⁾
    b⁽ˡ⁾ ← b⁽ˡ⁾ - α × ∂L/∂b⁽ˡ⁾

  α = learning rate (small step size, typically 0.001-0.01)

CHAIN RULE IS THE KEY:
  ∂L/∂w = ∂L/∂a × ∂a/∂z × ∂z/∂w
  Each layer just passes its error to the previous layer!
```

[↑ Back to Top](#-neural-networks-mlp--backpropagation--rbf-net)

---

## 6. RBF Networks

### 👶 Easy Story
An RBF network puts "bell curves" (Gaussians) on top of key locations in data space. Each bell curve measures "how close is the input to this center?" The output layer then combines these closeness scores with weights to make a prediction. Unlike MLP which uses hyperplanes, RBF uses proximity!

```
RBF NETWORK ARCHITECTURE:
━━━━━━━━━━━━━━━━━━━━━━━━
  Input → RBF Layer (K neurons) → Linear Output
  
  x ──→ φ₁(x) = exp(-||x-c₁||²/2σ₁²) ──┐
  x ──→ φ₂(x) = exp(-||x-c₂||²/2σ₂²) ──┼──→ Σ wₖφₖ(x) + b = ŷ
  x ──→ φₖ(x) = exp(-||x-cₖ||²/2σₖ²) ───┘

  cₖ = centers (found by K-Means or random selection)
  σₖ = widths (determines how far each bell curve reaches)
  wₖ = output weights (learned by linear regression)

TRAINING:
  1. Fix centers cₖ (e.g., use K-Means on training data)
  2. Fix widths σₖ (e.g., average distance to nearest centers)
  3. Compute φ matrix: Φᵢₖ = φₖ(xᵢ)
  4. Solve for weights: w = (ΦᵀΦ)⁻¹Φᵀy  (linear regression!)

RBF vs MLP:
┌──────────────┬──────────────────────┬──────────────────────┐
│              │ MLP                  │ RBF Network          │
├──────────────┼──────────────────────┼──────────────────────┤
│ Hidden units │ Hyperplane-based     │ Gaussian-based       │
│ Activation   │ Sigmoid/ReLU         │ Gaussian exp(-r²)    │
│ Response     │ Global (whole space) │ Local (near center)  │
│ Training     │ Full backprop        │ Two-stage (fast!)    │
│ Good for     │ Complex patterns     │ Interpolation        │
└──────────────┴──────────────────────┴──────────────────────┘
```

[↑ Back to Top](#-neural-networks-mlp--backpropagation--rbf-net)

---

## 7. Numericals

### N1: Forward Pass (2-1-1 MLP)

```
Network: 2 inputs, 1 hidden neuron (sigmoid), 1 output (sigmoid)
  W⁽¹⁾ = [0.5, -0.3], b⁽¹⁾ = 0.1
  W⁽²⁾ = [0.8],        b⁽²⁾ = -0.2
  Input: x = [1, 2]

FORWARD:
  z⁽¹⁾ = 0.5×1 + (-0.3)×2 + 0.1 = 0.5 - 0.6 + 0.1 = 0.0
  a⁽¹⁾ = σ(0.0) = 1/(1+e⁰) = 1/2 = 0.500

  z⁽²⁾ = 0.8×0.500 + (-0.2) = 0.4 - 0.2 = 0.2
  a⁽²⁾ = σ(0.2) = 1/(1+e⁻⁰·²) = 1/1.819 = 0.550

  ŷ = 0.550 ✅
```

### N2: Backprop (one step)

```
Continuing N1: true y = 1, ŷ = 0.550, using MSE loss

  L = ½(1 - 0.550)² = ½(0.450)² = 0.101

OUTPUT LAYER:
  δ⁽²⁾ = (ŷ - y) × σ'(z⁽²⁾) = (0.550-1) × 0.550×(1-0.550)
       = -0.450 × 0.2475 = -0.111
  ∂L/∂W⁽²⁾ = δ⁽²⁾ × a⁽¹⁾ = -0.111 × 0.500 = -0.056
  ∂L/∂b⁽²⁾ = δ⁽²⁾ = -0.111

HIDDEN LAYER:
  δ⁽¹⁾ = (W⁽²⁾ᵀ × δ⁽²⁾) × σ'(z⁽¹⁾)
       = (0.8 × -0.111) × 0.500×(1-0.500)
       = -0.089 × 0.250 = -0.022
  ∂L/∂W⁽¹⁾ = δ⁽¹⁾ × xᵀ = -0.022 × [1, 2] = [-0.022, -0.044]
  ∂L/∂b⁽¹⁾ = δ⁽¹⁾ = -0.022

UPDATE (α = 0.1):
  W⁽²⁾ = 0.8 - 0.1×(-0.056) = 0.806
  b⁽²⁾ = -0.2 - 0.1×(-0.111) = -0.189
  W⁽¹⁾ = [0.5-0.1×(-0.022), -0.3-0.1×(-0.044)] = [0.502, -0.296]
  b⁽¹⁾ = 0.1 - 0.1×(-0.022) = 0.102
```

[↑ Back to Top](#-neural-networks-mlp--backpropagation--rbf-net)

---

## 8. Cheat Sheet & Exam Hacks

```
┌────────────────────────────────────────────────────────────────┐
│            NEURAL NETWORKS CHEAT SHEET                         │
├──────────────────┬─────────────────────────────────────────────┤
│ Forward pass     │ z=Wa+b, a=f(z), layer by layer              │
│ Output δ         │ δ⁽ᴸ⁾ = (ŷ-y) ⊙ f'(z⁽ᴸ⁾)                     │
│ Hidden δ         │ δ⁽ˡ⁾ = (Wˡ⁺¹ᵀ δˡ⁺¹) ⊙ f'(zˡ)                │
│ Weight gradient  │ ∂L/∂W = δ × aᵀ (previous layer activations) │
│ Update rule      │ W ← W - α × ∂L/∂W                           │
│ σ(z) derivative  │ σ(z)(1-σ(z))                                │
│ ReLU derivative  │ 1 if z>0, 0 if z≤0                          │
│ tanh derivative  │ 1 - tanh²(z)                                │
│ RBF activation   │ exp(-||x-c||²/2σ²)                          │
│ RBF training     │ Centers (K-Means) + Weights (linear reg)    │
│ Universal approx │ 1 hidden layer + enough neurons = any fn    │
│ Vanishing grad   │ Sigmoid/Tanh in deep nets → use ReLU        │
└──────────────────┴─────────────────────────────────────────────┘

🧪 EXAM HACKS:
💡 Forward: input→hidden→output (multiply, add bias, activate)
💡 Backward: output→hidden→input (chain rule, δ propagation)
💡 ∂L/∂W⁽ˡ⁾ = δ⁽ˡ⁾ × (a⁽ˡ⁻¹⁾)ᵀ — MOST IMPORTANT BACKPROP FORMULA
💡 σ'(z) = σ(z)(1-σ(z)) — memorize for sigmoid derivative
💡 ReLU default for hidden layers. Sigmoid only for output (binary).
💡 RBF = local (close to center matters). MLP = global.
💡 In exam: show FULL forward pass numbers, THEN backward pass numbers
```

---

> **Nav:** [← SVM](../SVM-Kernels/ml_svm_kernels_theory.md) | **Neural Networks** | [Deep Learning →](../Deep-Learning/ml_dl_cnn_ae_theory.md)

[↑ Back to Top](#-neural-networks-mlp--backpropagation--rbf-net)

---

*AI · ML · github.com/rpaut03l/TS-01*
