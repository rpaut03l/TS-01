# K-Nearest Neighbors (K-NN) Algorithm - Complete Guide

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [Core Concepts](#core-concepts)
3. [Mathematical Foundation](#mathematical-foundation)
4. [Data Representation](#data-representation)
5. [Distance Metrics](#distance-metrics)
6. [Algorithm Variants](#algorithm-variants)
7. [Implementation Guide](#implementation-guide)
8. [Visualizations & Diagrams](#visualizations--diagrams)
9. [Cheat Sheet](#cheat-sheet)
10. [Mnemonics & Memory Aids](#mnemonics--memory-aids)
11. [Practical Examples](#practical-examples)
12. [Best Practices](#best-practices)
13. [Common Pitfalls](#common-pitfalls)

---

## 🎯 Introduction

**K-Nearest Neighbors (K-NN)** is a simple, intuitive, and powerful supervised machine learning algorithm used for both **classification** and **regression** tasks.

### Key Characteristics:
- **Instance-based learning**: No explicit training phase
- **Non-parametric**: Makes no assumptions about data distribution
- **Lazy learning**: Computation happens during prediction
- **Memory-based**: Stores all training data

---

## 🧠 Core Concepts

### 1. **Distance-Based Learning**

K-NN operates on the principle: **"Similar things are close to each other"**

```
If it walks like a duck, quacks like a duck, and looks like a duck,
it's probably a duck!
```

### 2. **Feature Vector Representation**

Each data point is represented as a vector in D-dimensional space:

**Mathematical Notation:**
- **x_n** ∈ ℝ^(D×1) = feature vector (point in D-dimensional space)
- **D** = number of features/dimensions
- **N** = number of training examples

**Example:**
```
A 7×7 image → 49×1 vector of pixel intensities
```

### 3. **Training Data Structure**

**Feature Matrix (X):**
```
X = {x₁, x₂, ..., x_N}  (N × D matrix)
```
- **Rows**: Individual examples (n = 1, 2, ..., N)
- **Columns**: Features (d = 1, 2, ..., D)

**Label Vector (y):**
```
y = {y₁, y₂, ..., y_N}  (N × 1 vector)
```
- **y_n**: Label/response for the n-th example
- Can be categorical (classification) or continuous (regression)

---

## 📐 Mathematical Foundation

### Distance Metrics

Distance metrics measure similarity between data points.

#### 1. **Euclidean Distance (L₂ norm)**

**Formula:**
```
d(x_n, x_m) = ||x_n - x_m|| = √[(x_n - x_m)ᵀ(x_n - x_m)]
            = √[Σ(x_nd - x_md)²] for d=1 to D
```

**Components:**
- `||·||`: L₂ norm (Euclidean norm)
- `x_n, x_m`: Two feature vectors
- `x_nd`: d-th feature of n-th example
- `√`: Square root
- `Σ`: Summation over all D features

**Visual Representation:**
```
Point A (x₁, y₁) ──┐
                   │  Distance = √[(x₂-x₁)² + (y₂-y₁)²]
Point B (x₂, y₂) ──┘
```

#### 2. **Manhattan Distance (L₁ norm)**

**Formula:**
```
d₁(x_n, x_m) = ||x_n - x_m||₁ = Σ|x_nd - x_md| for d=1 to D
```

**When to use:** Grid-based movements, high-dimensional data

#### 3. **Inner Product Similarity**

**Formula:**
```
s(x_n, x_m) = x_nᵀ x_m = Σ(x_nd × x_md) for d=1 to D
```

**For unit vectors:**
```
s(x_n, x_m) = cos(θ)  where θ is angle between vectors
```

**Components:**
- `ᵀ`: Transpose operator
- `·`: Dot product
- Higher value → More similar

#### 4. **Mahalanobis Distance**

**Formula:**
```
d_M(x_n, x_m) = √[(x_n - x_m)ᵀ M (x_n - x_m)]
```

**Where:**
- `M`: Positive semi-definite matrix (learned from data)
- Accounts for correlations between features
- Generalizes Euclidean distance

---

## 📊 Data Representation

### Vector Space Model

Each data point exists as a point in D-dimensional space:

```
x_n ∈ ℝ^(D×1)  →  [x_n1]
                    [x_n2]
                    [ : ]
                    [x_nD]
```

### Feature Matrix Layout

```
        Feature 1  Feature 2  ...  Feature D
       ┌─────────┬──────────┬───┬──────────┐
Ex 1   │  x₁₁    │   x₁₂    │...│   x₁D    │
Ex 2   │  x₂₁    │   x₂₂    │...│   x₂D    │
  :    │   :     │    :     │...│    :     │
Ex N   │  x_N1   │   x_N2   │...│   x_ND   │
       └─────────┴──────────┴───┴──────────┘
```

### Supervised Learning Setup

**Input-Output Pairs:**
```
{(x₁, y₁), (x₂, y₂), ..., (x_N, y_N)}
```

**Types of Outputs:**
- **Classification**: y_n ∈ {class₁, class₂, ...}
- **Regression**: y_n ∈ ℝ (continuous values)

---

## 🎯 Algorithm Variants

### 1. Distance from Means Classifier

**Concept:** Classify based on distance to class centroids

**Algorithm:**
```
1. Compute mean for each class:
   μ₊ = (1/N₊) Σ x_n  (for positive class)
   μ₋ = (1/N₋) Σ x_n  (for negative class)

2. For new point x:
   Distance to μ₊: ||μ₊ - x||²
   Distance to μ₋: ||μ₋ - x||²

3. Decision rule:
   f(x) = ||μ₋ - x||² - ||μ₊ - x||²
   
   If f(x) > 0 → Positive class
   If f(x) < 0 → Negative class
```

**Expanded Form:**
```
f(x) = 2⟨μ₊ - μ₋, x⟩ + ||μ₋||² - ||μ₊||²
       └────┬────┘     └──────┬──────┘
          w (weight)      b (bias)
```

**Hyperplane Equation:**
```
w = μ₊ - μ₋  (direction normal to hyperplane)
b = ||μ₋||² - ||μ₊||²  (bias term)
```

**Key Properties:**
- Simple and efficient
- Requires sufficient training data per class
- Only learns linear decision boundaries
- Can be extended with nonlinear distance functions

### 2. 1-Nearest Neighbor (1-NN)

**Algorithm:**
```
For test point x:
1. Compute distance to all training points
2. Find nearest neighbor: x_nearest
3. Assign label of x_nearest to x
```

**Prediction Rule:**
```
ŷ = y_nearest  where  x_nearest = argmin d(x, x_n)
                                   n∈{1,...,N}
```

**Properties:**
- Most sensitive to noise/outliers
- Creates Voronoi tessellation
- Decision boundary: perpendicular bisectors between points

### 3. K-Nearest Neighbors (K-NN)

**Algorithm:**
```
For test point x:
1. Compute distances to all training points
2. Select K nearest neighbors
3. For classification: Majority vote
   For regression: Average of labels
```

**Classification Rule:**
```
ŷ = mode{y_n : x_n ∈ N_K(x)}

where N_K(x) = set of K nearest neighbors
```

**Regression Rule:**
```
ŷ = (1/K) Σ y_n  for x_n ∈ N_K(x)
```

**Choosing K:**
- **K = 1**: High variance, low bias
- **Large K**: Low variance, high bias
- **Odd K**: Avoids ties in binary classification
- **Selection method**: Cross-validation

---

## 💻 Implementation Guide

### Step-by-Step K-NN Algorithm

```python
# Pseudocode for K-NN Classification

function knn_predict(X_train, y_train, x_test, K):
    """
    Parameters:
    -----------
    X_train : array of shape (N, D) - training features
    y_train : array of shape (N,) - training labels
    x_test : array of shape (D,) - test point
    K : int - number of neighbors
    
    Returns:
    --------
    prediction : predicted class label
    """
    
    # Step 1: Compute distances
    distances = []
    for i in range(N):
        dist = euclidean_distance(x_test, X_train[i])
        distances.append((dist, y_train[i]))
    
    # Step 2: Sort by distance
    distances.sort(key=lambda x: x[0])
    
    # Step 3: Select K nearest neighbors
    k_nearest = distances[:K]
    
    # Step 4: Majority vote (classification)
    labels = [label for (_, label) in k_nearest]
    prediction = most_common(labels)
    
    return prediction
```

### Distance Calculation Functions

```python
import numpy as np

def euclidean_distance(x1, x2):
    """
    Compute Euclidean distance between two vectors
    
    Formula: d = √[Σ(x1_i - x2_i)²]
    """
    return np.sqrt(np.sum((x1 - x2) ** 2))

def manhattan_distance(x1, x2):
    """
    Compute Manhattan distance between two vectors
    
    Formula: d = Σ|x1_i - x2_i|
    """
    return np.sum(np.abs(x1 - x2))

def mahalanobis_distance(x1, x2, M):
    """
    Compute Mahalanobis distance
    
    Formula: d = √[(x1-x2)ᵀ M (x1-x2)]
    """
    diff = x1 - x2
    return np.sqrt(diff.T @ M @ diff)
```

---

## 🎨 Visualizations & Diagrams

### 1. Voronoi Tessellation (1-NN)

```
         Red Region  |  Blue Region
                    |
        ●           |        ●
    (red point)     |    (blue point)
                    |
    ────────────────┼────────────────
                    |
        ●           |        ●
                    |
```

### 2. Decision Boundaries for Different K

```
K=1: Jagged, complex boundary
┌───────────────────────┐
│ ●●  ▲▲▲    ●●   ▲▲   │
│  ●▲▲▲  ▲▲ ●  ●▲▲  ▲  │
│ ●● ▲▲▲▲  ● ●●  ▲▲▲   │
└───────────────────────┘

K=5: Smoother boundary
┌───────────────────────┐
│ ●●●●     ▲▲▲▲▲▲▲▲▲   │
│ ●●●●     ▲▲▲▲▲▲▲▲▲   │
│ ●●●●     ▲▲▲▲▲▲▲▲▲   │
└───────────────────────┘
```

### 3. Effect of K on Prediction

```
Test Point: ★

K=1:  Find 1 nearest → Class A
      ★───→ ● (A)

K=3:  Find 3 nearest → Majority vote
      ★───→ ● (A)
       ├───→ ● (A)
       └───→ ▲ (B)
      Result: Class A (2 votes)

K=5:  Find 5 nearest → Majority vote
      ★───→ ● (A)
       ├───→ ● (A)
       ├───→ ▲ (B)
       ├───→ ▲ (B)
       └───→ ▲ (B)
      Result: Class B (3 votes)
```

---

## 📝 Cheat Sheet

### Quick Reference

| Aspect | Details |
|--------|---------|
| **Type** | Supervised Learning |
| **Tasks** | Classification, Regression |
| **Training** | None (lazy learning) |
| **Prediction Time** | O(ND) per prediction |
| **Space Complexity** | O(ND) - stores all data |
| **Pros** | Simple, no assumptions, versatile |
| **Cons** | Slow prediction, memory-intensive |

### Common Parameters

| Parameter | Symbol | Typical Values | Notes |
|-----------|--------|----------------|-------|
| Number of neighbors | K | 3, 5, 7, 9 | Use odd for binary class |
| Distance metric | d(·,·) | Euclidean, Manhattan | Match to data type |
| Weights | uniform/distance | uniform | Distance-weighted for better results |

### Distance Metrics Quick Guide

| Metric | Formula | Use Case |
|--------|---------|----------|
| Euclidean | √[Σ(xᵢ-yᵢ)²] | Default, continuous features   |
| Manhattan | Σ\|xᵢ-yᵢ\| | High dimensions, grid paths      |
| Mahalanobis | √[(x-y)ᵀM(x-y)] | Correlated features       |
| Cosine | 1 - (x·y)/(||x|| ||y||) | Text, high-dimensional |

### Notation Reference

| Symbol | Meaning |
|--------|---------|
| x_n | n-th training example (feature vector) |
| y_n | Label for n-th example |
| N | Total number of training examples |
| D | Number of features/dimensions |
| K | Number of neighbors |
| d(·,·) | Distance function |
| ||·|| | Euclidean norm (L₂) |
| ||·||₁ | Manhattan norm (L₁) |
| ⟨·,·⟩ | Inner product |
| ᵀ | Transpose |
| ∈ | Element of / belongs to |
| ℝ | Real numbers |
| Σ | Summation |
| μ | Mean/centroid |

---

## 🧠 Mnemonics & Memory Aids

### K-NN Core Principle
```
"K-NN = K Nearest Neighbors"
K - Keep
N - Neighbors
N - Near
```

### Algorithm Steps (D-S-S-V)
```
D - Distance: Calculate distances to all points
S - Sort: Order by distance (ascending)
S - Select: Pick K nearest neighbors
V - Vote: Majority vote (classification) or Average (regression)
```

### Distance Metrics (E-M-C-M)
```
E - Euclidean: "As the crow flies" (straight line)
M - Manhattan: "Taxi cab" distance (grid)
C - Cosine: Angle between vectors
M - Mahalanobis: Scaled Euclidean (accounts for correlations)
```

### Choosing K
```
"K Should Be:
O - Odd (for binary classification)
D - Determined by cross-validation
D - √N is a good starting point"
```

### Bias-Variance Trade-off
```
Small K → High Variance (overfitting)
  "Small = Sensitive"

Large K → High Bias (underfitting)
  "Large = Smooth"
```

---

## 🔍 Practical Examples

### Example 1: Binary Classification

**Problem:** Classify a new point based on 2 features

**Training Data:**
```
Class A (●): (1, 2), (2, 3), (3, 3)
Class B (▲): (6, 5), (7, 7), (8, 6)
Test Point (★): (4, 4)
```

**Solution with K=3:**

1. **Calculate distances (Euclidean):**
   ```
   d(★, ●₁) = √[(4-1)² + (4-2)²] = √13 ≈ 3.61
   d(★, ●₂) = √[(4-2)² + (4-3)²] = √5 ≈ 2.24
   d(★, ●₃) = √[(4-3)² + (4-3)²] = √2 ≈ 1.41
   d(★, ▲₁) = √[(4-6)² + (4-5)²] = √5 ≈ 2.24
   d(★, ▲₂) = √[(4-7)² + (4-7)²] = √18 ≈ 4.24
   d(★, ▲₃) = √[(4-8)² + (4-6)²] = √20 ≈ 4.47
   ```

2. **Sort by distance:**
   ```
   1. ●₃ → 1.41
   2. ●₂ → 2.24
   3. ▲₁ → 2.24
   4. ●₁ → 3.61
   5. ▲₂ → 4.24
   6. ▲₃ → 4.47
   ```

3. **Select K=3 nearest:**
   ```
   ●₃, ●₂, ▲₁
   ```

4. **Majority vote:**
   ```
   Class A: 2 votes
   Class B: 1 vote
   
   Prediction: Class A (●)
   ```

### Example 2: Regression

**Problem:** Predict house price based on area

**Training Data:**
```
Area (sqft) | Price ($k)
------------|----------
1000        | 200
1200        | 240
1500        | 300
1800        | 350
2000        | 400

Test: Area = 1400 sqft, K = 3
```

**Solution:**

1. **Calculate distances:**
   ```
   |1400 - 1000| = 400
   |1400 - 1200| = 200  ← 2nd nearest
   |1400 - 1500| = 100  ← 1st nearest
   |1400 - 1800| = 400
   |1400 - 2000| = 600  ← 3rd nearest
   ```

2. **K=3 nearest neighbors:**
   ```
   1500 sqft → $300k
   1200 sqft → $240k
   2000 sqft → $400k
   ```

3. **Average:**
   ```
   Prediction = (300 + 240 + 400) / 3 = $313.33k
   ```

---

## ✅ Best Practices

### 1. Feature Scaling
```python
# Always normalize features before using K-NN
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

**Why?** Features on different scales dominate distance calculations

### 2. Choosing K

```python
# Use cross-validation
from sklearn.model_selection import cross_val_score

k_values = range(1, 31)
cv_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=5)
    cv_scores.append(scores.mean())

optimal_k = k_values[np.argmax(cv_scores)]
```

### 3. Distance Metric Selection

| Data Type | Recommended Metric |
|-----------|-------------------|
| Continuous, similar scales | Euclidean |
| Mixed scales | Mahalanobis |
| Binary/categorical | Hamming |
| Text data | Cosine |
| High dimensional | Manhattan |

### 4. Handling Imbalanced Data

```python
# Use weighted K-NN
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')
```

### 5. Optimization Techniques

**For large datasets:**
- Use KD-Trees or Ball Trees
- Apply dimensionality reduction (PCA)
- Use approximate nearest neighbor algorithms

```python
# Using KD-Tree
knn = KNeighborsClassifier(n_neighbors=5, algorithm='kd_tree')
```

---

## ⚠️ Common Pitfalls

### 1. Curse of Dimensionality

**Problem:** K-NN performance degrades in high dimensions

**Why?**
```
In high dimensions:
- All points become equidistant
- Nearest neighbors aren't actually "near"
```

**Solution:**
- Dimensionality reduction (PCA, t-SNE)
- Feature selection
- Use alternative algorithms for D > 20

### 2. No Feature Scaling

**Problem:**
```
Feature 1: [0, 1]      (normalized)
Feature 2: [0, 10000]  (not normalized)

Distance dominated by Feature 2!
```

**Solution:** Always scale features

### 3. Even K in Binary Classification

**Problem:** Ties in voting

```
K=4, Classes: A, A, B, B → Tie!
```

**Solution:** Use odd K

### 4. Outliers

**Impact:** 1-NN highly sensitive to noise

```
True pattern:  ●●●●●   ▲▲▲▲▲
Outlier:       ●●●○●   ▲▲▲▲▲
                    ↑
               Misclassifies nearby points
```

**Solutions:**
- Use larger K
- Remove outliers during preprocessing
- Use robust distance metrics

### 5. Not Considering Computational Cost

**Problem:**
```
Prediction time: O(ND) per query
Large N, D → Very slow!
```

**Solutions:**
- Use indexing structures (KD-Tree)
- Consider approximate methods
- For real-time systems, use alternative algorithms

---

## 📊 Performance Metrics

### Classification Metrics

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Accuracy
accuracy = accuracy_score(y_true, y_pred)

# Precision
precision = precision_score(y_true, y_pred, average='weighted')

# Recall
recall = recall_score(y_true, y_pred, average='weighted')

# F1-Score
f1 = f1_score(y_true, y_pred, average='weighted')
```

### Regression Metrics

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# MSE
mse = mean_squared_error(y_true, y_pred)

# MAE
mae = mean_absolute_error(y_true, y_pred)

# R² Score
r2 = r2_score(y_true, y_pred)
```

---

## 🎓 Advanced Topics

### 1. Weighted K-NN

```
Instead of equal votes, weight by inverse distance:

w_i = 1 / d(x_test, x_i)

Closer neighbors have more influence
```

### 2. Locally Weighted Learning

```
Fit local model at prediction time using nearby points
```

### 3. Adaptive K

```
Use different K values for different regions of space
Dense regions → larger K
Sparse regions → smaller K
```

---

## 📚 Additional Resources

### Key Papers
1. Cover & Hart (1967) - Original K-NN paper
2. Fix & Hodges (1951) - Nearest neighbor classification

### Libraries
```python
# scikit-learn
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

# For large scale
import faiss  # Facebook AI Similarity Search
```

### Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Training | O(1) | O(ND) |
| Prediction (brute force) | O(ND) | O(1) |
| Prediction (KD-Tree) | O(D log N) | O(ND) |
| Prediction (Ball Tree) | O(D log N) | O(ND) |

---

## 🎯 Summary

K-NN is a powerful, intuitive algorithm that:
- ✅ Requires no training phase
- ✅ Works for classification and regression
- ✅ Handles multi-class problems naturally
- ✅ Can capture complex decision boundaries
- ❌ Slow at prediction time
- ❌ Requires lots of memory
- ❌ Sensitive to irrelevant features
- ❌ Needs careful feature scaling

**Best Use Cases:**
- Small to medium datasets
- Low to moderate dimensions
- When interpretability matters
- As a baseline model

---
