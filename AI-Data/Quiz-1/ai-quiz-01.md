# 🎯 AI SEARCH TECHNIQUES - Master Cheat Sheet

> **Ultimate Quick Reference for AI Quiz Preparation**  
> *20-Minute Quiz | MCQs + MSQs + One-Liners*

---

## 📚 Table of Contents

- [Top 25 Must-Know Facts](#top-25-must-know-facts)
- [Essential Formulas](#essential-formulas)
- [Algorithm Comparison Table](#algorithm-comparison-table)
- [Heuristic Properties](#heuristic-properties)
- [Common Traps & Mistakes](#common-traps--mistakes)
- [MCQ Practice Questions](#mcq-practice-questions)
- [MSQ Practice Questions](#msq-practice-questions)
- [One-Liner Questions](#one-liner-questions)
- [Pattern Recognition Guide](#pattern-recognition-guide)
- [Exam Strategy](#exam-strategy)
- [Quick Reference Cards](#quick-reference-cards)

---

## 🔥 Top 25 Must-Know Facts

[↑ Back to Top](#-table-of-contents)

### Data Structures
1. **BFS** → Queue (FIFO)
2. **DFS** → Stack (LIFO)
3. **UCS** → Priority Queue (by cost)
4. **A*** → Priority Queue (by f(n) = g(n) + h(n))

### Algorithm Properties
5. **IDS Space**: O(bd) ⭐ **BEST SPACE COMPLEXITY**
6. **UCS**: ALWAYS optimal (no conditions)
7. **BFS**: Optimal ONLY for uniform cost
8. **DFS**: NOT complete (infinite loops)
9. **A* Optimal**: Only if h is admissible

### Heuristics
10. **Admissible**: h(n) ≤ h*(n)
11. **Consistent**: h(n) ≤ c(n,a,n') + h(n')
12. **Relationship**: Consistent → Admissible (NOT reverse!)
13. **Goal Heuristic**: h(goal) = 0 ALWAYS
14. **Dominance**: h₂ dominates h₁ if h₂(n) ≥ h₁(n) for all n

### Search Properties
15. **Greedy**: Uses h(n) only (NOT optimal)
16. **Manhattan Distance**: |x₁-x₂| + |y₁-y₂|
17. **Euclidean Distance**: √[(x₁-x₂)² + (y₁-y₂)²]

### Local Search
18. **Simulated Annealing**: P = e^(-ΔE/T)
19. **Hill Climbing**: Stuck at Local maxima, Ridges, Plateaux (LRP)
20. **GA Process**: GERMS (Generate, Evaluate, Reproduce, Mutate, Select)
21. **Roulette Wheel**: P(i) = fitness(i) / Σfitness

### Adversarial Search
22. **Alpha-Beta**: Prune when α ≥ β
23. **AND nodes**: SUM of children
24. **OR nodes**: MIN of children
25. **IDA***: IDS with f-cost cutoff

---

## 📐 Essential Formulas

[↑ Back to Top](#-table-of-contents)

### A* and Search
```
f(n) = g(n) + h(n)
where:
  g(n) = actual cost from start to n
  h(n) = estimated cost from n to goal
  f(n) = estimated total cost
```

### Heuristic Conditions
```
Admissible:  h(n) ≤ h*(n)  for all n
Consistent:  h(n) ≤ c(n,a,n') + h(n')  for all n, a, n'
Goal:        h(goal) = 0
```

### Distance Metrics
```
Manhattan:   d = |x₁ - x₂| + |y₁ - y₂|
Euclidean:   d = √[(x₁-x₂)² + (y₁-y₂)²]
```

### Local Search
```
Simulated Annealing:  P = e^(-ΔE/T)
GA Selection:         P(i) = fitness(i) / Σfitness
Expected Count:       EC = P(i) × population_size
```

### Complexity
```
BFS Time:   O(b^d)
BFS Space:  O(b^d)
DFS Space:  O(bm)
IDS Space:  O(bd)  ⭐ BEST
```

---

## 📊 Algorithm Comparison Table

[↑ Back to Top](#-table-of-contents)

| Algorithm | Data Structure | Complete | Optimal | Time | Space | Notes |
|-----------|---------------|----------|---------|------|-------|-------|
| **BFS** | Queue | ✅ Yes | ⚠️ Uniform cost only | O(b^d) | O(b^d) | Level-by-level |
| **DFS** | Stack | ❌ No | ❌ No | O(b^m) | O(bm) | Can loop infinitely |
| **UCS** | PQ (cost) | ✅ Yes | ✅ Always | O(b^d) | O(b^d) | Expands cheapest first |
| **IDS** | Stack | ✅ Yes | ⚠️ Uniform cost only | O(b^d) | O(bd) ⭐ | Best space! |
| **Greedy** | PQ (h) | ❌ No | ❌ No | O(b^m) | O(b^m) | h(n) only |
| **A*** | PQ (f) | ✅ Yes | ⚠️ If h admissible | O(b^d) | O(b^d) | f(n)=g(n)+h(n) |
| **IDA*** | Stack | ✅ Yes | ⚠️ If h admissible | O(b^d) | O(bd) ⭐ | Memory-bounded A* |

**Legend:**
- b = branching factor
- d = depth of solution
- m = maximum depth
- PQ = Priority Queue

---

## 🎯 Heuristic Properties

[↑ Back to Top](#-table-of-contents)

### Admissible Heuristic
```
Definition: h(n) ≤ h*(n) for all n
Meaning:    Never overestimates actual cost
Property:   Optimistic
Guarantee:  A* finds optimal solution
Example:    Straight-line distance for road navigation
```

### Consistent (Monotone) Heuristic
```
Definition: h(n) ≤ c(n,a,n') + h(n') for all n, a, n'
Meaning:    Triangle inequality satisfied
Property:   Values non-decreasing along paths
Guarantee:  Admissible + never re-opens nodes
```

### Key Relationships
```
Consistent → Admissible  ✅ (always true)
Admissible → Consistent  ❌ (not always)

Consistent is STRONGER condition
Admissible is WEAKER condition
```

### Dominance
```
h₂ dominates h₁ if: h₂(n) ≥ h₁(n) for all n

If both admissible:
  h₂ is better (more informed)
  A* with h₂ expands fewer nodes
```

---

## ⚠️ Common Traps & Mistakes

[↑ Back to Top](#-table-of-contents)

| ❌ WRONG STATEMENT | ✅ CORRECT ANSWER |
|-------------------|-------------------|
| "BFS is always optimal" | BFS optimal ONLY for uniform cost |
| "Admissible → Consistent" | NO! Consistent → Admissible (one-way) |
| "DFS has best space so use it" | DFS NOT complete (can loop infinitely) |
| "Higher h is always better" | NO! Must satisfy h ≤ h* (admissible) |
| "IDS wastes time re-expanding" | Only 11% overhead, saves exponential space |
| "AND nodes take minimum" | AND = SUM, OR = MIN |
| "Greedy is optimal if h is good" | Greedy NEVER optimal (ignores g(n)) |
| "A* always finds optimal" | Only if h is admissible |
| "UCS needs admissible heuristic" | NO! UCS has no heuristic |
| "Alpha-Beta changes minimax result" | NO! Same result, just prunes nodes |

---

## 📝 MCQ Practice Questions

[↑ Back to Top](#-table-of-contents)

### Section 1: Algorithm Properties

**Q1. Which search algorithm is ALWAYS optimal?**
- A) BFS
- B) DFS
- C) UCS ✅
- D) Greedy

**Q2. Space complexity of IDS?**
- A) O(b^d)
- B) O(bd) ✅
- C) O(bm)
- D) O(d)

**Q3. Which is TRUE about heuristics?**
- A) Admissible → Consistent
- B) Consistent → Admissible ✅
- C) Both equivalent
- D) Neither implies other

**Q4. DFS is NOT:**
- A) Memory efficient
- B) Complete ✅
- C) Uses stack
- D) Capable of backtracking

**Q5. A* evaluation function:**
- A) f(n) = g(n) - h(n)
- B) f(n) = g(n) + h(n) ✅
- C) f(n) = h(n)
- D) f(n) = g(n)

