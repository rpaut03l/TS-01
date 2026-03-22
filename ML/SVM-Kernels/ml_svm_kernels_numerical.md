# 🔢 SVM & Kernels: NUMERICAL

### *Margin calc, kernel math, SVM classify. Every step shown.*

> **Nav:** [📖 THEORY](ml_svm_kernels_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_svm_kernels_practice.md)

---

## 📦 KEY FORMULAS

```
┌─────────────────────────────────────────────────────────────┐
│ MARGIN = 2/||w||                                            │
│ ||w|| = √(Σwᵢ²)                                             │
│ Decision: f(x) = sign(wᵀx + b)                              │
│ Dual decision: f(x) = sign(Σαᵢyᵢ K(xᵢ,x) + b)               │
│ Linear kernel:  K(x,z) = xᵀz                                │
│ Poly kernel:    K(x,z) = (xᵀz + c)ᵈ                         │
│ RBF kernel:     K(x,z) = exp(-γ||x-z||²)                    │
│ Dist to hyperplane: |wᵀx + b| / ||w||                       │
└─────────────────────────────────────────────────────────────┘
```

---

## P1: Compute Margin

```
Given: w = [2, -1], b = 3
  ||w|| = √(4+1) = √5 = 2.236
  Margin = 2/||w|| = 2/2.236 = 0.894

  Hyperplane: 2x₁ - x₂ + 3 = 0
  Positive margin: 2x₁ - x₂ + 3 = +1
  Negative margin: 2x₁ - x₂ + 3 = -1

  Point [0, 0]: distance = |2×0-1×0+3|/2.236 = 3/2.236 = 1.342
  Since distance(1.342) > margin/2(0.447) → outside margin ✅
```

[↑ Back to Top](#-svm--kernels-numerical)

---

## P2: Kernel Computations

```
x = [2, 3], z = [1, 4]

LINEAR:  K = xᵀz = 2×1 + 3×4 = 14
POLY(d=2,c=1): K = (xᵀz + 1)² = (14+1)² = 225
RBF(γ=0.1):    ||x-z||² = (2-1)² + (3-4)² = 1+1 = 2
                K = exp(-0.1×2) = exp(-0.2) = 0.819
RBF(γ=1.0):    K = exp(-1.0×2) = exp(-2) = 0.135
RBF(γ=10):     K = exp(-10×2) = exp(-20) ≈ 0 (very dissimilar)

INSIGHT: Larger γ → K drops faster → only VERY close points matter
```

[↑ Back to Top](#-svm--kernels-numerical)

---

## P3: SVM Dual Classification

```
Trained SVM (linear kernel):
  Support vectors: sv₁=[1,1](y=+1, α=0.4), sv₂=[3,2](y=-1, α=0.4)
  b = 0.3

Classify x_new = [2, 2]:
  f(x) = Σ αᵢyᵢ K(svᵢ, x) + b
       = 0.4×(+1)×(1×2+1×2) + 0.4×(-1)×(3×2+2×2) + 0.3
       = 0.4×4 + 0.4×(-10) + 0.3
       = 1.6 - 4.0 + 0.3 = -2.1
  sign(-2.1) = -1 → CLASS -1 ✅
```

[↑ Back to Top](#-svm--kernels-numerical)

---

## P4: SVR ε-tube

```
ε = 0.5, C = 10
Predictions: [2.1, 3.5, 4.8]
Actuals:     [2.0, 4.2, 5.0]
Errors:      [0.1, 0.7, 0.2]

  Point 1: |error|=0.1 < ε=0.5 → NO penalty (inside tube) ✅
  Point 2: |error|=0.7 > ε=0.5 → ξ=0.7-0.5=0.2 penalty
  Point 3: |error|=0.2 < ε=0.5 → NO penalty (inside tube) ✅

  Total slack = 0 + 0.2 + 0 = 0.2
  Only point 2 is a support vector (outside ε-tube)
```

---

> **Nav:** [📖 THEORY](ml_svm_kernels_theory.md) | 🔢 NUMERICAL | [💻 PRACTICE →](ml_svm_kernels_practice.md)

[↑ Back to Top](#-svm--kernels-numerical)

*AI · ML · github.com/rpaut03l/TS-01*
