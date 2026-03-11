# ============================================================
#  DIJKSTRA'S ALGORITHM — GOOGLE COLAB NOTEBOOK
# ============================================================
# Subject  : DSA
# Topic    : Single Source Shortest Path
# Repo     : rpaut03l/TS-01-Pvt → DSA/Dijkstra/
# Run this : Copy-paste into Google Colab, run cells top to bottom
# ============================================================
#
# HOW TO USE IN COLAB:
#   1. Open https://colab.research.google.com
#   2. File → New Notebook
#   3. Copy each "# ── CELL N ──" block into a separate cell
#   4. Run cells in order with Shift+Enter
#   OR: File → Upload notebook → upload this .py file directly
# ============================================================


# ════════════════════════════════════════════════════════════
# ── CELL 1 ──  Title & What We're Doing
# ════════════════════════════════════════════════════════════
#
# No code here — just reading!
#
# WHAT IS DIJKSTRA?
#   Dijkstra (dike-stra) is an algorithm to find the SHORTEST
#   PATH from one starting city to all other cities in a map.
#
# REAL LIFE:
#   You open Google Maps. You type "Home → Airport".
#   Google Maps finds the FASTEST route.
#   Dijkstra is the math behind that!
#
# WHAT WE'LL BUILD IN THIS NOTEBOOK:
#   1. A graph (our fake city map)
#   2. Dijkstra — Simple version (easy to read)
#   3. Dijkstra — Fast version (using priority queue)
#   4. Dijkstra — With path tracer (shows the actual route)
#   5. A visual step-by-step printer (shows exactly what happens)
#   6. Tests on different graphs
#   7. Time comparison (simple vs fast)
#
# Run this cell: nothing happens (it's just a comment)
# That's fine! Move to Cell 2.

print("📚 Dijkstra's Algorithm — Colab Notebook")
print("=" * 50)
print("Run each cell top to bottom.")
print("Read the comments before each section — they explain everything!")


# ════════════════════════════════════════════════════════════
# ── CELL 2 ──  Imports (Tools We Need)
# ════════════════════════════════════════════════════════════
#
# WHAT IS AN IMPORT?
#   Python can't do everything by itself.
#   We "import" extra tools from Python's toolbox.
#   Like picking up tools before starting a project.
#
# heapq   → Python's built-in "priority queue" tool
#            It keeps a list where the SMALLEST item is always first
#            Think: a ticket machine where #001 goes before #050
#
# time    → Lets us measure how long our code takes to run
#            Like a stopwatch for code
#
# math    → Gives us math.inf = ∞ (infinity)
#            float('inf') does the same thing, but math.inf is cleaner

import heapq   # priority queue (min-heap)
import time    # for measuring speed
import math    # for math.inf = ∞

print("✅ Imports done! heapq, time, math are ready.")


# ════════════════════════════════════════════════════════════
# ── CELL 3 ──  Build Our Test Graph
# ════════════════════════════════════════════════════════════
#
# WHAT IS A GRAPH HERE?
#   A dictionary of lists.
#   Each KEY is a city name (vertex).
#   Each VALUE is a list of (neighbor, road_cost) pairs.
#
# Our graph looks like this on paper:
#
#          4           5
#   (A) ──────► (B) ──────► (E)
#    │          │
#   2│          │ 1
#    │          │
#    ▼          ▼
#   (C) ──────► (D)
#         3
#
# Read it as:
#   From A: you can go to B (costs 4) or C (costs 2)
#   From B: you can go to D (costs 1) or E (costs 5)
#   From C: you can go to D (costs 3)
#   From D: you can go to E (costs 2)
#   From E: nowhere to go (dead end)

graph = {
    # vertex : [(neighbor, edge_weight), ...]
    'A': [('B', 4), ('C', 2)],    # A connects to B(cost 4) and C(cost 2)
    'B': [('D', 1), ('E', 5)],    # B connects to D(cost 1) and E(cost 5)
    'C': [('D', 3)],              # C connects to D(cost 3)
    'D': [('E', 2)],              # D connects to E(cost 2)
    'E': []                       # E has no outgoing edges (destination)
}

