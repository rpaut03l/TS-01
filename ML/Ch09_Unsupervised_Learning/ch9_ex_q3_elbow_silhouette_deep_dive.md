# 📊 Aurelien Geron | Ch9 Exercises - Q3: How to Choose K for K-Means 
### *Elbow Method + Silhouette Score — Theory + Code + Output Explained*

*Q3: Describe two techniques to select the right number of clusters when using K-means?*


Colab Link: https://colab.research.google.com/drive/1pEbLmXvvEG2XjJvDuK7bj3UqB_0qmrmn#scrollTo=E5DsI6v6N7H1

> **Nav:** [← Ch9 INDEX](./ml_ch9_index.md) | [📖 THEORY](./ml_ch9_theory.md) | [🔢 NUMERICAL](./ml_ch9_numerical.md) | 💻 **PRACTICE**(./ml_ch9_practice.md) | [📖 COLAB-CODE](./ml_ch9_theory.md)

---

## 🗺️ What This File Covers

```
1. WHY we need to choose K
2. TECHNIQUE 1 — Elbow Method (what it is, how to read it, the code)
3. TECHNIQUE 2 — Silhouette Score (what it is, how to read it, the code)
4. FULL RUNNABLE CODE — self-contained, paste in Colab
5. OUTPUT EXPLAINED — every number, every curve, every line on both graphs
6. WHEN THEY DISAGREE — what to do
7. GOTCHAS — mistakes to avoid in Colab
8. CHEAT SHEET + EXAM HACKS
```

---

## 1️⃣ WHY Do We Need to Choose K?

```
👶 You have a bag of mixed Lego bricks. No labels. You want to sort them into groups.
   But HOW MANY groups? 2? 5? 10?

   K-Means needs you to say the number BEFORE it starts.
   If you say a wrong number → bad groupings → useless results.

   So we try K=2, K=3, K=4 ... K=10
   For each try, we measure HOW GOOD the grouping is
   Then we pick the K with the best score.

TWO WAYS TO MEASURE "HOW GOOD":
  Method 1 — Elbow:      look at INERTIA (tightness of clusters)
  Method 2 — Silhouette: look at SEPARATION (how well-separated clusters are)
```

---

## 2️⃣ TECHNIQUE 1 — Elbow Method

### What is Inertia?

```
👶 After grouping, each point belongs to a cluster with a centre (centroid).
   Inertia = total distance² from every point to its centroid.
   LOW inertia  = points are CLOSE to their centre = TIGHT clusters = GOOD
   HIGH inertia = points are FAR from their centre = LOOSE clusters = BAD

FORMULA:  Inertia J = Σᵢ  distance²(xᵢ, its centroid)
```

### Why Inertia Always Drops With More K

```
ALWAYS: More groups → smaller groups → points closer to centre → lower inertia.
K=1:  ONE group containing everything → huge inertia
K=10: TEN groups → tiny groups → very low inertia
K=n:  Every point is its OWN cluster → inertia = 0 (useless!)

So we can't just pick "lowest inertia" → we'd always pick K = n (total points).
Instead: look for where IMPROVEMENT SLOWS DOWN = the ELBOW.
```

### Reading the Elbow Graph

```
Inertia
33000 |●                         ← K=1: one messy blob, terrible
      | \
15000 |  ●                       ← K=2: split in two, big drop
      |   \
 3500 |    ●                     ← K=3: still improving fast
      |     \
  800 |      ●─────────────────  ← K=4: ELBOW! tiny drop after this
    0 |________________________________ K
            1   2   3   4   5   6   7   8   9   10

The "elbow" = the point where the curve BENDS from steep to flat.
Before elbow: each extra group helps a LOT.
After elbow:  each extra group helps a TINY bit (not worth it).
Pick K at the elbow! → K=4 here ✅
```

### The Elbow Code — Line by Line

