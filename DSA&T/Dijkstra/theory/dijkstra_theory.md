# 📚 Dijkstra's Algorithm — Theory Guide

> **Subject:** DSA | **Topic:** Shortest Paths | **Algo:** Dijkstra  
> **Repo:** `rpaut03l/TS-01-Pvt` → `DSA/Dijkstra/theory/`

---

## 🗺️ Navigation

| ← Prev | This File | Next → |
|--------|-----------|--------|
| [🏠 Dijkstra Hub](../dijkstra_hub.md) | 📚 Theory | [🔢 Numericals](../numericals/dijkstra_numericals.md) |

**Jump Inside This File:**
- [1. Easy Story — What Even IS This?](#1-Easy-story--what-even-is-this)
- [2. Graph Basics First](#2-graph-basics-first)
- [3. The Shortest Path Problem](#3-the-shortest-path-problem)
- [4. Dijkstra's Big Idea](#4-dijkstras-big-idea)
- [5. The Algorithm Step by Step](#5-the-algorithm-step-by-step)
- [6. All the Notation You Need](#6-all-the-notation-you-need)
- [7. Mathematical Rules](#7-mathematical-rules)
- [8. Priority Queue — The Secret Weapon](#8-priority-queue--the-secret-weapon)
- [9. ASCII Diagrams](#9-ascii-diagrams)
- [10. Why It Works — The Proof Idea](#10-why-it-works--the-proof-idea)
- [11. Time Complexity](#11-time-complexity)
- [12. Mnemonic + Cheatsheet](#12-mnemonic--cheatsheet)
- [13. Exam Hacks](#13-exam-hacks)
- [14. Q&A Viva Prep](#14-qa-viva-prep)

---

## 1. Easy Story — What Even IS This?

Imagine you live in a city with **many roads**. Each road has a **toll price** (weight).  
You want to drive from **your house** to **grandma's house** spending the **least money**.

You don't know the shortest route right away. So you do this:

> 🏠 Start at home. Write **₹0** on a sticky note on your door.  
> Write **₹∞ (super expensive!)** on every other house's door.  
> Each time, visit the house with the **cheapest sticky note** you haven't visited yet.  
> From there, check all roads going out. If going through THIS house makes a neighbor **cheaper**, update their sticky note!  
> Repeat until everyone is visited.

That's **literally** Dijkstra's algorithm. You update sticky notes (distances) and always pick the cheapest unvisited house next.

---

## 2. Graph Basics First

### What is a Graph?

```
A graph G = (V, E)
     V = set of vertices (nodes, like cities)
     E = set of edges (roads connecting cities)
```

### Types

| Term | Meaning | Example |
|------|---------|---------|
| **Vertex (node)** | A point/city | A, B, C |
| **Edge** | A connection between 2 vertices | A→B |
| **Weight** | Cost on an edge | road toll = 5 |
| **Directed** | Edge has direction (one-way road) | A→B only |
| **Undirected** | Edge goes both ways | A↔B |
| **Adjacent** | Two vertices connected by an edge | A and B are adjacent |
| **Degree** | Number of edges on a vertex | deg(A) = 3 |
| **Path** | Sequence of vertices connected by edges | A→B→C→D |
| **Cycle** | Path that comes back to start | A→B→C→A |

### Graph Representations

#### 1. Adjacency List (Most common for Dijkstra)
```
Vertex A: [(B, weight=4), (C, weight=2)]
Vertex B: [(D, weight=5)]
Vertex C: [(B, weight=1), (D, weight=8)]
Vertex D: []
```
✅ Memory efficient for sparse graphs  
✅ Fast to iterate neighbors

#### 2. Adjacency Matrix
```
     A    B    C    D
A  [ 0    4    2    ∞ ]
B  [ ∞    0    ∞    5 ]
C  [ ∞    1    0    8 ]
D  [ ∞    ∞    ∞    0 ]
```
✅ Fast edge lookup  
❌ Wastes memory for sparse graphs

#### 3. Incidence Matrix
```
       e1   e2   e3   e4
A    [  1    1    0    0 ]   ← A is in edges e1, e2
B    [  1    0    0    1 ]   ← B is in edges e1, e4
C    [  0    1    1    0 ]
D    [  0    0    1    1 ]
```
Rows = vertices, Columns = edges. Entry = 1 if vertex is in that edge.

---

## 3. The Shortest Path Problem

### Single Source Shortest Path (SSSP)

> **Problem:** Given a graph G with weights, and a **source vertex s**,  
> find the **shortest distance** from **s to every other vertex**.

**Formal definition:**
```
Given:  G = (V, E, w)   where w(u,v) = weight of edge (u,v)
Find:   δ(s, v)  for all v ∈ V

where δ(s, v) = min weight over all paths from s to v
              = ∞ if no path exists
```

### Key constraint for Dijkstra:
> ⚠️ **All edge weights must be non-negative** (w(u,v) ≥ 0)  
> For negative weights → use Bellman-Ford instead.

---

## 4. Dijkstra's Big Idea

### The Greedy Approach

At every step, Dijkstra **greedily** picks the closest unvisited vertex.

Think of it like this:

```
S   = the "settled" set — vertices whose shortest distance is CONFIRMED
B-S = "unsettled" set — vertices whose distance might still improve

π(v) = current best known distance from source s to vertex v
```

**Core insight:**  
> If we always pick the vertex with minimum π(v) from B-S and add it to S,  
> that vertex's distance is **already optimal** and will never decrease.

Why? Because all weights are ≥ 0, adding more edges can only make paths longer!

---

## 5. The Algorithm Step by Step

### Pseudocode (Conceptual Level)

```
DIJKSTRA(G, s):
  1. Initialise:
       π(s) = 0               ← source is distance 0 from itself
       π(v) = ∞  for all v ≠ s ← everyone else is "unreachable" at start
       S = {}                  ← settled set is empty
       B = V                   ← all vertices are unsettled

  2. While B is not empty:
       a. u = vertex in B with minimum π(u)    ← pick closest unsettled
       b. Add u to S  (remove from B)           ← settle it!
       c. For each neighbor v of u:
             if π(u) + w(u,v) < π(v):           ← found a shorter path!
                π(v) = π(u) + w(u,v)            ← update v's distance
                parent(v) = u                   ← remember the path

  3. Return π  (all shortest distances from s)
```

### With Priority Queue (Efficient Implementation)

```
DIJKSTRA_PQ(G, s):
  1. dist[s] = 0 ; dist[v] = ∞ for all v ≠ s
  2. PQ = MinHeap containing all vertices keyed by dist[]
  3. While PQ is not empty:
       u = PQ.extract_min()          ← pulls out vertex with smallest dist
       For each neighbor v of u:
           new_dist = dist[u] + w(u,v)
           if new_dist < dist[v]:
               dist[v] = new_dist
               PQ.decrease_key(v, new_dist)   ← update in heap
  4. Return dist[]
```

---

## 6. All the Notation You Need

| Symbol | Full Name | Meaning |
|--------|-----------|---------|
| `G = (V, E)` | Graph | V vertices, E edges |
| `w(u, v)` | Weight function | Cost of edge from u to v |
| `δ(s, v)` | True shortest distance | Optimal answer from s to v |
| `π(v)` or `d[v]` | Current estimated distance | Our best guess so far |
| `S` | Settled set | Vertices with confirmed distances |
| `B` or `Q` | Unsettled set / Priority Queue | Vertices still to process |
| `B - S` | Frontier | Unsettled vertices |
| `π(u) + w(u,v)` | Relaxation formula | Candidate new distance for v |
| `parent(v)` or `prev(v)` | Predecessor | Which vertex comes before v in shortest path |
| `N` | \|V\| | Number of vertices |
| `M` | \|E\| | Number of edges |

---

## 7. Mathematical Rules

### Rule 1: Initialisation
```
π(s) = 0
π(v) = ∞   for all v ≠ s
```

### Rule 2: Relaxation
```
If π(u) + w(u, v) < π(v):
    π(v) ← π(u) + w(u, v)
```
This is the heart of Dijkstra. Every time you settle vertex u, you try to "relax" all its outgoing edges.

### Rule 3: Greedy Selection
```
u = argmin { π(v) : v ∈ B - S }
```
Always pick the unsettled vertex with the smallest current distance.

### Rule 4: Optimality Condition
```
When u is extracted from PQ:
    π(u) = δ(s, u)    ← this is now the TRUE shortest distance
```

### Rule 5: Triangle Inequality (Shortest Paths)
```
δ(s, v) ≤ δ(s, u) + w(u, v)   for any edge (u, v)
```

---

## 8. Priority Queue — The Secret Weapon

Without a priority queue, finding the minimum π each step takes O(N) time.  
With a **min-heap** priority queue:

| Operation | Time |
|-----------|------|
| Insert vertex | O(log N) |
| Extract minimum | O(log N) |
| Decrease key | O(log N) |

The priority queue is like a **self-sorting waiting room** — whoever has the smallest number on their ticket always goes next.

```
MinHeap state example:
Priority Queue (min-heap):

     [s:0]
    /      \
[A:4]    [B:2]
  \
[C:7]

Extract min → s:0 comes out first ✅
```

---

## 9. ASCII Diagrams

### Example Graph
```
        4         5
   A -------> B -------> E
   |         /^          |
  2|        / 1          |3
   |       /             |
   v      /              v
   C ----/               F
      (1)
```

Edges with weights:
```
A → B : 4
A → C : 2
C → B : 1
B → E : 5
E → F : 3
```

### Settled vs Unsettled Sets
```
Initial State:
  S (settled):   {}
  B-S (unsettled): {A:0, B:∞, C:∞, E:∞, F:∞}
  
                  ┌─────────────┐    ┌──────────────────────────┐
  SETTLED (S)     │             │    │  UNSETTLED (B-S)         │
  Confirmed ✓     │    empty    │    │  A:0  B:∞  C:∞  E:∞  F:∞ │
                  └─────────────┘    └──────────────────────────┘
```

### State After Each Step
```
Step 1: Pick A (min π = 0), settle it, relax neighbors B and C
  S:   {A:0}
  B-S: {B:4, C:2, E:∞, F:∞}
  
Step 2: Pick C (min π = 2), settle it, relax neighbors B
  C→B: π(C)+w(C,B) = 2+1 = 3 < 4  → update B to 3!
  S:   {A:0, C:2}
  B-S: {B:3, E:∞, F:∞}

Step 3: Pick B (min π = 3), settle it, relax E
  B→E: 3+5 = 8
  S:   {A:0, C:2, B:3}
  B-S: {E:8, F:∞}

Step 4: Pick E (min π = 8), relax F
  E→F: 8+3 = 11
  S:   {A:0, C:2, B:3, E:8}
  B-S: {F:11}

Step 5: Pick F (min π = 11)
  S:   {A:0, C:2, B:3, E:8, F:11}
  B-S: {} ← done!

Final distances from A:
  A=0, C=2, B=3, E=8, F=11
```

---

## 10. Why It Works — The Proof Idea

**Invariant (what stays true every loop):**  
> For every vertex in S, its π value equals the true shortest distance δ(s, v).

**Why picking the minimum is safe:**  
When we pick vertex u with minimum π(u) from B-S:
- Any other path to u must go through some other vertex x ∈ B-S first
- But π(x) ≥ π(u) (because u was minimum)
- And all weights are ≥ 0, so adding more edges only increases the path
- Therefore, no path through x can give a shorter route to u
- → π(u) is already optimal! ✅

This is why **negative weights break Dijkstra** — a negative edge could make π(x) + w < π(u) even if π(x) > π(u).

---

## 11. Time Complexity

### With Adjacency List + Binary Min-Heap

| Part | Cost | Why |
|------|------|-----|
| Initialisation | O(N) | Set all distances to ∞ |
| N × extract_min | O(N log N) | Each extract = O(log N) |
| M × decrease_key | O(M log N) | Each edge triggers ≤1 decrease |
| **Total** | **O((N + M) log N)** | Dominant term |

For dense graphs (M ≈ N²): O(N² log N)  
For sparse graphs (M ≈ N): O(N log N) ← very fast!

### With Fibonacci Heap (theoretical best)
```
Total: O(M + N log N)
```
Harder to implement but optimal theoretically.

### Simple Array (no heap):
```
Total: O(N²)    ← fine for dense graphs
```

---

## 12. Mnemonic + Cheatsheet

### 🧠 MNEMONIC: **"GREP-S"**
```
G - Greedy pick the minimum
R - Relax all neighbors
E - Every settled vertex is optimal
P - Priority Queue speeds it up
S - Source starts at 0, rest at ∞
```

### ⚡ Cheatsheet Card
```
┌─────────────────────────────────────────────────────┐
│              DIJKSTRA CHEATSHEET                    │
├─────────────────────────────────────────────────────┤
│ Works on:    weighted graph, w ≥ 0                  │
│ Doesn't work: negative weights → use Bellman-Ford   │
│                                                     │
│ Init:        dist[s]=0, dist[v]=∞, PQ=all vertices  │
│ Loop:        u = extract_min(PQ)                    │
│              for v in neighbors(u):                 │
│                if dist[u]+w(u,v) < dist[v]:         │
│                   dist[v] = dist[u]+w(u,v)          │
│                   decrease_key(v)                   │
│                                                     │
│ Complexity:  O((N+M) log N) with min-heap           │
│ Stops when:  PQ is empty (all settled)              │
│                                                     │
│ Key sets:    S = settled, B-S = unsettled           │
│ Key formula: dist[u] + w(u,v) < dist[v]  → RELAX!   │
└─────────────────────────────────────────────────────┘
```

### 📌 Quick Rules
```
✓ Always pick MINIMUM from unsettled
✓ Settle means: distance is FINAL, never update again
✓ Only relax neighbors of NEWLY settled vertex
✓ If new path < old dist → update + decrease_key
✓ Stop when PQ empty OR when target is settled
```

---

## 13. Exam Hacks

### 🎯 Trick 1: Table Method for Tracing
Always draw a table — examiners love it:
```
Iter | Settled u | dist[A] | dist[B] | dist[C] | dist[D]
-----|-----------|---------|---------|---------|--------
Init |     -     |    0    |    ∞    |    ∞    |    ∞
  1  |     A     |    0    |    4    |    2    |    ∞
  2  |     C     |    0    |    3    |    2    |    ∞
  3  |     B     |    0    |    3    |    2    |    8
  4  |     D     |    0    |    3    |    2    |    8
```

### 🎯 Trick 2: Only Update When Shorter
Many students update ALL neighbors — wrong! Only update if:
```python
dist[u] + w(u,v)  <  dist[v]      ← strictly less than
```

### 🎯 Trick 3: Dijkstra ≠ BFS ≠ Prim
```
BFS       → unweighted shortest path (# edges)
Dijkstra  → weighted shortest path (min cost)
Prim      → minimum spanning tree (not shortest path!)
```
They look similar but do DIFFERENT things!

### 🎯 Trick 4: Path Reconstruction
To get the actual path (not just distances), store `parent[]`:
```
parent[v] = u   whenever you update dist[v] via u
Then trace back: target → parent[target] → ... → source
```

### 🎯 Trick 5: When to Stop Early
If you only need shortest path to ONE target t:
```python
if u == t: break    ← stop as soon as target is settled!
```

---

## 14. Q&A Viva Prep

**Q: What is Dijkstra's algorithm used for?**  
A: Finding shortest paths from one source vertex to all others in a graph with non-negative edge weights.

**Q: Why doesn't Dijkstra work with negative weights?**  
A: Because the greedy assumption breaks — a negative edge could make an "already settled" vertex's distance shorter later. Use Bellman-Ford for negatives.

**Q: What is the role of the priority queue?**  
A: It efficiently gives us the unsettled vertex with minimum distance in O(log N) instead of scanning all vertices in O(N).

**Q: What is relaxation?**  
A: Updating a vertex's distance if we found a shorter path. If dist[u] + w(u,v) < dist[v], we "relax" edge (u,v) by updating dist[v].

**Q: What do S and B-S represent?**  
A: S is the settled set — vertices with confirmed final distances. B-S is the unsettled frontier — vertices still being processed.

**Q: What is the time complexity and why?**  
A: O((N+M) log N) with a binary min-heap. We do N extract_min operations and up to M decrease_key operations, each costing O(log N).

**Q: Is Dijkstra a greedy algorithm?**  
A: Yes. At each step it greedily selects the minimum distance unsettled vertex, trusting that this is already the optimal choice.

**Q: How do you reconstruct the actual shortest path?**  
A: Maintain a parent[] array. When relaxing v via u, set parent[v] = u. Then trace back from target to source using parent pointers.

---

## ↩️ Navigation

| ← Back | This File | Next → |
|--------|-----------|--------|
| [🏠 Dijkstra Hub](../dijkstra_hub.md) | 📚 Theory | [🔢 Numericals →](../numericals/dijkstra_numericals.md) |

[⬆️ Back to Top](#-dijkstras-algorithm--theory-guide)

---
*DSA/ → Dijkstra/ → theory/dijkstra_theory.md | rpaut03l/TS-01-Pvt*
