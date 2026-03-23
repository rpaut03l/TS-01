# ╔══════════════════════════════════════════════════════════╗
# ║  💑 BIPARTITE MAXIMUM MATCHING — Colab Ready             ║
# ╚══════════════════════════════════════════════════════════╝
# STORY: Match students to projects. Max pairs. If stuck,
#        ask a matched person to switch so you can match!
# MNEMONIC: "Try to match. Stuck? Ask matched to switch!"

def max_matching(left, right, edges):
    adj = {u: [] for u in left}
    for u, v in edges:
        adj[u].append(v)
    match_r = {v: None for v in right}

    def try_match(u, visited):
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                if match_r[v] is None or try_match(match_r[v], visited):
                    match_r[v] = u
                    return True
        return False

    count = 0
    for u in left:
        print(f"  Trying to match {u}...")
        if try_match(u, set()):
            count += 1
            print(f"    Matched! Current: {dict((v,u) for v,u in match_r.items() if u)}")
        else:
            print(f"    Could not match {u}")
    return count, {v: u for v, u in match_r.items() if u}

print("="*50)
print("  BIPARTITE MATCHING TEST")
print("="*50)
left = ['Alice','Bob','Charlie','Dana']
right = ['P1','P2','P3','P4']
edges = [('Alice','P1'),('Alice','P3'),('Bob','P2'),
         ('Charlie','P1'),('Charlie','P2'),('Dana','P3'),('Dana','P4')]
count, matching = max_matching(left, right, edges)
print(f"\n  Max matching = {count}")
for project, student in matching.items():
    print(f"    {student} -> {project}")
