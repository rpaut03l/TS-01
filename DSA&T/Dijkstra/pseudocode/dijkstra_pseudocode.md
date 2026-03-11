# 🧩 Dijkstra's Algorithm — Pseudocode Explained Step by Step

> **Subject:** DSA | **Topic:** Shortest Paths | **Algo:** Dijkstra

---

## 🗺️ Navigation

| ← Prev | This File | Next → |
|--------|-----------|--------|
| [💻 Practice & Code](../practice/dijkstra_practice.md) | 🧩 Pseudocode | [🏠 Hub →](../dijkstra_hub.md) |

**Jump Inside This File:**
- [What Even Is Pseudocode?](#what-even-is-pseudocode)
- [Part 1 — RELAX Sub-function](#part-1--relax-sub-function)
- [Part 2 — Full Algorithm (Set Version)](#part-2--full-algorithm-set-version)
- [Part 3 — With Priority Queue](#part-3--with-priority-queue)
- [Part 4 — Line-by-Line Annotated Walkthrough](#part-4--line-by-line-annotated-walkthrough)
- [Part 5 — Dry Run on a Tiny Graph](#part-5--dry-run-on-a-tiny-graph)
- [Pseudocode vs Real Code Mapping](#pseudocode-vs-real-code-mapping)
- [Cheatsheet — All Rules at a Glance](#cheatsheet--all-rules-at-a-glance)
- [Exam Hacks for Pseudocode Questions](#exam-hacks-for-pseudocode-questions)

---

## What Even Is Pseudocode?

Think of pseudocode as **a recipe written in plain English with a little math**.  
Not real Python. Not real C++. Just the *steps* — so any human can follow.

```
Real life example:
  Make tea:
    1. Boil water
    2. Put teabag in cup
    3. Pour hot water
    4. Wait 3 minutes
    5. Remove bag
    6. Add milk if you want

That's pseudocode! It tells WHAT to do, not exactly HOW a kettle works inside.
```

Same idea here. Dijkstra pseudocode tells the computer WHAT to do.  
The Python code (in the Colab file) is HOW it actually runs.

---

## Part 1 — RELAX Sub-function

### The Pseudocode
```
RELAX(u, v, w):
  ┌─────────────────────────────────────────────────────────┐
  │  1.  if π[u] + w(u, v)  <  π[v]  then                  │
  │  2.      π[v]  ←  π[u] + w(u, v)                       │
  │  3.      parent[v]  ←  u                               │
  └─────────────────────────────────────────────────────────┘
```

### What Each Line Means (Easy Version)

```
Line 1:  if π[u] + w(u, v)  <  π[v]
         ───────────────────────────
         "If I travel to u first (costing π[u]),
          then take the road from u to v (costing w(u,v)),
          is that CHEAPER than what I thought v cost before (π[v])?"

         π[u]      = current known best distance to reach u
         w(u, v)   = weight (cost) of the road between u and v
         π[v]      = current known best distance to reach v
         <         = strictly less than (cheaper!)

         Like: "I thought going to grandma's costs ₹50 (π[v]=50).
                But if I go via uncle's house first (π[u]=10),
                then take uncle's shortcut road (w=5),
                total = 10+5 = 15. Is 15 < 50? YES! Use this route!"

Line 2:  π[v]  ←  π[u] + w(u, v)
         ─────────────────────────
         "YES it's cheaper! So ERASE the old cost on v's sticky note.
          Write the NEW cheaper cost instead."
         ← means ASSIGN (like = in Python)

Line 3:  parent[v]  ←  u
         ────────────────
         "Remember: we reached v by coming FROM u.
          This lets us trace the actual path backwards later."
         parent[v] = u  means  "the step before v was u"
```

---

## Part 2 — Full Algorithm (Set Version)

### The Complete Pseudocode
```
DIJKSTRA(G, s):
  ══════════════════════════════════════════════════════════
  PHASE 1 — SETUP (do this once, before the loop)
  ══════════════════════════════════════════════════════════

  1.  for each vertex v ∈ G.V  do
  2.      π[v]       ←  ∞
  3.      parent[v]  ←  NIL
  4.  end for

  5.  π[s]  ←  0

  6.  S  ←  ∅
  7.  Q  ←  G.V

  ══════════════════════════════════════════════════════════
  PHASE 2 — MAIN LOOP (repeat until everyone is settled)
  ══════════════════════════════════════════════════════════

  8.  while Q  ≠  ∅  do
  9.      u  ←  EXTRACT-MIN(Q)
  10.     S  ←  S  ∪  {u}

  11.     for each vertex v  ∈  Adj[u]  do
  12.         RELAX(u, v, w)
  13.     end for

  14. end while

  ══════════════════════════════════════════════════════════
  PHASE 3 — RETURN RESULT
  ══════════════════════════════════════════════════════════

  15. return π, parent
```

---

### What Each Line Means (Easy Version)

```
──────────────────────────────────────────────────────────────
PHASE 1 — Setup
──────────────────────────────────────────────────────────────

Line 1:  for each vertex v ∈ G.V  do
         ────────────────────────────
         "Go through EVERY city/node in the whole graph.
          We're about to give each one a starting value."
         G.V = the complete list of all vertices in graph G

Line 2:  π[v]  ←  ∞
         ────────────
         "Write INFINITY on every city's sticky note.
          ∞ means: 'I have NO IDEA how to get there yet.'
          In code: float('inf') = a number bigger than anything."

Line 3:  parent[v]  ←  NIL
         ──────────────────
         "Write NOTHING in the 'came from' box for every city.
          NIL = None = empty = no path found yet."

Line 4:  end for
         ────────
         "Done setting up all vertices."

Line 5:  π[s]  ←  0
         ──────────
         "THE MOST IMPORTANT LINE!
          The source city costs ZERO to reach — we start there!
          Overwrite the ∞ we just wrote with 0."
         s = source vertex (starting point)

Line 6:  S  ←  ∅
         ─────────
         "Create an empty bag called S (settled set).
          ∅ = empty set = nothing inside yet.
          Vertices go in here once their distance is CONFIRMED."

Line 7:  Q  ←  G.V
         ──────────
         "Create another bag called Q (the unsettled queue).
          Start by putting ALL vertices in here.
          Everyone starts as 'unsettled' — nobody confirmed yet."

──────────────────────────────────────────────────────────────
PHASE 2 — Main Loop
──────────────────────────────────────────────────────────────

Line 8:  while Q  ≠  ∅  do
         ──────────────────
         "Keep looping AS LONG AS there are unsettled vertices.
          When Q becomes empty, everyone is confirmed → stop."
         ≠ means 'not equal to'

Line 9:  u  ←  EXTRACT-MIN(Q)
         ──────────────────────
         "From ALL unsettled vertices in Q,
          pick the one with the SMALLEST π value.
          That vertex is called u."

         WHY smallest? Because if we haven't found anything
         cheaper yet, this IS the cheapest we can ever reach u.
         (Only works because all weights ≥ 0!)

         EXTRACT-MIN also REMOVES u from Q automatically.

Line 10: S  ←  S  ∪  {u}
         ────────────────
         "Drop u into the settled bag S.
          ∪ means UNION = 'add u to the S set'.
          u's distance π[u] is NOW FINAL. It will never change."

Line 11: for each vertex v  ∈  Adj[u]  do
         ──────────────────────────────────
         "Look at all roads going OUT from u.
          For each neighbor city v that u connects to..."
         Adj[u] = adjacency list of u = all neighbors of u

Line 12: RELAX(u, v, w)
         ────────────────
         "Try to improve v's distance using the road u→v.
          (See RELAX explanation above — 3 lines of magic!)"

Line 13: end for
         ─────────
         "Done checking all of u's neighbors."

Line 14: end while
         ──────────
         "Go back to line 8. Pick next minimum. Repeat."

──────────────────────────────────────────────────────────────
PHASE 3 — Return
──────────────────────────────────────────────────────────────

Line 15: return π, parent
         ─────────────────
         "Hand back two things:
          π      = array of shortest distances from s to every vertex
          parent = array to trace actual paths back"
```

---

## Part 3 — With Priority Queue

This is the EFFICIENT version. Same logic, faster in practice.

### The Pseudocode
```
DIJKSTRA-PQ(G, s):
  ══════════════════════════════════════════════════════════
  SETUP
  ══════════════════════════════════════════════════════════

  1.  dist[s]   ←  0
  2.  dist[v]   ←  ∞      for all v ≠ s
  3.  parent[v] ←  NIL    for all v

  4.  PQ  ←  MAKE-MIN-HEAP()
  5.  INSERT(PQ, (0, s))

  ══════════════════════════════════════════════════════════
  MAIN LOOP
  ══════════════════════════════════════════════════════════

  6.  while PQ is not empty  do

  7.      (d, u)  ←  EXTRACT-MIN(PQ)

  8.      if  d  >  dist[u]  then
  9.          continue                ← SKIP (stale entry)
  10.     end if

  11.     for each (v, weight) in Adj[u]  do

  12.         new_dist  ←  dist[u]  +  weight

  13.         if  new_dist  <  dist[v]  then
  14.             dist[v]    ←  new_dist
  15.             parent[v]  ←  u
  16.             INSERT(PQ, (new_dist, v))
  17.         end if

  18.     end for

  19. end while

  ══════════════════════════════════════════════════════════
  RETURN
  ══════════════════════════════════════════════════════════

  20. return dist, parent
```

### What's New / Different Here

```
Line 4:  PQ  ←  MAKE-MIN-HEAP()
         ──────────────────────
         "Create a special sorted list called a Min-Heap.
          It AUTOMATICALLY keeps the smallest item on top.
          Like a priority ticket system — lowest number goes first."

Line 5:  INSERT(PQ, (0, s))
         ────────────────────
         "Put the source vertex into the heap.
          Its ticket says distance=0.
          (We don't put EVERYONE in upfront — we add as we discover them.)"

Line 7:  (d, u)  ←  EXTRACT-MIN(PQ)
         ────────────────────────────
         "Pull out the pair at the TOP of the heap.
          d = the distance number on the ticket
          u = which vertex this ticket belongs to"

Lines 8-10:  if  d  >  dist[u]  then continue
             ──────────────────────────────────
             "IMPORTANT CHECK! This vertex might have been added
              to the heap MULTIPLE TIMES (old + new updated entries).
              If the ticket distance d is WORSE than what we already know,
              this ticket is STALE (outdated). Throw it away, skip."

             Example: We first added (dist=9, E). Later found dist=7, E.
             When we pop (9, E), dist[E] is already 7.
             9 > 7 → STALE → skip it!

Line 16:  INSERT(PQ, (new_dist, v))
          ───────────────────────────
          "Instead of updating v's existing entry in the heap
           (which is hard to find), just ADD A NEW ENTRY.
           The old stale entry will be caught by the check on lines 8-10."
```

---

## Part 4 — Line-by-Line Annotated Walkthrough

Here's the FULL pseudocode with INLINE comments — like reading code with subtitles:

```
DIJKSTRA-PQ(G, s):

  ┌──┬────────────────────────────────────────┬──────────────────────────┐
  │# │ Pseudocode                             │ Plain English            │
  ├──┼────────────────────────────────────────┼──────────────────────────┤
  │1 │ dist[s] ← 0                            │ Source = free to reach   │
  │2 │ dist[v] ← ∞  (all v ≠ s)               │ Others = unknown cost    │
  │3 │ parent[v] ← NIL  (all v)               │ No path found yet        │
  │4 │ PQ ← MAKE-MIN-HEAP()                   │ Empty sorted queue       │
  │5 │ INSERT(PQ, (0, s))                     │ Add source to queue      │
  ├──┼────────────────────────────────────────┼──────────────────────────┤
  │6 │ while PQ not empty do                  │ Until everyone processed │
  │7 │   (d, u) ← EXTRACT-MIN(PQ)             │ Get cheapest vertex      │
  │8 │   if d > dist[u] then                  │ Is this ticket outdated? │
  │9 │     continue                           │ Yes → throw away, skip   │
  │10│   end if                               │                          │
  ├──┼────────────────────────────────────────┼──────────────────────────┤
  │11│   for each (v, weight) in Adj[u] do    │ Check each neighbor road │
  │12│     new_dist ← dist[u] + weight        │ Cost via u = dist + road │
  │13│     if new_dist < dist[v] then         │  Is this cheaper?        │
  │14│       dist[v] ← new_dist               │ Yes! Update sticky note  │
  │15│       parent[v] ← u                    │ Remember: came from u    │
  │16│       INSERT(PQ, (new_dist, v))        │ Add v to queue w new cost│
  │17│     end if                             │                          │
  │18│   end for                              │ Done checking neighbors  │
  ├──┼────────────────────────────────────────┼──────────────────────────┤
  │19│ end while                              │ Loop back if PQ not empty│
  │20│ return dist, parent                    │ Done! Return results     │
  └──┴────────────────────────────────────────┴──────────────────────────┘
```

---

## Part 5 — Dry Run on a Tiny Graph

Let's manually run the pseudocode on the smallest useful graph.

### Graph
```
         4
  (A) ──────► (B)
   │           │
  2│           │ 1
   │           │
   ▼           ▼
  (C) ──────► (D)
         3
```
Edges: A→B:4, A→C:2, B→D:1, C→D:3  |  Source = A

---

### Step 0 — Execute Lines 1-5 (Setup)
```
dist   = {A:0, B:∞, C:∞, D:∞}
parent = {A:NIL, B:NIL, C:NIL, D:NIL}
PQ     = [(0, A)]
```

---

### Step 1 — Execute Lines 6-18 (Iteration 1)

```
Line 6:  PQ not empty? YES → enter loop
Line 7:  EXTRACT-MIN(PQ) → (d=0, u=A)   PQ is now []
Line 8:  d=0 > dist[A]=0? NO → don't skip
Line 11: Adj[A] = [(B,4), (C,2)] → loop over them

  Neighbor B (weight=4):
    Line 12: new_dist = dist[A] + 4 = 0 + 4 = 4
    Line 13: 4 < dist[B]=∞? YES
    Line 14: dist[B] ← 4
    Line 15: parent[B] ← A
    Line 16: INSERT PQ → (4, B)

  Neighbor C (weight=2):
    Line 12: new_dist = 0 + 2 = 2
    Line 13: 2 < dist[C]=∞? YES
    Line 14: dist[C] ← 2
    Line 15: parent[C] ← A
    Line 16: INSERT PQ → (2, C)

State after iteration 1:
  dist   = {A:0, B:4, C:2, D:∞}
  parent = {A:NIL, B:A, C:A, D:NIL}
  PQ     = [(2,C), (4,B)]   ← heap sorted! C is min
```

---

### Step 2 — Iteration 2

```
Line 7:  EXTRACT-MIN → (d=2, u=C)   PQ = [(4,B)]
Line 8:  2 > dist[C]=2? NO → don't skip
Line 11: Adj[C] = [(D,3)]

  Neighbor D (weight=3):
    new_dist = dist[C] + 3 = 2 + 3 = 5
    5 < dist[D]=∞? YES
    dist[D] ← 5, parent[D] ← C
    INSERT PQ → (5, D)

State:
  dist   = {A:0, B:4, C:2, D:5}
  parent = {A:NIL, B:A, C:A, D:C}
  PQ     = [(4,B), (5,D)]
```

---

### Step 3 — Iteration 3

```
Line 7:  EXTRACT-MIN → (d=4, u=B)   PQ = [(5,D)]
Line 8:  4 > dist[B]=4? NO → don't skip
Line 11: Adj[B] = [(D,1)]

  Neighbor D (weight=1):
    new_dist = dist[B] + 1 = 4 + 1 = 5
    5 < dist[D]=5? NO (equal, not less)  ← NO UPDATE!

State:
  dist   = {A:0, B:4, C:2, D:5}
  PQ     = [(5,D)]  ← unchanged
```

---

### Step 4 — Iteration 4

```
Line 7:  EXTRACT-MIN → (d=5, u=D)   PQ = []
Line 11: Adj[D] = []  (no neighbors going out)

State:
  dist   = {A:0, B:4, C:2, D:5}  ← FINAL ANSWER!
  PQ     = []

Line 6:  PQ empty? YES → exit while loop
Line 20: return dist, parent
```

---

### Final Answer
```
Shortest distances from A:
  A → A : 0
  A → B : 4   path: A → B
  A → C : 2   path: A → C
  A → D : 5   path: A → C → D
              (not A→B→D = 4+1 = 5, same cost but C route found first)
```

---

## Pseudocode vs Real Code Mapping

```
┌──────────────────────────────┬────────────────────────────────────────┐
│ Pseudocode                   │ Python (heapq)                         │
├──────────────────────────────┼────────────────────────────────────────┤
│ π[v] ← ∞                     │ dist[v] = float('inf')                 │
│ π[s] ← 0                     │ dist[source] = 0                       │
│ parent[v] ← NIL              │ parent[v] = None                       │
│ S ← ∅                        │ visited = set()                        │
│ Q ← G.V                      │ (implicit in heapq)                    │
│ MAKE-MIN-HEAP()              │ pq = []  (heapq operates on a list)    │
│ INSERT(PQ, (d, v))           │ heapq.heappush(pq, (d, v))             │
│ EXTRACT-MIN(PQ)              │ heapq.heappop(pq)                      │
│ if d > dist[u]: continue     │ if d > dist[u]: continue               │
│ for v in Adj[u]              │ for v, w in graph[u]                   │
│ new_dist ← dist[u] + weight  │ new_dist = dist[u] + weight            │
│ if new_dist < dist[v]        │ if new_dist < dist[v]:                 │
│ dist[v] ← new_dist           │ dist[v] = new_dist                     │
│ parent[v] ← u                │ parent[v] = u                          │
│ return dist, parent          │ return dist, parent                    │
└──────────────────────────────┴────────────────────────────────────────┘
```

---

## Cheatsheet — All Rules at a Glance

```
╔══════════════════════════════════════════════════════════════╗
║           DIJKSTRA PSEUDOCODE CHEATSHEET                     ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  SETUP RULES:                                                ║
║  ✓ dist[source] = 0, all others = ∞                          ║  
║  ✓ parent[all] = NIL                                         ║
║  ✓ Push only (0, source) into PQ at start                    ║
║                                                              ║
║  LOOP RULES:                                                 ║
║  ✓ Always EXTRACT the minimum from PQ                        ║
║  ✓ Check if entry is STALE → skip if d > dist[u]             ║
║  ✓ Check ALL neighbors of u, not just one                    ║
║                                                              ║
║  RELAX RULE:                                                 ║
║  ✓ new = dist[u] + w(u,v)                                    ║
║  ✓ Update ONLY if new < dist[v]  (strictly less!)            ║
║  ✓ Update BOTH dist[v] and parent[v] together                ║
║  ✓ Push new (dist[v], v) to PQ after update                  ║
║                                                              ║
║  STOP RULE:                                                  ║
║  ✓ Stop when PQ is empty (all processed)                     ║
║  ✓ OR stop early when target vertex is popped                ║
║                                                              ║
║  NEVER DO:                                                   ║
║  ✗ Update a vertex already confirmed (settled)               ║
║  ✗ Use on graphs with negative weights                       ║
║  ✗ Forget the stale check (causes wrong answers)             ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Exam Hacks for Pseudocode Questions

### 🎯 Hack 1: If asked to WRITE pseudocode
```
Structure to always use:
  1. Initialise (dist, parent, PQ)
  2. while PQ not empty:
  3.     u = extract_min
  4.     for each neighbor v:
  5.         RELAX(u, v, w)
  6. return dist

Memorise this skeleton → fill in details → done!
```

### 🎯 Hack 2: If asked WHY a line exists
```
Line           → Say this
─────────────────────────────────────────────────
dist[s] = 0   → "Source has zero cost to reach itself"
dist[v] = ∞   → "Unknown = infinity before exploration"
extract_min   → "Greedy choice: closest vertex = optimal next"
stale check   → "Avoid reprocessing outdated heap entries"
RELAX         → "Improve estimate if shorter path found"
parent[v] = u → "Store predecessor for path reconstruction"
```

### 🎯 Hack 3: If asked what happens WITHOUT a line
```
Remove dist[s]=0    → source never gets processed (stuck at ∞)
Remove stale check  → process same vertex multiple times (wrong!)
Remove parent[v]=u  → can't reconstruct path, only get distances
Remove < condition  → update unnecessarily, might still work but wastes time
```

### 🎯 Hack 4: Notation quick fire
```
π[v]     = dist[v]    = current best known distance to v
δ(s,v)   = TRUE shortest distance (only known at the end)
Adj[u]   = adjacency list of u = all neighbors
w(u,v)   = weight of edge from u to v
∅        = empty set
∪        = union (combine two sets)
∈        = "belongs to" / "is in"
≠        = not equal
←        = assign (like = in Python)
NIL/None = nothing / null / empty
```

---

## ↩️ Navigation

| ← Back | This File | Next → |
|--------|-----------|--------|
| [💻 Practice & Code](../practice/dijkstra_practice.md) | 🧩 Pseudocode | [🏠 Hub →](../dijkstra_hub.md) |

[⬆️ Back to Top](#-dijkstras-algorithm--pseudocode-explained-step-by-step)

---
*DSA/ → Dijkstra/ → pseudocode/dijkstra_pseudocode.md | rpaut03l/TS-01-Pvt*