```python
inertias = []                              # empty bag to collect scores
for k in range(1, 11):                    # try K = 1, 2, 3 ... 10
    km = KMeans(n_clusters=k,             # "try grouping into k groups"
                n_init=10,                # try 10 random starts, keep best
                random_state=42           # same random seed = reproducible
               ).fit(X)                   # train on data X
    inertias.append(km.inertia_)          # grab inertia score, drop in bag
```

```
After loop: inertias = [33000, 15000, 3500, 800, 600, 550, 520, ...]
                         K=1    K=2    K=3   K=4  K=5  K=6  K=7
```

```python
plt.plot(range(1, 11), inertias, 'bo-')  # 'b'=blue 'o'=circle '-'=line
plt.xlabel('K (number of clusters)')
plt.ylabel('Inertia (lower = tighter clusters)')
plt.title('Elbow Method - look for the bend')
plt.xticks(range(1, 11))                  # show tick marks at 1,2,3...10
```

---

## 3️⃣ TECHNIQUE 2 — Silhouette Score

### What is Silhouette Score?

```
👶 For each point, silhouette asks TWO questions:
   Q1: "How close is this point to its OWN group?" → a(i)
   Q2: "How far is this point from the NEAREST other group?" → b(i)

   Formula: s(i) = (b - a) / max(a, b)

   PERFECT  (+1): very close to own group, very far from others ✅
   BORDER   ( 0): sitting right on the fence between two groups 😐
   WRONG    (-1): closer to another group than its own ❌

Overall silhouette = average s(i) across all points.
HIGHER = BETTER. Pick K with HIGHEST score.
```

### Reading the Silhouette Graph

```
Silhouette
 0.9 |
 0.8 |      ●  ← PEAK at K=4 (0.8336) → best K!
 0.7 |   ●     ●
 0.6 | ●           ●
 0.5 |                 ●
 0.4 |                    ●
 0.3 |                       ●  ●  ●
     |________________________________ K
          2   3   4   5   6   7   8   9   10
              |
          green dashed line drawn at K=4 by plt.axvline()

Rule: Pick the K at the PEAK. Simple!
No subjectivity. No "squinting at the curve". Just argmax.
```

### The Silhouette Code — Line by Line

```python
sil_scores = []                            # empty bag for silhouette scores
for k in range(2, 11):                    # START at 2! (k=1 crashes silhouette)
    labels = KMeans(n_clusters=k,
                    n_init=10,
                    random_state=42
                   ).fit_predict(X)        # fit + assign labels in ONE step
    #  fit_predict = fit() + predict() combined
    #  labels looks like: [0, 2, 1, 0, 0, 2, 1, ...] — one number per point
    score = silhouette_score(X, labels)   # one score for this whole K
    sil_scores.append(score)
    print(f"  K={k:2d}  silhouette={score:.4f}")
```

```
After loop:
  sil_scores = [0.6072, 0.7819, 0.8336, 0.7005, 0.5635, ...]
  positions  = [  0,      1,      2,      3,      4,    ...]
  K values   = [  2,      3,      4,      5,      6,    ...]
```

### The Best-K Line — Peeled Like an Onion 🧅

```python
best_idx   = sil_scores.index(max(sil_scores))
best_k     = range(2, 11)[best_idx]
best_score = max(sil_scores)
```

```
LAYER 1 — max(sil_scores)
  max([0.6072, 0.7819, 0.8336, 0.7005, ...]) = 0.8336
  Finds the single highest number in the list.

LAYER 2 — sil_scores.index(0.8336)
  .index() asks: "at which POSITION is 0.8336 sitting?"
  sil_scores = [0.6072, 0.7819, 0.8336, ...]
  positions  = [  0,      1,      2,    ...]
  Answer: position 2

LAYER 3 — range(2, 11)[2]
  range(2,11) = [2, 3, 4, 5, 6, 7, 8, 9, 10]
  positions  = [0, 1, 2, 3, 4, 5, 6, 7, 8 ]
  [2]        = 4   ← the K value at position 2

LAYER 4 — best_k = 4  ✅

Same thing written two other ways (all identical):
  best_k = list(range(2, 11))[sil_scores.index(max(sil_scores))]
  best_k = sil_scores.index(max(sil_scores)) + 2   # +2 because loop starts at K=2
```

