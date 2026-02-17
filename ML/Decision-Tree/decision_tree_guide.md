# 🌳 Decision Trees — Complete Study Guide

> **Reference:** CS583, Bing Liu, UIC | Subhash Bhagat Sir ML Slides  
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

### 5.1 Entropy

#### What is Entropy?

Entropy measures **how mixed/disordered** a dataset is.

```
High Entropy = Mixed Classes = Uncertain = More info needed
Low Entropy  = Pure Classes  = Certain   = Less info needed

Coin example:
• Fair coin (50/50): entropy = 1.0  → you know nothing!
• Biased coin (99/1): entropy ≈ 0.08 → pretty predictable
• One-sided coin (100/0): entropy = 0  → you know everything!
```

#### Formula

$$\text{entropy}(D) = -\sum_{j=1}^{|C|} \Pr(c_j) \cdot \log_2 \Pr(c_j)$$

**Notation Key:**

| Symbol | Meaning |
|---|---|
| `D` | Dataset (set of examples) |
| `C` | Set of all class labels |
| `\|C\|` | Number of distinct classes |
| `Pr(cⱼ)` | Proportion of class cⱼ in D |
| `log₂` | Logarithm base 2 |

> ⚠️ Convention: `0 × log₂(0) = 0` (not undefined)

#### Step-by-Step Entropy Calculation

**Example:** Dataset D has 9 Yes, 6 No (total 15 examples)

```
Step 1: Find class probabilities
        Pr(Yes) = 9/15 = 0.6
        Pr(No)  = 6/15 = 0.4

Step 2: Apply entropy formula
        entropy(D) = -(0.6 × log₂0.6) - (0.4 × log₂0.4)

Step 3: Calculate each log
        log₂(0.6) = log(0.6)/log(2) = -0.737
        log₂(0.4) = log(0.4)/log(2) = -1.322

Step 4: Multiply
        -(0.6 × -0.737) = +0.442
        -(0.4 × -1.322) = +0.529

Step 5: Sum
        entropy(D) = 0.442 + 0.529 = 0.971
```

#### Entropy Intuition Table

| Pr(positive) | Pr(negative) | Entropy | Meaning |
|---|---|---|---|
| 0.5 | 0.5 | **1.000** | Maximum confusion |
| 0.2 | 0.8 | **0.722** | Leaning negative |
| 0.9 | 0.1 | **0.469** | Mostly positive |
| 1.0 | 0.0 | **0.000** | Perfectly pure |

#### Entropy Curve

```
Entropy
  1.0 │         ●
      │      ●     ●
  0.7 │    ●         ●
      │  ●             ●
  0.4 │●                 ●
      │                    ●
  0.0 ●──────────────────────●
      0   0.2  0.4  0.6  0.8  1.0
                              Pr(positive)

Peak at 0.5 → maximum uncertainty
Drops to 0 at 0 or 1 → completely certain
```

---

### 5.2 Information Gain

#### What is Information Gain?

Information Gain tells us **how much an attribute reduces uncertainty** in the data. We always pick the attribute with the **highest gain**.

```
Gain = entropy BEFORE split  −  weighted entropy AFTER split
     = How messy things were  −  How messy things are now
```

#### Formulas

**Step 1 — Entropy of current node:**
$$\text{entropy}(D) = -\sum_{j=1}^{|C|} \Pr(c_j) \cdot \log_2 \Pr(c_j)$$

**Step 2 — Expected entropy AFTER splitting on attribute Aᵢ (with v values):**
$$\text{entropy}_{A_i}(D) = \sum_{j=1}^{v} \frac{|D_j|}{|D|} \times \text{entropy}(D_j)$$

**Step 3 — Information Gain:**
$$\text{gain}(D, A_i) = \text{entropy}(D) - \text{entropy}_{A_i}(D)$$

**Notation Key:**

| Symbol | Meaning |
|---|---|
| `Aᵢ` | Attribute being evaluated |
| `v` | Number of distinct values of Aᵢ |
| `Dⱼ` | Subset of D where Aᵢ = vⱼ |
| `\|Dⱼ\|` | Size of subset Dⱼ |
| `\|D\|` | Total size of dataset |
| `\|Dⱼ\|/\|D\|` | Weight (fraction of data in this subset) |

---

### 5.3 Gain Ratio

#### Problem with Information Gain

Information Gain is **biased** toward attributes with many values (e.g., a unique ID column would always win, but gives useless splits).

#### Fix: Gain Ratio (used in C4.5)

$$\text{GainRatio}(D, A_i) = \frac{\text{gain}(D, A_i)}{\text{SplitInfo}(A_i)}$$

$$\text{SplitInfo}(A_i) = -\sum_{j=1}^{v} \frac{|D_j|}{|D|} \cdot \log_2 \frac{|D_j|}{|D|}$$

> 💡 SplitInfo is the entropy of the split itself. Attributes that split data very unevenly get penalized.