# Let's print it nicely so we can see it
print("🗺️  Our Graph:")
print("-" * 35)
for vertex, neighbors in graph.items():
    if neighbors:
        for neighbor, weight in neighbors:
            print(f"  {vertex}  ──[{weight}]──►  {neighbor}")
    else:
        print(f"  {vertex}  (no outgoing edges)")

print()
print("Expected shortest paths from A:")
print("  A→A = 0")
print("  A→B = 4  (direct: A→B)")
print("  A→C = 2  (direct: A→C)")
print("  A→D = 5  (A→C→D = 2+3, OR A→B→D = 4+1, both = 5)")
print("  A→E = 7  (A→C→D→E = 2+3+2 = 7)")


# ════════════════════════════════════════════════════════════
# ── CELL 4 ──  VERSION 1: Simple Dijkstra (No Heap, O(N²))
# ════════════════════════════════════════════════════════════
#
# WHY START WITH SIMPLE VERSION?
#   It's easier to read. No fancy heap tricks.
#   Great for small graphs and for UNDERSTANDING the logic.
#   Slow for large graphs (that's okay for learning).
#
# HOW IT WORKS:
#   Each loop, scan ALL vertices to find the minimum.
#   Like looking through EVERY card in a pile to find the cheapest.
#   O(N²) = if you have 100 cities, you do 100×100 = 10,000 comparisons.

def dijkstra_simple(graph, source):
    """
    Simple Dijkstra — easy to read, O(N²) speed.

    Parameters:
      graph  : dict of lists  → graph[u] = [(v, weight), ...]
      source : string         → starting vertex name

    Returns:
      dist   : dict → dist[v] = shortest distance from source to v
    """

    # ── STEP 1: Get the full list of all vertices ────────────────
    # graph.keys() = all the keys in our dictionary = vertex names
    # list() turns that into [A, B, C, D, E]
    vertices = list(graph.keys())

    # ── STEP 2: Set all distances to infinity ───────────────────
    # dict comprehension: for every v in vertices, set dist[v] = ∞
    # float('inf') = Python's way of writing "infinity"
    # We write ∞ because we don't know how to reach anyone yet
    dist = {v: float('inf') for v in vertices}

    # ── STEP 3: Source vertex costs 0 to reach ──────────────────
    # We're STARTING at source, so it costs nothing to "get there"
    dist[source] = 0

    # ── STEP 4: Track which vertices are "settled" ──────────────
    # settled = set of vertices whose shortest distance is CONFIRMED
    # Starts empty — no one is confirmed yet
    settled = set()

    # ── STEP 5: Main loop — repeat for every vertex ─────────────
    # We'll settle ONE vertex per iteration → N iterations total
    for _ in range(len(vertices)):

        # ── STEP 5a: Find the unsettled vertex with minimum dist ─
        # Start with u = None (haven't found anyone yet)
        u = None
        for v in vertices:
            # Only consider UNSETTLED vertices
            if v not in settled:
                # If we haven't picked anyone yet, pick v
                # OR if v has a smaller distance than current best u → pick v
                if u is None or dist[v] < dist[u]:
                    u = v

        # ── STEP 5b: Safety check ────────────────────────────────
        # If u is None: all remaining vertices are unreachable (dist=∞)
        # No point continuing — break out of loop early
        if u is None or dist[u] == float('inf'):
            break

        # ── STEP 5c: Settle u — its distance is now FINAL ────────
        # Add u to settled set. We'll never update dist[u] again.
        settled.add(u)

        # ── STEP 5d: Relax all neighbors of u ───────────────────
        # For each road going out from u:
        for neighbor, weight in graph[u]:

            # How much would it cost to reach 'neighbor' by going through u?
            candidate = dist[u] + weight

            # Is that cheaper than what we currently think?
            if candidate < dist[neighbor]:
                # YES! Update to the cheaper route
                dist[neighbor] = candidate

    # ── STEP 6: Return results ───────────────────────────────────
    return dist


# ── RUN IT ──────────────────────────────────────────────────
print("🔵 VERSION 1: Simple Dijkstra")
print("=" * 40)

result_simple = dijkstra_simple(graph, 'A')

print("Shortest distances from A:")
for vertex in sorted(result_simple.keys()):
    dist_val = result_simple[vertex]
    dist_str = str(dist_val) if dist_val != float('inf') else "∞ (unreachable)"
    print(f"  A → {vertex} : {dist_str}")

