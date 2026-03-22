# 🔢 Deep Learning: NUMERICAL

### *Conv sizes, param counts, pooling, autoencoder loss.*

> **Nav:** [📖 THEORY](ml_dl_cnn_ae_theory.md) | 🔢 **NUMERICAL** | [💻 PRACTICE →](ml_dl_cnn_ae_practice.md)

---

## 📦 KEY FORMULAS

```
┌──────────────────────────────────────────────────────────────┐
│ CONV OUTPUT: O = (I - K + 2P)/S + 1                          │
│ CONV PARAMS: K×K×C_in×C_out + C_out                          │
│ POOL OUTPUT: O = I/S  (for pool_size=S, stride=S)            │
│ FC PARAMS:   input_size × output_size + output_size          │
│ AE LOSS:     L = ||x - x̂||² = Σ(xᵢ - x̂ᵢ)²                    │
│ TOTAL PARAMS: Σ (conv params) + Σ (FC params)                │
└──────────────────────────────────────────────────────────────┘
```

---

## P1: Conv Layer Output Sizes

```
Input: 32×32×3 (e.g., CIFAR-10 image)

CONV1: 16 filters, 3×3, stride=1, padding=1
  O = (32 - 3 + 2×1)/1 + 1 = 32 → output: 32×32×16
  Params: 3×3×3×16 + 16 = 448

POOL1: MaxPool 2×2, stride=2
  O = 32/2 = 16 → output: 16×16×16
  Params: 0 (pooling has no learnable parameters!)

CONV2: 32 filters, 3×3, stride=1, padding=0
  O = (16 - 3 + 0)/1 + 1 = 14 → output: 14×14×32
  Params: 3×3×16×32 + 32 = 4,640

POOL2: MaxPool 2×2, stride=2
  O = 14/2 = 7 → output: 7×7×32
  Params: 0

FLATTEN: 7×7×32 = 1,568

FC1: 1568 → 256
  Params: 1568×256 + 256 = 401,664

FC2: 256 → 10
  Params: 256×10 + 10 = 2,570

TOTAL PARAMS: 448 + 4,640 + 401,664 + 2,570 = 409,322
NOTE: FC layers dominate (>98% of params)!
```

[↑ Back to Top](#-deep-learning-numerical)

---

## P2: Convolution by Hand (3×3 on 4×4)

```
Input I:          Kernel K:
[1 2 0 1]        [1 0 1]
[0 1 3 2]        [0 1 0]
[2 0 1 0]        [1 0 1]
[1 3 2 1]

Output (stride=1, no padding): O = (4-3)/1 + 1 = 2 → 2×2

O[0,0] = 1×1+2×0+0×1 + 0×0+1×1+3×0 + 2×1+0×0+1×1 = 1+0+0+0+1+0+2+0+1 = 5
O[0,1] = 2×1+0×0+1×1 + 1×0+3×1+2×0 + 0×1+1×0+0×1 = 2+0+1+0+3+0+0+0+0 = 6
O[1,0] = 0×1+1×0+3×1 + 2×0+0×1+1×0 + 1×1+3×0+2×1 = 0+0+3+0+0+0+1+0+2 = 6
O[1,1] = 1×1+3×0+2×1 + 0×0+1×1+0×0 + 3×1+2×0+1×1 = 1+0+2+0+1+0+3+0+1 = 8

Output: [5  6]
        [6  8]  ✅
```

[↑ Back to Top](#-deep-learning-numerical)

---

## P3: MaxPool Computation

```
Input (4×4):       MaxPool 2×2, stride=2:
[3  1  |  2  4]
[2  5  |  7  1]    → [max(3,1,2,5)  max(2,4,7,1)] = [5  7]
───────┼────────
[8  0  |  3  2]    → [max(8,0,6,1)  max(3,2,4,5)] = [8  5]
[6  1  |  4  5]

Output: [5  7]
        [8  5]

AvgPool same window: [(3+1+2+5)/4  (2+4+7+1)/4] = [2.75  3.50]
                     [(8+0+6+1)/4  (3+2+4+5)/4]   [3.75  3.50]
```

[↑ Back to Top](#-deep-learning-numerical)

---

## P4: Autoencoder Reconstruction Error

```
Original:       x = [0.8, 0.2, 0.9, 0.1, 0.7]
Reconstructed: x̂ = [0.7, 0.3, 0.8, 0.2, 0.6]

L = Σ(xᵢ - x̂ᵢ)²
  = (0.1)² + (-0.1)² + (0.1)² + (-0.1)² + (0.1)²
  = 0.01 × 5 = 0.05

LOW loss → good reconstruction!

Anomaly test: x_anom = [0.1, 0.9, 0.1, 0.9, 0.1]  (unusual pattern)
  x̂_anom = [0.6, 0.4, 0.7, 0.3, 0.5]  (AE can't reconstruct unusual data well)
  L = (0.5)²+(0.5)²+(0.6)²+(0.6)²+(0.4)² = 0.25+0.25+0.36+0.36+0.16 = 1.38

HIGH loss → ANOMALY detected! ✅
```

---

> **Nav:** [📖 THEORY](ml_dl_cnn_ae_theory.md) | 🔢 NUMERICAL | [💻 PRACTICE →](ml_dl_cnn_ae_practice.md)

[↑ Back to Top](#-deep-learning-numerical)

*AI · ML · github.com/rpaut03l/TS-01*
