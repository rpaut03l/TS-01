# 🌳 Decision Tree Theory

> **Topic:** Decision Tree Learning using Entropy & Information Gain

---

## 📋 Table of Contents

1. [Introduction](#1-introduction)
2. [The Loan Dataset](#2-the-loan-dataset)
3. [A Decision Tree from the Loan Data](#3-a-decision-tree-from-the-loan-data)
4. [Using the Decision Tree](#4-using-the-decision-tree)
5. [Is the Decision Tree Unique?](#5-is-the-decision-tree-unique)
6. [From Tree to Rules](#6-from-tree-to-rules)
7. [Algorithm for Decision Tree Learning](#7-algorithm-for-decision-tree-learning)
8. [The Formal Algorithm](#8-the-formal-algorithm)
9. [Choosing an Attribute to Partition](#9-choosing-an-attribute-to-partition)
10. [Information Theory](#10-information-theory)
11. [Entropy Measure](#11-entropy-measure)
12. [Entropy: Worked Examples](#12-entropy-worked-examples)
13. [Information Gain](#13-information-gain)
14. [Full Worked Example — Loan Dataset](#14-full-worked-example--loan-dataset)
15. [Building the Final Tree](#15-building-the-final-tree)
16. [Handling Continuous Attributes](#16-handling-continuous-attributes)
17. [Continuous Attribute Example](#17-continuous-attribute-example)
18. [Avoiding Overfitting](#18-avoiding-overfitting)
19. [Overfitting Example](#19-overfitting-example)
20. [Other Issues in Decision Tree Learning](#20-other-issues-in-decision-tree-learning)
21. [Cheat Sheet and Mnemonics](#21-cheat-sheet-and-mnemonics)
22. [Formula Quick Reference](#22-formula-quick-reference)

---

## 1. Introduction

> *Slide 15 — CS583, Bing Liu, UIC*

Decision tree learning is one of the most **widely used techniques for classification**.

```
Key properties:
  ✅ Competitive accuracy with other methods
  ✅ Very efficient to train and predict
  ✅ Produces a human-readable model (a tree)
  ✅ C4.5 by Ross Quinlan is the best-known system
```

**What is a Decision Tree?**

The classification model is a **tree structure** where:

```
                    ┌───────────────┐
                    │  Root Node    │  ← First split (best attribute)
                    │  (Attribute?) │
                    └──────┬────────┘
               ┌───────────┼───────────┐
             val1         val2        val3
               │           │           │
          ┌────┴────┐  ┌───┴────┐  ┌──┴─────┐
          │Decision │  │  Leaf  │  │Decision│
          │  Node   │  │(Class) │  │  Node  │
          └────┬────┘  └────────┘  └───┬────┘
           ┌───┴───┐               ┌───┴───┐
         true    false           true    false
           │       │               │       │
        ┌──┴─┐  ┌──┴─┐         ┌──┴─┐  ┌──┴─┐
        │LEAF│  │LEAF│         │LEAF│  │LEAF│
        │Yes │  │ No │         │Yes │  │ No │
        └────┘  └────┘         └────┘  └────┘

Legend:
  ┌───────┐  = Decision Node (internal) — asks a question
  LEAF       = Leaf Node — gives the final class label
```

**Key Terminology:**

| Term | Definition |
|---|---|
| **Root Node** | The topmost decision node; the first attribute tested |
| **Decision Node** | An internal node that tests an attribute and branches |
| **Leaf Node** | A terminal node that holds a class label (the answer) |
| **Branch / Edge** | A path from a node labelled with an attribute value |
| **Path** | A sequence of nodes from root to leaf |
| **Depth** | Number of edges from root to deepest leaf |

[🔝 Back to Top](#-table-of-contents)

---

## 2. The Loan Dataset

> *Slides 16 and 24 — The Loan Data (reproduced)*

15 applicants, 4 features, binary outcome (Approve loan or not).

| ID | Age | Has Job | Own House | Credit Rating | Class |
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

```
Summary:
  Total examples : 15
  Approved (Yes) :  9
  Rejected (No)  :  6
  Features       :  4  (Age, Has Job, Own House, Credit Rating)

Attribute types:
  Age           categorical   {young, middle, old}
  Has Job       boolean       {true, false}
  Own House     boolean       {true, false}
  Credit Rating categorical   {fair, good, excellent}
```

[🔝 Back to Top](#-table-of-contents)

---

## 3. A Decision Tree from the Loan Data

> *Slide 17 — Decision nodes and leaf nodes (classes)*

One possible tree using Age as root (from the slides):

```
                         ┌──────────┐
                         │   Age?   │
                         └────┬─────┘
           ┌─────────────────┬┴─────────────────┐
         young             middle               old
           │                 │                   │
     ┌─────┴──────┐    ┌─────┴──────┐    ┌──────┴──────┐
     │  Has job?  │    │ Own house? │    │Credit rating?│
     └─────┬──────┘    └─────┬──────┘    └──────┬──────┘
        ┌──┴──┐           ┌──┴──┐        ┌──────┼──────┐
      true  false       true  false     fair   good  excellent
        │      │          │      │        │      │       │
      Yes     No         Yes    No       No     Yes     Yes
      (2/2)  (3/3)      (3/3) (2/2)    (1/1)  (2/2)   (2/2)
```

**Reading notation (x/x):** `(2/2)` = 2 examples reach this leaf, 2 classified correctly. Every leaf here is 100% confident.

**Two node types side-by-side:**

```
  ┌─────────────────┐      ┌───────────────────────────┐
  │  DECISION NODE  │  vs  │        LEAF NODE           │
  │                 │      │                            │
  │     Age?        │      │   Class: Yes               │
  │   ↙   ↓   ↘   │      │   Confidence: 2/2 = 100%   │
  └─────────────────┘      └───────────────────────────┘
   Asks a question           Gives the final answer
```

[🔝 Back to Top](#-table-of-contents)

---

## 4. Using the Decision Tree

> *Slide 18 — Use the decision tree*

**How to classify a new example:** follow the path from root to leaf.

**New example:** Age=young, Has Job=false, Own House=false, Credit Rating=good

```
  Trace:
  ┌──────────┐
  │   Age?   │  → Age = young → take "young" branch
  └────┬─────┘
  ┌─────┴──────┐
  │  Has job?  │  → Has Job = false → take "false" branch
  └─────┬──────┘
        │
       No  ← LEAF: Class = No (reject the application)
      (3/3)

  Answer: REJECT
```

**General rule:** at each decision node, match the attribute value → follow that branch → repeat until leaf.

[🔝 Back to Top](#-table-of-contents)

---

## 5. Is the Decision Tree Unique?

> *Slide 19 — Is the decision tree unique?*

**No.** The slide shows two valid trees for the same data:

```
  TREE (A) — Rooted at Age          TREE (B) — Rooted at Own House
  ────────────────────────          ──────────────────────────────
        ┌───────┐                          ┌────────────┐
        │  Age? │                          │ Own house? │
        └───┬───┘                          └─────┬──────┘
    ┌───────┼───────┐                    ┌───────┴───────┐
  Young   Middle   Old                 true           false
    │       │        │                   │               │
  No:3    No:2     No:1               No: 0           No: 6
  Yes:2   Yes:3    Yes:4              Yes: 6          Yes: 3

  (A) No branch is pure              (B) Left branch is PURE!
                                         → TREE B IS BETTER
```

**Key insight from the slide:**

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  We want: SMALLER tree  +  ACCURATE tree                        │
  │  Smaller = easier to understand + generalise better             │
  │                                                                 │
  │  BUT: Finding the globally BEST tree is NP-hard.                │
  │  All current tree-building algorithms are HEURISTIC.            │
  │  They make the best LOCAL choice at each step.                  │
  │  Not guaranteed to find the global optimum.                     │
  └─────────────────────────────────────────────────────────────────┘
```

[🔝 Back to Top](#-table-of-contents)

---

## 6. From Tree to Rules

> *Slide 20 — From a decision tree to a set of rules*

Every decision tree converts mechanically to IF-THEN rules. **Each root-to-leaf path = one rule.**

```
  THE TREE (from slide):

        ┌────────────┐
        │ Own house? │
        └─────┬──────┘
         ┌────┴────┐
       true      false
         │          │
        Yes      ┌──┴──────┐
       (6/6)     │ Has job?│
                 └────┬────┘
               ┌──────┴──────┐
             true           false
               │               │
              Yes              No
             (5/5)            (4/4)

  ──────────────────────────────────────────────────────────────
  THE 3 RULES:

  Rule 1 (Path: Own house=true → Yes):
    Own house = true
    → Class = Yes    [support=6/15, confidence=6/6=100%]

  Rule 2 (Path: Own house=false, Has job=true → Yes):
    Own house = false  AND  Has job = true
    → Class = Yes    [support=5/15, confidence=5/5=100%]

  Rule 3 (Path: Own house=false, Has job=false → No):
    Own house = false  AND  Has job = false
    → Class = No     [support=4/15, confidence=4/4=100%]
  ──────────────────────────────────────────────────────────────
```

**Support vs Confidence:**

| Metric | Formula | Meaning |
|---|---|---|
| **Support** | (examples covered) / (total) | How often this rule fires |
| **Confidence** | (correctly classified) / (covered) | How accurate when it fires |

[🔝 Back to Top](#-table-of-contents)

---

## 7. Algorithm for Decision Tree Learning

> *Slide 21 — Algorithm for decision tree learning*

**Basic algorithm: greedy divide-and-conquer**

```
  PROPERTIES:
    Type:       Greedy, divide-and-conquer
    Direction:  Top-down, recursive
    Start:      All training examples at the root
    Split:      Based on impurity function (e.g., information gain)

  FLOW:
  ┌─────────────────────────────────────────────────────────────┐
  │  ALL examples at root                                       │
  │              ↓                                              │
  │  Pick BEST attribute → split into subsets                   │
  │              ↓                                              │
  │  For each subset → RECURSE                                  │
  │              ↓                                              │
  │  Stop when a stopping condition is met                      │
  └─────────────────────────────────────────────────────────────┘
```

**Three Stopping Conditions:**

```
  STOP 1 — Purity:
    All examples in subset belong to the SAME class
    → Leaf node labelled with that class

  STOP 2 — No attributes:
    A is empty (all attributes used up)
    → Leaf node labelled with MAJORITY class

  STOP 3 — No examples:
    Subset is empty
    → Leaf node labelled with parent's majority class
```

[🔝 Back to Top](#-table-of-contents)

---

## 8. The Formal Algorithm

> *Slide 22 — Decision tree learning algorithm (pseudocode)*

```
Algorithm decisionTree(D, A, T)
─────────────────────────────────────────────────────────────────────
INPUT:
  D = training examples at current node
  A = set of available attributes
  T = current tree node being built
─────────────────────────────────────────────────────────────────────

1   IF D contains only examples of the same class ci THEN
2       make T a leaf node labeled class ci
        RETURN                              ← Stopping Condition 1

3   ELSEIF A = empty THEN
4       make T a leaf node labeled with majority class in D
        RETURN                              ← Stopping Condition 2

5   ELSE   (D has mixed classes, attributes still available)

6       p0 = impurityEval(D)               ← baseline entropy

7       FOR each attribute Ai in A DO
8           pi = impurityEval(Ai, D)       ← post-split entropy
9       END

10      Select Ag = attribute with BIGGEST reduction (p0 - pi)

11      IF (p0 - p_Ag) < threshold THEN   ← gain too small
12          make T a leaf with majority class
            RETURN                          ← Pre-pruning stop

13      ELSE
14          Make T a DECISION NODE on Ag
15          Partition D into subsets D1, D2, ..., Dm
            (one subset per value of Ag)

16          FOR each Dj in {D1, ..., Dm} DO
17              IF Dj is not empty THEN
18                  Create child node Tj
19                  decisionTree(Dj, A minus {Ag}, Tj)   ← RECURSE
20              END
21          END
22      END
23  END
─────────────────────────────────────────────────────────────────────
```

**Line-by-line plain English:**

| Lines | What happens |
|---|---|
| 1–2 | All one class → leaf. Done. |
| 3–4 | No attributes left → majority vote → leaf. Done. |
| 6 | Measure current entropy (how impure is D now). |
| 7–9 | For each remaining attribute, measure post-split entropy. |
| 10 | Pick the attribute with the biggest entropy drop. |
| 11–12 | If best gain is tiny → stop now (pre-pruning). |
| 14–15 | Make a decision node; split D into one subset per value. |
| 16–21 | For each non-empty subset: recurse (Ag removed from A). |

[🔝 Back to Top](#-table-of-contents)

---

## 9. Choosing an Attribute to Partition

> *Slide 23 — Choose an attribute to partition data*

```
  ┌─────────────────────────────────────────────────────────────┐
  │  GOAL: Choose the attribute that reduces                    │
  │        impurity as MUCH as possible                         │
  │                                                             │
  │  KEY DEFINITION:                                            │
  │  A subset is PURE if ALL instances belong to the same class │
  │  → entropy = 0                                              │
  │                                                             │
  │  C4.5 HEURISTIC:                                            │
  │  Choose attribute with maximum Information Gain             │
  │  or Gain Ratio (based on information theory)                │
  └─────────────────────────────────────────────────────────────┘
```

**Purity spectrum:**

```
  entropy = 0            entropy ≈ 0.5          entropy = 1
      │                      │                      │
      ▼                      ▼                      ▼
  ██████████           ███████░░░░░           █████░░░░░░
  All one class        Mostly one class       50/50 split
  PURE — stop!         Leaning one way        MAX confusion
```

**Choosing the right question:**

```
  Good split → subsets become PURER than before → high gain
  Bad split  → subsets stay as mixed as before  → low gain

  Intuition: "Which question helps me guess the answer fastest?"
```

[🔝 Back to Top](#-table-of-contents)

---

## 10. Information Theory

> *Slides 26 and 27 — Information theory*

The entropy formula comes from information theory.

```
  CORE IDEA:
  "How much would you pay for advance information about an outcome?"

  Fair coin (50/50):
    → You have NO idea what's coming
    → Advance information is VERY VALUABLE
    → High entropy = high uncertainty

  Rigged coin (heads 99%):
    → You already know the outcome
    → Advance information has little value
    → Low entropy = low uncertainty

  ┌─────────────────────────────────────────────────┐
  │  Less you know  =  more valuable the info        │
  │  More you know  =  less valuable the info        │
  │  Entropy MEASURES this uncertainty in BITS       │
  └─────────────────────────────────────────────────┘
```

**What is a bit?**

```
  1 bit = enough information to answer 1 yes/no question
          about which you have NO prior knowledge

  Example — fair coin flip:
    Before: you know nothing → 1 bit of uncertainty
    After:  you know the result → 0 bits remaining

  Example — 99% heads coin:
    Before: you strongly suspect heads → < 0.08 bits
    After:  almost no new information gained
```

**Why bits instead of dollars?**

Information theory translates the "value of information" from subjective dollars into an objective, universal, mathematical unit: **bits**.

[🔝 Back to Top](#-table-of-contents)

---

## 11. Entropy Measure

> *Slide 28 — Information theory: Entropy measure*

**The Entropy Formula:**

$$\text{entropy}(D) = -\sum_{j=1}^{|C|} \Pr(c_j) \cdot \log_2 \Pr(c_j)$$

**Every symbol explained:**

```
  entropy(D)         Measure of disorder / impurity in dataset D

  |C|                Number of distinct classes
                     (binary classification: |C|=2)

  j                  Class index  (j = 1, 2, ..., |C|)

  Pr(cj)             Probability of class cj in D
                     = count(class cj) / total examples

  log2 Pr(cj)        Always NEGATIVE (probabilities < 1)
                     The rarer the class, the more negative

  -Pr(cj) * log2Pr   Each class contributes a POSITIVE term
                     (negative times negative = positive)

  Sigma (sum)        Sum contributions from ALL classes
```

**What the values mean:**

```
  ┌──────────────────────────────────────────────────────────────┐
  │  entropy = 0.000   Dataset is PERFECTLY PURE                 │
  │                    All examples are one class                │
  │                    → Make a LEAF node, stop splitting        │
  │                                                              │
  │  entropy = 1.000   Maximum UNCERTAINTY (binary case)         │
  │                    50% positive, 50% negative                │
  │                    → Must keep splitting                     │
  │                                                              │
  │  0 < entropy < 1   Somewhere in between                      │
  │                    Lower = purer = better                    │
  └──────────────────────────────────────────────────────────────┘
```

**Special convention:** `0 × log₂(0) = 0` (defined, not undefined). A class with 0 examples contributes 0 to entropy.

[🔝 Back to Top](#-table-of-contents)

---

## 12. Entropy: Worked Examples

> *Slide 29 — Entropy measure: let us get a feeling*

### Case 1 — 50/50 split → entropy = 1.0 (maximum)

```
  Pr(positive) = 0.5,   Pr(negative) = 0.5
  log2(0.5) = -1

  entropy = -(0.5 × -1) - (0.5 × -1)
           = 0.5 + 0.5
           = 1.0   ← maximum disorder

  Meaning: Complete uncertainty. You know nothing.
```

### Case 2 — 20/80 split → entropy = 0.722

```
  Pr(positive) = 0.2,   Pr(negative) = 0.8

  log2(0.2) = log10(0.2)/0.3010 = -0.699/0.301 = -2.322
  log2(0.8) = log10(0.8)/0.3010 = -0.097/0.301 = -0.322

  entropy = -(0.2 × -2.322) - (0.8 × -0.322)
           = 0.464 + 0.258
           = 0.722

  Meaning: Leaning towards negative, but still some uncertainty.
```

### Case 3 — 100/0 split → entropy = 0.0 (pure!)

```
  Pr(positive) = 1.0,   Pr(negative) = 0.0

  log2(1.0) = 0
  0 × log2(0) = 0   (special convention)

  entropy = -(1.0 × 0) - (0)
           = 0.0   ← perfectly pure!

  Meaning: All examples are the same class. Make a leaf node. Stop.
```

### The Slide's Key Takeaway:

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  "As the data become purer and purer, the entropy value         │
  │   becomes smaller and smaller. This is useful to us!"           │
  │                                        — Bing Liu, UIC          │
  └─────────────────────────────────────────────────────────────────┘
```

### Entropy Curve

```
  entropy
   1.0 ┤              *              ← 50/50 peak
       │          *       *
   0.7 ┤       *             *       ← 20/80 or 80/20
       │     *                 *
   0.4 ┤   *                     *
       │  *                       *
   0.1 ┤ *                         *
       │*                           *
   0.0 *─────────────────────────────* ← 0/100 or 100/0 (pure)
       0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0
                         Pr(positive class)
```

[🔝 Back to Top](#-table-of-contents)

---

## 13. Information Gain

> *Slides 30 and 31 — Information gain*

**Concept:** How much does splitting on attribute Aᵢ reduce entropy?

```
  Gain = entropy BEFORE split  -  entropy AFTER split
       = How messy things were  -  How messy things are now
```

### Formula 1 — Entropy of current node:

$$\text{entropy}(D) = -\sum_{j=1}^{|C|} \Pr(c_j) \cdot \log_2 \Pr(c_j)$$

### Formula 2 — Expected entropy after splitting on Aᵢ:

$$\text{entropy}_{A_i}(D) = \sum_{j=1}^{v} \frac{|D_j|}{|D|} \times \text{entropy}(D_j)$$

### Formula 3 — Information Gain:

$$\text{gain}(D, A_i) = \text{entropy}(D) - \text{entropy}_{A_i}(D)$$

**Symbol reference:**

| Symbol | Meaning | Example |
|---|---|---|
| `D` | Dataset at current node | All 15 loan records |
| `Aᵢ` | Attribute being evaluated | "Own House" |
| `v` | Number of distinct values of Aᵢ | Own House: v=2 |
| `Dⱼ` | Subset where Aᵢ = its j-th value | D₁ = {Own House=true} |
| `Dⱼ / D` | Weight = fraction of data in subset | 6/15 = 0.40 |

**Decision rule:**

```
  ╔══════════════════════════════════════════════════════════════╗
  ║  Choose the attribute with the HIGHEST gain.                 ║
  ║  It reduces impurity the most → gives the best split.        ║
  ╚══════════════════════════════════════════════════════════════╝
```

**Visual intuition:**

```
  Before split: all 15 examples mixed → entropy = 0.971
  ┌─────────────────────────────────────────┐
  │  ○ ○ ○ ○ ○ ○ ● ● ● ● ● ● ● ● ●        │  9 Yes, 6 No
  └─────────────────────────────────────────┘

  After split on Own House:
  ┌──────────────────┐     ┌────────────────────────────┐
  │  Own House=true  │     │  Own House=false           │
  │  ● ● ● ● ● ●     │     │  ○ ○ ○ ○ ○ ○  ● ● ●        │
  │  6 Yes, 0 No     │     │  6 No, 3 Yes               │
  │  entropy = 0.000 │     │  entropy = 0.918           │
  │  PURE!           │     │  Still mixed, recurse      │
  └──────────────────┘     └────────────────────────────┘

  Weighted after = (6/15)×0.000 + (9/15)×0.918 = 0.551
  Gain = 0.971 - 0.551 = 0.420  ← best of all 4 attributes
```

[🔝 Back to Top](#-table-of-contents)

---

## 14. Full Worked Example — Loan Dataset

> *Slide 32 — An example*

### Root Entropy

$$\text{entropy}(D) = -\frac{9}{15}\log_2\frac{9}{15} - \frac{6}{15}\log_2\frac{6}{15} = 0.971$$

```
  Pr(Yes) = 9/15 = 0.6  → -(0.6 × -0.737) = +0.442
  Pr(No)  = 6/15 = 0.4  → -(0.4 × -1.322) = +0.529
  entropy(D) = 0.442 + 0.529 = 0.971
```

---

### Gain for Age (3 values: young / middle / old)

| Age | Yes | No | Total | Entropy |
|---|---|---|---|---|
| young | 2 | 3 | 5 | 0.971 |
| middle | 3 | 2 | 5 | 0.971 |
| old | 4 | 1 | 5 | 0.722 |

$$\text{entropy}_\text{Age}(D) = \frac{5}{15}(0.971) + \frac{5}{15}(0.971) + \frac{5}{15}(0.722) = 0.888$$

$$\text{gain}(D,\text{Age}) = 0.971 - 0.888 = \mathbf{0.083}$$

---

### Gain for Own House (2 values: true / false)

| Own House | Yes | No | Total | Entropy |
|---|---|---|---|---|
| true | 6 | 0 | 6 | **0.000** (pure!) |
| false | 3 | 6 | 9 | 0.918 |

$$\text{entropy}_\text{OwnHouse}(D) = \frac{6}{15}(0) + \frac{9}{15}(0.918) = 0.551$$

$$\text{gain}(D,\text{OwnHouse}) = 0.971 - 0.551 = \mathbf{0.420}$$

---

### Gain for Has Job (2 values: true / false)

| Has Job | Yes | No | Total | Entropy |
|---|---|---|---|---|
| true | 5 | 0 | 5 | **0.000** (pure!) |
| false | 4 | 6 | 10 | 0.971 |

$$\text{entropy}_\text{HasJob}(D) = \frac{5}{15}(0) + \frac{10}{15}(0.971) = 0.647$$

$$\text{gain}(D,\text{HasJob}) = 0.971 - 0.647 = \mathbf{0.324}$$

---

### Gain for Credit Rating (3 values: fair / good / excellent)

| Credit Rating | Yes | No | Total | Entropy |
|---|---|---|---|---|
| fair | 1 | 4 | 5 | 0.722 |
| good | 4 | 2 | 6 | 0.918 |
| excellent | 4 | 0 | 4 | **0.000** (pure!) |

$$\text{entropy}_\text{Credit}(D) = \frac{5}{15}(0.722) + \frac{6}{15}(0.918) + \frac{4}{15}(0) = 0.608$$

$$\text{gain}(D,\text{CreditRating}) = 0.971 - 0.608 = \mathbf{0.363}$$

---

### Gain Comparison — from Slide 32

```
  ┌──────────────────────┬──────────────┬──────────────┐
  │  Attribute           │  Weighted    │  Gain        │
  │                      │  Entropy     │              │
  ├──────────────────────┼──────────────┼──────────────┤
  │  Age                 │  0.888       │  0.083       │
  │  Has Job             │  0.647       │  0.324       │
  │  Credit Rating       │  0.608       │  0.363       │
  │  Own House           │  0.551       │  0.420  ✅   │
  └──────────────────────┴──────────────┴──────────────┘

  Slide conclusion: "Own house is the best choice for the root."
```

[🔝 Back to Top](#-table-of-contents)

---

## 15. Building the Final Tree

> *Slide 33 — We build the final tree*

After choosing Own House as root, recurse on each branch:

**Branch 1: Own House = true**
6 Yes, 0 No → entropy = 0 → LEAF: Yes (6/6)

**Branch 2: Own House = false**
3 Yes, 6 No → entropy = 0.918 → not pure → recurse with {Age, Has Job, Credit Rating}
Among these 9 examples, Has Job wins → splits perfectly:
- Has Job = true → 5 Yes, 0 No → LEAF: Yes (5/5)
- Has Job = false → 0 Yes, 4 No → LEAF: No (4/4)

**The final tree (from slide):**

```
                  ┌────────────────┐
                  │  Own house?    │   ← ROOT  (gain = 0.420)
                  └───────┬────────┘
           ┌──────────────┴──────────────┐
         true                          false
           │                              │
        ✅ Yes                   ┌───────┴────────┐
         (6/6)                   │   Has job?     │
                                 └───────┬────────┘
                          ┌──────────────┴──────────────┐
                        true                          false
                          │                              │
                       ✅ Yes                        ❌ No
                        (5/5)                         (4/4)

  Rules:
    Own house = true                       → Yes  [conf=6/6=100%]
    Own house = false, Has job = true      → Yes  [conf=5/5=100%]
    Own house = false, Has job = false     → No   [conf=4/4=100%]

  Training accuracy: 15/15 = 100%
```

**Slide note:** "We can use information gain ratio to evaluate the impurity as well."

**Gain Ratio formula (C4.5):**

$$\text{GainRatio}(D, A_i) = \frac{\text{gain}(D, A_i)}{\text{SplitInfo}(A_i)}$$

$$\text{SplitInfo}(A_i) = -\sum_{j=1}^{v} \frac{|D_j|}{|D|} \cdot \log_2 \frac{|D_j|}{|D|}$$

[🔝 Back to Top](#-table-of-contents)

---

## 16. Handling Continuous Attributes

> *Slide 34 — Handling continuous attributes*

Continuous values (temperature, salary, age as a number) cannot have one branch per value. The solution: **binary threshold split**.

**Strategy:**

```
  Instead of: Temp=15 → ..., Temp=18 → ..., Temp=22 → ... (impractical)

  Use a threshold:
    Temp ≤ 23.5  →  Left branch
    Temp  > 23.5  →  Right branch
```

**Algorithm to find best threshold:**

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  STEP 1: Sort all values in increasing order                    │
  │          {v1, v2, v3, ..., vr}                                  │
  │                                                                 │
  │  STEP 2: Candidate thresholds = midpoints between adjacent      │
  │          values: t = (vi + vi+1) / 2                            │
  │                                                                 │
  │  STEP 3: For each candidate threshold t:                        │
  │          Split into {x ≤ t}  and  {x > t}                       │
  │          Compute information gain (or gain ratio)               │
  │                                                                 │
  │  STEP 4: Choose threshold with MAXIMUM gain                     │
  └─────────────────────────────────────────────────────────────────┘
```

**Why midpoints?**

```
  Values:     15   18   22   25   30   35
  Classes:    No   No   No  Yes  Yes  Yes

  Candidates: 16.5  20.0  23.5  27.5  32.5
                            ↑
                    Best threshold!
                    Sits at the class boundary

  Left  (≤23.5): {15,18,22} → all No  → entropy = 0 (pure!)
  Right  (>23.5): {25,30,35} → all Yes → entropy = 0 (pure!)
  Gain = 1.0 - 0 = 1.0  ← PERFECT SPLIT
```

[🔝 Back to Top](#-table-of-contents)

---

## 17. Continuous Attribute Example

> *Slide 35 — An example in a continuous space*

The slide shows a 2D dataset (features X, Y) and its decision tree:

```
  DATA SPACE (X-Y plot):                 RESULTING DECISION TREE:
  ■ = Class 1 (black squares)
  ○ = Class 2 (white circles)                   ┌─────┐
                                                 │  X  │
  Y↑                                             └──┬──┘
  2.6│■ ■ ○  ○   ○  ○                        ≤2  ╱  ╲ >2
  2.5│■ ■  ○   ○   ○                            ╱    ╲
    2│■ ■  ■  ○○ ○                         ┌───┐      ┌───┐
     │■ ■ ■ ■ ■ ○ ○                        │ Y │      │ Y │
     │     ■ ■ ■ ○○                         └─┬─┘      └─┬─┘
     └──────────────→X                   ≤2.5 >2.5    ≤2 >2
       0    2   3  4                      ■    ...    ...  ○

  Decision boundaries are AXIS-ALIGNED
  (horizontal and vertical lines only)
  Each rectangular region = one leaf node
```

**Key property:**

```
  Decision trees create RECTANGULAR regions in feature space.
  Advantage:    Very interpretable
  Disadvantage: Cannot capture diagonal decision boundaries
                naturally — may need many splits to approximate
```

[🔝 Back to Top](#-table-of-contents)

---

## 18. Avoiding Overfitting

> *Slide 36 — Avoid overfitting in classification*

**What is overfitting?**

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  A tree may OVERFIT the training data                           │
  │                                                                 │
  │  Symptom:  High accuracy on TRAINING data                       │
  │            Poor accuracy on TEST data / new examples            │
  │                                                                 │
  │  Signs:    Tree is too DEEP                                     │
  │            Too many BRANCHES                                    │
  │            Some branches reflect NOISE or OUTLIERS              │
  └─────────────────────────────────────────────────────────────────┘
```

**Two strategies to avoid overfitting:**

```
  ┌──────────────────┬───────────────────────────────────────────────┐
  │  APPROACH        │  HOW IT WORKS                                 │
  ├──────────────────┼───────────────────────────────────────────────┤
  │  Pre-pruning     │  STOP early before tree grows too deep        │
  │  (Early stop)    │  • Stop if gain < threshold                   │
  │                  │  • Stop if node has fewer than min examples   │
  │                  │                                               │
  │                  │  PROBLEM: Hard to decide when to stop.        │
  │                  │  May miss a great split just ahead.           │
  ├──────────────────┼───────────────────────────────────────────────┤
  │  Post-pruning    │  Grow FULL tree, then TRIM back               │
  │  (Most common)   │  Remove branches that do not help             │
  │                  │                                               │
  │                  │  C4.5: uses statistical error estimation      │
  │                  │  Alternative: use a VALIDATION SET            │
  │                  │  to test which branches hurt accuracy         │
  └──────────────────┴───────────────────────────────────────────────┘
```

**Trade-off:**

```
  Perfect fit on training:   100% train acc,  60% test acc  ← BAD
  Pruned tree:                90% train acc,  88% test acc  ← GOOD

  Moral: Being LESS perfect on training can make you
         MORE accurate on real unseen data.
```

[🔝 Back to Top](#-table-of-contents)

---

## 19. Overfitting Example

> *Slide 37 — An example (Likely to overfit the data)*

The slide shows the same 2D continuous dataset with two trees:

```
  OVERFITTED TREE                       PRUNED TREE
  ───────────────────────────           ───────────────────────────
  Many levels, memorises noise          Fewer levels, generalises

         ┌─────┐                               ┌─────┐
         │  X  │                               │  X  │
         └──┬──┘                               └──┬──┘
      ≤2  ╱  ╲ >2                          ≤2  ╱  ╲ >2
      ┌───┐   ┌───┐                         ■      ┌───┐
      │ Y │   │ Y │                                │ Y │
      └─┬─┘   └─┬─┘                               └─┬─┘
   ≤2.5 >2.5 ≤2  >2                            ≤2    >2
    ■   ┌Y┐  ┌X┐  ○                           ┌───┐    ○
        2.6>  ≤3 >3                            │ X │
         ■    ■  ┌X┐                          └─┬─┘
               ≤4  >4                         ≤3  >3
               ○    ■                          ■   ┌X┐
                                                  ≤4 >4
                                                  ○   ■

  6 levels deep, fits every            3 levels deep, ignores
  noisy outlier perfectly              noise, generalises well
```

**Rule of thumb:**

```
  Prune branches where gain is due to NOISE (few examples, unusual)
  Keep branches where gain is due to SIGNAL (many examples, consistent)

  C4.5 uses statistical confidence intervals to decide which is which.
```

[🔝 Back to Top](#-table-of-contents)

---

## 20. Other Issues in Decision Tree Learning

> *Slide 38 — Other issues in decision tree learning*

```
  ┌─────────────────────────────────────────────────────────────┐
  │  ADVANCED TOPICS (beyond the core algorithm):               │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  1. From tree to rules, and rule pruning                    │
  │     Remove redundant conditions from converted rules        │
  │                                                             │
  │  2. Handling missing values                                 │
  │     What if an attribute is unknown for an example?         │
  │     Strategies: skip, fill most common value, distribute    │
  │                                                             │
  │  3. Handling skewed distributions                           │
  │     When one class is very rare (e.g., fraud = 0.1%)        │
  │     Entropy dominated by majority → need cost-sensitivity   │
  │                                                             │
  │  4. Attributes and classes with different costs             │
  │     Misclassifying cancer as benign is far worse than       │
  │     the reverse → costs must be factored into splitting     │
  │                                                             │
  │  5. Attribute construction                                  │
  │     Create new derived attributes to improve splits         │
  │     e.g., income brackets, age groups, ratios               │
  │                                                             │
  │  6. Etc. — active research area!                            │
  └─────────────────────────────────────────────────────────────┘
```

[🔝 Back to Top](#-table-of-contents)

---

## 21. Cheat Sheet and Mnemonics

> Quick-recall reference for exams and revision

### The Big Picture — "SEGS"

```
  S — Split on best attribute (highest Information Gain)
  E — Entropy measures disorder  (0 = pure, 1 = max confusion)
  G — Gain = entropy BEFORE − entropy AFTER split
  S — Stop when pure, no attributes left, or gain < threshold
```

---

### Entropy Rules — "PZML"

```
  P — Probabilities always sum to 1.0
  Z — Zero entropy = pure node → STOP, make a leaf
  M — Maximum entropy = 1.0 (binary case) at 50/50
  L — Log₂ of any probability is NEGATIVE
      (formula has leading minus → entropy is always POSITIVE)
```

---

### Log₂ Quick Reference Card

```
  ┌──────────────────────────────────────────────────────────┐
  │  EXACT VALUES (memorise):                                │
  │    log₂(1.000) =  0.000   log₂(0.500) = -1.000           │
  │    log₂(0.250) = -2.000   log₂(0.125) = -3.000           │
  │                                                          │
  │  FORMULA (for everything else):                          │
  │    log₂(x) = log10(x) / 0.3010                           │
  │                                                          │
  │  COMMON EXAM VALUES:                                     │
  │    log₂(0.600) = -0.737      Pr = 9/15                   │
  │    log₂(0.400) = -1.322      Pr = 6/15                   │
  │    log₂(0.667) = -0.585      Pr = 2/3                    │
  │    log₂(0.333) = -1.585      Pr = 1/3                    │
  │    log₂(0.800) = -0.322      Pr = 4/5                    │
  │    log₂(0.200) = -2.322      Pr = 1/5                    │
  └──────────────────────────────────────────────────────────┘
```

---

### The Gain Calculation Flowchart

```
  ┌────────────────────────────────────────────────────────────┐
  │  1. Count classes in D                                     │
  │     → Pr(cj) = count(cj) / total                           │
  │                   ↓                                        │
  │  2. Compute entropy(D)                                     │
  │     = −Σ Pr(cj) × log₂(Pr(cj))                             │
  │                   ↓                                        │
  │  3. For each attribute Ai:                                 │
  │     a. Split D into subsets D1, D2, ..., Dv                │
  │     b. Compute entropy(Dj) for each subset                 │
  │     c. Weighted entropy = Σ (|Dj|/|D|) × entropy(Dj)       │
  │     d. gain = entropy(D) − weighted entropy                │
  │                   ↓                                        │
  │  4. Pick Ai with MAXIMUM gain → split here                 │
  │                   ↓                                        │
  │  5. Recurse on each subset (Ai removed from A)             │
  └────────────────────────────────────────────────────────────┘
```

---

### Decision Tree Quick Facts

```
  Type:         Supervised learning, classification
  Algorithm:    Greedy, top-down, divide-and-conquer
  Best system:  C4.5 by Ross Quinlan (uses Gain Ratio)
  Python:       sklearn uses CART with Gini impurity
  Unique?       NO — same data can produce many valid trees
  Optimal?      Finding the globally best tree is NP-hard
  How?          Heuristics (locally optimal at each step)
  Overfit?      YES — must prune (pre or post)
  Rules:        Each root-to-leaf path = one IF-THEN rule
```

---

### Splitting Criteria Comparison

```
  ┌───────────────┬──────────────────────┬───────────────────────┐
  │  Criterion    │  Formula             │  Used by              │
  ├───────────────┼──────────────────────┼───────────────────────┤
  │  Info Gain    │  entropy(D)          │  ID3 (original)       │
  │               │  - entropy_Ai(D)     │  biased to many vals  │
  ├───────────────┼──────────────────────┼───────────────────────┤
  │  Gain Ratio   │  Gain / SplitInfo    │  C4.5 (recommended)   │
  │               │  SplitInfo penalises │  corrects the bias    │
  │               │  wide/uneven splits  │                       │
  ├───────────────┼──────────────────────┼───────────────────────┤
  │  Gini         │  1 − Σ Pr(cj)²      │  CART / sklearn        │
  │               │  No log needed       │  fast to compute      │
  └───────────────┴──────────────────────┴───────────────────────┘
```

---

### Three Stopping Conditions

```
  ╔═══════════════════════════════════════════════════════════════╗
  ║  STOP 1 — All same class:   entropy = 0   → leaf node         ║
  ║  STOP 2 — No attributes:    A = empty      → majority vote    ║
  ║  STOP 3 — Gain too small:   gain < theta   → pre-prune        ║
  ╚═══════════════════════════════════════════════════════════════╝
```

[🔝 Back to Top](#-table-of-contents)

---

## 22. Formula Quick Reference

> Every formula from the slides in one place

### Entropy

$$\text{entropy}(D) = -\sum_{j=1}^{|C|} \Pr(c_j) \cdot \log_2 \Pr(c_j)$$

**Key values:**

| Distribution | Entropy |
|---|---|
| All one class (100/0) | **0.000** |
| 80/20 split | **0.722** |
| 60/40 split (9 Yes, 6 No) | **0.971** |
| 50/50 split | **1.000** |
| Three equal classes (1/3 each) | **1.585** |

### Expected Entropy After Split

$$\text{entropy}_{A_i}(D) = \sum_{j=1}^{v} \frac{|D_j|}{|D|} \times \text{entropy}(D_j)$$

### Information Gain

$$\text{gain}(D, A_i) = \text{entropy}(D) - \text{entropy}_{A_i}(D)$$

### Gain Ratio (C4.5)

$$\text{GainRatio}(D, A_i) = \frac{\text{gain}(D, A_i)}{\text{SplitInfo}(A_i)}$$

$$\text{SplitInfo}(A_i) = -\sum_{j=1}^{v} \frac{|D_j|}{|D|} \cdot \log_2 \frac{|D_j|}{|D|}$$

### Gini Impurity (CART / sklearn)

$$\text{Gini}(D) = 1 - \sum_{j=1}^{|C|} \Pr(c_j)^2$$

### Change of Base Formula

$$\log_2(x) = \frac{\log_{10}(x)}{0.30103} = \frac{\ln(x)}{0.69315}$$

### Loan Dataset Final Gain Summary

```
  ┌──────────────────┬──────────────┬──────────────┐
  │  Attribute       │  Weighted    │  Gain        │
  │                  │  Entropy     │              │
  ├──────────────────┼──────────────┼──────────────┤
  │  Age             │  0.888       │  0.083       │
  │  Has Job         │  0.647       │  0.324       │
  │  Credit Rating   │  0.608       │  0.363       │
  │  Own House       │  0.551       │  0.420  ✅   │
  └──────────────────┴──────────────┴──────────────┘
  Root node: Own House (highest gain = 0.420)
```

---

> **ML Course:** Subhash Bhagat, Sir..
> **Topic:** Decision Tree Learning — Entropy and Information Gain

[🔝 Back to Top](#-table-of-contents)
