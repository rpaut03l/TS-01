# 🚨 20-MINUTE AI QUIZ SURVIVAL CARD 🚨

> **Last-minute cramming guide for AI Search Techniques Quiz**  
> *Print this. Keep it visible. Save your grade.*

---

## 🎯 TOP 25 MUST-KNOW FACTS

### Data Structures & Algorithms
1. **BFS** → Queue (FIFO)
2. **DFS** → Stack (LIFO)
3. **UCS** → Priority Queue (by cost)
4. **IDS** → Stack (iterative depth limits)

### A* and Heuristics
5. **A* Formula**: `f(n) = g(n) + h(n)`
   - g(n) = actual cost from start
   - h(n) = estimated cost to goal
6. **Admissible**: `h(n) ≤ h*(n)` (never overestimate)
7. **Consistent**: `h(n) ≤ c(n,a,n') + h(n')` (triangle inequality)
8. **Key Relationship**: Consistent → Admissible (ALWAYS TRUE)
9. **Heuristic Dominance**: h₂ dominates h₁ if `h₂(n) ≥ h₁(n)` for all n
10. **Goal Heuristic**: `h(goal) = 0` ALWAYS

### Algorithm Properties
11. **IDS Space**: O(bd) ⭐ **BEST SPACE COMPLEXITY**
12. **UCS**: ALWAYS optimal (no conditions needed)
13. **BFS**: Optimal ONLY for uniform cost
14. **DFS**: NOT complete (can loop infinitely)
15. **Greedy**: Uses h(n) only (NOT optimal)

### Distance Metrics
16. **Manhattan Distance**: `|x₁ - x₂| + |y₁ - y₂|`
17. **Euclidean Distance**: `√[(x₁-x₂)² + (y₁-y₂)²]`

### Local Search
18. **Simulated Annealing**: `P = e^(ΔE/T)`
   - Accept worse solution with this probability
   - High T → explore, Low T → exploit
19. **Hill Climbing**: Gets stuck at Local maxima, Ridges, Plateaux (LRP)
20. **GA Process**: GERMS
   - **G**enerate initial population
   - **E**valuate fitness
   - **R**eproduce (crossover)
   - **M**utate
   - **S**elect next generation
21. **Roulette Wheel Selection**: `P(i) = fitness(i) / Σfitness`

### Adversarial & Non-deterministic Search
22. **Alpha-Beta Pruning**: Prune when `α ≥ β`
   - α-cutoff at MAX nodes
   - β-cutoff at MIN nodes
23. **AND-OR Trees**:
   - AND nodes = SUM of children
   - OR nodes = MIN of children
24. **Minimax**: MAX chooses max, MIN chooses min

### Memory-Bounded Search
25. **IDA***: IDS with f-cost cutoff (instead of depth)

---

## 🧠 ESSENTIAL MNEMONICS

### SAGI-H (Search Problem Components)
- **S**tate space
- **A**ctions
- **G**oal test
- **I**nitial state
- **H**euristics

### BUD-DI (Uninformed Search)
- **B**readth-first
- **U**niform-cost
- **D**epth-first
- **D**epth-limited
- **I**terative deepening

### HiSaGa (Local Search)
- **Hi**ll climbing
- **Sa**（Simulated Annealing)
- **Ga**（Genetic Algorithms)

### ACORN (Heuristic Properties)
- **A**dmissible
- **C**onsistent
- **O**ptimistic (never overestimate)
- **R**easonable (computable)
- **N**on-negative

### LRP (Hill Climbing Problems)
- **L**ocal maxima
- **R**idges
- **P**lateaux

### GERMS (Genetic Algorithm Steps)
- **G**enerate
- **E**valuate
- **R**eproduce
- **M**utate
- **S**elect

---

## ⚠️ COMMON TRAPS (Read This 3 Times!)

| ❌ WRONG STATEMENT | ✅ CORRECT ANSWER |
|-------------------|-------------------|
| "BFS is always optimal" | BFS optimal ONLY for uniform cost |
| "Admissible → Consistent" | NO! Consistent → Admissible (one-way) |
| "DFS has best space so use it" | DFS NOT complete (infinite loops) |
| "Higher h is always better" | NO! Must satisfy h ≤ h* (admissible) |
| "IDS wastes time re-expanding" | Only 11% overhead, saves exponential space |
| "AND nodes take minimum" | AND = SUM, OR = MIN |
| "Greedy is optimal if h is good" | Greedy NEVER optimal (ignores g(n)) |
| "A* always finds optimal" | Only if h is admissible |
| "UCS needs admissible heuristic" | NO! UCS has no heuristic |
| "Alpha-Beta changes minimax result" | NO! Just prunes, same result |

---

## 📊 ALGORITHM COMPARISON TABLE