**Example:** Attribute with 15 unique values → SplitInfo ≈ log₂(15) = 3.91 (large penalty). Attribute with 2 balanced values → SplitInfo = 1.0 (small penalty).

---

### 5.4 Gini Impurity (CART)

Used by the **CART** algorithm (sklearn's default):

$$\text{Gini}(D) = 1 - \sum_{j=1}^{|C|} \Pr(c_j)^2$$

**Comparison:**

| Scenario | Entropy | Gini |
|---|---|---|
| 50/50 split | 1.000 | 0.500 |
| 80/20 split | 0.722 | 0.320 |
| 100/0 split | 0.000 | 0.000 |

Both measure impurity. Gini is slightly faster to compute (no log needed).

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

| ID | Age | Has_Job | Own_House | Credit_Rating | Class |
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

### Step 1: Compute Root Entropy

$$\text{entropy}(D) = -\frac{6}{15}\log_2\frac{6}{15} - \frac{9}{15}\log_2\frac{9}{15}$$

```
Pr(No)  = 6/15 = 0.4   →  -0.4 × log₂(0.4) = -0.4 × (-1.322) = 0.529
Pr(Yes) = 9/15 = 0.6   →  -0.6 × log₂(0.6) = -0.6 × (-0.737) = 0.442

entropy(D) = 0.529 + 0.442 = 0.971
```

---

### Step 2: Compute Gain for Each Attribute

#### Attribute: Age

Subsets after splitting on Age:

| Age Value | Yes | No | Total | Entropy of subset |
|---|---|---|---|---|
| young | 2 | 3 | 5 | −(2/5)log₂(2/5) − (3/5)log₂(3/5) = **0.971** |
| middle | 3 | 2 | 5 | −(3/5)log₂(3/5) − (2/5)log₂(2/5) = **0.971** |
| old | 4 | 1 | 5 | −(4/5)log₂(4/5) − (1/5)log₂(1/5) = **0.722** |

$$\text{entropy}_{Age}(D) = \frac{5}{15}(0.971) + \frac{5}{15}(0.971) + \frac{5}{15}(0.722)$$
$$= 0.333 \times (0.971 + 0.971 + 0.722) = 0.888$$

$$\text{gain}(D, \text{Age}) = 0.971 - 0.888 = \mathbf{0.083}$$

---

#### Attribute: Own_House

| Own_House | Yes | No | Total | Entropy |
|---|---|---|---|---|
| true | 6 | 0 | 6 | **0.000** (pure!) |
| false | 3 | 6 | 9 | **0.918** |

$$\text{entropy}_{Own\_house}(D) = \frac{6}{15}(0) + \frac{9}{15}(0.918) = 0 + 0.551 = 0.551$$

$$\text{gain}(D, \text{Own\_House}) = 0.971 - 0.551 = \mathbf{0.420}$$ ✅ **HIGHEST!**

---

#### Attribute: Has_Job

| Has_Job | Yes | No | Total | Entropy |
|---|---|---|---|---|
| true | 5 | 0 | 5 | **0.000** (pure!) |
| false | 4 | 6 | 10 | **0.971** |

$$\text{entropy}_{Has\_Job}(D) = \frac{5}{15}(0) + \frac{10}{15}(0.971) = 0.647$$

$$\text{gain}(D, \text{Has\_Job}) = 0.971 - 0.647 = \mathbf{0.324}$$

---

#### Attribute: Credit_Rating

| Credit | Yes | No | Total | Entropy |
|---|---|---|---|---|
| fair | 1 | 4 | 5 | 0.722 |
| good | 4 | 2 | 6 | 0.918 |
| excellent | 4 | 0 | 4 | 0.000 |

$$\text{entropy}_{Credit}(D) = \frac{5}{15}(0.722) + \frac{6}{15}(0.918) + \frac{4}{15}(0) = 0.608$$

$$\text{gain}(D, \text{Credit\_Rating}) = 0.971 - 0.608 = \mathbf{0.363}$$

---

### Step 3: Compare All Gains

```
┌────────────────────┬──────────────────────┬──────────────┐
│ Attribute          │ Expected Entropy     │ Gain         │
├────────────────────┼──────────────────────┼──────────────┤
│ Age                │ 0.888                │ 0.083        │
│ Has_Job            │ 0.647                │ 0.324        │
│ Own_House          │ 0.551                │ 0.420  ← MAX │ ✅
│ Credit_Rating      │ 0.608                │ 0.363        │
└────────────────────┴──────────────────────┴──────────────┘

Winner: Own_House → becomes ROOT NODE
```

---

### Step 4: Split and Recurse

**Branch 1: Own_House = true** → 6 Yes, 0 No → **PURE LEAF → Yes**

**Branch 2: Own_House = false** → 3 Yes, 6 No → not pure, recurse!

For the "false" subset, compute gains for remaining attributes:
- Has_Job wins → splits into Has_Job=true (5 Yes, 0 No → **Yes**) and Has_Job=false (4 No, 0 Yes → **No**)

---

### Final Tree

```
                    ┌──────────────┐
                    │  Own_House?  │
                    └──────┬───────┘
                    ┌──────┴──────┐
                  true          false
                    │               │
               ✅ Yes           ┌────┴────┐
               (6/6)            │ Has_Job?│
                                └────┬────┘
                              ┌─────┴─────┐
                            true         false
                              │               │
                           ✅ Yes          ❌ No
                            (5/5)          (4/4)
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
<summary>Solution</summary>

```
Pr(positive) = 7/10 = 0.7
Pr(negative) = 3/10 = 0.3

entropy(D) = -(0.7 × log₂0.7) - (0.3 × log₂0.3)
           = -(0.7 × -0.515) - (0.3 × -1.737)
           = 0.361 + 0.521
           = 0.882
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
<summary>Solution</summary>

```
entropy(D) = -(0.5 × log₂0.5) - (0.5 × log₂0.5) = 1.0

Split A:
  Left  (4 Yes, 0 No): entropy = 0          [size=4]
  Right (1 Yes, 5 No): -1/6×log₂(1/6) - 5/6×log₂(5/6)
                      = 0.650               [size=6]
  entropy_A = (4/10)×0 + (6/10)×0.650 = 0.390
  gain_A = 1.0 - 0.390 = 0.610

Split B:
  Left  (3 Yes, 2 No): -0.6×log₂0.6 - 0.4×log₂0.4 = 0.971  [size=5]
  Right (2 Yes, 3 No): same = 0.971                            [size=5]
  entropy_B = (5/10)×0.971 + (5/10)×0.971 = 0.971
  gain_B = 1.0 - 0.971 = 0.029

WINNER: Split A (gain=0.610 >> 0.029)
Reason: Split A creates a pure left node!
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
<summary>Solution</summary>

```
entropy(D) = -(5/8)log₂(5/8) - (3/8)log₂(3/8) = 0.954

Attribute: Weather
  Sunny    → 1 Yes, 2 No → entropy = 0.918   [size=3]
  Overcast → 2 Yes, 0 No → entropy = 0        [size=2]
  Rainy    → 2 Yes, 1 No → entropy = 0.918   [size=3]
  entropy_Weather = (3/8)(0.918) + (2/8)(0) + (3/8)(0.918)
                  = 0.344 + 0 + 0.344 = 0.688
  gain(Weather) = 0.954 - 0.688 = 0.266

Attribute: Wind
  Weak   → 4 Yes, 1 No → entropy = 0.722  [size=5]
  Strong → 1 Yes, 2 No → entropy = 0.918  [size=3]
  entropy_Wind = (5/8)(0.722) + (3/8)(0.918) = 0.451 + 0.344 = 0.795
  gain(Wind) = 0.954 - 0.795 = 0.159

Attribute: Humidity
  High   → 2 Yes, 2 No → entropy = 1.0   [size=4]
  Normal → 3 Yes, 1 No → entropy = 0.811  [size=4]
  entropy_Humidity = (4/8)(1.0) + (4/8)(0.811) = 0.500 + 0.406 = 0.906
  gain(Humidity) = 0.954 - 0.906 = 0.048

WINNER: Weather (gain=0.266) → Root Node
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
<summary>Solution</summary>

```
entropy(D): 3 Yes, 3 No → entropy = 1.0

Candidate thresholds: 16.5, 20, 23.5, 27.5, 32.5

Threshold 23.5 (≤23.5 vs >23.5):
  Left  (15,18,22 → No,No,No): entropy = 0   [size=3]
  Right (25,30,35 → Yes,Yes,Yes): entropy = 0 [size=3]
  expected entropy = (3/6)(0) + (3/6)(0) = 0
  gain = 1.0 - 0 = 1.0  ← PERFECT SPLIT! ✅

Best threshold = 23.5
```
</details>

---

### Problem 5 — Gain Ratio (Hard)

Using the same dataset as the worked example (15 loans):  
**Compute Gain Ratio for Own_House and Age.**

<details>
<summary>Solution</summary>

```
SplitInfo(Own_House):
  P(true) = 6/15,  P(false) = 9/15
  SplitInfo = -(6/15)log₂(6/15) - (9/15)log₂(9/15)
            = -0.4×(-1.322) - 0.6×(-0.737) = 0.529 + 0.442 = 0.971

GainRatio(Own_House) = 0.420 / 0.971 = 0.432

SplitInfo(Age):
  P(young)=P(middle)=P(old) = 5/15 = 1/3 each
  SplitInfo = -3 × (1/3)log₂(1/3) = -3 × (1/3 × -1.585) = 1.585

GainRatio(Age) = 0.083 / 1.585 = 0.052

CONCLUSION: Own_House still wins (0.432 >> 0.052)
Age gets penalized heavily for having 3 equal-sized groups
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

*Last updated: February 2026 | Based on CS583 (Bing Liu, UIC) + Subhash Bhagat Sir ML Slides*
