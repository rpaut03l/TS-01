# ✂️ Topic 09 — Alpha-Beta Pruning

> **Difficulty**: 🔴 Hard | **Syllabus Section**: Adversarial Search 
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐⭐

---

## 🍼 The Big Story (ELI5)

### The Gift Bag Story 🎁

You're at a birthday party with 3 gift bags. You want the BEST gift. Your mean sister picks WHICH gift you get from each bag (she picks the worst one for you).

**Bag 1**: You look inside and see toys worth $8 and $3. Sister will pick $3 (the worst for you). So Bag 1 = $3.

**Bag 2**: You peek at the first toy — it's worth $2. 

🛑 **STOP! Think!** Your sister will pick the worst toy from Bag 2. The worst is AT MOST $2 (might be even worse if there are cheaper toys). But you already have Bag 1 = $3. Since $2 < $3, **Bag 2 can NEVER beat Bag 1!** 

**Skip the rest of Bag 2!** ✂️ That's **pruning!**

> 🍼 **The Simple Rule**: "I already have a guaranteed $3 from Bag 1. Bag 2 can give me at most $2. Why bother looking at the rest of Bag 2? Skip it!"

---

## 📚 Table of Contents

1. [Why Prune?](#1-why-prune)
2. [What Are α and β?](#2-alpha-beta)
3. [The Pruning Rules](#3-rules)
4. [🧮 Complete Trace #1 (Simple)](#4-trace-1)
5. [🧮 Complete Trace #2 (With Actual Pruning!)](#5-trace-2)
6. [How Much Does Pruning Save?](#6-savings)
7. [Key Takeaways](#7-key-takeaways)
8. [Exam Tips](#8-exam-tips)

---

## 1. Why Prune?

Minimax explores the ENTIRE game tree → O(b^m) nodes. For chess, that's 35^100 — impossible!

Alpha-Beta pruning gives the **EXACT SAME answer** as minimax but **skips branches** that can't possibly affect the final decision!

```
Minimax:      Looks at EVERY leaf
Alpha-Beta:   Skips "useless" branches → same answer, fewer nodes! 

Best case: examines only O(b^(m/2)) nodes — effectively DOUBLES the depth!
```

---

## 2. What Are α and β?

### The Definitions (Super Simple!)

| Symbol | Carried Along By | Meaning | ELI5 |
|---|---|---|---|
| **α (alpha)** | MAX | Best score MAX can guarantee SO FAR | "I already have at least THIS good" |
| **β (beta)** | MIN | Best score MIN can guarantee SO FAR | "I won't let MAX get more than THIS" |

```
α = "MAX's floor" — MAX will get AT LEAST this much
β = "MIN's ceiling" — MIN won't allow MORE than this for MAX
```

### When to Prune

**PRUNE when α ≥ β!**

```
If MAX says "I can guarantee at least $8" (α = 8)
And MIN says "I won't let you have more than $5" (β = 5)

α(8) ≥ β(5) → IMPOSSIBLE! This branch can't produce a useful result.
PRUNE IT! ✂️
```

> 🍼 **Kid Version**:
> - α is MAX saying: "I already found a gift worth $8. You need to beat that!"
> - β is MIN saying: "I'll make sure you don't get more than $5."
> - But $8 > $5... MAX wants ≥$8 but MIN gives ≤$5. Deal impossible! Skip!

---

## 3. The Pruning Rules

### At a MAX node: β-cutoff

```
After evaluating a child, update α = max(α, child_value)
If α ≥ β → PRUNE remaining children! ✂️
"I found something so good that MIN would never allow this path."
```

### At a MIN node: α-cutoff

```
After evaluating a child, update β = min(β, child_value)
If β ≤ α → PRUNE remaining children! ✂️
"MIN found something so bad for MAX that MAX would never choose this path."
```

---

## 4. 🧮 Complete Trace #1 (Simple — No Pruning)

Let's first trace WITHOUT any pruning happening, to understand the mechanics:

```
                    A (MAX)
                   /       \
            B (MIN)       C (MIN)
            / \            / \
           3   5          2   9
```

**Start: α = -∞, β = +∞** (no bounds yet)

**Step 1: Go to B (MIN node). B inherits α=-∞, β=+∞**

**Step 2: B's first child = 3**
```
β = min(+∞, 3) = 3     ← MIN found 3, so β = 3 now
Check: β(3) ≤ α(-∞)?   → 3 ≤ -∞? NO → Don't prune, continue
```

**Step 3: B's second child = 5**
```
β = min(3, 5) = 3       ← 5 is worse for MIN (bigger), keep β=3
B returns 3 to parent A
```

**Step 4: Back at A (MAX). Got 3 from B.**
```
α = max(-∞, 3) = 3      ← MAX now guarantees at least 3
```

**Step 5: Go to C (MIN node). C inherits α=3, β=+∞**

**Step 6: C's first child = 2**
```
β = min(+∞, 2) = 2      ← MIN found 2
Check: β(2) ≤ α(3)?     → 2 ≤ 3? YES! ✂️ PRUNE! 
```

**🎯 PRUNING HAPPENED!** C's second child (value 9) is **NEVER examined!**

**Why?** MIN at C already found value 2. C will return at most 2. But MAX at A already has 3 from B. Since 2 < 3, MAX will NEVER choose C. No point checking C's other children!

**Step 7: A returns max(3, 2) = 3. Best move = B.**

**Nodes examined**: 3, 5, 2 = **only 3 leaves** (skipped the 9!)
**Minimax would examine**: 3, 5, 2, 9 = **4 leaves**
**Savings**: 25%

---

## 5. 🧮 Complete Trace #2 (Larger Tree with Multiple Prunes!)

```
                           A (MAX)
                        /    |    \
                B (MIN)   C (MIN)   D (MIN)
               / \        / \        / \
              3   12     8   2      14   5
```

**Start: α = -∞, β = +∞**

---

**BRANCH B:**

**Go to B (MIN, α=-∞, β=+∞)**

B's child E = 3:
```
β = min(+∞, 3) = 3
β(3) ≤ α(-∞)? NO → continue
```

B's child F = 12:
```
β = min(3, 12) = 3     (12 is bigger, MIN keeps 3)
```

**B returns 3** to A.

**Back at A:** α = max(-∞, 3) = **3**

---

**BRANCH C:**

**Go to C (MIN, α=3, β=+∞)** ← Notice α=3 from branch B!

C's child G = 8:
```
β = min(+∞, 8) = 8
β(8) ≤ α(3)? → 8 ≤ 3? NO → continue
```

C's child H = 2:
```
β = min(8, 2) = 2
β(2) ≤ α(3)? → 2 ≤ 3? YES! ✂️ PRUNE!
```

But wait — C only has 2 children and we checked both. The pruning would trigger if there were MORE children. C returns **2**.

**Back at A:** α = max(3, 2) = **3** (no improvement)

---

**BRANCH D:**

**Go to D (MIN, α=3, β=+∞)**

D's child I = 14:
```
β = min(+∞, 14) = 14
β(14) ≤ α(3)? → 14 ≤ 3? NO → continue
```

D's child J = 5:
```
β = min(14, 5) = 5
β(5) ≤ α(3)? → 5 ≤ 3? NO → no pruning
```

**D returns 5.**

**Back at A:** α = max(3, 5) = **5** → **MAX chooses D!**

```
                        A = 5 (MAX) → Choose D!
                       /    |    \
              B = 3      C = 2     D = 5 ★
             / \        / \        / \
            3   12     8   2      14   5
```

### Summary of This Trace

| Node | α when entering | β when entering | Value returned | Pruning? |
|---|---|---|---|---|
| B | -∞ | +∞ | 3 | No |
| C | 3 | +∞ | 2 | β≤α after child H (2≤3) |
| D | 3 | +∞ | 5 | No |
| **A** | — | — | **5** | — |

---

## 6. How Much Does Pruning Save?

### Best Case: Perfect Move Ordering

If we ALWAYS explore the best move first:

```
Minimax:     O(b^d) nodes
Alpha-Beta:  O(b^(d/2)) nodes → SQUARE ROOT of minimax!
```

**This effectively DOUBLES the searchable depth!**

| Without pruning | With pruning | Improvement |
|---|---|---|
| Depth 4 | Depth 8 | 2× deeper! |
| Depth 6 | Depth 12 | 2× deeper! |

### Worst Case: Terrible Ordering

If we always explore the WORST move first: **no pruning at all** = same as minimax.

### How to Get Good Ordering

1. **Iterative deepening**: Search to depth 1, then 2, then 3... Use shallow results to order moves for deeper search
2. **Killer heuristic**: Moves that caused cutoffs before likely work again
3. **History heuristic**: Track which moves have been good across the search

---

## 7. Key Takeaways

1. **Alpha-Beta gives SAME result as minimax** but examines fewer nodes
2. **α** = MAX's guaranteed minimum score ("I have at least this")
3. **β** = MIN's guaranteed maximum for MAX ("I won't let you have more than this")
4. **Prune when α ≥ β** — this branch is irrelevant
5. **α-cutoff** at MIN nodes; **β-cutoff** at MAX nodes
6. **Best case: O(b^(d/2))** — effectively doubles searchable depth
7. **Move ordering is critical** — better ordering = more pruning

---

## 8. Exam Tips

### The Exam Trace Method (Do This EXACTLY!)

1. Write α = -∞, β = +∞ at the root
2. Traverse LEFT to RIGHT, DEPTH FIRST
3. At each node, inherit α, β from parent
4. After each child: at MAX nodes update α = max(α, child); at MIN nodes update β = min(β, child)
5. After updating: check if α ≥ β → if yes, PRUNE remaining children, write ✂️
6. Return the node's value to parent

### Common Mistakes

❌ **#1 Mistake**: Forgetting that α and β are INHERITED from the parent (not reset to -∞, +∞ at each node!)
❌ Updating α at MIN nodes or β at MAX nodes (α goes with MAX, β goes with MIN!)
❌ Pruning at the wrong time (prune AFTER updating, BEFORE next child)
❌ Confusing the returned value with α or β

### Memory Aid

- **α** = "**A**t **L**east" for MAX → MAX gets at least α
- **β** = "**B**elow" this for MAX → MIN keeps MAX below β
- **Prune**: α ≥ β → "MAX's floor hit MIN's ceiling — impossible, skip!"

---

## 📖 References

- AIMA — Chapter 5.3

---

[⬅️ Prev: Minimax](../08_Adversarial_Search_Minimax/README.md) | [Back to Main](../README.md) | [Next: Expectimax ➡️](../10_Expectimax_Search/README.md)
