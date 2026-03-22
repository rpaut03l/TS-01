# 💻 ML Foundations: PRACTICE

### *Code it, test it.*

> **Nav:** [📖 THEORY](ml_foundations_theory.md) | [🔢 NUMERICAL](ml_foundations_numerical.md) | 💻 **PRACTICE**

---

## Ex1: Normalization

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

X = np.array([[10, 50000], [20, 60000], [30, 55000], [40, 70000], [50, 80000]])

# Min-Max → [0,1]
mm = MinMaxScaler()
X_mm = mm.fit_transform(X)
print("Min-Max:\n", X_mm.round(3))

# Z-Score → mean=0, std=1
ss = StandardScaler()
X_ss = ss.fit_transform(X)
print("Z-Score:\n", X_ss.round(3))
print("Means:", X_ss.mean(axis=0).round(3))   # [0, 0]
print("Stds:", X_ss.std(axis=0).round(3))      # [1, 1]
```

## Ex2: Confusion Matrix & Metrics

```python
from sklearn.metrics import (confusion_matrix, accuracy_score,
                              precision_score, recall_score, f1_score,
                              classification_report)
import numpy as np

y_true = [1,1,1,1,1,0,0,0,0,0]
y_pred = [1,1,1,0,0,0,0,0,1,0]

cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:\n", cm)
#  [[4, 1],    TN=4, FP=1
#   [2, 3]]    FN=2, TP=3
print(f"Accuracy:  {accuracy_score(y_true, y_pred):.3f}")
print(f"Precision: {precision_score(y_true, y_pred):.3f}")
print(f"Recall:    {recall_score(y_true, y_pred):.3f}")
print(f"F1:        {f1_score(y_true, y_pred):.3f}")
print("\nFull Report:\n", classification_report(y_true, y_pred))
```

## Ex3: K-Fold Cross-Validation

```python
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=300, noise=0.3, random_state=42)
clf = DecisionTreeClassifier(max_depth=5, random_state=42)

scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print(f"5-Fold CV: {scores}")
print(f"Mean: {scores.mean():.3f} ± {scores.std():.3f}")
print(f"SE: {scores.std()/np.sqrt(5):.4f}")
```

## Ex4: Bias-Variance Visual

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

np.random.seed(42)
x_true = np.linspace(0, 1, 100)
y_true = np.sin(2 * np.pi * x_true)  # true function

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, degree, label in zip(axes, [1, 4, 15],
    ["High Bias (degree=1)", "Good Fit (degree=4)", "High Variance (degree=15)"]):
    for _ in range(5):  # 5 different training sets
        x_train = np.random.uniform(0, 1, 20)
        y_train = np.sin(2*np.pi*x_train) + np.random.normal(0, 0.3, 20)
        model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        model.fit(x_train.reshape(-1,1), y_train)
        ax.plot(x_true, model.predict(x_true.reshape(-1,1)), alpha=0.4, c='blue')
    ax.plot(x_true, y_true, 'r-', linewidth=2, label='True')
    ax.set_title(label, fontsize=12)
    ax.set_ylim(-2, 2)
    ax.legend()
plt.tight_layout()
plt.show()
# Degree 1: all lines similar but wrong (HIGH BIAS)
# Degree 15: lines wildly different (HIGH VARIANCE)
# Degree 4: lines similar AND close to truth (GOOD FIT)
```

---

> **Nav:** [📖 THEORY](ml_foundations_theory.md) | [🔢 NUMERICAL](ml_foundations_numerical.md) | 💻 PRACTICE

[↑ Back to Top](#-ml-foundations-practice)

*AI · ML · github.com/rpaut03l/TS-01*
