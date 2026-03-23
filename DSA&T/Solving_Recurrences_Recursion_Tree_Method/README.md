# 🌳 Solving Recurrences — Recursion Tree Method — Crystal Clear Guide

> **One-Liner**: Draw a tree where each node is a piece of work. Add up all the work at each level. Sum all levels = total time!

---

## 🧒 ELI5 — Explain Like I'm 5

**Story time!** You're the boss of a toy factory.

You have a BIG job: sort 100 toys. But you're smart (and lazy in a good way!), so you say:

*"I'll split the work! I'll hire TWO helpers. Each helper sorts 50 toys."*

Each helper thinks the same way:

*"I'll hire TWO helpers. Each sorts 25 toys."*

This keeps going until someone has just **1 toy** (already sorted — easiest job ever!).

BUT, after the helpers are done, each boss has to **combine** (merge) the results. This takes time too!

Now imagine you draw this on paper:
- **You** at the top (100 toys, combine time = 100)
- **Your 2 helpers** below (50 toys each, combine time = 50 + 50 = 100)
- **Their 4 helpers** below (25 toys each, combine time = 25 × 4 = 100)
- ...all the way down until 100 people each have 1 toy.

**At EVERY level of the tree, the total work = 100!**
And there are about **log₂(100) ≈ 7 levels**.
So total work ≈ 100 × 7 = 700. That's **O(n log n)**!

---

## 📝 What Is a Recurrence? (Start Here!)

A **recurrence** is a math equation that describes how long an algorithm takes in terms of **smaller versions of itself**.

### What Does That Mean?

When you have a recursive algorithm (one that calls itself on smaller inputs), the time it takes can be written as:

```
"Time for big problem = Time for smaller problems + Time to combine"
```

For example, Merge Sort:
```
T(n) = 2 · T(n/2) + n
       ─────────   ─
       ↑             ↑
       time to sort   time to merge
       two halves     the two sorted halves
```

**In words**: "The time to sort n things = the time to sort two halves (each of size n/2) PLUS n units of work to merge them together."

### More Examples of Recurrences

| Algorithm | Recurrence | In Words |
|-----------|-----------|----------|
| Binary Search | T(n) = T(n/2) + c | "Look at one half + do O(1) work" |
| Merge Sort | T(n) = 2T(n/2) + cn | "Sort two halves + merge in O(n)" |
| Naive Fibonacci | T(n) = T(n-1) + T(n-2) + c | "Solve both smaller problems + O(1)" |

### The Big Question

Given a recurrence, **what is T(n) in simple form?** Is it O(n)? O(n log n)? O(n²)? O(2ⁿ)?

The **Recursion Tree Method** is a visual way to find the answer!

---

## 🌲 What Is the Recursion Tree Method?

The Recursion Tree Method converts a recurrence into a **tree diagram** where:
- Each **node** represents a subproblem
- The **value** at each node = the non-recursive work done at that level
- You **sum up** the work at each level
- Then you **sum all levels** to get the total

### The Recipe (Step by Step)

```
STEP 1: Write the recurrence.
        Example: T(n) = 2T(n/2) + cn

STEP 2: Draw the root.
        The root represents the original problem of size n.
        It does cn work (the non-recursive part).
        It has 2 children (because of the 2T).

STEP 3: Draw the children.
        Each child is a problem of size n/2.
        Each does c(n/2) work.
        Each has 2 children of its own.

STEP 4: Keep expanding until you reach the base case (size 1).

STEP 5: Calculate the TOTAL WORK at each level.
        Level k: (number of nodes) × (work per node)

STEP 6: Count the number of levels.
        We divide by b each time: n/b^k = 1 → k = log_b(n)

STEP 7: Sum the work across all levels.
        Often this is a geometric series!

STEP 8: Simplify to get the Big-O answer.
```

---

## 📐 Worked Example 1: T(n) = 2T(n/2) + n (Merge Sort)

This is the MOST IMPORTANT example. Let me go through it in extreme detail.

### Step 1: Identify the parts