| Algorithm | Complete? | Optimal? | Time | Space | Notes |
|-----------|-----------|----------|------|-------|-------|
| **BFS** | ✅ Yes | ⚠️ Uniform cost only | O(b^d) | O(b^d) | Queue (FIFO) |
| **UCS** | ✅ Yes | ✅ Yes | O(b^d) | O(b^d) | Priority queue by cost |
| **DFS** | ❌ No | ❌ No | O(b^m) | O(bm) | Stack (LIFO) |
| **DLS** | ⚠️ If d≤l | ❌ No | O(b^l) | O(bl) | Depth limit l |
| **IDS** | ✅ Yes | ⚠️ Uniform cost only | O(b^d) | O(bd) ⭐ | Best space! |
| **Greedy** | ❌ No | ❌ No | O(b^m) | O(b^m) | Uses h(n) only |
| **A*** | ✅ Yes | ✅ If h admissible | O(b^d) | O(b^d) | f(n)=g(n)+h(n) |
| **IDA*** | ✅ Yes | ✅ If h admissible | O(b^d) | O(bd) | A* + IDS |

*b = branching factor, d = solution depth, m = max depth*

---

## 🎓 QUICK FORMULA REFERENCE

### Search Costs
```
f(n) = g(n) + h(n)     [A* evaluation function]
g(n) = path cost so far [known, exact]
h(n) = estimated cost to goal [heuristic]
```

### Heuristic Properties
```
Admissible:   h(n) ≤ h*(n)
Consistent:   h(n) ≤ c(n,a,n') + h(n')
Goal:         h(goal) = 0
```

### Distance Metrics
```
Manhattan:    d = |x₁-x₂| + |y₁-y₂|
Euclidean:    d = √[(x₁-x₂)² + (y₁-y₂)²]
```

### Local Search
```
SA Acceptance:     P = e^(ΔE/T)
GA Selection:      P(i) = fitness(i) / Σfitness
Expected Count:    EC = P(i) × population_size
```

### Complexity
```
BFS/UCS time:      O(b^d)
BFS/UCS space:     O(b^d)
DFS space:         O(bm)    [MUCH BETTER!]
IDS space:         O(bd)    [BEST OF BOTH!]
```

---

## 🔥 LAST-MINUTE CRAMMING STRATEGY

### 5 Minutes Before Quiz:
1. ✅ Read "Common Traps" section 3 times
2. ✅ Memorize: f(n) = g(n) + h(n)
3. ✅ Remember: Consistent → Admissible (one way only!)
4. ✅ Know: IDS space = O(bd) is the hero
5. ✅ Recall: AND=SUM, OR=MIN

### During Quiz:
1. **See "optimal"?** → Check if UCS or A* with admissible h
2. **See "space complexity"?** → IDS wins at O(bd)
3. **See "admissible"?** → Check h(n) ≤ h*(n)
4. **See "complete"?** → DFS is the only common one that's NOT
5. **See "BFS optimal"?** → Only if uniform cost!

---

## 💡 QUICK DECISION TREE

```
Need optimal solution?
  ├─ Yes → Need heuristic?
  │   ├─ Yes → A* (if h admissible)
  │   └─ No → UCS
  └─ No → Limited space?
      ├─ Yes → IDS (complete) or DFS (not complete)
      └─ No → BFS (uniform cost) or Greedy (fast but not optimal)
```

---

## 🎯 PROBLEM-SOLVING CHECKLIST

When answering questions, ask yourself:

- [ ] **Is the cost uniform?** (BFS vs UCS distinction)
- [ ] **Is the heuristic admissible?** (A* optimality)
- [ ] **Is there a space constraint?** (IDS advantage)
- [ ] **Are there cycles?** (DFS danger zone)
- [ ] **Is it asking about time or space?** (Very different answers!)
- [ ] **Is the question about theory or implementation?** (Data structures!)

---

## 📝 SAMPLE QUESTION PATTERNS

### Pattern 1: "Which is optimal?"
**Answer Strategy**: 
- UCS → Always optimal
- BFS → Only if uniform cost
- A* → Only if h is admissible
- DFS/Greedy → Never optimal

### Pattern 2: "Best space complexity?"
**Answer**: IDS at O(bd) beats everything

### Pattern 3: "Is this heuristic admissible?"
**Check**: Does h(n) ≤ h*(n) for ALL n? (Never overestimate?)

### Pattern 4: "Complete or not?"
**Remember**: DFS is the common one that's NOT complete

### Pattern 5: "Difference between X and Y?"
- BFS vs UCS: Uniform cost vs any cost
- Admissible vs Consistent: h≤h* vs triangle inequality
- Greedy vs A*: h(n) only vs g(n)+h(n)

---

## ⚡ POWER MOVES

### If You Forget Everything Else:
1. **f(n) = g(n) + h(n)** ← Write this first
2. **Consistent → Admissible** ← Not the other way!
3. **IDS space = O(bd)** ← The space hero
4. **UCS is always optimal** ← No conditions
5. **AND=SUM, OR=MIN** ← Don't mix them up!

### Time-Saving Recognition:
- Queue → BFS
- Stack → DFS
- Priority Queue → UCS or A*
- f(n) appears → A* or IDA*
- Only h(n) → Greedy
- Temperature → Simulated Annealing
- Population → Genetic Algorithm
- α, β → Alpha-Beta Pruning

