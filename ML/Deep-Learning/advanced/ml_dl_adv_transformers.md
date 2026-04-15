# 📖 DL Advanced: Transformers & Self-Attention

### *QKV · Self-attention · Multi-head · Positional encoding · Encoder/Decoder*

> **Nav:** [← RNN/LSTM/GRU](ml_dl_adv_rnn_lstm_gru.md) | [advanced README](README.md) | [Generative Models →](ml_dl_adv_generative.md)

---

## 🧠 MNEMONIC: **"QKV-PMFM"**

> **Q**uery · **K**ey · **V**alue · **P**ositional enc · **M**ulti-head · **F**FN · **M**ask

---

## 📚 Table of Contents

| # | Topic | Jump |
|---|-------|------|
| 1 | Motivation — Why Attention Replaced RNNs | [§1](#1-motivation) |
| 2 | Self-Attention — the QKV Machinery | [§2](#2-self-attention) |
| 3 | Scaled Dot-Product Attention | [§3](#3-scaled-dot-product-attention) |
| 4 | Multi-Head Attention | [§4](#4-multi-head-attention) |
| 5 | Positional Encoding | [§5](#5-positional-encoding) |
| 6 | Transformer Block (Pre-LN vs Post-LN) | [§6](#6-transformer-block) |
| 7 | Encoder · Decoder · Masking | [§7](#7-encoder-decoder-masking) |
| 8 | Complexity & Efficient Attention | [§8](#8-complexity--efficient-attention) |
| 9 | Cheat Sheet | [§9](#9-cheat-sheet--exam-hacks) |

---

## 1. Motivation

RNNs process sequences **one step at a time**. Two consequences:
1. **No parallelism** — GPU idle most of the time.
2. **Long-range dependencies** — information from step 1 must survive through hundreds of steps of hidden-state compression.

**Self-attention** (Vaswani et al. 2017) lets every token interact with every other token in **one step** and **in parallel**. No recurrence. This is the entire idea behind the transformer.

```
RNN       O(T)    sequential  ❌ parallel
Attn      O(T²)   parallel    ✅ parallel
```

Transformers trade quadratic cost in sequence length for massive parallelism.

[↑ Back to Top](#-dl-advanced-transformers--self-attention)

---

## 2. Self-Attention

### The idea in one sentence
Each token **looks at** every other token, **weights** their contributions by similarity, and produces a new representation of itself that incorporates relevant information from everywhere.

### Three projections per token
```
q_i = x_i · W_Q      (query — what am I looking for?)
k_i = x_i · W_K      (key   — what do I represent?)
v_i = x_i · W_V      (value — what information do I carry?)
```

### Attention weight
```
α_{ij} = softmax_j ( q_i · k_j )
```
Token i attends to token j with weight proportional to how similar q_i is to k_j.

### Weighted sum
```
o_i = Σ_j α_{ij} · v_j
```

Each output token is a **convex combination** of all value vectors, where the weights come from the Q-K similarity.

[↑ Back to Top](#-dl-advanced-transformers--self-attention)

---

## 3. Scaled Dot-Product Attention

In matrix form for a whole sequence:

```
Q = X W_Q      [n × d_k]
K = X W_K      [n × d_k]
V = X W_V      [n × d_v]

Attention(Q, K, V) = softmax( Q Kᵀ / √d_k ) V
                           └──── attention scores ────┘
```

### Why the √d_k scale?
- QKᵀ has variance that grows linearly in d_k.
- Without the scale, for large d_k the softmax saturates (one value near 1, rest near 0), and gradients vanish.
- Dividing by √d_k keeps the pre-softmax logits at ~constant variance across depths/widths.

### Masking
To prevent tokens from attending where they shouldn't (e.g., future positions in a language model), set the corresponding logits to **−∞** before the softmax:
```
scores = scores.masked_fill(mask == 0, float('-inf'))
```
After softmax those positions get weight 0.

[↑ Back to Top](#-dl-advanced-transformers--self-attention)

---

## 4. Multi-Head Attention

Running attention once is limited — every token gets a **single** weighted sum. Splitting into **h heads** lets the model attend to **h different relations** in parallel:

```
For head i ∈ 1..h:
  Q_i = X W_Q^i        [n × d_k / h]
  K_i = X W_K^i        [n × d_k / h]
  V_i = X W_V^i        [n × d_v / h]
  O_i = Attention(Q_i, K_i, V_i)

MultiHead(X) = concat(O_1, ..., O_h) · W_O
```

### Interpretation
Different heads can specialize — one tracks syntactic agreement, another semantic similarity, etc. Interpretability research shows this is real but messy.

### Shapes
- Total dimensions still d_model across all heads.
- Each head uses d_model / h dimensions.
- Typical: d_model = 768, h = 12 → d_k = 64 per head (BERT base).

[↑ Back to Top](#-dl-advanced-transformers--self-attention)

---

## 5. Positional Encoding

Self-attention is **permutation-invariant** — shuffling the tokens gives the same set of outputs. We must inject position information somehow.

### Sinusoidal (original transformer)
```
PE_{pos, 2i}   = sin( pos / 10000^(2i / d) )
PE_{pos, 2i+1} = cos( pos / 10000^(2i / d) )
```
- **Deterministic** — no learned parameters.
- **Extrapolates** (sort of) beyond the training length.
- Used in the original "Attention Is All You Need."

### Learned absolute
A simple embedding table `nn.Embedding(max_len, d_model)`. Used in **BERT** and **GPT-2**.
- Limited to the max length seen during training.
- Works great in practice.

### Relative (Shaw 2018)
Encode the **distance** between positions in the attention score, not the absolute position.
- Better generalization to longer sequences.
- Used in **Transformer-XL**, **DeBERTa**.

### Rotary (RoPE, Su 2021)
Rotate the Q and K vectors by an angle proportional to position before computing attention.
- Combines benefits: relative, no extra parameters, extrapolates well.
- Used in **LLaMA**, **PaLM**, most modern LLMs.

[↑ Back to Top](#-dl-advanced-transformers--self-attention)

---

## 6. Transformer Block

A single transformer block has:
1. **Multi-head self-attention**
2. **Residual + LayerNorm**
3. **Feed-forward network (FFN)** — two linear layers with a nonlinearity
4. **Residual + LayerNorm**

### Post-LayerNorm (original)
```
x ← x + MultiHead(x)
x ← LayerNorm(x)
x ← x + FFN(x)
x ← LayerNorm(x)
```

### Pre-LayerNorm (modern default)
```
x ← x + MultiHead(LayerNorm(x))
x ← x + FFN(LayerNorm(x))
```
- **Pre-LN is more stable** for deep models — gradient paths are cleaner.
- **Original post-LN** can work but needs careful LR warmup to avoid divergence.
- Most modern LLMs (GPT-2+, LLaMA) use pre-LN.

### FFN
```
FFN(x) = Linear(GELU(Linear(x)))
```
- Expands to 4 × d_model in the middle.
- Most of the parameters of a transformer live in the FFN.
- Modern variants: SwiGLU, GeGLU — gated variants that slightly improve quality.

[↑ Back to Top](#-dl-advanced-transformers--self-attention)

---

## 7. Encoder · Decoder · Masking

Original transformer (2017) had both halves for machine translation:

### Encoder (e.g., BERT)
- Bidirectional self-attention — every token sees every other token.
- Used for **understanding / classification / embeddings**.

### Decoder (e.g., GPT)
- **Causal / masked** self-attention — token i only attends to tokens 1..i.
- Used for **generation** — autoregressive next-token prediction.

### Cross-attention (seq2seq, e.g., T5 decoder)
- Decoder attends to the encoder's output as well as its own past tokens.
- Used for **translation**, **summarization**.

### Attention masks — at a glance
```
BIDIRECTIONAL (encoder/BERT)         CAUSAL (decoder/GPT)
[1 1 1 1 1]                          [1 0 0 0 0]
[1 1 1 1 1]                          [1 1 0 0 0]
[1 1 1 1 1]                          [1 1 1 0 0]
[1 1 1 1 1]                          [1 1 1 1 0]
[1 1 1 1 1]                          [1 1 1 1 1]
```
0 = mask out (logits → −∞).

[↑ Back to Top](#-dl-advanced-transformers--self-attention)

---

## 8. Complexity & Efficient Attention

### Standard complexity
- **Time:** O(n² · d)   (dominated by Q Kᵀ for n tokens, each of dim d)
- **Memory:** O(n²)    (the attention matrix itself)

For long documents (n = 100k tokens), n² = 10¹⁰ — infeasible.

### Efficient attention variants
| Method | Complexity | Key idea |
|---|---|---|
| **Standard** | O(n²) | baseline |
| **FlashAttention** | O(n²) but I/O-aware | fused CUDA kernel, 2-4× faster, no accuracy loss |
| **Sparse attention** | O(n√n) or O(n log n) | attend only to local + global tokens |
| **Longformer / BigBird** | O(n) | sliding window + a few global tokens |
| **Linformer** | O(n) | project keys and values to smaller rank |
| **Performer** | O(n) | approximate softmax with random features |
| **Mamba / State-space** | O(n) | structured state space model, not attention |

### Practical reality in 2026
- **FlashAttention-2/3** — almost free speedup, use it by default.
- **Long-context LLMs** use combinations of sliding window + global tokens + RoPE tricks.
- **True subquadratic** attention variants exist but rarely beat flash-attention for n < ~100k on modern hardware.

[↑ Back to Top](#-dl-advanced-transformers--self-attention)

---

## 9. Cheat Sheet & Exam Hacks

```
╔══════════════════════════════════════════════════════════════╗
║  TRANSFORMER FORMULAE                                        ║
╠══════════════════════════════════════════════════════════════╣
║  Q = XW_Q,  K = XW_K,  V = XW_V                              ║
║  Attn(Q,K,V) = softmax(QKᵀ/√d_k) · V                         ║
║  MultiHead: split dim, run h attentions, concat, project     ║
║  Block (pre-LN):                                             ║
║     x ← x + Attn(LN(x))                                      ║
║     x ← x + FFN(LN(x))                                       ║
║  FFN = Linear(GELU(Linear(x))), inner dim = 4·d_model        ║
║  Positional encoding required (attention is perm-invariant)  ║
║  Causal mask for decoder/autoregressive LMs                  ║
║  Complexity: O(n² · d)                                       ║
╚══════════════════════════════════════════════════════════════╝
```

### ⚡ Exam Red Flags
1. **"Why divide by √d_k?"** — keeps QKᵀ logits from growing with d_k and saturating the softmax.
2. **"Why multi-head?"** — lets different heads attend to different patterns in parallel; roughly equivalent to an ensemble of attention mechanisms within one layer.
3. **"Why positional encoding?"** — self-attention is permutation-invariant; position info must be added or the model can't tell token order.
4. **"What's the difference between BERT and GPT?"** — BERT uses bidirectional encoder attention for understanding tasks; GPT uses causal masked decoder attention for generation.
5. **"Self-attention complexity?"** — O(n² · d) in both time and memory; the n² term dominates for long sequences.
6. **"Pre-LN vs Post-LN?"** — pre-LN (layer-norm inside the residual) is more stable at depth; post-LN (original) needs careful warmup to train without diverging.

[↑ Back to Top](#-dl-advanced-transformers--self-attention)

---

### 💻 Quick Code — scaled dot-product attention from scratch

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

def attention(q, k, v, mask=None):
    """
    q, k, v: [B, h, n, d_k]
    mask:    [B, 1, n, n] or similar broadcast shape
    """
    d_k = q.size(-1)
    scores = (q @ k.transpose(-2, -1)) / math.sqrt(d_k)      # [B, h, n, n]
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))
    weights = F.softmax(scores, dim=-1)
    return weights @ v

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_heads):
        super().__init__()
        self.h = n_heads
        self.d_k = d_model // n_heads
        self.W_qkv = nn.Linear(d_model, 3 * d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        B, n, d = x.shape
        qkv = self.W_qkv(x).reshape(B, n, 3, self.h, self.d_k)
        q, k, v = qkv.permute(2, 0, 3, 1, 4)     # each [B, h, n, d_k]
        out = attention(q, k, v, mask)           # [B, h, n, d_k]
        out = out.transpose(1, 2).reshape(B, n, d)
        return self.W_o(out)
```

Or just use `nn.MultiheadAttention` or `torch.nn.functional.scaled_dot_product_attention` (calls FlashAttention where available).

---

> **Next:** [Generative Models →](ml_dl_adv_generative.md)
>
> *ML · Deep Learning Advanced · github.com/rpaut03l/TS-01*
