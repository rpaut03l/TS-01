# 🗺️ Dijkstra's Algorithm — Crystal Clear Complete Guide

> **One-Liner**: Dijkstra finds the cheapest/shortest route from one starting point to EVERY other point — like Google Maps finding the fastest route from your house to everywhere!

---

## 🧒 ELI5 — Explain Like I'm 5

**Imagine you're at your house and want to find the cheapest bus route to every place in town.**

Each road has a "cost" (bus fare). Here's your strategy:

1. **Write in your notebook**: "Distance to my house = $0. Distance to everywhere else = infinity (don't know yet)."
2. **Look around from home**: "I can reach the library for $2 and the mall for $4. Write those down."
3. **Visit the CHEAPEST unvisited place**: "Library is cheapest at $2. Go there!"
4. **From the library, look around again**: "From here, I can reach the school for $2+$3=$5. Hey, that's cheaper than what I knew before! Update my notebook."
5. **Visit the next cheapest unvisited place.** Keep going until everywhere is visited.

**The key rule: Always visit the cheapest unvisited place first.** This is the "greedy" choice, and it works because all costs are positive!

---

## 📝 What Problem Does Dijkstra Solve?

**The Single-Source Shortest Path (SSSP) Problem:**

> Given a weighted graph with **non-negative** edge weights and a starting vertex s, find the shortest (cheapest) path from s to EVERY other vertex.

**CRITICAL REQUIREMENT**: All edge weights must be **≥ 0**. Negative weights break the algorithm! (Use Bellman-Ford for negative weights.)

---

## 💡 The Two Key Concepts

### Concept 1: Relaxation — "Can I Find a Shortcut?"

**Relaxation** is the act of checking: "Can I reach vertex v CHEAPER by going through vertex u?"

```
Current best known distance to v: d[v] = 10
Cost to go through u instead: d[u] + weight(u,v) = 3 + 5 = 8

Is 8 < 10? YES! → Update d[v] = 8. Remember: "I got to v through u."
```

**ELI5**: "Hey, I just found a shortcut! Let me update my map!"

```
RELAX(u, v, w)
1   if d[v] > d[u] + w(u,v)         // Is going through u cheaper?
2       d[v] = d[u] + w(u,v)        // YES! Update the distance
3       parent[v] = u                // Remember: came through u
```

### Concept 2: Greedy Choice — "Always Visit the Closest Unvisited Place"

Among all unvisited vertices, always pick the one with the **smallest known distance**. Once you visit it, its distance is FINAL (proven correct).

**Why does this work?** Because all edges are non-negative! If the closest unvisited vertex has d[v] = 5, no future path can give a shorter distance to v (every other path would go through vertices with d ≥ 5, plus some positive edge weight, making the total ≥ 5).

---

## 📜 The Full Algorithm — Crystal Clear

```
DIJKSTRA(G, w, s)
1   for each vertex v ∈ V:
2       d[v] = ∞                    // Unknown distance
3       parent[v] = NIL             // Unknown predecessor
4   d[s] = 0                        // Distance to source = 0
5   S = ∅                           // Set of finalized vertices
6   Q = min-priority-queue(V)       // All vertices, ordered by d[v]
7   while Q is not empty:
8       u = EXTRACT-MIN(Q)          // Get vertex with smallest d[u]
9       S = S ∪ {u}                 // Finalize u
10      for each neighbor v of u:
11          RELAX(u, v, w)          // Try to improve d[v] via u
```

### Line-by-Line Explanation:

**Lines 1-4 (Initialize)**: Set all distances to ∞ except the source (which is 0). We don't know the shortest path to anywhere yet.

**Lines 5-6 (Setup)**: Create a priority queue with ALL vertices, ordered by their current distance. The source (d=0) will be at the front.

**Line 8 (Greedy Choice)**: Extract the vertex with the SMALLEST distance from the queue. This vertex's distance is now FINALIZED — it will never change.

**Lines 10-11 (Relaxation)**: For each neighbor of u, check if going through u gives a shorter path. If yes, update!

---

## 🎨 COMPLETE Visual Walkthrough

### Graph:
```
    A ---4--- B
    |         |
    2         1
    |         |
    C ---3--- E
         |
         5
         |
         D
```

Edges: A-B(4), A-C(2), B-C(1), B-D(5), C-E(3), D-E(2)

### Dijkstra from A:

