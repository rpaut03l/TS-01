# 🕸️ Graphs — Introduction — Crystal Clear Complete Guide

> **One-Liner**: A graph = dots (vertices) connected by lines (edges). BFS explores like ripples in a pond. DFS explores like a maze runner.

---

## 🧒 ELI5 — Explain Like I'm 5

**Imagine a treasure map!** 🗺️

- The **islands** are called **vertices** (or nodes) — they're the dots on the map.
- The **bridges** between islands are called **edges** — they're the lines connecting dots.
- Some bridges are **one-way** (like a slide — you can only go down!). That's a **directed** graph.
- Some bridges have **distance numbers** (this bridge is 5 km). That's a **weighted** graph.

Now, if someone says "Visit every island starting from Island A," you have two strategies:

**Strategy 1 — BFS (Breadth-First Search)**: Visit ALL neighboring islands first, then THEIR neighbors, then THEIR neighbors... Like dropping a stone in water — ripples spread outward evenly! 🌊

**Strategy 2 — DFS (Depth-First Search)**: Go as FAR as possible down one path before turning back. Like exploring a maze — run forward until you hit a dead end, then backtrack! 🔦

---

## 📝 What Exactly Is a Graph?

A **graph** G = (V, E) has two parts:
- **V** (Vertices) = the set of dots/nodes. Example: V = {A, B, C, D}
- **E** (Edges) = the set of connections between dots. Example: E = {(A,B), (A,C), (B,D), (C,D)}

```
    A ------- B
    |         |
    |         |
    C ------- D
```

That's it! A graph is just dots and lines. Simple concept, incredibly powerful applications:
- **Social networks**: People are vertices, friendships are edges
- **Road maps**: Cities are vertices, roads are edges
- **The internet**: Web pages are vertices, hyperlinks are edges
- **Computer networks**: Devices are vertices, connections are edges

---

## 🏷️ Types of Graphs — Know the Vocabulary

| Type | What It Means | Example |
|------|--------------|---------|
| **Undirected** | Edges go BOTH ways | Friendships (if A is B's friend, B is A's friend) |
| **Directed** | Edges have a direction (one-way arrows) | Twitter follows (A follows B ≠ B follows A) |
| **Weighted** | Each edge has a number (cost/distance) | Road map with distances |
| **Unweighted** | All edges are equal | Social connections |
| **Connected** | You can reach any vertex from any other | One group of friends |
| **Disconnected** | Some vertices can't reach others | Multiple isolated groups |
| **Cyclic** | Contains at least one "loop" | A→B→C→A |
| **Acyclic** | No loops | Family tree |
| **DAG** | Directed + Acyclic | Task dependencies |

---

## 💻 How to Store a Graph in Code

### Method 1: Adjacency List (Most Common — Use This!)

Each vertex keeps a LIST of its neighbors.

```
Graph:  A—B, A—C, B—D, C—D

Adjacency List:
  A: [B, C]      ← A is connected to B and C
  B: [A, D]      ← B is connected to A and D
  C: [A, D]
  D: [B, C]
```

**Space**: O(V + E). **Great for sparse graphs** (few edges relative to vertices).

### Method 2: Adjacency Matrix

A 2D table where cell [i][j] = 1 if edge exists, 0 otherwise.

```
    A  B  C  D
A [ 0  1  1  0 ]     ← A connects to B and C
B [ 1  0  0  1 ]
C [ 1  0  0  1 ]
D [ 0  1  1  0 ]
```

**Space**: O(V²). **Good for dense graphs** (many edges) or when you need O(1) edge lookup.

### When to Use Which?

| | Adjacency List | Adjacency Matrix |
|-|---------------|-----------------|
| **Space** | O(V + E) — efficient for sparse | O(V²) — wastes space for sparse |
| **Check if edge (u,v) exists?** | O(degree of u) — scan u's list | **O(1)** — just check M[u][v] |
| **Find all neighbors of u?** | **O(degree of u)** — just read the list | O(V) — scan entire row |
| **Best for** | **Most real-world graphs** | Dense graphs, weighted matrices |