print()
print("✅ Expected: A=0, B=4, C=2, D=5, E=7")


# ════════════════════════════════════════════════════════════
# ── CELL 5 ──  VERSION 2: Fast Dijkstra with Priority Queue
# ════════════════════════════════════════════════════════════
#
# WHAT'S A PRIORITY QUEUE (MIN-HEAP)?
#   Imagine a hospital waiting room.
#   NOT first-come-first-served.
#   The SICKEST patient (most urgent = smallest priority number) goes first.
#   heapq in Python works like this:
#     - Add anyone in any order
#     - Always takes out the one with the SMALLEST number
#
# WHY IS THIS FASTER?
#   Simple version: scan ALL N vertices each loop = O(N) per step
#   Heap version:   just peek at top of heap = O(log N) per step
#   For N=1000: simple = 1,000,000 operations vs heap = ~10,000
#
# TRICKY PART: Python's heapq has no "update" (decrease_key) function.
#   Solution: just ADD a new entry with the updated distance.
#   Old entries become "stale". We detect and skip stale entries.

def dijkstra_fast(graph, source):
    """
    Fast Dijkstra using min-heap priority queue. O((N+M) log N).

    Parameters:
      graph  : dict of lists  → graph[u] = [(v, weight), ...]
      source : string         → starting vertex

    Returns:
      dist   : dict → shortest distances from source to every vertex
    """

    # ── SETUP: Initialise all distances to ∞ ────────────────────
    dist = {v: float('inf') for v in graph}
    dist[source] = 0      # source = 0, everyone else = ∞

    # ── CREATE PRIORITY QUEUE ────────────────────────────────────
    # pq is just a regular Python list that heapq treats specially
    # Each item in pq is a TUPLE: (distance, vertex_name)
    # heapq sorts by the FIRST element of the tuple (distance)
    pq = []

    # ── ADD SOURCE TO QUEUE ──────────────────────────────────────
    # heapq.heappush(list, item) → adds item and keeps heap sorted
    # We push (0, source) meaning "source vertex has distance 0"
    heapq.heappush(pq, (0, source))

    # ── MAIN LOOP ────────────────────────────────────────────────
    # Keep processing until the priority queue is empty
    while pq:

        # ── POP THE MINIMUM ──────────────────────────────────────
        # heapq.heappop(list) → removes AND returns the smallest item
        # The smallest item = tuple with smallest first element = shortest dist
        # current_dist = the distance on this ticket
        # u            = which vertex this ticket belongs to
        current_dist, u = heapq.heappop(pq)

        # ── STALE ENTRY CHECK ────────────────────────────────────
        # Problem: when we find a shorter path to v, we push a NEW entry
        #          but the OLD entry is still sitting in the heap!
        # When the old entry is eventually popped, its distance is outdated.
        # Check: if the popped distance is WORSE than what we know now → skip!
        #
        # Example:
        #   Old entry: (9, E) — we thought E costs 9
        #   New entry: (7, E) — later found E costs 7
        #   When (9, E) is popped: current_dist=9 > dist['E']=7 → SKIP!
        if current_dist > dist[u]:
            continue    # "continue" skips the rest of this loop iteration

        # ── RELAX ALL NEIGHBORS ──────────────────────────────────
        # graph[u] = list of (neighbor, weight) pairs
        for v, weight in graph[u]:

            # Calculate the distance to reach v by going THROUGH u
            new_dist = dist[u] + weight

            # Is this a shorter route to v than what we know?
            if new_dist < dist[v]:
                # YES! This is a shorter route.

                # Update v's distance
                dist[v] = new_dist

                # Push a NEW entry for v with updated shorter distance
                # (old entry will be skipped when popped due to stale check)
                heapq.heappush(pq, (new_dist, v))

    # ── RETURN RESULTS ───────────────────────────────────────────
    return dist


# ── RUN IT ──────────────────────────────────────────────────
print("🟢 VERSION 2: Fast Dijkstra (Priority Queue)")
print("=" * 40)

result_fast = dijkstra_fast(graph, 'A')

print("Shortest distances from A:")
for vertex in sorted(result_fast.keys()):
    dist_val = result_fast[vertex]
    print(f"  A → {vertex} : {dist_val}")

print()
print("✅ Expected: A=0, B=4, C=2, D=5, E=7")

