# 📖 Clustering: K-Means · GMM · EM Algorithm

### *K-Means · Elbow Method · GMM (Gaussian Mixture Model) · EM (Expectation-Maximization) · Hierarchical Clustering*

> **Nav:** [← Feature Selection](../Feature-Selection-DimRed/ml_pca_ica_fs_theory.md) | **Clustering** | [SVM →](../SVM-Kernels/ml_svm_kernels_theory.md)


---

## 🧠 MNEMONIC: **"KGE-HELP"**

> **K**-means · **G**MM · **E**M algorithm · **H**ierarchical · **E**lbow method · **L**loyd's · **P**robability (soft)

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | K-Means | [§1](#1-k-means-clustering) |
| 2 | GMM | [§2](#2-gaussian-mixture-models-gmm) |
| 3 | EM Algorithm | [§3](#3-em-algorithm) |
| 4 | Hierarchical Clustering | [§4](#4-hierarchical-clustering) |
| 5 | Numericals | [§5](#5-numericals) |
| 6 | Cheat Sheet | [§6](#6-cheat-sheet--exam-hacks) |

---

## 1. K-Means Clustering

### 👶 Easy Story
You have a bag of 100 marbles of different colours, but the colours are all mixed up. You want to sort them into 3 groups. You randomly pick 3 marbles as "leaders". Each marble joins the closest leader's group. Then each group picks a NEW leader (the average marble in that group). Repeat until nobody wants to switch groups!

```
K-MEANS ALGORITHM (Lloyd's):
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INPUT: data X, number of clusters K
  
  1. INITIALIZE: randomly pick K centroids μ₁,...,μK
  2. REPEAT until convergence:
     a. ASSIGN: each point → nearest centroid
        Cₖ = {xᵢ : ||xᵢ − μₖ|| ≤ ||xᵢ − μⱼ|| ∀j≠k}
     b. UPDATE: move centroids to cluster means
        μₖ = (1/|Cₖ|) Σ xᵢ   for xᵢ ∈ Cₖ
  3. STOP when: assignments don't change (or max iterations)

OBJECTIVE (minimized):
  J = Σₖ Σ_{xᵢ∈Cₖ} ||xᵢ − μₖ||²    (within-cluster sum of squares)

  ┌──────────────────────────────────────────────────┐
  │ Iteration 0:        Iteration 3 (converged):     │
  │   •  ★  •  •          ★ • • •                    │
  │ ★ •  •  •  •          • • • •                    │
  │   •  •  •  •          × × ★ ×                    │
  │ ★ •  ×  ×  ×          × × × ×                    │
  │   ×  ×  ×  ×          ★ × × ×                    │
  │ (★=random centroids)  (★=final centroids)        │
  └──────────────────────────────────────────────────┘

CHOOSING K (Elbow Method):
  Run K-means for K=1,2,3,...
  Plot total J (within-cluster SS) vs K
  Look for "elbow" where J stops decreasing sharply

     J
     │╲
     │ ╲
     │  ╲___
     │      ╲____
     │           ╲___________
     └──────────────────────→ K
           ↑ elbow = optimal K

PROS: Simple, fast O(n·K·d·t), parallelizable
CONS: Must choose K upfront, sensitive to initialization (use K-means++),
      only spherical clusters, sensitive to outliers
```

[↑ Back to Top](#-clustering-k-means--gmm--em-algorithm)

---

## 2. Gaussian Mixture Models (GMM)

### 👶 Easy Story
K-Means says "this marble is RED, period." GMM says "this marble is 70% likely red and 30% likely orange." GMM gives PROBABILITIES — it's the gentle, uncertain version of K-Means!

```
GMM MODEL:
━━━━━━━━━━
  P(x) = Σ_{k=1}^{K} πₖ · N(x | μₖ, Σₖ)

  Each cluster k has:
    πₖ = mixing coefficient (weight), Σ πₖ = 1
    μₖ = mean (center of cluster)
    Σₖ = covariance matrix (shape & spread of cluster)
    N() = Gaussian/Normal distribution

K-MEANS vs GMM:
┌────────────────────┬────────────────────┬────────────────────┐
│ Feature            │ K-Means            │ GMM                │
├────────────────────┼────────────────────┼────────────────────┤
│ Assignment         │ Hard (0 or 1)      │ Soft (probability) │
│ Cluster shape      │ Spherical ONLY     │ Any elliptical     │
│ Algorithm          │ Lloyd's            │ EM algorithm       │
│ Parameters         │ μₖ only            │ μₖ, Σₖ, πₖ           │
│ Handles overlap?   │ Poorly             │ Well               │
│ Output             │ Cluster label      │ P(cluster|point)   │
│ Faster?            │ Yes                │ No                 │
└────────────────────┴────────────────────┴────────────────────┘
```

[↑ Back to Top](#-clustering-k-means--gmm--em-algorithm)

---

## 3. EM Algorithm

### 👶 Easy Story
Imagine a game: you have a coin that's either 60% heads or 40% heads, but you don't know which. You flip it 10 times. E-step: GUESS which coin it probably is given the flips. M-step: UPDATE your guess of the coin's bias given which coin you think it is. Repeat!

```
EM ALGORITHM FOR GMM:
━━━━━━━━━━━━━━━━━━━━
  INITIALIZE: guess μₖ, Σₖ, πₖ for each cluster k

  REPEAT until convergence:
  ┌──────────────────────────────────────────────────────────┐
  │ E-STEP (Expectation): compute responsibilities           │
  │                                                          │
  │   γᵢₖ = πₖ · N(xᵢ|μₖ,Σₖ) / Σⱼ πⱼ · N(xᵢ|μⱼ,Σⱼ)             │
  │                                                          │
  │   γᵢₖ = "how much does cluster k own point i?"            │
  │   Σₖ γᵢₖ = 1 for each point i                             │
  │                                                          │
  ├──────────────────────────────────────────────────────────┤
  │ M-STEP (Maximization): update parameters                 │
  │                                                          │
  │   Nₖ = Σᵢ γᵢₖ           (effective # points in k)         │
  │   μₖ = (1/Nₖ) Σᵢ γᵢₖ xᵢ           (new mean)              │
  │   Σₖ = (1/Nₖ) Σᵢ γᵢₖ (xᵢ-μₖ)(xᵢ-μₖ)ᵀ  (new cov)            │
  │   πₖ = Nₖ / n                      (new weight)           │
  └──────────────────────────────────────────────────────────┘

  CONVERGENCE: when log-likelihood stops increasing:
    LL = Σᵢ ln[ Σₖ πₖ · N(xᵢ|μₖ,Σₖ) ]

  EM GUARANTEES: LL increases or stays same each iteration (never decreases)
  BUT: may converge to LOCAL optimum → run multiple times, pick best LL

GENERAL EM (beyond GMM):
  EM works for ANY model with "hidden/latent" variables:
    E-step: compute expected value of hidden vars given current params
    M-step: maximize likelihood with hidden vars treated as known
```

[↑ Back to Top](#-clustering-k-means--gmm--em-algorithm)

---

## 4. Hierarchical Clustering

```
AGGLOMERATIVE (bottom-up):
━━━━━━━━━━━━━━━━━━━━━━━━━
  1. Start: each point = own cluster (n clusters)
  2. Merge two CLOSEST clusters
  3. Repeat until 1 cluster remains
  → Result: DENDROGRAM (tree showing merge order)

LINKAGE METHODS (how to measure cluster distance):
  Single:   min distance between any two points (can create chains)
  Complete: max distance between any two points (compact clusters)
  Average:  average of all pairwise distances
  Ward's:   minimize total within-cluster variance (like K-Means)

DENDROGRAM:
  Height
    │     ┌────────┐
    │  ┌──┤        │
    │  │  └──┐     │
    │  │     │  ┌──┤
    │  │     │  │  │
    └──A──B──C──D──E
  
  Cut at a height → get K clusters
  No need to choose K upfront! ✅
```

[↑ Back to Top](#-clustering-k-means--gmm--em-algorithm)

---

## 5. Numericals

### N1: K-Means (2 iterations)

```
DATA: x₁=[1,1], x₂=[2,1], x₃=[4,3], x₄=[5,4]   K=2
INIT: μ₁=[1,1], μ₂=[5,4]

ITERATION 1:
  Assign (Euclidean distance):
    x₁→μ₁: √((1-1)²+(1-1)²)=0      x₁→μ₂: √(16+9)=5     → C1
    x₂→μ₁: √(1+0)=1                 x₂→μ₂: √(9+9)=4.24   → C1
    x₃→μ₁: √(9+4)=3.61              x₃→μ₂: √(1+1)=1.41   → C2
    x₄→μ₁: √(16+9)=5                x₄→μ₂: √(0+0)=0      → C2
  
  C1={x₁,x₂}, C2={x₃,x₄}
  
  Update:
    μ₁ = [(1+2)/2, (1+1)/2] = [1.5, 1.0]
    μ₂ = [(4+5)/2, (3+4)/2] = [4.5, 3.5]

ITERATION 2:
  Assign:
    x₁→μ₁: √(0.25+0)=0.5            x₁→μ₂: √(12.25+6.25)=4.3  → C1
    x₂→μ₁: √(0.25+0)=0.5            x₂→μ₂: √(6.25+6.25)=3.5   → C1
    x₃→μ₁: √(6.25+4)=3.2            x₃→μ₂: √(0.25+0.25)=0.7   → C2
    x₄→μ₁: √(12.25+9)=4.6           x₄→μ₂: √(0.25+0.25)=0.7   → C2
  
  Same assignments → CONVERGED! ✅
  FINAL: C1={x₁,x₂} centered at [1.5,1.0], C2={x₃,x₄} centered at [4.5,3.5]
  J = (0.5²+0.5² + 0.7²+0.7²) = (0.5+0.5+0.98) = 1.98 (total within-SS)
```

### N2: GMM E-step (1D, 2 components)

```
K=2: π₁=0.6, μ₁=2, σ₁=1, π₂=0.4, μ₂=6, σ₂=1.5
Point: x=3

N(3|2,1) = (1/√(2π)) exp(-(3-2)²/2) = 0.399 × 0.607 = 0.242
N(3|6,1.5) = (1/√(2π×2.25)) exp(-(3-6)²/(2×2.25))
           = (1/3.760) × exp(-2) = 0.266 × 0.135 = 0.036

γ₁ = (0.6×0.242) / (0.6×0.242 + 0.4×0.036)
   = 0.1452 / (0.1452 + 0.0144) = 0.1452/0.1596 = 0.910

γ₂ = 0.0144 / 0.1596 = 0.090

Check: 0.910 + 0.090 = 1.000 ✅
Point x=3 is 91% likely from Component 1 (μ=2). Makes sense!
```

### N3: Full EM iteration (M-step)

```
After E-step, responsibilities for 4 points, K=2:
  γ₁=[0.9, 0.8, 0.2, 0.1], γ₂=[0.1, 0.2, 0.8, 0.9]
  x = [1, 2, 5, 6]

M-STEP:
  N₁ = 0.9+0.8+0.2+0.1 = 2.0     N₂ = 0.1+0.2+0.8+0.9 = 2.0
  μ₁ = (0.9×1+0.8×2+0.2×5+0.1×6)/2.0 = (0.9+1.6+1.0+0.6)/2.0 = 4.1/2.0 = 2.05
  μ₂ = (0.1×1+0.2×2+0.8×5+0.9×6)/2.0 = (0.1+0.4+4.0+5.4)/2.0 = 9.9/2.0 = 4.95
  π₁ = 2.0/4 = 0.5    π₂ = 2.0/4 = 0.5
```

[↑ Back to Top](#-clustering-k-means--gmm--em-algorithm)

---

## 6. Cheat Sheet & Exam Hacks

```
┌─────────────────────────────────────────────────────────────┐
│              CLUSTERING CHEAT SHEET                         │
├──────────────────┬──────────────────────────────────────────┤
│ K-Means obj      │ min Σₖ Σᵢ∈Cₖ ||xᵢ-μₖ||²                   │
│ K-Means steps    │ Assign → Update → Repeat                 │
│ Choose K         │ Elbow method (plot J vs K)               │
│ GMM model        │ P(x) = Σ πₖ N(x|μₖ,Σₖ)                    │
│ E-step           │ γᵢₖ = πₖN(xᵢ|μₖ,Σₖ) / Σⱼ πⱼN(...)          │
│ M-step           │ Update μₖ, Σₖ, πₖ from γ's                │
│ EM guarantee     │ Log-likelihood never decreases           │
│ K-Means vs GMM   │ Hard vs soft, spherical vs elliptical    │
│ Hierarchical     │ Bottom-up merging → dendrogram           │
│ Linkage          │ Single/Complete/Average/Ward's           │
│ K-Means++        │ Smart initialization → better results    │
│ Complexity       │ K-Means: O(nKdt), EM: O(nK²d²t)          │
└──────────────────┴──────────────────────────────────────────┘

🧪 EXAM HACKS:
💡 K-Means = EM for GMM with equal spherical covariances
💡 EM can find LOCAL optima only → run multiple times
💡 K-Means sensitive to initialization → use K-Means++ (smart init)
💡 GMM gives probabilities → useful for soft clustering tasks
💡 Elbow method is subjective. Also try: Silhouette score, BIC/AIC
💡 In exam: show BOTH assign and update steps for K-Means
💡 For EM: show N() computation, then γ, then M-step update
```

---

> **Nav:** [← Feature Selection](../Feature-Selection-DimRed/ml_pca_ica_fs_theory.md) | **Clustering** | [SVM →](../SVM-Kernels/ml_svm_kernels_theory.md)

[↑ Back to Top](#-clustering-k-means--gmm--em-algorithm)

---

*AI · ML · github.com/rpaut03l/TS-01*
