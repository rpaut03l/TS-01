# 🧠 Neural Networks — ADVANCED

### *Everything beyond MLP + backprop: how to actually train a deep net*

> **Nav:** [← NN Theory (basics)](../ml_nn_mlp_bp_theory.md) | [← ML Master Index](../../ml_master_gap_index.md) | [Deep Learning Advanced →](../../Deep-Learning/advanced/README.md)

---

## 📚 Contents of this folder

| # | File | Topics |
|---|---|---|
| 1 | [ml_nn_adv_initialization.md](ml_nn_adv_initialization.md) | Why init matters, Xavier/Glorot, He/Kaiming, LeCun, orthogonal, universal approximation theorem |
| 2 | [ml_nn_adv_optimizers.md](ml_nn_adv_optimizers.md) | SGD → Momentum → Nesterov → AdaGrad → RMSProp → Adam → AdamW, learning-rate schedules |
| 3 | [ml_nn_adv_regularization.md](ml_nn_adv_regularization.md) | Dropout, BatchNorm, LayerNorm, weight decay, early stopping, label smoothing |
| 4 | [ml_nn_adv_gradients_activations.md](ml_nn_adv_gradients_activations.md) | Vanishing / exploding gradients, ReLU → LeakyReLU → ELU → SELU → GELU → Swish → Mish, gradient clipping, skip connections |
| 5 | [ml_nn_adv_losses.md](ml_nn_adv_losses.md) | Classification: CE / focal / label-smoothed. Regression: Huber / log-cosh. Metric learning: contrastive / triplet / InfoNCE |

---

## 🧭 Reading order

If you're new to training deep networks, read them in the order above. Each file assumes the basics from [ml_nn_mlp_bp_theory.md](../ml_nn_mlp_bp_theory.md) (perceptron, forward/backward pass, activation functions).

---

## 🔗 Prerequisites

- **Forward + backward pass** from [NN theory basics](../ml_nn_mlp_bp_theory.md) §4–§5
- **Chain rule** (calculus)
- Basic NumPy / PyTorch familiarity for the code snippets

---

## 🎯 What you'll know after reading

- Why naive Gaussian init makes deep nets impossible to train, and how He/Xavier fix it
- Why Adam works when SGD struggles, and when it's the wrong choice
- What BatchNorm actually does (and doesn't) and why LayerNorm is the default in transformers
- How to diagnose vanishing / exploding gradients and what to do about each
- When to use focal loss vs plain cross-entropy, and how contrastive losses work

---

> *ML · Neural Networks Advanced · github.com/rpaut03l/TS-01*