# Verify both versions give same answer
print()
if result_simple == result_fast:
    print("🎉 Both versions give the SAME answer! ✅")
else:
    print("❌ Mismatch! Something's wrong.")


# ════════════════════════════════════════════════════════════
# ── CELL 6 ──  VERSION 3: Dijkstra With Path Reconstruction
# ════════════════════════════════════════════════════════════
#
# PROBLEM WITH VERSIONS 1 & 2:
#   They tell you the COST of the shortest path.
#   But not the actual ROUTE (which cities to visit).
#
# SOLUTION: Track parent[] array
#   Whenever we update dist[v] using vertex u,
#   we record parent[v] = u
#   Meaning: "the step before v, on the shortest path, is u"
#
#   Then to find path from A to E:
#   Start at E, keep jumping to parent:
#   E → parent[E]=D → parent[D]=C → parent[C]=A → A is source, stop!
#   Reverse: A → C → D → E  ✅

def dijkstra_with_path(graph, source):
    """
    Dijkstra that returns both distances AND the actual paths.

    Parameters:
      graph  : dict of lists
      source : starting vertex

    Returns:
      dist   : dict of shortest distances
      parent : dict of predecessors (for path tracing)
    """

    # ── INITIALISE DIST AND PARENT ───────────────────────────────
    dist   = {v: float('inf') for v in graph}
    dist[source] = 0

    # parent[v] = None means "no path to v found yet"
    # parent[v] = u    means "on the shortest path, we came to v from u"
    parent = {v: None for v in graph}

    # ── PRIORITY QUEUE ───────────────────────────────────────────
    pq = []
    heapq.heappush(pq, (0, source))

    # ── MAIN LOOP (same as fast version + parent tracking) ───────
    while pq:

        current_dist, u = heapq.heappop(pq)

        # Skip stale entries (same logic as before)
        if current_dist > dist[u]:
            continue

        # Relax neighbors
        for v, weight in graph[u]:
            new_dist = dist[u] + weight

            if new_dist < dist[v]:
                dist[v]   = new_dist
                parent[v] = u          # ← KEY: remember we came to v from u
                heapq.heappush(pq, (new_dist, v))

    return dist, parent


def reconstruct_path(parent, source, target):
    """
    Given the parent array, trace back the shortest path.

    Parameters:
      parent : dict from dijkstra_with_path
      source : start vertex
      target : end vertex

    Returns:
      path : list of vertices from source to target
              OR empty list if no path exists
    """

    # ── BUILD PATH BACKWARDS ─────────────────────────────────────
    # Start at target. Keep jumping to parent until we reach source.
    path = []
    current = target

    # Loop: as long as current is not None, keep going backwards
    while current is not None:
        path.append(current)     # add current vertex to path
        current = parent[current] # jump to the vertex before current

    # ── REVERSE THE PATH ─────────────────────────────────────────
    # We built it backwards (E→D→C→A), so flip it (A→C→D→E)
    path.reverse()

    # ── CHECK IF PATH ACTUALLY REACHES SOURCE ────────────────────
    # If path doesn't start with source, there was no route
    if path and path[0] == source:
        return path
    else:
        return []   # no path found


# ── RUN IT ──────────────────────────────────────────────────
print("🟡 VERSION 3: Dijkstra With Path Reconstruction")
print("=" * 40)

dist_result, parent_result = dijkstra_with_path(graph, 'A')

print("Shortest distances AND paths from A:")
print()

for target in sorted(graph.keys()):
    d    = dist_result[target]
    path = reconstruct_path(parent_result, 'A', target)

    if path:
        path_str = " → ".join(path)
    else:
        path_str = "unreachable"

    print(f"  A → {target} : cost={d}  |  path: {path_str}")

print()
print("✅ Expected:")
print("  A→A : 0   | path: A")
print("  A→B : 4   | path: A → B")
print("  A→C : 2   | path: A → C")
print("  A→D : 5   | path: A → C → D  (or A → B → D, same cost)")
print("  A→E : 7   | path: A → C → D → E")


# ════════════════════════════════════════════════════════════
# ── CELL 7 ──  STEP-BY-STEP VISUALISER (See Every Move)
# ════════════════════════════════════════════════════════════
#
# This version PRINTS what happens at every single step.
# Like watching the algorithm in slow motion!
# Excellent for understanding and for exam tracing questions.