### The Graph Code — Line by Line

```python
plt.subplot(1, 2, 2)                      # right chart (1 row, 2 cols, position 2)
plt.plot(range(2, 11), sil_scores, 'rs-') # 'r'=red 's'=square '-'=line
plt.axvline(                              # axvline = axis vertical line
    x=best_k,                             # draw at x=4
    color='green',
    linestyle='--',                       # dashed line
    label=f'Best K={best_k}'             # text in legend
)
plt.xlabel('K (number of clusters)')
plt.ylabel('Silhouette Score (higher = better)')
plt.title('Silhouette - pick the peak')
plt.xticks(range(2, 11))
plt.legend()                              # show the green dashed line label
```

---

## 4️⃣ FULL RUNNABLE CODE — Paste in Colab

```python
# ── CELL: fully self-contained, paste & run in Colab ─────────────
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Create demo data (replace with your own X if you have it)
X, _ = make_blobs(n_samples=500, centers=4, cluster_std=0.8, random_state=42)
# make_blobs creates fake clustered data
# n_samples=500  = 500 data points total
# centers=4      = 4 natural groups (the secret answer!)
# cluster_std    = how spread out each group is
# random_state   = reproducible results

# ── TECHNIQUE 1: Elbow Method ────────────────────────────────────
inertias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
    inertias.append(km.inertia_)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(range(1, 11), inertias, 'bo-')
plt.xlabel('K (number of clusters)')
plt.ylabel('Inertia (lower = tighter clusters)')
plt.title('Elbow Method - look for the bend')
plt.xticks(range(1, 11))

# ── TECHNIQUE 2: Silhouette Score ───────────────────────────────
sil_scores = []
for k in range(2, 11):           # k=1 is invalid for silhouette!
    labels = KMeans(n_clusters=k, n_init=10, random_state=42).fit_predict(X)
    score  = silhouette_score(X, labels)
    sil_scores.append(score)
    print(f"  K={k:2d}  silhouette={score:.4f}")

# Find best K
best_idx   = sil_scores.index(max(sil_scores))  # position of highest score
best_k     = range(2, 11)[best_idx]              # the actual K value
best_score = max(sil_scores)

print(f"\nBest K = {best_k}  (silhouette = {best_score:.4f})")

plt.subplot(1, 2, 2)
plt.plot(range(2, 11), sil_scores, 'rs-')
plt.axvline(x=best_k, color='green', linestyle='--', label=f'Best K={best_k}')
plt.xlabel('K (number of clusters)')
plt.ylabel('Silhouette Score (higher = better)')
plt.title('Silhouette - pick the peak')
plt.xticks(range(2, 11))
plt.legend()

plt.tight_layout()
plt.show()

# Memory Trick (comment only — arrow symbols crash Python if in live code!)
# S-I-L = Score, Index, Lookup
# sil_scores         = collect Scores for each K
# .index(max(...))   = find Index of the best score
# range(2,11)[index] = Lookup the actual K at that index
```

---

## 5️⃣ OUTPUT EXPLAINED — Every Number, Every Line

### Printed Numbers

