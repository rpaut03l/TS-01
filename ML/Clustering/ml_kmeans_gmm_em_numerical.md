# 🔢 Clustering: NUMERICAL

### *K-Means iterations, GMM E-step, EM M-step. Every step shown.*

> **Nav:** [📖 THEORY](ml_kmeans_gmm_em_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_kmeans_gmm_em_practice.md)

---

## 📦 KEY FORMULAS

```
┌─────────────────────────────────────────────────────────────┐
│ K-MEANS OBJECTIVE: J = Σₖ Σᵢ∈Cₖ ||xᵢ - μₖ||²                 │
│ CENTROID UPDATE:   μₖ = (1/|Cₖ|) Σᵢ∈Cₖ xᵢ                    │
│ GMM MODEL:         P(x) = Σₖ πₖ N(x|μₖ,Σₖ)                   │
│ E-STEP:            γᵢₖ = πₖN(xᵢ|μₖ,Σₖ) / Σⱼ πⱼN(xᵢ|μⱼ,Σⱼ)    │
│ M-STEP:  Nₖ=Σᵢγᵢₖ, μₖ=Σᵢγᵢₖxᵢ/Nₖ, πₖ=Nₖ/n                     │
│ GAUSSIAN 1D: N(x|μ,σ) = (1/√(2πσ²))exp(-(x-μ)²/(2σ²))      │
└────────────────────────────────────────────────────────────┘
```

---

## P1: K-Means (3 points, K=2, 2 iterations)

```
DATA: x₁=[0,0], x₂=[1,0], x₃=[5,5]   K=2
INIT: μ₁=[0,0] (=x₁), μ₂=[1,0] (=x₂)

ITERATION 1 — ASSIGN:
  d(x₁,μ₁)=0    d(x₁,μ₂)=1      → x₁→C1
  d(x₂,μ₁)=1    d(x₂,μ₂)=0      → x₂→C2
  d(x₃,μ₁)=√50=7.07  d(x₃,μ₂)=√41=6.40  → x₃→C2

  C1={x₁}, C2={x₂,x₃}

ITERATION 1 — UPDATE:
  μ₁ = [0,0]
  μ₂ = [(1+5)/2, (0+5)/2] = [3.0, 2.5]

ITERATION 2 — ASSIGN:
  d(x₁,μ₁)=0         d(x₁,μ₂)=√(9+6.25)=3.91  → x₁→C1
  d(x₂,μ₁)=1         d(x₂,μ₂)=√(4+6.25)=3.20  → x₂→C1 ← CHANGED!
  d(x₃,μ₁)=7.07      d(x₃,μ₂)=√(4+6.25)=3.20  → x₃→C2

  C1={x₁,x₂}, C2={x₃}

ITERATION 2 — UPDATE:
  μ₁ = [(0+1)/2, 0] = [0.5, 0]
  μ₂ = [5, 5]

ITERATION 3 — ASSIGN:
  d(x₁,μ₁)=0.5    d(x₁,μ₂)=7.07   → C1
  d(x₂,μ₁)=0.5    d(x₂,μ₂)=6.40   → C1
  d(x₃,μ₁)=6.73   d(x₃,μ₂)=0      → C2
  Same as iteration 2 → CONVERGED! ✅

FINAL: C1={x₁,x₂} at [0.5,0], C2={x₃} at [5,5]
J = (0.5²+0+0.5²+0+0+0) = 0.50
```

[↑ Back to Top](#-clustering-numerical)

---

## P2: GMM E-step (1D, K=2)

```
Components: π₁=0.7, μ₁=0, σ₁=1  |  π₂=0.3, μ₂=4, σ₂=1
Point: x = 2

N(2|0,1) = (1/√(2π)) × exp(-4/2) = 0.3989 × 0.1353 = 0.0540
N(2|4,1) = (1/√(2π)) × exp(-4/2) = 0.3989 × 0.1353 = 0.0540

γ₁ = (0.7×0.0540) / (0.7×0.0540 + 0.3×0.0540)
   = 0.0378 / (0.0378 + 0.0162) = 0.0378/0.0540 = 0.700

γ₂ = 0.0162 / 0.0540 = 0.300

NOTE: Both N values are equal (x=2 is equidistant from both means)
so γ's just follow the mixing weights π! Makes sense.
```

[↑ Back to Top](#-clustering-numerical)

---

## P3: Full EM Round (M-step)

```
4 points: x=[0, 1, 4, 5], K=2
After E-step: γ₁=[0.95, 0.85, 0.10, 0.05]
              γ₂=[0.05, 0.15, 0.90, 0.95]

M-STEP:
  N₁ = 0.95+0.85+0.10+0.05 = 1.95
  N₂ = 0.05+0.15+0.90+0.95 = 2.05

  μ₁ = (0.95×0+0.85×1+0.10×4+0.05×5)/1.95
     = (0+0.85+0.40+0.25)/1.95 = 1.50/1.95 = 0.769

  μ₂ = (0.05×0+0.15×1+0.90×4+0.95×5)/2.05
     = (0+0.15+3.60+4.75)/2.05 = 8.50/2.05 = 4.146

  π₁ = 1.95/4 = 0.4875
  π₂ = 2.05/4 = 0.5125

  σ₁² = Σγᵢ₁(xᵢ-μ₁)²/N₁
     = [0.95×(0-0.769)²+0.85×(1-0.769)²+0.10×(4-0.769)²+0.05×(5-0.769)²]/1.95
     = [0.95×0.591+0.85×0.053+0.10×10.44+0.05×17.91]/1.95
     = [0.561+0.045+1.044+0.896]/1.95 = 2.546/1.95 = 1.305

SUMMARY: After 1 EM round:
  Comp 1: μ=0.77, σ²=1.31, π=0.49
  Comp 2: μ=4.15, σ²=...,  π=0.51
  (would continue E-step → M-step until LL converges)
```

---

## P4: Elbow Method

```
K=1: J=150,  K=2: J=45,  K=3: J=20,  K=4: J=17,  K=5: J=15

     J
  150│×
     │
     │
   45│  ×
   20│    × ← elbow
   17│      ×
   15│        ×
     └─────────→ K
      1  2  3  4  5

  K=1→2: drop 105 (70%)
  K=2→3: drop 25  (56%)
  K=3→4: drop 3   (15%) ← diminishing returns start
  K=4→5: drop 2

  ANSWER: K=3 (elbow) ✅
```

---

> **Nav:** [📖 THEORY](ml_kmeans_gmm_em_theory.md) | 🔢 NUMERICAL | [💻 PRACTICE →](ml_kmeans_gmm_em_practice.md)

[↑ Back to Top](#-clustering-numerical)

*AI · ML · github.com/rpaut03l/TS-01*
