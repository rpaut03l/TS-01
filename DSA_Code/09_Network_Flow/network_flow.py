# ╔══════════════════════════════════════════════════════════╗
# ║  🚰 NETWORK FLOW (Ford-Fulkerson/Edmonds-Karp)           ║
# ╚══════════════════════════════════════════════════════════╝
# STORY: Push water through pipes. Find path→push→repeat!
# MNEMONIC: "Find path → Push flow → Update pipes → Repeat"

from collections import deque

def max_flow(capacity, s, t, n):
    residual = [row[:] for row in capacity]
    total = 0
    while True:
        parent = [-1]*n; parent[s]=s
        q = deque([s])
        while q and parent[t]==-1:
            u = q.popleft()
            for v in range(n):
                if parent[v]==-1 and residual[u][v]>0:
                    parent[v]=u; q.append(v)
        if parent[t]==-1: break
        delta=float('inf'); v=t
        while v!=s: delta=min(delta,residual[parent[v]][v]); v=parent[v]
        v=t
        while v!=s:
            u=parent[v]; residual[u][v]-=delta; residual[v][u]+=delta; v=u
        total+=delta
        print(f"  Push {delta} units. Total flow = {total}")
    return total

print("="*50)
print("  MAX FLOW TEST")
print("="*50)
cap=[[0,10,5,0],[0,0,6,8],[0,0,0,7],[0,0,0,0]]
print(f"  Max flow = {max_flow(cap,0,3,4)}")
