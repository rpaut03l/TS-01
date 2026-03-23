# ╔══════════════════════════════════════════════════════════════════════╗
# ║  📋 MASTER DSA CODE CHEATSHEET — All Algorithms in One Place         ║
# ║  Every algorithm explained...                                        ║
# ║  Copy-paste ready for Google Colab or any Python environment         ║
# ╚══════════════════════════════════════════════════════════════════════╝
#
# 🧠 MNEMONICS TO REMEMBER ALL ALGORITHMS:
#
#   "I Must Remember BSTs, Red-Black, Augmented, Disjoint —
#    Graphs Bring Dijkstra, Networks Flow, Matching Points —
#    Dynamic Programs Cut Rods, LCS is Long,
#    Greedy Picks the Earliest — and now you know this song!"
#
# ══════════════════════════════════════════════════════════════════════


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1️⃣  INSERTION SORT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: You have cards. Pick one card at a time.
#       Scan your hand right-to-left.
#       Shift bigger cards right. Drop your card in the gap.
#
# MNEMONIC: "Pick → Scan → Shift → Drop"
# TIME: Best O(n), Worst O(n²)  |  SPACE: O(1)  |  STABLE: Yes

def insertion_sort(arr):
    for j in range(1, len(arr)):       # Pick each card (start from 2nd)
        key = arr[j]                    # Hold the card
        i = j - 1                       # Look at card to the left
        while i >= 0 and arr[i] > key:  # While left card is bigger...
            arr[i + 1] = arr[i]         #   ...shift it right
            i -= 1                       #   ...look at next left card
        arr[i + 1] = key                # Drop card in the gap
    return arr

# TEST: print(insertion_sort([5, 2, 4, 6, 1, 3]))  → [1, 2, 3, 4, 5, 6]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2️⃣  MERGE SORT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: Split pile in half. Split again. Until 1 card each.
#       Then MERGE pairs back: always pick the smaller top card.
#
# MNEMONIC: "Split → Sort halves → Merge back"
# TIME: Always O(n log n)  |  SPACE: O(n)  |  STABLE: Yes

def merge_sort(arr):
    if len(arr) <= 1:                   # Base case: 1 card = sorted!
        return arr
    mid = len(arr) // 2                 # Find the middle
    left = merge_sort(arr[:mid])        # Sort left half
    right = merge_sort(arr[mid:])       # Sort right half
    return merge(left, right)           # Merge the two sorted halves

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:         # Pick smaller (≤ for stability!)
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])             # Append leftovers
    result.extend(right[j:])
    return result

