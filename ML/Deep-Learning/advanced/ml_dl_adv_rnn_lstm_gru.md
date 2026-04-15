# 📖 DL Advanced: RNN · LSTM · GRU

### *Vanishing gradients in time · Gates · Seq2seq · Teacher forcing*

> **Nav:** [← advanced README](README.md) | [DL Basics](../ml_dl_cnn_ae_theory.md) | [Transformers →](ml_dl_adv_transformers.md)

---

## 🧠 MNEMONIC: **"VGSL-TB"**

> **V**anilla RNN · **G**RU · **S**equence-to-sequence · **L**STM · **T**eacher forcing · **B**idirectional

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Why RNNs | [§1](#1-why-rnns) |
| 2 | Vanilla RNN | [§2](#2-vanilla-rnn) |
| 3 | Vanishing Gradients in Time | [§3](#3-vanishing-gradients-in-time) |
| 4 | LSTM — Long Short-Term Memory | [§4](#4-lstm) |
| 5 | GRU — Gated Recurrent Unit | [§5](#5-gru) |
| 6 | Bidirectional RNNs | [§6](#6-bidirectional-rnns) |
| 7 | Sequence-to-Sequence & Teacher Forcing | [§7](#7-sequence-to-sequence--teacher-forcing) |
| 8 | When to Use RNNs vs Transformers | [§8](#8-when-to-use-rnns-vs-transformers) |
| 9 | Cheat Sheet | [§9](#9-cheat-sheet--exam-hacks) |

---

## 1. Why RNNs

Feedforward networks take a **fixed-size** input. Language, audio, video, and time series have **variable-length** sequences with temporal structure. RNNs handle this by maintaining a **hidden state** that evolves as they walk through the sequence:

```
h_t = f(h_{t-1}, x_t)
y_t = g(h_t)
```

The same function **f** is applied at every step. The network can process sequences of any length and (in theory) remember information indefinitely via h_t.

[↑ Back to Top](#-dl-advanced-rnn--lstm--gru)

---

## 2. Vanilla RNN

### Recurrence
```
h_t = tanh( W_xh · x_t  +  W_hh · h_{t-1}  +  b_h )
y_t = W_hy · h_t + b_y
```

### Unrolled view
```
   x_1      x_2      x_3      x_4
    │        │        │        │
    ▼        ▼        ▼        ▼
  [RNN]→[RNN]→[RNN]→[RNN]
    │        │        │        │
    ▼        ▼        ▼        ▼
   y_1      y_2      y_3      y_4
```

### BPTT — Backpropagation Through Time
Treat the unrolled RNN as a deep feedforward net and backprop through it. Gradients flow **backward in time**, accumulating contributions from every step.

### Complexity
- **O(T)** in time for forward/backward (T = sequence length).
- **O(T)** memory to store all hidden states (needed for BPTT).
- **Truncated BPTT** — only unroll K steps back → trades memory for accurate gradient.

[↑ Back to Top](#-dl-advanced-rnn--lstm--gru)

---

## 3. Vanishing Gradients in Time

Backprop through T steps multiplies **T − 1 Jacobians**:

```
∂L/∂h_1 = ∂L/∂h_T · ∂h_T/∂h_{T-1} · ... · ∂h_2/∂h_1
                   └────────── product of T−1 terms ──────────┘
```

If the repeated Jacobian has spectral radius:
- **< 1** → **vanishing** gradients; the network can't remember more than ~10 steps back.
- **> 1** → **exploding** gradients; training diverges.

### Why it's worse than feedforward vanishing
In a feedforward net, each layer has different weights, so multiplying L different Jacobians can cancel out in any direction. In an RNN, it's the **same matrix** W_hh every time, so shrinking/growing in the same eigendirection compounds unchecked.

### Fixes (in order of effectiveness)
1. **Gated architectures** (LSTM, GRU) — have an additive path for the cell state.
2. **Orthogonal init** of W_hh — keeps the spectral radius at 1.
3. **Gradient clipping** — for exploding gradients specifically.
4. **Skip connections across time** (rare).

[↑ Back to Top](#-dl-advanced-rnn--lstm--gru)

---

## 4. LSTM

Hochreiter & Schmidhuber (1997). Introduces a **cell state c_t** with an additive update path, protected by **gates**.

### Gates
```
f_t = σ(W_f [h_{t-1}, x_t] + b_f)       forget gate
i_t = σ(W_i [h_{t-1}, x_t] + b_i)       input  gate
o_t = σ(W_o [h_{t-1}, x_t] + b_o)       output gate
g_t = tanh(W_g [h_{t-1}, x_t] + b_g)    candidate cell
```

### Cell and hidden state updates
```
c_t = f_t * c_{t-1}  +  i_t * g_t        (element-wise)
h_t = o_t * tanh(c_t)
```

### Why gates solve vanishing
The cell state has an **additive** update (+) instead of a multiplicative one. If the forget gate stays near 1 and the input gate near 0, **c_t ≈ c_{t-1}** — information survives arbitrarily long with no gradient decay. During backprop, the gradient through the cell state is essentially multiplied by the diagonal matrix `diag(f_t)` — as long as forget gates stay near 1 in the relevant dimensions, gradients flow undiminished.

### Forget-gate bias init = 1
A common trick: initialize `b_f = 1` so that the forget gate starts near σ(1) ≈ 0.73 — meaning "remember by default." Without this, random init makes forget ≈ 0.5 and long-term info is lost at the start of training.

### LSTM variants
- **Peephole connections** — gates look at c_{t-1} too (rarely helps).
- **Coupled input/forget** — f_t = 1 − i_t (fewer parameters, similar performance).
- **LayerNorm-LSTM** — normalize gate pre-activations for stability.

[↑ Back to Top](#-dl-advanced-rnn--lstm--gru)

---

## 5. GRU

Cho et al. (2014). A simplified, faster alternative with comparable performance.

### Gates
```
r_t = σ(W_r [h_{t-1}, x_t])     reset gate
z_t = σ(W_z [h_{t-1}, x_t])     update gate
h̃_t = tanh(W_h [r_t * h_{t-1}, x_t])
h_t = (1 − z_t) * h_{t-1}  +  z_t * h̃_t
```

### Differences from LSTM
- **No separate cell state** — just h_t.
- **2 gates** instead of 3.
- **~25% fewer parameters** for the same width.
- **Faster** per step.
- Comparable accuracy on most tasks; LSTM slightly wins on very long sequences.

### Which to use?
- **GRU** — smaller datasets, time-constrained, small models.
- **LSTM** — very long sequences, largest language models from the pre-transformer era.
- **Neither** — for most things in 2026 you reach for a transformer instead.

[↑ Back to Top](#-dl-advanced-rnn--lstm--gru)

---

## 6. Bidirectional RNNs

Run one RNN forward through the sequence and another backward, concatenate the hidden states:

```
→ h_t →  forward h at step t
← h_t ←  backward h at step t
final h_t = [→h_t ; ←h_t]
```

### Use
- **Tagging tasks** (POS tagging, NER) — each token gets context from both sides.
- **Speech recognition** — read ahead helps phoneme resolution.
- **NOT for generation** — you can't peek at future tokens you haven't generated yet.

[↑ Back to Top](#-dl-advanced-rnn--lstm--gru)

---

## 7. Sequence-to-Sequence & Teacher Forcing

Sutskever et al. (2014). Map an input sequence to an output sequence of different length.

### Architecture
```
ENCODER (RNN)       DECODER (RNN)
 x_1 ─┐
 x_2 ─┼→  h ─→ [context c]  ─→ y_1 ─→ y_2 ─→ ... ─→ <EOS>
 x_3 ─┘                        ↑      ↑      ↑
                             (prev token feeds next step)
```

The encoder compresses the input sequence into a **context vector** (final hidden state). The decoder starts from this context and generates tokens autoregressively.

### Training — Teacher Forcing
At train time, feed the **ground-truth** previous token to the decoder, not its own prediction. This prevents early errors from compounding.

```
TEACHER FORCING
  At step t, decoder input = y_{t-1}^true   (not ŷ_{t-1})

PROS: stable training, fast convergence
CONS: exposure bias — at inference, the model feeds its own (imperfect) predictions,
      and it has never seen its own mistakes during training.
```

### Scheduled sampling
Bengio et al. (2015). Mix ground truth and predictions during training with a schedule that progressively relies more on the model's own output. Helps close the train/inference gap.

### The attention fix
The context vector becomes a bottleneck for long sequences. **Attention** (Bahdanau 2014) lets the decoder look at **all encoder hidden states** at each step, weighted by relevance → massively improves long-sequence translation → led directly to the transformer (see next file).

[↑ Back to Top](#-dl-advanced-rnn--lstm--gru)

---

## 8. When to Use RNNs vs Transformers

```
┌────────────────────────┬────────────┬─────────────┐
│ SITUATION              │ RNN/LSTM   │ TRANSFORMER │
├────────────────────────┼────────────┼─────────────┤
│ General NLP / LLMs     │ ❌         │ ✅          │
│ Big compute budget     │ —          │ ✅          │
│ Tiny compute / on-device│ ✅        │ —           │
│ Streaming / real-time  │ ✅         │ (tricky)    │
│ Very short sequences   │ OK         │ ✅          │
│ Very long sequences    │ ❌         │ (with care) │
│ Online learning (1 step│ ✅         │ ❌          │
│  at a time)            │            │             │
└────────────────────────┴────────────┴─────────────┘
```

- **Transformers** dominate almost every serious NLP task.
- **RNNs / LSTMs** still find niches where the **streaming** nature or **constant memory** per step matters — speech decoding, online control, tiny embedded models.

[↑ Back to Top](#-dl-advanced-rnn--lstm--gru)

---

## 9. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  RNN / LSTM / GRU ONE-LINERS                                 ║
╠══════════════════════════════════════════════════════════════╣
║  Vanilla RNN:   h_t = tanh(W[h, x])                          ║
║  LSTM:   cell state w/ additive updates + 3 gates            ║
║  GRU:    simpler, 2 gates, no separate cell                  ║
║  Gates fix vanishing by giving gradient an identity path     ║
║  Forget-gate bias init = 1                                   ║
║  Teacher forcing: train with ground-truth prev tokens        ║
║  Scheduled sampling: bridge train/inference gap              ║
║  Seq2seq context vector is a bottleneck → attention          ║
║  Transformers replaced LSTMs for most NLP (2017+)            ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Why does LSTM not vanish?"** — additive cell-state update + gates allow long-term information to persist without multiplicative decay.
2. **"GRU vs LSTM — which is better?"** — GRU is faster and smaller; LSTM slightly more powerful on very long sequences; in practice both are dominated by transformers now.
3. **"What is teacher forcing and its drawback?"** — feeding ground-truth previous tokens during training; drawback is exposure bias (model never sees its own mistakes).
4. **"BPTT complexity?"** — O(T) time and memory.
5. **"Why init forget-gate bias to 1?"** — so the network starts out *remembering* by default, not forgetting — essential for learning long dependencies.
6. **"Why are bidirectional RNNs not used for generation?"** — you can't look at future tokens that haven't been generated yet.

[↑ Back to Top](#-dl-advanced-rnn--lstm--gru)

---

### 💻 Quick Code

```python
import torch
import torch.nn as nn

# Vanilla-ish (use nn.RNN / nn.LSTM / nn.GRU)
rnn  = nn.RNN(input_size=64, hidden_size=128, num_layers=2, batch_first=True)
lstm = nn.LSTM(input_size=64, hidden_size=128, num_layers=2, batch_first=True, dropout=0.1)
gru  = nn.GRU(input_size=64, hidden_size=128, num_layers=2, batch_first=True, bidirectional=True)

x = torch.randn(32, 50, 64)          # [batch, time, features]
out, _ = lstm(x)                     # out: [32, 50, 128]

# Gradient clipping is essential for LSTMs
loss.backward()
torch.nn.utils.clip_grad_norm_(lstm.parameters(), max_norm=1.0)
```

---

> **Next:** [Transformers →](ml_dl_adv_transformers.md)
>
> *ML · Deep Learning Advanced · github.com/rpaut03l/TS-01*
