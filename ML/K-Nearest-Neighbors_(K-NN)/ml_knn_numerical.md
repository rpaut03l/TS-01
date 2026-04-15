# 🔢 ML K-Nearest Neighbors: NUMERICAL

### *Rules first → then solve. Every step shown.*

> **Nav:** [← INDEX](../ml_master_gap_index.md) | [📖 THEORY](ml_knn_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE GUIDE](k-nn_algorithm_practice_guide_with_code.md)

---

## 📦 ALL FORMULAS

```
┌──────────────────────────────────────────────────────────────┐
│ EUCLIDEAN:   d(x,y) = √ Σ (xᵢ − yᵢ)²                         │
│ MANHATTAN:   d(x,y) = Σ |xᵢ − yᵢ|                            │
│ MINKOWSKI:   d(x,y) = ( Σ |xᵢ − yᵢ|ᵖ )^(1/p)                 │
│ CHEBYSHEV:   d(x,y) = max |xᵢ − yᵢ|                          │
│ COSINE:      d(x,y) = 1 − (x·y)/(‖x‖‖y‖)                     │
│ HAMMING:     d(x,y) = (1/d) Σ 1[xᵢ ≠ yᵢ]                     │
│                                                              │
│ VOTE (unweighted):  ŷ = argmax_c Σᵢ∈Nₖ 1[yᵢ=c]               │
│ VOTE (weighted):    ŷ = argmax_c Σᵢ∈Nₖ (1/dᵢ) · 1[yᵢ=c]      │
│ REGRESSION:         ŷ = (1/k) Σᵢ∈Nₖ yᵢ                       │
│                                                              │
│ STANDARDIZE:   x' = (x − μ) / σ                              │
│ MIN-MAX:       x' = (x − x_min) / (x_max − x_min)            │
└──────────────────────────────────────────────────────────────┘
```

---

## P1: Classify a query with k = 3 (Euclidean)

```
TRAINING (feature = [x1, x2], label):
  (2, 3) → A
  (1, 1) → A
  (4, 5) → B
  (6, 7) → B
  (3, 3) → A

QUERY: x = (3, 4),  k = 3

STEP 1 — Euclidean distances
  d to (2,3) : √(1² + 1²) = √2   ≈ 1.414
  d to (1,1) : √(2² + 3²) = √13  ≈ 3.606
  d to (4,5) : √(1² + 1²) = √2   ≈ 1.414
  d to (6,7) : √(3² + 3²) = √18  ≈ 4.243
  d to (3,3) : √(0² + 1²) = √1   = 1.000

STEP 2 — Sort
  (3,3)=1.000 A
  (2,3)=1.414 A
  (4,5)=1.414 B
  (1,1)=3.606 A
  (6,7)=4.243 B

STEP 3 — Pick k=3 closest
  (3,3) A,  (2,3) A,  (4,5) B

STEP 4 — Majority vote
  Counts: A = 2, B = 1
  ŷ = A ✓
```