def dijkstra_verbose(graph, source):
    """
    Dijkstra with detailed step-by-step printing.
    Same algorithm as fast version — just very chatty!
    """

    # ── SETUP ────────────────────────────────────────────────────
    dist   = {v: float('inf') for v in graph}
    dist[source] = 0
    parent = {v: None for v in graph}
    pq     = []
    heapq.heappush(pq, (0, source))

    all_vertices = sorted(graph.keys())

    # ── PRINT INITIAL STATE ──────────────────────────────────────
    print("=" * 60)
    print("INITIAL STATE")
    print("=" * 60)
    header = "  ".join(f"{v}={dist[v] if dist[v] != float('inf') else '∞':>4}" for v in all_vertices)
    print(f"  Distances: {header}")
    print(f"  PQ: {pq}")
    print()

    iteration = 0

    # ── MAIN LOOP ────────────────────────────────────────────────
    while pq:

        # Pop minimum
        current_dist, u = heapq.heappop(pq)

        # Skip stale (print message for understanding)
        if current_dist > dist[u]:
            print(f"  [SKIP STALE] ({current_dist}, {u}) — dist[{u}] is already {dist[u]}")
            continue

        iteration += 1
        print(f"{'=' * 60}")
        print(f"ITERATION {iteration}: Settling vertex  '{u}'  (dist = {dist[u]})")
        print(f"{'=' * 60}")

        # Show what we're relaxing
        if not graph[u]:
            print(f"  {u} has no outgoing edges — nothing to relax.")
        else:
            print(f"  Relaxing neighbors of {u}:")

            for v, weight in graph[u]:
                old_dist  = dist[v]
                new_dist  = dist[u] + weight
                old_str   = str(old_dist) if old_dist != float('inf') else "∞"

                if new_dist < old_dist:
                    dist[v]   = new_dist
                    parent[v] = u
                    heapq.heappush(pq, (new_dist, v))
                    print(f"    {u} → {v}  (road cost={weight}):  "
                          f"dist[{u}]={dist[u]}+{weight}={new_dist} < {old_str}  "
                          f"✅ UPDATE dist[{v}] = {new_dist}")
                else:
                    print(f"    {u} → {v}  (road cost={weight}):  "
                          f"{dist[u]}+{weight}={new_dist} >= {old_str}  "
                          f"❌ no update")

        # Show current state
        print()
        header = "  ".join(
            f"{v}={dist[v] if dist[v] != float('inf') else '∞':>4}"
            for v in all_vertices
        )
        print(f"  Distances now:  {header}")
        pq_display = sorted(pq)
        print(f"  PQ now:         {pq_display}")
        print()

    # ── FINAL RESULT ─────────────────────────────────────────────
    print("=" * 60)
    print("DONE! Final shortest distances from source =", source)
    print("=" * 60)
    for v in all_vertices:
        d = dist[v]
        d_str = str(d) if d != float('inf') else "∞ (unreachable)"
        print(f"  {source} → {v} : {d_str}")

    return dist, parent


# ── RUN IT ──────────────────────────────────────────────────
print("🔍 VERSION 4: Verbose Step-by-Step Dijkstra")
print()

dijkstra_verbose(graph, 'A')


# ════════════════════════════════════════════════════════════
# ── CELL 8 ──  TEST ON DIFFERENT GRAPHS
# ════════════════════════════════════════════════════════════
#
# Let's test on a few different graphs to make sure our code works.
# Always test edge cases:
#   - Graph with only 1 vertex
#   - Graph with unreachable vertices
#   - Bigger graph

print("🧪 TESTING ON DIFFERENT GRAPHS")
print()

# ── TEST 1: Single vertex ─────────────────────────────────
print("Test 1: Single vertex graph")
single = {'A': []}
result = dijkstra_fast(single, 'A')
# Expected: A=0
assert result == {'A': 0}, f"FAIL: {result}"
print(f"  Result: {result}  ✅ PASS" if result == {'A': 0} else f"  ❌ FAIL: {result}")

