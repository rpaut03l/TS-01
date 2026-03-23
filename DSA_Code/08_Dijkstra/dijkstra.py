# ╔══════════════════════════════════════════════════════════════════╗
# ║  🗺️ DIJKSTRA'S ALGORITHM — Complete Code Tutorial (Colab Ready)  ║
# ╚══════════════════════════════════════════════════════════════════╝
#
# 🧒 THE STORY:
# You're at home. You want the CHEAPEST bus route to every place.
# Each road has a cost. Strategy: always visit the CHEAPEST unvisited place.
# From there, check: "Can I reach neighbors cheaper through here?"
#
# 🧠 MNEMONIC: "Dijkstra = always pick the Daintiest (smallest) Distance"
# ⚠️ NO negative weights allowed!

import heapq  # Min-heap: always gives the smallest item first

def dijkstra(graph, source):
    """
    Find shortest paths from source to all vertices.
    
    graph: dict where graph[u] = [(neighbor, weight), ...]
    
    WHAT EACH VARIABLE MEANS:
    - dist[v]   = cheapest known cost to reach v from source
    - parent[v] = which vertex we came from to reach v cheaply
    - heap      = priority queue: (cost, vertex) — smallest cost always on top
    - visited   = set of vertices we've FINALIZED (won't change)
    
    THE KEY OPERATION — RELAXATION:
    "Can I reach v cheaper by going THROUGH u?"
    if dist[u] + weight(u,v) < dist[v]:  → YES! Update!
    """
    # Step 1: Initialize all distances to infinity, source to 0
    dist = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}
    dist[source] = 0
    
    # Step 2: Min-heap with (distance, vertex)
    heap = [(0, source)]    # Source costs 0 to reach
    visited = set()
    
    print(f"  Dijkstra from '{source}':")
    print(f"  Initial distances: {dist}\n")
    
    while heap:
        # Step 3: Get the CHEAPEST unvisited vertex
        d_u, u = heapq.heappop(heap)
        
        if u in visited:
            continue        # Already finalized — skip!
        visited.add(u)      # Finalize this vertex
        
        print(f"  ✅ Finalize '{u}' with distance {d_u}")
        
        # Step 4: RELAX all neighbors
        for v, weight in graph[u]:
            if v not in visited:
                new_dist = dist[u] + weight
                if new_dist < dist[v]:    # Found a SHORTER path!
                    dist[v] = new_dist
                    parent[v] = u
                    heapq.heappush(heap, (new_dist, v))
                    print(f"     Relax {u}→{v}: {dist[u]}+{weight}={new_dist} < old {dist[v] if dist[v] != new_dist else '∞'} → UPDATE!")
    
    return dist, parent

def get_path(parent, target):
    """Reconstruct path by following parent pointers backwards."""
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    return path[::-1]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TEST
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("=" * 60)
print("  DIJKSTRA — Step-by-Step Demo")
print("=" * 60)

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('E', 3)],
    'D': [('B', 5), ('E', 2)],
    'E': [('C', 3), ('D', 2)],
}

dist, parent = dijkstra(graph, 'A')

print(f"\n📊 Final Results:")
print(f"{'Vertex':<8} {'Distance':<10} {'Path'}")
print(f"{'─'*8} {'─'*10} {'─'*20}")
for v in sorted(dist):
    path = get_path(parent, v)
    print(f"{v:<8} {dist[v]:<10} {' → '.join(path)}")


print("""
╔══════════════════════════════════════════════════════╗
║  DIJKSTRA CHEAT SHEET                                ║
╠══════════════════════════════════════════════════════╣
║  1. Init: dist[source]=0, all others=∞               ║
║  2. Loop: extract CHEAPEST from heap                 ║
║  3. For each neighbor: RELAX                         ║
║     if dist[u]+w < dist[v] → update dist[v]          ║
║  4. Repeat until heap empty                          ║
║                                                      ║
║  TIME: O((V+E) log V) with binary heap               ║
║  ⚠️ NO negative weights!                             ║
║  For unweighted → just use BFS (simpler)             ║
║                                                      ║
║  RELAX MNEMONIC: "Can I get there cheaper via you?"  ║
╚══════════════════════════════════════════════════════╝
""")