[↑ Back to Top](#-ml-k-nearest-neighbors-numerical)

---

## P2: Same query, distance-weighted voting

```
Using the neighbors from P1:
  (3,3) d=1.000  A   weight = 1/1.000 = 1.000
  (2,3) d=1.414  A   weight = 1/1.414 ≈ 0.707
  (4,5) d=1.414  B   weight = 1/1.414 ≈ 0.707

VOTE TOTALS:
  A: 1.000 + 0.707 = 1.707
  B:                 0.707

ŷ = A ✓   (same result, but margin is bigger)

TAKEAWAY: weighting by 1/d gives the very-close neighbor a bigger say.
```

[↑ Back to Top](#-ml-k-nearest-neighbors-numerical)

---

## P3: Manhattan vs Euclidean — different winners

```
Points:
  P1 = (0, 0)
  P2 = (3, 4)
  P3 = (5, 0)

Euclidean:
  d(P1,P2) = √(9+16) = √25 = 5
  d(P1,P3) = √(25+0) = 5
  TIE at distance 5

Manhattan:
  d(P1,P2) = 3 + 4 = 7
  d(P1,P3) = 5 + 0 = 5
  P3 is closer (5 < 7)

LESSON: metric choice can change which neighbor wins. Pick based
on your data — grid data prefers Manhattan, continuous prefers
Euclidean.
```

[↑ Back to Top](#-ml-k-nearest-neighbors-numerical)

---

## P4: Feature scaling really matters

```
DATA (2 features, very different scales)
  age     [years]
  salary  [dollars]

Training point  A:  age=25,  salary=40000   → class 0
Training point  B:  age=55,  salary=42000   → class 1
Query           Q:  age=27,  salary=41500

WITHOUT SCALING — Euclidean
  d(Q, A) = √( (27−25)² + (41500−40000)² )
          = √( 4 + 2,250,000 )
          ≈ 1500.0
  d(Q, B) = √( (27−55)² + (41500−42000)² )
          = √( 784 + 250,000 )
          ≈ 500.8

  B is "closer"  ⟹  predict class 1 (wrong intuitively — Q's age is near A)

WITH STANDARDIZATION (fit on the two training points; σ is small but we just illustrate)
  Assume μ_age=40, σ_age=15,  μ_sal=41000, σ_sal=1000  (from full training set)

  A' = ((25−40)/15, (40000−41000)/1000) = (−1.0, −1.0)
  B' = ((55−40)/15, (42000−41000)/1000) = (+1.0, +1.0)
  Q' = ((27−40)/15, (41500−41000)/1000) = (−0.867, +0.500)

  d(Q', A') = √((−0.867+1)² + (0.500+1)²) = √(0.018 + 2.25) = 1.506
  d(Q', B') = √((−0.867−1)² + (0.500−1)²) = √(3.486 + 0.25) = 1.933

  A is closer  ⟹  predict class 0 (now the age signal is visible)

LESSON: without scaling, "salary" dominated everything.
```

[↑ Back to Top](#-ml-k-nearest-neighbors-numerical)

---

## P5: K-NN regression by hand (k = 3)

```
TRAINING ((x), price in $k):
  (1000 sqft) → 200
  (1200 sqft) → 240
  (1500 sqft) → 320
  (1800 sqft) → 380
  (2000 sqft) → 420

QUERY: x = 1400 sqft, k = 3

DISTANCES
  1000: |1400−1000| = 400
  1200: |1400−1200| = 200
  1500: |1400−1500| = 100
  1800: |1400−1800| = 400
  2000: |1400−2000| = 600

SORT → top 3: 1500 (100), 1200 (200), 1000 (400) or 1800 (400)  ← tie

Assume we pick 1500, 1200, and 1000 (sklearn uses stable order):
  y values: 320, 240, 200

UNWEIGHTED MEAN:  ŷ = (320 + 240 + 200) / 3 = 253.33

DISTANCE-WEIGHTED MEAN:
  weights:  1/100, 1/200, 1/400  = 0.010, 0.005, 0.0025
  Σw = 0.0175
  ŷ = (320·0.010 + 240·0.005 + 200·0.0025) / 0.0175
    = (3.200 + 1.200 + 0.500) / 0.0175
    = 4.900 / 0.0175
    ≈ 280.0

NOTE: weighting pulls the prediction toward the very-close 1500 sqft point.
```

[↑ Back to Top](#-ml-k-nearest-neighbors-numerical)

---

## P6: Effect of k on bias/variance — toy 1-D sketch

```
TRAIN: 10 points along the line y = sin(x) + noise
TEST : predict at x = 3.5

k=1 :   ŷ equals the single nearest training y → tracks noise → HIGH VARIANCE
k=3 :   ŷ = avg of 3 nearest → smoother
k=5 :   ŷ = avg of 5 nearest → even smoother
k=10:   ŷ = global mean → constant function → HIGH BIAS

Generalization error shape vs k:
      error
        │
        │\
        │ \            ______
        │  \_________/
        │
        └─────────────────── k
       1   3   5   7   9

→ U-shape.  Optimal k is usually found by CV.
```

[↑ Back to Top](#-ml-k-nearest-neighbors-numerical)

---

## P7: Cosine similarity for text-style vectors

```
DOCS (term-frequency vectors)
  d1 = [1, 2, 3]
  d2 = [2, 4, 6]
  d3 = [3, 0, 0]

QUERY: q = [1, 1, 1]

Cosine similarity: sim(x, y) = (x·y) / (‖x‖ ‖y‖)

q · d1 = 1+2+3 = 6    ‖q‖=√3,  ‖d1‖=√14
sim(q, d1) = 6 / (√3·√14) = 6 / 6.481 ≈ 0.926

q · d2 = 2+4+6 = 12   ‖d2‖=√56
sim(q, d2) = 12 / (√3·√56) = 12 / 12.961 ≈ 0.926   ← same as d1!

q · d3 = 3           ‖d3‖=3
sim(q, d3) = 3 / (√3·3) = 3 / 5.196 ≈ 0.577

OBSERVE: d1 and d2 point in the SAME direction (d2 = 2·d1), so they
have equal cosine similarity. Magnitude (document length) is ignored.

Cosine DISTANCE = 1 − sim  →  d1, d2 both 0.074; d3 is 0.423
→ nearest neighbor is d1 (or d2, tie).
```

[↑ Back to Top](#-ml-k-nearest-neighbors-numerical)

---

## P8: CV error vs k — pseudo table

```
SUPPOSE 5-fold CV on a dataset gives:

  k   CV error
  1   0.220
  3   0.165
  5   0.150   ← min
  7   0.158
  9   0.170
 11   0.190

Choose k = 5.  Error goes UP on both sides → classic bias-variance U-curve.
Rule of thumb (k ≈ √n) for n = 25 would also give k ≈ 5 ✓.
```

[↑ Back to Top](#-ml-k-nearest-neighbors-numerical)

---

> **Next:** [📖 THEORY](ml_knn_theory.md) · [💻 PRACTICE GUIDE](k-nn_algorithm_practice_guide_with_code.md)
>
> *ML · K-NN · github.com/rpaut03l/TS-01*