---

## 🌊 BFS — Breadth-First Search (Explore Layer by Layer)

### The Big Idea

BFS starts at a source vertex and explores in **waves** — first all vertices at distance 1, then distance 2, then distance 3, etc. It uses a **queue** (First-In-First-Out).

**Think of it like dropping a stone in a pond**: the ripples spread outward, reaching nearby points first, then farther points.

### Why BFS Is Useful

BFS finds the **shortest path** (fewest edges) from the source to every reachable vertex. If the graph is unweighted, BFS gives you the shortest path automatically!

### Full Pseudocode — Explained

```
BFS(G, s)                              // s = source vertex
1   for each vertex u ≠ s:             // Initialize everything
2       u.color = WHITE                 // WHITE = not yet discovered
3       u.d = ∞                         // distance = unknown
4       u.π = NIL                       // parent = unknown
5   s.color = GRAY                      // Mark source as discovered
6   s.d = 0                             // Distance to itself = 0
7   s.π = NIL                           // Source has no parent
8   Q = empty queue                     // Create the queue
9   ENQUEUE(Q, s)                       // Start with source in queue
10  while Q is not empty                // While there are vertices to process
11      u = DEQUEUE(Q)                  // Take the FRONT vertex out
12      for each v adjacent to u        // Look at all neighbors
13          if v.color == WHITE         // If this neighbor is undiscovered
14              v.color = GRAY          // Mark it as discovered
15              v.d = u.d + 1           // Its distance = parent's distance + 1
16              v.π = u                 // Its parent = the vertex we came from
17              ENQUEUE(Q, v)           // Add to queue for later processing
18      u.color = BLACK                 // u is now fully processed

```

### What Do the Colors Mean?

| Color | Meaning | ELI5 |
|-------|---------|------|
| WHITE | Not yet discovered | "Haven't visited this island yet" |
| GRAY | Discovered, in the queue, waiting to be fully explored | "I know about this island, but haven't explored all its bridges" |
| BLACK | Fully explored (all neighbors checked) | "Done with this island — checked all its bridges" |

### Complete BFS Walkthrough

```
Graph: A—B, A—C, B—D, C—D, D—E

BFS from A:

Step 1: Initialize. A is GRAY (d=0). Queue: [A]

Step 2: Dequeue A. Check A's neighbors:
  B is WHITE → mark GRAY, d=1, parent=A. Queue: [B]
  C is WHITE → mark GRAY, d=1, parent=A. Queue: [B, C]
  A is now BLACK.

Step 3: Dequeue B (front of queue). Check B's neighbors:
  A is BLACK → skip.
  D is WHITE → mark GRAY, d=2, parent=B. Queue: [C, D]
  B is now BLACK.

Step 4: Dequeue C. Check C's neighbors:
  A is BLACK → skip.
  D is GRAY → skip (already discovered!).
  C is now BLACK. Queue: [D]

Step 5: Dequeue D. Check D's neighbors:
  B is BLACK → skip.
  C is BLACK → skip.
  E is WHITE → mark GRAY, d=3, parent=D. Queue: [E]
  D is now BLACK.

Step 6: Dequeue E. E has only neighbor D (BLACK) → skip.
  E is now BLACK. Queue: [] → DONE!

RESULTS:
  A: d=0, parent=NIL
  B: d=1, parent=A
  C: d=1, parent=A
  D: d=2, parent=B
  E: d=3, parent=D

SHORTEST PATH from A to E: A → B → D → E (distance 3)
(Trace parents: E.π=D, D.π=B, B.π=A)
```

### BFS Time Complexity

**O(V + E)** — every vertex is enqueued/dequeued once (O(V)), and every edge is examined once (O(E)).

---

## 🔦 DFS — Depth-First Search (Explore as Deep as Possible)

