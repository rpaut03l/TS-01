# 🚰 Network Flow & Ford-Fulkerson — Crystal Clear Complete Guide

> **One-Liner**: Push as much "stuff" through a network of pipes as possible — Ford-Fulkerson finds the maximum by repeatedly finding paths with room and pushing flow through them!

---

## 🧒 ELI5 — Explain Like I'm 5

**Imagine a water park!** 🏊

There's a big pool at the TOP (called the **source**) and a big pool at the BOTTOM (called the **sink**). Between them are many water slides (pipes) connecting smaller pools.

Each slide can only carry a LIMITED amount of water per second (that's the **capacity**).

**Question**: What's the MOST water per second you can get from the top pool to the bottom pool?

**Ford-Fulkerson's trick**:
1. Find ANY path from top to bottom that still has room.
2. Push as much water as possible through that path (limited by the narrowest slide on the path — that's the **bottleneck**).
3. Update how much room is left on each slide.
4. Repeat until no more paths exist.

**The magic**: If you made a BAD choice earlier (sent water down the wrong pipe), you can FIX it! The "residual network" includes **backward edges** that let you "undo" previous flow decisions. This is what makes the algorithm find the TRUE maximum!

---

## 📝 Key Definitions — Explained Very Carefully

### Flow Network

A **flow network** is a directed graph where:
- Each edge has a **capacity** c(u,v) ≥ 0 (max it can carry)
- There's a special vertex **s** called the **source** (where stuff originates)
- There's a special vertex **t** called the **sink** (where stuff arrives)

### Flow

A **flow** assigns a value f(u,v) to each edge, with two rules:

| Rule | Formal | ELI5 |
|------|--------|------|
| **Capacity constraint** | 0 ≤ f(u,v) ≤ c(u,v) | "You can't push more than the pipe can handle" |
| **Flow conservation** | Σ flow_in = Σ flow_out (at every vertex except s and t) | "Water in = Water out at every intermediate pool" |

### Value of Flow

|f| = total flow OUT of source = total flow INTO sink.

---

## 🔄 Residual Networks — THE Key Insight

After some flow is assigned, the **residual network** shows what's STILL possible:

For each edge (u,v) with capacity c and current flow f:

**Forward residual edge** (u→v): capacity left = c - f
*"This pipe can still carry (c-f) more units."*

**Backward residual edge** (v→u): capacity = f
*"We can UNDO up to f units of the flow on this pipe."*

```
EXAMPLE:
Original edge: A ---(cap=10, flow=7)--→ B

Residual:  A ---(3)--→ B     ← can push 3 more forward
           A ←---(7)--- B    ← can "undo" up to 7 backward
```

### Why Do Backward Edges Exist?

They're the SECRET WEAPON of Ford-Fulkerson! Without them, the algorithm might get stuck with a suboptimal solution.

**Example**: Imagine you sent water down Path 1, but it turns out Path 2 would have been better. The backward edge lets a later augmenting path "steal" water from Path 1 and reroute it through Path 2. It's like saying "undo that decision" — but without actually going back in time!

---

## 📜 The Ford-Fulkerson Algorithm

```
FORD-FULKERSON(G, s, t)
1   Initialize all flows to 0
2   Build the residual graph G_f
3   while there exists a path from s to t in G_f:
4       Find such a path p (called an "augmenting path")
5       δ = min residual capacity along p (the bottleneck)
6       For each edge (u,v) on p:
7           if (u,v) is a forward edge: f(u,v) += δ
8           if (u,v) is a backward edge: f(v,u) -= δ
9       Update the residual graph
10  return f (the maximum flow!)
```

### How to Find the Augmenting Path?

Ford-Fulkerson is a **method** — it doesn't specify HOW to find paths:
- **DFS** → basic Ford-Fulkerson (might be slow with large capacities)
- **BFS** → **Edmonds-Karp algorithm** (guaranteed O(VE²) — use this!)

### Why Does It Stop?

It stops when there's NO path from s to t in the residual graph. At that point, the flow is maximum — guaranteed by the Max-Flow Min-Cut theorem!

---

## 🎨 Complete Visual Walkthrough

### Network:
```
s →(10)→ A →(8)→ t
s →(5)→ B →(7)→ t
A →(6)→ B
```

### Step by Step:

```
═══ INIT: All flows = 0 ═══
Residual: s→A(10), s→B(5), A→t(8), B→t(7), A→B(6)

═══ ITERATION 1 ═══
BFS finds path: s → A → t
Bottleneck = min(10, 8) = 8
Push 8 units: f(s,A)=8, f(A,t)=8
Residual: s→A(2), A→s(8), A→t(0), t→A(8), s→B(5), B→t(7), A→B(6)

Total flow = 8

═══ ITERATION 2 ═══
BFS finds path: s → B → t
Bottleneck = min(5, 7) = 5
Push 5 units: f(s,B)=5, f(B,t)=5
Residual: s→B(0), B→s(5), B→t(2), t→B(5)

Total flow = 8 + 5 = 13

═══ ITERATION 3 ═══
BFS finds path: s → A → B → t  (using remaining capacity)
Bottleneck = min(s→A:2, A→B:6, B→t:2) = 2
Push 2 units: f(s,A)=10, f(A,B)=2, f(B,t)=7

Total flow = 13 + 2 = 15

═══ ITERATION 4 ═══
No more paths from s to t in residual. DONE!

MAXIMUM FLOW = 15 ✅
```

---

## ✂️ Max-Flow Min-Cut Theorem

> **The maximum flow from s to t equals the minimum capacity of any s-t cut.**

### What's a Cut?

An **s-t cut** divides vertices into two groups: S (containing s) and T (containing t). The cut's capacity = sum of capacities of edges going from S to T.

**ELI5**: Imagine CUTTING the graph with scissors somewhere between s and t. The cut's capacity = total capacity of the edges you cut. The MIN cut = the tightest bottleneck.

### The Theorem Says:

The most water you can push (max flow) = the smallest possible bottleneck (min cut).

**Why it matters**: If you find a flow and a cut with the SAME value, you've proven BOTH are optimal!

---

## 🐍 Python Implementation (Edmonds-Karp)

```python
from collections import deque

def edmonds_karp(capacity, s, t, n):
    """
    Find maximum flow using Edmonds-Karp (BFS-based Ford-Fulkerson).
    
    capacity: 2D list where capacity[u][v] = capacity of edge u→v
    s: source, t: sink, n: number of vertices
    """
    # Make a copy for the residual graph
    residual = [row[:] for row in capacity]
    max_flow = 0
    
    while True:
        # BFS to find augmenting path
        parent = [-1] * n
        parent[s] = s
        queue = deque([s])
        
        while queue and parent[t] == -1:
            u = queue.popleft()
            for v in range(n):
                if parent[v] == -1 and residual[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
        
        if parent[t] == -1:
            break  # No more augmenting paths!
        
        # Find bottleneck
        delta = float('inf')
        v = t
        while v != s:
            u = parent[v]
            delta = min(delta, residual[u][v])
            v = u
        
        # Update residual graph
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= delta  # Reduce forward capacity
            residual[v][u] += delta  # Increase backward capacity
            v = u
        
        max_flow += delta
    
    return max_flow

# Example: 4 vertices (0=s, 3=t)
cap = [
    [0, 10, 5, 0],   # s→A=10, s→B=5
    [0, 0, 6, 8],    # A→B=6, A→t=8
    [0, 0, 0, 7],    # B→t=7
    [0, 0, 0, 0],    # t (sink)
]
print(f"Max flow: {edmonds_karp(cap, 0, 3, 4)}")  # 15
```

---

## 📝 Practice Questions with Detailed Solutions

### Q1: Find max flow: s→a(10), s→b(8), a→b(5), a→t(7), b→t(10).

**Solution:**
```
Path 1: s→a→t, bottleneck=min(10,7)=7. Push 7. Total=7.
Path 2: s→b→t, bottleneck=min(8,10)=8. Push 8. Total=15.
Path 3: s→a→b→t, bottleneck=min(10-7=3, 5, 10-8=2)=2. Push 2. Total=17.
No more paths. Max flow = 17 ✅
```

### Q2: Find the min-cut for Q1.

**Solution:** After max flow, BFS on residual from s. Reachable from s = S.
Residual: s→a(1), s→b(0), a→b(3), a→t(0), b→t(0). Back edges: a→s(9), b→s(8), etc.
From s: can reach a (residual s→a=1). From a: can reach b (a→b=3). From b: b→t=0 → can't reach t!
S = {s, a, b}. T = {t}.
Cut edges from S to T: a→t(cap 7) + b→t(cap 10) = **17 = max flow** ✅

### Q3: Multiple sources/sinks — how to handle?

**Solution:** Add **super-source** s' connected to ALL original sources (capacity ∞). Add **super-sink** t' connected FROM all original sinks (capacity ∞). Run max flow on modified network.

### Q4: Why BFS (Edmonds-Karp) instead of DFS?

**Solution:** DFS can take O(E × |f*|) time where |f*| is the max flow value — potentially huge! BFS guarantees O(VE²) because each BFS augmentation uses the SHORTEST path, limiting the total number of augmentations to O(VE).

### Q5: What if there's no path from s to t?

**Solution:** Max flow = **0**. BFS immediately fails to find any path. This means s and t are in disconnected components.

### Q6: Why do backward edges matter?

**Solution:** Without them, you might get stuck. Example: you push flow through a suboptimal path. A backward edge lets a later augmenting path "undo" that choice and reroute the flow through a better path. It's the algorithm's way of correcting mistakes!

### Q7: Verify flow conservation: s→a=9, s→b=8, a→b=2, a→t=7, b→t=10.

**Solution:**
- Node a: in = f(s,a) = 9. Out = f(a,b) + f(a,t) = 2 + 7 = 9. 9=9 ✅
- Node b: in = f(s,b) + f(a,b) = 8 + 2 = 10. Out = f(b,t) = 10. 10=10 ✅
- |f| = out of s = 9+8 = 17 = into t = 7+10 = 17 ✅
- **Valid flow!**

### Q8: Time complexity of Edmonds-Karp?

**Solution:** **O(VE²)**. Each BFS is O(E). Number of augmentations ≤ O(VE) because each augmentation increases the length of the shortest augmenting path, and lengths are bounded.

---

## 📋 Quick Revision Cheat Sheet

```
┌──────────────────────────────────────────────────────┐
│  NETWORK FLOW — EVERYTHING IN ONE BOX                │
├──────────────────────────────────────────────────────┤
│                                                      │
│  FLOW NETWORK: directed graph + capacities + s + t   │
│  FLOW RULES: capacity constraint + conservation      │
│                                                      │
│  RESIDUAL NETWORK:                                   │
│    Forward: room left = c - f                        │
│    Backward: can undo = f                            │
│                                                      │
│  FORD-FULKERSON: find path → push flow → repeat      │
│  EDMONDS-KARP: use BFS → O(VE²) guaranteed           │
│                                                      │
│  MAX-FLOW = MIN-CUT (THE key theorem!)               │
│                                                      │
│  Backward edges allow correcting bad choices!        │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## 📚 References
- [CLRS Chapter 26](https://walkccc.me/CLRS/Chap26/26.1/)
- Lec's 15, 16 — Pr V Raj S
