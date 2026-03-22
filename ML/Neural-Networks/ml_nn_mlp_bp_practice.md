# 💻 Neural Networks: PRACTICE

> **Nav:** [📖 THEORY](ml_nn_mlp_bp_theory.md) | [🔢 NUMERICAL](ml_nn_mlp_bp_numerical.md) | 💻 **PRACTICE**

---

## Ex1: MLP with sklearn

```python
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np

X, y = make_moons(n_samples=500, noise=0.2, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

mlp = MLPClassifier(hidden_layer_sizes=(10, 5), activation='relu',
                     max_iter=500, random_state=42)
mlp.fit(X_tr, y_tr)
print(f"Train acc: {mlp.score(X_tr, y_tr):.3f}")
print(f"Test acc:  {mlp.score(X_te, y_te):.3f}")
print(f"Layers: {[c.shape for c in mlp.coefs_]}")
print(f"Total params: {sum(c.size for c in mlp.coefs_) + sum(b.size for b in mlp.intercepts_)}")
```

## Ex2: Forward Pass from Scratch

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 2-2-1 network
W1 = np.array([[0.3, 0.4], [0.5, -0.2]])  # 2×2
b1 = np.array([0.1, -0.1])
W2 = np.array([[0.6, 0.7]])               # 1×2
b2 = np.array([0.2])
x = np.array([1.0, 0.5])

# Forward
z1 = W1.T @ x + b1     # hidden pre-activation
a1 = sigmoid(z1)        # hidden activation
z2 = W2 @ a1 + b2       # output pre-activation
y_hat = sigmoid(z2)      # output

print(f"Hidden z: {z1.round(3)}")
print(f"Hidden a: {a1.round(3)}")
print(f"Output:   {y_hat[0]:.4f}")

# Backprop (y_true = 1)
y_true = 1.0
delta2 = (y_hat - y_true) * y_hat * (1 - y_hat)    # output δ
dW2 = delta2.reshape(-1,1) @ a1.reshape(1,-1)       # ∂L/∂W2
delta1 = (W2.T @ delta2).flatten() * a1 * (1 - a1)  # hidden δ
dW1 = np.outer(x, delta1)                            # ∂L/∂W1

print(f"\nδ_output: {delta2.round(5)}")
print(f"∂L/∂W2:   {dW2.round(5)}")
print(f"δ_hidden: {delta1.round(5)}")
print(f"∂L/∂W1:\n{dW1.round(5)}")

# Update
lr = 0.5
W2 -= lr * dW2
W1 -= lr * dW1.T
print(f"\nUpdated W2: {W2.round(4)}")
print(f"Updated W1:\n{W1.round(4)}")
```

## Ex3: Activation Functions Visual

```python
import numpy as np, matplotlib.pyplot as plt

z = np.linspace(-5, 5, 200)
fig, axes = plt.subplots(1, 4, figsize=(16, 3))

funcs = [('Sigmoid', 1/(1+np.exp(-z))),
         ('Tanh', np.tanh(z)),
         ('ReLU', np.maximum(0, z)),
         ('Leaky ReLU', np.where(z>0, z, 0.01*z))]

for ax, (name, vals) in zip(axes, funcs):
    ax.plot(z, vals, linewidth=2)
    ax.axhline(0, c='gray', lw=0.5); ax.axvline(0, c='gray', lw=0.5)
    ax.set_title(name); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.show()
```

## Ex4: Loss Curve (training progress)

```python
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons

X, y = make_moons(500, noise=0.2, random_state=42)
mlp = MLPClassifier(hidden_layer_sizes=(20,10), max_iter=300, random_state=42)
mlp.fit(X, y)

import matplotlib.pyplot as plt
plt.plot(mlp.loss_curve_, 'b-', linewidth=2)
plt.xlabel("Epoch"); plt.ylabel("Loss"); plt.title("MLP Training Loss")
plt.grid(True, alpha=0.3); plt.show()
```

---

> **Nav:** [📖 THEORY](ml_nn_mlp_bp_theory.md) | [🔢 NUMERICAL](ml_nn_mlp_bp_numerical.md) | 💻 PRACTICE

[↑ Back to Top](#-neural-networks-practice)

*AI · ML · github.com/rpaut03l/TS-01*