### Section 2: Complexity

**Q6. BFS time complexity:**
- A) O(bd)
- B) O(bm)
- C) O(b^d) ✅
- D) O(d^b)

**Q7. Which has BEST space complexity?**
- A) BFS
- B) UCS
- C) IDS ✅
- D) A*

**Q8. DFS space complexity:**
- A) O(b^d)
- B) O(bd)
- C) O(bm) ✅
- D) O(d)

### Section 3: Local Search

**Q9. Hill climbing gets stuck at:**
- A) Global maxima only
- B) Local maxima, ridges, plateaux ✅
- C) Goal states
- D) Initial states

**Q10. SA acceptance probability:**
- A) e^(T/ΔE)
- B) e^(-ΔE/T) ✅
- C) T/ΔE
- D) ΔE/T

### Section 4: Adversarial Search

**Q11. In minimax, MIN nodes choose:**
- A) Maximum value
- B) Minimum value ✅
- C) Average value
- D) Random value

**Q12. Alpha-beta pruning when:**
- A) α < β
- B) α = β
- C) α ≥ β ✅
- D) α ≤ β

**Q13. AND nodes calculate:**
- A) Minimum of children
- B) Maximum of children
- C) Sum of children ✅
- D) Average of children

### Section 5: Heuristics

**Q14. Admissible heuristic:**
- A) Overestimates
- B) Never overestimates ✅
- C) Always exact
- D) Can be negative

