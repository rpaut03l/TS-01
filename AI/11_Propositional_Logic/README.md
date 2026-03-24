# 📐 Topic 11 — Propositional Logic & Reasoning Patterns

> **Difficulty**: 🟡 Medium | **Syllabus Section**: Knowledge & Reasoning
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐⭐

---

## 🍼 The Big Story (ELI5)

### The Detective Story 🔍

You're a detective. You know some FACTS:
- "If it rained, the ground is wet." (a RULE)
- "It rained." (a FACT)

From these, you can DEDUCE: "The ground is wet!" without even going outside to check!

**That's what logic does** — it lets you discover NEW truths from OLD truths, just by thinking!

> 🍼 **Kid Version**: Logic is like a truth machine. You feed it things you KNOW are true. It churns and produces NEW things that MUST also be true. Like dominos — knock one over, and the rest fall automatically!

---

## 📚 Table of Contents

1. [What Is a Proposition?](#1-propositions)
2. [The 5 Connectives (AND, OR, NOT, IF-THEN, IFF)](#2-connectives)
3. [🧮 Truth Tables — How to Build Them](#3-truth-tables)
4. [Implication (→) — The Tricky One!](#4-implication)
5. [Logical Equivalences (Must Memorize!)](#5-equivalences)
6. [Inference Rules — Discovering New Truths](#6-inference)
7. [🧮 Resolution Proof — Complete Example](#7-resolution)
8. [Key Takeaways](#8-key-takeaways)
9. [Exam Tips](#9-exam-tips)

---

## 1. What Is a Proposition?

A **proposition** is a statement that is either **TRUE** or **FALSE**. Nothing in between!

| ✅ Propositions | ❌ NOT Propositions |
|---|---|
| "It is raining" → TRUE or FALSE | "What time is it?" → it's a question! |
| "2 + 2 = 4" → TRUE | "Close the door" → it's a command! |
| "Paris is in Germany" → FALSE | "Wow!" → it's an exclamation! |
| "The sky is green" → FALSE | "x + 5 = 10" → depends on x! (not fixed) |

**We use capital letters** to represent propositions: P, Q, R, S, etc.

```
P = "It is raining"
Q = "The ground is wet"
R = "I carry an umbrella"
```

---

## 2. The 5 Connectives

Connectives JOIN propositions together to make BIGGER statements:

### 2.1 NOT (¬) — Negation

```
¬P = "NOT P" = "It is NOT raining"

If P is TRUE  → ¬P is FALSE
If P is FALSE → ¬P is TRUE

It just FLIPS the truth value!
```

> 🍼 Like flipping a light switch: ON becomes OFF, OFF becomes ON.

### 2.2 AND (∧) — Conjunction

```
P ∧ Q = "P AND Q" = "It is raining AND the ground is wet"

Only TRUE when BOTH P and Q are TRUE!

P=TRUE,  Q=TRUE  → P ∧ Q = TRUE   "Raining AND wet? Yes, both!"
P=TRUE,  Q=FALSE → P ∧ Q = FALSE  "Raining but NOT wet? Not both!"
P=FALSE, Q=TRUE  → P ∧ Q = FALSE  "Not raining but wet? Not both!"
P=FALSE, Q=FALSE → P ∧ Q = FALSE  "Neither? Definitely not both!"
```

> 🍼 Like two keys needed to open a safe: BOTH must turn for it to open.

### 2.3 OR (∨) — Disjunction

```
P ∨ Q = "P OR Q" = "It is raining OR the ground is wet"

TRUE when AT LEAST ONE of P, Q is TRUE!

P=TRUE,  Q=TRUE  → P ∨ Q = TRUE   "Both true? At least one is, so yes!"
P=TRUE,  Q=FALSE → P ∨ Q = TRUE   "P is true? That's enough!"
P=FALSE, Q=TRUE  → P ∨ Q = TRUE   "Q is true? That's enough!"
P=FALSE, Q=FALSE → P ∨ Q = FALSE  "Neither is true? Then no."
```

**Important**: This is INCLUSIVE or — "A or B or both." NOT "A or B but not both."

> 🍼 Like a hallway with two doors: if EITHER door is open, you can get through.

### 2.4 IF-THEN (→) — Implication

This is THE TRICKIEST connective! See Section 4 below for a deep explanation.

```
P → Q = "IF P THEN Q" = "If it rains, then the ground is wet"
```

### 2.5 IF AND ONLY IF (↔) — Biconditional

```
P ↔ Q = "P if and only if Q"

TRUE when P and Q have the SAME truth value (both true or both false)

P=TRUE,  Q=TRUE  → TRUE   "Both true? Same value, yes!"
P=TRUE,  Q=FALSE → FALSE  "Different values!"
P=FALSE, Q=TRUE  → FALSE  "Different values!"
P=FALSE, Q=FALSE → TRUE   "Both false? Same value, yes!"
```

> 🍼 Like a twin detector: it says TRUE only if both twins are wearing the same color shirt.

---

## 3. 🧮 Truth Tables — How to Build Them

### Step-by-Step Method

1. **List all variables** (P, Q, R, ...)
2. **Count rows**: 2 variables → 4 rows. 3 variables → 8 rows. n variables → 2ⁿ rows.
3. **Fill in all combinations** of T/F
4. **Compute the formula** column by column, innermost first

### 🧮 Example: Build truth table for (P ∧ Q) → R

**Step 1**: 3 variables (P, Q, R) → 2³ = 8 rows

**Step 2**: Fill in combinations systematically:

| P | Q | R | P ∧ Q | (P ∧ Q) → R |
|---|---|---|---|---|
| T | T | T | T | **T** |
| T | T | F | T | **F** |
| T | F | T | F | **T** |
| T | F | F | F | **T** |
| F | T | T | F | **T** |
| F | T | F | F | **T** |
| F | F | T | F | **T** |
| F | F | F | F | **T** |

**How I computed column 4 (P ∧ Q)**:
```
Row 1: T ∧ T = T  (both true → and is true)
Row 2: T ∧ T = T
Row 3: T ∧ F = F  (not both true → and is false)
...etc
```

**How I computed column 5 ((P ∧ Q) → R)**:
```
Row 1: T → T = T   (true implies true → OK!)
Row 2: T → F = F   (true implies false → BROKEN promise!)
Row 3: F → T = T   (false premise → always true, see Section 4)
Row 4: F → F = T   (false premise → always true)
...etc
```

---

## 4. Implication (→) — The Tricky One!

### The Truth Table for P → Q

| P | Q | P → Q | Explanation |
|---|---|---|---|
| T | T | **T** | Promise kept! ✅ |
| T | F | **F** | Promise BROKEN! ❌ |
| F | T | **T** | Promise not tested (doesn't matter) |
| F | F | **T** | Promise not tested (doesn't matter) |

### 🍼 Mom's Promise Story (THE Way to Understand This!)

Your mom says: **"IF you eat your veggies, THEN you get dessert."**

Let P = "you eat veggies" and Q = "you get dessert."

**Case 1: P=T, Q=T** — You eat veggies AND you get dessert.
```
Mom kept her promise! → P → Q = TRUE ✅
```

**Case 2: P=T, Q=F** — You eat veggies but NO dessert!
```
Mom BROKE her promise! → P → Q = FALSE ❌
This is the ONLY case where implication is FALSE!
```

**Case 3: P=F, Q=T** — You DON'T eat veggies but you still get dessert.
```
Did mom break her promise? NO! She only promised dessert IF you ate veggies.
She never said "if you DON'T eat veggies, you DON'T get dessert."
Getting dessert anyway is fine — promise intact! → P → Q = TRUE ✅
```

**Case 4: P=F, Q=F** — You don't eat veggies and no dessert.
```
Mom's promise was about what happens IF you eat veggies.
You didn't eat them, so the promise doesn't apply either way.
→ P → Q = TRUE ✅
```

> 🍼 **The Golden Rule**: P → Q is ONLY FALSE when P is TRUE and Q is FALSE.
> "The promise is only broken when you DO your part but mom DOESN'T."
> If you don't do your part (P is false), the promise is automatically "not broken."

### The Most Important Equivalence

```
P → Q  ≡  ¬P ∨ Q

"If P then Q" is the SAME as "either NOT P, or Q (or both)"

Think about it: P → Q is false ONLY when P is true and Q is false.
¬P ∨ Q is false ONLY when ¬P is false AND Q is false → P is true AND Q is false.
Same thing! ✅
```

---

## 5. Logical Equivalences (Must Memorize!)

### The Essential List

| Name | Equivalence | ELI5 Memory Trick |
|---|---|---|
| **Double Negation** | ¬(¬P) ≡ P | "NOT NOT happy = happy" |
| **De Morgan's 1** | ¬(P ∧ Q) ≡ ¬P ∨ ¬Q | "NOT (A AND B) = NOT-A OR NOT-B" |
| **De Morgan's 2** | ¬(P ∨ Q) ≡ ¬P ∧ ¬Q | "NOT (A OR B) = NOT-A AND NOT-B" |
| **Implication** | P → Q ≡ ¬P ∨ Q | "IF P THEN Q = NOT-P OR Q" |
| **Contrapositive** | P → Q ≡ ¬Q → ¬P | "IF rain→wet = IF not-wet→not-rain" |
| **Biconditional** | P ↔ Q ≡ (P→Q) ∧ (Q→P) | "Both directions of implication" |

### 🍼 De Morgan's Laws — The Most Used!

```
¬(P ∧ Q) = ¬P ∨ ¬Q
"It's NOT the case that (it's raining AND cold)"
= "It's NOT raining OR it's NOT cold" (at least one isn't true)

¬(P ∨ Q) = ¬P ∧ ¬Q
"It's NOT the case that (it's raining OR cold)"
= "It's NOT raining AND it's NOT cold" (NEITHER is true)
```

> 🍼 **Memory trick**: When you push ¬ through the parentheses:
> - ∧ FLIPS to ∨ (AND becomes OR)
> - ∨ FLIPS to ∧ (OR becomes AND)
> - Each term gets its own ¬

---

## 6. Inference Rules — Discovering New Truths

### 6.1 Modus Ponens (THE Most Important Rule!)

```
Rule:   P → Q       "If it rains, ground is wet"
Fact:   P            "It IS raining"
─────────────
Conclude: Q          "Therefore: ground IS wet"
```

> 🍼 "I know the rule (rain → wet). I know it's raining. So it MUST be wet!"

### 6.2 Modus Tollens

```
Rule:   P → Q       "If it rains, ground is wet"
Fact:   ¬Q           "Ground is NOT wet"
─────────────
Conclude: ¬P         "Therefore: it is NOT raining"
```

> 🍼 "If rain makes the ground wet, and the ground is DRY, then it CAN'T be raining!"

### 6.3 Resolution (The Universal Rule — see next section!)

```
Clause 1:  P ∨ Q      "Either it's raining OR it's cold"
Clause 2:  ¬P ∨ R     "Either it's NOT raining OR roads are slippery"
─────────────
Resolvent:  Q ∨ R     "Either it's cold OR roads are slippery"
```

The P and ¬P CANCEL out, and we combine what's left!

> 🍼 "If one of {rain, cold} is true, and one of {not-rain, slippery} is true, then one of {cold, slippery} must be true! Because if it's raining, the second clause forces slippery. If it's NOT raining, the first clause forces cold."

---

## 7. 🧮 Resolution Proof — Complete Example

### The Problem

**Given:**
1. P → Q  ("If it rains, ground is wet")
2. Q → R  ("If ground is wet, roads are slippery")
3. P      ("It is raining")

**Prove:** R ("Roads are slippery")

### Step 1: Convert Everything to CNF (Clause Form)

CNF = "AND of ORs" — each clause is a disjunction (OR of literals)

```
Formula 1: P → Q  =  ¬P ∨ Q      (using P → Q ≡ ¬P ∨ Q)
Formula 2: Q → R  =  ¬Q ∨ R      (same conversion)
Formula 3: P      =  P            (already a clause)
```

### Step 2: Add the NEGATION of What We Want to Prove

```
We want to prove R. So add ¬R to the knowledge base.
If this leads to a contradiction → R must be TRUE!
```

**Our clauses:**
```
C1: ¬P ∨ Q       (from P → Q)
C2: ¬Q ∨ R       (from Q → R)
C3: P             (given fact)
C4: ¬R            (negation of goal — we ASSUME R is false)
```

### Step 3: Apply Resolution Repeatedly

**Resolve C1 and C3** (they share P and ¬P):
```
C1: ¬P ∨ Q     contains ¬P
C3: P           contains P
     ↓ P and ¬P cancel out
C5: Q           "The ground IS wet" (we derived this!)
```

> 🍼 "C1 says: either NOT-raining or ground-wet. C3 says: it IS raining. So NOT-raining is false, which means ground-wet must be true!"

**Resolve C2 and C5** (they share Q and ¬Q):
```
C2: ¬Q ∨ R      contains ¬Q
C5: Q            contains Q
     ↓ Q and ¬Q cancel out
C6: R            "Roads ARE slippery" (derived!)
```

**Resolve C6 and C4** (they share R and ¬R):
```
C6: R            contains R
C4: ¬R           contains ¬R
     ↓ R and ¬R cancel out
C7: □ (EMPTY CLAUSE!)    ← CONTRADICTION! 🎯
```

### Step 4: Conclusion

We assumed ¬R (roads are NOT slippery) and derived a CONTRADICTION (empty clause). Therefore our assumption was wrong, and R MUST be true!

**Proven: Roads ARE slippery!** ✅

```
Summary of the proof:
  C1: ¬P ∨ Q    (given: rain → wet)
  C3: P          (given: it's raining)
  ──resolve──→ C5: Q (ground is wet)
  
  C2: ¬Q ∨ R    (given: wet → slippery)
  C5: Q          (derived: ground is wet)
  ──resolve──→ C6: R (roads are slippery)
  
  C4: ¬R         (assumed: roads NOT slippery)
  C6: R          (derived: roads ARE slippery)
  ──resolve──→ □ CONTRADICTION! → R is TRUE! 🎯
```

---

## 8. Key Takeaways

1. **Propositions** = statements that are TRUE or FALSE
2. **5 connectives**: ¬(NOT), ∧(AND), ∨(OR), →(IF-THEN), ↔(IFF)
3. **P → Q is ONLY false when P=T and Q=F** (mom's broken promise!)
4. **P → Q ≡ ¬P ∨ Q** — the most important equivalence!
5. **De Morgan's**: ¬(A∧B) = ¬A∨¬B and ¬(A∨B) = ¬A∧¬B
6. **Modus Ponens**: P→Q + P = Q (the bread and butter of reasoning)
7. **Resolution**: P∨Q + ¬P∨R = Q∨R (the universal inference rule)
8. **Resolution proofs**: add ¬goal → resolve → reach □ → goal is proven!

---

## 9. Exam Tips

### Must-Know

1. **Build truth tables** for any formula (2, 3 variables)
2. **Convert P → Q to ¬P ∨ Q** (you WILL need this!)
3. **Apply De Morgan's** correctly
4. **Do a resolution proof** from start to finish

### Common Mistakes

❌ Saying P → Q is FALSE when P is FALSE (it's TRUE! Promise not tested!)
❌ Forgetting to negate the goal in resolution proofs
❌ Applying De Morgan's without flipping ∧ to ∨
❌ Confusing ≡ (equivalence/always same) with → (implication/one direction)

---

## 📖 References

- AIMA — Chapter 7

---

[⬅️ Prev: Expectimax](../10_Expectimax_Search/README.md) | [Back to Main](../README.md) | [Next: FOL Syntax & Semantics ➡️](../12_FOL_Syntax_Semantics/README.md)