### The Big Idea

DFS starts at a vertex and goes as **DEEP** as possible along one path before backtracking. It uses a **stack** (or recursion, which is an implicit stack).

**Think of it like exploring a maze**: you always go forward. When you hit a dead end, you backtrack to the last intersection and try a different path.

### Why DFS Is Useful

DFS is great for:
- **Cycle detection** (back edge = cycle!)
- **Topological sorting** (ordering tasks with dependencies)
- **Finding connected components**
- **Exploring all paths**

### Full Pseudocode — Explained

```
DFS(G)
1   for each u ∈ V:                // Initialize
2       u.color = WHITE
3       u.π = NIL
4   time = 0                        // Global clock
5   for each u ∈ V:                // Check every vertex
6       if u.color == WHITE         // If not yet visited
7           DFS-VISIT(G, u)         // Start a DFS from u

DFS-VISIT(G, u)
1   time = time + 1
2   u.d = time                      // Discovery time (when first found)
3   u.color = GRAY                  // Mark as "being processed"
4   for each v adjacent to u:       // Check all neighbors
5       if v.color == WHITE          // If neighbor is undiscovered
6           v.π = u                  // Set parent
7           DFS-VISIT(G, v)          // Go DEEPER! (recursive call)
8   u.color = BLACK                  // All neighbors checked
9   time = time + 1
10  u.f = time                       // Finish time (when fully processed)
```

### Discovery Time and Finish Time

DFS gives each vertex TWO timestamps:
- **d[u]** = **discovery time** — when u was first found (turned GRAY)
- **f[u]** = **finish time** — when u was fully processed (turned BLACK)

These satisfy the **Parenthesis Theorem**: If v is a descendant of u in the DFS tree, then d[u] < d[v] < f[v] < f[u]. Like nested parentheses: u opens, v opens, v closes, u closes.

### Edge Classification — How DFS Categorizes Edges

When DFS encounters an edge (u, v):

| v's color when discovered | Edge Type | What It Means |
|--------------------------|-----------|--------------|
| WHITE | **Tree edge** | v is a new vertex — part of DFS tree |
| GRAY | **Back edge** | v is an ANCESTOR of u — **CYCLE DETECTED!** |
| BLACK (d[u] < d[v]) | **Forward edge** | v is a descendant (already finished) |
| BLACK (d[u] > d[v]) | **Cross edge** | v is in a different branch |