```
  K= 2  silhouette=0.6072   ← ok but not great
  K= 3  silhouette=0.7819   ← getting better
  K= 4  silhouette=0.8336   ← BEST! peak here
  K= 5  silhouette=0.7005   ← dropped, too many groups
  K= 6  silhouette=0.5635   ← dropping more
  K= 7  silhouette=0.4506
  K= 8  silhouette=0.3489
  K= 9  silhouette=0.3470
  K=10  silhouette=0.3509

  Best K = 4  (silhouette = 0.8336)

WHY K=4 is the answer:
  We created data with centers=4 in make_blobs.
  The algorithm had NO IDEA. It tried all K from 2 to 10.
  It independently found K=4 produces the best clusters. ✅
  Algorithm discovered the hidden truth!

WHAT 0.8336 MEANS:
  Close to 1.0 = very clean clusters.
  Points are snug inside their own group.
  Points are far from neighbouring groups.
  Excellent result!
```

### Left Graph — Elbow

```
What you see:
  K=1 → inertia ~33,000  (one giant blob, terrible)
  K=2 → inertia ~15,000  (big drop, 2 groups is better)
  K=3 → inertia ~3,500   (still big drop)
  K=4 → inertia ~800     (another big drop)
  K=5 → inertia ~600     (small drop — slowing!)
  K=6+ → almost flat

The curve looks like a ski slope that suddenly flattens.
The bend point = elbow = K=4 here.

Blue dots  = one dot per K value
Blue line  = connects the dots
Y-axis     = inertia value (goes DOWN as K goes UP)
X-axis     = K from 1 to 10
```

### Right Graph — Silhouette

```
What you see:
  Rises from K=2 to K=4, peaks at K=4, then steadily falls.
  Green dashed vertical line drawn at K=4 (best_k).

Red squares = one per K value (range 2-10)
Red line    = connects the squares
Green dash  = plt.axvline(x=best_k) → marks the winner
Y-axis      = silhouette score (HIGHER = BETTER)
X-axis      = K from 2 to 10 (no K=1 — invalid for silhouette!)

Legend box  = shows what the green line means (f'Best K={best_k}')
```

---

## 6️⃣ WHEN ELBOW AND SILHOUETTE DISAGREE

```
Elbow says K=3, Silhouette says K=5 → which to trust?

ALWAYS trust Silhouette more. Here's why:

Elbow problems:
  ✗ Subjective — "where exactly is the bend?" is debatable
  ✗ Sometimes no clear bend exists (gradual curve, no obvious elbow)
  ✗ Only measures tightness, not separation between clusters

Silhouette advantages:
  ✓ One clear number — pick the peak, no debate
  ✓ Measures BOTH tightness (a) AND separation (b)
  ✓ Detects wrong assignments (negative scores)
  ✓ Works even when data isn't spherical

BEST PRACTICE: Run both. If they agree → high confidence.
               If they disagree → go with Silhouette.
               Always report BOTH in assignments! ✅
```

---

## 7️⃣ GOTCHAS — Mistakes to Avoid in Colab

```
GOTCHA 1: Arrow symbol → in code lines
  sil_scores    → collect Scores   ← CRASH! SyntaxError: invalid character
  Fix: put arrows only inside # comments, never on live code lines

  BROKEN: sil_scores  → collect Scores for each K
  FIXED:  # sil_scores = collect Scores for each K

GOTCHA 2: range(2, 11) silhouette starts at K=2
  silhouette_score(X, labels) with only 1 cluster crashes with ValueError.
  Silhouette needs at least 2 clusters to measure "nearest other cluster".
  ALWAYS start your silhouette loop at range(2, ...) not range(1, ...)

GOTCHA 3: range(2, 11) does NOT include 11
  range(2, 11) = [2, 3, 4, 5, 6, 7, 8, 9, 10]   ← 10 is last, NOT 11
  range(2, 10) = [2, 3, 4, 5, 6, 7, 8, 9]         ← only goes to 9!
  Rule: range(start, stop) → stop is EXCLUDED

GOTCHA 4: X must be defined before this cell runs
  This code uses X. If you haven't created X yet → NameError.
  Fix: run the make_blobs line first OR define your own X.

GOTCHA 5: n_init=10 is important
  n_init=1  → single random start → might get stuck in bad clusters
  n_init=10 → tries 10 starts, keeps best → reliable result
  Newer sklearn: n_init='auto' is the default (usually fine)
  For reproducibility: always set n_init=10 and random_state=42

GOTCHA 6: f-string needs the f!
  print("Best K = {best_k}")   → prints: Best K = {best_k}  ← WRONG
  print(f"Best K = {best_k}")  → prints: Best K = 4          ← CORRECT
  The f before the quote activates the {} substitution.

GOTCHA 7: Silhouette is slow on large data
  On 100,000+ points: use sample_size to speed it up:
  silhouette_score(X, labels, sample_size=5000, random_state=42)
```