**Q15. h(goal) must be:**
- A) Maximum
- B) Zero ✅
- C) Greater than zero
- D) Less than zero

---

## 🎯 MSQ Practice Questions

[↑ Back to Top](#-table-of-contents)

### MSQ1: BFS Properties (Select all TRUE)
- A) Uses FIFO queue ✅
- B) Always optimal
- C) Complete ✅
- D) Space O(b^d) ✅
- E) Uses stack

**Answer: A, C, D**

---

### MSQ2: Admissible Heuristics (Select all TRUE)
- A) h(n) ≤ h*(n) ✅
- B) h(n) ≥ 0 ✅
- C) h(goal) = 0 ✅
- D) h(n) can be negative
- E) h(n) overestimates

**Answer: A, B, C**

---

### MSQ3: Complete Algorithms (Select all)
- A) BFS ✅
- B) DFS
- C) UCS ✅
- D) IDS ✅
- E) Greedy

**Answer: A, C, D**

---

### MSQ4: A* Optimality (Select all required)
- A) h(n) admissible ✅
- B) All costs ≥ ε > 0 ✅
- C) h(n) consistent
- D) Tree-search
- E) h(n) = 0

**Answer: A, B**

---

### MSQ5: Hill Climbing Issues (Select all)
- A) Local maxima ✅
- B) Ridges ✅
- C) Plateaux ✅
- D) Global maxima
- E) Initial state

**Answer: A, B, C**

---

### MSQ6: Priority Queue Users (Select all)
- A) BFS
- B) UCS ✅
- C) A* ✅
- D) DFS
- E) Greedy ✅

**Answer: B, C, E**

---

### MSQ7: IDS Properties (Select all TRUE)
- A) Complete ✅
- B) Space O(bd) ✅
- C) Optimal for uniform cost ✅
- D) Uses queue
- E) Best space ✅

**Answer: A, B, C, E**

---

### MSQ8: Consistent Heuristic (Select all TRUE)
- A) Admissible ✅
- B) h(n) ≤ c+h(n') ✅
- C) Triangle inequality ✅
- D) Overestimates
- E) Monotonic ✅

**Answer: A, B, C, E**

---

### MSQ9: AND-OR Trees (Select all TRUE)
- A) AND nodes sum children ✅
- B) OR nodes take minimum ✅
- C) Non-deterministic actions ✅
- D) AND nodes minimum
- E) OR nodes sum

**Answer: A, B, C**

---

### MSQ10: Alpha-Beta Pruning (Select all TRUE)
- A) Reduces nodes ✅
- B) Maintains correctness ✅
- C) Prunes when α ≥ β ✅
- D) Changes result
- E) Can double depth ✅

**Answer: A, B, C, E**

---

## 📋 One-Liner Questions