```
T(n) = 2·T(n/2) + n
       ↑   ↑      ↑
       a   n/b    f(n)

a = 2      (number of subproblems = 2 children per node)
b = 2      (each subproblem is half the size)
f(n) = n   (non-recursive work at each node)
```

### Step 2-4: Draw the tree

```
Level 0 (root):
                        n                       ← 1 node, does n work
                       / \
Level 1:            n/2   n/2                   ← 2 nodes, each does n/2
                   / \   / \
Level 2:        n/4 n/4 n/4 n/4                 ← 4 nodes, each does n/4
                ...  ...  ...  ...
Level k:    (2^k nodes, each does n/2^k)
                ...
Level log₂n: (n nodes, each does 1)             ← BASE CASE
```

### Step 5: Calculate work per level

| Level | # Nodes | Work per Node | Total Work at Level |
|-------|---------|---------------|-------------------|
| 0 | 1 | n | 1 × n = **n** |
| 1 | 2 | n/2 | 2 × n/2 = **n** |
| 2 | 4 | n/4 | 4 × n/4 = **n** |
| 3 | 8 | n/8 | 8 × n/8 = **n** |
| ... | ... | ... | **n** |
| k | 2^k | n/2^k | 2^k × n/2^k = **n** |

**Key observation**: EVERY level does exactly **n** work! The number of nodes doubles, but the work per node halves, so they cancel out!

### Step 6: Count levels

We keep dividing by 2 until we reach size 1:
```
n / 2^k = 1
n = 2^k
k = log₂(n)
```

Number of levels = **log₂(n) + 1** (including level 0 and the base case level).

### Step 7: Sum all levels

```
Total = n + n + n + ... + n   (log₂(n) + 1 times)
      = n × (log₂(n) + 1)
      = n·log₂(n) + n
      = O(n log n)  ✅
```

**Answer: T(n) = O(n log n).** This is the time complexity of Merge Sort!

---

## 📐 Worked Example 2: T(n) = 3T(n/4) + n² (Root-Heavy)

### Step 1: Identify parts

```
a = 3 (3 children per node)
b = 4 (each child is size n/4)
f(n) = n² (work at each node)
```

### Step 2-4: Draw the tree

```
Level 0:       n²                           ← 1 node, does n² work
             / | \
Level 1: (n/4)² (n/4)² (n/4)²              ← 3 nodes, each does (n/4)² = n²/16
```

### Step 5: Work per level

| Level | # Nodes | Work per Node | Total at Level | Ratio to Previous |
|-------|---------|---------------|---------------|-------------------|
| 0 | 1 | n² | n² | — |
| 1 | 3 | n²/16 | 3n²/16 | 3/16 |
| 2 | 9 | n²/256 | 9n²/256 | 3/16 |
| k | 3^k | (n/4^k)² | n²×(3/16)^k | 3/16 |

**Pattern**: Each level's work is **(3/16)** times the previous level!

This is a **geometric series** with ratio r = 3/16.

### Step 6-7: Since r = 3/16 < 1, this is a DECREASING series!

```
Total = n² × (1 + 3/16 + (3/16)² + (3/16)³ + ...)
```

For a geometric series with ratio r < 1, the sum converges to:
```
Sum = first_term / (1 - r) = n² / (1 - 3/16) = n² / (13/16) = 16n²/13
```

**Total = O(n²)**

### What does this mean?

The ROOT does most of the work! Each level does LESS than the previous one. The root's work (n²) dominates everything. This is called a **root-heavy** tree.

---

## 📐 Worked Example 3: T(n) = 4T(n/2) + n (Leaf-Heavy)

### Step 5: Work per level

| Level | # Nodes | Work per Node | Total at Level |
|-------|---------|---------------|---------------|
| 0 | 1 | n | n |
| 1 | 4 | n/2 | 4 × n/2 = 2n |
| 2 | 16 | n/4 | 16 × n/4 = 4n |
| k | 4^k | n/2^k | 4^k × n/2^k = n × 2^k |

**Pattern**: Each level does **2 times** the work of the previous level!

