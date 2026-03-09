# 🔢 Ch9 — Unsupervised Learning: NUMERICAL
### *Rules first → then solve. Mind-friendly. Every step shown.*

> **Nav:** [← INDEX](./ml_ch9_index.md) | [📖 THEORY](./ml_ch9_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](./ml_ch9_practice.md)

---

## 📦 ALL FORMULAS — Read This First!

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. K-MEANS DISTANCE                                             │
│    Squared Euclidean: d²(a,b) = (x₂−x₁)² + (y₂−y₁)²             │
│    Assign point xᵢ → cluster k with SMALLEST d²                 │
│    Update centroid: μₖ = average of all points in cluster k     │
│    Inertia J = Σᵢ d²(xᵢ, its centroid)                          │
├─────────────────────────────────────────────────────────────────┤
│ 2. SILHOUETTE SCORE                                             │
│    a(i) = mean distance to points in SAME cluster               │
│    b(i) = mean distance to points in NEAREST other cluster      │
│    s(i) = (b−a) / max(a,b)                                      │
│    Range: −1 (wrong cluster) → 0 (border) → +1 (perfect)        │
│    Overall score = mean of all s(i)                             │
├─────────────────────────────────────────────────────────────────┤
│ 3. GMM — E-STEP (responsibilities)                              │
│    Normal PDF: N(x|μ,σ) = (1/σ√2π) · exp(−(x−μ)²/2σ²)           │
│    Unnorm: r̃(i,k) = φₖ · N(xᵢ|μₖ,σₖ)                             │
│    Normalize: r(i,k) = r̃(i,k) / Σⱼ r̃(i,j)                       │
│    r(i,k) = probability point i belongs to Gaussian k           │
├─────────────────────────────────────────────────────────────────┤
│ 4. GMM — M-STEP (update parameters)                             │
│    Nₖ = Σᵢ r(i,k)          ← effective count for cluster k      │
│    φₖ = Nₖ / n              ← mixing weight                      │
│    μₖ = Σᵢ r(i,k)·xᵢ / Nₖ ← weighted mean                        │
├─────────────────────────────────────────────────────────────────┤
│ 5. MODEL SELECTION (BIC / AIC)                                  │
│    BIC = −2·ℓ + k·ln(n)   ← penalises complexity more           │
│    AIC = −2·ℓ + 2k                                              │
│    ℓ = maximised log-likelihood, k = #params, n = #samples      │
│    LOWER = BETTER. Pick K with lowest BIC/AIC.                  │
├─────────────────────────────────────────────────────────────────┤
│ 6. ANOMALY THRESHOLD (GMM)                                      │
│    score = gm.score_samples(x) → log probability                │
│    threshold = percentile(training_scores, 4)                   │
│    If score < threshold → ANOMALY ⚠️                            │
└─────────────────────────────────────────────────────────────────┘
```

> 💡 **Key constants:** ln(2)≈0.693, 1/√(2π)≈0.3989, e⁻¹≈0.368, e⁻²≈0.135
> 💡 **Euclidean vs Squared:** K-Means uses SQUARED distance (no √ needed, faster)

---

## P1 — K-Means: Full Iteration by Hand

**Given:** Points A(1,1) B(2,2) C(8,8) D(9,9) E(1,2). K=2. Start: μ₁=A(1,1), μ₂=C(8,8).

```
👶 Think: each point runs to the nearest magnet. Then each magnet moves to centre of its group.

── ITERATION 1: Assign ──────────────────────────────────────
d²(point, μ) = (x−μx)² + (y−μy)²

Point A(1,1): d²(A,μ₁)=0         d²(A,μ₂)=(1−8)²+(1−8)²=98   → C1
Point B(2,2): d²(B,μ₁)=1+1=2     d²(B,μ₂)=36+36=72            → C1
Point C(8,8): d²(C,μ₁)=49+49=98  d²(C,μ₂)=0                   → C2
Point D(9,9): d²(D,μ₁)=64+64=128 d²(D,μ₂)=1+1=2               → C2
Point E(1,2): d²(E,μ₁)=0+1=1     d²(E,μ₂)=49+36=85            → C1

Cluster 1: {A(1,1), B(2,2), E(1,2)}
Cluster 2: {C(8,8), D(9,9)}

── ITERATION 1: Update centroids ───────────────────────────
μ₁_new = mean of {(1,1),(2,2),(1,2)}
       = ((1+2+1)/3, (1+2+2)/3) = (4/3, 5/3) = (1.33, 1.67)

μ₂_new = mean of {(8,8),(9,9)}
       = ((8+9)/2, (8+9)/2) = (8.5, 8.5)

── ITERATION 2: Re-assign with new centroids ────────────────
(All assignments stay the same → CONVERGED ✅)

── INERTIA ──────────────────────────────────────────────────
J = d²(A,μ₁) + d²(B,μ₁) + d²(E,μ₁) + d²(C,μ₂) + d²(D,μ₂)