[↑ Back to Top](#-table-of-contents)

### Definitions

**Q1. Define search in AI**  
**A:** Computational method for exploring state spaces to find goal states from initial states via actions.

**Q2. What is a heuristic function?**  
**A:** Estimated cost h(n) from node n to nearest goal state.

**Q3. Define admissible heuristic**  
**A:** h(n) ≤ h*(n) for all n (never overestimates actual cost).

**Q4. Define consistent heuristic**  
**A:** h(n) ≤ c(n,a,n') + h(n') for all nodes and actions (triangle inequality).

**Q5. What is branching factor?**  
**A:** Maximum number of successors any node can have (b).

---

### Formulas

**Q6. Write A* evaluation function**  
**A:** f(n) = g(n) + h(n)

**Q7. Write Manhattan distance formula**  
**A:** d = |x₁ - x₂| + |y₁ - y₂|

**Q8. Write SA acceptance probability**  
**A:** P = e^(-ΔE/T)

**Q9. Write admissibility condition**  
**A:** h(n) ≤ h*(n)

**Q10. Write consistency condition**  
**A:** h(n) ≤ c(n,a,n') + h(n')

---

### Complexity

**Q11. BFS time complexity?**  
**A:** O(b^d)

**Q12. IDS space complexity?**  
**A:** O(bd)

**Q13. DFS space complexity?**  
**A:** O(bm)

**Q14. UCS time complexity?**  
**A:** O(b^d)

**Q15. A* space complexity?**  
**A:** O(b^d)

---

### True/False

**Q16. BFS is always optimal**  
**A:** False - only optimal for uniform cost.

**Q17. DFS is complete**  
**A:** False - can loop infinitely in infinite spaces.

**Q18. UCS is always optimal**  
**A:** True - when transition costs ≥ ε > 0.

**Q19. Consistent implies admissible**  
**A:** True - consistency is stronger condition.

**Q20. Admissible implies consistent**  
**A:** False - admissibility is weaker.

**Q21. IDS has best space**  
**A:** True - O(bd) vs O(b^d) for BFS.

**Q22. Greedy is optimal**  
**A:** False - ignores path cost g(n).

**Q23. A* is complete**  
**A:** True - when h admissible and costs ≥ ε > 0.

**Q24. Hill climbing finds global optimum**  
**A:** False - gets stuck at local optima.

**Q25. Alpha-beta changes minimax**  
**A:** False - same result, just prunes nodes.

---

### Comparisons

**Q26. BFS vs DFS space?**  
**A:** BFS: O(b^d), DFS: O(bm) - DFS better.

**Q27. BFS vs UCS optimality?**  
**A:** BFS: uniform cost only, UCS: always.

**Q28. A* vs Greedy?**  
**A:** A*: f=g+h optimal, Greedy: h only not optimal.

**Q29. IDS vs BFS space?**  
**A:** IDS: O(bd), BFS: O(b^d) - IDS exponentially better.

**Q30. Admissible vs Consistent?**  
**A:** Consistent → Admissible (stronger → weaker).

---

### Data Structures

**Q31. BFS data structure?**  
**A:** FIFO Queue

**Q32. DFS data structure?**  
**A:** LIFO Stack

**Q33. UCS data structure?**  
**A:** Priority queue by g(n)

**Q34. A* data structure?**  
**A:** Priority queue by f(n)

**Q35. Greedy data structure?**  
**A:** Priority queue by h(n)

---

### Problem-Specific

**Q36. Romania heuristic?**  
**A:** Straight-line distance to Bucharest.

**Q37. Water jug state?**  
**A:** (gal3, gal4) tuple.

**Q38. Optimal Arad→Bucharest cost?**  
**A:** 418 km (via Sibiu→Rimnicu→Pitesti)

**Q39. Why straight-line admissible?**  
**A:** Roads cannot be shorter than straight line.

**Q40. 8-puzzle heuristics?**  
**A:** Manhattan distance, misplaced tiles.

---

## 🔍 Pattern Recognition Guide

[↑ Back to Top](#-table-of-contents)

### Instant Recognition

| You See | Think | Answer Involves |
|---------|-------|----------------|
| "Queue" | BFS | FIFO, level-by-level |
| "Stack" | DFS | LIFO, depth-first |
| "Priority Queue + cost" | UCS | Always optimal |
| "Priority Queue + f(n)" | A* | g(n) + h(n) |
| "h(n) ≤ h*(n)" | Admissible | Never overestimate |
| "Triangle inequality" | Consistent | h(n) ≤ c+h(n') |
| "Temperature" | SA | e^(-ΔE/T) |
| "Population" | GA | Crossover, mutation |
| "α, β" | Alpha-Beta | Prune when α≥β |
| "AND/OR" | Non-deterministic | AND=SUM, OR=MIN |
| "Best space" | IDS | O(bd) |
| "Always optimal" | UCS | (or A* with admissible h) |
| "Uniform cost only" | BFS | Not always optimal |
| "Local optima" | Hill Climbing | Gets stuck |

---

## 🎓 Exam Strategy

[↑ Back to Top](#-table-of-contents)

### Time Management (20 Minutes)

**First 2 Minutes:**
1. ✅ Scan all questions
2. ✅ Mark easy (✓), tricky (?), calculation (calc)

**Next 12 Minutes:**
1. ✅ Answer all easy questions
2. ✅ Do calculations
3. ✅ Leave tricky for last

**Final 6 Minutes:**
1. ✅ Tackle tricky questions
2. ✅ Review MSQs carefully
3. ✅ Quick verification

### Time Allocation
- **MCQs:** 30 seconds each
- **MSQs:** 45 seconds each
- **One-liners:** 20 seconds each

### MSQ Strategy
- ✅ Read ALL options first
- ✅ Watch for "True about" vs "False about"
- ✅ Be conservative if negative marking
- ✅ Select all you're confident about if no penalty

---

## 💳 Quick Reference Cards

[↑ Back to Top](#-table-of-contents)

### Card 1: Essential Formulas
```
f(n) = g(n) + h(n)           [A* formula]
h(n) ≤ h*(n)                 [Admissible]
h(n) ≤ c(n,a,n') + h(n')     [Consistent]
d = |x₁-x₂| + |y₁-y₂|        [Manhattan]
P = e^(-ΔE/T)                [SA]
P(i) = fitness(i)/Σfitness   [GA]
```

### Card 2: Algorithm Selection
```
Need optimal?
  With heuristic → A* (if h admissible)
  No heuristic → UCS
  
Need complete?
  BFS, UCS, IDS, A* ✅
  DFS ❌
  
Limited space?
  IDS (O(bd)) ⭐
```

### Card 3: Critical Rules
```
1. Consistent → Admissible (NOT reverse!)
2. UCS always optimal
3. BFS optimal only for uniform cost
4. DFS NOT complete
5. IDS best space: O(bd)
6. AND = SUM, OR = MIN
7. Prune when α ≥ β
8. h(goal) = 0 always
```

### Card 4: Data Structures
```
BFS    → Queue
DFS    → Stack
UCS    → Priority Queue (cost)
A*     → Priority Queue (f=g+h)
Greedy → Priority Queue (h)
```

### Card 5: Complexity Ladder
```
Space (Best to Worst):
IDS:  O(bd)  ⭐⭐⭐⭐⭐
DFS:  O(bm)  ⭐⭐⭐⭐
BFS:  O(b^d) ⭐

Time:
All similar: O(b^d) approximately
```

---

## 🚨 Last-Minute Checklist

[↑ Back to Top](#-table-of-contents)

### 15-Second Memory Drill

Can you answer these instantly?

1. **f(n) = ?** → g(n) + h(n)
2. **IDS space?** → O(bd)
3. **UCS optimal?** → Always
4. **BFS optimal?** → Uniform cost only
5. **Consistent → ?** → Admissible
6. **Admissible → ?** → Not necessarily consistent
7. **DFS complete?** → No
8. **AND nodes?** → SUM
9. **OR nodes?** → MIN
10. **h(goal)?** → 0
11. **Prune when?** → α ≥ β
12. **SA formula?** → e^(-ΔE/T)
13. **Manhattan?** → |x₁-x₂| + |y₁-y₂|
14. **Best space?** → IDS
15. **Greedy optimal?** → No

**Score 15/15? YOU'RE READY! 🎉**

---

## 📞 Quick Links

[↑ Back to Top](#-table-of-contents)

### Jump to Section
- [Top 25 Facts](#top-25-must-know-facts)
- [Formulas](#essential-formulas)
- [Algorithm Table](#algorithm-comparison-table)
- [Common Traps](#common-traps--mistakes)
- [MCQ Practice](#mcq-practice-questions)
- [MSQ Practice](#msq-practice-questions)
- [One-Liners](#one-liner-questions)
- [Exam Strategy](#exam-strategy)

---

## ⚡ Power Moves

[↑ Back to Top](#-table-of-contents)

### If You Forget Everything Else, Remember:

1. **f(n) = g(n) + h(n)** ← Write this first
2. **Consistent → Admissible** ← Not the other way!
3. **IDS space = O(bd)** ← The space hero
4. **UCS is always optimal** ← No conditions
5. **AND=SUM, OR=MIN** ← Don't mix them up!
6. **BFS optimal only for uniform cost** ← Not always!
7. **DFS not complete** ← Can loop infinitely
8. **h(goal) = 0** ← Always true
9. **Prune when α ≥ β** ← Alpha-beta condition
10. **Greedy never optimal** ← Ignores g(n)

---

## 🌟 Final Words

[↑ Back to Top](#-table-of-contents)

**You've got this!**

✅ You've reviewed the material  
✅ You know the formulas  
✅ You understand the traps  
✅ You're prepared  

**Now go ace that quiz!** 🚀

---

## 📄 Document Info

**Created:** For AI Search Quiz Preparation  
**Format:** Markdown with navigation  
**Coverage:** Slides 1-86  
**Quiz Type:** MCQs + MSQs + One-Liners  
**Duration:** 20 minutes  

**Version:** 1.0  
**Last Updated:** Quiz Day  

---

**Made with ❤️ for quiz success**

[⬆️ Back to Top](#-ai-search-techniques---master-cheat-sheet)