This is a geometric series with ratio r = 2 > 1. **INCREASING** series!

### The Last Level (Leaves)

The tree has log₂(n) levels. The last level has **4^(log₂n) = n^(log₂4) = n²** nodes, each doing O(1) work.

Total at last level = n² × O(1) = O(n²)

Since the series is increasing, the **leaves dominate**:

**Total = O(n²)**

This is a **leaf-heavy** tree. Most work happens at the bottom!

---

## 📐 Worked Example 4: T(n) = T(n/3) + T(2n/3) + n (Uneven Split)

This is special because the Master Theorem DOESN'T directly apply (different-sized subproblems). But the Recursion Tree Method handles it beautifully!

### Drawing the tree

```
Level 0:              n                    Total: n
                   /      \
Level 1:        n/3       2n/3             Total: n/3 + 2n/3 = n
               / \       / \
Level 2:    n/9  2n/9  2n/9  4n/9          Total: n/9+2n/9+2n/9+4n/9 = n
```

**Every level sums to n!** Just like Merge Sort!

### But how many levels?

The tree is LOPSIDED. The LEFT path (always taking n/3) reaches 1 faster than the RIGHT path (always taking 2n/3).

- Shortest path: n → n/3 → n/9 → ... → 1. Depth = log₃(n).
- Longest path: n → 2n/3 → (2/3)²n → ... → 1. Depth = log₃/₂(n) ≈ 2.41 × log₂(n).

The levels near the bottom aren't completely full (some paths ended early), but every complete level sums to n.

**Total ≤ n × log₃/₂(n) = O(n log n)** ✅

---

## 📊 The Three Types of Trees — Cheat Sheet

When you compute the ratio between consecutive levels:

```
ratio = (total work at level k+1) / (total work at level k)
```

| If ratio... | What happens | Total dominated by | Name |
|------------|-------------|-------------------|------|
| < 1 | Each level does LESS work | ROOT (first term) | **Root-heavy** |
| = 1 | Every level does SAME work | ALL levels equally | **Balanced** |
| > 1 | Each level does MORE work | LEAVES (last term) | **Leaf-heavy** |

### Geometric Series Formulas

```
Sum = a + ar + ar² + ... + ar^k

If r < 1:  Sum ≈ a/(1-r) = O(a)          ← root dominates
If r = 1:  Sum = a × (k+1) = O(a × k)   ← all levels equal
If r > 1:  Sum ≈ a × r^k = O(last term)  ← leaves dominate
```

---

## 🔗 How This Connects to the Master Theorem

The Master Theorem is a SHORTCUT for recurrences T(n) = aT(n/b) + f(n):

| Case | Condition | Tree Type | Answer |
|------|-----------|-----------|--------|
| 1 | f(n) ≪ n^(log_b a) | Leaf-heavy | Θ(n^(log_b a)) |
| 2 | f(n) ≈ n^(log_b a) | Balanced | Θ(n^(log_b a) × log n) |
| 3 | f(n) ≫ n^(log_b a) | Root-heavy | Θ(f(n)) |

The Recursion Tree gives you the INTUITION for why these cases exist!

---

## 📋 Common Recurrences Reference Table

| Recurrence | Solution | Tree Type | Algorithm |
|-----------|----------|-----------|-----------|
| T(n) = T(n/2) + O(1) | O(log n) | Root-heavy | Binary Search |
| T(n) = 2T(n/2) + O(n) | O(n log n) | Balanced | Merge Sort |
| T(n) = 2T(n/2) + O(1) | O(n) | Leaf-heavy | Tree traversal |
| T(n) = T(n-1) + O(n) | O(n²) | Linear chain | Selection sort |
| T(n) = T(n-1) + O(1) | O(n) | Linear chain | Linear scan |
| T(n) = 2T(n-1) + O(1) | O(2ⁿ) | Exponential | Fibonacci (naive) |
| T(n) = 3T(n/4) + O(n²) | O(n²) | Root-heavy | — |
| T(n) = 4T(n/2) + O(n) | O(n²) | Leaf-heavy | — |

