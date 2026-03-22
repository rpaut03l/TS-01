# 📖 Feature Selection & Dim Reduction: PCA · ICA · SFFS · SBFS

### *PCA · LDA(dimred) · ICA · Sequential Feature Selection*

> **Nav:** [← LDA](../LDA/ml_lda_theory.md) | **Feature Selection & DimRed** | [Clustering →](../Clustering/ml_kmeans_gmm_em_theory.md)
>
> **Syllabus:** Fractal II — Feature Selection & Dimensionality Reduction (4 Lectures)

---

## 🧠 MNEMONIC: **"PLIS-FS"**

> **P**CA · **L**DA · **I**CA · **S**FFS · **F**eature importance · **S**BFS

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Why Reduce Dimensions? | [§1](#1-why-reduce-dimensions) |
| 2 | PCA | [§2](#2-pca--principal-component-analysis) |
| 3 | ICA | [§3](#3-ica--independent-component-analysis) |
| 4 | SFFS & SBFS | [§4](#4-sffs--sbfs--sequential-feature-selection) |
| 5 | Numericals | [§5](#5-numericals) |
| 6 | Cheat Sheet | [§6](#6-cheat-sheet--exam-hacks) |

---

## 1. Why Reduce Dimensions?

### 👶 Easy Story
Imagine describing your friend to someone. You could use 100 features (height, weight, hair count, nostril width...) but really just 5 features (tall, brown hair, glasses, deep voice, beard) are enough to identify them. Removing the useless features = dimensionality reduction. Less noise, faster computation, easier to visualize!

```
CURSE OF DIMENSIONALITY:
  As dimensions ↑:
  - Distance metrics lose meaning (all points equidistant!)
  - Data becomes sparse (need exponentially more samples)
  - Models overfit easily
  
  Fix: Remove irrelevant dimensions BEFORE training.

TWO APPROACHES:
  Feature SELECTION:  pick a SUBSET of original features (SFFS, SBFS, Lasso)
  Feature EXTRACTION: create NEW features from old ones (PCA, ICA, LDA)
  
  Selection: keeps interpretability (feature X matters!)
  Extraction: may give better compression (fewer dims needed)
```

[↑ Back to Top](#-feature-selection--dim-reduction-pca--ica--sffs--sbfs)

---

## 2. PCA — Principal Component Analysis

### 👶 Easy Story
You're photographing a 3D sculpture. The BEST photo is from the angle where you see the MOST variation (most detail). PCA finds that "best angle" — the direction of maximum variance!

```
PCA ALGORITHM (5 steps):
━━━━━━━━━━━━━━━━━━━━━━━
  1. CENTER:  X̃ = X - μ  (subtract mean from each feature)
  2. COVARIANCE:  C = (1/n) X̃ᵀX̃   (d × d matrix)
  3. EIGENDECOMPOSE:  C vₖ = λₖ vₖ  (find eigenvectors & eigenvalues)
  4. SORT:  λ₁ ≥ λ₂ ≥ ... ≥ λd  (largest first)
  5. PROJECT:  Z = X̃ V_k  (keep top k eigenvectors)

  PC1 = direction of MAX variance    (eigenvector for λ₁)
  PC2 = direction of 2nd max variance, ORTHOGONAL to PC1
  ...

VARIANCE EXPLAINED:
  By PCk = λₖ / Σλᵢ
  Total by top k = Σ(k) λₖ / Σ(d) λᵢ
  Rule of thumb: keep enough PCs for ≥ 95% variance

         Variance Explained
   100%│─────────────────── ←flat
    95%│          ●────────
       │       ●
    80%│    ●
       │  ●
       │●
    0% └──────────────────→ # of PCs
         1  2  3  4  5 ... d
         Keep k where cumulative ≥ 95%

PROPERTIES:
  - Unsupervised (no labels needed)
  - Linear transformation only
  - PCs are orthogonal (uncorrelated)
  - First PC captures most info, rest capture less and less
  - Sensitive to scale → ALWAYS standardize first!
```

[↑ Back to Top](#-feature-selection--dim-reduction-pca--ica--sffs--sbfs)

---

## 3. ICA — Independent Component Analysis

### 👶 Easy Story
You're at a party with 3 speakers. 3 microphones record mixed sounds. ICA is like a magical unmixer that separates each speaker's voice from the mix — even though you only hear the mixed recordings!

```
ICA vs PCA:
━━━━━━━━━━━━━━━━━━━━━━━
  PCA:  finds UNCORRELATED components (orthogonal, max variance)
  ICA:  finds INDEPENDENT components (statistically independent, non-Gaussian)

  PCA removes 2nd-order correlations (covariance)
  ICA removes ALL statistical dependencies (higher-order too)

MODEL:
  x = A s    (observed = mixing_matrix × sources)
  s = W x    (sources = unmixing_matrix × observed)
  
  Goal: find W such that components of s are maximally independent
  
  Algorithm (FastICA):
  1. Center and whiten data (PCA first)
  2. Find W that maximizes non-Gaussianity of Ws
     (central limit theorem: mixtures are more Gaussian than sources)
  3. Use negentropy or kurtosis as measure of non-Gaussianity

ASSUMPTIONS:
  - Sources are statistically independent
  - Sources are NON-Gaussian (at most one can be Gaussian)
  - Mixing is linear and instantaneous
  
APPLICATIONS: blind source separation, fMRI analysis, signal processing
```

[↑ Back to Top](#-feature-selection--dim-reduction-pca--ica--sffs--sbfs)

---

## 4. SFFS & SBFS — Sequential Feature Selection

### 👶 Easy Story
**SFFS (Forward)**: Start with zero toys. Add the BEST toy. Then add the 2nd best. If adding a 3rd toy made the 1st one useless, remove it! Keep going: add one, optionally remove one.

**SBFS (Backward)**: Start with ALL toys. Remove the WORST one. Then remove the next worst. If removing one made another essential again, add it back!

```
SFFS — Sequential Forward Floating Selection:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Start: empty set S = {}
  Repeat:
    1. INCLUSION: add feature that gives BEST improvement
       S = S ∪ {best_feature}
    2. CONDITIONAL EXCLUSION: check if removing any feature improves S
       While removing a feature from S improves performance:
         Remove the worst feature
  Until |S| = desired size or no improvement

SBFS — Sequential Backward Floating Selection:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Start: full set S = {all features}
  Repeat:
    1. EXCLUSION: remove feature whose removal causes LEAST damage
       S = S \ {worst_feature}
    2. CONDITIONAL INCLUSION: check if adding back any removed feature helps
       While adding a feature to S improves performance:
         Add the best feature back
  Until |S| = desired size or no improvement

COMPARISON:
┌────────────┬──────────────────┬──────────────────┐
│            │ Forward (SFFS)   │ Backward (SBFS)  │
├────────────┼──────────────────┼──────────────────┤
│ Starts with│ Empty set        │ Full set         │
│ Direction  │ Add then remove  │ Remove then add  │
│ Good when  │ Few features     │ Many features    │
│            │ truly matter     │ with some noise  │
│ Complexity │ O(d²) evaluations│ O(d²) evaluations│
│ "Floating" │ backtrack step   │ backtrack step   │
│ = smarter  │ undoes bad adds  │ undoes bad drops │
└────────────┴──────────────────┴──────────────────┘

vs SIMPLE FORWARD/BACKWARD (no floating):
  SFS: only add, never remove → can get stuck
  SBS: only remove, never add back → can get stuck
  SFFS/SBFS: floating step = BACKTRACK = better solutions!
  
OTHER METHODS:
  Filter:   Correlation, chi-squared, mutual info (fast, model-free)
  Wrapper:  SFFS, SBFS, genetic algo (uses model, slow but better)
  Embedded: Lasso (L1), RF importance (built into model)
```

[↑ Back to Top](#-feature-selection--dim-reduction-pca--ica--sffs--sbfs)

---

## 5. Numericals

### N1: PCA on 2D Data

```
DATA: X = [[2,4], [4,6], [6,8], [8,10]]  (4 points, 2 features)

STEP 1: Center
  μ = [5, 7]
  X̃ = [[-3,-3], [-1,-1], [1,1], [3,3]]

STEP 2: Covariance
  C = (1/4) X̃ᵀX̃ = (1/4) × [9+1+1+9  9+1+1+9] = [5  5]
                              [9+1+1+9  9+1+1+9]   [5  5]

STEP 3: Eigenvalues
  det(C - λI) = 0
  (5-λ)² - 25 = 0 → λ² - 10λ = 0 → λ(λ-10) = 0
  λ₁ = 10, λ₂ = 0

STEP 4: Eigenvectors
  For λ₁=10: (C-10I)v = 0 → [-5  5][v₁] = 0 → v₁ = [1/√2, 1/√2]
  For λ₂=0:  Cv = 0 → v₂ = [1/√2, -1/√2]

STEP 5: Variance explained
  PC1 = 10/(10+0) = 100%!
  All variance in one direction → data is perfectly linear.

  PC1 direction: [1/√2, 1/√2] = 45° line (makes sense: y = x + 2)
```

### N2: How Many PCs to Keep?

```
Eigenvalues: λ = [4.5, 2.1, 0.8, 0.4, 0.2]
Total = 8.0

  PC1: 4.5/8.0 = 56.3%    cumulative = 56.3%
  PC2: 2.1/8.0 = 26.3%    cumulative = 82.5%
  PC3: 0.8/8.0 = 10.0%    cumulative = 92.5%
  PC4: 0.4/8.0 = 5.0%     cumulative = 97.5% ← ≥ 95%, stop here!
  
  ANSWER: Keep 4 PCs (97.5% variance retained)
  Reduced from 5D → 4D (only 1 dim removed, data is high-info)
```

### N3: SFFS Walkthrough

```
Features: {A, B, C, D}, using accuracy as criterion

Round 1 (ADD): Try each alone:
  {A}→72%, {B}→68%, {C}→81%, {D}→75%
  BEST: add C → S = {C}, acc = 81%

Round 1 (REMOVE): only C in set, can't remove → skip

Round 2 (ADD): Try adding each to {C}:
  {C,A}→85%, {C,B}→79%, {C,D}→88%
  BEST: add D → S = {C,D}, acc = 88%

Round 2 (REMOVE): Try removing each:
  {C} without D → 81% < 88% → don't remove
  {D} without C → 75% < 88% → don't remove
  → No removal

Round 3 (ADD): Try adding to {C,D}:
  {C,D,A}→90%, {C,D,B}→87%
  BEST: add A → S = {C,D,A}, acc = 90%

Round 3 (REMOVE): Try removing each:
  {C,D}→88%, {C,A}→85%, {D,A}→82%
  All worse → no removal

FINAL: S = {C, D, A} with accuracy 90%
Selected 3 out of 4 features (removed B as it added noise)
```

[↑ Back to Top](#-feature-selection--dim-reduction-pca--ica--sffs--sbfs)

---

## 6. Cheat Sheet & Exam Hacks

```
┌────────────────────────────────────────────────────────────────┐
│           FEATURE SELECTION & DIM REDUCTION CHEAT SHEET        │
├──────────────────┬─────────────────────────────────────────────┤
│ PCA              │ Max variance, unsupervised, eigendecompose C│
│ PCA steps        │ Center → Cov → Eigen → Sort → Project       │
│ Variance of PCk  │ λₖ / Σλᵢ                                    │
│ Keep # PCs       │ Until cumulative variance ≥ 95%             │
│ ICA              │ Max independence, non-Gaussian sources      │
│ ICA vs PCA       │ ICA: independent. PCA: uncorrelated.        │
│ SFFS             │ Forward + floating (add then maybe remove)  │
│ SBFS             │ Backward + floating (remove then maybe add) │
│ Filter           │ Correlation, chi-sq (fast, model-free)      │
│ Wrapper          │ SFFS/SBFS (slow, uses model)                │
│ Embedded         │ Lasso L1, RF importance (built-in)          │
│ PCA vs LDA       │ PCA=unsupervised, LDA=supervised            │
│ Kernel PCA       │ PCA in kernel space (non-linear)            │
└──────────────────┴─────────────────────────────────────────────┘

🧪 EXAM HACKS:
💡 PCA: ALWAYS center/standardize first!
💡 Eigenvalue = variance along that PC direction
💡 PCA is LINEAR. For non-linear: use Kernel PCA
💡 ICA needs NON-Gaussian sources (at most 1 Gaussian allowed)
💡 SFFS > SFS because floating step avoids local optima
💡 Curse of dimensionality: need exponentially more data as d↑
💡 Scree plot: plot eigenvalues, look for "elbow"
```

---

> **Nav:** [← LDA](../LDA/ml_lda_theory.md) | **Feature Selection & DimRed** | [Clustering →](../Clustering/ml_kmeans_gmm_em_theory.md)

[↑ Back to Top](#-feature-selection--dim-reduction-pca--ica--sffs--sbfs)

---

*AI · ML · github.com/rpaut03l/TS-01*