```
═══ INITIALIZATION ═══
d[A]=0, d[B]=∞, d[C]=∞, d[D]=∞, d[E]=∞
Queue: {A(0), B(∞), C(∞), D(∞), E(∞)}
Finalized: {}

═══ STEP 1: Extract A (d=0) — cheapest in queue ═══
Finalize A. Now check A's neighbors:
  Relax A→B: d[B] = min(∞, 0+4) = 4. Update! parent[B] = A.
  Relax A→C: d[C] = min(∞, 0+2) = 2. Update! parent[C] = A.

Status: d[A]=0✓  d[B]=4  d[C]=2  d[D]=∞  d[E]=∞
Queue: {C(2), B(4), D(∞), E(∞)}

═══ STEP 2: Extract C (d=2) — cheapest unvisited ═══
Finalize C. Check C's neighbors:
  Relax C→A: A is finalized → skip!
  Relax C→B: d[B] = min(4, 2+1) = 3. SHORTER VIA C! parent[B] = C.
  Relax C→E: d[E] = min(∞, 2+3) = 5. Update! parent[E] = C.

Status: d[A]=0✓  d[B]=3  d[C]=2✓  d[D]=∞  d[E]=5
Queue: {B(3), E(5), D(∞)}

═══ STEP 3: Extract B (d=3) — cheapest unvisited ═══
Finalize B. Check B's neighbors:
  Relax B→A: finalized → skip.
  Relax B→C: finalized → skip.
  Relax B→D: d[D] = min(∞, 3+5) = 8. Update! parent[D] = B.

Status: d[A]=0✓  d[B]=3✓  d[C]=2✓  d[D]=8  d[E]=5
Queue: {E(5), D(8)}

═══ STEP 4: Extract E (d=5) — cheapest unvisited ═══
Finalize E. Check E's neighbors:
  Relax E→C: finalized → skip.
  Relax E→D: d[D] = min(8, 5+2) = 7. SHORTER VIA E! parent[D] = E.

Status: d[A]=0✓  d[B]=3✓  d[C]=2✓  d[D]=7  d[E]=5✓
Queue: {D(7)}

═══ STEP 5: Extract D (d=7) — last vertex ═══
Finalize D. No new improvements possible.

Status: d[A]=0✓  d[B]=3✓  d[C]=2✓  d[D]=7✓  d[E]=5✓
```

### Final Results:

| Vertex | Shortest Distance | Shortest Path | How We Found It |
|--------|------------------|---------------|-----------------|
| A | 0 | A | (source) |
| B | 3 | A → C → B | Through C was shorter than direct A→B(4)! |
| C | 2 | A → C | Direct |
| D | 7 | A → C → E → D | Through E was shorter than through B! |
| E | 5 | A → C → E | Through C |

---

## ⚠️ Why Negative Weights Break Dijkstra

Once Dijkstra "finalizes" a vertex, it NEVER revisits it. But with negative edges:

```
    A --(-10)-- B
     \         /
      3       2
       \    /
         C

Dijkstra from A:
  d[A]=0, d[B]=-10?, d[C]=3
  Extract A: d[B]=-10, d[C]=3
  Extract B (d=-10): finalize. But what about A→C→B = 3+2 = 5?
  5 > -10 so it seems fine. But what if:

    A --(1)--> B --(1)--> C --(-5)--> A
  
  This creates a negative cycle! Going around reduces distance forever.
  Dijkstra can't handle this — use Bellman-Ford instead.
```

---

## ⏱️ Time Complexity

| Priority Queue Implementation | EXTRACT-MIN | DECREASE-KEY | Total Time |
|-------------------------------|-------------|-------------|-----------|
| Simple array (scan for min) | O(V) | O(1) | **O(V²)** |
| Binary min-heap | O(log V) | O(log V) | **O((V+E) log V)** |
| Fibonacci heap | O(log V) | O(1) amortized | **O(V log V + E)** |

**For most cases**: Use binary heap → **O((V+E) log V)**

---

## 🐍 Python Implementation

```python
import heapq

def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using a min-heap.
    
    graph: dict where graph[u] = [(neighbor, weight), ...]
    source: starting vertex
    
    Returns: (distances dict, parents dict)
    """
    # Initialize: all distances = infinity, source = 0
    dist = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}
    dist[source] = 0
    
    # Min-heap: (distance, vertex). Smallest distance always at front.
    heap = [(0, source)]
    visited = set()  # Finalized vertices
    
    while heap:
        d_u, u = heapq.heappop(heap)  # Get cheapest unvisited vertex
        
        if u in visited:
            continue  # Already finalized — skip duplicate entries
        visited.add(u)  # Finalize u
        
        # Check all neighbors of u
        for v, weight in graph[u]:
            if v not in visited:
                new_dist = dist[u] + weight
                if new_dist < dist[v]:  # Found a shorter path!
                    dist[v] = new_dist
                    parent[v] = u
                    heapq.heappush(heap, (new_dist, v))
    
    return dist, parent

def get_path(parent, target):
    """Reconstruct path from source to target using parent pointers."""
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    return path[::-1]  # Reverse to get source → target

# Example:
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('E', 3)],
    'D': [('B', 5), ('E', 2)],
    'E': [('C', 3), ('D', 2)],
}

dist, parent = dijkstra(graph, 'A')
for v in sorted(dist):
    path = get_path(parent, v)
    print(f"A → {v}: distance = {dist[v]}, path = {' → '.join(path)}")
```

