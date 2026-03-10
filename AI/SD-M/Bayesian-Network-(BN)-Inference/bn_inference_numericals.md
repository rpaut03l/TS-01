# 🔢 Bayesian Network Inference — NUMERICALS
### Artificial Intelligence AI 
### Book: Norvig | Unit: Probabilistic Reasoning — Part 2

> **Navigation:** [📋 INDEX](./bn_inference_index.md) | [← THEORY](./bn_inference_theory.md) | 🔢 **NUMERICALS** *(you are here)* | [💻 PRACTICE →](./bn_inference_practice.md)

---

## 📚 Table of Contents

| # | Problem | Answer |
|---|---------|--------|
| P1 | [α Normalisation — Slide Example](#p1--normalisation--slide-example) | P(x=T\|e)=0.4615, P(x=F\|e)=0.5385 |
| P2 | [Full Posterior P(Burglary\|John=T,Mary=T)](#p2--full-posterior-pburglary--johnt-maryt) | P(B=T\|j,m)=0.284 |
| P3 | [Variable Elimination for P(B\|j,m)](#p3--variable-elimination-for-pbjm) | Same answer, 56% fewer ops |
| P4 | [P(JohnCalls=T, Earthquake=T)](#p4--pjohncallst-earthquaket) | 0.000594 |
| P5 | [P(MaryCalls=F, Alarm=T, Earthquake=T)](#p5--pmarycallsf-alarmt-earthquaket) | 0.000174 |
| P6 | [P(JohnCalls=T)](#p6--pjohncallst) | 0.0521 = 5.21% |
| P7 | [P(MaryCalls=F)](#p7--pmarycallsf) | 0.9883 = 98.83% |
| P8 | [Joint Probability P(j,m,a,¬b,¬e)](#p8--joint-probability-pjmanb-ne) | 0.000628 |
| — | [All Answers Summary Table](#all-answers-summary-table) | All 8 problems |
| — | [Pre-Exam Checklist](#pre-exam-checklist) | Step-by-step guide |

---

## P1 — α Normalisation — Slide Example

> [🔝 Top](#-table-of-contents) · [Next P2 →](#p2--full-posterior-pburglary--johnt-maryt)

**Given:** P(x=T, e) = 0.192 and P(x=F, e) = 0.224
**Find:** The normalised posterior P(X|e) and the value of α

### Working

```
STEP 1 — Write as unnormalised vector:
  P(X|e) = α × [0.192]
                [0.224]

STEP 2 — Probabilities MUST sum to 1 (always!):
  α × 0.192 + α × 0.224 = 1
  α × (0.192 + 0.224)   = 1
  α × 0.416             = 1
  α = 1/0.416 = 2.4038

STEP 3 — Compute final values:
  P(x=T|e) = 0.192 / 0.416 = 0.4615  (46.15%)
  P(x=F|e) = 0.224 / 0.416 = 0.5385  (53.85%)

STEP 4 — Verify:
  0.4615 + 0.5385 = 1.0000 ✅

COMPLEMENT CHECK:
  P(x=F|e) via complement = 1 - 0.4615 = 0.5385 ✅  (matches!)
```

### Answer

```
α = 1/0.416 = 2.4038
P(x=T|e) = 0.4615
P(x=F|e) = 0.5385
```

---

## P2 — Full Posterior P(Burglary | John=T, Mary=T)

> [← P1](#p1--normalisation--slide-example) · [🔝 Top](#-table-of-contents) · [Next P3 →](#p3--variable-elimination-for-pbjm)

**Question:** Both John and Mary called. What's the probability of a burglary?

### Step 0 — Classify Variables

```
X (query)    = Burglary (B)           ← what we WANT
e (evidence) = {JohnCalls=T, MaryCalls=T}  ← what we KNOW
Y (hidden)   = {Alarm (A), Earthquake (E)} ← SUM OVER THESE!
```

### Step 1 — Write the Formula

```
P(B | j, m) = α × P(B, j, m)

P(B, j, m) = Σ    P(j|a) × P(m|a) × P(a|b,e) × P(b) × P(e)
              a,e

P(b) pulled outside immediately (constant to both a and e sums):
= P(b) × Σ    P(j|a) × P(m|a) × P(a|b,e) × P(e)
           a,e
```

### Step 2 — Shortcuts to memorise

```
When a=T: P(j=T|A=T) × P(m=T|A=T) = 0.90 × 0.70 = 0.63
When a=F: P(j=T|A=F) × P(m=T|A=F) = 0.05 × 0.01 = 0.0005
```

---

### Computing P(B=T, j, m)  [Burglar Case]

```
P(B=T) = 0.001   [pulled outside]
Alarm CPT column to use: P(A|B=T, e)
```

```
┌────┬────┬──────┬──────┬─────────────────┬────────┬──────────────┐
│ a  │ e  │P(j|a)│P(m|a)│ P(a=T | B=T, e) │  P(e)  │  Product     │
│    │    │      │      │ or P(a=F | B=T,e)│       │              │
├────┼────┼──────┼──────┼─────────────────┼────────┼──────────────┤
│ T  │ T  │ 0.90 │ 0.70 │ 0.950           │ 0.002  │              │
│    │    │ 0.63 × 0.950 × 0.002                = 0.001197000     │
├────┼────┼──────┼──────┼─────────────────┼────────┼──────────────┤
│ T  │ F  │ 0.90 │ 0.70 │ 0.940           │ 0.998  │              │
│    │    │ 0.63 × 0.940 × 0.998                = 0.591016000     │
├────┼────┼──────┼──────┼─────────────────┼────────┼──────────────┤
│ F  │ T  │ 0.05 │ 0.01 │ 0.050           │ 0.002  │              │
│    │    │ 0.0005 × 0.050 × 0.002              = 0.000000050     │
├────┼────┼──────┼──────┼─────────────────┼────────┼──────────────┤
│ F  │ F  │ 0.05 │ 0.01 │ 0.060           │ 0.998  │              │
│    │    │ 0.0005 × 0.060 × 0.998              = 0.000029940     │
└────┴────┴──────┴──────┴─────────────────┴────────┴──────────────┘

Inner sum = 0.001197000 + 0.591016000 + 0.000000050 + 0.000029940
          = 0.592242990

P(B=T, j, m) = 0.001 × 0.592242990 = 0.000592243
```

---

### Computing P(B=F, j, m)  [No Burglar Case]

```
P(B=F) = 0.999   [pulled outside]
Alarm CPT column to use: P(A|B=F, e)
```

```
┌────┬────┬──────┬──────┬─────────────────┬────────┬──────────────┐
│ a  │ e  │P(j|a)│P(m|a)│ P(a | B=F, e)   │  P(e)  │  Product     │
├────┼────┼──────┼──────┼─────────────────┼────────┼──────────────┤
│ T  │ T  │ 0.90 │ 0.70 │ 0.290           │ 0.002  │              │
│    │    │ 0.63 × 0.290 × 0.002                = 0.000365400     │
├────┼────┼──────┼──────┼─────────────────┼────────┼──────────────┤
│ T  │ F  │ 0.90 │ 0.70 │ 0.001           │ 0.998  │              │
│    │    │ 0.63 × 0.001 × 0.998                = 0.000628740     │
├────┼────┼──────┼──────┼─────────────────┼────────┼──────────────┤
│ F  │ T  │ 0.05 │ 0.01 │ 0.710           │ 0.002  │              │
│    │    │ 0.0005 × 0.710 × 0.002              = 0.000000710     │
├────┼────┼──────┼──────┼─────────────────┼────────┼──────────────┤
│ F  │ F  │ 0.05 │ 0.01 │ 0.999           │ 0.998  │              │
│    │    │ 0.0005 × 0.999 × 0.998              = 0.000498501     │
└────┴────┴──────┴──────┴─────────────────┴────────┴──────────────┘

Inner sum = 0.000365400 + 0.000628740 + 0.000000710 + 0.000498501
          = 0.001493351

P(B=F, j, m) = 0.999 × 0.001493351 = 0.001491858
```

---

### Step 3 — Normalise with α

```
Unnormalised values:
  P(B=T, j, m) = 0.000592243
  P(B=F, j, m) = 0.001491858
  ─────────────────────────
  Total         = 0.002084101

α = 1 / 0.002084101

P(B=T | j, m) = 0.000592243 / 0.002084101 = 0.2840
P(B=F | j, m) = 0.001491858 / 0.002084101 = 0.7160

VERIFY: 0.2840 + 0.7160 = 1.0000 ✅
```

### Final Answer + Insight

```
╔══════════════════════════════════════════════════════════╗
║  P(Burglary=T | John=T, Mary=T) = 0.2840 = 28.40%       ║
║  P(Burglary=F | John=T, Mary=T) = 0.7160 = 71.60%       ║
╠══════════════════════════════════════════════════════════╣
║  Before evidence:  P(Burglary) = 0.001 = 0.10%          ║
║  After  evidence:  P(Burglary) = 0.284 = 28.4%          ║
║  Belief jumped 284× higher!                              ║
║  BUT: still only 28.4% — rare events stay rare! 😅       ║
╚══════════════════════════════════════════════════════════╝
```

---

## P3 — Variable Elimination for P(B|j,m)

> [← P2](#p2--full-posterior-pburglary--johnt-maryt) · [🔝 Top](#-table-of-contents) · [Next P4 →](#p4--pjohncallst-earthquaket)

**Same query as P2 — showing VE is smarter**

### Step 1 — Reorganise Formula

```
BEFORE:
Σ    P(j|a)·P(m|a)·P(a|b,e)·P(b)·P(e)
a,e

AFTER (apply Golden Rules):
P(b) × Σ  P(e) × [Σ  P(a|b,e)·P(j|a)·P(m|a)]
          e          a
                     └───────────────────────┘
                           = f(b,e)  📝 saved factor!

WHY:
• P(b) has no 'a' and no 'e' → exits BOTH sums
• P(e) has no 'a' → exits the inner 'a' sum
• f(b,e) = inner sum computed ONCE per (b,e) combo
```

### Step 2 — Compute All 4 Factors

```
f(b,e) = Σ P(a|b,e)×P(j=T|a)×P(m=T|a)
          a
Using shortcuts: a=T multiplier = 0.63, a=F multiplier = 0.0005

┌───────┬───────┬────────────────────────────────────────────┬──────────┐
│  b    │  e    │  Calculation                               │  f(b,e)  │
├───────┼───────┼────────────────────────────────────────────┼──────────┤
│  T    │  T    │  P(A=T|T,T)×0.63 + P(A=F|T,T)×0.0005       │          │
│       │       │  = 0.950×0.63 + 0.050×0.0005               │          │
│       │       │  = 0.59850 + 0.000025                      │ 0.598525 │
├───────┼───────┼────────────────────────────────────────────┼──────────┤
│  T    │  F    │  0.940×0.63 + 0.060×0.0005                 │          │
│       │       │  = 0.59220 + 0.000030                      │ 0.592230 │
├───────┼───────┼────────────────────────────────────────────┼──────────┤
│  F    │  T    │  P(A=T|F,T)×0.63 + P(A=F|F,T)×0.0005       │          │
│       │       │  = 0.290×0.63 + 0.710×0.0005               │          │
│       │       │  = 0.18270 + 0.000355                      │ 0.183055 │
├───────┼───────┼────────────────────────────────────────────┼──────────┤
│  F    │  F    │  0.001×0.63 + 0.999×0.0005                 │          │
│       │       │  = 0.000630 + 0.000500                     │ 0.001130 │
└───────┴───────┴────────────────────────────────────────────┴──────────┘
📝 These 4 factors are now SAVED and REUSED below for both B=T and B=F!
```

### Step 3 — Outer e-Sum using Saved Factors

```
For B=T:
Σ P(e) × f(T, e)
 e
= P(E=T) × f(T,T)  +  P(E=F) × f(T,F)
= 0.002   × 0.598525  +  0.998 × 0.592230
= 0.001197050         +  0.591045540
= 0.592242590

For B=F:
Σ P(e) × f(F, e)
 e
= P(E=T) × f(F,T)  +  P(E=F) × f(F,F)
= 0.002   × 0.183055  +  0.998 × 0.001130
= 0.000366110         +  0.001127740
= 0.001493850
```

### Step 4 — Multiply by P(b) and Normalise

```
P(B=T, j, m) = P(B=T) × e-sum = 0.001 × 0.592242590 = 0.000592243
P(B=F, j, m) = P(B=F) × e-sum = 0.999 × 0.001493850 = 0.001492357

Total = 0.002084600
α     = 1 / 0.002084600

P(B=T | j, m) = 0.2840 ✅  (same as P2 Enumeration!)
P(B=F | j, m) = 0.7160 ✅
```

### Operations Comparison

```
Enumeration:         32 multiplications
Variable Elimination: 14 multiplications  (8 factors + 4 e-sum + 2 P(b))
Saved:               18 ops = 56% fewer! ⚡
```

---

## P4 — P(JohnCalls=T, Earthquake=T)

> [← P3](#p3--variable-elimination-for-pbjm) · [🔝 Top](#-table-of-contents) · [Next P5 →](#p5--pmarycallsf-alarmt-earthquaket)

**Question:** What's the joint probability that John calls AND an earthquake happens?

### Setup

```
Both J=T and E=T are EVENTS (not query vs evidence).
Hidden: Alarm (A), Burglary (B)
P(E=T) = 0.002 → pulled outside (constant!)

P(J=T, E=T) = P(E=T) × Σ   P(J=T|a) × P(a|b, E=T) × P(b)
                         a,b
            = 0.002   × [inner sum over 4 worlds]
```

### 4 Worlds

```
┌────┬────┬──────────────┬────────────────┬────────┬──────────────┐
│ a  │ b  │  P(J=T | a)  │  P(a|b, E=T)   │  P(b)  │  Product     │
├────┼────┼──────────────┼────────────────┼────────┼──────────────┤
│ T  │ T  │    0.90      │     0.950      │ 0.001  │ 0.000855000  │
│ T  │ F  │    0.90      │     0.290      │ 0.999  │ 0.260739000  │
│ F  │ T  │    0.05      │     0.050      │ 0.001  │ 0.000002500  │
│ F  │ F  │    0.05      │     0.710      │ 0.999  │ 0.035464500  │
└────┴────┴──────────────┴────────────────┴────────┴──────────────┘
                                                Sum = 0.297061000
```

### Final Answer

```
P(J=T, E=T) = 0.002 × 0.297061 = 0.000594122
```

---

## P5 — P(MaryCalls=F, Alarm=T, Earthquake=T)

> [← P4](#p4--pjohncallst-earthquaket) · [🔝 Top](#-table-of-contents) · [Next P6 →](#p6--pjohncallst)

**Question:** Mary silent, alarm ringing, earthquake happening — all at once?

### Key Insight — A and E are Fixed!

```
M=F, A=T, E=T are all FIXED (given values, not summed over).
Only hidden variable: Burglary (B) — just 2 worlds!

Constants that factor out immediately:
  P(M=F | A=T) = 1 - 0.70 = 0.30
  P(E=T)       = 0.002

Combined constant = 0.30 × 0.002 = 0.0006

P(M=F, A=T, E=T) = 0.0006 × Σ  P(A=T | b, E=T) × P(b)
                               b
```

### 2 Worlds (only B is hidden)

```
┌────┬──────────────────────┬────────┬──────────────┐
│ b  │  P(A=T | b, E=T)     │  P(b)  │  Product     │
├────┼──────────────────────┼────────┼──────────────┤
│ T  │       0.950          │ 0.001  │  0.000950    │
│ F  │       0.290          │ 0.999  │  0.289710    │
└────┴──────────────────────┴────────┴──────────────┘
                                  Sum = 0.290660
```

### Final Answer

```
P(M=F, A=T, E=T) = 0.0006 × 0.290660 = 0.000174396
```

---

## P6 — P(JohnCalls=T)

> [← P5](#p5--pmarycallsf-alarmt-earthquaket) · [🔝 Top](#-table-of-contents) · [Next P7 →](#p7--pmarycallsf)

**Question:** No evidence. What's the base-rate chance John calls today?

### Compute P(Alarm=T) First — Inner Sum

```
P(A=T) = Σ   P(A=T | b, e) × P(b) × P(e)
          b,e

┌────┬────┬────────────────┬────────┬────────┬──────────────┐
│ b  │ e  │ P(A=T | b, e)  │  P(b)  │  P(e)  │  Product     │
├────┼────┼────────────────┼────────┼────────┼──────────────┤
│ T  │ T  │     0.950      │ 0.001  │ 0.002  │ 0.00000190   │
│ T  │ F  │     0.940      │ 0.001  │ 0.998  │ 0.00093812   │
│ F  │ T  │     0.290      │ 0.999  │ 0.002  │ 0.00057942   │
│ F  │ F  │     0.001      │ 0.999  │ 0.998  │ 0.00099700   │
└────┴────┴────────────────┴────────┴────────┴──────────────┘
P(A=T) = 0.00251644
P(A=F) = 1 - 0.00251644 = 0.99748356
```

### Compute P(JohnCalls=T)

```
P(J=T) = P(J=T|A=T) × P(A=T)  +  P(J=T|A=F) × P(A=F)
       =    0.90    × 0.00251644  +    0.05   × 0.99748356
       = 0.00226480               + 0.04987418
       = 0.05213898
```

**Answer: P(JohnCalls=T) = 0.0521 = 5.21%**

```
Note: most of John's calls (4.99% / 5.21% = 95.7%) are him calling
randomly without an alarm! Only 0.23% are due to actual alarms. 😅
```

---

## P7 — P(MaryCalls=F)

> [← P6](#p6--pjohncallst) · [🔝 Top](#-table-of-contents) · [Next P8 →](#p8--joint-probability-pjmanb-ne)

**Question:** No evidence. What's the base-rate chance Mary stays silent?

### Reuse P(Alarm) from P6 ♻️

```
P(A=T) = 0.00251644   ← computed in P6, reuse!
P(A=F) = 0.99748356
```

### Mary's CPT Values

```
P(M=F | A=T) = 1 - 0.70 = 0.30
P(M=F | A=F) = 1 - 0.01 = 0.99
```

### Compute P(MaryCalls=F)

```
P(M=F) = P(M=F|A=T) × P(A=T)  +  P(M=F|A=F) × P(A=F)
       =    0.30    × 0.00251644  +    0.99   × 0.99748356
       = 0.00075493               + 0.98750872
       = 0.98826365
```

**Answer: P(MaryCalls=F) = 0.9883 = 98.83%**

```
VERIFY:
P(M=T) = P(M=T|A=T)×P(A=T) + P(M=T|A=F)×P(A=F)
       = 0.70×0.00251644 + 0.01×0.99748356
       = 0.00176151 + 0.00997484 = 0.01173635

P(M=T) + P(M=F) = 0.01173635 + 0.98826365 = 1.00000000 ✅
```

---

## P8 — Joint Probability P(j,m,a,¬b,¬e)

> [← P7](#p7--pmarycallsf) · [🔝 Top](#-table-of-contents) · [Next →](#all-answers-summary-table)

**Question:** Alarm rang, John called, Mary called, NO burglar, NO earthquake. How likely is this whole scenario?

### Direct CPT Lookup — No Summation Needed!

```
All variables are FIXED (no hidden) → just multiply all CPT values!

P(j,m,a,¬b,¬e) = P(j=T|a=T) × P(m=T|a=T) × P(a=T|b=F,e=F) × P(b=F) × P(e=F)
```

### Values Lookup

```
P(j=T | a=T)        = 0.90   [John CPT, row A=T]
P(m=T | a=T)        = 0.70   [Mary CPT, row A=T]
P(a=T | b=F, e=F)   = 0.001  [Alarm CPT, row B=F,E=F — false alarm!]
P(b=F)              = 0.999  [Burglary CPT, complement]
P(e=F)              = 0.998  [Earthquake CPT, complement]
```

### Calculation

```
= 0.90 × 0.70 × 0.001 × 0.999 × 0.998
= 0.63 × 0.001 × 0.999 × 0.998
= 0.00063 × 0.999 × 0.998
= 0.00063 × 0.997002
= 0.000628
```

**Answer: P(j,m,a,¬b,¬e) = 0.000628 ≈ 0.063%**

```
Interpretation: This world (alarm+john+mary+no-burglar+no-quake)
happens about 6 times out of every 10,000 days.
It's a "false alarm" scenario — alarm triggered randomly!
```

---

## All Answers Summary Table

> [🔝 Top](#-table-of-contents) · [Next →](#pre-exam-checklist)

```
┌────┬──────────────────────────────────────────────────────────────┬─────────────────┐
│ P# │ Query                                                        │  Answer         │
├────┼──────────────────────────────────────────────────────────────┼─────────────────┤
│ P1 │ P(x=T|e) given unnorm {0.192, 0.224}                         │ 0.4615          │
│    │ P(x=F|e) given unnorm {0.192, 0.224}                         │ 0.5385          │
│    │ α                                                            │ 2.4038          │
├────┼──────────────────────────────────────────────────────────────┼─────────────────┤
│ P2 │ P(Burglary=T | John=T, Mary=T)  [Enumeration]                │0.2840 = 28.4%   │
│    │ P(Burglary=F | John=T, Mary=T)                               │ 0.7160 = 71.6%  │
├────┼──────────────────────────────────────────────────────────────┼─────────────────┤
│ P3 │ P(B|j,m) via Variable Elimination                            │ 0.2840 / 0.7160 │
│    │ Operations saved vs Enumeration                              │ 18 ops = 56%    │
├────┼──────────────────────────────────────────────────────────────┼─────────────────┤
│ P4 │ P(JohnCalls=T, Earthquake=T)                                 │ 0.000594122     │
├────┼──────────────────────────────────────────────────────────────┼─────────────────┤
│ P5 │ P(MaryCalls=F, Alarm=T, Earthquake=T)                        │ 0.000174396     │
├────┼──────────────────────────────────────────────────────────────┼─────────────────┤
│ P6 │ P(JohnCalls=T)  [base rate, no evidence]                     │ 0.0521 = 5.21%  │
├────┼──────────────────────────────────────────────────────────────┼─────────────────┤
│ P7 │ P(MaryCalls=F)  [base rate, no evidence]                     │ 0.9883 = 98.83% │
├────┼──────────────────────────────────────────────────────────────┼─────────────────┤
│ P8 │ P(j=T, m=T, a=T, b=F, e=F)  [joint, all fixed]               │ 0.000628        │
└────┴──────────────────────────────────────────────────────────────┴─────────────────┘
```

---

## Pre-Exam Checklist

> [← Summary](#all-answers-summary-table) · [🔝 Top](#-table-of-contents)

```
Before writing ANY Bayesian inference answer:

□  Step 1:  Write down X (query), e (evidence), Y (hidden)
□  Step 2:  Decide: posterior P(X|e) or joint P(X,e)?
            Posterior → needs α normalisation!
            Joint     → direct multiplication only!
□  Step 3:  Write P(X,e) = Σ P(X,e,y) over all hidden Y
□  Step 4:  Expand joint using BN chain rule
□  Step 5:  Pull P(b) outside FIRST (constant to all sums)
□  Step 6:  Check independence: no arrow → multiply directly
□  Step 7:  For VE: draw dependency table, identify what exits each sum
□  Step 8:  Fill in CPT table row by row — one world at a time
□  Step 9:  Sum all worlds to get unnormalised value
□  Step 10: Repeat for other query value (B=T vs B=F)
□  Step 11: α = 1/(sum of both unnorm values)
□  Step 12: Divide each by total → normalised P(X|e)
□  Step 13: VERIFY: all probabilities sum to 1.0 ✅
□  Step 14: Sanity check: if prior is tiny, posterior should stay small
```

---

> **Navigation:** [📋 INDEX](./bn_inference_index.md) | [← THEORY](./bn_inference_theory.md) | 🔢 **NUMERICALS** *(you are here)* | [💻 PRACTICE →](./bn_inference_practice.md)
>
> **Source:** Book: Norvig - AI
[🔝 Back to Top](#-bayesian-network-inference--numericals)
