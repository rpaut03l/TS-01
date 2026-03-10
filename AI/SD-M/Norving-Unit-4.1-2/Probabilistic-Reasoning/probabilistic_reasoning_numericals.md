# 🔢 Probabilistic Reasoning — NUMERICALS Guide
### Artificial Intelligence · AI 
### All Solved Problems from Units 4.1 + 4.2

---

> **Navigation:** [📋 INDEX](./probabilistic_reasoning_index.md) | [📘 THEORY](./probabilistic_reasoning_theory.md) | [🧠 BN Inference: More Problems](https://github.com/rpaut03l/TS-01/blob/ai-sdm-probabilistic-reasoning/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_numericals.md) | [🏋️ BN Practice](https://github.com/rpaut03l/TS-01/blob/ai-sdm-probabilistic-reasoning/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_practice.md)

---

## 📚 Problem Index

| # | Problem | Difficulty | Theory Link |
|---|---------|-----------|-------------|
| 1 | [Weather-Traffic Axioms](#problem-1-weather-traffic-axioms) | ⭐ Easy | [Axioms](./probabilistic_reasoning_theory.md#3-probability-axioms--rules) |
| 2 | [Toothache-Cavity-Catch Joint Table](#problem-2-toothache-cavity-catch-joint-table) | ⭐ Easy | [Joint Dist](./probabilistic_reasoning_theory.md#5-inference-using-full-joint-distribution) |
| 3 | [Produce-Weather Conditioning](#problem-3-produce-weather-conditioning) | ⭐ Easy | [Conditioning](./probabilistic_reasoning_theory.md#5-inference-using-full-joint-distribution) |
| 4 | [Burglary-Alarm BN Construction](#problem-4-burglary-alarm-bn-construction) | ⭐⭐ Medium | [BN Syntax](./probabilistic_reasoning_theory.md#9-bayesian-networks--syntax) |
| 5 | [P(JohnCalls = true)](#problem-5-pjohncalls--true) | ⭐⭐ Medium | [BN Inference](./probabilistic_reasoning_theory.md#12-obtaining-full-joint-from-bn) |
| 6 | [P(MaryCalls = false)](#problem-6-pmarycalls--false) | ⭐⭐ Medium | [BN Inference](./probabilistic_reasoning_theory.md#12-obtaining-full-joint-from-bn) |
| 7 | [Joint entry P(j,m,a,¬b,¬e)](#problem-7-joint-entry-pjma¬b¬e) | ⭐⭐ Medium | [Joint from BN](./probabilistic_reasoning_theory.md#12-obtaining-full-joint-from-bn) |
| 8 | [P(Burglary\|j,m) — Enumeration](#problem-8-pburglary--jm--enumeration) | ⭐⭐⭐ Hard | [Enumeration](./probabilistic_reasoning_theory.md#15-exact-inference--enumeration) |
| 9 | [P(B\|j,m) — Variable Elimination](#problem-9-pb--jm--variable-elimination) | ⭐⭐⭐ Hard | [Var Elim](./probabilistic_reasoning_theory.md#16-exact-inference--variable-elimination) |
| 10 | [HW: P(j,e) and P(¬m,a,e)](#problem-10-homework-problems) | ⭐⭐ Medium | [BN Inference](./probabilistic_reasoning_theory.md#12-obtaining-full-joint-from-bn) |
| 11 | [P(Cavity\|toothache ∨ catch)](#problem-11-pcavity--toothache--catch) | ⭐⭐⭐ Hard | [Normalization](./probabilistic_reasoning_theory.md#14-normalization-constant-α) |

---

## Reference Data Used Across Problems

### Weather-Traffic Tables

```
  P(Weather):                    P(Traffic):
  ┌─────────┬───────┐           ┌───────┬────────┐
  │ sunny   │ 0.6   │           │ more  │ 0.2999 │
  │ rainy   │ 0.1   │           │ less  │ 0.7001 │
  │ cloudy  │ 0.29  │           └───────┴────────┘
  │ snowy   │ 0.01  │
  └─────────┴───────┘

  P(Weather, Traffic):
  ┌─────────┬───────┬────────┐
  │ sunny   │ more  │ 0.05   │
  │ sunny   │ less  │ 0.55   │
  │ rainy   │ more  │ 0.095  │
  │ rainy   │ less  │ 0.005  │
  │ cloudy  │ more  │ 0.145  │
  │ cloudy  │ less  │ 0.145  │
  │ snowy   │ more  │ 0.0099 │
  │ snowy   │ less  │ 0.0001 │
  └─────────┴───────┴────────┘
```

### Burglary Network & CPTs

```
              P(B)=0.001          P(E)=0.002
             ┌───────┐           ┌───────┐
             │Burglary│           │Earthqu.│
             └───┬────┘           └───┬────┘
                 └────────┬───────────┘
                          ▼
                    ┌──────────┐
                    │  Alarm   │
                    └────┬─────┘
                    ╱         ╲
                   ▼           ▼
            ┌──────────┐  ┌──────────┐
            │JohnCalls │  │MaryCalls │
            └──────────┘  └──────────┘

  P(A|B,E):                         P(J|A):           P(M|A):
  ┌───┬───┬──────┬───────┐         ┌───┬──────┬─────┐ ┌───┬──────┬─────┐
  │ B │ E │ P(a) │ P(¬a) │         │ A │ P(j) │P(¬j)│ │ A │ P(m) │P(¬m)│
  ├───┼───┼──────┼───────┤         ├───┼──────┼─────┤ ├───┼──────┼─────┤
  │ t │ t │ 0.95 │ 0.05  │         │ t │ 0.90 │0.10 │ │ t │ 0.70 │0.30 │
  │ t │ f │ 0.94 │ 0.06  │         │ f │ 0.05 │0.95 │ │ f │ 0.01 │0.99 │
  │ f │ t │ 0.29 │ 0.71  │         └───┴──────┴─────┘ └───┴──────┴─────┘
  │ f │ f │ 0.001│ 0.999 │
  └───┴───┴──────┴───────┘
```

---

## Problem 1: Weather-Traffic Axioms

> ⭐ Easy | [Theory: Axioms](./probabilistic_reasoning_theory.md#3-probability-axioms--rules) | [Next →](#problem-2-toothache-cavity-catch-joint-table)

### Q1: Calculate P(rainy ∨ more Traffic)

```
  FORMULA: P(a ∨ b) = P(a) + P(b) - P(a ∧ b)
                       ╰inclusion-exclusion principle╯

  Step 1: Identify values
  P(rainy) = 0.1
  P(more)  = 0.2999
  P(rainy ∧ more) = P(rainy, more) = 0.095  (from joint table)

  Step 2: Apply formula
  P(rainy ∨ more) = 0.1 + 0.2999 - 0.095
                   = 0.3049

  ANSWER: P(rainy ∨ more Traffic) = 0.3049
```

### Q2: P(less | sunny) — Conditional probability

```
  FORMULA: P(a | b) = P(a ∧ b) / P(b)

  Step 1: Get values from tables
  P(less ∧ sunny) = P(sunny, less) = 0.55   (from joint table)
  P(sunny) = 0.6                              (from weather table)

  Step 2: Apply formula
  P(less | sunny) = 0.55 / 0.6
                   = 0.9167

  ANSWER: P(less traffic | sunny) = 0.9167 ≈ 91.67%

  MAKES SENSE? Yes! Sunny weather → most people don't rush → less traffic.
```

### Q3: P(less | ¬sunny) — Using complement intersection

```
  FORMULA: P(a ∧ ¬b) = P(a) - P(a ∧ b)

  Step 1: Find P(less ∧ ¬sunny)
  P(less ∧ ¬sunny) = P(less) - P(less ∧ sunny)
                    = 0.7001 - 0.55
                    = 0.1501

  Step 2: Find P(¬sunny)
  P(¬sunny) = 1 - P(sunny) = 1 - 0.6 = 0.4

  Step 3: Apply conditional formula
  P(less | ¬sunny) = P(less ∧ ¬sunny) / P(¬sunny)
                    = 0.1501 / 0.4
                    = 0.37525

  ANSWER: P(less traffic | not sunny) = 0.37525

  MAKES SENSE? Yes! Bad weather → more traffic → LESS chance of "less traffic."
```

### Q4: Joint distribution P(snowy, Traffic)

```
  P(snowy, Traffic) means: list P for EVERY Traffic value when Weather=snowy.

  From the joint table:
  P(snowy, more) = 0.0099
  P(snowy, less) = 0.0001

  ANSWER: P(snowy, Traffic) = [0.0099, 0.0001]

  CHECK: 0.0099 + 0.0001 = 0.01 = P(snowy) ✓
```

> [🔝 Top](#-problem-index) | [Next →](#problem-2-toothache-cavity-catch-joint-table)

---

## Problem 2: Toothache-Cavity-Catch Joint Table

> ⭐ Easy | [Theory: Joint Distribution](./probabilistic_reasoning_theory.md#5-inference-using-full-joint-distribution) | [← Prev](#problem-1-weather-traffic-axioms) | [Next →](#problem-3-produce-weather-conditioning)

### Given: Full Joint Distribution

```
  ┌──────────┬───────────┬────────┬────────┐
  │          │           │ catch  │ ¬catch  │
  ├──────────┼───────────┼────────┼────────┤
  │ cavity   │ toothache │ 0.108  │ 0.012  │
  │ cavity   │¬toothache │ 0.072  │ 0.008  │
  │ ¬cavity  │ toothache │ 0.016  │ 0.064  │
  │ ¬cavity  │¬toothache │ 0.144  │ 0.576  │
  └──────────┴───────────┴────────┴────────┘
```

### Q1: P(cavity) — Marginalization

```
  Sum all rows where cavity = true:
  P(cavity) = 0.108 + 0.012 + 0.072 + 0.008 = 0.2

  ANSWER: P(cavity) = 0.2
```

### Q2: P(toothache) — Marginalization

```
  Sum all rows where toothache = true:
  P(toothache) = 0.108 + 0.012 + 0.016 + 0.064 = 0.2

  ANSWER: P(toothache) = 0.2
```

### Q3: P(¬catch) — Marginalization

```
  Sum all rows where catch = false:
  P(¬catch) = 0.012 + 0.008 + 0.064 + 0.576 = 0.66

  ANSWER: P(¬catch) = 0.66
```

### Q4: P(cavity ∨ toothache) — Inclusion-Exclusion

```
  P(cavity ∨ toothache) = P(cavity) + P(toothache) - P(cavity ∧ toothache)

  P(cavity ∧ toothache) = 0.108 + 0.012 = 0.12

  = 0.2 + 0.2 - 0.12 = 0.28

  ANSWER: P(cavity ∨ toothache) = 0.28
```

### Q5: P(¬cavity | toothache) — Conditional

```
  P(¬cavity | toothache) = P(¬cavity ∧ toothache) / P(toothache)

  P(¬cavity ∧ toothache) = 0.016 + 0.064 = 0.08

  = 0.08 / 0.2 = 0.4

  ANSWER: P(¬cavity | toothache) = 0.4

  So P(cavity | toothache) = 1 - 0.4 = 0.6
```

> [🔝 Top](#-problem-index) | [Next →](#problem-3-produce-weather-conditioning)

---

## Problem 3: Produce-Weather Conditioning

> ⭐ Easy | [Theory: Conditioning](./probabilistic_reasoning_theory.md#5-inference-using-full-joint-distribution) | [← Prev](#problem-2-toothache-cavity-catch-joint-table) | [Next →](#problem-4-burglary-alarm-bn-construction)

### Given

```
  P(non-favourable weather) = 0.26
  P(favourable weather) = 0.74

  ┌──────────────┬──────────────┬──────────────┐
  │ P(Produce|W) │ Non-Fav      │ Favourable   │
  ├──────────────┼──────────────┼──────────────┤
  │ Poor         │ 0.6923       │ 0.0270       │
  │ Good         │ 0.3077       │ 0.9730       │
  └──────────────┴──────────────┴──────────────┘

  FIND: P(good produce)
```

### Solution — Using Conditioning Formula

```
  FORMULA: P(X) = Σ_y P(X|y) · P(y)

  P(good) = Σ_{w ∈ Weather} P(good | w) · P(w)

  = P(good | non-fav) × P(non-fav) + P(good | fav) × P(fav)

  = 0.3077 × 0.26 + 0.9730 × 0.74

  = 0.080002 + 0.72002

  = 0.8

  ANSWER: P(good produce) = 0.8 = 80%

  MAKES SENSE? Most of the time weather is favourable (74%) and
  good produce in fav weather is 97.3%, so overall good produce is high.
```

> [🔝 Top](#-problem-index) | [Next →](#problem-4-burglary-alarm-bn-construction)

---

## Problem 4: Burglary-Alarm BN Construction

> ⭐⭐ Medium | [Theory: BN Syntax](./probabilistic_reasoning_theory.md#9-bayesian-networks--syntax) | [← Prev](#problem-3-produce-weather-conditioning) | [Next →](#problem-5-pjohncalls--true)

### Step-by-Step BN Construction

```
  STEP 1: Read the story and identify VARIABLES
  ┌──────────────────────────────────────────────────────┐
  │ "Burglar alarm detects burglary but also responds   │
  │  to minor earthquakes. John and Mary call when      │
  │  they hear the alarm."                              │
  │                                                      │
  │ Variables: Burglary, Earthquake, Alarm,              │
  │            JohnCalls, MaryCalls                      │
  └──────────────────────────────────────────────────────┘

  STEP 2: Identify CAUSE → EFFECT (arrows)
  ┌──────────────────────────────────────────────────────┐
  │ Q: What CAUSES Burglary?   → Nothing (root node)   │
  │ Q: What CAUSES Earthquake? → Nothing (root node)   │
  │ Q: What CAUSES Alarm?      → Burglary, Earthquake  │
  │ Q: What CAUSES JohnCalls?  → Alarm                 │
  │ Q: What CAUSES MaryCalls?  → Alarm                 │
  └──────────────────────────────────────────────────────┘

  STEP 3: Draw the DAG
              Burglary        Earthquake
                 ╲              ╱
                  ╲            ╱
                   ▼          ▼
                    Alarm
                   ╱     ╲
                  ╱       ╲
                 ▼         ▼
            JohnCalls    MaryCalls

  STEP 4: List conditional independencies
  • JohnCalls ⫫ Burglary | Alarm
  • JohnCalls ⫫ Earthquake | Alarm
  • MaryCalls ⫫ Burglary | Alarm
  • MaryCalls ⫫ Earthquake | Alarm
  • JohnCalls ⫫ MaryCalls | Alarm

  STEP 5: Count CPT entries
  P(B): 1 free param (since P(¬b)=1-P(b))
  P(E): 1
  P(A|B,E): 4 rows × 1 free param = 4
  P(J|A): 2 rows × 1 = 2
  P(M|A): 2 rows × 1 = 2
  Total independent params = 1+1+4+2+2 = 10

  vs Full Joint: 2^5 - 1 = 31 params needed!
```

> [🔝 Top](#-problem-index) | [Next →](#problem-5-pjohncalls--true)

---

## Problem 5: P(JohnCalls = true)

> ⭐⭐ Medium | [Theory: BN Inference](./probabilistic_reasoning_theory.md#12-obtaining-full-joint-from-bn) | [← Prev](#problem-4-burglary-alarm-bn-construction) | [Next →](#problem-6-pmarycalls--false)

### Step-by-Step Solution

```
  FIND: P(j) = P(JohnCalls = true)

  STEP 1: Use CONDITIONING on Alarm (J's parent)
  P(j) = Σ_{a ∈ A} P(j|a) · P(a)
       = P(j|a)·P(a) + P(j|¬a)·P(¬a)
       = 0.90·P(a) + 0.05·P(¬a)

  We need P(a) first!

  STEP 2: Find P(a) = P(Alarm = true)
  Use CONDITIONING on Alarm's parents (B, E):
  P(a) = Σ_{b,e} P(a|b,e) · P(b,e)

  Since B ⫫ E (independent root nodes): P(b,e) = P(b)·P(e)

  P(a) = P(a|b,e)·P(b)·P(e)     + P(a|b,¬e)·P(b)·P(¬e)
       + P(a|¬b,e)·P(¬b)·P(e)   + P(a|¬b,¬e)·P(¬b)·P(¬e)

       = 0.95 × 0.001 × 0.002   + 0.94 × 0.001 × 0.998
       + 0.29 × 0.999 × 0.002   + 0.001 × 0.999 × 0.998

       = 0.0000019   + 0.0009388
       + 0.0005794   + 0.0009980

       = 0.002516442

  P(a) ≈ 0.0025
  P(¬a) = 1 - 0.0025 = 0.9975

  STEP 3: Substitute back
  P(j) = 0.90 × 0.0025 + 0.05 × 0.9975
       = 0.00225 + 0.049875
       = 0.052125

  ANSWER: P(JohnCalls = true) ≈ 0.0521 ≈ 5.2%

  MAKES SENSE? Burglaries (0.1%) and earthquakes (0.2%) are rare,
  so alarm rarely rings, so John rarely calls. 5.2% is reasonable.
```

> [🔝 Top](#-problem-index) | [Next →](#problem-6-pmarycalls--false)

---

## Problem 6: P(MaryCalls = false)

> ⭐⭐ Medium | [Theory: BN Inference](./probabilistic_reasoning_theory.md#12-obtaining-full-joint-from-bn) | [← Prev](#problem-5-pjohncalls--true) | [Next →](#problem-7-joint-entry-pjma¬b¬e)

### Step-by-Step Solution

```
  FIND: P(¬m) = P(MaryCalls = false)

  STEP 1: Use CONDITIONING on Alarm
  P(¬m) = Σ_{a ∈ A} P(¬m|a) · P(a)
        = P(¬m|a)·P(a) + P(¬m|¬a)·P(¬a)
        = 0.30·P(a) + 0.99·P(¬a)

  STEP 2: We already know P(a) from Problem 5!
  P(a) = 0.0025
  P(¬a) = 0.9975

  STEP 3: Substitute
  P(¬m) = 0.30 × 0.0025 + 0.99 × 0.9975
        = 0.00075 + 0.987525
        = 0.988275

  ANSWER: P(MaryCalls = false) ≈ 0.9883 ≈ 98.8%

  MAKES SENSE? Alarm almost never rings → Mary almost never calls
  → "not calling" is ~99%. Yes!

  EXAM HACK: Reuse P(a) from previous problem! Don't recalculate!
```

> [🔝 Top](#-problem-index) | [Next →](#problem-7-joint-entry-pjma¬b¬e)

---

## Problem 7: Joint entry P(j,m,a,¬b,¬e)

> ⭐⭐ Medium | [Theory: Joint from BN](./probabilistic_reasoning_theory.md#12-obtaining-full-joint-from-bn) | [← Prev](#problem-6-pmarycalls--false) | [Next →](#problem-8-pburglary--jm--enumeration)

### Step-by-Step Solution

```
  FIND: P(j, m, a, ¬b, ¬e) = ?

  FORMULA: P(X₁,...,Xₙ) = Π P(Xᵢ | parents(Xᵢ))

  STEP 1: Write the product (use node ordering — effects before causes)
  P(j, m, a, ¬b, ¬e)
  = P(j | a) × P(m | a) × P(a | ¬b, ¬e) × P(¬b) × P(¬e)

  STEP 2: Look up each value from CPTs
  P(j | a)       = 0.90
  P(m | a)       = 0.70
  P(a | ¬b, ¬e)  = 0.001  (row: B=f, E=f in P(A|B,E) table)
  P(¬b)          = 0.999
  P(¬e)          = 0.998

  STEP 3: Multiply
  = 0.90 × 0.70 × 0.001 × 0.999 × 0.998
  = 0.63 × 0.001 × 0.999 × 0.998
  = 0.000630 × 0.999 × 0.998
  = 0.000628

  ANSWER: P(j, m, a, ¬b, ¬e) ≈ 0.000628

  What this means: "The chance that John calls, Mary calls,
  alarm rings, but there's NO burglary and NO earthquake"
  = about 0.06%. This is a false alarm scenario!
```

> [🔝 Top](#-problem-index) | [Next →](#problem-8-pburglary--jm--enumeration)

---

## Problem 8: P(Burglary | j,m) — Enumeration

> ⭐⭐⭐ Hard | [Theory: Enumeration](./probabilistic_reasoning_theory.md#15-exact-inference--enumeration) | [← Prev](#problem-7-joint-entry-pjma¬b¬e) | [Next →](#problem-9-pb--jm--variable-elimination)

### Problem Setup

```
  FIND: P(b | j, m)  where j=JohnCalls=true, m=MaryCalls=true

  Identify variable types:
  X (Query)    = Burglary
  E (Evidence) = JohnCalls=t, MaryCalls=t
  Y (Hidden)   = Alarm, Earthquake

  FORMULA: P(b | j,m) = P(b,j,m)/P(j,m) = α × P(b,j,m)
```

### Step 1: Write using marginalization over hidden vars

```
  P(b | j,m) = α × Σ_{a,e} P(b, j, m, a, e)
```

### Step 2: Node ordering + factor as product of CPTs

```
  P(b, j, m, a, e) written with effects before causes:
  = P(j, m, a, b, e)
  = P(j|a) × P(m|a) × P(a|b,e) × P(b) × P(e)
```

### Step 3: Enumerate ALL combos of (a, e) — 4 combos

```
  ┌──────┬──────┬─────────────────────────────────────────────────────────────┐
  │  a   │  e   │  P(j|a) × P(m|a) × P(a|b,e) × P(b) × P(e)               │
  ├──────┼──────┼─────────────────────────────────────────────────────────────┤
  │  t   │  t   │  0.90 × 0.70 × 0.95 × 0.001 × 0.002 = 0.000001197       │
  │  t   │  f   │  0.90 × 0.70 × 0.94 × 0.001 × 0.998 = 0.000591156       │
  │  f   │  t   │  0.05 × 0.01 × 0.05 × 0.001 × 0.002 = 0.0000000000500   │
  │  f   │  f   │  0.05 × 0.01 × 0.06 × 0.001 × 0.998 = 0.0000000299400   │
  └──────┴──────┴─────────────────────────────────────────────────────────────┘

  Sum = 0.000001197 + 0.000591156 + 0.00000000005 + 0.00000002994
      ≈ 0.00059224

  P(b | j,m) = α × 0.00059224
```

### Step 4: To get P(B|j,m) we also need P(¬b|j,m)

```
  Similarly calculate with ¬b (replacing P(b)=0.001 with P(¬b)=0.999):

  ┌──────┬──────┬─────────────────────────────────────────────────────────────┐
  │  a   │  e   │  P(j|a) × P(m|a) × P(a|¬b,e) × P(¬b) × P(e)            │
  ├──────┼──────┼─────────────────────────────────────────────────────────────┤
  │  t   │  t   │  0.90 × 0.70 × 0.29 × 0.999 × 0.002 = 0.000365         │
  │  t   │  f   │  0.90 × 0.70 × 0.001× 0.999 × 0.998 = 0.000628         │
  │  f   │  t   │  0.05 × 0.01 × 0.71 × 0.999 × 0.002 = 0.000000710      │
  │  f   │  f   │  0.05 × 0.01 × 0.999× 0.999 × 0.998 = 0.000000499      │
  └──────┴──────┴─────────────────────────────────────────────────────────────┘

  Sum for ¬b ≈ 0.000994 (approximate — exact calculation needed for precision)
```

### Step 5: Normalize

```
  P(B|j,m) = α × [0.00059224, P(¬b sum)]

  α = 1 / (P(b sum) + P(¬b sum))

  Then:
  P(b|j,m) = 0.00059224 / (0.00059224 + 0.000994...)
           ≈ 0.284  (about 28.4%)

  COMPUTATIONAL COST:
  For b alone: 4 combos × 4 multiplications each = 16 mul + 3 add
  For both b and ¬b: 32 multiplications + 6 additions
```

> [🔝 Top](#-problem-index) | [Next →](#problem-9-pb--jm--variable-elimination)

---

## Problem 9: P(B | j,m) — Variable Elimination

> ⭐⭐⭐ Hard | [Theory: Variable Elimination](./probabilistic_reasoning_theory.md#16-exact-inference--variable-elimination) | [← Prev](#problem-8-pburglary--jm--enumeration) | [Next →](#problem-10-homework-problems)

### Same problem, SMARTER method

```
  P(B|j,m) = α × f₁(B) × Σ_e f₂(E) × Σ_a f₃(A,B,E) × f₄(A) × f₅(A)

  WHERE (j and m are fixed to true):
  f₁(B) = P(B)         = [0.001, 0.999]
  f₂(E) = P(E)         = [0.002, 0.998]
  f₃(A,B,E) = P(A|B,E) = 8-entry matrix
  f₄(A) = P(j|A)       = [0.90, 0.05]    (j=true is fixed)
  f₅(A) = P(m|A)       = [0.70, 0.01]    (m=true is fixed)
```

### STEP 1: Sum out A (innermost summation)

```
  f₆(B,E) = Σ_a f₃(A,B,E) × f₄(A) × f₅(A)

  For each (B,E) combo, sum over A = {t, f}:

  f₆(b,e)  = f₃(a,b,e)×f₄(a)×f₅(a) + f₃(¬a,b,e)×f₄(¬a)×f₅(¬a)
           = 0.95 × 0.90 × 0.70 + 0.05 × 0.05 × 0.01
           = 0.5985 + 0.000025
           = 0.598525

  f₆(b,¬e) = 0.94 × 0.90 × 0.70 + 0.06 × 0.05 × 0.01
           = 0.5922 + 0.00003
           = 0.59223

  f₆(¬b,e) = 0.29 × 0.90 × 0.70 + 0.71 × 0.05 × 0.01
           = 0.1827 + 0.000355
           = 0.183055

  f₆(¬b,¬e)= 0.001 × 0.90 × 0.70 + 0.999 × 0.05 × 0.01
           = 0.00063 + 0.000499
           = 0.001130

  COST: 4 multiplications + 1 addition (per B,E combo, but counted as 1 factor operation)
```

### STEP 2: Sum out E

```
  f₇(B) = Σ_e f₂(E) × f₆(B,E)

  f₇(b)  = f₂(e)×f₆(b,e) + f₂(¬e)×f₆(b,¬e)
         = 0.002 × 0.598525 + 0.998 × 0.59223
         = 0.001197 + 0.591246
         = 0.592443

  f₇(¬b) = f₂(e)×f₆(¬b,e) + f₂(¬e)×f₆(¬b,¬e)
         = 0.002 × 0.183055 + 0.998 × 0.001130
         = 0.000366 + 0.001128
         = 0.001494

  COST: 2 multiplications + 1 addition
```

### STEP 3: Final multiply + normalize

```
  P(B|j,m) = α × f₁(B) × f₇(B)

  unnormalized(b)  = 0.001 × 0.592443 = 0.000592
  unnormalized(¬b) = 0.999 × 0.001494 = 0.001493

  α = 1 / (0.000592 + 0.001493) = 1 / 0.002085

  P(b|j,m)  = 0.000592 / 0.002085 ≈ 0.284
  P(¬b|j,m) = 0.001493 / 0.002085 ≈ 0.716

  ANSWER: P(B|j,m) = [0.284, 0.716]

  COST: 1 multiplication

  TOTAL VE COST: 7 multiplications + 2 additions
  vs ENUMERATION: 32 multiplications + 6 additions
  
  ┌──────────────────────────────────────┐
  │  VE is ~4.5× faster for this        │
  │  problem. Gap grows exponentially    │
  │  with more variables!               │
  └──────────────────────────────────────┘

  MAKES SENSE? P(burglary|both call) ≈ 28%. Even though both neighbors
  called, burglary is still unlikely because the alarm often goes off for
  other reasons (earthquakes, false alarms) and both events are rare.
```

> [🔝 Top](#-problem-index) | [Next →](#problem-10-homework-problems)

---

## Problem 10: Homework Problems

> ⭐⭐ Medium | [Theory: BN Inference](./probabilistic_reasoning_theory.md#12-obtaining-full-joint-from-bn) | [← Prev](#problem-9-pb--jm--variable-elimination) | [Next →](#problem-11-pcavity--toothache--catch)

### Q1: P(JohnCalls=true, Earthquake=true) = P(j, e)

```
  P(j, e) = Σ_{b,a} P(j, e, b, a)       ...marginalize over B, A
          = Σ_{b,a} P(j|a) × P(a|b,e) × P(b) × P(e)

  (MaryCalls doesn't appear because we marginalize over it,
   and P(m|a) sums to 1 over m when not conditioned)

  Wait — actually we need to be more careful. Let's include M marginalization:
  P(j, e) = Σ_{b,a,m} P(j|a) P(m|a) P(a|b,e) P(b) P(e)
           = Σ_{b,a} P(j|a) [Σ_m P(m|a)] P(a|b,e) P(b) P(e)
           = Σ_{b,a} P(j|a) × 1 × P(a|b,e) P(b) P(e)
           = P(e) × Σ_b P(b) × Σ_a P(j|a) P(a|b,e)

  Inner sum over a (for each b):
  Σ_a P(j|a)P(a|b,e):
    b=t: 0.90×0.95 + 0.05×0.05 = 0.855 + 0.0025 = 0.8575
    b=f: 0.90×0.29 + 0.05×0.71 = 0.261 + 0.0355 = 0.2965

  Sum over b:
  = 0.8575 × 0.001 + 0.2965 × 0.999
  = 0.0008575 + 0.2962035
  = 0.297061

  Multiply by P(e):
  P(j,e) = 0.002 × 0.297061 = 0.000594122

  ANSWER: P(j, e) ≈ 0.000594122 ✓ (matches slides)
```

### Q2: P(MaryCalls=false, Alarm=true, Earthquake=true) = P(¬m, a, e)

```
  P(¬m, a, e) = Σ_{b} P(¬m|a) × P(a|b,e) × P(b) × P(e)
              (marginalize over B; J marginalized out since Σ_j P(j|a)=1)

  = P(¬m|a) × P(e) × Σ_b P(a|b,e) × P(b)

  Inner sum over b:
  Σ_b P(a|b,e) × P(b) = 0.95 × 0.001 + 0.29 × 0.999
                       = 0.00095 + 0.28971
                       = 0.29066

  P(¬m, a, e) = 0.30 × 0.002 × 0.29066
              = 0.30 × 0.00058132
              = 0.000174396

  ANSWER: P(¬m, a, e) ≈ 0.000174396 ✓ (matches slides)
```

> [🔝 Top](#-problem-index) | [Next →](#problem-11-pcavity--toothache--catch)

---

## Problem 11: P(Cavity | toothache ∨ catch)

> ⭐⭐⭐ Hard | [Theory: Normalization](./probabilistic_reasoning_theory.md#14-normalization-constant-α) | [← Prev](#problem-10-homework-problems)

### Given: Toothache-Cavity-Catch joint table (same as Problem 2)

### Find: P(Cavity | toothache ∨ catch)

```
  This is a DISTRIBUTION:
  P(Cavity | toothache ∨ catch) = [ P(cavity | toothache ∨ catch)  ]
                                   [ P(¬cavity | toothache ∨ catch) ]
```

### Step 1: Find P(cavity | toothache ∨ catch) using the definition

```
  P(cavity | toothache ∨ catch) = P(cavity ∧ (toothache ∨ catch))
                                   ─────────────────────────────────
                                       P(toothache ∨ catch)
```

### Step 2: Expand the numerator using distribution law

```
  P(cavity ∧ (toothache ∨ catch))
  = P((cavity ∧ toothache) ∨ (cavity ∧ catch))

  Use inclusion-exclusion:
  = P(cavity ∧ toothache) + P(cavity ∧ catch) - P(cavity ∧ toothache ∧ catch)

  From joint table:
  P(cavity ∧ toothache) = 0.108 + 0.012 = 0.12
  P(cavity ∧ catch)     = 0.108 + 0.072 = 0.18
  P(cavity ∧ toothache ∧ catch) = 0.108

  = 0.12 + 0.18 - 0.108 = 0.192
```

### Step 3: Find the denominator P(toothache ∨ catch)

```
  P(toothache ∨ catch)
  = P(toothache) + P(catch) - P(toothache ∧ catch)

  P(toothache) = 0.108 + 0.012 + 0.016 + 0.064 = 0.2
  P(catch)     = 0.108 + 0.072 + 0.016 + 0.144 = 0.34
  P(toothache ∧ catch) = 0.108 + 0.016 = 0.124

  = 0.2 + 0.34 - 0.124 = 0.416
```

### Step 4: Divide

```
  P(cavity | toothache ∨ catch) = 0.192 / 0.416 = 0.4615
  P(¬cavity | toothache ∨ catch) = 1 - 0.4615 = 0.5385

  OR verify directly:
  P(¬cavity ∧ (toothache ∨ catch))
  = P(¬cavity ∧ toothache) + P(¬cavity ∧ catch) - P(¬cavity ∧ toothache ∧ catch)
  = (0.016+0.064) + (0.016+0.144) - 0.016
  = 0.08 + 0.16 - 0.016
  = 0.224

  P(¬cavity | toothache ∨ catch) = 0.224 / 0.416 = 0.5385 ✓

  ANSWER: P(Cavity | toothache ∨ catch) = [0.4615, 0.5385]
```

### Using α Notation

```
  α = 1/P(toothache ∨ catch) = 1/0.416

  P(Cavity | toothache ∨ catch) = α × [0.192, 0.224]
                                 = [0.192/0.416, 0.224/0.416]
                                 = [0.4615, 0.5385]

  Check: 0.4615 + 0.5385 = 1.0 ✓
```

> [🔝 Top](#-problem-index)

---

## 🧠 Want More BN Inference Problems?

```
┌──────────────────────────────────────────────────────────────────┐
│  The problems above cover Unit 4.1 + 4.2 from SDM slides.      │
│  For EXTENDED coverage of BN Inference including:               │
│                                                                  │
│  • More Enumeration & VE worked examples                        │
│  • Approximate inference (sampling) problems                    │
│  • d-Separation & conditional independence queries              │
│  • Practice problems with hints (no solutions — try first!)    │
│                                                                  │
│  CHECK OUT THE DEDICATED BN INFERENCE FOLDER:                   │
└──────────────────────────────────────────────────────────────────┘
```

| File | Link |
|------|------|
| 📋 BN Index | [bn_inference_index.md](https://github.com/rpaut03l/TS-01/blob/ai-sdm-probabilistic-reasoning/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_index.md) |
| 📘 BN Theory | [bn_inference_theory.md](https://github.com/rpaut03l/TS-01/blob/ai-sdm-probabilistic-reasoning/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_theory.md) |
| 🔢 BN Numericals | [bn_inference_numericals.md](https://github.com/rpaut03l/TS-01/blob/ai-sdm-probabilistic-reasoning/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_numericals.md) |
| 🏋️ BN Practice | [bn_inference_practice.md](https://github.com/rpaut03l/TS-01/blob/ai-sdm-probabilistic-reasoning/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_practice.md) |

---

## ⚡ Numerical Tricks Cheat Sheet

```
┌──────────────────────────────────────────────────────────────────┐
│  TRICK 1: Reuse intermediate results!                            │
│  P(a) computed once → use in P(j) AND P(¬m) problems             │
│                                                                  │
│  TRICK 2: Independent root nodes multiply directly               │
│  P(b, e) = P(b) × P(e)  — no CPT lookup needed                   │
│                                                                  │
│  TRICK 3: P(¬X|parents) = 1 - P(X|parents)                       │
│  Never look up ¬X in CPT — just subtract from 1!                 │
│                                                                  │
│  TRICK 4: α trick — don't compute P(evidence) separately         │
│  Compute unnormalized for all values, then divide by sum         │
│                                                                  │
│  TRICK 5: Marginalize over binary variable                       │
│  Σ_m P(m|a) = P(m|a) + P(¬m|a) = 1                               │
│  When a variable doesn't appear in query/evidence, its           │
│  sum disappears!                                                 │
│                                                                  │
│  TRICK 6: VE order — sum out innermost variable first            │
│  Pull out terms that don't depend on the summation variable      │
│                                                                  │
│  TRICK 7: Sanity check your answer                               │
│  • All probs between 0 and 1                                     │
│  • Distribution sums to 1                                        │
│  • Does the answer make intuitive sense?                         │
└──────────────────────────────────────────────────────────────────┘
```

---

> **Navigation:** [📋 INDEX](./probabilistic_reasoning_index.md) | [📘 THEORY](./probabilistic_reasoning_theory.md) | [🧠 BN Inference Deep Dive](https://github.com/rpaut03l/TS-01/blob/ai-sdm-probabilistic-reasoning/AI/SD-M/Bayesian-Network-(BN)-Inference/bn_inference_index.md)
>
> **Source:** (SDM) Slides · Book: Norvig · AI

[🔝 Back to Top](#-probabilistic-reasoning--numericals-guide)