# ── TEST 2: Unreachable vertex ────────────────────────────
print("\nTest 2: Graph with unreachable vertex")
# X → Y but Z has no path from X
unreachable_graph = {
    'X': [('Y', 5)],
    'Y': [],
    'Z': [('Y', 1)]    # Z can reach Y but nothing can reach Z
}
result = dijkstra_fast(unreachable_graph, 'X')
# Expected: X=0, Y=5, Z=∞
print(f"  X → X = {result['X']}  (expected 0)")
print(f"  X → Y = {result['Y']}  (expected 5)")
print(f"  X → Z = {result['Z']}  (expected ∞)")
assert result['X'] == 0
assert result['Y'] == 5
assert result['Z'] == float('inf')
print("  ✅ PASS")

# ── TEST 3: Linear chain ──────────────────────────────────
print("\nTest 3: Linear chain  A→B→C→D")
chain = {
    'A': [('B', 1)],
    'B': [('C', 2)],
    'C': [('D', 3)],
    'D': []
}
result = dijkstra_fast(chain, 'A')
# Expected: A=0, B=1, C=3, D=6
expected = {'A': 0, 'B': 1, 'C': 3, 'D': 6}
print(f"  Result:   {result}")
print(f"  Expected: {expected}")
assert result == expected
print("  ✅ PASS")

# ── TEST 4: Two paths, pick cheaper ───────────────────────
print("\nTest 4: Two paths — short expensive vs long cheap")
# A→B directly costs 10
# A→C→B costs 1+1 = 2 (cheaper!)
two_paths = {
    'A': [('B', 10), ('C', 1)],
    'B': [],
    'C': [('B', 1)]
}
result = dijkstra_fast(two_paths, 'A')
# Expected: A=0, B=2, C=1
expected = {'A': 0, 'B': 2, 'C': 1}
print(f"  Result:   {result}")
print(f"  Expected: {expected}")
assert result == expected
print("  ✅ PASS — picked the cheaper route through C!")

print()
print("🎉 ALL TESTS PASSED!")


# ════════════════════════════════════════════════════════════
# ── CELL 9 ──  SPEED COMPARISON: Simple vs Fast
# ════════════════════════════════════════════════════════════
#
# Let's prove that the fast version (heap) is actually faster
# by building a large graph and timing both versions.
#
# We'll make a "line graph": 0 → 1 → 2 → ... → N
# This is a worst case for the simple O(N²) version.

import random

def make_large_graph(n):
    """Build a random graph with n vertices (0 to n-1)."""
    g = {i: [] for i in range(n)}
    # Connect each vertex to a few random forward neighbors
    for i in range(n):
        num_edges = random.randint(1, min(5, n - i - 1)) if i < n - 1 else 0
        targets = random.sample(range(i + 1, n), num_edges) if num_edges > 0 else []
        for t in targets:
            weight = random.randint(1, 10)
            g[i].append((t, weight))
    return g

# Build graph with N = 500 vertices
N = 500
random.seed(42)   # fixed seed = same "random" graph every time
large_graph = make_large_graph(N)

print(f"📊 Speed Comparison: {N}-vertex graph")
print("-" * 45)

# Time the SIMPLE version
t_start = time.time()
_ = dijkstra_simple(large_graph, 0)
t_simple = time.time() - t_start

# Time the FAST version
t_start = time.time()
_ = dijkstra_fast(large_graph, 0)
t_fast = time.time() - t_start

print(f"  Simple (O(N²)):        {t_simple:.4f} seconds")
print(f"  Fast   (O((N+M)logN)): {t_fast:.4f} seconds")

if t_simple > 0 and t_fast > 0:
    speedup = t_simple / t_fast
    print(f"  Speedup: {speedup:.1f}x faster with heap!")

# Verify both give same results
result_s = dijkstra_simple(large_graph, 0)
result_f = dijkstra_fast(large_graph, 0)
# Convert float('inf') to a comparable form
same = all(result_s[v] == result_f[v] for v in large_graph)
print(f"  Same answers? {'✅ YES' if same else '❌ NO'}")