**The most important one**: **Back edge = CYCLE!** In an undirected graph, if DFS encounters a gray vertex (that isn't the parent), the graph has a cycle.

### Complete DFS Walkthrough

```
Graph: A—B, A—C, B—D, C—D

DFS from A:
  Visit A (d=1, GRAY)
    Visit B (d=2, GRAY)  ← first neighbor of A
      Visit D (d=3, GRAY)  ← first neighbor of B (that's WHITE)
        Visit C (d=4, GRAY)  ← first neighbor of D that's WHITE
          C's neighbors: A is GRAY (back edge!), D is GRAY (back edge!)
          C finished (f=5, BLACK)
        D's other neighbors: B is GRAY (back edge)
        D finished (f=6, BLACK)
      B finished (f=7, BLACK)
    C is already BLACK (visited) → skip
    A finished (f=8, BLACK)

RESULTS:
  A: (d=1, f=8)    ← discovered first, finished last (root of DFS tree)
  B: (d=2, f=7)
  D: (d=3, f=6)
  C: (d=4, f=5)    ← discovered last in this path, finished first (deepest point)

DFS Tree: A → B → D → C
```

### DFS Time Complexity

**O(V + E)** — same as BFS! Every vertex and every edge is examined exactly once.

---

## ⚖️ BFS vs DFS — When to Use Which?

| Feature | BFS 🌊 | DFS 🔦 |
|---------|--------|--------|
| Data structure | Queue (FIFO) | Stack / Recursion |
| Explores | Level by level (breadth first) | Path by path (depth first) |
| Finds shortest path? | ✅ YES (unweighted) | ❌ NO |
| Detects cycles? | ⚠️ Yes but harder | ✅ YES (back edge = cycle!) |
| Topological sort? | ❌ No | ✅ YES (reverse finish order) |
| Time | O(V + E) | O(V + E) |
| Space | O(V) — queue can hold entire level | O(V) — stack/recursion depth |
| Best for | Shortest paths, level-order | Cycle detection, topological sort, exploring all paths |

---

## 🐍 Python Implementation — Commented

```python
from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, directed=False):
        self.adj.setdefault(u, []).append(v)
        if not directed:
            self.adj.setdefault(v, []).append(u)

    def bfs(self, source):
        """BFS from source. Returns distances and parents."""
        dist = {source: 0}
        parent = {source: None}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in self.adj.get(u, []):
                if v not in dist:  # Not yet discovered
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
        return dist, parent

    def shortest_path(self, source, target):
        """Shortest path using BFS."""
        dist, parent = self.bfs(source)
        if target not in parent:
            return None  # No path!
        path = []
        curr = target
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        return path[::-1]  # Reverse: source → target

    def dfs(self):
        """Full DFS. Returns discovery/finish times."""
        color = {v: 'W' for v in self.adj}
        disc, fin, parent = {}, {}, {}
        self.time = 0

        def visit(u):
            self.time += 1
            disc[u] = self.time
            color[u] = 'G'
            for v in self.adj.get(u, []):
                if color.get(v) == 'W':
                    parent[v] = u
                    visit(v)
            color[u] = 'B'
            self.time += 1
            fin[u] = self.time

        for u in self.adj:
            if color.get(u) == 'W':
                parent[u] = None
                visit(u)
        return disc, fin, parent

# Example:
g = Graph()
for u, v in [('A','B'), ('A','C'), ('B','D'), ('C','D'), ('D','E')]:
    g.add_edge(u, v)

dist, par = g.bfs('A')
print(f"BFS distances from A: {dist}")
print(f"Shortest A→E: {g.shortest_path('A', 'E')}")
```

---

## 📝 Practice Questions with Detailed Solutions

### Q1: Draw the graph for edges (1,2),(1,3),(2,4),(3,4),(4,5). Write adjacency list.

**Solution:**
```
    1—2
    |\ |
    3—4—5

Adjacency list:
1: [2, 3]
2: [1, 4]
3: [1, 4]
4: [2, 3, 5]
5: [4]
```

### Q2: BFS from vertex 1 in the above graph. Show order, distances, tree.

**Solution:**
```
Queue: [1(d=0)]
Dequeue 1: enqueue 2(d=1), 3(d=1). Queue: [2, 3]
Dequeue 2: enqueue 4(d=2). Queue: [3, 4]
Dequeue 3: 4 already discovered. Queue: [4]
Dequeue 4: enqueue 5(d=3). Queue: [5]
Dequeue 5: done. Queue: []

BFS order: 1, 2, 3, 4, 5
Distances: 1→0, 2→1, 3→1, 4→2, 5→3
BFS tree edges: 1→2, 1→3, 2→4, 4→5
Shortest path 1→5: 1→2→4→5 (or 1→3→4→5), distance = 3
```

### Q3: DFS from vertex 1. Show discovery/finish times.

**Solution:**
```
Visit 1(d=1) → Visit 2(d=2) → Visit 4(d=3) → Visit 3(d=4)
  3's unvisited neighbors: 1 is GRAY → back edge! (cycle detected)
  3 finishes (f=5)
  Back at 4: Visit 5(d=6) → 5 finishes (f=7)
  4 finishes (f=8)
  Back at 2: 2 finishes (f=9)
  Back at 1: 3 is already BLACK → skip. 1 finishes (f=10)

Times: 1(1/10), 2(2/9), 4(3/8), 3(4/5), 5(6/7)
DFS tree: 1→2→4→3, 4→5
```

### Q4: Does this graph have a cycle? How does DFS tell you?

**Solution:** YES! When DFS explores 3, it sees neighbor 1 which is GRAY (still being processed). A GRAY neighbor in DFS = **back edge** = **CYCLE!** The cycle is 1→2→4→3→1 (or 1→3→4→2→1).

### Q5: Is this graph bipartite?

**Solution:** Try 2-coloring with BFS:
```
Color 1=A. Color 2,3=B (neighbors of 1). Color 4=A (neighbor of 2 and 3).
Color 5=B (neighbor of 4).
Check all edges: (1A,2B)✅ (1A,3B)✅ (2B,4A)✅ (3B,4A)✅ (4A,5B)✅
All edges connect different colors → YES, bipartite! ✅
```

### Q6: Shortest path from 1 to 5?

**Solution:** From BFS: parent[5]=4, parent[4]=2, parent[2]=1. Path: **1→2→4→5**, distance=3.

### Q7: Topological sort of DAG: A→C, B→C, C→D, B→D.

**Solution:**
```
DFS: Visit A(1/)→C(2/)→D(3/4)→C(2/5)→A(1/6)
     Visit B(7/)→C already done, D already done→B(7/8)

Finish order: D(4), C(5), A(6), B(8)
Topological sort = REVERSE finish order: B, A, C, D ✅
(B and A can be in either order since they're independent)
```

### Q8: How many connected components in {1..6} with edges (1,2),(3,4),(5,6)?

**Solution:** 3 components: {1,2}, {3,4}, {5,6}. BFS/DFS from 1 finds {1,2}. Restart from 3 finds {3,4}. Restart from 5 finds {5,6}. **3 components.**

### Q9: In a directed graph (A→B, B→C, C→A, B→D), classify all DFS edges.

**Solution:**
```
DFS from A: A(1/G)→B(2/G)→C(3/G)→A is GRAY → BACK EDGE (C→A)! = cycle!
C(3/4). B→D: D(5/G)→D(5/6). B(2/7). A(1/8).

Edges:
A→B: Tree edge (B was WHITE) ✅
B→C: Tree edge (C was WHITE) ✅
C→A: BACK edge (A was GRAY) → CYCLE! ✅
B→D: Tree edge (D was WHITE) ✅
```

### Q10: What is the maximum number of edges in an undirected graph with n vertices?

**Solution:** Each pair of vertices can have at most 1 edge. Number of pairs = n × (n-1) / 2 = **n(n-1)/2**. For n=5: 5×4/2 = 10 edges maximum (this is a "complete graph" K₅).

---

## 📋 Quick Revision Cheat Sheet

```
┌──────────────────────────────────────────────────────┐
│  GRAPHS — EVERYTHING IN ONE BOX                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│  GRAPH = Vertices + Edges: G = (V, E)                │
│                                                      │
│  REPRESENTATIONS:                                    │
│  Adjacency List: O(V+E) space — use for sparse       │
│  Adjacency Matrix: O(V²) space — use for dense       │ 
│                                                      │
│  BFS (Breadth-First Search):                         │
│  Uses: Queue    Finds: Shortest paths (unweighted)   │
│  Time: O(V+E)  Space: O(V)                           │
│                                                      │
│  DFS (Depth-First Search):                           │
│  Uses: Stack/Recursion  Finds: Cycles, Topo sort     │
│  Time: O(V+E)  Space: O(V)                           │
│  Back edge (to GRAY vertex) = CYCLE!                 │
│                                                      │
│  KEY FACTS:                                          │
│  Max edges (undirected): n(n-1)/2                    │
│  Connected check: BFS/DFS from any vertex            │
│  Bipartite check: BFS 2-coloring                     │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## 📚 References
- [CLRS Chapter 22](https://walkccc.me/CLRS/Chap22/22.1/)