---

## 🚀 CONFIDENCE BOOSTERS

**You know this if you can answer:**
1. What's the A* formula? → `f(n) = g(n) + h(n)` ✓
2. Which has best space? → IDS at O(bd) ✓
3. Is BFS always optimal? → No, only uniform cost ✓
4. Admissible means? → `h(n) ≤ h*(n)` ✓
5. AND nodes calculate? → SUM of children ✓

**If you got 5/5: You're ready! 🎉**

---

## 📚 ONE-LINER DEFINITIONS

**BFS**: Explore level by level (Queue)  
**DFS**: Explore deep first (Stack)  
**UCS**: Expand cheapest first (Priority Queue)  
**IDS**: DFS with increasing depth limits  
**Greedy**: Expand node with lowest h(n)  
**A***: Expand node with lowest f(n) = g(n) + h(n)  
**IDA***: IDS using f-cost cutoffs  
**Hill Climbing**: Move to best neighbor  
**SA**: Hill climbing that accepts worse moves  
**GA**: Evolution-inspired population search  
**Minimax**: Assume opponent plays optimally  
**Alpha-Beta**: Minimax with pruning  

---

## 🎨 VISUAL MEMORY AIDS

### A* Formula Triangle:
```
      f(n)
     /    \
  g(n)    h(n)
 [past]  [future]
```

### Heuristic Relationship:
```
Consistent ──→ Admissible
    ✓            ✓
    (stronger)   (weaker)
```

### Search Space Complexity:
```
Small ←──────────────────→ Large
IDS(bd) < DFS(bm) < BFS(b^d)
  ⭐        OK         💀
```

### Algorithm Selection Spectrum:
```
Optimal ←───────────→ Fast
  UCS      A*    Greedy   DFS
   ✓       ✓      ✗       ✗
```

---

## 🔑 KEY INSIGHTS

### Why IDS is Amazing:
- Combines BFS completeness + DFS space efficiency
- Only 11% time overhead vs BFS
- Saves exponential space: O(bd) vs O(b^d)

### Why Consistency Matters:
- Consistent → Admissible (always)
- Ensures A* never re-opens nodes
- Makes A* more efficient

### Why Greedy Fails:
- Ignores g(n) completely
- Can be led astray by optimistic heuristic
- Example: Short-looking path that costs a lot

### Why UCS Always Works:
- No heuristic needed
- Explores in cost order
- First path to goal is optimal (if costs ≥ ε)

---

## 📞 EMERGENCY HOTLINES

**Forgot algorithm properties?**  
→ Check Algorithm Comparison Table

**Confused about heuristics?**  
→ Remember: Admissible = never overestimate = h ≤ h*

**Mixed up data structures?**  
→ BFS=Queue, DFS=Stack, UCS=Priority Queue

**Can't decide between algorithms?**  
→ Use Quick Decision Tree

**Question seems like a trap?**  
→ Check Common Traps section

---

## 🎯 FINAL CHECKLIST

Before submitting quiz:

- [ ] Did I check if BFS is "always optimal"? (It's not!)
- [ ] Did I verify heuristic admissibility when needed?
- [ ] Did I choose IDS for space-optimal questions?
- [ ] Did I remember UCS is always optimal?
- [ ] Did I avoid mixing up AND (SUM) and OR (MIN)?
- [ ] Did I write f(n) = g(n) + h(n) correctly?
- [ ] Did I check the question for trick words? (always, never, only)

---

## 💪 YOU'VE GOT THIS!

**Remember:**
- Trust your preparation
- Read questions carefully (watch for "always" and "only")
- Sketch small examples if stuck
- Check common traps list
- You know more than you think!

---

> **🌟 Pro Tip**: Take a deep breath. You've studied this. Trust your knowledge. Good luck! 🌟

---

*Last updated: Before your quiz*  
*Difficulty survived: All of them*  
*Confidence level: MAXIMUM* 🚀

---

## 📖 APPENDIX: QUICK REFERENCE TABLES

### Complete vs Optimal Summary
| Algorithm | Complete | Optimal | When Optimal |
|-----------|----------|---------|--------------|
| BFS | ✅ | ⚠️ | Uniform cost only |
| UCS | ✅ | ✅ | Always |
| DFS | ❌ | ❌ | Never |
| IDS | ✅ | ⚠️ | Uniform cost only |
| A* | ✅ | ⚠️ | If h admissible |
| Greedy | ❌ | ❌ | Never |

### Space Complexity Ranking
```
1. IDS:        O(bd)    ⭐⭐⭐⭐⭐
2. DFS:        O(bm)    ⭐⭐⭐⭐
3. A*/UCS/BFS: O(b^d)   ⭐
```

### When to Use What
- **Need optimal + have heuristic** → A*
- **Need optimal + no heuristic** → UCS
- **Need complete + tight space** → IDS
- **Large space + approximate OK** → Local search
- **Two-player game** → Minimax/Alpha-Beta
- **Uncertainty in actions** → AND-OR search

---

**END OF SURVIVAL CARD**

