# 🌳 Topic 05 — And-Or Search

> **Difficulty**: 🟡 Medium | **Syllabus Section**: Search
>
> **Slides**: RB-M | **Quiz Relevance**: ⭐⭐⭐

---

## 🍼 The Big Story (ELI5)

### The Umbrella Problem ☂️

Imagine you're planning a trip to the park. In NORMAL search, YOU control everything:
- "I'll walk to the park, then play on swings, then go home."

But what if NATURE makes some decisions?
- "I'll go to the park. But then it might rain OR stay sunny."
- If sunny → play on swings
- If rainy → play in the covered area

**You can't control the weather!** Your plan needs to handle BOTH possibilities!

> 🍼 **Kid Version**: Think of a "Choose Your Own Adventure" book where sometimes YOU choose what happens, and sometimes the BOOK chooses (randomly flips to a page). Your plan must work NO MATTER which pages the book flips to!

**Two types of choices:**
- **OR nodes** = **YOUR choice**: "Should I go left or right?" You pick the best one! 🙋
- **AND nodes** = **WORLD's choice**: "It might rain or shine." Your plan must handle BOTH! 🌍

---

## 📚 Table of Contents

1. [Why Regular Search Isn't Enough](#1-why-and-or)
2. [OR Nodes vs AND Nodes](#2-or-vs-and)
3. [And-Or Tree Example (Detailed!)](#3-example)
4. [The Algorithm](#4-algorithm)
5. [Conditional Plans](#5-conditional-plans)
6. [Cyclic Solutions](#6-cyclic)
7. [Key Takeaways](#7-key-takeaways)
8. [Exam Tips](#8-exam-tips)

---

## 1. Why Regular Search Isn't Enough

### Deterministic vs Nondeterministic

```
DETERMINISTIC (what we've seen so far):
  Action "move right" → ALWAYS goes right
  ONE outcome per action
  Plan = simple sequence: Step1, Step2, Step3

NONDETERMINISTIC (real world!):
  Action "vacuum" → MIGHT clean (80%) or MIGHT spread dirt (20%)
  MULTIPLE possible outcomes per action
  Plan = if-then-else tree: "Vacuum. IF clean, stop. IF dirty, vacuum again."
```

**Real examples:**
| Action | Possible Outcomes | Why nondeterministic? |
|---|---|---|
| Robot picks up cup | Grasped ✅ or Slipped ❌ | Robot gripper isn't perfect |
| Drive to work | Normal route or Detour (road closed) | Road conditions unknown |
| Flip a coin | Heads or Tails | Random! |
| Take medicine | Cured or Side effects | Biology is complex |

---

## 2. OR Nodes vs AND Nodes

### The Two Node Types — With Pictures!

```
OR Node (YOUR choice):           AND Node (WORLD's choice):
"Which action should I take?"    "What outcomes might happen?"

        YOU 🙋                          WORLD 🌍
       / | \                           / | \
      A  B  C                        X  Y  Z
      
You need JUST ONE                You need to handle
path to work.                    ALL outcomes.
"Pick the best!"                 "Plan for everything!"
```

### 🧮 How to Tell Them Apart

**OR node** = Agent's decision point
- Success if ANY child succeeds
- Like choosing a restaurant: any good one works!

**AND node** = Nature's/environment's decision point
- Success if ALL children succeed
- Like packing for unpredictable weather: need to handle sun AND rain!

### Visual Notation in And-Or Trees

```
         ○ OR node (agent chooses)
        /|\
       / | \
      ●  ●  ●  AND node (nature chooses, shown with arc connecting children)
     /\  |  /\
    ○  ○ ○ ○  ○  OR nodes again
```

The **arc** connecting children of an AND node means "ALL of these must be solved."

---

## 3. And-Or Tree Example (Detailed!)

### The Erratic Vacuum Cleaner

**Setup**: Two rooms (Left and Right). Robot vacuum wants BOTH rooms clean.

**Actions**: Suck (vacuum current room), Left (move left), Right (move right)

**The catch**: "Suck" is **erratic** — it MIGHT clean the room, or it MIGHT deposit dirt!

```
State: [Left=Dirty, Right=Dirty], Robot in Left room

                    [L=D, R=D, in Left] ← OR: Robot chooses action
                    /          |          \
               Suck         Left        Right
               (AND)        (move)       (move)
              /      \
    [L=Clean,R=D]  [L=D,R=D]     ← AND: TWO possible outcomes of Suck!
    Robot in Left   Robot in Left    (clean worked OR dirt deposited)
         |              |
        (OR)           (OR)         ← Robot chooses again
         |              |
       Right          Suck again!   ← Keep trying until it works
         |
    [L=Clean,R=D]
    Robot in Right
         |
        (OR)
         |
        Suck
        (AND)
       /      \
 [L=C,R=C]  [L=C,R=D]     ← Two possible outcomes again
 GOAL! 🎯   Try again!
```

### The Conditional Plan (Solution)

The solution is NOT a simple sequence. It's an **if-then-else plan**:

```
Plan:
  1. Suck (vacuum left room)
  2. IF left is now clean:
       a. Move Right
       b. Suck (vacuum right room)
       c. IF right is now clean: DONE! 🎯
       d. ELSE: Go back to step b (suck again)
  3. ELSE (left still dirty):
       a. Go back to step 1 (suck again)
```

> 🍼 **Kid Version**: "Try to clean the left room. Did it work? Great, go clean the right room! Didn't work? Try again! Keep trying until both rooms are clean. You have a plan for EVERY possible outcome!"

---

## 4. The Algorithm

### Pseudocode (Simplified with Explanation)

```
function AND_OR_SEARCH(problem):
    return OR_SEARCH(initial_state, problem, [])
                                              ↑ path = visited states (for cycle detection)

function OR_SEARCH(state, problem, path):
    ── Agent's turn to choose!
    if state is GOAL: return empty plan 🎯
    if state in path: return FAILURE        ← Cycle! We've been here before!
    
    for each action the agent can take:
        plan = AND_SEARCH(possible_outcomes, problem, [state] + path)
        if plan ≠ FAILURE:
            return [action, plan]           ← This action works!
    
    return FAILURE                          ← No action works from here

function AND_SEARCH(outcome_states, problem, path):
    ── Nature's turn! Must handle ALL outcomes!
    plan = {}
    for each possible outcome state:
        sub_plan = OR_SEARCH(outcome_state, problem, path)
        if sub_plan == FAILURE:
            return FAILURE                  ← Can't handle this outcome!
        plan[outcome_state] = sub_plan      ← Store plan for this outcome
    
    return plan                             ← Plans for ALL outcomes!
```

### 🧮 How OR and AND Work Together

```
OR_SEARCH at state S:
  "I need at least ONE action that works"
  Try action A₁ → call AND_SEARCH on outcomes
    AND_SEARCH: "I need ALL outcomes handled"
      Try outcome O₁ → call OR_SEARCH → works? ✅
      Try outcome O₂ → call OR_SEARCH → works? ✅
      ALL outcomes handled → return success to OR_SEARCH ✅
  Action A₁ works! Return it.
```

---

## 5. Conditional Plans

### Simple Plan vs Conditional Plan

```
Simple plan (deterministic world):
  [Move-Right, Move-Up, Pick-Up-Key, Open-Door]
  Just a list. Do step 1, then 2, then 3, then 4.

Conditional plan (nondeterministic world):
  [Suck,
    IF clean: [Right, Suck,
                IF clean: DONE
                IF dirty: Suck again]
    IF dirty: [Suck again,
                IF clean: [Right, Suck, ...]
                IF dirty: Suck yet again...]]
  A TREE of if-then-else branches!
```

> 🍼 **Kid Version**: A simple plan is like a recipe: "Step 1, Step 2, Step 3." A conditional plan is like a recipe with backup options: "Step 1. If it works, Step 2. If it fails, try Step 1 again. If Step 2 works, Step 3. If not..."

---

## 6. Cyclic Solutions

Sometimes the only solution involves **loops**: "Try until it works!"

```
Suck → clean? → DONE!
  ↓ not clean
Suck → clean? → DONE!
  ↓ not clean
Suck → ... (keep trying!)
```

This is a **cyclic plan** — it might loop many times. But if each Suck has SOME chance of working, it will EVENTUALLY succeed (with probability 1).

The basic algorithm detects cycles (with the `path` check) and avoids them. For domains where cycles are the ONLY solution, we need a modified version.

---

## 7. Key Takeaways

1. **And-Or search** handles **nondeterministic** environments (actions with multiple outcomes)
2. **OR nodes** = agent's choice → need ONE child to succeed
3. **AND nodes** = nature's choice → need ALL children to succeed
4. **Solution = conditional plan** (if-then-else tree), not a simple sequence
5. **Cycle detection** prevents infinite loops
6. **The algorithm alternates**: OR_SEARCH (pick action) → AND_SEARCH (handle all outcomes) → OR_SEARCH...

---

## 8. Exam Tips

### Must-Know

1. **Draw an And-Or tree** for a given problem (mark OR and AND nodes!)
2. **Extract the conditional plan** from a solved tree
3. **Identify which nodes are OR** (agent) **vs AND** (nature)
4. **Explain why simple plans fail** for nondeterministic problems

### Common Mistakes

❌ Confusing OR and AND — remember: **OR = you choose, AND = world chooses**
❌ Writing a linear plan for a nondeterministic problem (MUST be conditional!)
❌ Thinking AND means "do all actions" — no! AND means "handle all OUTCOMES of ONE action"
❌ Forgetting cycle detection

---

## 📖 References

- AIMA — Chapter 4.3-4.4

---

[⬅️ Prev: Local & Evolutionary Search](../04_Search_Local_and_Evolutionary/README.md) | [Back to Main](../README.md) | [Next: CSP — Backtracking ➡️](../06_CSP_Backtracking/README.md)