---

## 🧰 Problem-Solving Techniques

### Technique 1: Find the Pattern at Level k

For T(n) = aT(n/b) + f(n):
```
Level k cost = a^k × f(n / b^k)
```

Compute this for k = 0, 1, 2, 3. Look for a pattern — is it increasing, constant, or decreasing?

### Technique 2: Find the Ratio

```
ratio = level_(k+1)_cost / level_k_cost
```

If ratio < 1 → root-heavy → answer is O(f(n))
If ratio = 1 → balanced → answer is O(f(n) × log n)
If ratio > 1 → leaf-heavy → answer is O(n^(log_b a))

### Technique 3: Count the Leaves

Number of leaves = a^(depth) = a^(log_b n) = **n^(log_b a)**. This tells you the Case 1 (leaf-heavy) answer.

### Technique 4: Verify with Master Theorem

Use the tree to get a guess, then double-check with the Master Theorem formula.

---

## ⚠️ Common Mistakes

| Mistake | Fix |
|---------|-----|
| Forgetting that nodes MULTIPLY at each level | Level k has a^k nodes, not a×k |
| Wrong depth calculation | Depth = log_b(n), NOT always log₂(n) |
| Mixing up geometric series types | Check: is ratio <1, =1, or >1? |
| Ignoring the leaf cost | Leaves contribute n^(log_b a) × O(1) |
| Applying Master Theorem to T(n) = T(n-1) + ... | Master Theorem only works for T(n) = aT(n/b) + f(n) where b > 1! |

---

## 📝 Practice Questions with Detailed Solutions

### Q1: Solve T(n) = 4T(n/2) + n using recursion tree.

**Full Solution:**
```
Level k cost = 4^k × n/2^k = n × (4/2)^k = n × 2^k

This INCREASES with k → leaf-heavy!

Depth = log₂(n).
Leaf cost = n × 2^(log₂n) = n × n = n²
Total ≈ n + 2n + 4n + ... + n² = O(n²)

Alternatively: leaves = 4^(log₂n) = n^(log₂4) = n² → O(n²) ✅
```

### Q2: Solve T(n) = T(n/2) + n.

**Full Solution:**
```
Level 0: n. Level 1: n/2. Level 2: n/4. Level 3: n/8. ...
Ratio = 1/2 < 1 → root-heavy → root dominates!

Total = n + n/2 + n/4 + n/8 + ... = n × (1/(1-1/2)) = 2n = O(n) ✅
```

### Q3: Solve T(n) = 2T(n/2) + n². Root-heavy or leaf-heavy?

**Full Solution:**
```
Level 0: n². Level 1: 2×(n/2)² = n²/2. Level 2: 4×(n/4)² = n²/4.
Ratio = 1/2 < 1 → root-heavy → O(n²) ✅

Verify: n^(log₂2) = n¹ = n. f(n) = n² ≫ n → Case 3 → Θ(n²) ✅
```

### Q4: Solve T(n) = T(n-1) + n. (NOT divide-and-conquer!)

**Full Solution:**
```
This is a SUBTRACTIVE recurrence (n-1, not n/b). No tree needed — just expand!

T(n) = n + T(n-1)
     = n + (n-1) + T(n-2)
     = n + (n-1) + (n-2) + ... + 2 + 1
     = n(n+1)/2
     = O(n²)

This is Insertion Sort's worst-case behavior!
```

### Q5: Solve T(n) = 2T(n/2) + 1.

**Full Solution:**
```
Level 0: 1. Level 1: 2×1 = 2. Level 2: 4×1 = 4. Level k: 2^k.
Ratio = 2 > 1 → leaf-heavy!

Total = 1 + 2 + 4 + ... + 2^(log₂n) = 2^(log₂n + 1) - 1 = 2n - 1 = O(n)

Verify: n^(log₂2) = n. f(n) = 1 ≪ n → Case 1 → Θ(n) ✅
```

### Q6: How many levels in T(n) = 3T(n/9) + √n?