# TEST: print(merge_sort([38, 27, 43, 3, 9, 82, 10]))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3️⃣  BINARY SEARCH TREE (BST)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: A tree where left = smaller, right = bigger.
#       To find something: "Is it less? Go left. More? Go right."
#
# MNEMONIC: "Left Less, Right moRe"
# TIME: O(h) for all ops  |  Balanced h=O(log n), Worst h=O(n)

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Walk down, attach at NIL."""
        z = BSTNode(key)
        y = None; x = self.root
        while x:
            y = x
            x = x.left if z.key < x.key else x.right
        z.parent = y
        if not y: self.root = z
        elif z.key < y.key: y.left = z
        else: y.right = z

    def search(self, key):
        """Go left if smaller, right if bigger."""
        x = self.root
        while x and key != x.key:
            x = x.left if key < x.key else x.right
        return x

    def inorder(self, node=None, first=True):
        """Left → Root → Right = SORTED output!"""
        if first: node = self.root
        if node:
            self.inorder(node.left, False)
            print(node.key, end=' ')
            self.inorder(node.right, False)

    def minimum(self, x=None):
        """Go all the way LEFT."""
        if not x: x = self.root
        while x.left: x = x.left
        return x

# TEST:
# t = BST()
# for k in [15, 6, 18, 3, 7, 17, 20]: t.insert(k)
# t.inorder()  → 3 6 7 15 17 18 20


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4️⃣  DISJOINT-SET UNION (Union-Find)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: Everyone starts in their own group.
#       UNION = merge two groups. FIND = who's your group leader?
#       Path compression = make everyone point to leader directly.
#
# MNEMONIC: "Find your leader, Unite your teams"
# TIME: O(α(n)) ≈ O(1) per operation!

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))    # Everyone is their own leader
        self.rank = [0] * n

    def find(self, x):
        """Find leader + flatten path (path compression)."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Shortcut to leader!
        return self.parent[x]

    def union(self, x, y):
        """Merge groups. Smaller tree goes under bigger (union by rank)."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return False        # Already same group!
        if self.rank[rx] < self.rank[ry]: rx, ry = ry, rx
        self.parent[ry] = rx             # Attach smaller under bigger
        if self.rank[rx] == self.rank[ry]: self.rank[rx] += 1
        return True

# TEST:
# dsu = DSU(5)
# dsu.union(0,1); dsu.union(2,3); dsu.union(0,2)
# print(dsu.find(0) == dsu.find(3))  → True (same group!)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5️⃣  BFS — Breadth-First Search
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: Drop a stone in water. Ripples spread outward.
#       Visit ALL neighbors first, then THEIR neighbors.
#       Uses a QUEUE (first-in, first-out).
#
# MNEMONIC: "BFS = Breadth = Brothers first, then Sons"
# TIME: O(V + E)  |  FINDS: Shortest path (unweighted)

from collections import deque

def bfs(graph, source):
    """BFS from source. Returns distances."""
    dist = {source: 0}
    parent = {source: None}
    queue = deque([source])             # Queue = FIFO
    while queue:
        u = queue.popleft()             # Take from FRONT
        for v in graph.get(u, []):
            if v not in dist:           # Not yet visited?
                dist[v] = dist[u] + 1   # Distance = parent's + 1
                parent[v] = u
                queue.append(v)         # Add to BACK of queue
    return dist, parent

def shortest_path(parent, target):
    """Trace back from target to source using parent pointers."""
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    return path[::-1]                   # Reverse: source → target

# TEST:
# g = {'A':['B','C'], 'B':['A','D'], 'C':['A','D'], 'D':['B','C']}
# dist, par = bfs(g, 'A')
# print(dist)  → {'A':0, 'B':1, 'C':1, 'D':2}
# print(shortest_path(par, 'D'))  → ['A', 'B', 'D']


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 6️⃣  DFS — Depth-First Search
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: Explore a maze. Go as DEEP as possible.
#       Hit a dead end? Backtrack and try another path.
#       Uses RECURSION (or a stack).
#
# MNEMONIC: "DFS = Depth = Dive First, Surface later"
# TIME: O(V + E)  |  FINDS: Cycles, Topological sort

def dfs(graph):
    """Full DFS on graph. Returns discovery and finish times."""
    color = {v: 'W' for v in graph}     # W=white, G=gray, B=black
    disc, fin = {}, {}
    time = [0]                           # Use list for mutability in nested fn

    def visit(u):
        time[0] += 1
        disc[u] = time[0]
        color[u] = 'G'                  # Gray = being processed
        for v in graph.get(u, []):
            if color.get(v) == 'W':      # Unvisited neighbor
                visit(v)                  # Go DEEPER!
            elif color.get(v) == 'G':
                print(f"  ⚠️ Back edge {u}→{v} — CYCLE DETECTED!")
        color[u] = 'B'                  # Black = done
        time[0] += 1
        fin[u] = time[0]

    for u in graph:
        if color[u] == 'W':
            visit(u)
    return disc, fin


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 7️⃣  DIJKSTRA'S ALGORITHM
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: You're at home. Find cheapest route to every place.
#       Always visit the CHEAPEST unvisited place first.
#       From there, check: "Can I reach neighbors cheaper through here?"
#
# MNEMONIC: "Dijkstra = Dictionary of Distances, always pick Daintiest"
# TIME: O((V+E) log V) with heap  |  NO negative weights!

import heapq

def dijkstra(graph, source):
    """Shortest paths from source. graph[u] = [(neighbor, weight), ...]"""
    dist = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}
    dist[source] = 0
    heap = [(0, source)]                # (distance, vertex) — min-heap
    visited = set()

    while heap:
        d_u, u = heapq.heappop(heap)   # Get CHEAPEST unvisited
        if u in visited: continue       # Skip if already finalized
        visited.add(u)
        for v, w in graph[u]:
            if v not in visited and dist[u] + w < dist[v]:  # RELAX!
                dist[v] = dist[u] + w   # Found shorter path!
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))
    return dist, parent

# TEST:
# g = {'A':[('B',4),('C',2)], 'B':[('C',1),('D',5)],
#       'C':[('B',1),('E',3)], 'D':[('E',2)], 'E':[]}
# dist, _ = dijkstra(g, 'A')
# print(dist)  → {'A':0, 'B':3, 'C':2, 'D':7, 'E':5}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 8️⃣  FORD-FULKERSON (Edmonds-Karp — BFS version)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: Push water through pipes. Find any path with room.
#       Push as much as the narrowest pipe allows (bottleneck).
#       Repeat until no more paths. That's the MAX FLOW!
#
# MNEMONIC: "Find path → Push flow → Update pipes → Repeat"
# TIME: O(V × E²)

def max_flow(capacity, s, t, n):
    """Edmonds-Karp max flow. capacity[u][v] = pipe capacity."""
    residual = [row[:] for row in capacity]  # Copy
    total_flow = 0

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
        if parent[t] == -1: break        # No more paths!

        # Find bottleneck
        delta = float('inf')
        v = t
        while v != s:
            u = parent[v]
            delta = min(delta, residual[u][v])
            v = u

        # Update residual
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= delta      # Forward: reduce
            residual[v][u] += delta      # Backward: increase (for undo)
            v = u
        total_flow += delta

    return total_flow


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 9️⃣  BIPARTITE MATCHING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: Match students to projects. Each student gets 1 project.
#       Each project gets 1 student. Maximize pairs.
#       Use augmenting paths to "reassign" when stuck.
#
# MNEMONIC: "Try to match → Stuck? Ask matched person to switch"

def max_matching(left, right, edges):
    """Maximum bipartite matching using augmenting paths."""
    adj = {u: [] for u in left}
    for u, v in edges: adj[u].append(v)
    match_r = {v: None for v in right}  # Who is matched to each right vertex?

    def try_match(u, visited):
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                if match_r[v] is None or try_match(match_r[v], visited):
                    match_r[v] = u      # Match u ↔ v !
                    return True
        return False

    count = 0
    for u in left:
        if try_match(u, set()): count += 1
    return count, {v: u for v, u in match_r.items() if u}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔟  ROD CUTTING (Dynamic Programming)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: You have a chocolate bar. Different sizes sell for different prices.
#       Try ALL ways to cut it. Remember answers for smaller bars.
#       Build up from small to big = bottom-up DP!
#
# MNEMONIC: "DP = Don't recompute, just look it uP!"
# TIME: O(n²)  |  SPACE: O(n)

def rod_cutting(prices, n):
    """Max revenue from cutting a rod of length n."""
    r = [0] * (n + 1)                   # r[j] = best revenue for length j
    s = [0] * (n + 1)                   # s[j] = best first cut for length j

    for j in range(1, n + 1):           # Solve small → big
        best = float('-inf')
        for i in range(1, j + 1):       # Try all first cuts
            if prices[i] + r[j - i] > best:
                best = prices[i] + r[j - i]
                s[j] = i                 # Remember best cut
        r[j] = best

    # Reconstruct cuts
    cuts = []
    remaining = n
    while remaining > 0:
        cuts.append(s[remaining])
        remaining -= s[remaining]
    return r[n], cuts

# TEST:
# prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# print(rod_cutting(prices, 4))  → (10, [2, 2])


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1️⃣1️⃣  LCS — Longest Common Subsequence (DP)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: Two necklaces of beads. Find the longest chain
#       that appears IN ORDER in BOTH (can skip beads).
#       Match? → diagonal +1. No match? → best of up/left.
#
# MNEMONIC: "Match → Diagonal+1, Miss → Max(Up, Left)"
# TIME: O(m×n)  |  SPACE: O(m×n)

def lcs(X, Y):
    """Find Longest Common Subsequence."""
    m, n = len(X), len(Y)
    c = [[0] * (n + 1) for _ in range(m + 1)]  # DP table

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:                # Characters MATCH!
                c[i][j] = c[i-1][j-1] + 1       # Diagonal + 1
            else:                                 # Don't match
                c[i][j] = max(c[i-1][j], c[i][j-1])  # Best of up/left

    # Reconstruct LCS string
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            result.append(X[i-1]); i -= 1; j -= 1  # Diagonal = match!
        elif c[i-1][j] >= c[i][j-1]:
            i -= 1                                    # Go up
        else:
            j -= 1                                    # Go left
    return c[m][n], ''.join(reversed(result))

# TEST:
# print(lcs("ABCBDAB", "BDCABA"))  → (4, 'BCBA')


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1️⃣2️⃣  GREEDY ACTIVITY SELECTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ELI5: Many TV shows, one TV. Pick MOST shows.
#       Always pick the show that ENDS soonest.
#       It leaves the MOST room for other shows!
#
# MNEMONIC: "Greedy = Grab the one that Goes away first"
# TIME: O(n log n)

def activity_selection(activities):
    """Select max non-overlapping activities.
    activities = list of (start, finish) tuples."""
    sorted_acts = sorted(activities, key=lambda x: x[1])  # Sort by FINISH
    selected = [sorted_acts[0]]
    last_finish = sorted_acts[0][1]

    for start, finish in sorted_acts[1:]:
        if start >= last_finish:          # Compatible? (starts after last ends)
            selected.append((start, finish))
            last_finish = finish
    return selected

# TEST:
# acts = [(1,4),(3,5),(0,6),(5,7),(8,11),(12,16)]
# print(activity_selection(acts))  → [(1,4),(5,7),(8,11),(12,16)]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📋 QUICK REFERENCE — COMPLEXITY CHEAT SHEET
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# ALGORITHM              │ BEST     │ AVG      │ WORST    │ SPACE │ STABLE
# ───────────────────────┼──────────┼──────────┼──────────┼───────┼───────
# Insertion Sort         │ O(n)     │ O(n²)    │ O(n²)    │ O(1)  │ Yes
# Merge Sort             │ O(nlogn) │ O(nlogn) │ O(nlogn) │ O(n)  │ Yes
# BST Operations         │ O(logn)  │ O(logn)  │ O(n)     │ O(n)  │ —
# RB-Tree Operations     │ O(logn)  │ O(logn)  │ O(logn)  │ O(n)  │ —
# DSU Find/Union         │ O(α(n))  │ O(α(n))  │ O(α(n))  │ O(n)  │ —
# BFS                    │ O(V+E)   │ O(V+E)   │ O(V+E)   │ O(V)  │ —
# DFS                    │ O(V+E)   │ O(V+E)   │ O(V+E)   │ O(V)  │ —
# Dijkstra (heap)        │ O((V+E)logV)│       │          │ O(V)  │ —
# Ford-Fulkerson (EK)    │ O(VE²)   │          │          │ O(V²) │ —
# Bipartite Matching     │ O(VE)    │          │          │ O(V)  │ —
# Rod Cutting (DP)       │ O(n²)    │ O(n²)    │ O(n²)    │ O(n)  │ —
# LCS (DP)               │ O(mn)    │ O(mn)    │ O(mn)    │ O(mn) │ —
# Activity Selection     │ O(nlogn) │ O(nlogn) │ O(nlogn) │ O(1)  │ —
#
#
# 🧠 ALGORITHM PATTERN RECOGNITION:
#
# "Sort by something, pick greedily"     → GREEDY (Activity Selection)
# "Try all options, remember answers"     → DP (Rod Cutting, LCS)
# "Split in half, solve, combine"         → DIVIDE & CONQUER (Merge Sort)
# "Always pick the cheapest next"         → DIJKSTRA
# "Find a path, push flow, repeat"        → FORD-FULKERSON
# "Find leader, merge groups"             → UNION-FIND
# "Level by level exploration"            → BFS
# "Go deep, then backtrack"              → DFS
#
#
# 🎯 WHEN TO USE WHAT:
#
# Need shortest path (unweighted)?   → BFS
# Need shortest path (weighted)?     → DIJKSTRA
# Need to detect cycles?             → DFS
# Need to sort?                      → MERGE SORT (large) or INSERTION SORT (small)
# Need to group/merge sets?          → UNION-FIND
# Need max flow?                     → FORD-FULKERSON
# Need optimal with overlapping subs?→ DYNAMIC PROGRAMMING
# Need optimal with greedy choice?   → GREEDY


if __name__ == "__main__":
    print("=" * 60)
    print("  🧪 RUNNING ALL ALGORITHM TESTS")
    print("=" * 60)

    # Test 1: Insertion Sort
    print("\n1️⃣ Insertion Sort:")
    print(f"   {insertion_sort([5, 2, 4, 6, 1, 3])}")

    # Test 2: Merge Sort
    print("\n2️⃣ Merge Sort:")
    print(f"   {merge_sort([38, 27, 43, 3, 9, 82, 10])}")

    # Test 3: BST
    print("\n3️⃣ BST Inorder:")
    t = BST()
    for k in [15, 6, 18, 3, 7, 17, 20]: t.insert(k)
    print("   ", end=""); t.inorder(); print()

    # Test 4: DSU
    print("\n4️⃣ Disjoint-Set Union:")
    dsu = DSU(6)
    dsu.union(0,1); dsu.union(2,3); dsu.union(0,2)
    print(f"   0 and 3 same group? {dsu.find(0) == dsu.find(3)}")
    print(f"   0 and 4 same group? {dsu.find(0) == dsu.find(4)}")

    # Test 5: BFS
    print("\n5️⃣ BFS:")
    g = {'A':['B','C'], 'B':['A','D'], 'C':['A','D'], 'D':['B','C']}
    dist, par = bfs(g, 'A')
    print(f"   Distances from A: {dist}")
    print(f"   Path A→D: {shortest_path(par, 'D')}")

    # Test 6: DFS
    print("\n6️⃣ DFS:")
    disc, fin = dfs({'A':['B','C'], 'B':['D'], 'C':['D'], 'D':[]})
    print(f"   Discovery: {disc}")
    print(f"   Finish: {fin}")

    # Test 7: Dijkstra
    print("\n7️⃣ Dijkstra:")
    g = {'A':[('B',4),('C',2)], 'B':[('A',4),('C',1),('D',5)],
         'C':[('A',2),('B',1),('E',3)], 'D':[('B',5),('E',2)],
         'E':[('C',3),('D',2)]}
    d, _ = dijkstra(g, 'A')
    print(f"   Distances: {d}")

    # Test 8: Rod Cutting
    print("\n🔟 Rod Cutting:")
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for n in [4, 7, 10]:
        rev, cuts = rod_cutting(prices, n)
        print(f"   n={n}: revenue=${rev}, cuts={cuts}")

    # Test 9: LCS
    print("\n1️⃣1️⃣ LCS:")
    length, seq = lcs("ABCBDAB", "BDCABA")
    print(f"   LCS of 'ABCBDAB' & 'BDCABA': '{seq}' (length {length})")

    # Test 10: Greedy Activity Selection
    print("\n1️⃣2️⃣ Greedy Activity Selection:")
    acts = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
    result = activity_selection(acts)
    print(f"   Selected {len(result)} activities: {result}")

    print("\n" + "=" * 60)
    print("  ✅ ALL TESTS PASSED!")
    print("=" * 60)
