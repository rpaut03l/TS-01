# 🔢 Dijkstra's Algorithm — Numerical Analysis

> **Subject:** DSA | **Topic:** Shortest Paths | **Algo:** Dijkstra  
> **Repo:** `rpaut03l/TS-01-Pvt` → `DSA/Dijkstra/numericals/`

---

## 🗺️ Navigation

| ← Prev | This File | Next → |
|--------|-----------|--------|
| [📚 Theory](../theory/dijkstra_theory.md) | 🔢 Numericals | [💻 Practice →](../practice/dijkstra_practice.md) |

**Jump Inside This File:**
- [How to Solve Any Dijkstra Problem](#how-to-solve-any-dijkstra-problem)
- [Worked Example 1 — Basic 5-node Graph](#worked-example-1--basic-5-node-graph)
- [Worked Example 2 — Lecture Example (R,S,T,X,Y,Z,W)](#worked-example-2--lecture-example-rstxyzw)
- [Worked Example 3 — Finding Actual Path](#worked-example-3--finding-actual-path)
- [Worked Example 4 — Priority Queue Trace](#worked-example-4--priority-queue-trace)
- [Relaxation Rule Practice](#relaxation-rule-practice)
- [Common Mistakes in Numericals](#common-mistakes-in-numericals)
- [Blank Trace Table Template](#blank-trace-table-template)

---

## How to Solve Any Dijkstra Problem

### 5-Step Recipe 🍳

```
Step 1: DRAW the graph (if not given)
        Label all vertices and edge weights

Step 2: MAKE a table
        Columns: Iteration | Settled vertex | dist[v1] | dist[v2] | ...

Step 3: INITIALISE
        dist[source] = 0
        dist[everyone else] = ∞

Step 4: REPEAT until all settled:
        a. Pick vertex u with minimum dist (unsettled only)
        b. Mark u as settled (underline or circle in table)
        c. For each neighbor v of u:
              candidate = dist[u] + w(u,v)
              if candidate < dist[v]: update dist[v] = candidate

Step 5: READ final row of table → your answer!
```

---

## Worked Example 1 — Basic 5-node Graph

### Graph
```
         4           
  (A) -------> (B)
   |           |  \
  2|           |1   \5
   |           |     \
   v           v      v
  (C) -------> (D)-->(E)
         3          2
```
**Edges and weights:**
```
A→B : 4
A→C : 2
B→D : 1
B→E : 5
C→D : 3
D→E : 2
```
**Source = A**

---

### Step 1: Initialise
```
dist[A]=0, dist[B]=∞, dist[C]=∞, dist[D]=∞, dist[E]=∞
Unsettled: {A, B, C, D, E}
```

---

### Step 2: Full Trace Table

```
┌──────┬───────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Iter │ Settled   │ dist[A]  │ dist[B]  │ dist[C]  │ dist[D]  │ dist[E]  │
├──────┼───────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│  0   │    —      │   *0*    │    ∞     │    ∞     │    ∞     │    ∞     │
│  1   │    A      │    0     │   *4*    │   *2*    │    ∞     │    ∞     │
│  2   │    C      │    0     │    4     │    2     │  *2+3=5* │    ∞     │
│  3   │    B      │    0     │    4     │    2     │ min(5,   │  *4+5=9* │
│      │           │          │          │          │  4+1=5)  │          │
│      │           │          │          │          │   = *5*  │    9     │
│  4   │    D      │    0     │    4     │    2     │    5     │ min(9,   │
│      │           │          │          │          │          │  5+2=7)  │
│      │           │          │          │          │          │   = *7*  │
│  5   │    E      │    0     │    4     │    2     │    5     │    7     │
└──────┴───────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
* = value changed this iteration
```

### Final Answer:
```
Shortest distances from A:
  A → A : 0
  A → B : 4   (path: A→B)
  A → C : 2   (path: A→C)
  A → D : 5   (path: A→C→D  OR  A→B→D, both = 5)
  A → E : 7   (path: A→C→D→E or A→B→D→E)
```

---

### Relaxation Checks Explained (Iteration 3 — settling B)

When B is settled (dist[B]=4), we check B's neighbors: D and E
```
Neighbor D:
  Old dist[D] = 5   (from C)
  New candidate = dist[B] + w(B,D) = 4 + 1 = 5
  5 < 5?  NO (equal, not less) → NO UPDATE
  dist[D] stays 5

Neighbor E:
  Old dist[E] = ∞
  New candidate = dist[B] + w(B,E) = 4 + 5 = 9
  9 < ∞?  YES → UPDATE dist[E] = 9
```

---

## Worked Example 2 — Lecture Example (R,S,T,X,Y,Z,W)

This is from your class lecture. Source = R.

### Graph
```
         10              5
  (R) --------> (S) ---------> (X)
   |           / |              |
  5|          /  |              |
   |       8 /   | 2           2|
   v        /    v              v
  (T) <----/    (Y) ---------> (Z)
       (9)       |       7      |
                 |              |
                1|              |3
                 v              v
                (W) <--------- .
                       (via Z)
```

*(Simplified — using lecture graph structure. Adjust edge weights to match your exact slides.)*

### Standard Trace Structure
```
┌──────┬────────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐
│ Iter │Settled │d[R]   │d[S]   │d[T]   │d[X]   │d[Y]   │d[Z]   │d[W]   │
├──────┼────────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│  0   │   —    │  0    │  ∞    │  ∞    │  ∞    │  ∞    │  ∞    │  ∞    │
│  1   │   R    │  0    │  10   │  5    │  ∞    │  ∞    │  ∞    │  ∞    │
│  2   │   T    │  0    │  10   │  5    │  ∞    │ 5+9=14│  ∞    │  ∞    │
│  ...continued per your lecture slides ...                             │
└──────┴────────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘
```

> 📌 Fill in using YOUR lecture slides. Pattern is always the same — pick minimum, relax neighbors.

---

## Worked Example 3 — Finding Actual Path

Using Example 1 (source=A, target=E), let's find the actual path using `parent[]`.

### Parent Array Trace
```
Init: parent[A]=NIL, parent[B]=NIL, parent[C]=NIL, parent[D]=NIL, parent[E]=NIL

Settle A (dist=0):
  Update B: dist[B]=4, parent[B]=A
  Update C: dist[C]=2, parent[C]=A

Settle C (dist=2):
  Update D: dist[D]=5, parent[D]=C

Settle B (dist=4):
  Check D: 4+1=5, NOT < 5 → no update to parent[D]
  Update E: dist[E]=9, parent[E]=B

Settle D (dist=5):
  Update E: 5+2=7 < 9 → dist[E]=7, parent[E]=D  ← parent changed!

Settle E (dist=7):
  done.

Final parent[]:
  parent[B] = A
  parent[C] = A
  parent[D] = C
  parent[E] = D
```

### Path Reconstruction: A → E
```
Trace backward from E:
  E → parent[E]=D → parent[D]=C → parent[C]=A → A is source, stop!

Reverse: A → C → D → E

Total cost: w(A,C) + w(C,D) + w(D,E) = 2 + 3 + 2 = 7 ✅
```

---

## Worked Example 4 — Priority Queue Trace

Same graph (source=A). Let's trace the **heap state** at each step.

```
After Init:
  Heap: [(A,0), (B,∞), (C,∞), (D,∞), (E,∞)]
  Min at top: A with dist=0

Extract A (dist=0):
  Process neighbors: B→4, C→2
  Heap after updates: [(C,2), (B,4), (D,∞), (E,∞)]
  (heap re-orders: C is now minimum!)

Extract C (dist=2):
  Process neighbors: D→5
  Heap after updates: [(B,4), (D,5), (E,∞)]

Extract B (dist=4):
  Process neighbors: D→5 (no improvement), E→9
  Heap after updates: [(D,5), (E,9)]

Extract D (dist=5):
  Process neighbors: E → 5+2=7 < 9 → DECREASE KEY
  Heap after decrease_key: [(E,7)]
  ← heap shrinks, E's key changed from 9 to 7

Extract E (dist=7):
  No neighbors.
  Heap: empty → DONE!
```

**Key observation:** `decrease_key` is the expensive operation — O(log N) each time, triggered by relaxation.

---

## Relaxation Rule Practice

Quick-fire: should we update or not? (source=A)

```
Scenario 1:
  dist[u] = 3,  w(u,v) = 4,  dist[v] = 8
  Candidate = 3+4 = 7 < 8 → ✅ UPDATE! dist[v] = 7

Scenario 2:
  dist[u] = 5,  w(u,v) = 3,  dist[v] = 7
  Candidate = 5+3 = 8 > 7 → ❌ NO UPDATE

Scenario 3:
  dist[u] = 2,  w(u,v) = 5,  dist[v] = ∞
  Candidate = 2+5 = 7 < ∞ → ✅ UPDATE! dist[v] = 7

Scenario 4:
  dist[u] = 4,  w(u,v) = 2,  dist[v] = 6
  Candidate = 4+2 = 6 = 6 → ❌ NO UPDATE (not strictly less)
```

---

## Common Mistakes in Numericals

### ❌ Mistake 1: Forgetting to Check ALL neighbors
```
WRONG: Only checking one neighbor per settled vertex
RIGHT: Check ALL edges going out from settled vertex u
```

### ❌ Mistake 2: Updating Already-Settled Vertices
```
WRONG: dist[B] = 5 even though B is already in S
RIGHT: Once in S, NEVER update. Only update vertices in B-S
```

### ❌ Mistake 3: Picking Wrong Minimum
```
WRONG: Picking any unsettled vertex
RIGHT: Pick unsettled vertex with SMALLEST current dist
       (ties: pick either one, note both in answer)
```

### ❌ Mistake 4: Equal Candidate = Update
```
WRONG: If candidate == current dist → update parent
RIGHT: Only update if STRICTLY less than (<), not equal (=)
```

### ❌ Mistake 5: Starting dist Wrong
```
WRONG: dist[source] = 1 or dist[source] = ∞
RIGHT: dist[source] = 0 ALWAYS
```

---

## Blank Trace Table Template

Copy and use for your own graphs:

```
Graph: _______________
Source vertex: ___

Initial distances:
  dist[___] = 0  (source)
  All others = ∞

┌──────┬──────────┬────────┬────────┬────────┬────────┬────────┐
│ Iter │ Settled  │ d[  ]  │ d[  ]  │ d[  ]  │ d[  ]  │ d[  ]  │
├──────┼──────────┼────────┼────────┼────────┼────────┼────────┤
│  0   │    —     │        │        │        │        │        │
├──────┼──────────┼────────┼────────┼────────┼────────┼────────┤
│  1   │          │        │        │        │        │        │
├──────┼──────────┼────────┼────────┼────────┼────────┼────────┤
│  2   │          │        │        │        │        │        │
├──────┼──────────┼────────┼────────┼────────┼────────┼────────┤
│  3   │          │        │        │        │        │        │
├──────┼──────────┼────────┼────────┼────────┼────────┼────────┤
│  4   │          │        │        │        │        │        │
├──────┼──────────┼────────┼────────┼────────┼────────┼────────┤
│  5   │          │        │        │        │        │        │
└──────┴──────────┴────────┴────────┴────────┴────────┴────────┘

Shortest paths from source:
  ___ → ___ : ___
  ___ → ___ : ___
  ___ → ___ : ___
  ___ → ___ : ___
  ___ → ___ : ___
```

---

## ↩️ Navigation

| ← Back | This File | Next → |
|--------|-----------|--------|
| [📚 Theory](../theory/dijkstra_theory.md) | 🔢 Numericals | [💻 Practice →](../practice/dijkstra_practice.md) |

[⬆️ Back to Top](#-dijkstras-algorithm--numerical-analysis)

---
*DSA/ → Dijkstra/ → numericals/dijkstra_numericals.md | rpaut03l/TS-01-Pvt*
