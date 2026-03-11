# 🗺️ Dijkstra's Algorithm — Complete Study Hub

> **Subject:** DSA | **Topic:** Single Source Shortest Path  
> **Repo:** `rpaut03l/TS-01-Pvt` → `DSA/Dijkstra/`

---

## 📂 What's In Here

| File | What You'll Learn |
|------|------------------|
| [📚 dijkstra_theory.md](theory/dijkstra_theory.md) | All concepts, notation, proofs, cheatsheet, viva Q&A |
| [🔢 dijkstra_numericals.md](numericals/dijkstra_numericals.md) | Worked examples, trace tables, path reconstruction |
| [🧩 dijkstra_pseudocode.md](pseudocode/dijkstra_pseudocode.md) | Every pseudocode line explained like you're 10 years old |
| [💻 dijkstra_practice.md](practice/dijkstra_practice.md) | Python implementations + practice problems |
| [🚀 dijkstra_colab.py](practice/dijkstra_colab.py) | Run directly in Google Colab — 5 versions, every line commented |

---

## 🧠 30-Second Summary

```
PROBLEM:  Shortest path from ONE source to ALL other vertices.
ANSWER:   Dijkstra's Algorithm.

One sentence: "Always visit the nearest unvisited city,
               then update estimates for its neighbors."

Constraint:   All edge weights ≥ 0  (no negatives!)
Complexity:   O((N + M) log N)  with priority queue
```

---

## 🔑 The 3 Big Ideas

```
1. INITIALISE     dist[source]=0,  everyone else = ∞

2. GREEDY PICK    Always settle the vertex with MINIMUM dist

3. RELAX          if dist[u] + w(u,v) < dist[v]  →  update dist[v]

Repeat 2 & 3 until PQ empty = Dijkstra!
```

---

## ⚡ Ultra Cheatsheet

```
┌────────────────────────────────────────────────────────────┐
│  dist[s]=0 | dist[v]=∞ | PQ = MinHeap with (0, s)          │
│                                                            │
│  while PQ not empty:                                       │
│      (d, u) = PQ.extract_min()                             │
│      if d > dist[u]: continue        ← skip stale          │
│      for (v, w) in adj[u]:                                 │
│          if dist[u]+w < dist[v]:                           │
│              dist[v] = dist[u]+w                           │
│              PQ.push( (dist[v], v) )                       │
│                                                            │
│  Complexity: O((N+M) log N)                                │
│  Works only: all w(e) ≥ 0                                  │
│  Negatives?: Bellman-Ford                                  │
└────────────────────────────────────────────────────────────┘
```

---

## 🗂️ GitHub Structure

```
DSA/
└── Dijkstra/
    ├── dijkstra_hub.md              ← YOU ARE HERE (Hub)
    ├── theory/
    │   └── dijkstra_theory.md       ← Concepts, notation, proofs, viva Q&A
    ├── numericals/
    │   └── dijkstra_numericals.md   ← Worked examples + trace tables
    ├── pseudocode/
    │   └── dijkstra_pseudocode.md   ← Every pseudocode line explained simply
    └── practice/
        ├── dijkstra_practice.md     ← Practice problems + Python overview
        └── dijkstra_colab.py        ← 🚀 Run directly in Google Colab!
```

---

## 📌 Start Here Based on Your Goal

| I want to... | Go to... |
|--------------|----------|
| Understand from scratch | [📚 Theory](theory/dijkstra_theory.md) |
| Understand pseudocode line-by-line | [🧩 Pseudocode](pseudocode/dijkstra_pseudocode.md) |
| Solve a numerical / trace table | [🔢 Numericals](numericals/dijkstra_numericals.md) |
| Run and test code in Colab | [🚀 dijkstra_colab.py](practice/dijkstra_colab.py) |
| Viva prep Q&A | [Theory → Q&A section](theory/dijkstra_theory.md#14-qa-viva-prep) |

---

[⬆️ Back to Top](#️-dijkstras-algorithm--complete-study-hub)

---
*DSA/ → Dijkstra/ → dijkstra_hub.md | rpaut03l/TS-01-Pvt*