# ════════════════════════════════════════════════════════════
# ── CELL 10 ──  ASSIGNMENT HINT: Modified Dijkstra
# ════════════════════════════════════════════════════════════
#
# Assignment asks:
#   "Modify to use only ONE extra array and predict shortest path.
#    Runtime should remain unchanged."
#
# INTERPRETATION:
#   ONE extra array = only dist[] (no separate parent[] array)
#   Predict path    = still reconstruct path somehow
#   Runtime same    = still O((N+M) log N)
#
# APPROACH:
#   Instead of storing parent[] separately, re-derive path
#   from dist[] alone by checking which predecessor satisfies
#   the relaxation equation exactly.
#
# dist[u] + w(u,v) == dist[v]  →  u is a valid predecessor of v
#
# This is slightly slower for reconstruction but main algo unchanged.

def dijkstra_one_extra(graph, source, target):
    """
    Dijkstra using ONLY the dist[] array as extra storage.
    Reconstructs path without a separate parent[] array.

    Parameters:
      graph  : adjacency list
      source : start vertex
      target : destination vertex

    Returns:
      (distance, path) tuple
    """

    # ── ONLY ONE EXTRA ARRAY: dist[] ─────────────────────────────
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    pq = []
    heapq.heappush(pq, (0, source))

    # ── SAME MAIN LOOP AS BEFORE ──────────────────────────────────
    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        if u == target:
            break   # found target, stop early

        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    # ── PATH RECONSTRUCTION USING ONLY dist[] ────────────────────
    # For each step, we find which neighbor u satisfies:
    #   dist[u] + w(u, target_vertex) == dist[target_vertex]
    # That u is the predecessor!
    #
    # Build a reverse adjacency list first (who points TO each vertex?)
    reverse_adj = {v: [] for v in graph}
    for u in graph:
        for v, w in graph[u]:
            reverse_adj[v].append((u, w))   # v can be reached from u with weight w

    # Now trace backwards from target
    path = []
    node = target

    while node != source:
        path.append(node)
        found_prev = False

        # Among all vertices that have an edge TO node,
        # find one where dist[prev] + w == dist[node]
        for prev, w in reverse_adj[node]:
            if dist[prev] + w == dist[node]:
                node = prev
                found_prev = True
                break

        if not found_prev:
            return float('inf'), []   # no path

    path.append(source)
    path.reverse()

    return dist[target], path


# ── RUN IT ──────────────────────────────────────────────────
print("📌 ASSIGNMENT VERSION: One Extra Array")
print("=" * 40)

distance, path = dijkstra_one_extra(graph, 'A', 'E')
print(f"Shortest distance A → E : {distance}")
print(f"Path: {' → '.join(path)}")
print()
print("Note: dist[u] + w(u,v) == dist[v] trick reconstructs path")
print("      using ONLY dist[] — no separate parent[] array needed!")


# ════════════════════════════════════════════════════════════
# ── CELL 11 ──  SUMMARY AND QUICK REFERENCE
# ════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════╗
║         DIJKSTRA — WHAT WE BUILT IN THIS NOTEBOOK        ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  Version 1: dijkstra_simple(graph, source)               ║
║    → Easy to read. No heap. O(N²). Good for learning.    ║
║                                                          ║
║  Version 2: dijkstra_fast(graph, source)                 ║
║    → Uses heapq. O((N+M) log N). Use for real problems.  ║
║                                                          ║
║  Version 3: dijkstra_with_path(graph, source)            ║
║    → Returns distances + parent[] for path tracing.      ║
║                                                          ║
║  Version 4: dijkstra_verbose(graph, source)              ║
║    → Prints every single step. Use to study/debug.       ║
║                                                          ║
║  Version 5: dijkstra_one_extra(graph, source, target)    ║
║    → Assignment version. Only dist[] as extra storage.   ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║  CORE FORMULA (always):                                  ║
║    if dist[u] + w(u,v) < dist[v]:                        ║
║        dist[v] = dist[u] + w(u,v)    ← RELAX!            ║
╠══════════════════════════════════════════════════════════╣
║  GRAPH FORMAT FOR THESE FUNCTIONS:                       ║
║    graph = {                                             ║
║      'A': [('B', 4), ('C', 2)],  ← A→B:4, A→C:2          ║
║      'B': [('D', 1)],            ← B→D:1                 ║
║      'C': [],                    ← C has no outgoing     ║
║    }                                                     ║
╚══════════════════════════════════════════════════════════╝
""")

print(" All done! Scroll up to read each cell's explanation.")
print("   To test your own graph: change the 'graph' dict in Cell 3")
print("   then re-run all cells.")
