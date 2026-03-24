# 🔀 Topic 16 — Partial Order Planning (POP)

> **Difficulty**: 🔴 Hard | **Syllabus Section**: Planning
>
> **Slides**: RB-M | **Quiz Relevance**: ⭐⭐⭐

---

## 🍼 The Big Story (ELI5)

### The Sandwich & Juice Problem 🥪🧃

Making a PB&J (Peanut Butter & Jelly) sandwich:
- You MUST spread peanut butter BEFORE closing the sandwich
- You MUST spread jelly BEFORE closing the sandwich
- But you can spread PB first OR jelly first — **doesn't matter!**

**Total Order Planning** would commit: "PB first, then jelly, then close."
**Partial Order Planning** keeps it flexible: "PB before close. Jelly before close. PB and jelly can happen in any order!"

> 🍼 **Kid Version**: Your mom says "brush your teeth AND put on shoes before leaving." She doesn't care which you do FIRST — teeth or shoes. But BOTH must happen before leaving. POP keeps this flexibility!

---

## 📚 Table of Contents

1. [Total Order vs Partial Order](#1-total-vs-partial)
2. [POP Components](#2-components)
3. [Threats and How to Fix Them](#3-threats)
4. [🧮 Worked Example](#4-example)
5. [Why POP Beats Total Order (Sussman Anomaly!)](#5-sussman)
6. [Key Takeaways](#6-key-takeaways)
7. [Exam Tips](#7-exam-tips)

---

## 1. Total Order vs Partial Order

```
Total Order:    A₁ → A₂ → A₃ → A₄     (ONE fixed sequence)

Partial Order:       → A₂ →
                A₁ →           → A₄    (A₂ and A₃ can be in ANY order!)
                     → A₃ →

Valid sequences: A₁→A₂→A₃→A₄  OR  A₁→A₃→A₂→A₄  (both work!)
```

### Why Keep It Flexible?

| Advantage | Explanation |
|---|---|
| **Least commitment** | Don't order things unless you HAVE to |
| **Avoids Sussman Anomaly** | Doesn't force sub-goal ordering that causes undoing work |
| **Parallelism** | Unordered steps could run simultaneously |
| **Flexibility** | Multiple valid execution orders |

---

## 2. POP Components

A partial-order plan has four parts:

| Component | What It Is | Example |
|---|---|---|
| **Actions** | Steps in the plan (including Start and Finish) | {Start, Move(A,B), Move(C,Table), Finish} |
| **Ordering Constraints** | "A must come before B" (A ≺ B) | Move(C,Table) ≺ Move(A,B) |
| **Causal Links** | "Action A provides fact p to Action B" (A →p→ B) | Move(A,B) →On(A,B)→ Finish |
| **Open Preconditions** | Goals not yet achieved | {On(B,C) — still needs an action to achieve this} |

### Special Actions

```
START action:
  Preconditions: NONE
  Effects: ALL facts true in the initial state

FINISH action:
  Preconditions: ALL goal conditions
  Effects: NONE
```

Every plan starts with just: `Start ≺ Finish` and the goals as open preconditions of Finish.

---

## 3. Threats and How to Fix Them

### What is a Threat?

A **threat** happens when an action might DESTROY a fact that another action needs!

```
Causal link: A₁ ──(provides "block clear")──→ A₂
                        ↑
                   A₃ might delete "block clear"! 💥 THREAT!
```

> 🍼 **Kid Version**: You made a sandwich (A₁ provides "sandwich exists" to A₂ "eat sandwich"). But your dog (A₃) might eat the sandwich between A₁ and A₂! The dog is a THREAT!

### Two Ways to Fix Threats

**1. Promotion** — Force the threat BEFORE the causal link:
```
A₃ ≺ A₁ ──(p)──→ A₂
"The dog eats BEFORE you make the sandwich. Then you make a new one!"
```

**2. Demotion** — Force the threat AFTER the causal link:
```
A₁ ──(p)──→ A₂ ≺ A₃
"You eat the sandwich BEFORE the dog gets to it!"
```

```
Original threat:        Promotion fix:           Demotion fix:
A₁ ──(p)──→ A₂         A₃ → A₁ ──(p)──→ A₂    A₁ ──(p)──→ A₂ → A₃
      ↑ A₃              (threat before link)     (threat after link)
```

---

## 4. 🧮 Worked Example

### Problem: Buying Groceries

```
Initial state: At(Home), ¬Have(Milk), ¬Have(Bread)
Goal:          Have(Milk) ∧ Have(Bread)
Actions:
  Go(Store): Pre: At(Home), Add: At(Store), Del: At(Home)
  Buy(Milk): Pre: At(Store), Add: Have(Milk)
  Buy(Bread): Pre: At(Store), Add: Have(Bread)
```

**Step 1**: Start with {Start, Finish}
- Open preconditions of Finish: Have(Milk), Have(Bread)

**Step 2**: Achieve Have(Milk) → add Buy(Milk)
- Causal link: Buy(Milk) →Have(Milk)→ Finish
- Buy(Milk) has precondition: At(Store) → new open precondition!

**Step 3**: Achieve Have(Bread) → add Buy(Bread)
- Causal link: Buy(Bread) →Have(Bread)→ Finish
- Buy(Bread) has precondition: At(Store) → open!

**Step 4**: Achieve At(Store) for Buy(Milk) → add Go(Store)
- Causal link: Go(Store) →At(Store)→ Buy(Milk)

**Step 5**: Achieve At(Store) for Buy(Bread) → reuse Go(Store)!
- Causal link: Go(Store) →At(Store)→ Buy(Bread)

**Step 6**: Achieve At(Home) for Go(Store) → Start provides At(Home)!
- Causal link: Start →At(Home)→ Go(Store)

**Ordering constraints**: Start ≺ Go(Store) ≺ Buy(Milk) ≺ Finish, Go(Store) ≺ Buy(Bread) ≺ Finish

**Note**: Buy(Milk) and Buy(Bread) have **NO ordering between them!** You can buy milk first or bread first — doesn't matter!

```
Final plan:
  Start → Go(Store) → Buy(Milk)  → Finish
                    → Buy(Bread) → Finish
  
  Buy(Milk) and Buy(Bread) are UNORDERED (partial order!)
```

---

## 5. Why POP Beats Total Order (Sussman Anomaly!)

### The Classic Problem

```
Initial:        Goal:
   C               A
   |               |
   A    B          B
   |    |          |
 Table Table       C → Table
```

**Goal**: On(A,B) ∧ On(B,C)

**Total order approach FAILS:**
- Solve On(A,B) first → move C off A, then put A on B
- Now solve On(B,C) → but B has A on top! Must undo On(A,B)! 💀

**POP doesn't commit** to solving one sub-goal completely before the other. It interleaves steps naturally:
1. Move C to table (clearing A)
2. Move B onto C
3. Move A onto B

POP finds this because it adds steps as needed without forcing a sub-goal order!

---

## 6. Key Takeaways

1. **POP** delays ordering decisions — least commitment strategy
2. **Causal links** record WHY actions are in the plan
3. **Threats** = actions that might destroy needed facts
4. **Promotion** (threater before link) and **Demotion** (threater after link) fix threats
5. **POP avoids the Sussman Anomaly** by not forcing sub-goal ordering
6. **Start/Finish** are dummy actions for initial state and goals

---

## 7. Exam Tips

### Must-Know
1. **Draw a partial order plan** showing actions, orderings, and causal links
2. **Identify threats** and resolve via promotion or demotion
3. **Explain the Sussman Anomaly** and how POP avoids it

### Common Mistakes
❌ Forgetting Start and Finish dummy actions
❌ Adding unnecessary ordering (defeats POP's purpose!)
❌ Confusing promotion with demotion

---

## 📖 References
- AIMA — Chapter 10.4

---

[⬅️ Prev: STRIPS](../15_Planning_STRIPS_Subgoal/README.md) | [Back to Main](../README.md) | [Next: Bayesian Networks ➡️](../17_Bayesian_Network/README.md)