**Full Solution:**
```
We divide by 9 each time. Depth: n/9^k = 1 → k = log₉(n).

There are log₉(n) + 1 levels. For n=81: log₉(81) = 2, so 3 levels.
```

### Q7: T(n) = 8T(n/2) + n². Solve.

**Full Solution:**
```
Level k cost = 8^k × (n/2^k)² = 8^k × n²/4^k = n² × (8/4)^k = n² × 2^k

Ratio = 2 > 1 → leaf-heavy!
Leaves = 8^(log₂n) = n^(log₂8) = n³
Total = O(n³)

Verify: n^(log₂8) = n³. f(n) = n² ≪ n³ → Case 1 → Θ(n³) ✅
```

### Q8: Draw the tree for T(8) = 2T(4) + 8 with T(1) = 1.

**Full Solution:**
```
T(8) = 2T(4) + 8     Level 0: work = 8
T(4) = 2T(2) + 4     Level 1: 2 nodes × 4 = 8
T(2) = 2T(1) + 2     Level 2: 4 nodes × 2 = 8
T(1) = 1              Level 3: 8 nodes × 1 = 8

Tree:
           8                     Level 0: 8
         /   \
        4     4                  Level 1: 4+4=8
       / \   / \
      2   2 2   2                Level 2: 2×4=8
     /\ /\ /\ /\
    1 1 1 1 1 1 1 1              Level 3: 1×8=8

Total = 8 + 8 + 8 + 8 = 32 = 8 × 4 = n × (log₂n + 1) ✅
```

### Q9: T(n) = T(n/4) + T(3n/4) + cn. Solve.

**Full Solution:**
```
Level 0: cn
Level 1: cn/4 + 3cn/4 = cn
Level 2: cn/16 + 3cn/16 + 3cn/16 + 9cn/16 = 16cn/16 = cn

Every level = cn! (Just like Example 2 in the main section)

Longest path: n → 3n/4 → (3/4)²n → ... → 1, depth = log₄/₃(n)
Total ≤ cn × log₄/₃(n) = O(n log n) ✅
```

### Q10: Is T(n) = 2T(n/2) + n log n solvable by the Master Theorem?

**Full Solution:**
```
a=2, b=2, f(n) = n log n. n^(log_b a) = n^1 = n.

f(n) = n log n vs n. Is n log n = Θ(n × log^k(n)) for some k ≥ 1?
Yes! f(n) = n × log n = Θ(n × log¹ n). This falls into the EXTENDED Case 2.

By the extended Master Theorem: T(n) = Θ(n × log²(n)).

Recursion tree verification:
Level k: 2^k × (n/2^k) × log(n/2^k) = n × (log n - k)
Total = Σ(k=0 to log n) n × (log n - k) = n × (log n + (log n - 1) + ... + 0)
      = n × log n × (log n + 1) / 2 = Θ(n log² n) ✅
```

---

## 📋 Quick Revision Cheat Sheet

```
┌──────────────────────────────────────────────────────────────┐
│  RECURSION TREE METHOD — EVERYTHING IN ONE BOX               │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  FOR T(n) = a·T(n/b) + f(n):                                 │
│                                                              │
│  1. Level k has a^k nodes, each does f(n/b^k) work           │
│  2. Total at level k = a^k × f(n/b^k)                        │ 
│  3. Number of levels = log_b(n) + 1                          │
│  4. Number of leaves = a^(log_b n) = n^(log_b a)             │
│                                                              │
│  RATIO = total_at_level_(k+1) / total_at_level_k             │
│                                                              │
│  ratio < 1 → ROOT-HEAVY  → Total = O(f(n))                   │
│  ratio = 1 → BALANCED    → Total = O(f(n) × log n)           │
│  ratio > 1 → LEAF-HEAVY  → Total = O(n^(log_b a))            │
│                                                              │
│  WORKS EVEN FOR UNEVEN SPLITS (unlike Master Theorem!)       │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 📚 References

- CLRS — Introduction to Algorithms, Chapter 4 (Section 4.4: Recursion-tree method)
- Lec's 3 — Pr V Raj S, DSA