---

## 8️⃣ CHEAT SHEET

```
┌──────────────────────────────────────────────────────────────────┐
│  METHOD          INERTIA (Elbow)        SILHOUETTE               │
├──────────────────────────────────────────────────────────────────┤
│  Range           K = 1 to max           K = 2 to max             │
│  Measure         tightness of cluster   tight + separated        │
│  Best value      LOWEST after elbow     HIGHEST across all K     │
│  How to read     find the bend          find the peak            │
│  Subjectivity    YES (debatable bend)   NO (clear max)           │
│  Trust level     Medium                 High                     │
│  sklearn call    km.inertia_            silhouette_score(X,lbl)  │
│  Score range     0 to infinity          -1 to +1                 │
│  Plot style      blue dots 'bo-'        red squares 'rs-'        │
└──────────────────────────────────────────────────────────────────┘

COLOUR CODES in the code:
  'bo-' = b(lue) o(circle marker) -(line)
  'rs-' = r(ed) s(square marker) -(line)
  axvline color='green' linestyle='--' = green dashed vertical line

KEY FORMULAS:
  Inertia:    J = Σ d²(xᵢ, μ_cluster)
  Silhouette: s(i) = (b - a) / max(a, b)
              a = mean dist to own cluster members
              b = mean dist to nearest OTHER cluster
```

---

## 🧪 EXAM HACKS

```
💡 "Silhouette of K=1?" → INVALID. Always start at K=2.
💡 "Inertia always decreases with K?" → YES. Never use it alone!
💡 "Elbow vs Silhouette — which is better?" → Silhouette. Always.
💡 "What does axvline do?" → draws a vertical line on the graph at x=best_k
💡 "Why n_init=10?" → avoids bad random initialisation, finds true optimum
💡 "Silhouette score of 0.8 means?" → very good clustering, close to 1.0
💡 "Silhouette score of 0 means?" → point is on the border between 2 clusters
💡 "Silhouette score of -1 means?" → point is in the WRONG cluster
💡 "range(2,11)[idx] vs idx+2?" → same result. range(2,11) maps index to K value.
💡 "Both methods agree?" → high confidence. Pick that K.
💡 "Arrow in code gives SyntaxError?" → Unicode arrow invalid in Python, use # comment
```

---

## 🧠 Memory Tricks

```
ELBOW:
  "Bend in the road = stop adding more lanes (clusters)"
   After the elbow, extra clusters don't improve things much.

SILHOUETTE:
  S-I-L = Score, Index, Lookup
  sil_scores         = collect Scores for each K
  .index(max(...))   = find Index of the best score
  range(2,11)[index] = Lookup the actual K at that index

RANGE GOTCHA:
  range(a, b) = a, a+1, a+2 ... b-1   (b is EXCLUDED)
  range(2,11) = 2, 3, 4, 5, 6, 7, 8, 9, 10   (NOT 11!)
```

---

> **Nav:** [← Ch9 INDEX](./ml_ch9_index.md) | [📖 THEORY](./ml_ch9_theory.md) | [🔢 NUMERICAL](./ml_ch9_numerical.md) | 💻 **PRACTICE**(./ml_ch9_practice.md)

* AI · ML · github.com/rpaut03l/TS-01*