A(1,1) to μ₁(1.33,1.67): 0.11+0.45 = 0.56
B(2,2) to μ₁(1.33,1.67): 0.45+0.11 = 0.56
E(1,2) to μ₁(1.33,1.67): 0.11+0.11 = 0.22
C(8,8) to μ₂(8.5,8.5):   0.25+0.25 = 0.50
D(9,9) to μ₂(8.5,8.5):   0.25+0.25 = 0.50

Total Inertia J = 0.56+0.56+0.22+0.50+0.50 = 2.34 ✅
```

---

## P2 — Silhouette Score by Hand

**Given:** P1(0,0), P2(1,0), P3(5,0). Clusters: C1={P1,P2}, C2={P3}.

```
👶 Think: Is each point cozy in its own group? Far from other groups?

DISTANCES (1D, just |x₂−x₁|):
  dist(P1,P2) = 1      dist(P1,P3) = 5      dist(P2,P3) = 4

── Point P1 (in C1) ─────────────────────────────────────────
  a(P1) = mean dist to other C1 members = dist(P1,P2) = 1
  b(P1) = mean dist to C2 = dist(P1,P3) = 5
  s(P1) = (b−a)/max(b,a) = (5−1)/5 = 4/5 = 0.80

── Point P2 (in C1) ─────────────────────────────────────────
  a(P2) = dist(P2,P1) = 1
  b(P2) = dist(P2,P3) = 4
  s(P2) = (4−1)/4 = 3/4 = 0.75

── Point P3 (in C2, alone) ──────────────────────────────────
  a(P3) = 0  (no other members in C2)
  b(P3) = mean dist to C1 = (5+4)/2 = 4.5
  s(P3) = (4.5−0)/4.5 = 1.00  ← perfect! Far from all others

── Overall ──────────────────────────────────────────────────
  Avg silhouette = (0.80 + 0.75 + 1.00) / 3 = 0.85 ✅

Interpretation: 0.85 is close to 1 → good clustering!
```

---

## P3 — GMM E-Step: Compute Responsibilities

**Given:** 1D, K=2 Gaussians. μ₁=0, σ₁=1, φ₁=0.5. μ₂=5, σ₂=1, φ₂=0.5. Point x=2.

```
👶 Think: which Gaussian (bell curve) is this point more likely from?

FORMULA: N(x|μ,σ) = (1/σ√2π) · exp(−(x−μ)²/2σ²)
         constant 1/√2π ≈ 0.3989

── Gaussian 1 (μ=0) ─────────────────────────────────────────
  N(2|0,1) = 0.3989 · exp(−(2−0)²/2)
            = 0.3989 · exp(−2)
            = 0.3989 × 0.1353
            = 0.0540

── Gaussian 2 (μ=5) ─────────────────────────────────────────
  N(2|5,1) = 0.3989 · exp(−(2−5)²/2)
            = 0.3989 · exp(−4.5)
            = 0.3989 × 0.0111
            = 0.00443

── Unnormalized responsibilities ───────────────────────────
  r̃(2,k1) = φ₁ · N₁ = 0.5 × 0.0540  = 0.0270
  r̃(2,k2) = φ₂ · N₂ = 0.5 × 0.00443 = 0.00222
  Sum = 0.0270 + 0.00222 = 0.02922

── Normalize ────────────────────────────────────────────────
  r(2,k1) = 0.0270 / 0.02922 = 0.924  → 92.4% from Gaussian 1
  r(2,k2) = 0.00222 / 0.02922 = 0.076 → 7.6%  from Gaussian 2

Makes sense! x=2 is close to μ₁=0, far from μ₂=5 ✅
```

---

## P4 — GMM M-Step: Update Parameters

**Given:** 3 points, after E-step responsibilities:

```
Point  x    r(k1)  r(k2)
 1     1    0.9    0.1
 2     2    0.8    0.2
 3     8    0.1    0.9
```

```
👶 Think: each Gaussian updates its "centre of gravity" using soft membership.

── Effective counts ─────────────────────────────────────────
  N₁ = 0.9 + 0.8 + 0.1 = 1.8
  N₂ = 0.1 + 0.2 + 0.9 = 1.2
  Check: 1.8 + 1.2 = 3 = n ✅

── Mixing weights φ ─────────────────────────────────────────
  φ₁ = N₁/n = 1.8/3 = 0.60
  φ₂ = N₂/n = 1.2/3 = 0.40

── Updated means μ ──────────────────────────────────────────
  μ₁ = (0.9×1 + 0.8×2 + 0.1×8) / 1.8
     = (0.9 + 1.6 + 0.8) / 1.8
     = 3.3 / 1.8
     = 1.83

  μ₂ = (0.1×1 + 0.2×2 + 0.9×8) / 1.2
     = (0.1 + 0.4 + 7.2) / 1.2
     = 7.7 / 1.2
     = 6.42

