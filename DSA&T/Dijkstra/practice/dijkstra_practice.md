# 💻 Dijkstra's Algorithm — Practice & Code

> **Subject:** DSA | **Topic:** Shortest Paths | **Algo:** Dijkstra

---

## 🗺️ Navigation

| ← Prev | This File | Next → |
|--------|-----------|--------|
| [🔢 Numericals](../numericals/dijkstra_numericals.md) | 💻 Practice | [🏠 Hub →](../dijkstra_hub.md) |

**Jump Inside This File:**
- [Pseudocode Deep Dive](#pseudocode-deep-dive)
- [Python Implementation — Simple Version](#python-implementation--simple-version)
- [Python Implementation — Priority Queue Version](#python-implementation--priority-queue-version)
- [Python — With Path Reconstruction](#python--with-path-reconstruction)
- [Line by Line Explanation — Kid Friendly](#line-by-line-explanation--kid-friendly)
- [Complexity Analysis Deep Dive](#complexity-analysis-deep-dive)
- [Assignment Hint — Modifying Dijkstra](#assignment-hint--modifying-dijkstra)
- [Practice Problems](#practice-problems)
- [Quick Test Your Understanding](#quick-test-your-understanding)

---

## Pseudocode Deep Dive

### Version 1 — Abstract (Set-Based)

```
DIJKSTRA(G, s):
  ─────────────────────────────────────────────
  SETUP:
    for each vertex v in G.V:
        π[v] = ∞           // nobody reachable yet
        parent[v] = NIL    // no path found yet
    π[s] = 0               // source costs nothing

    S = ∅                  // settled set is empty
    Q = G.V                // all vertices unsettled
  ─────────────────────────────────────────────
  MAIN LOOP:
    while Q ≠ ∅:
        u = EXTRACT-MIN(Q)         // pick cheapest unsettled
        S = S ∪ {u}                // settle it

        for each v in Adj[u]:      // check all neighbors
            RELAX(u, v, w)         // try to improve v's distance
  ─────────────────────────────────────────────
  RELAX(u, v, w):
    if π[u] + w(u,v) < π[v]:
        π[v] = π[u] + w(u,v)
        parent[v] = u
  ─────────────────────────────────────────────
```

### Version 2 — With Priority Queue (Implementation-Ready)

```
DIJKSTRA_PQ(G, s):
  ─────────────────────────────────────────────
  SETUP:
    dist[s]    = 0
    dist[v]    = ∞   for all v ≠ s
    parent[v]  = NIL for all v
    PQ         = MinHeap()
    PQ.insert((0, s))               // (priority=0, vertex=s)
  ─────────────────────────────────────────────
  MAIN LOOP:
    while PQ is not empty:
        (d, u) = PQ.extract_min()   // cheapest in queue

        if d > dist[u]:
            continue                // stale entry, skip

        for each (v, weight) in Adj[u]:
            new_dist = dist[u] + weight

            if new_dist < dist[v]:  // RELAX condition
                dist[v]   = new_dist
                parent[v] = u
                PQ.insert((new_dist, v))  // push updated entry
  ─────────────────────────────────────────────
  return dist, parent
```

> 💡 **Why `if d > dist[u]: continue`?**  
> In Python's heapq, we can't do decrease_key easily. Instead we push a NEW entry.  
> Old stale entries stay in heap. When popped, if `d > dist[u]`, skip them (they're outdated).

---

## Python Implementation — Simple Version

```python
# ============================================================
# Dijkstra's Algorithm — Simple Version (No Heap)
# Time: O(N^2)  |  Space: O(N)
# Best for: small graphs, easy to understand
# ============================================================

def dijkstra_simple(graph, source):
    """
    graph : dict of dict  → graph[u][v] = weight of edge u→v
    source: starting vertex
    returns: dist dict with shortest distances from source
    """
    # ── STEP 1: Get all vertices ──────────────────────────
    vertices = list(graph.keys())
    n = len(vertices)

    # ── STEP 2: Initialise distances ─────────────────────
    dist = {v: float('inf') for v in vertices}   # everyone = ∞
    dist[source] = 0                              # source = 0

    # ── STEP 3: Track visited ─────────────────────────────
    visited = set()

    # ── STEP 4: Main loop — repeat N times ───────────────
    for _ in range(n):

        # Find unvisited vertex with minimum dist
        u = None
        for v in vertices:
            if v not in visited:
                if u is None or dist[v] < dist[u]:
                    u = v

        if u is None or dist[u] == float('inf'):
            break   # no reachable unvisited vertices left

        # Mark u as visited (settled)
        visited.add(u)

        # Relax all neighbors of u
        for neighbor, weight in graph[u].items():
            candidate = dist[u] + weight
            if candidate < dist[neighbor]:
                dist[neighbor] = candidate

    return dist


# ── TEST ──────────────────────────────────────────────────
if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 1, 'E': 5},
        'C': {'D': 3},
        'D': {'E': 2},
        'E': {}
    }
    result = dijkstra_simple(graph, 'A')
    print("Shortest distances from A:")
    for vertex, distance in sorted(result.items()):
        print(f"  A → {vertex} : {distance}")

# Expected Output:
#   A → A : 0
#   A → B : 4
#   A → C : 2
#   A → D : 5
#   A → E : 7
```

---

## Python Implementation — Priority Queue Version

```python
# ============================================================
# Dijkstra's Algorithm — Priority Queue Version
# Time: O((N+M) log N)  |  Space: O(N + M)
# Best for: large sparse graphs, efficient
# ============================================================

import heapq

def dijkstra_pq(graph, source):
    """
    graph : dict of list  → graph[u] = [(v, weight), ...]
    source: starting vertex
    returns: dist dict with shortest distances from source
    """
    # ── STEP 1: Initialise all distances to ∞ ────────────
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    # ── STEP 2: Min-heap priority queue ──────────────────
    # Each entry: (distance, vertex)
    # heapq always pops the SMALLEST distance
    pq = [(0, source)]   # start: source at distance 0

    # ── STEP 3: Main loop ─────────────────────────────────
    while pq:
        # Get vertex with current minimum distance
        current_dist, u = heapq.heappop(pq)

        # Skip if this is a stale (outdated) entry
        # (happens because we push duplicates instead of decrease_key)
        if current_dist > dist[u]:
            continue

        # Relax all neighbors of u
        for v, weight in graph[u]:
            new_dist = dist[u] + weight

            # Only update if we found a SHORTER path
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))  # push updated entry

    return dist


# ── TEST ──────────────────────────────────────────────────
if __name__ == "__main__":
    # Adjacency list format: graph[u] = [(v, weight), ...]
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('D', 1), ('E', 5)],
        'C': [('D', 3)],
        'D': [('E', 2)],
        'E': []
    }
    result = dijkstra_pq(graph, 'A')
    print("Shortest distances from A:")
    for vertex, distance in sorted(result.items()):
        print(f"  A → {vertex} : {distance}")
```

---

## Python — With Path Reconstruction

```python
import heapq

def dijkstra_with_path(graph, source, target=None):
    """
    Full Dijkstra with path reconstruction.
    Returns both distances AND actual paths.
    """
    dist   = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        # Early stop: if we only need path to one target
        if target and u == target:
            break

        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v]   = new_dist
                parent[v] = u          # remember: came from u
                heapq.heappush(pq, (new_dist, v))

    # ── PATH RECONSTRUCTION ───────────────────────────────
    def get_path(end):
        path = []
        node = end
        while node is not None:         # trace back to source
            path.append(node)
            node = parent[node]
        path.reverse()                  # flip: source first
        if path[0] == source:
            return path
        return []  # no path found

    if target:
        return dist[target], get_path(target)
    return dist, {v: get_path(v) for v in graph}


# ── TEST ──────────────────────────────────────────────────
if __name__ == "__main__":
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('D', 1), ('E', 5)],
        'C': [('D', 3)],
        'D': [('E', 2)],
        'E': []
    }
    distance, path = dijkstra_with_path(graph, 'A', 'E')
    print(f"Shortest distance A→E: {distance}")
    print(f"Path: {' → '.join(path)}")

# Output:
# Shortest distance A→E: 7
# Path: A → C → D → E
```

---

## Line by Line Explanation — Kid Friendly

Here's the priority queue version explained like you're hearing it for the first time:

```python
import heapq
# heapq is Python's built-in "magic sorted list"
# It automatically keeps the SMALLEST thing at the front
# Think of it as a queue where people with smaller numbers get in first

def dijkstra_pq(graph, source):

    dist = {v: float('inf') for v in graph}
    # Make a dictionary (like a notebook) for EVERY vertex
    # Write "infinity" for each one — means "I don't know how to get there yet"
    # float('inf') is Python's way of writing ∞

    dist[source] = 0
    # The starting point costs NOTHING to get to — you're already there!

    pq = [(0, source)]
    # Make a priority queue (sorted waiting room)
    # First person in line: our source vertex, with distance 0
    # Format: (distance, vertex_name)

    while pq:
    # Keep going as long as there's someone in the waiting room

        current_dist, u = heapq.heappop(pq)
        # "heappop" = take out the person with the SMALLEST distance number
        # current_dist = their distance number
        # u = which vertex they represent

        if current_dist > dist[u]:
            continue
        # This is a "ghost" entry — an old outdated version of u
        # If the number on their ticket is WORSE than what we already know,
        # skip them. They're like someone who got a better seat later.

        for v, weight in graph[u]:
        # Look at ALL roads going OUT from u
        # v = where the road leads
        # weight = how long/expensive that road is

            new_dist = dist[u] + weight
            # If I go through u to reach v, total cost = dist to u + road cost

            if new_dist < dist[v]:
            # Is this new path CHEAPER than what we knew before?

                dist[v] = new_dist
                # YES! Update v's notebook entry to the cheaper cost

                heapq.heappush(pq, (new_dist, v))
                # Add v to the waiting room with its new (cheaper) ticket number
                # heappush = add to queue, auto-sorts by smallest number

    return dist
    # After everyone has been processed, return the notebook with all distances
```

---

## Complexity Analysis Deep Dive

```
┌──────────────────────────────────────────────────────────────┐
│                  WHERE DOES O((N+M) log N) COME FROM?        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  N = number of vertices                                      │
│  M = number of edges                                         │
│                                                              │
│  Operations:                                                 │
│  ┌──────────────────────┬──────────┬───────────────────────┐ │
│  │ What                 │ How many │ Cost each             │ │
│  ├──────────────────────┼──────────┼───────────────────────┤ │
│  │ Extract-min from PQ  │    N     │  O(log N) per extract │ │
│  │ Push to PQ           │    M     │  O(log N) per push    │ │
│  │ Total                │  N+M     │  × O(log N)           │ │
│  └──────────────────────┴──────────┴───────────────────────┘ │
│                                                              │
│  Total = O(N log N)  +  O(M log N)                           │
│        = O((N + M) log N)                                    │
│                                                              │
│  Special cases:                                              │
│    Dense graph  M ≈ N²  → O(N² log N)                        │
│    Sparse graph M ≈ N   → O(N log N)  ← very fast!           │
│    Simple array (no heap) → O(N²)                            │
│    Fibonacci heap         → O(M + N log N) ← theoretical     │
└──────────────────────────────────────────────────────────────┘
```

### Space Complexity
```
dist[]    : O(N)   — one entry per vertex
parent[]  : O(N)   — one entry per vertex
pq        : O(M)   — can have up to M entries (one per edge)
graph     : O(N+M) — adjacency list storage

Total Space: O(N + M)
```

---

## Assignment Hint — Modifying Dijkstra

Your assignment says:
> "Modify the algorithm to use only one extra ID for distance calculations and to predict the shortest path. Runtime should remain unchanged."

### What this likely means:

**Part 1: "One extra ID"** — probably means using only a SINGLE extra array/variable beyond the graph itself. This points to storing dist[] but NOT a separate parent[] — instead, encode parent info within dist or reconstruct path differently.

**Part 2: "Predict the shortest path"** — reconstructing the actual path, not just distances. This needs parent[] tracking (or equivalent).

**Part 3: "Runtime unchanged"** — keep O((N+M) log N). Don't add expensive loops.

### One approach — encode parent in a combined structure:
```python
def dijkstra_single_extra(graph, source, target):
    """Uses dist[] as single extra structure.
    Reconstruct path by re-running relaxations."""

    dist = {v: float('inf') for v in graph}
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == target:
            break
        for v, w in graph[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    # Reconstruct path using ONLY dist[] — no parent array!
    # Walk backward: from target, find which neighbor
    # could have preceded it on the shortest path
    path = []
    node = target
    while node != source:
        path.append(node)
        # Find predecessor: neighbor v where dist[v] + w(v,node) == dist[node]
        for v in graph:
            if node in dict(graph[v]):
                w = dict(graph[v])[node]
                if dist[v] + w == dist[node]:
                    node = v
                    break
    path.append(source)
    path.reverse()
    return dist[target], path
```

> ⚠️ This reconstruction is O(N×M) extra. For "runtime unchanged" you'd still want parent[].  
> Talk to your prof about exactly what "one extra ID" means in context.

---

## Practice Problems

### Problem 1 ⭐ (Easy)
```
Graph (directed, weighted):
  1 → 2 : 6
  1 → 3 : 1
  3 → 2 : 2
  2 → 4 : 1
  3 → 4 : 9

Find shortest distances from vertex 1.
```
**Answer:**
```
1→1: 0
1→2: 3  (1→3→2: 1+2=3)
1→3: 1  (direct)
1→4: 4  (1→3→2→4: 1+2+1=4)
```

---

### Problem 2 ⭐⭐ (Medium)
```
Graph (undirected, weighted):
  A-B: 7
  A-C: 9
  A-F: 14
  B-C: 10
  B-D: 15
  C-D: 11
  C-F: 2
  D-E: 6
  E-F: 9

Find shortest distances from A.
```
**Trace it yourself using the blank table template from Numericals!**

**Answers to check:**
```
A→A: 0
A→B: 7
A→C: 9
A→D: 20
A→E: 26
A→F: 11
```

---

### Problem 3 ⭐⭐ (Path Finding)
Using Problem 2's graph, find the actual path from A to E.

**Answer:** A → C → F → E (0+9+2+9=20? No...)  
Actually: A→B→D→E = 7+15+6=28, A→C→D→E = 9+11+6=26 ← shortest!

---

## Quick Test Your Understanding

**Q1: Can Dijkstra's handle this edge: A→B weight -3?**  
A: No. Negative weights break the greedy assumption.

**Q2: In the min-heap, what does extract_min return?**  
A: The vertex with the SMALLEST current distance estimate.

**Q3: After settling vertex u, can dist[u] change?**  
A: No. Once settled, dist[u] is final and never changes.

**Q4: If a vertex has no outgoing edges, what happens when we settle it?**  
A: Nothing — the "for each neighbor" loop has 0 iterations. Move on.

**Q5: What's the difference between Dijkstra and BFS?**  
A: BFS counts edges (all weight=1). Dijkstra uses actual weights. BFS is O(N+M), Dijkstra is O((N+M)logN).

**Q6: Why do we check `if current_dist > dist[u]: continue`?**  
A: Because Python's heapq has no decrease_key — we push duplicates. This skips stale outdated entries.

---

## ↩️ Navigation

| ← Back | This File | Next → |
|--------|-----------|--------|
| [🔢 Numericals](../numericals/dijkstra_numericals.md) | 💻 Practice | [🏠 Hub →](../dijkstra_hub.md) |

[⬆️ Back to Top](#-dijkstras-algorithm--practice--code)

---
*DSA/ → Dijkstra/ → practice/dijkstra_practice.md | rpaut03l/TS-01-Pvt*
