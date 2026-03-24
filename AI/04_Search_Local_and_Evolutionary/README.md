# 🏔️ Topic 04 — Local Search & Evolutionary Search

> **Difficulty**: 🟡 Medium | **Syllabus Section**: Search
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐

---

## 🍼 Explain Like I'm 5 (ELI5)

All the searches we learned before were about finding a **PATH** from start to goal. But sometimes we don't care about the path — we just want to find the **BEST answer**!

Imagine you're blindfolded on a hilly field and want to reach the TOP of the TALLEST hill:
- **Hill Climbing** = Feel the ground around you, take a step in whichever direction goes UP. Keep going until every direction goes DOWN. You're at a peak!
- **Simulated Annealing** = Same, but sometimes you purposely step DOWNHILL (take a bad move) hoping it leads to an even TALLER hill later. Like "getting worse before getting better"!
- **Genetic Algorithm** = You send 100 blindfolded friends onto the field. The ones at higher spots get to "breed" and create children who start near them. Over generations, everyone drifts toward the tallest hills!

---

## 📚 Table of Contents

1. [Why Local Search?](#1-why-local-search)
2. [Hill Climbing](#2-hill-climbing)
3. [Problems with Hill Climbing](#3-problems-with-hill-climbing)
4. [Hill Climbing Variants](#4-hill-climbing-variants)
5. [Simulated Annealing](#5-simulated-annealing)
6. [Local Beam Search](#6-local-beam-search)
7. [Genetic Algorithms](#7-genetic-algorithms)
8. [Comparison Table](#8-comparison-table)
9. [Key Takeaways](#9-key-takeaways)
10. [Exam Tips](#10-exam-tips)

---

## 1. Why Local Search?

### When Path Doesn't Matter

Some problems don't care HOW you got to the answer — they only care about the answer itself:

| Problem | What We Want | Path Needed? |
|---|---|---|
| **8-Queens** | Place 8 queens so none attack each other | ❌ Just the final arrangement |
| **Traveling Salesman** | Shortest tour visiting all cities | ❌ Just the tour |
| **Job Scheduling** | Schedule that minimizes completion time | ❌ Just the schedule |
| **Protein Folding** | Lowest energy configuration | ❌ Just the shape |

### Local Search Characteristics

- **No search tree** — just one (or a few) current state(s)
- **No explored set** — don't track where you've been
- **Very little memory** — usually O(1) or O(k) for k states
- **Can find solutions in infinite/continuous state spaces**
- **Not complete** (might miss the solution)
- **Not optimal** (might find a "good enough" solution)

### The Landscape Metaphor

Think of the state space as a **landscape** where:
- **Height** = quality of the state (higher = better)
- **Location** = the state itself
- **Our goal** = reach the highest peak (**global maximum**)

```
                        ★ Global Maximum
                       /|\
                      / | \
    Local            /  |  \
    Maximum         /   |   \
     /\            /    |    \
    /  \          /     |     \
   /    \        /      |      \
  /      \      /       |       \    Shoulder
_/   Flat  \___/        |        \___/\___
    Local                                  \
    Minimum (valley)                        \
```

---

## 2. Hill Climbing

### The Algorithm (Steepest Ascent Version)

```
function HILL_CLIMBING(problem):
    current = problem.initial_state
    
    loop:
        neighbor = the highest-valued successor of current
        if neighbor.value ≤ current.value:
            return current              ← Stuck! No improvement possible
        current = neighbor              ← Move to better neighbor
```

> 🍼 **ELI5**: Stand somewhere. Look at all nearby spots. Move to the HIGHEST one. Repeat. When every nearby spot is LOWER than where you are, stop — you're on a hilltop!

### Step-by-Step: 8-Queens Example

**State**: A configuration of 8 queens on an 8×8 board
**Heuristic h**: Number of pairs of queens attacking each other (LOWER is better — we minimize)
**Neighbor**: Move one queen within its column

```
Initial state (h = 17 attacking pairs):
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
Q . . . . . . .
. . . . . . . Q
. . . . Q . . .
. . . . . Q . .

After several hill-climbing steps (h = 1):
. . . . . Q . .
. . . Q . . . .
. Q . . . . . .
. . . . . . . Q
. . . . Q . . .
. . Q . . . . .
Q . . . . . . .
. . . . . . Q .    ← Almost there! But stuck with 1 conflict
```

---

## 3. Problems with Hill Climbing

### 3.1 Local Maxima

```
     ★ Global Max (but we can't see it!)
     |
     |      /\  ← We're stuck HERE (local max)
     |     /  \
     |    /    \
     |   /      \
_____|__/        \____________
```

**Problem**: We're at a peak, but it's NOT the highest. Every neighbor is lower, so we stop — but there's a better answer we missed!

### 3.2 Ridges (Plateaus)

```
_________________________________________
         ← Every step is FLAT (same value)
         Hill climbing doesn't know which way to go!
```

**Problem**: The landscape is flat. No neighbor is better, so we stop. But the actual peak might be at the other end of the plateau!

### 3.3 Shoulders

A ridge that slopes slightly — you can navigate it, but it's slow and confusing.

### How Bad Is It?

For the **8-Queens problem** (random initial state):
- Hill climbing gets **stuck 86% of the time**
- When it works (14%), it averages only **4 steps**
- When stuck, it takes **3 steps** on average before stopping
- With **random restarts**, we can solve it reliably (see below)!

---

## 4. Hill Climbing Variants

### 4.1 Stochastic Hill Climbing

Instead of always picking the BEST neighbor, pick randomly from uphill neighbors (weighted by steepness).

> 🍼 **ELI5**: Instead of always climbing the steepest slope, sometimes take a less steep path. This helps avoid getting trapped on narrow ridges!

### 4.2 First-Choice Hill Climbing

Generate neighbors one at a time, randomly. Accept the FIRST one that's better than current.

Good when there are too many neighbors to evaluate all of them.

### 4.3 Random-Restart Hill Climbing

**The silver bullet for local maxima!**

```
function RANDOM_RESTART_HC(problem):
    loop:
        result = HILL_CLIMBING(problem, random_initial_state())
        if result is good enough: return result
```

> 🍼 **ELI5**: If you're stuck on a small hill, just teleport to a RANDOM location and start climbing again! Do this enough times and you'll eventually land near the tallest hill!

**For 8-Queens:**
- Each attempt succeeds with probability ~14%
- Expected number of attempts = 1/0.14 ≈ **7 restarts**
- Expected steps = 7 × (4 success steps + 3 failure steps) ≈ **22 steps total**
- **Solves 8-Queens very efficiently!**

### 4.4 Sideways Moves

Allow moves to neighbors of **equal** value (not just better). This helps escape **shoulders/plateaus**.

But be careful! Infinite sideways moves = infinite loop on flat plateaus. Set a **limit** (e.g., 100 consecutive sideways moves before giving up).

---

## 5. Simulated Annealing

### The Inspiration: Metallurgy

In metalworking, **annealing** means heating metal and then SLOWLY cooling it. At high temperatures, atoms bounce around randomly (exploring many configurations). As it cools, atoms settle into a low-energy crystal structure (finding the optimal arrangement).

### The Algorithm

```
function SIMULATED_ANNEALING(problem, schedule):
    current = problem.initial_state
    
    for t = 1, 2, 3, ...:
        T = schedule(t)                    ← Temperature at time t
        if T == 0: return current          ← Frozen! Return result
        
        next = a randomly selected neighbor of current
        ΔE = value(next) - value(current)  ← Change in quality
        
        if ΔE > 0:                         ← Better? Always accept!
            current = next
        else:                              ← Worse? Accept with probability:
            accept with probability e^(ΔE/T)
```

### The Key Formula: Acceptance Probability

```
P(accept worse move) = e^(ΔE/T)

where ΔE = value(next) - value(current) < 0 (it's worse)
      T = current temperature (decreases over time)
```

### 🧮 How to Calculate e^(ΔE/T) — Step by Step!

Many students see e^(ΔE/T) and panic. Let's break it down!

**What is e?** It's Euler's number ≈ 2.71828. It's a special math constant (like π = 3.14159).

**How to compute e^x?** Use a calculator, or know that:
- e^0 = 1
- e^(-1) ≈ 0.368
- e^(-2) ≈ 0.135
- e^(-5) ≈ 0.007
- e^(-10) ≈ 0.0000454

**The rule**: As x gets MORE negative, e^x gets CLOSER to 0 (but never reaches 0).

#### Full Worked Examples

**Example 1: High temperature, small drop**
```
Current value = 50, Next value = 45, T = 100
ΔE = 45 - 50 = -5  (the move is 5 units WORSE)

P = e^(ΔE/T) = e^(-5/100) = e^(-0.05) ≈ 0.951

Result: 95.1% chance of accepting! "I'm hot and adventurous — sure, let's try it!"
```

**Example 2: Medium temperature, medium drop**
```
Current value = 50, Next value = 45, T = 10
ΔE = 45 - 50 = -5

P = e^(ΔE/T) = e^(-5/10) = e^(-0.5) ≈ 0.607

Result: 60.7% chance. "Hmm, it's worse, but there's a decent chance I'll try it."
```

**Example 3: Low temperature, medium drop**
```
Current value = 50, Next value = 45, T = 1
ΔE = 45 - 50 = -5

P = e^(ΔE/T) = e^(-5/1) = e^(-5) ≈ 0.0067

Result: Only 0.67% chance! "I'm cold and picky — almost certainly NOT accepting this."
```

**Example 4: Any temperature, BIG drop**
```
Current value = 50, Next value = 10, T = 10
ΔE = 10 - 50 = -40  (MUCH worse!)

P = e^(ΔE/T) = e^(-40/10) = e^(-4) ≈ 0.018

Result: Only 1.8% chance, even at medium temperature. "That's WAY worse — nope!"
```

### The Pattern (Memorize This!)

| What Happens | Temperature (T) | ΔE (quality drop) | Probability | Behavior |
|---|---|---|---|---|
| Early search | HIGH (100) | Small (-5) | e^(-5/100) = **0.95** | Accept almost everything! EXPLORE! |
| Early search | HIGH (100) | Big (-40) | e^(-40/100) = **0.67** | Still accept often — adventurous |
| Mid search | MEDIUM (10) | Small (-5) | e^(-5/10) = **0.61** | Maybe accept, maybe not |
| Mid search | MEDIUM (10) | Big (-40) | e^(-40/10) = **0.02** | Rarely accept big drops |
| Late search | LOW (1) | Small (-5) | e^(-5/1) = **0.007** | Almost never accept — EXPLOIT! |
| Late search | LOW (1) | Big (-40) | e^(-40/1) ≈ **0.0000** | Essentially never — frozen! |

### Two Key Insights

**Insight 1: Higher T → more likely to accept bad moves** (more exploration)
**Insight 2: Bigger drop → less likely to accept** (even at high T, a TERRIBLE move is usually rejected)

> 🍼 **Super Simple Kid Version**: 
> - **Hot** = You're a wild toddler who puts EVERYTHING in your mouth (explore all options!)
> - **Warm** = You're a curious kid who tries new foods but says no to really weird ones
> - **Cold** = You're a picky adult who only eats your favorite foods (exploit what works!)
> - **Frozen** = You're a grandpa who eats the EXACT same meal every day (completely stuck with current best)

### The Cooling Schedule

The function `schedule(t)` that determines how T decreases over time:

```
Common schedules:
- Linear:      T(t) = T₀ - αt          (T decreases by constant amount)
- Geometric:   T(t) = T₀ × α^t         (T decreases by constant ratio, e.g., α=0.99)
- Logarithmic: T(t) = T₀ / ln(1 + t)   (Very slow cooling — theoretical optimum)
```

**The rule**: If you cool slowly enough, simulated annealing will find the global optimum with probability approaching 1. But "slowly enough" might mean waiting until the heat death of the universe!

### Properties

| Property | Value |
|---|---|
| **Complete?** | ✅ Theoretically (if cooled infinitely slowly) |
| **Optimal?** | ✅ Theoretically (if cooled infinitely slowly) |
| **Practical** | Very good at finding near-optimal solutions |
| **Memory** | O(1) — stores only current state! |

---

## 6. Local Beam Search

### The Idea

Keep track of **k states** instead of just 1. At each step, generate ALL successors of ALL k states, then keep the **best k** overall.

> 🍼 **ELI5**: Send 10 kids to explore a playground. Each kid finds nearby fun spots. Then ALL kids compare notes, and the 10 who found the best spots continue. The others are "teleported" to help the winners explore further!

```
function LOCAL_BEAM_SEARCH(problem, k):
    states = k randomly generated states
    
    loop:
        all_successors = []
        for each state in states:
            all_successors.append(successors of state)
        
        if any successor is goal: return it
        states = best k states from all_successors
```

### Key Difference from Random Restarts

| Random Restart Hill Climbing | Local Beam Search |
|---|---|
| k independent searches in parallel | k searches that **share information** |
| Each search is completely separate | Useful states attract more search effort |
| Like sending 10 people to 10 separate mazes | Like sending 10 people into ONE maze where they can shout to each other |

### Problem: Diversity Loss

All k states might cluster together on the same hill! You lose diversity.

**Solution**: **Stochastic Beam Search** — instead of picking the best k, pick k states randomly, with probability proportional to quality. This maintains diversity!

---

## 7. Genetic Algorithms

### The Inspiration: Natural Evolution

In nature, the fittest organisms survive and reproduce, passing their genes to offspring. Over many generations, the population evolves toward better solutions!

### Key Vocabulary

| Term | Meaning | ELI5 |
|---|---|---|
| **Individual** | One solution (a state) | One creature |
| **Population** | Set of individuals | The whole herd |
| **Chromosome** | Encoding of the individual (often a string) | The creature's DNA |
| **Gene** | One element of the chromosome | One letter of DNA |
| **Fitness Function** | How good an individual is | How strong/fast the creature is |
| **Selection** | Choosing parents for breeding | Only the best get to have babies |
| **Crossover** | Combining two parents to make a child | Baby gets half DNA from each parent |
| **Mutation** | Random change in a gene | Rare DNA copying errors |

### The Algorithm

```
function GENETIC_ALGORITHM(population, fitness):
    loop:
        new_population = []
        
        for i = 1 to size(population):
            parent1 = SELECTION(population, fitness)    ← Pick good parents
            parent2 = SELECTION(population, fitness)
            child = CROSSOVER(parent1, parent2)         ← Combine them
            child = MUTATE(child)                        ← Small random change
            new_population.add(child)
        
        population = new_population
        
        if best individual is good enough: return it
```

### Step-by-Step: 8-Queens with GA

**Encoding**: A string of 8 digits, where digit i = row position of queen in column i

```
Individual:  [1, 6, 2, 5, 8, 3, 7, 4]  → Queen in col 1 is in row 1, etc.
Fitness:     28 - (number of attacking pairs)    Max fitness = 28 (0 conflicts)
```

**Step 1: Initial Population** (random)
```
Individual A: [2, 4, 7, 4, 8, 5, 5, 2]  Fitness = 24
Individual B: [3, 2, 7, 5, 2, 4, 1, 1]  Fitness = 23
Individual C: [2, 4, 4, 1, 5, 1, 2, 4]  Fitness = 20
Individual D: [3, 2, 5, 4, 3, 2, 1, 3]  Fitness = 11
```

**Step 2: Selection** (fitness-proportional)
- A has 24/78 ≈ 31% chance of being picked
- D has 11/78 ≈ 14% chance (lower chance, but not zero!)

**Step 3: Crossover** (single-point crossover)
```
Parent A: [2, 4, 7, 4 | 8, 5, 5, 2]     ← Pick crossover point
Parent B: [3, 2, 7, 5 | 2, 4, 1, 1]

Child 1:  [2, 4, 7, 4 | 2, 4, 1, 1]     ← Front of A + Back of B
Child 2:  [3, 2, 7, 5 | 8, 5, 5, 2]     ← Front of B + Back of A
```

**Step 4: Mutation** (small probability, e.g., 1%)
```
Child 1:  [2, 4, 7, 4, 2, 4, 1, 1]
                              ↓ mutation!
Child 1': [2, 4, 7, 4, 2, 4, 6, 1]      ← Changed gene 7 from 1 to 6
```

**Step 5**: Repeat for many generations!

### Selection Methods

| Method | How It Works | ELI5 |
|---|---|---|
| **Roulette Wheel** | Probability proportional to fitness | Spin a wheel — bigger fitness = bigger slice |
| **Tournament** | Pick k random individuals, best one wins | Mini competition among random contestants |
| **Rank-Based** | Sort by fitness, probability based on rank | Top rankers get more chances, regardless of fitness gap |

### Crossover Types

```
Single-Point:  [A A A A | B B B B]
Two-Point:     [A A | B B B | A A A]
Uniform:       [A B A B B A B A]     ← Each gene randomly from one parent
```

### Properties

| Property | Value |
|---|---|
| **Complete?** | ❌ No (might not find solution) |
| **Optimal?** | ❌ No (but finds good solutions) |
| **Memory** | O(k × n) where k = population size, n = chromosome length |
| **Good for** | Very large, complex search spaces |
| **Bad for** | Problems where you need guaranteed optimality |

---

## 8. Comparison Table

| Algorithm | Memory | Completeness | Optimality | Best For |
|---|---|---|---|---|
| **Hill Climbing** | O(1) | ❌ No | ❌ No | Simple optimization |
| **Random Restart HC** | O(1) | ✅ (probabilistically) | ❌ No | When landscape has many peaks |
| **Simulated Annealing** | O(1) | ✅ (theoretically) | ✅ (theoretically) | Escaping local optima |
| **Local Beam (k)** | O(k) | ❌ No | ❌ No | Exploring in parallel |
| **Genetic Algorithm** | O(k×n) | ❌ No | ❌ No | Complex, large search spaces |

---

## 9. Key Takeaways

1. **Local search** = don't care about the path, just find a good state
2. **Hill climbing** is greedy and gets stuck at local maxima 86% of the time (8-Queens)
3. **Random restarts** make hill climbing surprisingly effective
4. **Simulated annealing** = accept bad moves early (high T) to escape traps, then settle down (low T)
5. **Genetic algorithms** = population of solutions that evolve through selection, crossover, and mutation
6. **None of these guarantee optimality** in practice — they're heuristic methods for hard problems

### The Mental Model

- **Hill Climbing** = A single hiker climbing uphill (simple but can get stuck)
- **Simulated Annealing** = A drunk hiker who gradually sobers up (random early, focused late)
- **Beam Search** = A team of hikers who share the best spots they find
- **Genetic Algorithm** = A whole civilization evolving over generations

---

## 10. Exam Tips

### Must-Know

1. **Draw the landscape** showing local max, global max, plateau, shoulder
2. **Trace simulated annealing** — calculate acceptance probability e^(ΔE/T)
3. **Trace GA** — show selection, crossover, mutation for one generation
4. **Compare hill climbing variants** — when to use each
5. **Why random restart works** — probability calculation

### Common Mistakes

❌ Saying hill climbing is complete (it's NOT — gets stuck at local maxima)
❌ Confusing beam search with parallel random restarts (beam search shares information!)
❌ Forgetting that GA mutation rate should be LOW (typically 0.1-1%)
❌ Thinking simulated annealing always finds global optimum (only theoretically, with infinitely slow cooling)

---

## 📖 References

- AIMA — Chapter 4.1-4.2

---

[⬅️ Prev: Memory-Bounded Search](../03_Search_Memory_Bounded_Heuristic/README.md) | [Back to Main](../README.md) | [Next: And-Or Search ➡️](../05_Search_And_Or/README.md)