---

## 📝 Practice Questions with Detailed Solutions

### Q1: Run Dijkstra from S on: S-A(1), S-B(4), A-B(2), A-C(6), B-C(3).

**Solution:**
```
Init: S=0, A=∞, B=∞, C=∞

Extract S(0): relax S→A: d[A]=1. S→B: d[B]=4.
Extract A(1): relax A→B: d[B]=min(4,1+2)=3. A→C: d[C]=1+6=7.
Extract B(3): relax B→C: d[C]=min(7,3+3)=6.
Extract C(6): done.

Distances: S=0, A=1, B=3, C=6
Path to C: S→A→B→C (cost 1+2+3=6) ✅
```

### Q2: Why can't BFS replace Dijkstra on weighted graphs?

**Solution:** BFS treats all edges as equal (weight 1). On weighted graphs, a path with fewer edges might be LONGER (higher total weight) than a path with more edges but smaller weights. Example: S→A(10) has 1 edge but costs 10. S→B(1)→A(2) has 2 edges but costs only 3. BFS would say S→A is "closer" (1 hop), but Dijkstra correctly finds S→B→A (cost 3 < 10).

### Q3: Dijkstra with all edges weight 1 — how does it compare to BFS?

**Solution:** They give the SAME result (both find shortest path by hop count). But Dijkstra with a heap is O((V+E) log V) while BFS is O(V+E). **BFS is faster for unweighted graphs!**

### Q4: Show Dijkstra fails with negative edge: A-B(1), B-C(2), A-C(10), C-B(-5).

**Solution:**
```
Init: A=0, B=∞, C=∞
Extract A(0): d[B]=1, d[C]=10.
Extract B(1): d[C]=min(10, 1+2)=3. Finalize B.
Extract C(3): relax C→B: d[B]=min(1, 3+(-5))=-2.

But B is already finalized (d=1)! The true shortest path A→C→B has cost
A→B(1)→C(3)→B(-2)... wait, that creates a negative cycle!
B→C→B costs 2+(-5)=-3 per cycle. Going around infinitely → -∞.
Dijkstra can't handle this!
```

### Q5: Reconstruct the shortest path from A to D in Q1's walkthrough.

**Solution:** From the main walkthrough: parent[D]=E, parent[E]=C, parent[C]=A. Path: **A → C → E → D**, distance = 2+3+2 = **7** ✅.

### Q6: What is the time complexity with a simple array (no heap)?

**Solution:** EXTRACT-MIN scans all V vertices each time → O(V) per extraction. V extractions → O(V²). DECREASE-KEY is O(1) with an array. Total: **O(V²)**. This is actually BETTER than the heap version for dense graphs (where E ≈ V²), because O(V²) < O(V² log V).

### Q7: Can Dijkstra handle 0-weight edges?

**Solution:** YES! 0 is non-negative. The constraint is NO NEGATIVE weights, not "must be positive." Dijkstra works perfectly with 0-weight edges.

### Q8: What if the graph is disconnected and some vertices are unreachable?

**Solution:** Unreachable vertices keep d[v] = ∞. Dijkstra still works — it just can't reach those vertices. The algorithm finishes when the queue is empty (all reachable vertices have been finalized).

---

## 📋 Quick Revision Cheat Sheet

```
┌──────────────────────────────────────────────────────┐
│  DIJKSTRA — EVERYTHING IN ONE BOX                    │
├──────────────────────────────────────────────────────┤
│                                                      │
│  PROBLEM: Shortest path from ONE source to ALL       │
│                                                      │
│  STRATEGY: Greedy — always visit cheapest unvisited  │
│                                                      │
│  CORE OPERATION: Relaxation                          │
│  if d[v] > d[u] + w(u,v): update d[v], parent[v]     │
│                                                      │
│  REQUIREMENT: All edge weights ≥ 0 (NO negatives!)   │
│                                                      │
│  TIME: O((V+E) log V) with binary heap               │
│                                                      │
│  REMEMBER:                                           │
│  ✅ Works with 0-weight edges                        │
│  ❌ Fails with negative weights → use Bellman-Ford   │
│  For unweighted → just use BFS (simpler, faster)     │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## 📚 References
- CLRS Chapter 24 (Single-Source Shortest Paths - https://walkccc.me/CLRS/Chap24/24.1/)
- [Kleinberg & Tardos, Chapter 4](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/)
- Lec's 14 — Pr V Raj S
