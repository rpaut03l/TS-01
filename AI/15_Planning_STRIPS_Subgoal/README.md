# 📋 Topic 15 — Planning: STRIPS & Sub-goals

> **Difficulty**: 🟡 Medium | **Syllabus Section**: Planning 
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐

---

## 🍼 Explain Like I'm 5 (ELI5)

Situation calculus was like writing a WHOLE BOOK to describe how blocks move. STRIPS says: "Let's use simple CARDS instead!"

Each action gets a **card** with three parts:
- **When can I use this card?** (Preconditions)
- **What NEW things become true?** (Add effects)
- **What OLD things become false?** (Delete effects)

> 🍼 **ELI5**: Imagine you have recipe cards for a robot:
> 
> **Card: "Make Sandwich"**
> - **Need**: Bread on counter, Peanut butter available, Hands are free
> - **Get**: Sandwich exists! 🥪
> - **Lose**: Bread no longer on counter, Peanut butter jar less full
>
> The robot reads cards, checks which ones it CAN use, uses them, and updates its world!

---

## 📚 Table of Contents

1. [What is STRIPS?](#1-what-is-strips)
2. [STRIPS Action Representation](#2-strips-action-representation)
3. [The STRIPS Planning Algorithm](#3-the-strips-algorithm)
4. [Blocks World — The Classic Example](#4-blocks-world)
5. [Sub-goal Planning (Goal Decomposition)](#5-sub-goal-planning)
6. [Problems with Sub-goal Planning](#6-problems)
7. [Key Takeaways](#7-key-takeaways)
8. [Exam Tips](#8-exam-tips)

---

## 1. What is STRIPS?

### Stanford Research Institute Problem Solver

STRIPS (1971) was one of the first AI planners. It simplified planning by representing actions with simple add/delete lists instead of full FOL axioms.

### The STRIPS Representation

A planning problem has:

| Component | Description | Example |
|---|---|---|
| **States** | Sets of ground atomic sentences (facts that are true) | {On(A,Table), On(B,Table), Clear(A), Clear(B)} |
| **Initial State** | The starting set of facts | {On(A,Table), Clear(A), On(B,Table), Clear(B)} |
| **Goal** | A set of facts that must all be true | {On(A,B)} |
| **Actions** | Operators with preconditions and effects | Move(x, y, z): move x from y onto z |

### Closed World Assumption

**If a fact is NOT in the state, it's considered FALSE.**

State = {On(A, Table), Clear(A)}
- On(A, Table) → TRUE ✅
- Clear(A) → TRUE ✅
- On(A, B) → FALSE (not mentioned, so assumed false)
- Clear(B) → FALSE (not mentioned)

---

## 2. STRIPS Action Representation

### Action Schema

Every action (also called an **operator**) has three parts:

```
Action: Move(x, from, to)
─────────────────────────
Preconditions:  On(x, from) ∧ Clear(x) ∧ Clear(to) ∧ Block(x) ∧ (x ≠ to)
Add List:       {On(x, to), Clear(from)}
Delete List:    {On(x, from), Clear(to)}
```

### How Actions Work

**Applying an action to a state:**
```
New_State = (Old_State - Delete_List) ∪ Add_List
```

1. Check: Are ALL preconditions true in the current state?
2. If yes: Remove everything in the Delete List, Add everything in the Add List
3. If no: Action cannot be applied!

### Example

**State**: {On(A, Table), On(B, Table), Clear(A), Clear(B), Block(A), Block(B)}

**Apply**: Move(A, Table, B)

**Check preconditions**:
- On(A, Table) ✅
- Clear(A) ✅
- Clear(B) ✅
- Block(A) ✅
- A ≠ B ✅

**Apply effects**:
- Delete: {On(A, Table), Clear(B)}
- Add: {On(A, B), Clear(Table)}

**New State**: {On(A, B), On(B, Table), Clear(A), Clear(Table), Block(A), Block(B)}

```
Before:          After:
  A    B           A
  |    |           |
Table Table        B
                   |
                 Table
```

### Another Common Action: MoveToTable

```
Action: MoveToTable(x, from)
─────────────────────────────
Preconditions:  On(x, from) ∧ Clear(x) ∧ Block(x) ∧ Block(from)
Add List:       {On(x, Table), Clear(from)}
Delete List:    {On(x, from)}
```

---

## 3. The STRIPS Algorithm

### Forward Search (Progression)

Start from the initial state, try actions, see if you reach the goal:

```
function FORWARD_STRIPS(initial, goal, actions):
    state = initial
    plan = []
    
    while not goal ⊆ state:            ← Check if all goal facts are true
        action = choose an applicable action    ← Preconditions met in state
        state = apply(action, state)    ← Update state
        plan.append(action)
    
    return plan
```

### Backward Search (Regression)

Start from the goal, work backwards to find what initial state is needed:

```
function BACKWARD_STRIPS(initial, goal, actions):
    current_goal = goal
    plan = []
    
    while not current_goal ⊆ initial:
        action = choose an action that achieves some goal fact
        current_goal = regress(current_goal, action)
        plan.prepend(action)
    
    return plan
```

**Regression**: Given a goal G and action A that achieves part of G:
```
regressed_goal = (G - Add(A)) ∪ Preconditions(A)
"Replace the achieved goals with the action's preconditions"
```

---

## 4. Blocks World

### The Classic Planning Domain

**Objects**: Blocks (A, B, C, ...) and a Table
**Predicates**: On(x, y), Clear(x), Block(x), OnTable(x)

### Example Problem

```
Initial State:          Goal State:
   C                       A
   |                       |
   A    B                  B
   |    |                  |
  Table Table              C
                           |
                          Table

Initial: {On(C,A), On(A,Table), On(B,Table), Clear(C), Clear(B)}
Goal:    {On(A,B), On(B,C)}
```

### Plan

```
Step 1: Move(C, A, Table)     ← Unstack C from A
  State: {On(A,Table), On(B,Table), On(C,Table), Clear(A), Clear(B), Clear(C)}

Step 2: Move(B, Table, C)     ← Put B on C
  State: {On(A,Table), On(B,C), On(C,Table), Clear(A), Clear(B)}
  Wait — Clear(B) should be removed... Let me recheck.
  
  Actually: {On(A,Table), On(B,C), On(C,Table), Clear(A), Clear(B)}
  Delete Clear(C), add Clear(Table)
  State: {On(A,Table), On(B,C), On(C,Table), Clear(A), Clear(B)}
  
Step 3: Move(A, Table, B)     ← Put A on B
  State: {On(A,B), On(B,C), On(C,Table), Clear(A)}

Goal achieved: On(A,B) ✅ On(B,C) ✅ 🎯
```

**Plan**: [Move(C,A,Table), Move(B,Table,C), Move(A,Table,B)]

---

## 5. Sub-goal Planning

### The Idea

Break a complex goal into **independent sub-goals** and solve each separately!

```
Goal: On(A,B) ∧ On(B,C)

Sub-goal 1: On(A,B)    ← Solve this first
Sub-goal 2: On(B,C)    ← Then solve this

Combine the two plans!
```

> 🍼 **ELI5**: Want to build a LEGO castle with towers AND walls? Build the towers first, then build the walls, then put them together! Each part is a sub-goal.

### Means-Ends Analysis

A classic sub-goal planning strategy:
1. Look at the DIFFERENCE between current state and goal
2. Find an action that REDUCES this difference
3. If the action's preconditions aren't met, make achieving them a sub-goal
4. Recurse!

```
function MEANS_ENDS(state, goal, actions):
    diff = goal - state                    ← What's different?
    if diff is empty: return []            ← Goal achieved!
    
    pick a fact f from diff
    pick an action a that adds f           ← Find action to achieve f
    
    ← First, achieve a's preconditions (sub-goal!)
    pre_plan = MEANS_ENDS(state, preconditions(a), actions)
    
    ← Apply the plan so far to get intermediate state
    mid_state = apply_plan(pre_plan, state)
    
    ← Apply action a
    new_state = apply(a, mid_state)
    
    ← Solve remaining goals
    rest_plan = MEANS_ENDS(new_state, goal, actions)
    
    return pre_plan + [a] + rest_plan
```

---

## 6. Problems with Sub-goal Planning

### The Sussman Anomaly

**The classic example of why sub-goal planning fails!**

```
Initial:        Goal:
   C               A
   |               |
   A    B          B
   |    |          |
 Table Table       C
                   |
                 Table
```

**Goal**: On(A,B) ∧ On(B,C)

**Problem with solving sub-goals independently**:

Approach 1: Solve On(A,B) first, then On(B,C)
- Achieve On(A,B): Move C off A, then move A onto B → {On(A,B), On(C,Table), On(B,Table)}
- Now achieve On(B,C): But B has A on top! Need to undo On(A,B) first! 💀

Approach 2: Solve On(B,C) first, then On(A,B)
- Achieve On(B,C): Move B onto C → {On(B,C), On(C,A), ...}
- Wait, C is on A. Need to move C first. Move C to table, then B onto C.
- Now achieve On(A,B): But A has nothing on it... but B now has nothing on top? Actually we need to check...

The point: **The sub-goals are NOT independent!** Solving one can UNDO the other. This is called the **Sussman Anomaly**.

### Solutions

1. **Interleave sub-goals**: Don't fully solve one before starting another
2. **Partial Order Planning** (next topic!): Don't commit to a specific ordering
3. **Use a complete search**: Forward or backward search through the full space

---

## 7. Key Takeaways

1. **STRIPS** simplifies planning with Add/Delete lists instead of full FOL
2. **Closed World Assumption**: What's not stated is false
3. **State update**: New = (Old - Delete) ∪ Add
4. **Forward search** (progression) and **Backward search** (regression) are both possible
5. **Sub-goal planning** decomposes goals but can fail when sub-goals **interact** (Sussman Anomaly)
6. **Means-Ends Analysis** = find difference → find action to reduce it → achieve its preconditions recursively
7. The Sussman Anomaly shows that **goal ordering matters** and interleaving may be necessary

---

## 8. Exam Tips

### Must-Know

1. **Write STRIPS operators** (preconditions, add list, delete list) for a given domain
2. **Trace plan execution** step by step, showing state after each action
3. **Explain the Sussman Anomaly** — why sub-goal independence fails
4. **Perform regression** — given a goal, regress through an action
5. **Compare STRIPS with situation calculus** — advantages and limitations

### Common Mistakes

❌ Forgetting to delete facts in the delete list when applying an action
❌ Not checking ALL preconditions before applying an action
❌ Assuming sub-goals can always be solved independently
❌ Confusing the Add list with the Precondition list

---

## 📖 References

- AIMA — Chapter 10 (Classical Planning), Chapter 11 (Planning and Acting)

---

[⬅️ Prev: Situation Calculus](../14_Planning_Situation_Calculus/README.md) | [Back to Main](../README.md) | [Next: Partial Order Planning ➡️](../16_Planning_Partial_Order/README.md)