Before: μ₁=0, μ₂=5  →  After: μ₁=1.83, μ₂=6.42
Gaussian 1 pulled toward points 1,2. Gaussian 2 pulled toward point 3 ✅
```

---

## P5 — Choosing K: Elbow vs Silhouette

**Given inertias:** K=1:500, K=2:200, K=3:100, K=4:80, K=5:75, K=6:72
**Given silhouettes:** K=2:0.65, K=3:0.72, K=4:0.68, K=5:0.60

```
── ELBOW METHOD ─────────────────────────────────────────────
Drops: K1→2: 300  K2→3: 100  K3→4: 20  K4→5: 5  K5→6: 3

Inertia
500 │ ●
400 │
300 │
200 │    ●
100 │       ●
 80 │          ●─────────
    └──────────────────── K
         elbow at K=3 ✅

After K=3: tiny improvement → STOP at K=3

── SILHOUETTE METHOD ────────────────────────────────────────
K=2: 0.65
K=3: 0.72  ← HIGHEST → best K=3 ✅
K=4: 0.68
K=5: 0.60

Both methods agree: K=3 is optimal ✅
```

---

## P6 — BIC Model Selection

**Given:** n=100 samples, 2D data (d=2).

```
BIC = −2·ℓ + k·ln(n)
      where ℓ = log-likelihood, k = #free params

Parameters per GMM component (full covariance, 2D):
  mean vector:   d = 2 values
  covariance:    d(d+1)/2 = 3 values  (symmetric 2×2 matrix)
  mixing weight: 1 value
  Per component: 6 total
  For K components: K×6 − 1  (one φ is constrained: Σφ=1)

  ln(100) = 4.605

Scenario:
  K=1: k=5,  ℓ=−200  → BIC = 400 + 5×4.605 = 400+23 = 423
  K=2: k=11, ℓ=−150  → BIC = 300 + 11×4.605 = 300+51 = 351 ← LOWEST ✅
  K=3: k=17, ℓ=−145  → BIC = 290 + 17×4.605 = 290+78 = 368

Best model = K=2 (BIC=351 is smallest) ✅

Why K=3 loses despite better ℓ?
  Its 6 extra parameters cost 6×4.605=27.6 in BIC penalty
  But ℓ only improved by 5 → net effect: BIC gets WORSE
```

---

## P7 — Anomaly Detection Threshold

**Given:** GMM score_samples on training data: mean=−5.2, std=0.8. Flag bottom 4%.

```
👶 Think: points with very LOW probability are weird/rare → anomalies.

4th percentile ↔ z-score ≈ −1.75

threshold = mean + z×std
          = −5.2 + (−1.75)×0.8
          = −5.2 − 1.4
          = −6.6

Rule: If gm.score_samples(x) < −6.6 → flag as ANOMALY ⚠️

Visual:
  log-prob
  −4 │ normal zone ████████████████
  −5 │              ██████████████
  −6 │                       █████
  −6.6 ├── threshold ─────────────
  −7 │ anomalies ██
  −8 │ anomalies █
```

---

## 🃏 FORMULA CARD (Tear-Out)

```
K-MEANS assign:    c(i) = argmin_k  (xᵢ−μₖ)²
K-MEANS update:    μₖ = mean of all xᵢ in cluster k
INERTIA:           J = Σᵢ d²(xᵢ, μ_c(i))
SILHOUETTE s(i):   (b−a) / max(a,b)
                   a=intra-dist, b=nearest-other-dist
GMM E-step:        r(i,k) = φₖ·N(xᵢ|μₖ,σₖ) / Σⱼ φⱼ·N(xᵢ|μⱼ,σⱼ)
GMM M-step:        μₖ = Σ r(i,k)·xᵢ / Σ r(i,k);  φₖ = Nₖ/n
BIC:               −2ℓ + k·ln(n)   (lower=better)
AIC:               −2ℓ + 2k        (lower=better)
ANOMALY:           score_samples(x) < percentile(train_scores, 4)
```

---

## 🧪 EXAM HACKS

```
💡 K-Means: use SQUARED distance for assignment (no sqrt needed!)
💡 Silhouette +1 = perfect, 0 = border, −1 = wrong cluster
💡 GMM E-step output = probabilities (soft). M-step output = new μ, σ, φ.
💡 BIC vs AIC: BIC penalises more when n > 8 (ln(n) > 2). Use BIC for large n.
💡 Anomaly: LOW log-probability = unusual. Use gm.score_samples()
💡 Silhouette of a LONE point in its cluster = always 1.0 (no intra-dist)
💡 Inertia always ↓ as K↑ — not a good metric alone → use silhouette!
```

---

> **Nav:** [← INDEX](./ml_ch9_index.md) | [📖 THEORY](./ml_ch9_theory.md) | 🔢 NUMERICAL | [💻 PRACTICE →](./ml_ch9_practice.md)

* AI · ML · github.com/rpaut03l/TS-01*
