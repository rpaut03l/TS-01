# ╔══════════════════════════════════════════════════════════════════╗
# ║  🕸️ GRAPHS: BFS & DFS — Complete Code Tutorial (Colab Ready)     ║
# ╚══════════════════════════════════════════════════════════════════╝
#
# 🧒 BFS STORY: Drop a stone in a pond. Ripples spread OUTWARD evenly.
#    Visit ALL neighbors first, then THEIR neighbors. Uses a QUEUE.
#
# 🧒 DFS STORY: Explore a maze. Go as DEEP as possible.
#    Hit a dead end? BACKTRACK. Uses RECURSION (or a stack).
#
# 🧠 BFS MNEMONIC: "Brothers first, Sons later" (breadth = wide)
# 🧠 DFS MNEMONIC: "Dive First, Surface later" (depth = deep)

from collections import deque

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HOW WE STORE A GRAPH: Adjacency List
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# A dictionary where each vertex maps to a list of neighbors.
# Think of it as: "A is connected to B and C" → {'A': ['B', 'C']}

def build_graph(edges, directed=False):
    """Build adjacency list from edge list."""
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        if not directed:
            graph.setdefault(v, []).append(u)
    return graph

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BFS — Breadth-First Search
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def bfs(graph, source):
    """
    BFS from source vertex. Returns distances and parents.
    
    KEY DATA STRUCTURES:
    - dist{}    = how far each vertex is from source (in # of edges)
    - parent{}  = who discovered each vertex (for path reconstruction)
    - queue     = deque of vertices waiting to be explored (FIFO!)
    
    HOW IT WORKS:
    1. Start: source has distance 0. Put it in the queue.
    2. Loop: Take front of queue. Look at ALL its neighbors.
       - If neighbor not visited → set distance, set parent, add to queue.
    3. When queue is empty → done! All reachable vertices found.
    """
    dist = {source: 0}           # Source is distance 0 from itself
    parent = {source: None}      # Source has no parent
    queue = deque([source])      # Start with source in queue
    order = []                   # Track visit order
    
    print(f"  BFS from '{source}':")
    print(f"  Queue: [{source}]")
    
    while queue:
        u = queue.popleft()      # Take from FRONT (FIFO!)
        order.append(u)
        
        for v in graph.get(u, []):
            if v not in dist:     # Not yet discovered?
                dist[v] = dist[u] + 1   # Distance = parent + 1
                parent[v] = u
                queue.append(v)   # Add to BACK of queue
        
        print(f"  Dequeue '{u}' (d={dist[u]}). Neighbors: {graph.get(u,[])}. Queue: {list(queue)}")
    
    print(f"  Visit order: {order}")
    print(f"  Distances: {dist}")
    return dist, parent

def get_shortest_path(parent, target):
    """Trace parent pointers back to source."""
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = parent.get(curr)
    return path[::-1]


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# DFS — Depth-First Search
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def dfs(graph):
    """
    Full DFS. Returns discovery/finish times.
    
    COLORS: W = white (undiscovered), G = gray (in progress), B = black (done)
    
    KEY INSIGHT: If DFS sees a GRAY neighbor → BACK EDGE → CYCLE!
    """
    color = {v: 'W' for v in graph}
    disc, fin = {}, {}
    time = [0]
    has_cycle = [False]
    
    def visit(u, depth=0):
        indent = "  " * (depth + 1)
        time[0] += 1
        disc[u] = time[0]
        color[u] = 'G'
        print(f"{indent}Visit '{u}' (d={disc[u]}, color=GRAY)")
        
        for v in graph.get(u, []):
            if color.get(v) == 'W':
                visit(v, depth + 1)
            elif color.get(v) == 'G':
                print(f"{indent}  ⚠️ Back edge {u}→{v} — CYCLE!")
                has_cycle[0] = True
        
        color[u] = 'B'
        time[0] += 1
        fin[u] = time[0]
        print(f"{indent}Finish '{u}' (f={fin[u]}, color=BLACK)")
    
    print("  DFS:")
    for u in graph:
        if color[u] == 'W':
            visit(u)
    
    print(f"  Discovery: {disc}")
    print(f"  Finish: {fin}")
    if has_cycle[0]:
        print("  🔴 Graph has a CYCLE!")
    else:
        print("  🟢 Graph is ACYCLIC")
        topo = sorted(fin, key=lambda v: fin[v], reverse=True)
        print(f"  Topological sort: {topo}")
    
    return disc, fin


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TEST EVERYTHING!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("=" * 60)
print("  UNDIRECTED GRAPH: BFS")
print("=" * 60)
g = build_graph([('A','B'), ('A','C'), ('B','D'), ('C','D'), ('D','E')])
print(f"  Graph: {g}\n")
dist, parent = bfs(g, 'A')
path = get_shortest_path(parent, 'E')
print(f"\n  Shortest path A→E: {' → '.join(path)} (distance {dist['E']})")

print("\n" + "=" * 60)
print("  UNDIRECTED GRAPH: DFS")
print("=" * 60)
dfs(g)

print("\n" + "=" * 60)
print("  DIRECTED GRAPH: DFS (Cycle Detection)")
print("=" * 60)
dg = build_graph([('A','B'), ('B','C'), ('C','A'), ('B','D')], directed=True)
print(f"  Graph: {dg}\n")
dfs(dg)

print("\n" + "=" * 60)
print("  DAG: Topological Sort")
print("=" * 60)
dag = build_graph([('A','C'), ('B','C'), ('B','D'), ('C','D')], directed=True)
dag.setdefault('D', [])  # Ensure D is in the graph
print(f"  Graph: {dag}\n")
dfs(dag)


print("""
╔══════════════════════════════════════════════════════╗
║  BFS / DFS CHEAT SHEET                               ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  BFS:  Queue (FIFO) → level-by-level → shortest path ║
║  DFS:  Stack/Recursion → go deep → cycles, topo sort ║
║  BOTH: O(V + E) time                                 ║
║                                                      ║
║  BFS finds shortest path (unweighted graphs)         ║
║  DFS back edge (to GRAY) = CYCLE                     ║
║  DFS reverse finish order = topological sort         ║
║                                                      ║
║  BFS MNEMONIC: "Brothers first, Sons later"          ║
║  DFS MNEMONIC: "Dive First, Surface later"           ║
╚══════════════════════════════════════════════════════╝
""")
