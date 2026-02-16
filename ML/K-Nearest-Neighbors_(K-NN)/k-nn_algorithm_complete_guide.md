# K-Nearest Neighbors (K-NN) Algorithm - Complete Guide

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [Core Concepts](#core-concepts)
3. [Mathematical Foundation](#mathematical-foundation)
4. [Distance Metrics](#distance-metrics)
5. [Algorithm Variants](#algorithm-variants)
6. [Implementation Guide](#implementation-guide)
7. [Visualizations & Diagrams](#visualizations--diagrams)
8. [Cheat Sheet](#cheat-sheet)
9. [Practice Problems](#practice-problems)
10. [Best Practices](#best-practices)
11. [Common Pitfalls](#common-pitfalls)

---

## 🎯 Introduction

**K-Nearest Neighbors (K-NN)** is a simple, intuitive, and powerful supervised machine learning algorithm used for both **classification** and **regression** tasks.

### Key Characteristics:
- **Instance-based learning**: No explicit training phase
- **Non-parametric**: Makes no assumptions about data distribution
- **Lazy learning**: Computation happens during prediction
- **Memory-based**: Stores all training data

### Real-World Analogy:
```
Imagine you're in a new city and want to find a good restaurant.
You ask the 5 nearest people (K=5) for recommendations.
The majority vote determines where you eat!

That's exactly how K-NN works! 🎯
```

---

## 🧠 Core Concepts

### 1. **Distance-Based Learning**

K-NN operates on the principle: **"Similar things are close to each other"**

```
If it walks like a duck 🦆, quacks like a duck 🦆, and looks like a duck 🦆,
it's probably a duck! 🦆
```

### 2. **Feature Vector Representation**

Each data point is represented as a vector in D-dimensional space:

**Mathematical Notation:**
```
x_n ∈ ℝ^(D×1) = feature vector (point in D-dimensional space)
D = number of features/dimensions
N = number of training examples
```

**Example:**
```
A 7×7 grayscale image → 49×1 vector of pixel intensities
[pixel_1, pixel_2, ..., pixel_49]ᵀ
```

### 3. **Training Data Structure**

**Feature Matrix (X):**
```
        Feature_1  Feature_2  ...  Feature_D
      ┌──────────┬──────────┬───┬──────────┐
Ex_1  │   x₁₁    │   x₁₂    │...│   x₁D    │
Ex_2  │   x₂₁    │   x₂₂    │...│   x₂D    │
 :    │    :     │    :     │...│    :     │
Ex_N  │   x_N1   │   x_N2   │...│   x_ND   │
      └──────────┴──────────┴───┴──────────┘

X = N × D matrix (N examples, D features)
```

**Label Vector (y):**
```
y = [y₁, y₂, ..., y_N]ᵀ  (N × 1 vector)

Classification: y_n ∈ {Class_A, Class_B, ...}
Regression: y_n ∈ ℝ (real numbers)
```

---

## 📐 Mathematical Foundation

### Notation Reference

| Symbol | Meaning | Example |
|--------|---------|---------|
| x_n | n-th training example (vector) | x₃ = [2.1, 3.5, 1.2] |
| x_nd | d-th feature of n-th example | x₃₂ = 3.5 (2nd feature of 3rd example) |
| y_n | Label for n-th example | y₃ = "Class A" |
| N | Total number of training examples | N = 100 |
| D | Number of features/dimensions | D = 3 |
| K | Number of neighbors | K = 5 |
| d(·,·) | Distance function | d(x₁, x₂) = 2.5 |
| \\|·\\| | Euclidean norm (L₂) | \\|x\\| = √(x₁² + x₂² + ...) |
| \\|·\\|₁ | Manhattan norm (L₁) | \\|x\\|₁ = \|x₁\| + \|x₂\| + ... |
| ⟨·,·⟩ | Inner product (dot product) | ⟨x, y⟩ = x₁y₁ + x₂y₂ + ... |
| ᵀ | Transpose | [1,2,3]ᵀ = column vector |
| ∈ | Element of / belongs to | x ∈ ℝ³ |
| ℝ | Real numbers | ℝ = {..., -1.5, 0, 2.7, ...} |
| Σ | Summation | Σᵢ₌₁ⁿ xᵢ = x₁ + x₂ + ... + xₙ |
| μ | Mean/centroid | μ = (x₁ + x₂ + ... + xₙ)/n |
| argmin | Argument that minimizes | argmin f(x) = value of x where f(x) is minimum |

---

## 📏 Distance Metrics

### Distance Metrics Quick Guide

| Metric | Formula | Use Case | Range |
|--------|---------|----------|-------|
| **Euclidean** | √[Σ(xᵢ-yᵢ)²] | Default, continuous features | [0, ∞) |
| **Manhattan** | Σ\|xᵢ-yᵢ\| | High dimensions, grid paths | [0, ∞) |
| **Mahalanobis** | √[(x-y)ᵀM(x-y)] | Correlated features | [0, ∞) |
| **Cosine** | 1 - (x·y)/(\\|x\\| \\|y\\|) | Text, angles matter | [0, 2] |
| **Minkowski** | (Σ\|xᵢ-yᵢ\|ᵖ)^(1/p) | Generalization (p=1: Manhattan, p=2: Euclidean) | [0, ∞) |

### 1. **Euclidean Distance (L₂ norm)** - MOST COMMON ⭐

**Formula:**
```
d(x, y) = √[(x₁-y₁)² + (x₂-y₂)² + ... + (x_D-y_D)²]
        = √[Σ(xᵢ - yᵢ)²] for i=1 to D
```

**Visual Representation (2D):**
```
Point A (x₁, y₁) ──┐
                   │  Distance = √[(x₂-x₁)² + (y₂-y₁)²]
                   │  (straight line)
Point B (x₂, y₂) ──┘
```

**Example:**
```python
Point A = (1, 2)
Point B = (4, 6)

d = √[(4-1)² + (6-2)²]
  = √[3² + 4²]
  = √[9 + 16]
  = √25
  = 5
```

**When to use:** 
- Continuous features on similar scales
- Physical distances
- Default choice for K-NN

### 2. **Manhattan Distance (L₁ norm)** - TAXI CAB DISTANCE 🚕

**Formula:**
```
d(x, y) = |x₁-y₁| + |x₂-y₂| + ... + |x_D-y_D|
        = Σ|xᵢ - yᵢ| for i=1 to D
```

**Visual Representation (2D):**
```
Point A ────→────┐
                 │ Distance = |x₂-x₁| + |y₂-y₁|
                 ↓ (grid path, like city blocks)
Point B ─────────┘
```

**Example:**
```python
Point A = (1, 2)
Point B = (4, 6)

d = |4-1| + |6-2|
  = |3| + |4|
  = 3 + 4
  = 7
```

**When to use:**
- High-dimensional data
- Grid-based problems
- When diagonal movement isn't allowed

### 3. **Mahalanobis Distance** - SCALED EUCLIDEAN 📊

**Formula:**
```
d_M(x, y) = √[(x - y)ᵀ M (x - y)]

where M = covariance matrix (learned from data)
```

**Why use it?**
- Accounts for correlations between features
- Automatically scales features
- More robust to outliers

**Example Scenario:**
```
Height and Weight are correlated:
- Tall people usually weigh more
- Mahalanobis distance accounts for this relationship
- Euclidean distance treats them independently
```

**When to use:**
- Correlated features
- Features on different scales
- When you have enough data to estimate covariance

### 4. **Cosine Similarity** - ANGLE MEASURE 📐

**Formula:**
```
similarity(x, y) = (x · y) / (||x|| ||y||)
                 = cos(θ)

distance(x, y) = 1 - similarity(x, y)
```

**Visual:**
```
        y
        ↑
        │  ╱
        │θ╱  (angle between vectors)
        │╱
        └────→ x

Cosine similarity = cos(θ)
```

**Example:**
```python
x = [1, 2, 3]
y = [2, 4, 6]  # Same direction, different magnitude

x · y = 1×2 + 2×4 + 3×6 = 2 + 8 + 18 = 28
||x|| = √(1² + 2² + 3²) = √14 ≈ 3.74
||y|| = √(2² + 4² + 6²) = √56 ≈ 7.48

similarity = 28 / (3.74 × 7.48) ≈ 1.0  (very similar!)
```

**When to use:**
- Text data (document similarity)
- When magnitude doesn't matter, only direction
- Recommendation systems

### 5. **Minkowski Distance** - GENERAL FORM 🎛️

**Formula:**
```
d(x, y) = (Σ|xᵢ - yᵢ|ᵖ)^(1/p)

p = 1 → Manhattan distance
p = 2 → Euclidean distance
p → ∞ → Chebyshev distance (max difference)
```

**When to use:**
- Experiment with different p values
- Use cross-validation to find optimal p

---

## 🎯 Algorithm Variants

### 1. Distance from Means Classifier

**Concept:** Classify based on distance to class centroids (means)

**Step-by-Step Algorithm:**

```
Given: Training data with two classes (positive +, negative -)

Step 1: Compute mean for each class
        μ₊ = (1/N₊) Σ x_n  (average of positive class)
        μ₋ = (1/N₋) Σ x_n  (average of negative class)

Step 2: For new test point x, compute distances
        d₊ = ||x - μ₊||²  (distance to positive mean)
        d₋ = ||x - μ₋||²  (distance to negative mean)

Step 3: Decision rule
        f(x) = d₋ - d₊
        
        If f(x) > 0 → Closer to μ₊ → Predict Positive
        If f(x) < 0 → Closer to μ₋ → Predict Negative
        If f(x) = 0 → On decision boundary
```

**Expanded Form:**
```
f(x) = 2⟨μ₊ - μ₋, x⟩ + ||μ₋||² - ||μ₊||²
       └────┬────┘     └──────┬──────┘
          w (weight)      b (bias)

This is a LINEAR classifier!
Decision boundary: wx + b = 0 (hyperplane)
```

**Example:**
```python
# Training data
Class A (+): [1,1], [2,2], [3,3]  → μ₊ = [2, 2]
Class B (-): [6,6], [7,7], [8,8]  → μ₋ = [7, 7]

# Test point
x = [4, 5]

# Compute distances
d₊ = ||[4,5] - [2,2]||² = 2² + 3² = 13
d₋ = ||[4,5] - [7,7]||² = 3² + 2² = 13

# Decision: Tie! Point is on decision boundary
```

**Pros:**
- Very fast (only stores 2 points per class)
- Simple to understand

**Cons:**
- Only linear boundaries
- Sensitive to outliers
- Needs balanced classes

### 2. 1-Nearest Neighbor (1-NN)

**Algorithm:**
```
For test point x:
1. Compute distance to ALL training points
2. Find the nearest neighbor
3. Assign its label to x
```

**Mathematical Form:**
```
ŷ = y_nearest

where nearest = argmin d(x, x_n)
                n∈{1,...,N}
```

**Visual:**
```
        ●                    Test point: ★
      ●   ●
    ●   ★   ▲              Find closest: ●
      ●   ▲▲               
        ▲▲                 Prediction: Class ●
```

**Example:**
```python
Training:
A(●): (1,1), (2,2), (3,3)
B(▲): (8,8), (9,9)

Test: x = (2.5, 2.5)

Distances:
d(x, (1,1)) = √[(2.5-1)² + (2.5-1)²] = 2.12
d(x, (2,2)) = √[(2.5-2)² + (2.5-2)²] = 0.71 ← MINIMUM
d(x, (3,3)) = √[(2.5-3)² + (2.5-3)²] = 0.71 ← MINIMUM (tie)
d(x, (8,8)) = 7.78
d(x, (9,9)) = 9.19

Prediction: Class A (●) - from (2,2)
```

**Creates Voronoi Diagram:**
```
┌───────────────────────┐
│ ●●●│  Region A  │▲▲▲  │
│ ●●●│            │▲▲▲  │
├────┼────────────┼─────┤
│    │  Boundary  │     │
└────┴────────────┴─────┘
```

**Pros:**
- Most flexible decision boundary
- Can capture complex patterns

**Cons:**
- Very sensitive to noise
- Sensitive to outliers
- No smoothing

### 3. K-Nearest Neighbors (K-NN) ⭐ MAIN ALGORITHM

**Classification Algorithm:**
```
For test point x:

Step 1: Compute distances to ALL training points
        distances = [d(x, x₁), d(x, x₂), ..., d(x, x_N)]

Step 2: Sort distances in ascending order
        sorted_indices = argsort(distances)

Step 3: Select K nearest neighbors
        neighbors = sorted_indices[:K]

Step 4: MAJORITY VOTE
        labels = [y[i] for i in neighbors]
        prediction = most_common(labels)
```

**Regression Algorithm:**
```
For test point x:

Steps 1-3: Same as classification

Step 4: AVERAGE
        predictions = [y[i] for i in neighbors]
        prediction = mean(predictions)
```

**Mathematical Forms:**

**Classification:**
```
ŷ = mode{y_n : x_n ∈ N_K(x)}

where N_K(x) = set of K nearest neighbors to x
      mode = most frequent value
```

**Regression:**
```
ŷ = (1/K) Σ y_n  for x_n ∈ N_K(x)

      = average of K nearest labels
```

**Visual Example (K=5):**
```
Test point: ★

Find 5 nearest:
★───→ ● (Class A, distance=1.2)
 ├───→ ● (Class A, distance=1.5)
 ├───→ ▲ (Class B, distance=2.0)
 ├───→ ● (Class A, distance=2.3)
 └───→ ▲ (Class B, distance=2.8)

Vote count:
Class A: 3 votes ✓
Class B: 2 votes

Prediction: Class A
```

**Choosing K - THE CRITICAL DECISION:**

```
K = 1:  Most flexible, high variance (overfitting)
        ● ● ●│▲
        ● ● ●│▲ ▲  (jagged boundary)
        ──────┼──

K = 3:  Moderate flexibility
        ● ● ●│  ▲
        ● ● ●│▲ ▲  (smoother)
        ─────┼───

K = 10: Less flexible, high bias (underfitting)
        ● ● ●    ▲
        ● ● │ ▲ ▲  (very smooth)
        ────┼────
```

**Rules of Thumb for Choosing K:**
```
1. K should be ODD (for binary classification - avoids ties)
2. K = √N is a good starting point
3. Use cross-validation to find optimal K
4. Smaller K → more complex boundary
5. Larger K → smoother boundary
```

**Pros:**
- Balance between flexibility and stability
- Robust to noise (with appropriate K)
- Works for multi-class naturally

**Cons:**
- Need to choose K
- Computational cost increases with K
- Still stores all training data

---

## 💻 Implementation Guide

### Complete K-NN from Scratch

```python
import numpy as np
from collections import Counter

class KNNClassifier:
    """
    K-Nearest Neighbors Classifier
    
    Parameters:
    -----------
    k : int, default=5
        Number of neighbors to use
    distance_metric : str, default='euclidean'
        Distance metric to use ('euclidean', 'manhattan', 'cosine')
    """
    
    def __init__(self, k=5, distance_metric='euclidean'):
        self.k = k
        self.distance_metric = distance_metric
        self.X_train = None
        self.y_train = None
    
    def fit(self, X, y):
        """
        Fit the classifier (just store the data)
        
        Parameters:
        -----------
        X : array-like, shape (N, D)
            Training features
        y : array-like, shape (N,)
            Training labels
        """
        self.X_train = np.array(X)
        self.y_train = np.array(y)
        return self
    
    def _compute_distance(self, x1, x2):
        """Compute distance between two vectors"""
        if self.distance_metric == 'euclidean':
            return np.sqrt(np.sum((x1 - x2) ** 2))
        elif self.distance_metric == 'manhattan':
            return np.sum(np.abs(x1 - x2))
        elif self.distance_metric == 'cosine':
            return 1 - np.dot(x1, x2) / (np.linalg.norm(x1) * np.linalg.norm(x2))
        else:
            raise ValueError(f"Unknown distance metric: {self.distance_metric}")
    
    def predict_single(self, x):
        """
        Predict class for a single test point
        
        Parameters:
        -----------
        x : array-like, shape (D,)
            Test point
            
        Returns:
        --------
        prediction : class label
        """
        # Step 1: Compute distances to all training points
        distances = []
        for i, x_train in enumerate(self.X_train):
            dist = self._compute_distance(x, x_train)
            distances.append((dist, self.y_train[i]))
        
        # Step 2: Sort by distance
        distances.sort(key=lambda x: x[0])
        
        # Step 3: Get K nearest neighbors
        k_nearest = distances[:self.k]
        
        # Step 4: Majority vote
        k_nearest_labels = [label for (_, label) in k_nearest]
        most_common = Counter(k_nearest_labels).most_common(1)
        
        return most_common[0][0]
    
    def predict(self, X):
        """
        Predict classes for multiple test points
        
        Parameters:
        -----------
        X : array-like, shape (M, D)
            Test features
            
        Returns:
        --------
        predictions : array, shape (M,)
        """
        X = np.array(X)
        return np.array([self.predict_single(x) for x in X])
    
    def score(self, X, y):
        """Calculate accuracy"""
        predictions = self.predict(X)
        return np.mean(predictions == y)


class KNNRegressor:
    """
    K-Nearest Neighbors Regressor
    
    Parameters:
    -----------
    k : int, default=5
        Number of neighbors to use
    distance_metric : str, default='euclidean'
        Distance metric to use
    """
    
    def __init__(self, k=5, distance_metric='euclidean'):
        self.k = k
        self.distance_metric = distance_metric
        self.X_train = None
        self.y_train = None
    
    def fit(self, X, y):
        """Store training data"""
        self.X_train = np.array(X)
        self.y_train = np.array(y)
        return self
    
    def _compute_distance(self, x1, x2):
        """Compute distance between two vectors"""
        if self.distance_metric == 'euclidean':
            return np.sqrt(np.sum((x1 - x2) ** 2))
        elif self.distance_metric == 'manhattan':
            return np.sum(np.abs(x1 - x2))
        else:
            raise ValueError(f"Unknown distance metric: {self.distance_metric}")
    
    def predict_single(self, x):
        """Predict value for a single test point"""
        # Compute distances
        distances = []
        for i, x_train in enumerate(self.X_train):
            dist = self._compute_distance(x, x_train)
            distances.append((dist, self.y_train[i]))
        
        # Sort and get K nearest
        distances.sort(key=lambda x: x[0])
        k_nearest = distances[:self.k]
        
        # Average of K nearest labels
        k_nearest_values = [value for (_, value) in k_nearest]
        return np.mean(k_nearest_values)
    
    def predict(self, X):
        """Predict values for multiple test points"""
        X = np.array(X)
        return np.array([self.predict_single(x) for x in X])


# Example usage
if __name__ == "__main__":
    # Classification example
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    
    # Generate data
    X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, 
                                n_informative=2, random_state=42, n_clusters_per_class=1)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train K-NN
    knn = KNNClassifier(k=5, distance_metric='euclidean')
    knn.fit(X_train, y_train)
    
    # Predict
    accuracy = knn.score(X_test, y_test)
    print(f"Accuracy: {accuracy:.2f}")
```

### Using scikit-learn (Recommended for Production)

```python
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, GridSearchCV
import numpy as np

# Example: Classification
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# IMPORTANT: Always scale features!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train K-NN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Predict
y_pred = knn.predict(X_test_scaled)
accuracy = knn.score(X_test_scaled, y_test)
print(f"Accuracy: {accuracy:.2f}")

# Find optimal K using cross-validation
k_values = range(1, 31)
cv_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train_scaled, y_train, cv=5, scoring='accuracy')
    cv_scores.append(scores.mean())

# Best K
optimal_k = k_values[np.argmax(cv_scores)]
print(f"Optimal K: {optimal_k}")

# Or use GridSearchCV
param_grid = {
    'n_neighbors': range(1, 31),
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan']
}

grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train_scaled, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.2f}")
```

---

## 🎨 Visualizations & Diagrams

### 1. K-NN Decision Boundaries (Effect of K)

```
K=1: Very complex, overfitting
┌────────────────────────────┐
│ ●●●│  ▲▲▲    ●●●│  ▲▲▲    │
│ ●●●│▲▲▲      ●●●│▲▲▲      │
│────┼─────────────┼─────────│
│    │  Jagged     │         │
└────┴─────────────┴─────────┘

K=5: Balanced
┌────────────────────────────┐
│ ●●●●●  ▲▲▲▲▲   ●●●●  ▲▲▲  │
│ ●●●●●  ▲▲▲▲▲   ●●●●  ▲▲▲  │
│───────┼────────────────────│
│       │  Smooth            │
└───────┴────────────────────┘

K=20: Very smooth, underfitting
┌────────────────────────────┐
│ ●●●●●●●●●●  ▲▲▲▲▲▲▲▲▲▲▲   │
│ ●●●●●●●●●●  ▲▲▲▲▲▲▲▲▲▲▲   │
│────────────┼───────────────│
│            │ Too simple    │
└────────────┴───────────────┘
```

### 2. Distance Metrics Comparison

```python
import matplotlib.pyplot as plt
import numpy as np

# Create points
A = np.array([0, 0])
B = np.array([3, 4])

# Euclidean: straight line
euclidean = np.sqrt(np.sum((B - A) ** 2))
print(f"Euclidean: {euclidean}")  # 5.0

# Manhattan: grid path
manhattan = np.sum(np.abs(B - A))
print(f"Manhattan: {manhattan}")  # 7.0

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Euclidean
ax1.plot([A[0], B[0]], [A[1], B[1]], 'r-', linewidth=2, label='Euclidean')
ax1.plot([A[0]], [A[1]], 'bo', markersize=10, label='Point A')
ax1.plot([B[0]], [B[1]], 'go', markersize=10, label='Point B')
ax1.set_title('Euclidean Distance (Straight Line)')
ax1.grid(True)
ax1.legend()
ax1.set_xlabel('x')
ax1.set_ylabel('y')

# Manhattan
ax2.plot([A[0], B[0]], [A[1], A[1]], 'b-', linewidth=2)
ax2.plot([B[0], B[0]], [A[1], B[1]], 'b-', linewidth=2, label='Manhattan')
ax2.plot([A[0]], [A[1]], 'bo', markersize=10, label='Point A')
ax2.plot([B[0]], [B[1]], 'go', markersize=10, label='Point B')
ax2.set_title('Manhattan Distance (Grid Path)')
ax2.grid(True)
ax2.legend()
ax2.set_xlabel('x')
ax2.set_ylabel('y')

plt.tight_layout()
plt.show()
```

### 3. Voronoi Diagram (1-NN)

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d

# Training points
points = np.array([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]])
labels = ['A', 'A', 'B', 'B', 'A']

# Create Voronoi diagram
vor = Voronoi(points)

# Plot
fig, ax = plt.subplots(figsize=(8, 8))
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='black', line_width=2)

# Add points
colors = {'A': 'red', 'B': 'blue'}
for i, (point, label) in enumerate(zip(points, labels)):
    ax.plot(point[0], point[1], 'o', color=colors[label], markersize=15, 
            markeredgecolor='black', markeredgewidth=2)
    ax.text(point[0], point[1]+0.2, label, ha='center', fontsize=12, fontweight='bold')

ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_title('Voronoi Diagram for 1-NN', fontsize=16)
ax.set_xlabel('Feature 1', fontsize=12)
ax.set_ylabel('Feature 2', fontsize=12)
ax.grid(True, alpha=0.3)
plt.show()
```

### 4. K-NN Regression Visualization

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Generate data
np.random.seed(42)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])

# Create test points
X_test = np.linspace(0, 5, 500)[:, np.newaxis]

# Different K values
k_values = [1, 3, 10, 20]

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
axes = axes.ravel()

for idx, k in enumerate(k_values):
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X, y)
    y_pred = knn.predict(X_test)
    
    axes[idx].scatter(X, y, color='black', s=50, alpha=0.5, label='Training data')
    axes[idx].plot(X_test, y_pred, color='red', linewidth=2, label=f'K={k} prediction')
    axes[idx].plot(X_test, np.sin(X_test), color='blue', linewidth=2, 
                   linestyle='--', label='True function')
    axes[idx].set_title(f'K-NN Regression (K={k})', fontsize=14)
    axes[idx].set_xlabel('X', fontsize=12)
    axes[idx].set_ylabel('y', fontsize=12)
    axes[idx].legend()
    axes[idx].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## 📝 Cheat Sheet

### Quick Reference Card

```
╔════════════════════════════════════════════════════════════╗
║              K-NN ALGORITHM CHEAT SHEET                    ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  ALGORITHM TYPE:  Supervised, Instance-based, Lazy        ║
║  TASKS:           Classification, Regression               ║
║  TIME COMPLEXITY: O(ND) per prediction                    ║
║  SPACE COMPLEXITY: O(ND) storage                          ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║  PREDICTION RULE:                                          ║
║  ┌──────────────────────────────────────────────────────┐ ║
║  │ 1. Compute distances to ALL training points         │ ║
║  │ 2. Sort by distance (ascending)                      │ ║
║  │ 3. Select K nearest neighbors                        │ ║
║  │ 4. Classification: MAJORITY VOTE                     │ ║
║  │    Regression: AVERAGE                               │ ║
║  └──────────────────────────────────────────────────────┘ ║
╠════════════════════════════════════════════════════════════╣
║  DISTANCE METRICS:                                         ║
║  • Euclidean:    √[Σ(xᵢ-yᵢ)²]      → Default             ║
║  • Manhattan:    Σ|xᵢ-yᵢ|          → High-D              ║
║  • Mahalanobis:  √[(x-y)ᵀM(x-y)]   → Correlated          ║
║  • Cosine:       1-(x·y)/(||x||||y||) → Text             ║
╠════════════════════════════════════════════════════════════╣
║  CHOOSING K:                                               ║
║  ✓ Use ODD numbers (binary classification)                ║
║  ✓ K = √N is a good starting point                        ║
║  ✓ Use cross-validation for optimal K                     ║
║  ✓ Small K → Complex boundary (overfitting)               ║
║  ✓ Large K → Simple boundary (underfitting)               ║
╠════════════════════════════════════════════════════════════╣
║  PREPROCESSING (CRITICAL!):                                ║
║  1. Scale features: StandardScaler or MinMaxScaler        ║
║  2. Handle missing values                                  ║
║  3. Remove outliers (optional)                             ║
║  4. Feature selection (optional)                           ║
╠════════════════════════════════════════════════════════════╣
║  PROS (+):                                                 ║
║  • Simple and intuitive                                    ║
║  • No training phase                                       ║
║  • Works with any number of classes                        ║
║  • No assumptions about data                               ║
╠════════════════════════════════════════════════════════════╣
║  CONS (-):                                                 ║
║  • Slow prediction (O(ND))                                 ║
║  • High memory usage                                       ║
║  • Sensitive to irrelevant features                        ║
║  • Curse of dimensionality                                 ║
╚════════════════════════════════════════════════════════════╝
```

### Scikit-learn Quick Reference

```python
# Import
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

# Preprocessing
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Classification
knn_clf = KNeighborsClassifier(
    n_neighbors=5,           # K value
    weights='uniform',       # 'uniform' or 'distance'
    algorithm='auto',        # 'auto', 'ball_tree', 'kd_tree', 'brute'
    metric='euclidean'       # distance metric
)
knn_clf.fit(X_train_scaled, y_train)
y_pred = knn_clf.predict(X_test_scaled)

# Regression
knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_train_scaled, y_train)
y_pred = knn_reg.predict(X_test_scaled)

# Cross-validation
scores = cross_val_score(knn_clf, X_train_scaled, y_train, cv=5)
print(f"CV Score: {scores.mean():.2f} (+/- {scores.std():.2f})")
```

---

## 🎯 Practice Problems

### Problem 1: Basic K-NN Classification (Easy) 🟢

**Scenario:** You're building a fruit classifier based on weight and color intensity.

**Given Training Data:**
```
Fruit    Weight(g)  Color(0-10)  Label
─────────────────────────────────────
Apple    150        7            A
Apple    160        8            A
Apple    145        7            A
Orange   140        9            O
Orange   135        10           O
Orange   142        9            O
Banana   120        3            B
Banana   118        2            B
Banana   125        3            B
```

**Test Cases:**
```
Test 1: Weight=155g, Color=7.5
Test 2: Weight=138g, Color=9
Test 3: Weight=122g, Color=2.5
```

**Tasks:**
1. Use K=3 with Euclidean distance
2. Manually calculate distances for Test 1
3. Predict the class for all test cases
4. What happens if K=1? K=5?

**Solution:**

<details>
<summary>Click to reveal solution</summary>

```python
import numpy as np
from collections import Counter

# Training data
X_train = np.array([
    [150, 7],   # Apple
    [160, 8],   # Apple
    [145, 7],   # Apple
    [140, 9],   # Orange
    [135, 10],  # Orange
    [142, 9],   # Orange
    [120, 3],   # Banana
    [118, 2],   # Banana
    [125, 3]    # Banana
])

y_train = np.array(['A', 'A', 'A', 'O', 'O', 'O', 'B', 'B', 'B'])

# Test cases
X_test = np.array([
    [155, 7.5],
    [138, 9],
    [122, 2.5]
])

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def knn_predict(X_train, y_train, x_test, k=3):
    # Calculate distances
    distances = []
    for i, x_train in enumerate(X_train):
        dist = euclidean_distance(x_test, x_train)
        distances.append((dist, y_train[i]))
    
    # Sort and get k nearest
    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]
    
    # Majority vote
    labels = [label for (_, label) in k_nearest]
    prediction = Counter(labels).most_common(1)[0][0]
    
    return prediction, k_nearest

# Manual calculation for Test 1: [155, 7.5]
print("=" * 60)
print("MANUAL CALCULATION FOR TEST 1: [155, 7.5]")
print("=" * 60)

test1 = X_test[0]
print(f"\nTest point: Weight={test1[0]}g, Color={test1[1]}")
print("\nDistances to training points:")

for i, (x, y) in enumerate(zip(X_train, y_train)):
    dist = euclidean_distance(test1, x)
    print(f"{y} [{x[0]}, {x[1]}]: d = √[(155-{x[0]})² + (7.5-{x[1]})²] = {dist:.2f}")

# Predictions for all test cases
print("\n" + "=" * 60)
print("PREDICTIONS (K=3)")
print("=" * 60)

for i, test in enumerate(X_test):
    prediction, neighbors = knn_predict(X_train, y_train, test, k=3)
    print(f"\nTest {i+1}: {test}")
    print(f"  3 Nearest neighbors:")
    for dist, label in neighbors:
        print(f"    {label} (distance={dist:.2f})")
    print(f"  Prediction: {prediction}")

# Try different K values
print("\n" + "=" * 60)
print("EFFECT OF DIFFERENT K VALUES (Test 1)")
print("=" * 60)

for k in [1, 3, 5, 7]:
    prediction, _ = knn_predict(X_train, y_train, X_test[0], k=k)
    print(f"K={k}: {prediction}")
```

**Expected Output:**
```
Test 1: [155, 7.5] → Apple (A)
Test 2: [138, 9] → Orange (O)
Test 3: [122, 2.5] → Banana (B)
```

**Key Insights:**
- Feature scaling is important! Weight (100-160) has larger scale than Color (0-10)
- K=1 would be more sensitive to individual points
- K=5 would smooth out the decision
</details>

---

### Problem 2: K-NN Regression (Medium) 🟡

**Scenario:** Predict house prices based on area and number of rooms.

**Given Training Data:**
```
Area(sqft)  Rooms  Price($k)
───────────────────────────
1000        2      200
1200        2      240
1500        3      300
1800        3      350
2000        4      400
2200        4      440
2500        5      500
1100        2      220
1600        3      320
1900        3      370
```

**Test Cases:**
```
Test 1: Area=1400 sqft, Rooms=3
Test 2: Area=2100 sqft, Rooms=4
```

**Tasks:**
1. Implement K-NN regression with K=3
2. IMPORTANT: Scale features first!
3. Predict prices for test cases
4. Compare results with K=1, 3, 5, 7
5. Calculate MAE (Mean Absolute Error)

**Solution:**

<details>
<summary>Click to reveal solution</summary>

```python
import numpy as np
from sklearn.preprocessing import StandardScaler

# Training data
X_train = np.array([
    [1000, 2],
    [1200, 2],
    [1500, 3],
    [1800, 3],
    [2000, 4],
    [2200, 4],
    [2500, 5],
    [1100, 2],
    [1600, 3],
    [1900, 3]
])

y_train = np.array([200, 240, 300, 350, 400, 440, 500, 220, 320, 370])

# Test cases
X_test = np.array([
    [1400, 3],
    [2100, 4]
])

# CRITICAL: Scale features!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("=" * 60)
print("FEATURE SCALING")
print("=" * 60)
print("\nOriginal Test 1:", X_test[0])
print("Scaled Test 1:", X_test_scaled[0])
print("\nWhy? Area and Rooms have different scales!")
print("Area: 1000-2500, Rooms: 2-5")

def knn_regression(X_train, y_train, x_test, k=3):
    # Calculate distances
    distances = []
    for i, x_train in enumerate(X_train):
        dist = np.sqrt(np.sum((x_test - x_train) ** 2))
        distances.append((dist, y_train[i]))
    
    # Sort and get k nearest
    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]
    
    # Average of k nearest values
    values = [value for (_, value) in k_nearest]
    prediction = np.mean(values)
    
    return prediction, k_nearest

# Predictions for different K
print("\n" + "=" * 60)
print("PREDICTIONS FOR TEST 1: [1400 sqft, 3 rooms]")
print("=" * 60)

k_values = [1, 3, 5, 7]
predictions = {}

for k in k_values:
    pred, neighbors = knn_regression(X_train_scaled, y_train, X_test_scaled[0], k=k)
    predictions[k] = pred
    
    print(f"\nK = {k}:")
    print(f"  Nearest neighbors:")
    for dist, price in neighbors:
        print(f"    ${price}k (distance={dist:.3f})")
    print(f"  Average = ${pred:.2f}k")

# Detailed breakdown for K=3
print("\n" + "=" * 60)
print("DETAILED CALCULATION (K=3)")
print("=" * 60)

pred, neighbors = knn_regression(X_train_scaled, y_train, X_test_scaled[0], k=3)
values = [price for (_, price) in neighbors]

print(f"\n3 nearest neighbors: {values}")
print(f"Average: ({values[0]} + {values[1]} + {values[2]}) / 3")
print(f"       = {sum(values)} / 3")
print(f"       = ${pred:.2f}k")

# Predictions for both test cases
print("\n" + "=" * 60)
print("FINAL PREDICTIONS (K=3)")
print("=" * 60)

for i, (test_original, test_scaled) in enumerate(zip(X_test, X_test_scaled)):
    pred, _ = knn_regression(X_train_scaled, y_train, test_scaled, k=3)
    print(f"\nTest {i+1}: {test_original[0]} sqft, {test_original[1]} rooms")
    print(f"  Predicted Price: ${pred:.2f}k")

# Visualization of predictions
print("\n" + "=" * 60)
print("EFFECT OF K ON PREDICTIONS (Test 1)")
print("=" * 60)

import matplotlib.pyplot as plt

k_vals = list(predictions.keys())
pred_vals = list(predictions.values())

plt.figure(figsize=(10, 6))
plt.plot(k_vals, pred_vals, 'bo-', linewidth=2, markersize=10)
plt.xlabel('K (number of neighbors)', fontsize=12)
plt.ylabel('Predicted Price ($k)', fontsize=12)
plt.title('Effect of K on Price Prediction', fontsize=14)
plt.grid(True, alpha=0.3)
plt.xticks(k_vals)
for k, pred in zip(k_vals, pred_vals):
    plt.text(k, pred + 5, f'${pred:.0f}k', ha='center', fontsize=10)
plt.show()
```

**Expected Output:**
```
Test 1: [1400 sqft, 3 rooms] → ~$295k (K=3)
Test 2: [2100 sqft, 4 rooms] → ~$420k (K=3)
```

**Key Insights:**
- Feature scaling is CRITICAL! Without it, Area dominates
- Larger K → smoother predictions
- Smaller K → more sensitive to individual points
</details>

---

### Problem 3: Optimal K Selection with Cross-Validation (Hard) 🔴

**Scenario:** Build a customer churn predictor and find the optimal K.

**Dataset:** Customer data with features: Age, Income, Tenure, Support Calls

**Tasks:**
1. Load and preprocess data
2. Implement k-fold cross-validation
3. Test K values from 1 to 30
4. Find optimal K that maximizes accuracy
5. Analyze bias-variance trade-off
6. Compare different distance metrics

**Solution:**

<details>
<summary>Click to reveal solution</summary>

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

# Generate synthetic customer churn data
np.random.seed(42)
X, y = make_classification(
    n_samples=500,
    n_features=4,  # Age, Income, Tenure, Support Calls
    n_informative=3,
    n_redundant=1,
    n_classes=2,  # Churned / Not Churned
    random_state=42
)

# Feature names for interpretation
feature_names = ['Age', 'Income', 'Tenure', 'Support_Calls']
class_names = ['Not Churned', 'Churned']

print("=" * 60)
print("CUSTOMER CHURN PREDICTION - OPTIMAL K SELECTION")
print("=" * 60)
print(f"\nDataset: {X.shape[0]} customers, {X.shape[1]} features")
print(f"Features: {feature_names}")
print(f"Classes: {class_names}")
print(f"Class distribution: {np.bincount(y)}")

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n" + "=" * 60)
print("STEP 1: TEST DIFFERENT K VALUES (1-30)")
print("=" * 60)

k_values = range(1, 31)
cv_scores_mean = []
cv_scores_std = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_scaled, y, cv=5, scoring='accuracy')
    cv_scores_mean.append(scores.mean())
    cv_scores_std.append(scores.std())
    
    if k % 5 == 1:  # Print every 5th value
        print(f"K={k:2d}: Accuracy = {scores.mean():.4f} (+/- {scores.std():.4f})")

# Find optimal K
optimal_k = k_values[np.argmax(cv_scores_mean)]
optimal_score = max(cv_scores_mean)

print(f"\n{'='*60}")
print(f"OPTIMAL K: {optimal_k}")
print(f"Best CV Accuracy: {optimal_score:.4f}")
print(f"{'='*60}")

# Plot K vs Accuracy
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(k_values, cv_scores_mean, 'b-', linewidth=2, label='CV Accuracy')
plt.fill_between(k_values, 
                 np.array(cv_scores_mean) - np.array(cv_scores_std),
                 np.array(cv_scores_mean) + np.array(cv_scores_std),
                 alpha=0.2)
plt.axvline(optimal_k, color='r', linestyle='--', linewidth=2, label=f'Optimal K={optimal_k}')
plt.xlabel('K (Number of Neighbors)', fontsize=12)
plt.ylabel('Cross-Validation Accuracy', fontsize=12)
plt.title('K vs Accuracy (with standard deviation)', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

# Plot bias-variance trade-off
plt.subplot(1, 2, 2)
# Approximate bias and variance
bias = [1/k for k in k_values]  # Simplified: bias decreases with K
variance = [k/30 for k in k_values]  # Simplified: variance increases with K
total_error = np.array(bias) + np.array(variance)

plt.plot(k_values, bias, 'r-', linewidth=2, label='Bias (simplified)')
plt.plot(k_values, variance, 'b-', linewidth=2, label='Variance (simplified)')
plt.plot(k_values, total_error, 'g-', linewidth=2, label='Total Error')
plt.axvline(optimal_k, color='orange', linestyle='--', linewidth=2, 
            label=f'Optimal K={optimal_k}')
plt.xlabel('K (Number of Neighbors)', fontsize=12)
plt.ylabel('Error', fontsize=12)
plt.title('Bias-Variance Trade-off', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Compare different distance metrics
print("\n" + "=" * 60)
print("STEP 2: COMPARE DISTANCE METRICS (K=optimal)")
print("=" * 60)

metrics = ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
metric_scores = {}

for metric in metrics:
    knn = KNeighborsClassifier(n_neighbors=optimal_k, metric=metric)
    scores = cross_val_score(knn, X_scaled, y, cv=5, scoring='accuracy')
    metric_scores[metric] = scores.mean()
    print(f"{metric:12s}: {scores.mean():.4f} (+/- {scores.std():.4f})")

best_metric = max(metric_scores, key=metric_scores.get)
print(f"\nBest metric: {best_metric} ({metric_scores[best_metric]:.4f})")

# Plot metric comparison
plt.figure(figsize=(10, 6))
metrics_list = list(metric_scores.keys())
scores_list = list(metric_scores.values())

plt.barh(metrics_list, scores_list, color='steelblue', edgecolor='black')
plt.xlabel('Cross-Validation Accuracy', fontsize=12)
plt.ylabel('Distance Metric', fontsize=12)
plt.title(f'Distance Metric Comparison (K={optimal_k})', fontsize=14)
plt.xlim([min(scores_list) - 0.01, max(scores_list) + 0.01])

for i, (metric, score) in enumerate(zip(metrics_list, scores_list)):
    plt.text(score + 0.001, i, f'{score:.4f}', va='center', fontsize=10)

plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.show()

# Weighted vs Uniform
print("\n" + "=" * 60)
print("STEP 3: WEIGHTED vs UNIFORM (K=optimal)")
print("=" * 60)

for weights in ['uniform', 'distance']:
    knn = KNeighborsClassifier(n_neighbors=optimal_k, weights=weights)
    scores = cross_val_score(knn, X_scaled, y, cv=5, scoring='accuracy')
    print(f"{weights:8s}: {scores.mean():.4f} (+/- {scores.std():.4f})")

# Final model with best parameters
print("\n" + "=" * 60)
print("FINAL MODEL")
print("=" * 60)

final_knn = KNeighborsClassifier(
    n_neighbors=optimal_k,
    metric=best_metric,
    weights='distance'  # Usually better
)

final_scores = cross_val_score(final_knn, X_scaled, y, cv=5, scoring='accuracy')
print(f"\nFinal Model Configuration:")
print(f"  K: {optimal_k}")
print(f"  Metric: {best_metric}")
print(f"  Weights: distance")
print(f"\nFinal CV Accuracy: {final_scores.mean():.4f} (+/- {final_scores.std():.4f})")

# Learning curve
print("\n" + "=" * 60)
print("STEP 4: LEARNING CURVE")
print("=" * 60)

from sklearn.model_selection import learning_curve

train_sizes, train_scores, val_scores = learning_curve(
    final_knn, X_scaled, y, cv=5, n_jobs=-1,
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='accuracy'
)

train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
val_mean = np.mean(val_scores, axis=1)
val_std = np.std(val_scores, axis=1)

plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, 'o-', color='r', linewidth=2, label='Training score')
plt.plot(train_sizes, val_mean, 'o-', color='g', linewidth=2, label='Validation score')

plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1, color='r')
plt.fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.1, color='g')

plt.xlabel('Training Set Size', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.title('Learning Curve', fontsize=14)
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nInterpretation:")
print("- If training score >> validation score → Overfitting")
print("- If both converge at high value → Good!")
print("- If both converge at low value → Underfitting (need better features)")
```

**Key Insights:**
- Cross-validation prevents overfitting to training data
- Optimal K balances bias and variance
- Different metrics may work better for different datasets
- Distance-weighted voting often improves performance
- Learning curves help diagnose over/underfitting
</details>

---

### Problem 4: Multi-Class Classification with Imbalanced Data (Expert) 🔴

**Scenario:** Classify iris flowers (3 classes) with imbalanced dataset.

**Challenges:**
1. Imbalanced classes (Class A: 100, Class B: 50, Class C: 20)
2. Different feature scales
3. Outliers present
4. Need to optimize for F1-score, not accuracy

**Tasks:**
1. Handle class imbalance
2. Try different K values
3. Use weighted K-NN
4. Evaluate with appropriate metrics
5. Visualize decision boundaries

**Solution:**

<details>
<summary>Click to reveal solution</summary>

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.utils import resample
import seaborn as sns

# Load iris dataset
iris = load_iris()
X = iris.data[:, :2]  # Use only 2 features for visualization
y = iris.target

# Create imbalanced dataset
np.random.seed(42)

# Sample to create imbalance
idx_0 = np.where(y == 0)[0]
idx_1 = np.where(y == 1)[0]
idx_2 = np.where(y == 2)[0]

# Resample to create imbalance (100:50:20)
idx_0_sample = resample(idx_0, n_samples=100, random_state=42)
idx_1_sample = resample(idx_1, n_samples=50, random_state=42)
idx_2_sample = resample(idx_2, n_samples=20, random_state=42)

idx_imbalanced = np.concatenate([idx_0_sample, idx_1_sample, idx_2_sample])
X_imbalanced = X[idx_imbalanced]
y_imbalanced = y[idx_imbalanced]

print("=" * 60)
print("MULTI-CLASS CLASSIFICATION WITH IMBALANCED DATA")
print("=" * 60)
print(f"\nClass distribution:")
for i, count in enumerate(np.bincount(y_imbalanced)):
    print(f"  Class {i} ({iris.target_names[i]}): {count} samples")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_imbalanced, y_imbalanced, test_size=0.3, random_state=42, stratify=y_imbalanced
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Compare uniform vs weighted K-NN
print("\n" + "=" * 60)
print("STEP 1: UNIFORM vs DISTANCE-WEIGHTED K-NN")
print("=" * 60)

k_values = [3, 5, 7, 9, 11]
results = {'uniform': [], 'distance': []}

for k in k_values:
    for weights in ['uniform', 'distance']:
        knn = KNeighborsClassifier(n_neighbors=k, weights=weights)
        knn.fit(X_train_scaled, y_train)
        f1 = f1_score(y_test, knn.predict(X_test_scaled), average='weighted')
        results[weights].append(f1)

# Plot comparison
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(k_values, results['uniform'], 'bo-', linewidth=2, markersize=8, label='Uniform')
plt.plot(k_values, results['distance'], 'ro-', linewidth=2, markersize=8, label='Distance-weighted')
plt.xlabel('K (Number of Neighbors)', fontsize=12)
plt.ylabel('F1-Score (weighted)', fontsize=12)
plt.title('Uniform vs Distance-Weighted K-NN', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

# Find optimal K for weighted
optimal_k = k_values[np.argmax(results['distance'])]
print(f"\nOptimal K (distance-weighted): {optimal_k}")
print(f"Best F1-Score: {max(results['distance']):.4f}")

# Train final model
final_knn = KNeighborsClassifier(n_neighbors=optimal_k, weights='distance')
final_knn.fit(X_train_scaled, y_train)
y_pred = final_knn.predict(X_test_scaled)

# Confusion matrix
print("\n" + "=" * 60)
print("STEP 2: CONFUSION MATRIX")
print("=" * 60)

cm = confusion_matrix(y_test, y_pred)
print("\n" + classification_report(y_test, y_pred, target_names=iris.target_names))

plt.subplot(1, 2, 2)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=iris.target_names, 
            yticklabels=iris.target_names,
            cbar_kws={'label': 'Count'})
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.title('Confusion Matrix', fontsize=14)

plt.tight_layout()
plt.show()

# Visualize decision boundaries
print("\n" + "=" * 60)
print("STEP 3: DECISION BOUNDARY VISUALIZATION")
print("=" * 60)

def plot_decision_boundary(X, y, model, title):
    h = 0.02  # Step size
    
    # Create mesh
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    # Predict on mesh
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # Plot
    plt.figure(figsize=(10, 8))
    plt.contourf(xx, yy, Z, alpha=0.4, cmap='RdYlBu')
    
    # Plot training points
    scatter = plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdYlBu', 
                         edgecolors='black', linewidth=1.5)
    
    plt.xlabel(iris.feature_names[0], fontsize=12)
    plt.ylabel(iris.feature_names[1], fontsize=12)
    plt.title(title, fontsize=14)
    
    # Add legend
    handles, labels = scatter.legend_elements()
    plt.legend(handles, iris.target_names, loc='upper right')
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# Plot for different K values
for k in [1, 5, 15]:
    knn = KNeighborsClassifier(n_neighbors=k, weights='distance')
    knn.fit(X_train_scaled, y_train)
    plot_decision_boundary(X_train_scaled, y_train, knn, 
                          f'Decision Boundary (K={k}, Distance-weighted)')

# Class-wise performance analysis
print("\n" + "=" * 60)
print("STEP 4: CLASS-WISE PERFORMANCE")
print("=" * 60)

from sklearn.metrics import precision_score, recall_score, f1_score

for i, class_name in enumerate(iris.target_names):
    y_true_binary = (y_test == i).astype(int)
    y_pred_binary = (y_pred == i).astype(int)
    
    precision = precision_score(y_true_binary, y_pred_binary)
    recall = recall_score(y_true_binary, y_pred_binary)
    f1 = f1_score(y_true_binary, y_pred_binary)
    
    print(f"\n{class_name}:")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall:    {recall:.4f}")
    print(f"  F1-Score:  {f1:.4f}")

# Recommendations for handling imbalanced data
print("\n" + "=" * 60)
print("RECOMMENDATIONS FOR IMBALANCED DATA")
print("=" * 60)
print("""
1. Use distance-weighted voting (weights='distance')
2. Evaluate with F1-score, not accuracy
3. Use stratified sampling for train/test split
4. Consider oversampling minority class (SMOTE)
5. Consider undersampling majority class
6. Use appropriate metrics for each class
7. Adjust classification threshold if needed
""")
```

**Key Takeaways:**
- Imbalanced data needs special handling
- Distance-weighted K-NN helps with imbalance
- F1-score is better than accuracy for imbalanced data
- Visualize decision boundaries to understand behavior
- Analyze per-class performance separately
</details>

---

## ✅ Best Practices

### 1. Always Scale Your Features! ⚠️

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# StandardScaler: mean=0, std=1 (preferred for K-NN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# MinMaxScaler: scale to [0, 1]
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ⚠️ NEVER do this:
# X_test_scaled = scaler.fit_transform(X_test)  # WRONG!
# This leaks information from test set!
```

**Why is scaling critical?**
```
Without scaling:
Feature 1: Age (20-60) → range = 40
Feature 2: Income (20000-100000) → range = 80000

Distance dominated by Income!
Age contribution ≈ 0%
Income contribution ≈ 100%

With scaling:
Feature 1: Age (-1.5 to 1.5) → range = 3
Feature 2: Income (-1.5 to 1.5) → range = 3

Fair contribution from both features!
```

### 2. Choose K Wisely

```python
# Rule of thumb: K = √N
import numpy as np
N = len(X_train)
k_suggested = int(np.sqrt(N))

# Make it odd (for binary classification)
if k_suggested % 2 == 0:
    k_suggested += 1

print(f"Suggested K: {k_suggested}")

# But always use cross-validation!
from sklearn.model_selection import cross_val_score

k_values = range(1, min(31, N))
scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    cv_scores = cross_val_score(knn, X_train_scaled, y_train, cv=5)
    scores.append(cv_scores.mean())

optimal_k = k_values[np.argmax(scores)]
print(f"Optimal K: {optimal_k}")
```

### 3. Handle Missing Values

```python
from sklearn.impute import SimpleImputer

# For numerical features
imputer = SimpleImputer(strategy='mean')  # or 'median'
X_imputed = imputer.fit_transform(X)

# For categorical features
imputer = SimpleImputer(strategy='most_frequent')
X_imputed = imputer.fit_transform(X)
```

### 4. Use Appropriate Distance Metrics

```python
# Continuous features → Euclidean (default)
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

# High-dimensional → Manhattan
knn = KNeighborsClassifier(n_neighbors=5, metric='manhattan')

# Text data → Cosine
knn = KNeighborsClassifier(n_neighbors=5, metric='cosine')

# Correlated features → Mahalanobis (need to compute covariance)
from sklearn.covariance import EmpiricalCovariance
cov = EmpiricalCovariance().fit(X_train_scaled)
V = cov.covariance_

def mahalanobis_dist(x, y):
    return np.sqrt((x - y).T @ np.linalg.inv(V) @ (x - y))

knn = KNeighborsClassifier(n_neighbors=5, metric=mahalanobis_dist)
```

### 5. Optimize for Large Datasets

```python
# Use tree-based algorithms for faster search
knn = KNeighborsClassifier(
    n_neighbors=5,
    algorithm='kd_tree'  # or 'ball_tree'
)

# For very large datasets
from sklearn.neighbors import NearestNeighbors
# Use approximate methods or dimensionality reduction
```

### 6. Weighted Voting

```python
# Distance-weighted voting (usually better)
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')

# Uniform voting (default)
knn = KNeighborsClassifier(n_neighbors=5, weights='uniform')
```

---

## ⚠️ Common Pitfalls

### 1. Forgetting to Scale Features 🚫

```python
# ❌ WRONG - No scaling
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# ✅ CORRECT - With scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
knn.fit(X_train_scaled, y_train)
```

**Why it matters:**
```
Dataset: [Height(cm), Weight(kg)]
Person A: [170, 65]
Person B: [172, 70]

Without scaling:
d = √[(172-170)² + (70-65)²] = √[4 + 25] = √29 ≈ 5.4
     ↑small        ↑dominates

With scaling (mean=0, std=1):
Height: 170→0, 172→0.5
Weight: 65→-0.5, 70→0.5
d = √[(0.5-0)² + (0.5-(-0.5))²] = √[0.25 + 1] = √1.25 ≈ 1.1
     ↑balanced    ↑balanced
```

### 2. Using Even K for Binary Classification 🚫

```python
# ❌ WRONG - Even K can cause ties
knn = KNeighborsClassifier(n_neighbors=4)

# Example: 4 neighbors → [A, A, B, B] → TIE!

# ✅ CORRECT - Odd K avoids ties
knn = KNeighborsClassifier(n_neighbors=5)

# Example: 5 neighbors → [A, A, A, B, B] → A wins!
```

### 3. Not Handling Outliers 🚫

```python
# Outliers severely affect K-NN, especially with small K

# ✅ Remove outliers
from sklearn.ensemble import IsolationForest

iso = IsolationForest(contamination=0.1)
outlier_mask = iso.fit_predict(X_train) == 1
X_train_clean = X_train[outlier_mask]
y_train_clean = y_train[outlier_mask]

# Or use larger K for robustness
knn = KNeighborsClassifier(n_neighbors=15)  # More robust
```

### 4. Leaking Test Data 🚫

```python
# ❌ WRONG - Fitting scaler on all data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Includes test data!
X_train, X_test = X_scaled[:100], X_scaled[100:]

# ✅ CORRECT - Fit on train only
X_train, X_test = X[:100], X[100:]
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use fitted scaler
```

### 5. Ignoring Curse of Dimensionality 🚫

```python
# K-NN degrades with D > 20

# ✅ Reduce dimensions
from sklearn.decomposition import PCA

pca = PCA(n_components=10)  # Reduce to 10 dimensions
X_train_reduced = pca.fit_transform(X_train_scaled)
X_test_reduced = pca.transform(X_test_scaled)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_reduced, y_train)
```

### 6. Using K-NN for Large Datasets 🚫

```python
# K-NN has O(ND) prediction time

# For large N, use:
# 1. Tree-based algorithms
knn = KNeighborsClassifier(n_neighbors=5, algorithm='kd_tree')

# 2. Approximate methods
from sklearn.neighbors import NearestNeighbors

# 3. Dimensionality reduction
# 4. Alternative algorithms (SVM, Random Forest)
```

### 7. Not Cross-Validating 🚫

```python
# ❌ WRONG - Single train/test split
X_train, X_test = train_test_split(X, y)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
score = knn.score(X_test, y_test)  # Might be lucky/unlucky

# ✅ CORRECT - Cross-validation
scores = cross_val_score(knn, X, y, cv=5)
mean_score = scores.mean()
std_score = scores.std()
print(f"Score: {mean_score:.3f} (+/- {std_score:.3f})")
```

---

## 📊 Performance Metrics

### Classification Metrics

```python
from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score,
    confusion_matrix,
    classification_report
)

# Predictions
y_pred = knn.predict(X_test_scaled)

# Accuracy (use with balanced classes)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Precision (how many predicted positives are correct)
precision = precision_score(y_test, y_pred, average='weighted')
print(f"Precision: {precision:.4f}")

# Recall (how many actual positives were found)
recall = recall_score(y_test, y_pred, average='weighted')
print(f"Recall: {recall:.4f}")

# F1-Score (harmonic mean of precision and recall)
f1 = f1_score(y_test, y_pred, average='weighted')
print(f"F1-Score: {f1:.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Complete Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
```

### Regression Metrics

```python
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    median_absolute_error
)

# Predictions
y_pred = knn_reg.predict(X_test_scaled)

# Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"MSE: {mse:.4f}")

# Root Mean Squared Error
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.4f}")

# Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)
print(f"MAE: {mae:.4f}")

# R² Score (coefficient of determination)
r2 = r2_score(y_test, y_pred)
print(f"R²: {r2:.4f}")

# Median Absolute Error (robust to outliers)
med_ae = median_absolute_error(y_test, y_pred)
print(f"Median AE: {med_ae:.4f}")
```

---

## 📚 Additional Resources

### Documentation
- [scikit-learn K-NN Documentation](https://scikit-learn.org/stable/modules/neighbors.html)
- [K-NN Wikipedia](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)

### Key Papers
- Cover, T. M., & Hart, P. E. (1967). "Nearest neighbor pattern classification"
- Fix, E., & Hodges, J. L. (1951). "Discriminatory analysis"

### Online Courses
- [Coursera - Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning)
- [Fast.ai - Practical Deep Learning](https://www.fast.ai/)

### Books
- "Pattern Recognition and Machine Learning" by Christopher Bishop
- "The Elements of Statistical Learning" by Hastie, Tibshirani, and Friedman

---

## 🎓 Summary

### Key Takeaways

✅ **K-NN Strengths:**
- Simple and intuitive
- No training phase (lazy learning)
- Naturally handles multi-class problems
- Non-parametric (no assumptions)
- Can capture complex patterns

❌ **K-NN Weaknesses:**
- Slow prediction (O(ND))
- High memory usage (stores all data)
- Sensitive to irrelevant features
- Suffers from curse of dimensionality
- Requires feature scaling

### When to Use K-NN

✅ **Good for:**
- Small to medium datasets (N < 10,000)
- Low to moderate dimensions (D < 20)
- Baseline model
- When interpretability matters
- Non-linear decision boundaries

❌ **Avoid for:**
- Large datasets (N > 100,000)
- High dimensions (D > 50)
- Real-time predictions
- When training time doesn't matter but prediction must be fast

### Quick Decision Tree

```
Need a classifier?
│
├─ Small dataset (N < 10,000)?
│  ├─ Yes: Consider K-NN ✓
│  └─ No: Use Random Forest or SVM
│
├─ Low dimensions (D < 20)?
│  ├─ Yes: Consider K-NN ✓
│  └─ No: Use PCA → K-NN or switch algorithm
│
├─ Need fast predictions?
│  ├─ Yes: Switch to SVM or tree-based ✗
│  └─ No: Consider K-NN ✓
│
└─ Need interpretability?
   ├─ Yes: Consider K-NN ✓
   └─ No: Deep Learning might be better
```

---

## 🔗 Related Topics [WIP]

- [Support Vector Machines (SVM)](https://github.com/rpaut03l/TS-01/blob/main/ML/SVM/)
- [Decision Trees](https://github.com/rpaut03l/TS-01/blob/main/ML/Decision-Trees/)
- [Random Forests](https://github.com/rpaut03l/TS-01/blob/main/ML/Random-Forests/)
- [Naive Bayes](https://github.com/rpaut03l/TS-01/blob/main/ML/Naive-Bayes/)
- [Feature Scaling](https://github.com/rpaut03l/TS-01/blob/main/ML/Feature-Scaling/)

---

**🤝 Contributions welcome - open an issue or PR!**

---
