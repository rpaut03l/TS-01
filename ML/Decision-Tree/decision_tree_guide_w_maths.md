# 🌳 Decision Trees — Complete Study Guide
 
> **Topic:** Decision Tree Learning using Entropy & Information Gain  
> **Level:** Beginner → Advanced

---

## 📋 Table of Contents

1. [Introduction](#1-introduction)
2. [Core Concepts & Terminology](#2-core-concepts--terminology)
3. [Decision Tree Structure (Visual)](#3-decision-tree-structure-visual)
4. [How a Decision Tree Works](#4-how-a-decision-tree-works)
5. [Mathematics — Step by Step](#5-mathematics--step-by-step)
   - [5.1 Entropy](#51-entropy)
   - [5.2 Information Gain](#52-information-gain)
   - [5.3 Gain Ratio](#53-gain-ratio)
   - [5.4 Gini Impurity (CART)](#54-gini-impurity-cart)
6. [The Algorithm](#6-the-algorithm)
7. [Worked Example — Loan Dataset](#7-worked-example--loan-dataset)
8. [Tree → Rules Conversion](#8-tree--rules-conversion)
9. [Handling Continuous Attributes](#9-handling-continuous-attributes)
10. [Overfitting & Pruning](#10-overfitting--pruning)
11. [Algorithm Variants](#11-algorithm-variants)
12. [Visualizations & Diagrams](#12-visualizations--diagrams)
13. [Mnemonics & Cheat Sheet](#13-mnemonics--cheat-sheet)
14. [Practice Problems](#14-practice-problems)
15. [Best Practices](#15-best-practices)
16. [Common Pitfalls](#16-common-pitfalls)

---

## 1. Introduction

A **Decision Tree** is a supervised machine learning algorithm used for **classification** and **regression**. It learns a model shaped like a flowchart-tree where:

- Every **internal node** = a question about a feature
- Every **branch** = an answer/outcome to that question
- Every **leaf node** = a final class label or prediction

```
                  [Is it raining?]
                  /             \
               Yes               No
              /                    \
    [Do you have an umbrella?]    → Go outside ☀️
         /          \
       Yes           No
        |              |
   Stay dry ☂️     Get wet 🌧️
```

### Why Use Decision Trees?

| Advantage | Explanation |
|---|---|
| ✅ Interpretable | Humans can read the rules directly |
| ✅ No feature scaling needed | Works with raw values |
| ✅ Handles mixed data | Numerical + categorical features |
| ✅ Competitive accuracy | Often rivals complex models |
| ✅ Fast prediction | Just traverse the tree |
| ❌ Prone to overfitting | Can memorize training data |
| ❌ Instability | Small data change → different tree |
| ❌ NP-hard to optimize | All algorithms are heuristic |

> 💡 **Best-known system:** C4.5 by Ross Quinlan (downloadable, widely used in practice)

---

## 2. Core Concepts & Terminology

| Term | Meaning | Example |
|---|---|---|
| **Root Node** | Top-most node; first question asked | "Own House?" |
| **Decision Node** | Internal node that tests an attribute | "Has Job?" |
| **Leaf Node** | Terminal node; holds a class label | "Yes" / "No" |
| **Branch** | Edge connecting nodes; represents a value/outcome | "true" or "false" |
| **Depth** | Longest path from root to leaf | 3 levels deep |
| **Purity** | All examples in node are same class | 6 Yes, 0 No = pure |
| **Impurity** | Mix of classes in a node | 3 Yes, 3 No = max impure |
| **Entropy** | Mathematical measure of impurity/disorder | 0 = pure, 1 = max disorder |
| **Information Gain** | Reduction in entropy after a split | Higher = better attribute |
| **Pruning** | Removing branches to reduce overfitting | Pre/Post pruning |
| **Support** | Fraction of training data a rule covers | 6/15 = 40% |
| **Confidence** | Accuracy of the rule on covered examples | 6/6 = 100% |

---

## 3. Decision Tree Structure (Visual)

### Full Tree (from Loan Dataset)

```
                         ┌─────────────┐
                         │    Age?     │  ← Root Node (Decision Node)
                         └──────┬──────┘
              ┌─────────────────┼──────────────────┐
           Young             middle                old
              │                 │                   │
     ┌────────┴────────┐  ┌─────┴──────┐   ┌───────┴───────┐
     │   Has_Job?      │  │ Own_House? │   │ Credit_Rating?│
     └────────┬────────┘  └─────┬──────┘   └───────┬───────┘
          ┌───┴───┐         ┌───┴───┐        ┌──────┼──────┐
        true   false      true   false      fair  good  excellent
          │       │         │       │         │     │       │
        Yes      No        Yes     No        No   Yes     Yes
       (2/2)   (3/3)      (3/3)  (2/2)     (1/1)(2/2)   (2/2)
         ↑                                             ↑
      Leaf Node                                    Leaf Node
```

### Simpler Equivalent Tree (Better!)

```
                    ┌──────────────┐
                    │  Own_House?  │  ← Root (highest info gain)
                    └──────┬───────┘
                    ┌──────┴──────┐
                  true          false
                    │               │
               ┌────┴────┐    ┌────┴────┐
               │   Yes   │    │ Has_Job?│
               │  (6/6)  │    └────┬────┘
               └─────────┘   ┌────┴────┐
                            true     false
                              │          │
                            Yes         No
                           (5/5)       (4/4)
```

> 🎯 **Key insight:** The second tree is simpler AND equally accurate. Simpler trees generalize better!

---

## 4. How a Decision Tree Works

### Classification Flow (Step-by-step)

Given a new record: `Age=young, Has_Job=false, Own_house=false, Credit=good`

```
Step 1: Start at ROOT → "Own_House?"
                ↓
        Own_House = false → go RIGHT

Step 2: Reach "Has_Job?"
                ↓
        Has_Job = false → go RIGHT

Step 3: Reach LEAF → "No"
                ↓
        🏦 LOAN REJECTED
```

### Tree Building (High Level)

```
Start with ALL training data at root
         │
         ▼
  For each attribute, compute
  how much it reduces impurity
         │
         ▼
  Pick attribute with MAX gain
  → Make it the current node
         │
         ▼
  Split data into subsets
  (one per attribute value)
         │
         ▼
  Recurse on each subset
  until stopping condition
```

### Stopping Conditions

```
STOP when any of these are true:
┌─────────────────────────────────────────────────┐
│ ① All examples in node = same class             │
│    → Make leaf with that class                  │
│                                                 │
│ ② No attributes left to split on               │
│    → Make leaf with MAJORITY class              │
│                                                 │
│ ③ No examples left in this branch              │
│    → Make leaf with PARENT'S majority class     │
│                                                 │
│ ④ Gain < threshold (pre-pruning)               │
│    → Make leaf with majority class              │
└─────────────────────────────────────────────────┘
```

---

## 5. Mathematics — Step by Step

---

### 5.0 — Pre-Requisite: How to Calculate log₂ (Base-2 Logarithm)

> 💡 **Read this first.** Every entropy and gain calculation depends on computing log₂. Understanding this once makes all the math click.

---

#### 📐 What Is a Logarithm?

```
┌─────────────────────────────────────────────────────────────────┐
│  DEFINITION                                                     │
│                                                                 │
│  log_b(x) = y    means    b^y = x                               │
│                                                                 │
│  In plain English:                                              │
│  "To what POWER must I raise b to get x?"                       │
│                                                                 │
│  b = base (we use base 2 in entropy)                            │
│  x = the number we're taking the log of                         │
│  y = the answer (the exponent)                                  │
│                                                                 │
│  EXAMPLES with base 2:                                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ log₂(8)   = 3   because  2³ = 8                         │   │
│  │ log₂(4)   = 2   because  2² = 4                         │   │
│  │ log₂(2)   = 1   because  2¹ = 2                         │   │
│  │ log₂(1)   = 0   because  2⁰ = 1   ← always true!       │   │
│  │ log₂(0.5) = −1  because  2⁻¹ = 0.5                     │   │
│  │ log₂(0.25)= −2  because  2⁻² = 0.25                    │   │
│  │ log₂(0.125)=−3  because  2⁻³ = 0.125                   │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  CRITICAL RULE:                                                 │
│  Any number between 0 and 1 (a fraction/probability)           │
│  ALWAYS has a NEGATIVE logarithm.                               │
│                                                                 │
│  WHY? Because to get a fraction, you need a negative exponent:  │
│    2⁻¹ = 1/2 = 0.5    →  log₂(0.5) = −1                       │
│    2⁻² = 1/4 = 0.25   →  log₂(0.25) = −2                      │
│    Probabilities are always between 0 and 1                     │
│    So log₂(probability) is ALWAYS negative!                     │
│    That's why entropy has a leading − sign (to make it +ve)    │
└─────────────────────────────────────────────────────────────────┘
```

---

#### 📐 The Change of Base Formula

```
┌─────────────────────────────────────────────────────────────────┐
│  PROBLEM: Most calculators only have log₁₀ or ln buttons.      │
│           There is no log₂ button.                              │
│                                                                 │
│  SOLUTION: Change of Base Formula                               │
│                                                                 │
│              log₁₀(x)         ln(x)                            │
│  log₂(x) = ──────────   =   ─────────                          │
│              log₁₀(2)         ln(2)                             │
│                                                                 │
│  The FIXED denominator values:                                  │
│    log₁₀(2) = 0.30103   ← divide by this when using log₁₀      │
│    ln(2)    = 0.69315   ← divide by this when using ln         │
│                                                                 │
│  THE RECIPE (always the same 2 steps):                          │
│    Step A: Find log₁₀(x) on your calculator                     │
│    Step B: Divide that result by 0.30103                        │
│    → Result = log₂(x)                                           │
│                                                                 │
│  WHY DOES THIS WORK?                                            │
│  log_b(x) = log_a(x) / log_a(b)   ← mathematical identity     │
│  Choosing a=10: log₂(x) = log₁₀(x) / log₁₀(2) = log₁₀(x)/0.301│
└─────────────────────────────────────────────────────────────────┘
```

---

#### 📐 How to Find log₁₀ Without a Calculator

```
┌─────────────────────────────────────────────────────────────────┐
│  CORE VALUES TO MEMORISE (only 3 needed!)                       │
│                                                                 │
│    log₁₀(2)  = 0.3010                                           │
│    log₁₀(3)  = 0.4771                                           │
│    log₁₀(10) = 1.0000   ← always!                              │
│                                                                 │
│  RULES TO DERIVE EVERYTHING ELSE:                               │
│                                                                 │
│  Rule 1: log(a × b) = log(a) + log(b)                          │
│    log₁₀(6)  = log₁₀(2×3) = 0.3010 + 0.4771 = 0.7781          │
│    log₁₀(4)  = log₁₀(2×2) = 0.3010 + 0.3010 = 0.6021          │
│    log₁₀(8)  = log₁₀(2×2×2) = 3×0.3010      = 0.9031          │
│                                                                 │
│  Rule 2: log(a/b) = log(a) − log(b)                            │
│    log₁₀(0.6) = log₁₀(6/10) = log₁₀(6) − log₁₀(10)            │
│               = 0.7781 − 1.0000 = −0.2219                      │
│    log₁₀(0.4) = log₁₀(4/10) = log₁₀(4) − log₁₀(10)            │
│               = 0.6021 − 1.0000 = −0.3979                      │
│    log₁₀(0.5) = log₁₀(5/10) = log₁₀(5) − 1.0000               │
│               log₁₀(5) = log₁₀(10/2) = 1−0.3010 = 0.6990      │
│               = 0.6990 − 1.0000 = −0.3010                      │
│                                                                 │
│  Rule 3: log(aⁿ) = n × log(a)                                  │
│    log₁₀(4) = log₁₀(2²) = 2 × log₁₀(2) = 2 × 0.3010 = 0.6021 │
│    log₁₀(0.25) = log₁₀(1/4) = log₁₀(1)−log₁₀(4) = 0−0.6021   │
│               = −0.6021                                         │
└─────────────────────────────────────────────────────────────────┘
```

---

#### 📐 Complete Worked Examples: log₂(0.6) and log₂(0.4)

```
┌─────────────────────────────────────────────────────────────────┐
│  COMPUTING log₂(0.6) — every micro-step                        │
│                                                                 │
│  Sub-step 1: Recognise 0.6 = 6 ÷ 10                           │
│                                                                 │
│  Sub-step 2: Apply log division rule                            │
│              log₁₀(0.6) = log₁₀(6) − log₁₀(10)                │
│                                                                 │
│  Sub-step 3: Find log₁₀(6)                                     │
│              log₁₀(6) = log₁₀(2 × 3)                           │
│                       = log₁₀(2) + log₁₀(3)                    │
│                       = 0.3010    + 0.4771                      │
│                       = 0.7781                                  │
│                                                                 │
│  Sub-step 4: Find log₁₀(10) = 1.0000  (always)                 │
│                                                                 │
│  Sub-step 5: Subtract                                           │
│              log₁₀(0.6) = 0.7781 − 1.0000 = −0.2219           │
│                                                                 │
│  Sub-step 6: Change base — divide by log₁₀(2)                  │
│              log₂(0.6) = −0.2219 ÷ 0.3010                      │
│                        = −0.7370  ✅                             │
│                                                                 │
│  Sanity check: 2^(−0.737) = 1/2^(0.737) ≈ 1/1.667 ≈ 0.60 ✅   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  COMPUTING log₂(0.4) — every micro-step                        │
│                                                                 │
│  Sub-step 1: Recognise 0.4 = 4 ÷ 10                           │
│                                                                 │
│  Sub-step 2: Apply log division rule                            │
│              log₁₀(0.4) = log₁₀(4) − log₁₀(10)                │
│                                                                 │
│  Sub-step 3: Find log₁₀(4) using power rule                    │
│              log₁₀(4) = log₁₀(2²)                               │
│                       = 2 × log₁₀(2)                            │
│                       = 2 × 0.3010                              │
│                       = 0.6021                                  │
│                                                                 │
│  Sub-step 4: Find log₁₀(10) = 1.0000  (always)                 │
│                                                                 │
│  Sub-step 5: Subtract                                           │
│              log₁₀(0.4) = 0.6021 − 1.0000 = −0.3979           │
│                                                                 │
│  Sub-step 6: Change base — divide by log₁₀(2)                  │
│              log₂(0.4) = −0.3979 ÷ 0.3010                      │
│                        = −1.3219  ✅                             │
│                                                                 │
│  Sanity check: 2^(−1.322) = 1/2^(1.322) ≈ 1/2.499 ≈ 0.40 ✅   │
└─────────────────────────────────────────────────────────────────┘
```

---

#### 📊 Master Reference Table — log₂ of All Common Probabilities

```
┌───────────┬────────────┬─────────────────────────┬──────────────┐
│  x        │ log₁₀(x)  │ ÷ 0.3010  =  log₂(x)    │ Notes        │
├───────────┼────────────┼─────────────────────────┼──────────────┤
│  1.000    │  0.0000    │  0.0000 / 0.3010 =  0.000│ 2⁰=1        │
│  0.900    │ −0.0458    │ −0.0458 / 0.3010 = −0.152│              │
│  0.800    │ −0.0969    │ −0.0969 / 0.3010 = −0.322│              │
│  0.750    │ −0.1249    │ −0.1249 / 0.3010 = −0.415│ = 3/4        │
│  0.667    │ −0.1761    │ −0.1761 / 0.3010 = −0.585│ = 2/3        │
│  0.625    │ −0.2041    │ −0.2041 / 0.3010 = −0.678│ = 5/8        │
│  0.600    │ −0.2219    │ −0.2219 / 0.3010 = −0.737│ ← 9/15      │
│  0.500    │ −0.3010    │ −0.3010 / 0.3010 = −1.000│ 2⁻¹=1/2     │
│  0.400    │ −0.3979    │ −0.3979 / 0.3010 = −1.322│ ← 6/15      │
│  0.375    │ −0.4260    │ −0.4260 / 0.3010 = −1.415│ = 3/8        │
│  0.333    │ −0.4771    │ −0.4771 / 0.3010 = −1.585│ = 1/3        │
│  0.300    │ −0.5229    │ −0.5229 / 0.3010 = −1.737│              │
│  0.250    │ −0.6021    │ −0.6021 / 0.3010 = −2.000│ 2⁻²=1/4     │
│  0.200    │ −0.6990    │ −0.6990 / 0.3010 = −2.322│ = 1/5        │
│  0.167    │ −0.7782    │ −0.7782 / 0.3010 = −2.585│ = 1/6        │
│  0.143    │ −0.8451    │ −0.8451 / 0.3010 = −2.807│ = 1/7        │
│  0.125    │ −0.9031    │ −0.9031 / 0.3010 = −3.000│ 2⁻³=1/8     │
│  0.100    │ −1.0000    │ −1.0000 / 0.3010 = −3.322│ = 1/10       │
└───────────┴────────────┴─────────────────────────┴──────────────┘

PATTERN to remember:
  Probabilities of simple fractions 1/2ⁿ give exact integers:
  1/2 → −1,   1/4 → −2,   1/8 → −3,   1/16 → −4
  Everything else falls in between.
```

---

#### 🧠 Shortcut: How to Estimate log₂ Mentally

```
┌─────────────────────────────────────────────────────────────────┐
│  Anchor points to memorise:                                     │
│    log₂(1.0)  =  0       log₂(0.5) = −1                        │
│    log₂(0.25) = −2       log₂(0.125) = −3                      │
│                                                                 │
│  Interpolation trick: 0.6 is between 0.5 and 1.0               │
│    log₂(0.5) = −1,  log₂(1.0) = 0                              │
│    0.6 is 20% of the way from 0.5→1.0                           │
│    Rough estimate: −1 + 0.20×1 = −0.80                          │
│    Actual: −0.737  (close enough for sanity checks!)            │
│                                                                 │
│  Interpolation trick: 0.4 is between 0.25 and 0.5              │
│    log₂(0.25) = −2,  log₂(0.5) = −1                            │
│    0.4 is 60% of the way from 0.25→0.5                          │
│    Rough estimate: −2 + 0.60×1 = −1.40                          │
│    Actual: −1.322  (close enough!)                              │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5.1 Entropy

#### What is Entropy?

Entropy measures **how mixed/disordered** a dataset is.

```
High Entropy = Mixed Classes = Uncertain = More info needed
Low Entropy  = Pure Classes  = Certain   = Less info needed

Real-world analogy:
• A bag with ALL red balls  → entropy = 0   (you know exactly what you'll pick)
• A bag with HALF red, HALF blue → entropy = 1  (total surprise every time)
• A bag with mostly red, few blue → entropy is between 0 and 1

Coin example:
• Fair coin   (50/50):  entropy = 1.0  → you know nothing!
• Biased coin (99/1):   entropy ≈ 0.08 → pretty predictable
• Fixed coin  (100/0):  entropy = 0    → you know everything!
```

---

#### 📐 The Entropy Formula

$$\text{entropy}(D) = -\sum_{j=1}^{|C|} \Pr(c_j) \cdot \log_2 \Pr(c_j)$$

**Breaking down every symbol:**

| Symbol | Full Name | Meaning | Example |
|---|---|---|---|
| `D` | Dataset | The set of training examples at a node | All 15 loan records |
| `C` | Class set | The set of all possible class labels | {Yes, No} |
| `\|C\|` | Class count | How many distinct classes exist | 2 |
| `j` | Class index | Counts from 1 to \|C\| | j=1 → Yes, j=2 → No |
| `Pr(cⱼ)` | Class probability | Fraction of examples belonging to class cⱼ | Pr(Yes) = 9/15 |
| `log₂` | Log base 2 | Logarithm with base 2 (measures bits) | log₂(0.5) = -1 |
| `−` | Negation | Makes the result positive (logs of fractions are negative) | −(−0.971) = +0.971 |
| `Σ` | Summation | Add up the term for every class | Sum over Yes and No |

> ⚠️ **Special convention:** `0 × log₂(0) = 0` by definition (not undefined). Pure nodes don't contribute.

> 💡 **Why log base 2?** It measures information in *bits*. 1 bit = 1 yes/no question. A fair coin needs exactly 1 bit to describe its outcome.

---

#### 🔢 Step-by-Step: Entropy Calculation (Example 1)

**Given:** Dataset D has **9 Yes** and **6 No** out of **15 total** examples.

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — Count the classes                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Total examples  = 15                                           │
│  Yes count       = 9                                            │
│  No  count       = 6                                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2 — Compute class probabilities                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Pr(Yes) = count(Yes) / total = 9 / 15 = 0.6                   │
│  Pr(No)  = count(No)  / total = 6 / 15 = 0.4                   │
│                                                                 │
│  ✅ Check: 0.6 + 0.4 = 1.0  (must sum to 1)                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3 — Write out the entropy formula                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  entropy(D) = − [Pr(Yes) × log₂(Pr(Yes))]                      │
│             − [Pr(No)  × log₂(Pr(No))]                         │
│                                                                 │
│  entropy(D) = − [0.6 × log₂(0.6)]                              │
│             − [0.4 × log₂(0.4)]                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 4 — Calculate each log₂ value                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║  PART A — WHAT IS A LOGARITHM?                           ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
│                                                                 │
│  Definition:                                                    │
│    log_b(x) = y   ←→   b^y = x                                 │
│                                                                 │
│  Read as: "log base b of x equals y"                           │
│  Meaning: "b raised to the power y gives x"                    │
│           or "what exponent on b produces x?"                  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  EXACT examples with base 2 (log₂):                     │  │
│  │                                                          │  │
│  │  log₂(8)    = 3   ← because 2³    = 8                   │  │
│  │  log₂(4)    = 2   ← because 2²    = 4                   │  │
│  │  log₂(2)    = 1   ← because 2¹    = 2                   │  │
│  │  log₂(1)    = 0   ← because 2⁰    = 1  (always!)        │  │
│  │  log₂(0.5)  = −1  ← because 2⁻¹   = 1/2  = 0.5         │  │
│  │  log₂(0.25) = −2  ← because 2⁻²   = 1/4  = 0.25        │  │
│  │  log₂(0.125)= −3  ← because 2⁻³   = 1/8  = 0.125       │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  🔑 KEY INSIGHT: Probabilities are always between 0 and 1.     │
│     To get a number < 1 from 2^y, you need y to be NEGATIVE.   │
│     Therefore log₂(any probability) is ALWAYS NEGATIVE.        │
│     The − sign in the entropy formula flips it to positive.    │
│                                                                 │
│  WHY BASE 2? It measures information in bits.                  │
│    1 bit = 1 yes/no question with completely unknown answer     │
│    Fair coin → 1 bit of uncertainty → entropy = 1.0            │
│    Sure outcome → 0 bits of uncertainty → entropy = 0.0        │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║  PART B — THE 3 LOG RULES YOU NEED                       ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
│                                                                 │
│  Rule 1 — Product Rule:  log(a × b) = log(a) + log(b)          │
│    log₁₀(6) = log₁₀(2×3) = log₁₀(2) + log₁₀(3)                │
│                           = 0.3010   + 0.4771  = 0.7781        │
│                                                                 │
│  Rule 2 — Quotient Rule: log(a/b) = log(a) − log(b)            │
│    log₁₀(0.6) = log₁₀(6/10) = log₁₀(6) − log₁₀(10)            │
│                             = 0.7781  − 1.0000  = −0.2219      │
│                                                                 │
│  Rule 3 — Power Rule:    log(aⁿ) = n × log(a)                  │
│    log₁₀(4) = log₁₀(2²) = 2 × log₁₀(2) = 2 × 0.3010 = 0.6021 │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  CORE VALUES TO MEMORISE (only 3!)                       │  │
│  │                                                          │  │
│  │  log₁₀(2)  = 0.3010   ← most important!                 │  │
│  │  log₁₀(3)  = 0.4771                                     │  │
│  │  log₁₀(10) = 1.0000   ← always true                     │  │
│  │                                                          │  │
│  │  Derive everything else using the 3 rules above          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Derived values (using the 3 rules):                           │
│    log₁₀(4) = 2×log₁₀(2)        = 2×0.3010       = 0.6021    │
│    log₁₀(5) = log₁₀(10/2)       = 1.0000−0.3010  = 0.6990    │
│    log₁₀(6) = log₁₀(2)+log₁₀(3) = 0.3010+0.4771  = 0.7781    │
│    log₁₀(8) = 3×log₁₀(2)        = 3×0.3010        = 0.9031    │
│    log₁₀(9) = 2×log₁₀(3)        = 2×0.4771        = 0.9542    │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║  PART C — CHANGE OF BASE FORMULA                         ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
│                                                                 │
│  Problem: calculators have log₁₀ and ln, NOT log₂.            │
│                                                                 │
│  The Change of Base Formula:                                    │
│                                                                 │
│             log₁₀(x)          ln(x)                            │
│  log₂(x) = ──────────   =   ─────────                          │
│             log₁₀(2)          ln(2)                             │
│                                                                 │
│             log₁₀(x)          ln(x)                            │
│           = ──────────   =   ─────────                          │
│              0.30103          0.69315                            │
│                                                                 │
│  Why does this work?                                            │
│    General form:  log_b(x) = log_a(x) / log_a(b)               │
│    Set a=10:      log₂(x) = log₁₀(x) / log₁₀(2)               │
│    Substitute:    log₂(x) = log₁₀(x) / 0.30103                 │
│                                                                 │
│  THE 2-STEP RECIPE (same every time):                           │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Step A: Compute log₁₀(x)   [use calculator or rules]   │  │
│  │  Step B: Divide by 0.30103                               │  │
│  │  → Answer is log₂(x)   ✅                                │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║  PART D — COMPUTING log₂(0.6) — EVERY MICRO-STEP         ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
│                                                                 │
│  We need: log₂(0.6)                                            │
│                                                                 │
│  ── Sub-step 1: Rewrite as a fraction ──────────────────────── │
│                                                                 │
│    0.6 = 6 ÷ 10 = 6/10                                         │
│                                                                 │
│  ── Sub-step 2: Apply Quotient Rule to log₁₀ ───────────────── │
│                                                                 │
│    log₁₀(6/10) = log₁₀(6) − log₁₀(10)                         │
│                                                                 │
│  ── Sub-step 3: Find log₁₀(6) using Product Rule ──────────── │
│                                                                 │
│    6 = 2 × 3                                                    │
│    log₁₀(6) = log₁₀(2) + log₁₀(3)                              │
│             = 0.3010   + 0.4771                                 │
│             = 0.7781                                            │
│                                                                 │
│  ── Sub-step 4: Look up log₁₀(10) ─────────────────────────── │
│                                                                 │
│    log₁₀(10) = 1.0000   ← always, by definition                │
│                                                                 │
│  ── Sub-step 5: Subtract to get log₁₀(0.6) ────────────────── │
│                                                                 │
│    log₁₀(0.6) = log₁₀(6) − log₁₀(10)                          │
│               = 0.7781  − 1.0000                                │
│               = −0.2219                                         │
│                                                                 │
│    Note: negative because 0.6 < 1                               │
│                                                                 │
│  ── Sub-step 6: Apply Change of Base (divide by 0.30103) ───── │
│                                                                 │
│    log₂(0.6) = log₁₀(0.6) ÷ log₁₀(2)                          │
│              = −0.2219    ÷  0.30103                            │
│                                                                 │
│    How to do the division:                                      │
│      −0.2219 / 0.30103                                          │
│      = −(0.2219 / 0.30103)   ← handle sign separately          │
│                                                                 │
│      0.2219 / 0.30103 = ?                                       │
│      Try: 0.30103 × 0.7 = 0.21072                               │
│      Try: 0.30103 × 0.73 = 0.21975                              │
│      Try: 0.30103 × 0.737 = 0.22186  ← very close to 0.2219!  │
│      Try: 0.30103 × 0.7370 = 0.22186 ✅                         │
│                                                                 │
│    log₂(0.6) = −0.7370   ✅                                     │
│                                                                 │
│  ── Sub-step 7: Sanity check ───────────────────────────────── │
│                                                                 │
│    Verify: does 2^(−0.7370) ≈ 0.6?                             │
│    2^(−0.737) = 1 / 2^(0.737)                                   │
│    2^(0.737) ≈ 2^(0.5) × 2^(0.237) ≈ 1.414 × 1.179 ≈ 1.667   │
│    1 / 1.667 ≈ 0.600  ✅  Correct!                              │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║  PART E — COMPUTING log₂(0.4) — EVERY MICRO-STEP         ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
│                                                                 │
│  We need: log₂(0.4)                                            │
│                                                                 │
│  ── Sub-step 1: Rewrite as a fraction ──────────────────────── │
│                                                                 │
│    0.4 = 4 ÷ 10 = 4/10                                         │
│                                                                 │
│  ── Sub-step 2: Apply Quotient Rule to log₁₀ ───────────────── │
│                                                                 │
│    log₁₀(4/10) = log₁₀(4) − log₁₀(10)                         │
│                                                                 │
│  ── Sub-step 3: Find log₁₀(4) using Power Rule ────────────── │
│                                                                 │
│    4 = 2²                                                       │
│    log₁₀(4) = log₁₀(2²) = 2 × log₁₀(2)                        │
│             = 2 × 0.3010                                        │
│             = 0.6021  (just double log₁₀(2)!)                  │
│                                                                 │
│  ── Sub-step 4: Look up log₁₀(10) ─────────────────────────── │
│                                                                 │
│    log₁₀(10) = 1.0000                                          │
│                                                                 │
│  ── Sub-step 5: Subtract to get log₁₀(0.4) ────────────────── │
│                                                                 │
│    log₁₀(0.4) = log₁₀(4) − log₁₀(10)                          │
│               = 0.6021  − 1.0000                                │
│               = −0.3979                                         │
│                                                                 │
│    Note: negative because 0.4 < 1                               │
│    Note: more negative than log₁₀(0.6)=−0.2219 ✓ (0.4<0.6)   │
│                                                                 │
│  ── Sub-step 6: Apply Change of Base (divide by 0.30103) ───── │
│                                                                 │
│    log₂(0.4) = log₁₀(0.4) ÷ log₁₀(2)                          │
│              = −0.3979    ÷  0.30103                            │
│                                                                 │
│    How to do the division:                                      │
│      −0.3979 / 0.30103                                          │
│      = −(0.3979 / 0.30103)   ← handle sign separately          │
│                                                                 │
│      0.3979 / 0.30103 = ?                                       │
│      Try: 0.30103 × 1.0 = 0.30103                               │
│      Try: 0.30103 × 1.3 = 0.39134                               │
│      Try: 0.30103 × 1.32 = 0.39736  ← getting close            │
│      Try: 0.30103 × 1.322 = 0.39796  ≈ 0.3979  ✅              │
│                                                                 │
│    log₂(0.4) = −1.3219   ✅                                     │
│                                                                 │
│  ── Sub-step 7: Sanity check ───────────────────────────────── │
│                                                                 │
│    Verify: does 2^(−1.3219) ≈ 0.4?                             │
│    2^(−1.3219) = 1 / 2^(1.3219)                                 │
│    We know 2^1 = 2 and 2^1.5 = 2.828                           │
│    2^(1.322) ≈ 2 × 2^(0.322) ≈ 2 × 1.250 ≈ 2.500              │
│    1 / 2.500 = 0.400  ✅  Correct!                              │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║  PART F — COMPLETE REFERENCE TABLE (all exam values)     ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
│                                                                 │
│  Prob  │How log₁₀ is derived          │log₁₀(x) │log₂(x)      │
│  ──────┼──────────────────────────────┼─────────┼─────────     │
│  1.000 │log₁₀(1)= 0 always           │  0.0000 │  0.000       │
│  0.900 │log₁₀(9/10)=log₁₀(9)−1       │ −0.0458 │ −0.152       │
│  0.800 │log₁₀(8/10)=3×0.301−1        │ −0.0969 │ −0.322       │
│  0.750 │log₁₀(3/4)=0.4771−0.6021     │ −0.1249 │ −0.415       │
│  0.667 │log₁₀(2/3)=0.3010−0.4771     │ −0.1761 │ −0.585       │
│  0.625 │log₁₀(5/8)=0.699−0.903       │ −0.2041 │ −0.678       │
│  0.600 │log₁₀(6/10)=0.7781−1.000     │ −0.2219 │ −0.737  ←   │
│  0.500 │log₁₀(1/2)=0−0.3010          │ −0.3010 │ −1.000       │
│  0.400 │log₁₀(4/10)=0.6021−1.000     │ −0.3979 │ −1.322  ←   │
│  0.375 │log₁₀(3/8)=0.4771−0.9031     │ −0.4260 │ −1.415       │
│  0.333 │log₁₀(1/3)=0−0.4771          │ −0.4771 │ −1.585       │
│  0.300 │log₁₀(3/10)=0.4771−1.000     │ −0.5229 │ −1.737       │
│  0.250 │log₁₀(1/4)=0−0.6021          │ −0.6021 │ −2.000       │
│  0.200 │log₁₀(2/10)=0.3010−1.000     │ −0.6990 │ −2.322       │
│  0.167 │log₁₀(1/6)=0−0.7781          │ −0.7781 │ −2.585       │
│  0.143 │log₁₀(1/7)≈−0.8451           │ −0.8451 │ −2.807       │
│  0.125 │log₁₀(1/8)=0−3×0.3010        │ −0.9031 │ −3.000       │
│  0.100 │log₁₀(1/10)=0−1.000          │ −1.0000 │ −3.322       │
│                                                                 │
│  ← marks the two values used in our loan dataset example       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║  PART G — QUICK MENTAL ESTIMATION TRICK                  ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
│                                                                 │
│  Anchor points (exact, memorise 4):                            │
│    log₂(1.000) =  0    log₂(0.500) = −1                        │
│    log₂(0.250) = −2    log₂(0.125) = −3                        │
│                                                                 │
│  For any probability p between two anchors, interpolate:       │
│                                                                 │
│  Estimate log₂(0.6):                                           │
│    0.6 is between 0.5 (log=−1) and 1.0 (log=0)                │
│    0.6 is 20% of the way from 0.5→1.0                          │
│    [ (0.6−0.5)/(1.0−0.5) = 0.1/0.5 = 0.2 ]                   │
│    Estimate = −1 + 0.2×(0−(−1)) = −1 + 0.2 = −0.80            │
│    Actual = −0.737  (estimate was good, within 8%)             │
│                                                                 │
│  Estimate log₂(0.4):                                           │
│    0.4 is between 0.25 (log=−2) and 0.5 (log=−1)              │
│    0.4 is 60% of the way from 0.25→0.5                         │
│    [ (0.4−0.25)/(0.5−0.25) = 0.15/0.25 = 0.6 ]               │
│    Estimate = −2 + 0.6×(−1−(−2)) = −2 + 0.6 = −1.40           │
│    Actual = −1.322  (estimate was good, within 6%)             │
│                                                                 │
│  Use estimates for sanity checks — not for final answers!      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 5 — Multiply probability × log value                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  For class Yes:  0.6  × (−0.7370) = −0.4422                    │
│  For class No:   0.4  × (−1.3219) = −0.5288                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 6 — Apply the negative sign (the − in front of Σ)        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  − (−0.4422) = +0.4422                                          │
│  − (−0.5288) = +0.5288                                          │
│                                                                 │
│  💡 The double negative makes entropy always POSITIVE           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 7 — Sum all terms                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  entropy(D) = 0.4422 + 0.5288                                   │
│                                                                 │
│  entropy(D) = 0.9710  ≈ 0.971  ✅                               │
│                                                                 │
│  Interpretation: Close to 1.0 → dataset is quite mixed         │
│  (9 Yes vs 6 No — not too far from 50/50)                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

#### 🔢 Step-by-Step: Entropy Calculation (Example 2 — Pure Node)

**Given:** A subset with **6 Yes** and **0 No** (Own\_House = true branch).

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — Count the classes                                     │
│  Yes = 6,  No = 0,  Total = 6                                   │
├─────────────────────────────────────────────────────────────────┤
│  STEP 2 — Compute probabilities                                 │
│  Pr(Yes) = 6/6 = 1.0                                            │
│  Pr(No)  = 0/6 = 0.0                                            │
├─────────────────────────────────────────────────────────────────┤
│  STEP 3 — Apply formula                                         │
│  entropy = − [1.0 × log₂(1.0)] − [0.0 × log₂(0.0)]            │
├─────────────────────────────────────────────────────────────────┤
│  STEP 4 — Calculate logs                                        │
│  log₂(1.0) = 0     (because 2⁰ = 1)                            │
│  0.0 × log₂(0.0)  = 0  (special convention: 0 × −∞ = 0)        │
├─────────────────────────────────────────────────────────────────┤
│  STEP 5 — Final sum                                             │
│  entropy = − [1.0 × 0] − [0] = 0 + 0 = 0.000  ✅               │
│                                                                 │
│  Interpretation: 0 = perfectly pure → no uncertainty at all!   │
└─────────────────────────────────────────────────────────────────┘
```

---

#### 🔢 Step-by-Step: Entropy Calculation (Example 3 — Subset entropy)

**Given:** A subset with **3 Yes** and **6 No** (Own\_House = false branch, total = 9).

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — Count                                                 │
│  Yes = 3,  No = 6,  Total = 9                                   │
├─────────────────────────────────────────────────────────────────┤
│  STEP 2 — Probabilities                                         │
│  Pr(Yes) = 3/9 = 0.333                                          │
│  Pr(No)  = 6/9 = 0.667                                          │
│  Check:  0.333 + 0.667 = 1.0  ✅                                │
├─────────────────────────────────────────────────────────────────┤
│  STEP 3 — Logs                                                  │
│  log₂(0.333) = log₁₀(0.333) / log₁₀(2)                         │
│              = (−0.4771) / (0.3010) = −1.585                    │
│                                                                 │
│  log₂(0.667) = log₁₀(0.667) / log₁₀(2)                         │
│              = (−0.1761) / (0.3010) = −0.585                    │
├─────────────────────────────────────────────────────────────────┤
│  STEP 4 — Multiply                                              │
│  0.333 × (−1.585) = −0.528                                      │
│  0.667 × (−0.585) = −0.390                                      │
├─────────────────────────────────────────────────────────────────┤
│  STEP 5 — Negate and sum                                        │
│  entropy = −(−0.528) + −(−0.390)                                │
│          = 0.528 + 0.390                                        │
│          = 0.918  ✅                                             │
│                                                                 │
│  Interpretation: 0.918 is quite high → still very mixed        │
└─────────────────────────────────────────────────────────────────┘
```

---

#### 📊 Entropy Intuition Table

| Pr(positive) | Pr(negative) | Calculation | Entropy | Meaning |
|---|---|---|---|---|
| 1/2 = 0.500 | 1/2 = 0.500 | −0.5×(−1) − 0.5×(−1) | **1.000** | Maximum confusion |
| 2/10 = 0.200 | 8/10 = 0.800 | −0.2×(−2.322) − 0.8×(−0.322) | **0.722** | Leaning negative |
| 9/10 = 0.900 | 1/10 = 0.100 | −0.9×(−0.152) − 0.1×(−3.322) | **0.469** | Mostly positive |
| 1.000 | 0.000 | −1×0 − 0×(−∞) | **0.000** | Perfectly pure |

#### 📈 Entropy Curve

```
Entropy
  1.0 ┤         ●         ← Maximum (50/50 split)
      │      ●     ●
  0.8 ┤    ●         ●
      │  ●             ●
  0.6 ┤●                 ●
      │                    ●
  0.4 ┤                      ●
      │                        ●
  0.2 ┤                          ●
      │                             ●
  0.0 ●──────────────────────────────●  ← Zero (pure node)
      0   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0
                              Proportion of Positive Class

Key takeaway:
  entropy = 0    → data is 100% one class   → leaf node, stop splitting!
  entropy = 1    → data is 50/50 split      → most impure, must split!
  entropy = 0.97 → close to 1               → still quite mixed (our root node)
```

---

### 5.2 Information Gain

#### What is Information Gain?

Information Gain tells us **how much an attribute reduces uncertainty** in the data. We always pick the attribute with the **highest gain**.

```
┌──────────────────────────────────────────────────────────────┐
│  CONCEPT: Gain = disorder BEFORE − disorder AFTER split      │
│                                                              │
│  Think of it as:                                             │
│  "If I split the data on attribute A, how much cleaner       │
│   do the resulting groups become?"                           │
│                                                              │
│  Higher gain = attribute creates purer sub-groups            │
│  Lower  gain = attribute barely helps                         │
└──────────────────────────────────────────────────────────────┘
```

---

#### 📐 The Three Formulas

**Formula 1 — Entropy of the current node (before split):**

$$\text{entropy}(D) = -\sum_{j=1}^{|C|} \Pr(c_j) \cdot \log_2 \Pr(c_j)$$

**Formula 2 — Expected (weighted) entropy after splitting on attribute Aᵢ:**

$$\text{entropy}_{A_i}(D) = \sum_{j=1}^{v} \frac{|D_j|}{|D|} \times \text{entropy}(D_j)$$

**Formula 3 — Information Gain:**

$$\text{gain}(D, A_i) = \text{entropy}(D) - \text{entropy}_{A_i}(D)$$

**Complete Notation Reference:**

| Symbol | Meaning | Example |
|---|---|---|
| `D` | Full dataset at current node | All 15 records |
| `Aᵢ` | Attribute being evaluated | "Age" or "Own House" |
| `v` | Number of distinct values of Aᵢ | Age has 3: young/middle/old |
| `j` | Index for each subset | j=1 (young), j=2 (middle), j=3 (old) |
| `Dⱼ` | Subset of D where Aᵢ = its j-th value | D₁ = all young examples |
| `\|Dⱼ\|` | Size (count) of subset Dⱼ | 5 young examples |
| `\|D\|` | Total size of current dataset | 15 total |
| `\|Dⱼ\|/\|D\|` | Weight = proportion of data in this subset | 5/15 = 0.333 |
| `entropy(Dⱼ)` | Entropy of the j-th subset | entropy of young group |

---

#### 🔢 Step-by-Step: Information Gain for Own House

**Split: Own\_House = true (6 examples) vs Own\_House = false (9 examples)**

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — We already know entropy(D) = 0.971  (computed above) │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2 — Identify the subsets created by this split           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Subset D₁ (Own House = true):                                  │
│    Yes = 6,  No = 0,  Size = 6                                  │
│                                                                 │
│  Subset D₂ (Own House = false):                                 │
│    Yes = 3,  No = 6,  Size = 9                                  │
│                                                                 │
│  Check: |D₁| + |D₂| = 6 + 9 = 15 = |D|  ✅                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3 — Compute entropy of each subset                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  entropy(D₁) — Own House = true branch:                        │
│    Pr(Yes) = 6/6 = 1.0,  Pr(No) = 0/6 = 0.0                   │
│    entropy = −(1.0 × log₂1.0) − (0.0 × log₂0.0)               │
│            = −(1.0 × 0) − 0                                    │
│            = 0.000  ← PURE! ✅                                  │
│                                                                 │
│  entropy(D₂) — Own House = false branch:                       │
│    Pr(Yes) = 3/9 = 0.333,  Pr(No) = 6/9 = 0.667               │
│    log₂(0.333) = −1.585,  log₂(0.667) = −0.585                 │
│    entropy = −(0.333 × −1.585) − (0.667 × −0.585)              │
│            = −(−0.528) − (−0.390)                               │
│            = 0.528 + 0.390                                      │
│            = 0.918                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 4 — Compute the weights for each subset                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Weight of D₁ = |D₁| / |D| = 6 / 15 = 0.400                   │
│  Weight of D₂ = |D₂| / |D| = 9 / 15 = 0.600                   │
│                                                                 │
│  Check: 0.400 + 0.600 = 1.0  ✅                                 │
│                                                                 │
│  Why weights? Because larger subsets matter more!               │
│  A 14-example pure subset is more impressive than a            │
│  1-example pure subset.                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 5 — Compute the weighted (expected) entropy              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  entropy_OwnHouse(D) = (6/15) × entropy(D₁)                    │
│                      + (9/15) × entropy(D₂)                    │
│                                                                 │
│                      = (6/15) × 0.000                           │
│                      + (9/15) × 0.918                           │
│                                                                 │
│                      = 0.400 × 0.000                            │
│                      + 0.600 × 0.918                            │
│                                                                 │
│                      = 0.000 + 0.551                            │
│                                                                 │
│                      = 0.551                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 6 — Compute Information Gain                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  gain(D, Own House) = entropy(D) − entropy_OwnHouse(D)         │
│                     = 0.971     −  0.551                        │
│                     = 0.420   ✅  ← HIGHEST GAIN               │
│                                                                 │
│  Meaning: Splitting on Own House reduces entropy               │
│           from 0.971 → 0.551 (a drop of 0.420)                 │
│           One branch becomes perfectly pure!                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5.3 Gain Ratio

#### Why Gain Ratio Is Needed

Information Gain has a bias problem. Consider a useless attribute like "Customer ID" — it has 15 unique values for 15 examples, creating 15 perfectly pure subsets of 1 example each. Gain would be maximum (0.971), but this attribute is **completely useless** for prediction!

```
┌──────────────────────────────────────────────────────────────────┐
│  PROBLEM: Gain is biased toward high-cardinality attributes      │
│                                                                  │
│  Customer ID: 15 values → 15 subsets of 1 → each is pure        │
│               Gain = 0.971  (looks amazing but is useless!)     │
│                                                                  │
│  Own House:   2 values → 2 subsets → one is pure                │
│               Gain = 0.420  (actually useful!)                  │
│                                                                  │
│  FIX: Divide gain by how "wide" the split was → Gain Ratio      │
└──────────────────────────────────────────────────────────────────┘
```

---

#### 📐 The Gain Ratio Formulas

**Formula 1 — Split Information (measures how wide/even the split is):**

$$\text{SplitInfo}(A_i) = -\sum_{j=1}^{v} \frac{|D_j|}{|D|} \cdot \log_2 \frac{|D_j|}{|D|}$$

> 💡 SplitInfo is **exactly entropy applied to the split proportions** (not the class labels). It penalises attributes that split data into many or very unequal parts.

**Formula 2 — Gain Ratio:**

$$\text{GainRatio}(D, A_i) = \frac{\text{gain}(D, A_i)}{\text{SplitInfo}(A_i)}$$

---

#### 🔢 Step-by-Step: Gain Ratio for Own House

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — We already know:                                      │
│    gain(D, Own House) = 0.420                                   │
│    Split: 6 examples in D₁, 9 examples in D₂, total = 15       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2 — Compute split proportions                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  |D₁|/|D| = 6/15 = 0.400                                       │
│  |D₂|/|D| = 9/15 = 0.600                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3 — Compute logs of split proportions                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  log₂(0.400) = log₁₀(0.400) / log₁₀(2)                         │
│              = (−0.3979) / (0.3010) = −1.3219                   │
│                                                                 │
│  log₂(0.600) = log₁₀(0.600) / log₁₀(2)                         │
│              = (−0.2218) / (0.3010) = −0.7370                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 4 — Compute SplitInfo                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SplitInfo(Own House) = − [0.400 × (−1.3219)]                   │
│                        − [0.600 × (−0.7370)]                   │
│                                                                 │
│                       = − (−0.5288) − (−0.4422)                 │
│                       = 0.5288 + 0.4422                         │
│                       = 0.9710                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 5 — Compute Gain Ratio                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  GainRatio(D, Own House) = gain / SplitInfo                     │
│                          = 0.420 / 0.971                        │
│                          = 0.432  ✅                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

#### 🔢 Step-by-Step: Gain Ratio for Age (to see penalty in action)

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — We already know:                                      │
│    gain(D, Age) = 0.083                                         │
│    Split: 5 young, 5 middle, 5 old  (perfectly equal thirds)   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2 — Split proportions                                    │
│    5/15 = 5/15 = 5/15 = 0.333 each                             │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3 — Log of split proportion                              │
│    log₂(0.333) = log₁₀(0.333)/log₁₀(2) = −0.4771/0.3010       │
│               = −1.585                                          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 4 — SplitInfo for Age                                    │
│    = −[0.333×(−1.585)] − [0.333×(−1.585)] − [0.333×(−1.585)]  │
│    = 3 × [0.333 × 1.585]                                        │
│    = 3 × 0.528 = 1.585                                          │
│                                                                 │
│  Note: 1.585 = log₂(3) — 3 equal branches always gives this    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 5 — Gain Ratio for Age                                   │
│    = gain / SplitInfo = 0.083 / 1.585 = 0.052                  │
│                                                                 │
│  Compare:                                                       │
│    GainRatio(Own House) = 0.432   ← wins by a huge margin!     │
│    GainRatio(Age)       = 0.052   ← penalised for 3 branches   │
│                                                                 │
│  Conclusion: Own House is STILL the best root  ✅               │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5.4 Gini Impurity (CART)

Used by the **CART** algorithm (sklearn's default in Python).

#### 📐 The Formula

$$\text{Gini}(D) = 1 - \sum_{j=1}^{|C|} \Pr(c_j)^2$$

**Breaking down every symbol:**

| Symbol | Meaning |
|---|---|
| `1` | We start from 1 (maximum) and subtract purity |
| `Pr(cⱼ)²` | Square of each class probability |
| `Σ Pr(cⱼ)²` | Sum of squared probabilities = measure of "how pure" |
| `1 − Σ Pr(cⱼ)²` | 1 minus purity = impurity |

> 💡 **Intuition:** If all examples are one class, Pr = 1.0 → 1² = 1 → Gini = 1 − 1 = 0 (pure). If 50/50 split → (0.5² + 0.5²) = 0.5 → Gini = 1 − 0.5 = 0.5 (maximum impurity).

---

#### 🔢 Step-by-Step: Gini for the Root Node (9 Yes, 6 No)

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — Class probabilities                                   │
│    Pr(Yes) = 9/15 = 0.600                                       │
│    Pr(No)  = 6/15 = 0.400                                       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2 — Square each probability                              │
│    Pr(Yes)² = 0.600² = 0.360                                    │
│    Pr(No)²  = 0.400² = 0.160                                    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3 — Sum the squares                                      │
│    Σ Pr(cⱼ)² = 0.360 + 0.160 = 0.520                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 4 — Subtract from 1                                      │
│    Gini(D) = 1 − 0.520 = 0.480  ✅                              │
│                                                                 │
│  Compare: Entropy was 0.971 → different scale but same meaning │
│  Both tell us the data is impure and needs splitting            │
└─────────────────────────────────────────────────────────────────┘
```

---

#### 📊 Entropy vs Gini — Side-by-Side Comparison

| Scenario | Pr(+) | Pr(−) | Entropy Calculation | Entropy | Gini Calculation | Gini |
|---|---|---|---|---|---|---|
| Equal split | 0.5 | 0.5 | −0.5log₂0.5−0.5log₂0.5 | **1.000** | 1−(0.25+0.25) | **0.500** |
| 80/20 split | 0.8 | 0.2 | −0.8log₂0.8−0.2log₂0.2 | **0.722** | 1−(0.64+0.04) | **0.320** |
| 90/10 split | 0.9 | 0.1 | −0.9log₂0.9−0.1log₂0.1 | **0.469** | 1−(0.81+0.01) | **0.180** |
| Pure node   | 1.0 | 0.0 | −1×0 − 0 | **0.000** | 1−(1.00+0.00) | **0.000** |

**Key difference:** Entropy is more sensitive to class imbalance (uses log), Gini is faster to compute (no log). Both produce the same tree most of the time.

---

## 6. The Algorithm

```
Algorithm: decisionTree(D, A, T)
────────────────────────────────────────────────────────────
INPUT:
  D = set of training examples
  A = set of available attributes
  T = current tree node

────────────────────────────────────────────────────────────
1.  IF all examples in D belong to same class cᵢ:
        → make T a LEAF node labeled cᵢ
        → RETURN

2.  ELSE IF A is empty (no attributes left):
        → make T a LEAF node labeled with MAJORITY class in D
        → RETURN

3.  ELSE:  (D has mixed classes, attributes available)

    a. Compute p₀ = entropy(D)      ← baseline impurity

    b. FOR each attribute Aᵢ in A:
           compute pᵢ = entropy_Aᵢ(D)   ← post-split impurity

    c. Select Ag = attribute with MAXIMUM (p₀ - pᵢ)
                                         ← best gain

    d. IF (p₀ - p_Ag) < threshold:       ← gain too small
           → make T a LEAF with majority class
           → RETURN   (Pre-pruning)

    e. ELSE:
           → make T a DECISION NODE on Ag

           FOR each value vⱼ of Ag:
               Dⱼ = subset of D where Ag = vⱼ
               IF Dⱼ ≠ empty:
                   create child node Tⱼ
                   decisionTree(Dⱼ, A - {Ag}, Tⱼ)  ← recurse!
────────────────────────────────────────────────────────────
```

### Key Properties

```
TYPE:       Greedy, top-down, recursive divide-and-conquer
GUARANTEE:  Locally optimal (not globally optimal)
COMPLEXITY: Finding BEST tree is NP-hard → use heuristics
UNIQUENESS: Decision trees are NOT unique for the same data
```

---

## 7. Worked Example — Loan Dataset

### The Data (15 examples, 4 features)

| ID | Age | Has\_Job | Own\_House | Credit\_Rating | Class |
|---|---|---|---|---|---|
| 1 | young | false | false | fair | **No** |
| 2 | young | false | false | good | **No** |
| 3 | young | true | false | good | **Yes** |
| 4 | young | true | true | fair | **Yes** |
| 5 | young | false | false | fair | **No** |
| 6 | middle | false | false | fair | **No** |
| 7 | middle | false | false | good | **No** |
| 8 | middle | true | true | good | **Yes** |
| 9 | middle | false | true | excellent | **Yes** |
| 10 | middle | false | true | excellent | **Yes** |
| 11 | old | false | true | excellent | **Yes** |
| 12 | old | false | true | good | **Yes** |
| 13 | old | true | false | good | **Yes** |
| 14 | old | true | false | excellent | **Yes** |
| 15 | old | false | false | fair | **No** |

**Summary:** 9 Yes, 6 No out of 15 total

---

### ▶ STEP 1 — Compute Root Entropy

**Goal:** Find entropy(D) for the entire dataset before any split.

```
┌─────────────────────────────────────────────────────────────────┐
│  Count classes:                                                 │
│    Yes = 9  (IDs: 3,4,8,9,10,11,12,13,14)                      │
│    No  = 6  (IDs: 1,2,5,6,7,15)                                 │
│    Total = 15                                                   │
├─────────────────────────────────────────────────────────────────┤
│  Compute probabilities:                                         │
│    Pr(Yes) = 9/15 = 0.600                                       │
│    Pr(No)  = 6/15 = 0.400                                       │
│    Check:  0.600 + 0.400 = 1.0  ✅                              │
├─────────────────────────────────────────────────────────────────┤
│  Compute logs:                                                  │
│    log₂(0.600) = log₁₀(0.600)/log₁₀(2) = −0.2218/0.3010       │
│                = −0.7370                                        │
│    log₂(0.400) = log₁₀(0.400)/log₁₀(2) = −0.3979/0.3010       │
│                = −1.3219                                        │
├─────────────────────────────────────────────────────────────────┤
│  Multiply and negate:                                           │
│    Yes term: −(0.600 × −0.7370) = −(−0.4422) = +0.4422         │
│    No  term: −(0.400 × −1.3219) = −(−0.5288) = +0.5288         │
├─────────────────────────────────────────────────────────────────┤
│  Sum:                                                           │
│    entropy(D) = 0.4422 + 0.5288 = 0.9710 ≈ 0.971  ✅           │
└─────────────────────────────────────────────────────────────────┘
```

$$\text{entropy}(D) = -\frac{9}{15}\log_2\frac{9}{15} - \frac{6}{15}\log_2\frac{6}{15} = \mathbf{0.971}$$

---

### ▶ STEP 2 — Compute Gain for Every Attribute

We compute gain for all 4 attributes and pick the winner.

---

#### 📌 Attribute A: Age (3 values: young / middle / old)

**First, separate the data into 3 groups:**

```
Group young  (IDs 1–5):  Yes=2, No=3, Total=5
Group middle (IDs 6–10): Yes=3, No=2, Total=5
Group old    (IDs 11–15): Yes=4, No=1, Total=5
```

**Compute entropy for each group:**

```
┌────────────────────── entropy(D_young) ──────────────────────┐
│  Yes=2, No=3, Total=5                                        │
│  Pr(Yes) = 2/5 = 0.400,  Pr(No) = 3/5 = 0.600               │
│                                                              │
│  log₂(0.400) = −1.3219                                       │
│  log₂(0.600) = −0.7370                                       │
│                                                              │
│  entropy = −(0.400 × −1.3219) − (0.600 × −0.7370)           │
│          = 0.5288 + 0.4422                                   │
│          = 0.9710 ≈ 0.971                                    │
└──────────────────────────────────────────────────────────────┘

┌────────────────────── entropy(D_middle) ─────────────────────┐
│  Yes=3, No=2, Total=5                                        │
│  Pr(Yes) = 3/5 = 0.600,  Pr(No) = 2/5 = 0.400               │
│                                                              │
│  Same probabilities as young (just swapped) → same entropy  │
│  entropy = 0.971                                             │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────── entropy(D_old) ──────────────────────┐
│  Yes=4, No=1, Total=5                                        │
│  Pr(Yes) = 4/5 = 0.800,  Pr(No) = 1/5 = 0.200               │
│                                                              │
│  log₂(0.800) = log₁₀(0.800)/log₁₀(2) = −0.0969/0.3010       │
│              = −0.3219                                       │
│  log₂(0.200) = log₁₀(0.200)/log₁₀(2) = −0.6990/0.3010       │
│              = −2.3219                                       │
│                                                              │
│  entropy = −(0.800 × −0.3219) − (0.200 × −2.3219)           │
│          = 0.2575 + 0.4644                                   │
│          = 0.7219 ≈ 0.722                                    │
└──────────────────────────────────────────────────────────────┘
```

**Compute weighted entropy for Age:**

```
┌─────────────────────────────────────────────────────────────────┐
│  entropy_Age(D) = (|D_young|/|D|) × entropy(D_young)           │
│                + (|D_middle|/|D|) × entropy(D_middle)          │
│                + (|D_old|/|D|)   × entropy(D_old)              │
│                                                                 │
│                = (5/15) × 0.971                                 │
│                + (5/15) × 0.971                                 │
│                + (5/15) × 0.722                                 │
│                                                                 │
│                = 0.3333 × 0.971                                 │
│                + 0.3333 × 0.971                                 │
│                + 0.3333 × 0.722                                 │
│                                                                 │
│                = 0.3237 + 0.3237 + 0.2407                      │
│                                                                 │
│                = 0.888                                          │
└─────────────────────────────────────────────────────────────────┘
```

**Compute Gain for Age:**

```
┌─────────────────────────────────────────────────────────────────┐
│  gain(D, Age) = entropy(D) − entropy_Age(D)                    │
│              = 0.971 − 0.888                                    │
│              = 0.083                                            │
│                                                                 │
│  Interpretation: Age reduces entropy by only 0.083 — not much! │
└─────────────────────────────────────────────────────────────────┘
```

| Age group | Yes | No | Total | Weight | Entropy | Weighted |
|---|---|---|---|---|---|---|
| young | 2 | 3 | 5 | 5/15=0.333 | 0.971 | 0.324 |
| middle | 3 | 2 | 5 | 5/15=0.333 | 0.971 | 0.324 |
| old | 4 | 1 | 5 | 5/15=0.333 | 0.722 | 0.241 |
| **Total** | | | | | **entropy\_Age** | **0.888** |

$$\text{gain}(D, \text{Age}) = 0.971 - 0.888 = \mathbf{0.083}$$

---

#### 📌 Attribute B: Own House (2 values: true / false)

**Separate data:**

```
Group true  (IDs 4,8,9,10,11,12): Yes=6, No=0, Total=6
Group false (IDs 1,2,3,5,6,7,13,14,15): Yes=3, No=6, Total=9
```

**Compute entropy for each group:**

```
┌──────────────── entropy(D_true) ─────────────────────────────┐
│  Yes=6, No=0, Total=6                                        │
│  Pr(Yes) = 6/6 = 1.000,  Pr(No) = 0/6 = 0.000               │
│                                                              │
│  log₂(1.000) = 0   (because 2⁰ = 1)                         │
│  0.000 × log₂(0.000) = 0  (convention)                      │
│                                                              │
│  entropy = −(1.000 × 0) − (0)                                │
│          = 0.000  ← PERFECTLY PURE ✅                        │
└──────────────────────────────────────────────────────────────┘

┌──────────────── entropy(D_false) ────────────────────────────┐
│  Yes=3, No=6, Total=9                                        │
│  Pr(Yes) = 3/9 = 0.333,  Pr(No) = 6/9 = 0.667               │
│                                                              │
│  log₂(0.333) = log₁₀(0.333)/log₁₀(2) = −0.4771/0.3010       │
│              = −1.5850                                       │
│  log₂(0.667) = log₁₀(0.667)/log₁₀(2) = −0.1761/0.3010       │
│              = −0.5850                                       │
│                                                              │
│  entropy = −(0.333 × −1.5850) − (0.667 × −0.5850)           │
│          = 0.5278 + 0.3902                                   │
│          = 0.9180 ≈ 0.918                                    │
└──────────────────────────────────────────────────────────────┘
```

**Compute weighted entropy for Own House:**

```
┌─────────────────────────────────────────────────────────────────┐
│  entropy_OwnHouse(D) = (6/15) × entropy(D_true)                │
│                      + (9/15) × entropy(D_false)               │
│                                                                 │
│                      = (6/15) × 0.000                           │
│                      + (9/15) × 0.918                           │
│                                                                 │
│                      = 0.400 × 0.000                            │
│                      + 0.600 × 0.918                            │
│                                                                 │
│                      = 0.000 + 0.551                            │
│                                                                 │
│                      = 0.551                                    │
└─────────────────────────────────────────────────────────────────┘
```

**Compute Gain for Own House:**

```
┌─────────────────────────────────────────────────────────────────┐
│  gain(D, Own House) = entropy(D) − entropy_OwnHouse(D)         │
│                     = 0.971 − 0.551                             │
│                     = 0.420  ✅  ← HIGHEST GAIN!               │
│                                                                 │
│  Why so high? Because the "true" branch is perfectly pure      │
│  (all 6 examples are Yes → entropy = 0)                        │
└─────────────────────────────────────────────────────────────────┘
```

| Own House | Yes | No | Total | Weight | Entropy | Weighted |
|---|---|---|---|---|---|---|
| true | 6 | 0 | 6 | 6/15=0.400 | 0.000 | 0.000 |
| false | 3 | 6 | 9 | 9/15=0.600 | 0.918 | 0.551 |
| **Total** | | | | | **entropy\_OwnHouse** | **0.551** |

$$\text{gain}(D, \text{OwnHouse}) = 0.971 - 0.551 = \mathbf{0.420}$$ ✅ **HIGHEST!**

---

#### 📌 Attribute C: Has Job (2 values: true / false)

**Separate data:**

```
Group true  (IDs 3,4,8,13,14): Yes=5, No=0, Total=5
Group false (IDs 1,2,5,6,7,9,10,11,12,15): Yes=4, No=6, Total=10
```

**Compute entropy for each group:**

```
┌──────────────── entropy(D_true) ─────────────────────────────┐
│  Yes=5, No=0, Total=5                                        │
│  Pr(Yes) = 5/5 = 1.000,  Pr(No) = 0/5 = 0.000               │
│  entropy = 0.000  ← PURE ✅                                   │
└──────────────────────────────────────────────────────────────┘

┌──────────────── entropy(D_false) ────────────────────────────┐
│  Yes=4, No=6, Total=10                                       │
│  Pr(Yes) = 4/10 = 0.400,  Pr(No) = 6/10 = 0.600             │
│                                                              │
│  log₂(0.400) = −1.3219                                       │
│  log₂(0.600) = −0.7370                                       │
│                                                              │
│  entropy = −(0.400 × −1.3219) − (0.600 × −0.7370)           │
│          = 0.5288 + 0.4422                                   │
│          = 0.971                                             │
└──────────────────────────────────────────────────────────────┘
```

**Compute weighted entropy for Has Job:**

```
┌─────────────────────────────────────────────────────────────────┐
│  entropy_HasJob(D) = (5/15) × entropy(D_true)                  │
│                   + (10/15) × entropy(D_false)                  │
│                                                                 │
│                   = (5/15) × 0.000                              │
│                   + (10/15) × 0.971                             │
│                                                                 │
│                   = 0.3333 × 0.000                              │
│                   + 0.6667 × 0.971                              │
│                                                                 │
│                   = 0.000 + 0.647                               │
│                                                                 │
│                   = 0.647                                       │
└─────────────────────────────────────────────────────────────────┘
```

**Compute Gain for Has Job:**

```
┌─────────────────────────────────────────────────────────────────┐
│  gain(D, Has Job) = entropy(D) − entropy_HasJob(D)             │
│                  = 0.971 − 0.647                                │
│                  = 0.324                                        │
└─────────────────────────────────────────────────────────────────┘
```

| Has Job | Yes | No | Total | Weight | Entropy | Weighted |
|---|---|---|---|---|---|---|
| true | 5 | 0 | 5 | 5/15=0.333 | 0.000 | 0.000 |
| false | 4 | 6 | 10 | 10/15=0.667 | 0.971 | 0.647 |
| **Total** | | | | | **entropy\_HasJob** | **0.647** |

$$\text{gain}(D, \text{HasJob}) = 0.971 - 0.647 = \mathbf{0.324}$$

---

#### 📌 Attribute D: Credit Rating (3 values: fair / good / excellent)

**Separate data:**

```
Group fair      (IDs 1,4,5,6,15): Yes=1, No=4, Total=5
Group good      (IDs 2,3,7,8,12,13): Yes=4, No=2, Total=6
Group excellent (IDs 9,10,11,14): Yes=4, No=0, Total=4
```

**Compute entropy for each group:**

```
┌──────────────── entropy(D_fair) ─────────────────────────────┐
│  Yes=1, No=4, Total=5                                        │
│  Pr(Yes) = 1/5 = 0.200,  Pr(No) = 4/5 = 0.800               │
│                                                              │
│  log₂(0.200) = log₁₀(0.200)/log₁₀(2) = −0.6990/0.3010       │
│              = −2.3219                                       │
│  log₂(0.800) = log₁₀(0.800)/log₁₀(2) = −0.0969/0.3010       │
│              = −0.3219                                       │
│                                                              │
│  entropy = −(0.200 × −2.3219) − (0.800 × −0.3219)           │
│          = 0.4644 + 0.2575                                   │
│          = 0.7219 ≈ 0.722                                    │
└──────────────────────────────────────────────────────────────┘

┌──────────────── entropy(D_good) ─────────────────────────────┐
│  Yes=4, No=2, Total=6                                        │
│  Pr(Yes) = 4/6 = 0.667,  Pr(No) = 2/6 = 0.333               │
│                                                              │
│  log₂(0.667) = −0.5850                                       │
│  log₂(0.333) = −1.5850                                       │
│                                                              │
│  entropy = −(0.667 × −0.5850) − (0.333 × −1.5850)           │
│          = 0.3902 + 0.5278                                   │
│          = 0.9180 ≈ 0.918                                    │
└──────────────────────────────────────────────────────────────┘

┌──────────────── entropy(D_excellent) ────────────────────────┐
│  Yes=4, No=0, Total=4                                        │
│  Pr(Yes) = 4/4 = 1.000,  Pr(No) = 0/4 = 0.000               │
│  entropy = 0.000  ← PURE ✅                                   │
└──────────────────────────────────────────────────────────────┘
```

**Compute weighted entropy for Credit Rating:**

```
┌─────────────────────────────────────────────────────────────────┐
│  entropy_CreditRating(D) = (5/15) × entropy(D_fair)            │
│                          + (6/15) × entropy(D_good)            │
│                          + (4/15) × entropy(D_excellent)       │
│                                                                 │
│                          = (5/15) × 0.722                       │
│                          + (6/15) × 0.918                       │
│                          + (4/15) × 0.000                       │
│                                                                 │
│                          = 0.3333 × 0.722                       │
│                          + 0.4000 × 0.918                       │
│                          + 0.2667 × 0.000                       │
│                                                                 │
│                          = 0.2407 + 0.3672 + 0.000             │
│                                                                 │
│                          = 0.6079 ≈ 0.608                      │
└─────────────────────────────────────────────────────────────────┘
```

**Compute Gain for Credit Rating:**

```
┌─────────────────────────────────────────────────────────────────┐
│  gain(D, Credit Rating) = entropy(D) − entropy_CreditRating(D) │
│                         = 0.971 − 0.608                         │
│                         = 0.363                                 │
└─────────────────────────────────────────────────────────────────┘
```

| Credit Rating | Yes | No | Total | Weight | Entropy | Weighted |
|---|---|---|---|---|---|---|
| fair | 1 | 4 | 5 | 5/15=0.333 | 0.722 | 0.241 |
| good | 4 | 2 | 6 | 6/15=0.400 | 0.918 | 0.367 |
| excellent | 4 | 0 | 4 | 4/15=0.267 | 0.000 | 0.000 |
| **Total** | | | | | **entropy\_CreditRating** | **0.608** |

$$\text{gain}(D, \text{CreditRating}) = 0.971 - 0.608 = \mathbf{0.363}$$

---

### ▶ STEP 3 — Compare All Gains and Pick the Root

```
┌─────────────────────────────────────────────────────────────────┐
│           GAIN COMPARISON SUMMARY                               │
├────────────────────┬──────────────────┬────────────┬───────────┤
│ Attribute          │ Weighted Entropy │ Gain       │ Rank      │
├────────────────────┼──────────────────┼────────────┼───────────┤
│ Age                │ 0.888            │ 0.083      │ 4th (worst)│
│ Has Job            │ 0.647            │ 0.324      │ 3rd       │
│ Credit Rating      │ 0.608            │ 0.363      │ 2nd       │
│ Own House          │ 0.551            │ 0.420      │ 1st ✅    │
└────────────────────┴──────────────────┴────────────┴───────────┘

WINNER: Own House (gain = 0.420)
→ Own House becomes the ROOT NODE of the tree!

Why? Because splitting on Own House reduces entropy
from 0.971 → 0.551 — the biggest reduction of all 4 attributes.
One branch (Own House = true) becomes perfectly pure: all 6 are Yes!
```

---

### ▶ STEP 4 — Recurse on Each Branch

#### Branch 1: Own House = true → 6 Yes, 0 No

```
entropy(D_true) = 0.000  ← Pure!
→ STOP. Make a LEAF node: Class = Yes  (6/6 correct)
```

#### Branch 2: Own House = false → 3 Yes, 6 No (9 examples)

This branch is still impure (entropy = 0.918), so we recurse.
Compute gain for remaining attributes on these 9 examples:

**Re-compute root entropy for this sub-problem:**

```
Pr(Yes) = 3/9 = 0.333,  Pr(No) = 6/9 = 0.667
entropy(D_false) = −(0.333×log₂0.333) − (0.667×log₂0.667)
                 = 0.528 + 0.390 = 0.918
```

**Evaluate Has Job on the 9 "false" examples:**

```
Among Own House = false records:
  Has Job = true:  IDs 3,13,14 → Yes=3, No=0 → Total=3 → entropy=0.000
  Has Job = false: IDs 1,2,5,6,7,15 → Yes=0, No=6 → Total=6 → entropy=0.000

entropy_HasJob(D_false) = (3/9)×0.000 + (6/9)×0.000 = 0.000

gain(D_false, Has Job) = 0.918 − 0.000 = 0.918  ← PERFECT!
```

```
→ Has Job splits perfectly within the "false" branch:
    Has Job = true  → 3 Yes, 0 No → LEAF: Yes  (3/3)
    Has Job = false → 0 Yes, 6 No → LEAF: No   (6/6)
```

---

### ▶ FINAL TREE

```
                    ┌──────────────────┐
                    │  Own_House?      │  ← Root (gain=0.420)
                    └────────┬─────────┘
               ┌─────────────┴──────────────┐
             true                         false
               │                              │
          ✅ Yes                    ┌──────────┴──────────┐
          (6/6)                     │     Has_Job?        │
                                    └──────────┬──────────┘
                                ┌──────────────┴────────────┐
                              true                        false
                                │                              │
                            ✅ Yes                        ❌ No
                             (5/5)                         (4/4)

Rules extracted:
  Own House = true               → Yes  [conf=6/6=100%]
  Own House = false, Has Job = true  → Yes  [conf=5/5=100%]
  Own House = false, Has Job = false → No   [conf=4/4=100%]

Overall accuracy: 15/15 = 100% on training data
```

---

## 8. Tree → Rules Conversion

Each path from root to leaf = one IF-THEN rule

```
Own_house = true
    → Class = Yes    [support=6/15=40%, confidence=6/6=100%]

Own_house = false AND Has_job = true
    → Class = Yes    [support=5/15=33%, confidence=5/5=100%]

Own_house = false AND Has_job = false
    → Class = No     [support=4/15=27%, confidence=4/4=100%]
```

### Rule Metrics

| Metric | Formula | Meaning |
|---|---|---|
| **Support** | (# examples covered by rule) / (total examples) | How often the rule fires |
| **Confidence** | (# correctly classified) / (# covered) | How accurate the rule is |
| **Coverage** | Same as support (alternate name) | — |
| **Lift** | Confidence / Pr(class) | Improvement over random guessing |

---

## 9. Handling Continuous Attributes

### The Challenge

Continuous features (like Age=22, 35, 47…) can't be used directly for categorical splits.

### Solution: Binary Threshold Split

```
Approach:
1. Sort all values of continuous attribute: v₁ < v₂ < ... < vᵣ
2. Candidate thresholds = midpoints between adjacent values
   → t₁ = (v₁+v₂)/2, t₂ = (v₂+v₃)/2, ...
3. For each threshold tᵢ, create 2 branches:
   LEFT: examples where attribute ≤ tᵢ
   RIGHT: examples where attribute > tᵢ
4. Compute gain for each threshold
5. Pick threshold with MAXIMUM gain
```

### Example

```
Age values: [22, 25, 28, 35, 40]
Classes:    [No, No, Yes, Yes, Yes]

Candidate thresholds: 23.5, 26.5, 31.5, 37.5

Threshold 26.5:
  Left  (≤26.5): 22, 25  → [No, No]  → entropy = 0
  Right (>26.5): 28,35,40 → [Yes,Yes,Yes] → entropy = 0
  → gain = max possible!  ✅ Best threshold = 26.5
```

### Visual (from slides)

```
Y-axis
  2.6 │ ■ ■ ○ ○ ○              Corresponding Decision Tree:
  2.5 │ ■ ○ ○ ○ ○                        [X ≤ 2?]
  2.0 │ ■ ■ ○○■ ■                        /       \
      │ ■ ■ ■ ■○ ■              [Y ≤ 2.5]        [Y ≤ 2]
      └──────────── X-axis
         2   3   4
         
■ = Class 1,  ○ = Class 2
Horizontal/vertical splits partition the space
```

> ⚠️ Note: The SAME continuous attribute can be reused at different nodes with different thresholds!

---

## 10. Overfitting & Pruning

### What is Overfitting?

```
Overfitting = Tree memorizes training data
              → Perfect training accuracy
              → Poor test/real-world accuracy

Signs:
  • Tree is very deep (many levels)
  • Many branches with very few examples
  • Leaf nodes with 1-2 examples
  • Training accuracy >> Test accuracy
```

```
Training Data          Overfitted Tree        Generalized Tree
    ● ○ ●                   ┌─┐                    ┌─────┐
  ○ ● ○ ○            ┌─┐   │ │   ┌─┐              │     │
    ● ○ ●            │ │  ...│...  │ │         ┌───┘     └───┐
                  (very deep, fits noise)    (simpler, robust)
```

### Two Types of Pruning

#### Pre-Pruning (Early Stopping)

Stop growing the tree **before** it becomes too complex.

```
Conditions to stop:
  • Gain < threshold (e.g., gain < 0.01)
  • Node has < min_samples (e.g., < 5 examples)
  • Tree depth > max_depth
  • Statistical test shows improvement is not significant

PRO: Fast
CON: May stop too early (underfitting risk)
     Hard to know what you might miss
```

#### Post-Pruning (Preferred)

Grow a full tree FIRST, then trim it back.

```
Process:
  1. Grow full tree (no stopping conditions)
  2. Evaluate each subtree
  3. Compare: leaf_node vs full_subtree
     • Estimate error of subtree on validation data
     • If leaf ≥ subtree in accuracy → replace subtree with leaf
  4. Repeat bottom-up until no improvement

Methods:
  • C4.5: Pessimistic error estimation
  • Reduced Error Pruning: Use held-out validation set
  • Cost-Complexity Pruning (sklearn): α parameter

PRO: More reliable, empirically better
CON: Slightly slower (build full tree first)
```

### Visual: Before and After Pruning

```
BEFORE PRUNING (Overfitted):        AFTER PRUNING (Cleaner):

         [X]                                [X]
        /   \                              /   \
      ≤2     >2                          ≤2     >2
      /       \                          ■       [Y]
   [Y]         [Y]                              /   \
   / \         / \                           ≤2      >2
 ≤2.5 >2.5   ≤2  >2                         [X]      ○
 /    [Y]    [X]  ○                         / \
■     /\    / \                           ≤3   >3
   ≤2.6 >2.6 ≤3 >3                        ■   [X]
   ○    ■    ■  [X]                           / \
                /\                           ≤4  >4
              ≤4  >4                         ○   ■
              ○    ■
```

---

## 11. Algorithm Variants

| Algorithm | Year | Split Criterion | Splits | Handles Continuous | Missing Values |
|---|---|---|---|---|---|
| **ID3** | 1986 | Information Gain | Multi-way | ❌ No | ❌ No |
| **C4.5** | 1993 | Gain Ratio | Multi-way | ✅ Yes | ✅ Yes |
| **CART** | 1984 | Gini Impurity | Binary only | ✅ Yes | ✅ Yes |
| **CHAID** | 1980 | Chi-Square | Multi-way | ✅ Yes | ✅ Yes |
| **C5.0** | 2000s | Gain Ratio | Multi-way | ✅ Yes | ✅ Yes |

### ID3 vs C4.5 vs CART

```
ID3:                    C4.5:                   CART:
• Simple, classic       • Most popular          • sklearn default
• Gain only             • Gain Ratio            • Gini Impurity
• Categorical only      • Continuous ok         • Binary splits only
• Prone to bias         • Handles missing       • Regression too
                        • Post-pruning          • Produces 2-way splits
```

### Decision Trees in Ensembles

```
Single Tree          Random Forest           Gradient Boosting
    [T]              [T₁][T₂]...[Tₙ]         T₁→T₂→T₃→...→Tₙ
     │               Each trained on          Each tree corrects
     ↓               random data subset       errors of previous
  Prediction         + random features
                     Average predictions
                     
• High variance     • Low variance           • Low bias
• Interpretable     • Not interpretable      • Not interpretable
• Fast              • Slower                 • Slowest
```

---

## 12. Visualizations & Diagrams

### Entropy as a Function of Class Balance

```
      Entropy
  1.0 ┤         ●         ← Most impure (50/50)
      │      ●     ●
  0.8 ┤    ●         ●
      │  ●             ●
  0.6 ┤●                 ●
      │                    ●
  0.4 ┤                      ●
      │                        ●
  0.2 ┤                          ●
      │                             ●
  0.0 ●──────────────────────────────●  ← Pure (0/100 or 100/0)
      0   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0
                              Proportion of Positive Class
```

### Information Gain = Area Saved

```
Before Split:          After Split on Attr A:
┌──────────────┐       ┌──────┐  ┌──────────┐
│ ○ ● ● ○ ● ○ │  →   │ ● ● │  │ ○ ○ ○ ○ │
│ ○ ○ ● ● ○ ● │  →   │ ● ● │  │ ○ ○ ○   │
└──────────────┘       └──────┘  └──────────┘
entropy = 0.971         entropy=0  entropy=0
                       
Gain = 0.971 - (6/15×0 + 9/15×0) = 0.971 (perfect split!)
```

### Decision Boundary in 2D Space

```
Y
2.6 │──────────┐ ○ ○ ○
2.5 │    ■     │       ○    ← Decision tree creates
    │          │              axis-aligned rectangular
2.0 │    ■     ├──────────    boundaries in the feature
    │    ■     │ ○ ○  ■       space
    └──────────┴──────────
    0    2     3    4    X

Each vertical/horizontal line = one decision node split
```

### Overfitting Visualization

```
Model Complexity (Tree Depth)
         ↑ Accuracy
    100% │       ●─────────●  ← Training accuracy (keeps rising)
         │     ●         ●
     80% │   ●         ●
         │  ●         ●
     60% │ ●       ●         ← Test accuracy (peaks then drops)
         │         
     40% └──────────────────→
         0    2    4    6    8   Max Depth

        Underfitting ↔ Sweet Spot ↔ Overfitting
```

---

## 13. Mnemonics & Cheat Sheet

### 🧠 Remember: "SELF" to Build a Tree

```
S → Select best attribute (max information gain)
E → Expand the node (make it a decision node)
L → Leaf if stopping condition is met
F → Further recurse on each subset
```

### 🧠 Remember: Entropy Extremes

```
"No Mix = Zero, Equal Mix = One"
Pure dataset   → entropy = 0  (you know everything, no new info needed)
50/50 split    → entropy = 1  (you know nothing, maximum uncertainty)
```

### 🧠 Remember: Gain Formula in Words

```
GAIN = (Disorder BEFORE split) − (Disorder AFTER split)
     = What we started with   −  What we're left with
     = How much cleaner it got
```

### 🧠 Remember: Which Algorithm Uses What

```
"ID3 Gains, C4.5 Ratios, CART Grins (Gini)"
```

### 📋 Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│                   DECISION TREE QUICK REFERENCE                  │
├──────────────────────┬──────────────────────────────────────────┤
│ Formula              │ Description                              │
├──────────────────────┼──────────────────────────────────────────┤
│ entropy(D)           │ -Σ Pr(cⱼ) × log₂ Pr(cⱼ)               │
│ entropy_A(D)         │ Σ (|Dⱼ|/|D|) × entropy(Dⱼ)            │
│ gain(D, A)           │ entropy(D) - entropy_A(D)               │
│ gainRatio(D, A)      │ gain(D, A) / SplitInfo(A)               │
│ SplitInfo(A)         │ -Σ (|Dⱼ|/|D|) × log₂(|Dⱼ|/|D|)       │
│ Gini(D)              │ 1 - Σ Pr(cⱼ)²                          │
├──────────────────────┼──────────────────────────────────────────┤
│ Entropy range        │ [0, log₂(|C|)]  → [0, 1] for binary    │
│ Gain range           │ [0, entropy(D)]                          │
│ GainRatio range      │ [0, 1]                                   │
│ Gini range           │ [0, 0.5] for binary                      │
├──────────────────────┼──────────────────────────────────────────┤
│ Best attribute       │ MAX gain (or max gain ratio)             │
│ Stop condition       │ Pure node OR no attributes OR no data    │
│ Overfitting fix      │ Pruning (post > pre)                     │
│ Continuous feature   │ Try all midpoint thresholds              │
└──────────────────────┴──────────────────────────────────────────┘
```

---

## 14. Practice Problems

### Problem 1 — Basic Entropy (Easy)

A dataset has 10 examples: 7 positive, 3 negative.  
**Calculate entropy(D).**

<details>
<summary>▶ Full Step-by-Step Solution</summary>

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — Count the classes                                     │
│    Positive = 7,  Negative = 3,  Total = 10                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2 — Compute class probabilities                           │
│    Pr(positive) = 7/10 = 0.700                                  │
│    Pr(negative) = 3/10 = 0.300                                  │
│    Check: 0.700 + 0.300 = 1.0  ✅                               │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3 — Compute log₂ of each probability                     │
│    log₂(0.700) = log₁₀(0.700)/log₁₀(2)                         │
│                = (−0.1549) / (0.3010)                           │
│                = −0.5146                                        │
│                                                                 │
│    log₂(0.300) = log₁₀(0.300)/log₁₀(2)                         │
│                = (−0.5229) / (0.3010)                           │
│                = −1.7370                                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 4 — Multiply probability × log                           │
│    positive term:  0.700 × (−0.5146) = −0.3602                 │
│    negative term:  0.300 × (−1.7370) = −0.5211                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 5 — Apply the negative sign from the formula             │
│    − (−0.3602) = +0.3602                                        │
│    − (−0.5211) = +0.5211                                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 6 — Sum the terms                                         │
│    entropy(D) = 0.3602 + 0.5211 = 0.8813 ≈ 0.881  ✅           │
│                                                                 │
│  Interpretation: 0.881 is fairly close to 1.0 (max disorder)   │
│  Dataset is unbalanced but not pure.                            │
│  If it were 50/50, entropy would be 1.0                        │
│  If it were 100/0, entropy would be 0.0                        │
└─────────────────────────────────────────────────────────────────┘
```
</details>

---

### Problem 2 — Which Split is Better? (Medium)

| Split | Left Branch | Right Branch |
|---|---|---|
| **A** | 4 Yes, 0 No | 1 Yes, 5 No |
| **B** | 3 Yes, 2 No | 2 Yes, 3 No |

Original dataset: 5 Yes, 5 No. Total = 10 examples.  
**Which split gives higher information gain?**

<details>
<summary>▶ Full Step-by-Step Solution</summary>

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — Compute root entropy (before any split)              │
│    Pr(Yes) = 5/10 = 0.500,  Pr(No) = 5/10 = 0.500              │
│    log₂(0.500) = log₁₀(0.5)/log₁₀(2) = −0.3010/0.3010 = −1.0  │
│                                                                 │
│    entropy(D) = −(0.5 × −1.0) − (0.5 × −1.0)                  │
│              = 0.500 + 0.500 = 1.000  (maximum disorder)       │
└─────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  EVALUATING SPLIT A
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2A — Left branch: 4 Yes, 0 No, Total=4                   │
│    Pr(Yes) = 4/4 = 1.0,  Pr(No) = 0/4 = 0.0                   │
│    entropy(Left_A) = −(1.0 × log₂1.0) − 0                     │
│                    = −(1.0 × 0) = 0.000  ← PURE ✅             │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3A — Right branch: 1 Yes, 5 No, Total=6                  │
│    Pr(Yes) = 1/6 = 0.1667,  Pr(No) = 5/6 = 0.8333              │
│                                                                 │
│    log₂(0.1667) = log₁₀(0.1667)/0.3010 = −0.7782/0.3010        │
│                 = −2.5850                                       │
│    log₂(0.8333) = log₁₀(0.8333)/0.3010 = −0.0792/0.3010        │
│                 = −0.2630                                       │
│                                                                 │
│    entropy(Right_A) = −(0.1667 × −2.5850) − (0.8333 × −0.2630) │
│                     = 0.4309 + 0.2192                           │
│                     = 0.6500                                    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 4A — Weighted entropy for Split A                        │
│    Weight of Left  = 4/10 = 0.400                               │
│    Weight of Right = 6/10 = 0.600                               │
│                                                                 │
│    entropy_A = (0.400 × 0.000) + (0.600 × 0.650)               │
│              = 0.000 + 0.390                                    │
│              = 0.390                                            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 5A — Gain for Split A                                    │
│    gain_A = entropy(D) − entropy_A                              │
│           = 1.000 − 0.390 = 0.610  ✅                          │
└─────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  EVALUATING SPLIT B
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2B — Left branch: 3 Yes, 2 No, Total=5                   │
│    Pr(Yes) = 3/5 = 0.600,  Pr(No) = 2/5 = 0.400                │
│    log₂(0.600) = −0.7370,  log₂(0.400) = −1.3219               │
│                                                                 │
│    entropy(Left_B) = −(0.600 × −0.7370) − (0.400 × −1.3219)   │
│                    = 0.4422 + 0.5288 = 0.9710                  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3B — Right branch: 2 Yes, 3 No, Total=5                  │
│    Pr(Yes) = 2/5 = 0.400,  Pr(No) = 3/5 = 0.600                │
│    Same as Left_B with classes swapped → same entropy           │
│    entropy(Right_B) = 0.971                                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 4B — Weighted entropy for Split B                        │
│    Weight of Left  = 5/10 = 0.500                               │
│    Weight of Right = 5/10 = 0.500                               │
│                                                                 │
│    entropy_B = (0.500 × 0.971) + (0.500 × 0.971)               │
│              = 0.4855 + 0.4855 = 0.971                          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 5B — Gain for Split B                                    │
│    gain_B = entropy(D) − entropy_B                              │
│           = 1.000 − 0.971 = 0.029  (very small!)               │
└─────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  FINAL COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────────┬─────────────┬──────────────────┬──────────┐
│ Split        │ Weighted    │ Gain             │ Winner?  │
│              │ Entropy     │                  │          │
├──────────────┼─────────────┼──────────────────┼──────────┤
│ A            │ 0.390       │ 1.000−0.390=0.610│  ✅ YES  │
│ B            │ 0.971       │ 1.000−0.971=0.029│  ❌ NO   │
└──────────────┴─────────────┴──────────────────┴──────────┘

WINNER: Split A (gain=0.610 >> 0.029)
WHY? Split A creates a perfectly PURE left branch (entropy=0)
     Split B leaves both branches almost as mixed as before!
```
</details>

---

### Problem 3 — Build a Mini Tree (Medium-Hard)

**Dataset (Weather → Play Tennis):**

| Weather | Wind | Humidity | Play |
|---|---|---|---|
| Sunny | Weak | High | No |
| Sunny | Strong | High | No |
| Overcast | Weak | High | Yes |
| Rainy | Weak | High | Yes |
| Rainy | Weak | Normal | Yes |
| Rainy | Strong | Normal | No |
| Overcast | Strong | Normal | Yes |
| Sunny | Weak | Normal | Yes |

Total: 5 Yes, 3 No

**Task:** Compute entropy and information gain for each attribute. Which is the root?

<details>
<summary>▶ Full Step-by-Step Solution</summary>

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — Root entropy                                          │
│    Yes=5, No=3, Total=8                                         │
│    Pr(Yes) = 5/8 = 0.625,  Pr(No) = 3/8 = 0.375                │
│                                                                 │
│    log₂(0.625) = log₁₀(0.625)/0.3010 = −0.2041/0.3010 = −0.678 │
│    log₂(0.375) = log₁₀(0.375)/0.3010 = −0.4260/0.3010 = −1.415 │
│                                                                 │
│    entropy(D) = −(0.625×−0.678) − (0.375×−1.415)               │
│              = 0.424 + 0.531 = 0.954                            │
└─────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ATTRIBUTE: Weather (3 values: Sunny / Overcast / Rainy)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Group Sunny    (rows 1,2,8): Yes=1, No=2, Total=3
  Group Overcast (rows 3,7):   Yes=2, No=0, Total=2
  Group Rainy    (rows 4,5,6): Yes=2, No=1, Total=3

┌─── entropy(Sunny) ──────────────────────────────────────────────┐
│  Pr(Yes)=1/3=0.333, Pr(No)=2/3=0.667                           │
│  log₂(0.333)=−1.585,  log₂(0.667)=−0.585                       │
│  entropy = −(0.333×−1.585)−(0.667×−0.585) = 0.528+0.390 = 0.918│
└─────────────────────────────────────────────────────────────────┘

┌─── entropy(Overcast) ───────────────────────────────────────────┐
│  Pr(Yes)=2/2=1.0, Pr(No)=0/2=0.0                               │
│  entropy = 0.000  ← PURE ✅                                     │
└─────────────────────────────────────────────────────────────────┘

┌─── entropy(Rainy) ──────────────────────────────────────────────┐
│  Pr(Yes)=2/3=0.667, Pr(No)=1/3=0.333                           │
│  Same as Sunny (just swapped) → entropy = 0.918                 │
└─────────────────────────────────────────────────────────────────┘

  entropy_Weather = (3/8)×0.918 + (2/8)×0.000 + (3/8)×0.918
                  = 0.375×0.918 + 0 + 0.375×0.918
                  = 0.344 + 0 + 0.344 = 0.688

  gain(Weather) = 0.954 − 0.688 = 0.266  ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ATTRIBUTE: Wind (2 values: Weak / Strong)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Group Weak   (rows 1,3,4,5,8): Yes=4, No=1, Total=5
  Group Strong (rows 2,6,7):     Yes=1, No=2, Total=3

┌─── entropy(Weak) ───────────────────────────────────────────────┐
│  Pr(Yes)=4/5=0.800, Pr(No)=1/5=0.200                           │
│  log₂(0.800)=−0.322,  log₂(0.200)=−2.322                       │
│  entropy = −(0.800×−0.322)−(0.200×−2.322) = 0.258+0.464 = 0.722│
└─────────────────────────────────────────────────────────────────┘

┌─── entropy(Strong) ─────────────────────────────────────────────┐
│  Pr(Yes)=1/3=0.333, Pr(No)=2/3=0.667                           │
│  entropy = 0.918  (same calculation as Sunny above)             │
└─────────────────────────────────────────────────────────────────┘

  entropy_Wind = (5/8)×0.722 + (3/8)×0.918
               = 0.625×0.722 + 0.375×0.918
               = 0.451 + 0.344 = 0.795

  gain(Wind) = 0.954 − 0.795 = 0.159

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ATTRIBUTE: Humidity (2 values: High / Normal)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Group High   (rows 1,2,3,4): Yes=2, No=2, Total=4
  Group Normal (rows 5,6,7,8): Yes=3, No=1, Total=4

┌─── entropy(High) ───────────────────────────────────────────────┐
│  Pr(Yes)=2/4=0.500, Pr(No)=2/4=0.500                           │
│  entropy = 1.000  ← maximum disorder!                           │
└─────────────────────────────────────────────────────────────────┘

┌─── entropy(Normal) ─────────────────────────────────────────────┐
│  Pr(Yes)=3/4=0.750, Pr(No)=1/4=0.250                           │
│  log₂(0.750) = log₁₀(0.750)/0.3010 = −0.1249/0.3010 = −0.4150  │
│  log₂(0.250) = log₁₀(0.250)/0.3010 = −0.6021/0.3010 = −2.0000  │
│  entropy = −(0.750×−0.415)−(0.250×−2.000) = 0.311+0.500 = 0.811│
└─────────────────────────────────────────────────────────────────┘

  entropy_Humidity = (4/8)×1.000 + (4/8)×0.811
                   = 0.500×1.000 + 0.500×0.811
                   = 0.500 + 0.406 = 0.906

  gain(Humidity) = 0.954 − 0.906 = 0.048

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  FINAL COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────────┬─────────────────┬──────────┬──────────┐
│ Attribute    │ Weighted        │ Gain     │ Winner?  │
│              │ Entropy         │          │          │
├──────────────┼─────────────────┼──────────┼──────────┤
│ Weather      │ 0.688           │ 0.266    │  ✅ YES  │
│ Wind         │ 0.795           │ 0.159    │  ❌ NO   │
│ Humidity     │ 0.906           │ 0.048    │  ❌ NO   │
└──────────────┴─────────────────┴──────────┴──────────┘

WINNER: Weather (gain=0.266) → becomes ROOT NODE
Note: Overcast branch is already PURE → becomes a leaf (Yes) immediately!
```
</details>

---

### Problem 4 — Continuous Threshold (Medium)

Feature "Temperature" with values and classes:

| Temp | 15 | 18 | 22 | 25 | 30 | 35 |
|---|---|---|---|---|---|---|
| Class | No | No | No | Yes | Yes | Yes |

**Find the best binary split threshold.**

<details>
<summary>▶ Full Step-by-Step Solution</summary>

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — Root entropy                                          │
│    Yes=3, No=3, Total=6                                         │
│    Pr(Yes) = Pr(No) = 0.500                                     │
│    entropy(D) = −(0.5×−1.0) − (0.5×−1.0) = 1.000              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2 — Identify candidate thresholds                        │
│    Sort values: 15, 18, 22, 25, 30, 35                         │
│    Midpoints between adjacent values:                           │
│      (15+18)/2 = 16.5                                           │
│      (18+22)/2 = 20.0                                           │
│      (22+25)/2 = 23.5   ← class boundary here (No→Yes)        │
│      (25+30)/2 = 27.5                                           │
│      (30+35)/2 = 32.5                                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3 — Evaluate each threshold                              │
│                                                                 │
│  Threshold 16.5: (≤16.5 vs >16.5)                              │
│    Left : [15]       → 0 Yes, 1 No  → entropy=0.000  size=1    │
│    Right: [18,22,25,30,35] → 3 Yes, 2 No → entropy=0.971 size=5│
│    weighted = (1/6)×0 + (5/6)×0.971 = 0.809                    │
│    gain = 1.000 − 0.809 = 0.191                                 │
│                                                                 │
│  Threshold 20.0: (≤20 vs >20)                                   │
│    Left : [15,18]   → 0 Yes, 2 No  → entropy=0.000  size=2     │
│    Right: [22,25,30,35] → 3 Yes, 1 No → entropy=0.811 size=4   │
│    weighted = (2/6)×0 + (4/6)×0.811 = 0.541                    │
│    gain = 1.000 − 0.541 = 0.459                                 │
│                                                                 │
│  Threshold 23.5: (≤23.5 vs >23.5)  ← CLASS BOUNDARY           │
│    Left : [15,18,22] → 0 Yes, 3 No → entropy=0.000  size=3     │
│    Right: [25,30,35] → 3 Yes, 0 No → entropy=0.000  size=3     │
│    weighted = (3/6)×0 + (3/6)×0 = 0.000                        │
│    gain = 1.000 − 0.000 = 1.000  ← PERFECT SPLIT! ✅           │
│                                                                 │
│  (No need to check 27.5 or 32.5 since 1.0 is max possible)    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  RESULT SUMMARY                                                 │
│                                                                 │
│  Threshold │  Left (≤t)  │  Right (>t) │  Gain                 │
│  ──────────┼─────────────┼─────────────┼──────                 │
│   16.5     │ 0Y, 1N, E=0 │ 3Y, 2N, 0.971│  0.191              │
│   20.0     │ 0Y, 2N, E=0 │ 3Y, 1N, 0.811│  0.459              │
│   23.5     │ 0Y, 3N, E=0 │ 3Y, 0N, E=0 │  1.000  ✅ BEST      │
│                                                                 │
│  Best threshold = 23.5                                          │
│  Split rule: Temperature ≤ 23.5 → No,  Temperature > 23.5 → Yes│
└─────────────────────────────────────────────────────────────────┘
```
</details>

---

### Problem 5 — Gain Ratio (Hard)

Using the same dataset as the worked example (15 loans):  
**Compute Gain Ratio for Own\_House and Age.**

<details>
<summary>▶ Full Step-by-Step Solution</summary>

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  GAIN RATIO for Own House
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────┐
│  Known from earlier: gain(D, Own House) = 0.420                 │
│  Split: 6 examples in true-branch, 9 in false-branch           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — Compute split proportions                            │
│    |D_true|/|D|  = 6/15 = 0.400                                 │
│    |D_false|/|D| = 9/15 = 0.600                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2 — Compute log₂ of split proportions                    │
│    log₂(0.400) = log₁₀(0.400)/0.3010 = −0.3979/0.3010          │
│                = −1.3219                                        │
│                                                                 │
│    log₂(0.600) = log₁₀(0.600)/0.3010 = −0.2218/0.3010          │
│                = −0.7370                                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3 — Compute SplitInfo (entropy of the split)             │
│    SplitInfo(Own House) = − (0.400 × −1.3219)                   │
│                         − (0.600 × −0.7370)                    │
│                         = 0.5288 + 0.4422                       │
│                         = 0.9710 ≈ 0.971                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 4 — Compute Gain Ratio                                   │
│    GainRatio(Own House) = gain / SplitInfo                      │
│                         = 0.420 / 0.971                         │
│                         = 0.432  ✅                              │
└─────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  GAIN RATIO for Age
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────┐
│  Known: gain(D, Age) = 0.083                                    │
│  Split: 5 young + 5 middle + 5 old (perfectly equal thirds)    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 1 — Split proportions                                    │
│    |D_young|/|D|  = 5/15 = 0.3333                               │
│    |D_middle|/|D| = 5/15 = 0.3333                               │
│    |D_old|/|D|    = 5/15 = 0.3333                               │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 2 — Log of split proportion (same for all 3)             │
│    log₂(0.3333) = log₁₀(0.3333)/0.3010 = −0.4771/0.3010        │
│                 = −1.5850                                       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 3 — SplitInfo for Age                                    │
│    SplitInfo(Age) = − (0.3333 × −1.5850)                        │
│                   − (0.3333 × −1.5850)                          │
│                   − (0.3333 × −1.5850)                          │
│                                                                 │
│                 = 3 × (0.3333 × 1.5850)                         │
│                 = 3 × 0.5283                                    │
│                 = 1.585                                          │
│                                                                 │
│  Note: log₂(3) = 1.585. This is not a coincidence!             │
│  Equal splits always give SplitInfo = log₂(number of branches) │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  STEP 4 — Gain Ratio for Age                                   │
│    GainRatio(Age) = gain / SplitInfo                            │
│                   = 0.083 / 1.585                               │
│                   = 0.052                                       │
└─────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CONCLUSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────────┬────────────┬──────────────┬──────────────┬────────────┐
│ Attribute    │ Gain       │ SplitInfo    │ Gain Ratio   │ Winner?    │
├──────────────┼────────────┼──────────────┼──────────────┼────────────┤
│ Own House    │ 0.420      │ 0.971        │ 0.432        │  ✅ YES    │
│ Age          │ 0.083      │ 1.585        │ 0.052        │  ❌ NO     │
└──────────────┴────────────┴──────────────┴──────────────┴────────────┘

Own House still wins, but notice:
• Age was penalised because it splits into 3 branches (SplitInfo=1.585)
• Own House was barely penalised (SplitInfo=0.971, only 2 branches)
• Gain Ratio correctly identifies Own House as the better split
```
</details>

---

## 15. Best Practices

### 1. Choose the Right Split Criterion

```
Use Gain Ratio (C4.5) when:
  → You have attributes with many distinct values
  → You want to avoid bias toward high-cardinality features

Use Gini (CART) when:
  → You need speed (no log computation)
  → You want compatibility with sklearn

Use Information Gain (ID3) when:
  → Learning the concept (simpler math)
  → All attributes have similar cardinality
```

### 2. Control Tree Complexity

```python
# sklearn example — hyperparameters to tune
DecisionTreeClassifier(
    max_depth=5,           # Limit tree depth
    min_samples_split=10,  # Min samples to split a node
    min_samples_leaf=5,    # Min samples in each leaf
    max_features='sqrt',   # Use random subset of features
    ccp_alpha=0.01         # Cost-complexity pruning strength
)
```

### 3. Validation Strategy

```
ALWAYS evaluate on held-out test data:

Option A: Train/Test Split (simple)
  70% training → build tree
  30% testing  → evaluate

Option B: K-Fold Cross Validation (robust)
  Split data into k folds
  Train on k-1, test on 1
  Repeat k times, average the scores

Option C: Separate Pruning Set (for post-pruning)
  60% training → build full tree
  20% validation → pruning decisions
  20% testing  → final evaluation
```

### 4. Feature Engineering

```
Decision trees benefit from:
  ✅ Creating interaction features (A AND B)
  ✅ Binning continuous features carefully
  ✅ Encoding ordinal categories as ordered numbers
  ✅ Removing irrelevant/redundant features (reduces tree size)

Decision trees DON'T need:
  ❌ Feature scaling (not distance-based)
  ❌ Normalization
  ❌ Handling of correlated features (tree handles it)
```

### 5. Handling Class Imbalance

```
Problem: 95% Class A, 5% Class B
         Tree predicts A for everything → 95% accuracy but useless!

Solutions:
  • class_weight='balanced' in sklearn
  • Oversample minority class (SMOTE)
  • Undersample majority class
  • Use precision/recall/F1 instead of accuracy
```

---

## 16. Common Pitfalls

### ❌ Pitfall 1: Overfitting

```
Problem: Tree grows too deep, fits noise
         Training: 99% accuracy
         Test: 62% accuracy

Fix:
  • Post-pruning (preferred)
  • Set max_depth=5 or 10
  • Require min_samples_leaf ≥ 5
```

### ❌ Pitfall 2: Information Gain Bias

```
Problem: Attribute "Customer_ID" has 1000 unique values
         ID3 always picks it (perfect split, gain=max!)
         But it's USELESS for prediction

Fix:
  • Use Gain Ratio (C4.5) instead of raw Gain
  • Remove ID/timestamp columns before training
```

### ❌ Pitfall 3: Instability

```
Problem: Remove one training example → completely different tree
         Decision trees have HIGH variance

Fix:
  • Use ensemble methods: Random Forest, Gradient Boosting
  • Average predictions across many trees = stability
```

### ❌ Pitfall 4: Axis-Aligned Boundaries Only

```
Problem: Trees can only make horizontal/vertical splits
         Diagonal or curved boundaries require many nodes

Example: Data separated by diagonal line y = x
         Tree needs many steps to approximate it:
         
         Real boundary: /    Tree boundary: ┐
                                           │ ┐
                                             │ ┐

Fix:
  • Create diagonal features (e.g., feature1 - feature2)
  • Use SVM or neural nets for diagonal boundaries
```

### ❌ Pitfall 5: Missing Values

```
Problem: ID3 can't handle missing values at all

Fixes:
  • C4.5: Distributes example with weight across all branches
  • CART: Surrogate splits (use second-best attribute as backup)
  • Imputation: Fill missing values before training
  • sklearn: Does NOT support missing values natively → impute first
```

### ❌ Pitfall 6: Assuming the Tree is Optimal

```
REMEMBER: Finding the globally optimal tree is NP-HARD

All algorithms are greedy heuristics:
  • Make locally optimal choice at each step
  • May miss globally better tree structure
  • The tree YOU get ≠ the BEST possible tree

This is WHY ensembles (Random Forests) outperform single trees
```

---

## 📚 Summary Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DECISION TREE LEARNING — OVERVIEW                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  DATA → [Compute Entropy] → [Compute Gain per Attribute]             │
│                ↓                         ↓                            │
│           entropy(D)            gain(D, Aᵢ) = entropy(D)             │
│       = -Σ Pr(c)log₂Pr(c)       - Σ(|Dⱼ|/|D|)×entropy(Dⱼ)         │
│                                                                       │
│  [Pick MAX gain attribute] → [Split data] → [Recurse on subsets]     │
│                                                                       │
│  STOPPING: Pure node | No attributes | Gain < threshold               │
│                                                                       │
│  OVERFITTING: Prune! (Post-pruning preferred)                         │
│                                                                       │
│  CONTINUOUS: Try all midpoint thresholds, pick max gain               │
│                                                                       │
│  RULES: Each root→leaf path = one IF-THEN rule                        │
│                                                                       │
│  VARIANTS: ID3 (Gain) | C4.5 (GainRatio) | CART (Gini)               │
└─────────────────────────────────────────────────────────────────────┘
```

---
