# 💻 Deep Learning: PRACTICE

> **Nav:** [📖 THEORY](ml_dl_cnn_ae_theory.md) | [🔢 NUMERICAL](ml_dl_cnn_ae_numerical.md) | 💻 **PRACTICE**

---

## Ex1: CNN on MNIST (Keras)

```python
# Run in Colab (has TensorFlow pre-installed)
import tensorflow as tf
from tensorflow.keras import layers, models

# Load MNIST (28×28 grayscale digits)
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
X_test = X_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

# Build CNN
model = models.Sequential([
    layers.Conv2D(16, (3,3), activation='relu', input_shape=(28,28,1)),  # 26×26×16
    layers.MaxPooling2D((2,2)),                                          # 13×13×16
    layers.Conv2D(32, (3,3), activation='relu'),                         # 11×11×32
    layers.MaxPooling2D((2,2)),                                          # 5×5×32
    layers.Flatten(),                                                     # 800
    layers.Dense(64, activation='relu'),                                  # 64
    layers.Dropout(0.3),                                                  # regularization
    layers.Dense(10, activation='softmax')                                # 10 classes
])

model.summary()  # shows output shapes + param counts per layer

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=5, batch_size=64,
                     validation_split=0.1, verbose=1)

test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"\nTest accuracy: {test_acc:.4f}")
# Expected: ~99% accuracy in just 5 epochs!
```

## Ex2: Autoencoder for Anomaly Detection

```python
import numpy as np, matplotlib.pyplot as plt
from tensorflow.keras import layers, models

# Normal data: digits 1 (train autoencoder on normal)
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_normal = X_train[y_train == 1].astype('float32') / 255.0
X_normal = X_normal.reshape(-1, 784)  # flatten 28×28 → 784

# Autoencoder: 784 → 32 → 784
encoder = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dense(32, activation='relu')   # bottleneck
])
decoder = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(32,)),
    layers.Dense(784, activation='sigmoid')
])
autoencoder = models.Sequential([encoder, decoder])
autoencoder.compile(optimizer='adam', loss='mse')
autoencoder.fit(X_normal, X_normal, epochs=20, batch_size=64, verbose=0)

# Test: reconstruct normal (digit 1) and anomaly (digit 7)
X_test_1 = X_test[y_test == 1][:10].astype('float32').reshape(-1,784) / 255.0
X_test_7 = X_test[y_test == 7][:10].astype('float32').reshape(-1,784) / 255.0

loss_normal = np.mean((autoencoder.predict(X_test_1) - X_test_1)**2, axis=1)
loss_anomaly = np.mean((autoencoder.predict(X_test_7) - X_test_7)**2, axis=1)

print(f"Normal (1) avg loss:  {loss_normal.mean():.4f}")
print(f"Anomaly (7) avg loss: {loss_anomaly.mean():.4f}")
print(f"Anomaly loss is {loss_anomaly.mean()/loss_normal.mean():.1f}x higher → detected!")
```

## Ex3: Conv Output Size Calculator

```python
def conv_output(I, K, P=0, S=1):
    """Calculate output size of conv/pool layer."""
    return (I - K + 2*P) // S + 1

# Example architecture
sizes = [("Input", 32)]
configs = [("Conv1 3×3 p=1 s=1", 3, 1, 1),
           ("Pool 2×2 s=2", 2, 0, 2),
           ("Conv2 3×3 p=0 s=1", 3, 0, 1),
           ("Pool 2×2 s=2", 2, 0, 2)]

current = 32
for name, K, P, S in configs:
    current = conv_output(current, K, P, S)
    print(f"  {name:25s} → {current}×{current}")
# Shows how spatial dimensions shrink through the network
```

## Ex4: Training Curves (Overfit Detection)

```python
import matplotlib.pyplot as plt

# After training a model with history = model.fit(...)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(history.history['loss'], label='Train')
axes[0].plot(history.history['val_loss'], label='Val')
axes[0].set_title("Loss"); axes[0].legend(); axes[0].grid(True, alpha=0.3)

axes[1].plot(history.history['accuracy'], label='Train')
axes[1].plot(history.history['val_accuracy'], label='Val')
axes[1].set_title("Accuracy"); axes[1].legend(); axes[1].grid(True, alpha=0.3)

plt.tight_layout(); plt.show()
# If train↓ but val↑ → OVERFITTING! Add dropout/early stopping.
```

---

> **Nav:** [📖 THEORY](ml_dl_cnn_ae_theory.md) | [🔢 NUMERICAL](ml_dl_cnn_ae_numerical.md) | 💻 PRACTICE

[↑ Back to Top](#-deep-learning-practice)

*AI · ML · github.com/rpaut03l/TS-01*
