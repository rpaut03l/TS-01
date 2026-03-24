# 🗺️ Topic 14 — Planning: Situation Calculus

> **Difficulty**: 🔴 Hard | **Syllabus Section**: Planning
>
> **Slides**: RB-M | **Quiz Relevance**: ⭐⭐⭐⭐

---

## 🍼 The Big Story (ELI5)

### The Robot Butler 🤖

Imagine a robot butler that needs to set a dinner table. It needs to THINK about what to do:
"First pick up the plate, then put it on the table, then pick up the fork..."

**Situation Calculus** is a way to describe the ENTIRE WORLD using logic:

> 🍼 **Kid Version**: Think of a flipbook animation:
> - Each **PAGE** = a **situation** (snapshot of the world at one moment)
> - **FLIPPING** a page = taking an **action** (doing something that changes the world)
> - Things that **CHANGE** between pages = **fluents** (like a ball's position)
> - Things that **DON'T change** = **eternal facts** (like "the sky is blue")

---

## 📚 Table of Contents

1. [The Three Key Concepts](#1-three-concepts)
2. [Blocks World Example](#2-blocks-world)
3. [The Frame Problem (and Its Solution!)](#3-frame-problem)
4. [Successor-State Axioms](#4-successor-state)
5. [Key Takeaways](#5-key-takeaways)
6. [Exam Tips](#6-exam-tips)

---

## 1. The Three Key Concepts

### 1.1 Situations (Snapshots of the World)

A **situation** is a complete description of the world at a point in time.

```
S₀ = the initial situation (starting state)
Result(action, situation) = the new situation after doing the action

Example:
  S₀ = "Block A is on the table, Block B is on the table"
  S₁ = Result(Move(A, Table, B), S₀) = "A is on B, B is on table"
  S₂ = Result(Move(C, Table, A), S₁) = "C is on A, A is on B, B on table"
```

> 🍼 **Kid Version**: S₀ is page 1 of your flipbook. Result(Move, S₀) is page 2. Each new action creates a new page!

### 1.2 Actions (Things You Can Do)

Actions are objects in the logic — they're THINGS, not operators:

```
Move(A, B)        ← Move block A onto block B
Fly(Plane1, London, Paris)
Buy(Milk)
```

### 1.3 Fluents (Things That Change)

**Fluents** are predicates that take a SITUATION as their LAST argument:

```
On(A, B, S₀)           ← "A is on B in situation S₀" → TRUE
On(A, B, S₁)           ← "A is on B in situation S₁" → maybe FALSE (things changed!)
Clear(A, S₀)           ← "Nothing is on A in S₀"
```

**Eternal facts** DON'T have a situation argument:
```
Block(A)                ← "A is a block" → ALWAYS true, never changes
```

---

## 2. Blocks World Example

### The Classic AI Planning Domain

```
Initial State S₀:           Goal State:
   C                            A
   |                            |
   A    B                       B
   |    |                       |
 Table Table                    C
                                |
                              Table
```

### Describing S₀ in Situation Calculus

```
On(C, A, S₀)          ← C is on A
On(A, Table, S₀)      ← A is on the table
On(B, Table, S₀)      ← B is on the table
Clear(C, S₀)          ← Nothing is on C (C is the top block)
Clear(B, S₀)          ← Nothing is on B
Block(A)               ← A is a block (eternal — no situation needed!)
Block(B)               ← B is a block
Block(C)               ← C is a block
```

### Action Preconditions

"When CAN you move a block?"

```
Poss(Move(x, y), s) ↔ 
    Block(x) ∧ Clear(x, s) ∧ Clear(y, s) ∧ x ≠ y

"You can move x onto y IF:
  - x is a block (not the table!)
  - nothing is on top of x
  - nothing is on top of y (there's room)
  - x and y are different blocks"
```

### 🧮 Applying an Action — Full Trace

**Action**: Move(C, Table) — Move C from A to the Table

**Check preconditions**: Poss(Move(C, Table), S₀)?
```
Block(C)? YES ✅
Clear(C, S₀)? YES (nothing on C) ✅
Clear(Table, S₀)? YES (table always has room) ✅
C ≠ Table? YES ✅
All met! → Action is POSSIBLE!
```

**New situation**: S₁ = Result(Move(C, Table), S₀)

**What CHANGED:**
```
NEW:     On(C, Table, S₁) = TRUE    ← C is now on the table
REMOVED: On(C, A, S₁) = FALSE       ← C is no longer on A
NEW:     Clear(A, S₁) = TRUE        ← A is now clear (C moved off)
```

**What STAYED THE SAME:**
```
On(A, Table, S₁) = TRUE   ← A didn't move!
On(B, Table, S₁) = TRUE   ← B didn't move!
Clear(B, S₁) = TRUE       ← B is still clear!
Block(A) = TRUE            ← Still a block (eternal)
```

---

## 3. The Frame Problem

### The Biggest Problem in AI Planning!

The effect axioms tell us what CHANGES. But what about everything that DOESN'T change?

```
After Move(C, Table):
  ✅ On(C, Table) becomes TRUE     → effect axiom says this
  ✅ ¬On(C, A) becomes TRUE        → effect axiom says this
  
  But WHO says these are still true?
  ❓ On(A, Table) — didn't change, but where's the PROOF?
  ❓ On(B, Table) — didn't change, but where's the PROOF?
  ❓ Clear(B) — didn't change, but where's the PROOF?
```

**We need FRAME AXIOMS** — statements saying "this thing DIDN'T change":

```
∀x,y,z,s: On(z, w, s) ∧ z ≠ x → On(z, w, Result(Move(x, y), s))
"If z was on w, and we moved something ELSE (x ≠ z), then z is still on w"
```

**The problem**: For n fluents and m actions, we need O(n × m) frame axioms. That's HUGE!

> 🍼 **Kid Version**: If you move ONE block, the robot needs to be told "all other blocks stayed in place." For 100 blocks, that's 99 "nothing changed" statements for EACH move. So tedious!

---

## 4. Successor-State Axioms (The Solution!)

Instead of separate effect + frame axioms, write ONE axiom per fluent:

```
Fluent is TRUE after action ↔ 
  (action MADE it true) OR (it was ALREADY true AND action DIDN'T make it false)
```

### Example: On(x, y) Successor-State Axiom

```
∀a,s: On(x, y, Result(a, s)) ↔
    (a = Move(x, y))                              ← Made TRUE by moving x onto y
    ∨
    (On(x, y, s) ∧ ¬(a = Move(x, z) for some z)) ← Was true AND x wasn't moved away
```

> 🍼 **Kid Version**: "Block x is on block y AFTER an action if EITHER: (1) the action was putting x on y, OR (2) x was already on y and nobody moved x."

### Why This Solves the Frame Problem

One successor-state axiom per fluent handles EVERYTHING:
- When it becomes true (positive effects)
- When it becomes false (negative effects)  
- When it stays the same (persistence/frame)

**No separate frame axioms needed!** 

---

## 5. Key Takeaways

1. **Situations** = snapshots of the world; **Result(a,s)** = next snapshot after action a
2. **Fluents** take a situation argument; **eternal facts** don't
3. **Frame Problem** = how to state what DOESN'T change (requires too many axioms)
4. **Successor-State Axioms** solve frame problem: ONE axiom per fluent covers everything
5. Situation calculus is elegant but computationally expensive → motivates STRIPS (next topic!)

---

## 6. Exam Tips

### Must-Know
1. **Write situation calculus formulas** for blocks world
2. **Explain the frame problem** in 2-3 sentences
3. **Write a successor-state axiom** for a given fluent
4. **Distinguish fluents from eternal facts** (situation argument or not)

### Common Mistakes
❌ Forgetting the situation argument in fluents: `On(A, B)` should be `On(A, B, s)`
❌ Writing frame axioms instead of successor-state axioms
❌ Confusing `Move(A, B)` (an action) with `Result(Move(A,B), s)` (a situation)

---

## 📖 References
- AIMA — Chapter 10, Chapter 8.4.2

---

[⬅️ Prev: FOL Inference](../13_FOL_Inference_Unification/README.md) | [Back to Main](../README.md) | [Next: STRIPS ➡️](../15_Planning_STRIPS_Subgoal/README.md)
