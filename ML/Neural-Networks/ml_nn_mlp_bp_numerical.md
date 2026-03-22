# 🔢 Neural Networks: NUMERICAL

### *Forward pass numbers, backprop gradients, RBF computation.*

> **Nav:** [📖 THEORY](ml_nn_mlp_bp_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_nn_mlp_bp_practice.md)

---

## 📦 KEY FORMULAS

```
┌──────────────────────────────────────────────────────────────┐
│ FORWARD:   z = Wa + b,  a = f(z)                             │
│ σ(z):      1/(1+e⁻ᶻ)                                         │
│ σ'(z):     σ(z)(1-σ(z))                                      │
│ tanh'(z):  1 - tanh²(z)                                      │
│ ReLU'(z):  1 if z>0, else 0                                  │
│ δ_output:  (ŷ-y) × f'(z)                                     │
│ δ_hidden:  (Wᵀδ_next) ⊙ f'(z)                                │
│ ∂L/∂W:     δ × aᵀ_prev                                       │
│ UPDATE:    W ← W - α × ∂L/∂W                                 │
│ RBF:       φₖ(x) = exp(-||x-cₖ||²/(2σₖ²))                     │
└──────────────────────────────────────────────────────────────┘
```

---

## P1: Forward Pass (2-2-1 Network)

```
Architecture: 2 inputs → 2 hidden (sigmoid) → 1 output (sigmoid)
  W⁽¹⁾ = [[0.3, 0.5],    b⁽¹⁾ = [0.1, -0.1]
           [0.4, -0.2]]
  W⁽²⁾ = [[0.6, 0.7]]    b⁽²⁾ = [0.2]
  Input: x = [1, 0.5]

HIDDEN LAYER:
  z₁⁽¹⁾ = 0.3×1 + 0.5×0.5 + 0.1 = 0.65
  z₂⁽¹⁾ = 0.4×1 + (-0.2)×0.5 + (-0.1) = 0.20
  a₁⁽¹⁾ = σ(0.65) = 1/(1+e⁻⁰·⁶⁵) = 1/1.522 = 0.657
  a₂⁽¹⁾ = σ(0.20) = 1/(1+e⁻⁰·²⁰) = 1/1.819 = 0.550

OUTPUT LAYER:
  z⁽²⁾ = 0.6×0.657 + 0.7×0.550 + 0.2 = 0.394+0.385+0.2 = 0.979
  ŷ = σ(0.979) = 1/(1+e⁻⁰·⁹⁷⁹) = 1/1.376 = 0.727

  ŷ = 0.727 ✅
```

[↑ Back to Top](#-neural-networks-numerical)

---

## P2: Backprop (Continuation of P1)

```
True y = 1, ŷ = 0.727, Loss = ½(1-0.727)² = ½(0.273)² = 0.037

OUTPUT LAYER δ:
  σ'(z⁽²⁾) = ŷ(1-ŷ) = 0.727×0.273 = 0.198
  δ⁽²⁾ = (ŷ-y) × σ'(z⁽²⁾) = (0.727-1) × 0.198 = -0.273 × 0.198 = -0.054

  ∂L/∂W⁽²⁾ = δ⁽²⁾ × [a₁⁽¹⁾, a₂⁽¹⁾]
           = -0.054 × [0.657, 0.550] = [-0.036, -0.030]
  ∂L/∂b⁽²⁾ = -0.054

HIDDEN LAYER δ:
  (W⁽²⁾)ᵀ × δ⁽²⁾ = [[0.6], [0.7]] × (-0.054) = [-0.032, -0.038]
  
  σ'(z₁⁽¹⁾) = 0.657×(1-0.657) = 0.225
  σ'(z₂⁽¹⁾) = 0.550×(1-0.550) = 0.248
  
  δ₁⁽¹⁾ = -0.032 × 0.225 = -0.007
  δ₂⁽¹⁾ = -0.038 × 0.248 = -0.009

  ∂L/∂W⁽¹⁾ = [δ₁⁽¹⁾, δ₂⁽¹⁾]ᵀ × [x₁, x₂]
           = [[-0.007×1, -0.007×0.5],  = [[-0.007, -0.004],
              [-0.009×1, -0.009×0.5]]     [-0.009, -0.005]]

UPDATE (α=0.5):
  W⁽²⁾_new = [0.6-0.5×(-0.036), 0.7-0.5×(-0.030)] = [0.618, 0.715]
  W⁽¹⁾_new = [[0.3+0.004, 0.5+0.002], [0.4+0.005, -0.2+0.003]]
           = [[0.304, 0.502], [0.405, -0.197]]
  (All weights moved in direction that reduces loss) ✅
```

[↑ Back to Top](#-neural-networks-numerical)

---

## P3: RBF Network Output

```
Centers: c₁=[0,0], c₂=[3,3], σ=1.5 for both
Weights: w₁=2.0, w₂=-1.0, bias=0.5
Input: x=[1,1]

  φ₁ = exp(-||[1,1]-[0,0]||²/(2×1.5²)) = exp(-2/4.5) = exp(-0.444) = 0.641
  φ₂ = exp(-||[1,1]-[3,3]||²/(2×1.5²)) = exp(-8/4.5) = exp(-1.778) = 0.169

  ŷ = w₁φ₁ + w₂φ₂ + b = 2.0×0.641 + (-1.0)×0.169 + 0.5
    = 1.282 - 0.169 + 0.5 = 1.613 ✅
```

---

> **Nav:** [📖 THEORY](ml_nn_mlp_bp_theory.md) | 🔢 NUMERICAL | [💻 PRACTICE →](ml_nn_mlp_bp_practice.md)

[↑ Back to Top](#-neural-networks-numerical)

*AI · ML · github.com/rpaut03l/TS-01*
