# 🧩 Topic 06 — Constraint Satisfaction Problems: Backtracking Search

> **Difficulty**: 🟡 Medium | **Syllabus Section**: CSP | Backtracking, Arc Consistency, Forward Checking
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐⭐

---

## 🍼 Explain Like I'm 5 (ELI5)

Imagine you're coloring a map and your teacher says: "No two countries that share a border can have the SAME color!" You have red, green, and blue crayons.

You start with Australia:
- Color Western Australia **red**... okay!
- Now Northern Territory — it touches WA, so it can't be red. Try **green**... okay!
- Queensland touches NT, so not green. Try **red**... okay!
- New South Wales touches QLD, so not red. Try **green**... okay!
- Victoria touches NSW, so not green. Try **red**... okay!
- South Australia touches WA (red), NT (green), QLD (red), NSW (green), VIC (red)... 😱 It needs to be not-red AND not-green... Try **blue!** ✅

That's a **Constraint Satisfaction Problem** (CSP) — you have variables (countries), domains (colors), and constraints (neighbors can't match)!

---

## 📚 Table of Contents

1. [What is a CSP?](#1-what-is-a-csp)
2. [CSP Formulation](#2-csp-formulation)
3. [Famous CSP Examples](#3-famous-csp-examples)
4. [Backtracking Search](#4-backtracking-search)
5. [Improving Backtracking — Filtering](#5-improving-backtracking--filtering)
6. [Improving Backtracking — Ordering](#6-improving-backtracking--ordering)
7. [Improving Backtracking — Structure](#7-improving-backtracking--structure)
8. [Key Takeaways](#8-key-takeaways)
9. [Exam Tips](#9-exam-tips)

---

## 1. What is a CSP?

### Definition

A **Constraint Satisfaction Problem** consists of:

| Component | Symbol | Meaning |
|---|---|---|
| **Variables** | X = {X₁, X₂, ..., Xₙ} | Things we need to assign values to |
| **Domains** | D = {D₁, D₂, ..., Dₙ} | Possible values for each variable |
| **Constraints** | C = {C₁, C₂, ...} | Rules that limit which value combinations are allowed |

**Solution**: An assignment of values to ALL variables that satisfies ALL constraints.

### CSP vs Regular Search

| Feature | Regular Search | CSP |
|---|---|---|
| **State** | A black box | Structured (variable assignments) |
| **Goal Test** | Application-specific | Constraint checking (generic!) |
| **Heuristics** | Domain-specific | General-purpose (MRV, LCV, etc.) |
| **Key advantage** | Flexible | Can eliminate large portions of search space! |

> 💡 **Why CSPs are powerful**: Because the state has structure (variables + constraints), we can use smart techniques to prune massive parts of the search tree!

---

## 2. CSP Formulation

### Types of Variables

| Type | Domain | Example |
|---|---|---|
| **Discrete, Finite** | {red, green, blue} | Map coloring |
| **Discrete, Infinite** | Integers, Strings | Job scheduling (start times) |
| **Continuous** | Real numbers | Linear programming |

### Types of Constraints

| Type | Involves | Example |
|---|---|---|
| **Unary** | 1 variable | "SA ≠ green" (SA can't be green) |
| **Binary** | 2 variables | "SA ≠ WA" (SA and WA different colors) |
| **Higher-order** | 3+ variables | "A + B + C < 10" |
| **Global** | All variables | "all-different" (every variable unique) |
| **Preference/Soft** | Any | "Prefer morning classes" (desirable but not required) |

### Constraint Graph

Variables are nodes. An edge connects two variables that share a constraint.

```
Map of Australia:

    WA ──── NT ──── QLD
     \      |  \   / |
      \     |   \ /  |
       SA ──+────+───+
        |       |
       VIC ── NSW
         \   /
          TAS
```

---

## 3. Famous CSP Examples

### 3.1 Map Coloring

**Variables**: WA, NT, QLD, NSW, VIC, SA, TAS
**Domains**: {Red, Green, Blue} for each
**Constraints**: Adjacent regions must have different colors

### 3.2 N-Queens

**Variables**: Q₁, Q₂, ..., Qₙ (one per column)
**Domain**: {1, 2, ..., n} (row number)
**Constraints**:
- No two queens in same row: Qᵢ ≠ Qⱼ
- No two queens on same diagonal: |Qᵢ - Qⱼ| ≠ |i - j|

### 3.3 Cryptarithmetic

```
    T W O
  + T W O
  ─────────
  F O U R
```

**Variables**: T, W, O, F, U, R (and carry variables)
**Domains**: {0, 1, 2, ..., 9}
**Constraints**: The math must work + all letters represent different digits + F ≠ 0, T ≠ 0

### 3.4 Sudoku

**Variables**: Each empty cell
**Domains**: {1, 2, ..., 9}
**Constraints**: Each row, column, and 3×3 box has all different values

---

## 4. Backtracking Search

### The Core Idea

Backtracking = DFS + two key improvements for CSPs:

1. **Assign ONE variable at a time** (not random actions)
2. **Check constraints IMMEDIATELY** after each assignment (detect failure early)

> 🍼 **ELI5**: Color one country at a time. After each coloring, check — "Did I break any rule?" If yes, immediately try a different color. If all colors fail, go back and change the PREVIOUS country's color. Don't waste time coloring all countries before checking!

### Pseudocode

```
function BACKTRACKING_SEARCH(csp):
    return BACKTRACK({}, csp)          ← Start with empty assignment

function BACKTRACK(assignment, csp):
    if assignment is complete: return assignment    ← 🎯 All variables assigned!
    
    var = SELECT_UNASSIGNED_VARIABLE(csp)           ← Pick next variable
    for each value in ORDER_DOMAIN_VALUES(var, csp): ← Try each value
        if value is consistent with assignment:      ← Check constraints
            assignment[var] = value                  ← Assign
            result = BACKTRACK(assignment, csp)       ← Recurse
            if result != FAILURE: return result       ← Propagate success
            assignment.remove(var)                    ← Undo (backtrack!)
    
    return FAILURE                                    ← All values failed
```

### Step-by-Step: Map Coloring

```
Variables: WA, NT, QLD, NSW, VIC, SA, TAS
Domain: {R, G, B}

Step 1: Assign WA = R ✅
Step 2: Assign NT = ? 
        Try R → NT adj WA(R) → CONFLICT ❌
        Try G → OK ✅ NT = G
Step 3: Assign QLD = ?
        Try R → OK (adj to NT=G only so far) ✅ QLD = R
Step 4: Assign NSW = ?
        Try R → adj QLD(R) → CONFLICT ❌
        Try G → OK ✅ NSW = G
Step 5: Assign VIC = ?
        Try R → OK ✅ VIC = R
Step 6: Assign SA = ?
        Try R → adj WA(R) → CONFLICT ❌
        Try G → adj NT(G) → CONFLICT ❌
        Try B → adj WA(R)✅ NT(G)✅ QLD(R)✅ NSW(G)✅ VIC(R)✅ → ALL OK ✅ SA = B
Step 7: Assign TAS = ?
        Try R → OK ✅ TAS = R

SOLUTION: WA=R, NT=G, QLD=R, NSW=G, VIC=R, SA=B, TAS=R 🎯
```

---

## 5. Improving Backtracking — Filtering

### 5.1 Forward Checking

**After assigning a value to a variable, remove inconsistent values from NEIGHBORING variables' domains.**

> 🍼 **ELI5**: After coloring WA red, cross out "red" from the crayon box for all countries touching WA. This way, when you get to those countries, you already know red isn't an option!

**Example:**

```
After WA = R:
  NT domain: {R, G, B} → {G, B}        (remove R, since adj to WA)
  SA domain: {R, G, B} → {G, B}        (remove R, since adj to WA)

After NT = G:
  QLD domain: {R, G, B} → {R, B}       (remove G, since adj to NT)
  SA domain: {G, B} → {B}              (remove G, since adj to NT)
  
After QLD = R:
  NSW domain: {R, G, B} → {G, B}       (remove R)
  SA domain: {B} → {B}                 (already only B)
```

**When does FC detect failure?** When any variable's domain becomes **EMPTY**! This means no solution exists down this path → backtrack immediately.

### 5.2 Arc Consistency (AC-3)

Forward checking only looks ONE step ahead. **Arc consistency** goes further — it ensures EVERY pair of connected variables is consistent.

**An arc (Xᵢ, Xⱼ) is consistent if:** For EVERY value in Xᵢ's domain, there exists at LEAST ONE value in Xⱼ's domain that satisfies the constraint between them.

> 🍼 **ELI5**: For every color I might use for Country A, there must be at least one legal color left for Country B. If not, remove that color from A!

### AC-3 Algorithm

```
function AC3(csp):
    queue = all arcs (Xᵢ, Xⱼ) in csp
    
    while queue is not empty:
        (Xᵢ, Xⱼ) = queue.remove()
        if REVISE(csp, Xᵢ, Xⱼ):           ← Xᵢ's domain was reduced!
            if Xᵢ's domain is empty: return FAILURE
            for each Xₖ that is neighbor of Xᵢ (except Xⱼ):
                queue.add(Xₖ, Xᵢ)           ← Re-check Xₖ against Xᵢ
    return TRUE

function REVISE(csp, Xᵢ, Xⱼ):
    revised = false
    for each value x in Xᵢ's domain:
        if NO value y in Xⱼ's domain satisfies constraint(Xᵢ=x, Xⱼ=y):
            remove x from Xᵢ's domain
            revised = true
    return revised
```

### AC-3 Complexity

- **Time**: O(e × d³) where e = number of arcs (edges), d = max domain size
- Why d³? Each arc can be re-added to the queue d times (domain can shrink d times), and checking an arc takes O(d²)

### 🧮 AC-3 FULL TRACE EXAMPLE (Exam-Style!)

This is the kind of problem you WILL see on exams. Let's trace AC-3 completely.

**Problem**: Map coloring with 3 variables, 3 colors

```
Variables: A, B, C
Domains:   A: {R, G}, B: {R, G, B}, C: {R, G}
Constraints: A ≠ B, B ≠ C (A-B adjacent, B-C adjacent, A-C NOT adjacent)

Graph:  A ─── B ─── C    (A and C are NOT connected)
```

**Step 1: Initialize the arc queue**

For each edge, add BOTH directions:
```
Queue = [(A,B), (B,A), (B,C), (C,B)]
```

**Step 2: Process arc (A, B)**

```
REVISE(A, B):
  For each value in A's domain:
    A = R: Is there any value in B's domain where A ≠ B?
           B = R → R ≠ R? NO ❌
           B = G → R ≠ G? YES ✅ → R is supported! Keep R in A's domain.
    A = G: Is there any value in B's domain where A ≠ B?
           B = R → G ≠ R? YES ✅ → G is supported!
  
  Result: A's domain unchanged {R, G}. REVISE returns false.
  No neighbors to re-add.
  
Queue = [(B,A), (B,C), (C,B)]
```

**Step 3: Process arc (B, A)**

```
REVISE(B, A):
  B = R: A can be G (R ≠ G ✅) → Keep R
  B = G: A can be R (G ≠ R ✅) → Keep G
  B = B: A can be R (B ≠ R ✅) → Keep B
  
  Result: B's domain unchanged {R, G, B}. REVISE returns false.

Queue = [(B,C), (C,B)]
```

**Step 4: Process arc (B, C)**

```
REVISE(B, C):
  B = R: C can be G (R ≠ G ✅) → Keep R
  B = G: C can be R (G ≠ R ✅) → Keep G  
  B = B: C can be R (B ≠ R ✅) → Keep B

  Result: B's domain unchanged {R, G, B}. REVISE returns false.

Queue = [(C,B)]
```

**Step 5: Process arc (C, B)**

```
REVISE(C, B):
  C = R: B can be G (R ≠ G ✅) → Keep R
  C = G: B can be R (G ≠ R ✅) → Keep G

  Result: C's domain unchanged {R, G}. REVISE returns false.

Queue = [] ← EMPTY! We're done!
```

**Final domains**: A: {R, G}, B: {R, G, B}, C: {R, G} — no changes were needed!

---

**Now let's try a case where AC-3 DOES prune values:**

```
Variables: X, Y
Domains:   X: {1, 2, 3}, Y: {1, 2, 3}
Constraint: X > Y
```

```
Queue = [(X,Y), (Y,X)]

Process (X, Y):
  REVISE(X, Y):
    X = 1: Is there ANY y where 1 > y? y=1: 1>1? NO. y=2: 1>2? NO. y=3: 1>3? NO.
           NO support found! → REMOVE 1 from X's domain! ❌
    X = 2: y=1: 2>1? YES ✅ → Keep 2
    X = 3: y=1: 3>1? YES ✅ → Keep 3
  
  X's domain: {1, 2, 3} → {2, 3}  ← CHANGED! REVISE returns true!
  X's domain is not empty, so add neighbors of X (except Y) to queue.
  (X has no other neighbors, so nothing to add)

Queue = [(Y,X)]

Process (Y, X):
  REVISE(Y, X):
    Y = 1: X can be 2 (2 > 1 ✅) → Keep 1
    Y = 2: X can be 3 (3 > 2 ✅) → Keep 2
    Y = 3: Is there ANY x in {2,3} where x > 3? x=2: 2>3? NO. x=3: 3>3? NO.
           NO support! → REMOVE 3 from Y's domain! ❌

  Y's domain: {1, 2, 3} → {1, 2}  ← CHANGED! REVISE returns true!
  Add neighbors of Y (except X) → none.

Queue = [] ← DONE!

Final domains: X: {2, 3}, Y: {1, 2}
```

**AC-3 figured out that X can't be 1 (nothing smaller) and Y can't be 3 (nothing larger)!** These deductions would save us from trying X=1 or Y=3 during backtracking search.

> 🍼 **Kid Version of the X > Y trace**: 
> "Can X be 1? Well, X has to be BIGGER than Y. And Y can be 1, 2, or 3. Is 1 bigger than any of those? NO! So X definitely can't be 1. Cross it off!"
> "Can Y be 3? Well, X has to be BIGGER than Y. And X can now be 2 or 3. Is 2 bigger than 3? NO. Is 3 bigger than 3? NO. So Y definitely can't be 3. Cross it off!"

### Forward Checking vs Arc Consistency

| Feature | Forward Checking | Arc Consistency (AC-3) |
|---|---|---|
| **Looks ahead** | 1 step (just neighbors) | Multiple steps (transitive) |
| **When to run** | After each assignment | After each assignment (as preprocessing or maintained) |
| **Detects failure** | When a domain becomes empty | When a domain becomes empty |
| **Cost** | Cheap | More expensive but catches more failures early |
| **MAC** | — | **Maintaining AC** = run AC-3 after every assignment in backtracking |

---

## 6. Improving Backtracking — Ordering

### 6.1 Variable Ordering: MRV (Minimum Remaining Values)

**Choose the variable with the FEWEST legal values remaining!**

Also called the "fail-first" heuristic — if a variable is going to cause a failure, let's find out NOW rather than later!

> 🍼 **ELI5**: If one country only has 1 legal color left, color IT first! If you wait and that color gets taken by a neighbor, you'll have to backtrack all the way back. Better to handle the most constrained country ASAP!

**Example:**
```
Current domains:
  WA: {R, G, B}     ← 3 values
  NT: {G, B}         ← 2 values
  SA: {B}            ← 1 value ← 🚨 PICK THIS ONE! (MRV)
  QLD: {R, B}        ← 2 values
```

Pick SA first because it has only 1 remaining value → must be B.

### 6.2 Variable Ordering: Degree Heuristic

**Among tied MRV variables, pick the one involved in the MOST constraints with unassigned variables.**

> 🍼 **ELI5**: If two countries both have 2 colors left, pick the one that touches the MOST uncolored countries. Resolving it first will simplify the most neighbors!

### 6.3 Value Ordering: LCV (Least Constraining Value)

**When choosing a value for a variable, pick the value that rules out the FEWEST choices for neighboring variables.**

> 🍼 **ELI5**: When coloring a country, pick the color that leaves the MOST options for neighboring countries. Don't be greedy — be generous to your neighbors!

**Example:**
```
Assigning NSW. Options: {G, B}

If NSW = G:
  SA has {B} left        ← 1 option
  VIC has {R, B} left    ← 2 options
  Total remaining options for neighbors = 3

If NSW = B:
  SA has {G} left        ← 1 option  
  VIC has {R, G} left    ← 2 options
  Total remaining options for neighbors = 3

Tie! Pick either. (In practice, one might be better.)
```

### MRV vs LCV — Opposite Philosophies!

| Heuristic | Applied to | Philosophy |
|---|---|---|
| **MRV** | Variable selection | **Fail-first**: Pick the MOST constrained variable → detect failures early |
| **LCV** | Value selection | **Succeed-first**: Pick the LEAST constraining value → maximize chance of success |

---

## 7. Improving Backtracking — Structure

### 7.1 Independent Sub-problems

If the constraint graph has **disconnected components**, solve each independently!

If a CSP has n variables and can be broken into sub-problems of size c:
- **Without decomposition**: O(d^n)
- **With decomposition**: O(n/c × d^c) — **exponentially better!**

### 7.2 Tree-Structured CSPs

If the constraint graph is a **tree** (no cycles), the CSP can be solved in **O(n × d²)** time! (Linear in n, not exponential!)

**Algorithm for Tree CSPs:**
1. Choose any variable as root
2. Order variables from root to leaves (topological sort)
3. **Backward pass**: For each variable (leaf to root), make arc-consistent with parent
4. **Forward pass**: For each variable (root to leaves), assign any consistent value

### 7.3 Cutset Conditioning

For nearly tree-like constraint graphs (graphs with few cycles):
1. Find a small set of variables (the **cutset**) whose removal makes the graph a tree
2. For each possible assignment of the cutset variables:
   - Remove inconsistent values from remaining variables
   - Solve the resulting tree-structured CSP

If the cutset has c variables: O(d^c × (n-c) × d²)

---

## 8. Key Takeaways

1. **CSP = Variables + Domains + Constraints** — a structured way to formulate search problems
2. **Backtracking** = DFS + constraint checking after each assignment
3. **Forward Checking** = after assigning, remove inconsistent values from neighbors
4. **Arc Consistency (AC-3)** = stronger than FC, enforces pairwise consistency across ALL arcs
5. **MRV** = pick the most constrained variable first (fail-first)
6. **LCV** = pick the least constraining value first (succeed-first)
7. **Tree CSPs** are solvable in polynomial time!
8. **Combining FC/AC + MRV + LCV** makes backtracking extremely efficient in practice

---

## 9. Exam Tips

### Must-Know

1. **Formulate a problem as CSP** → identify variables, domains, constraints
2. **Trace backtracking** step by step on a graph
3. **Apply forward checking** → show domain reductions after each assignment
4. **Run AC-3** → show REVISE operations and domain reductions
5. **Apply MRV and LCV** → justify variable and value ordering
6. **Draw constraint graphs** for given problems

### Common Mistakes

❌ Confusing MRV (variable ordering) with LCV (value ordering)
❌ Forgetting to re-add arcs to the queue in AC-3 after a domain change
❌ Not detecting failure when a domain becomes empty (forward checking)
❌ Thinking backtracking always finds a solution (it returns FAILURE if none exists)
❌ Confusing arc consistency (pairwise) with path consistency (triples)

### Practice Problems

1. Formulate Sudoku as a CSP and show forward checking for first 3 assignments
2. Apply AC-3 to a map coloring problem — trace all REVISE calls
3. Given a constraint graph, find the MRV variable at each step

---

## 📖 References

- AIMA — Chapter 6 (Constraint Satisfaction Problems)

---

[⬅️ Prev: And-Or Search](../05_Search_And_Or/README.md) | [Back to Main](../README.md) | [Next: CSP — Local Search ➡️](../07_CSP_Local_Search/README.md)
