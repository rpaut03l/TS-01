# 🔢 Feature Selection & Dim Reduction: NUMERICAL

### *PCA eigendecomposition, variance %, SFFS step-by-step.*

> **Nav:** [📖 THEORY](ml_pca_ica_fs_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_pca_ica_fs_practice.md)

---

## 📦 KEY FORMULAS

```
┌──────────────────────────────────────────────────────────────┐
│ CENTER: X̃ = X - μ                                            │
│ COV:    C = (1/n) X̃ᵀX̃                                        │
│ EIGEN:  C v = λ v                                            │
│ VAR %:  λₖ / Σλᵢ                                             │
│ OUTPUT: O_pca = (I-K+2P)/S + 1  (wrong context — that's CNN) │
│ SFFS:   add best → remove worst if it helps → repeat         │
└──────────────────────────────────────────────────────────────┘
```

---

## P1: PCA on 3D Data → 2D

```
DATA (4 points, 3 features):
  x₁=[1,2,1], x₂=[3,4,2], x₃=[5,6,3], x₄=[7,8,4]

STEP 1: CENTER
  μ = [4, 5, 2.5]
  X̃ = [[-3,-3,-1.5], [-1,-1,-0.5], [1,1,0.5], [3,3,1.5]]

STEP 2: COVARIANCE (4 points)
  C = (1/4) X̃ᵀX̃
  X̃ᵀX̃[0,0] = 9+1+1+9 = 20    → C[0,0] = 5.0
  X̃ᵀX̃[0,1] = 9+1+1+9 = 20    → C[0,1] = 5.0
  X̃ᵀX̃[0,2] = 4.5+0.5+0.5+4.5=10 → C[0,2] = 2.5
  X̃ᵀX̃[1,1] = 9+1+1+9 = 20    → C[1,1] = 5.0
  X̃ᵀX̃[1,2] = 4.5+0.5+0.5+4.5=10 → C[1,2] = 2.5
  X̃ᵀX̃[2,2] = 2.25+0.25+0.25+2.25=5 → C[2,2] = 1.25

  C = [5.0  5.0  2.5]
      [5.0  5.0  2.5]
      [2.5  2.5  1.25]

STEP 3: EIGENVALUES
  det(C - λI) = 0
  λ₁ = 11.25, λ₂ = 0, λ₃ = 0
  (rank 1 data — all points on a line!)

STEP 4: VARIANCE EXPLAINED
  PC1: 11.25/11.25 = 100%  ← one component captures everything!
  Keep: 1 PC (3D → 1D)
```

[↑ Back to Top](#-feature-selection--dim-reduction-numerical)

---

## P2: How Many PCs? (Scree Analysis)

```
Eigenvalues: λ = [6.2, 3.1, 1.5, 0.8, 0.3, 0.1]
Total = 12.0

  PC1: 6.2/12 = 51.7%   cum = 51.7%
  PC2: 3.1/12 = 25.8%   cum = 77.5%
  PC3: 1.5/12 = 12.5%   cum = 90.0%
  PC4: 0.8/12 =  6.7%   cum = 96.7% ← ≥95%, STOP
  PC5: 0.3/12 =  2.5%   cum = 99.2%
  PC6: 0.1/12 =  0.8%   cum = 100%

  ANSWER: Keep 4 PCs (96.7% variance). Reduced 6D → 4D.
```

[↑ Back to Top](#-feature-selection--dim-reduction-numerical)

---

## P3: SFFS Walkthrough (4 Features)

```
Features {A,B,C,D}. Criterion: 5-fold CV accuracy.

Step 1 — ADD best singleton:
  {A}=71%, {B}=65%, {C}=78%, {D}=73%  → add C → S={C}
Step 1 — REMOVE? Only 1 feature, skip.

Step 2 — ADD best to {C}:
  {C,A}=82%, {C,B}=76%, {C,D}=85%  → add D → S={C,D}
Step 2 — REMOVE from {C,D}:
  {C}=78% < 85%, {D}=73% < 85%  → no removal.

Step 3 — ADD best to {C,D}:
  {C,D,A}=87%, {C,D,B}=84%  → add A → S={C,D,A}
Step 3 — REMOVE from {C,D,A}:
  {C,D}=85% < 87%, {C,A}=82% < 87%, {D,A}=80% < 87%  → no removal.

FINAL: S = {C, D, A} → 87% accuracy (3 of 4 features, dropped B)
```

---

> **Nav:** [📖 THEORY](ml_pca_ica_fs_theory.md) | 🔢 NUMERICAL | [💻 PRACTICE →](ml_pca_ica_fs_practice.md)

[↑ Back to Top](#-feature-selection--dim-reduction-numerical)

*AI · ML · github.com/rpaut03l/TS-01*
