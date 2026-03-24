# 🎮 Topic 19 — Reinforcement Learning: (Markov Decision Processes) MDP & Policy

> **Difficulty**: 🔴 Hard | **Syllabus Section**: Reinforcement Learning
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐⭐

---

## 🍼 Story (ELI5)

Imagine training a puppy. The puppy does something → you give a treat (reward) or say "no" (penalty). Over time, the puppy learns which actions lead to treats!

**Reinforcement Learning (RL)** is EXACTLY this — but for a computer agent:
- The agent is in a **state** (like "standing at a crossroads")
- It takes an **action** (like "go left")
- It gets a **reward** (like "+10 for finding treasure" or "-1 for each step taken")
- It learns a **policy** (a strategy): "In THIS state, do THIS action"

> 🍼 **ELI5**: Think of a video game character:
> - **State** = where you are on the map
> - **Action** = move up/down/left/right
> - **Reward** = +100 for getting the coin, -100 for falling in a pit, -1 for each step (hurry up!)
> - **Policy** = your strategy guide: "At position (3,2), go right!"

An **MDP** (Markov Decision Process) is the MATH behind all of this!

---

## 📚 Table of Contents

1. [What is an MDP?](#1-what-is-an-mdp)
2. [The Markov Property](#2-the-markov-property)
3. [Policies](#3-policies)
4. [Value Functions](#4-value-functions)
5. [The Bellman Equation](#5-the-bellman-equation)
6. [Value Iteration](#6-value-iteration)
7. [Policy Iteration](#7-policy-iteration)
8. [Key Takeaways](#8-key-takeaways)
9. [Exam Tips](#9-exam-tips)

---

## 1. What is an MDP?

### Definition

A **Markov Decision Process** is defined by:

| Component | Symbol | Meaning | Example (Grid World) |
|---|---|---|---|
| **States** | S | All possible situations | Every cell in the grid |
| **Actions** | A(s) | Actions available in state s | {Up, Down, Left, Right} |
| **Transition Model** | T(s, a, s') = P(s'\|s, a) | Probability of reaching s' from s via action a | P(moving right actually goes right) = 0.8 |
| **Reward Function** | R(s) or R(s, a, s') | Immediate reward for being in state s | +1 for goal, -1 for pit, -0.04 for each step |
| **Discount Factor** | γ (gamma), 0 ≤ γ ≤ 1 | How much we value future vs present rewards | γ = 0.9 means future rewards are worth 90% per step |

### Grid World Example

```
┌──────┬──────┬──────┬──────┐
│      │      │      │ +1   │  ← Goal (reward = +1)
│ (1,1)│ (1,2)│ (1,3)│ (1,4)│
├──────┼──────┼──────┼──────┤
│      │ ████ │      │ -1   │  ← Pit (reward = -1)
│ (2,1)│WALL  │ (2,3)│ (2,4)│
├──────┼──────┼──────┼──────┤
│START │      │      │      │
│ (3,1)│ (3,2)│ (3,3)│ (3,4)│
└──────┴──────┴──────┴──────┘

Living reward: -0.04 per step (encourages finding the goal fast!)
```

### Stochastic Transitions

Actions don't always work as intended!

```
If you choose "Go Right":
  80% chance: you go Right (intended)
  10% chance: you go Up (slip!)
  10% chance: you go Down (slip!)
  0% chance: you go Left (never backwards)

If you hit a wall, you stay in place.
```

---

## 2. The Markov Property

### What It Means

**The future depends only on the PRESENT state, not the history of how you got there.**

```
P(Sₜ₊₁ | Sₜ, Aₜ, Sₜ₋₁, Aₜ₋₁, ..., S₀) = P(Sₜ₊₁ | Sₜ, Aₜ)
```

> 🍼 **ELI5**: In chess, it doesn't matter HOW the pieces got to their current positions — what matters is WHERE they are NOW. The current board state is all you need to decide your next move.

### Why This Matters

The Markov property makes MDPs tractable! We only need to know the current state, not the entire history.

---

## 3. Policies

### What is a Policy?

A **policy** π is a function that tells the agent what to do in each state:

```
π(s) = a     "In state s, take action a"
```

### Types of Policies

| Type | Definition | Example |
|---|---|---|
| **Deterministic** | π(s) = a (one action per state) | "At (3,1), always go Right" |
| **Stochastic** | π(a\|s) = probability (distribution over actions) | "At (3,1), go Right with 70%, Up with 30%" |
| **Optimal** | π* = the policy that maximizes expected total reward | The BEST possible strategy |

### Example Policy for Grid World

```
→ → → ★     (★ = goal, ✗ = pit)
↑ ███ ↑ ✗
↑ → ↑ ←

"From (3,1) go Up, from (3,2) go Right, from (3,3) go Up..."
```

---

## 4. Value Functions

### First: What IS "V"? (The Most Important Letter in RL!)

**V stands for VALUE.** Specifically, **V(s) = the VALUE of being in state s.**

But what does "value" mean here? Let's build up from scratch:

> 🍼 **The Allowance Story**: Imagine you're standing at a spot in a board game. From this spot, you'll collect coins as you move forward. Some spots give coins (+1), some spots TAKE coins (-1), and the treasure chest at the end gives +10.
>
> **V(your current spot) = the TOTAL coins you EXPECT to collect from here until the end of the game.**
>
> If you're right next to the treasure → V is HIGH (you're about to get +10!)
> If you're far away → V is LOWER (you have to pay -1 for many steps first)
> If you're next to a trap → V is VERY LOW (you'll lose coins!)

**Formally:**
```
V(s) = "If I start at state s and follow my strategy until the game ends,
        how much TOTAL reward will I collect (on average)?"
```

**Why V matters:** If you know V for every state, you know which states are GOOD and which are BAD. Then you just move toward high-V states and away from low-V states!

```
V(next to goal)   = 9.0   ← "Being here is great! Goal is right there!"
V(middle of maze)  = 3.5   ← "Decent spot, goal is reachable"
V(next to a pit)   = -2.0  ← "Being here is TERRIBLE! Might fall!"
V(goal itself)     = 10.0  ← "I'm AT the goal! Maximum value!"
```

---

### But Wait — Why Not Just Add Up All Future Rewards? Why "Discount"?

Here's the problem: if the game goes on FOREVER, and you get +1 at every step:

```
V = 1 + 1 + 1 + 1 + 1 + ... = ∞ (INFINITY! 💀)
```

That's not useful! We need a way to make the sum FINITE. That's where **γ (gamma)** comes in.

---

### What IS γ (Gamma)? The Discount Factor — Explained From Zero!

**γ (gamma) is a number between 0 and 1** (like 0.9 or 0.5) that makes future rewards worth LESS than immediate rewards.

> 🍼 **The Melting Ice Cream Story 🍦**: Imagine someone offers you ice cream:
> - Ice cream RIGHT NOW = worth $1.00 (full value!)
> - Ice cream in 1 minute = worth $0.90 (it melted a little — only 90% as good)
> - Ice cream in 2 minutes = worth $0.81 (melted more — 81% as good)
> - Ice cream in 3 minutes = worth $0.73 (pretty melted — 73% as good)
> - Ice cream in 10 minutes = worth $0.35 (basically soup — 35% as good)
>
> **γ = 0.9 means each step into the future, the reward is worth 90% of what it was.**

### 🧮 How γ Works — The Exact Math

**γ is NOT calculated — γ is CHOSEN by the designer!** It's a setting, like a thermostat.

Common choices:
- **γ = 0.9** → most common in textbooks
- **γ = 0.99** → common in practice (very patient agent)
- **γ = 0.5** → for examples where you want strong discounting

**What γ does to rewards at different time steps:**

```
γ = 0.9

Reward NOW (step 0):        worth  γ⁰ = 0.9⁰ = 1.000  (100% — full value!)
Reward at step 1:           worth  γ¹ = 0.9¹ = 0.900  (90%)
Reward at step 2:           worth  γ² = 0.9² = 0.810  (81%)
Reward at step 3:           worth  γ³ = 0.9³ = 0.729  (72.9%)
Reward at step 5:           worth  γ⁵ = 0.9⁵ = 0.590  (59%)
Reward at step 10:          worth  γ¹⁰ = 0.9¹⁰ = 0.349 (34.9%)
Reward at step 20:          worth  γ²⁰ = 0.9²⁰ = 0.122 (12.2%)
Reward at step 100:         worth  γ¹⁰⁰ = 0.9¹⁰⁰ = 0.00003 (basically 0!)
```

**How to compute γⁿ?** Just multiply γ by itself n times!

```
γ² = γ × γ = 0.9 × 0.9 = 0.81
γ³ = γ × γ × γ = 0.9 × 0.9 × 0.9 = 0.729
γ⁴ = 0.9 × 0.9 × 0.9 × 0.9 = 0.6561
```

> 🍼 **Kid Version**: γ = 0.9 means "every step into the future, the reward shrinks to 90% of its size." Like a photocopy of a photocopy — each copy is 90% the size of the previous one. After many copies, it's tiny!

### Why γ = 0.9 Is Used (Not 0.8 or 0.95)

**γ = 0.9 is the textbook default** because it's a nice balance:
- **Future rewards still matter** (even 10 steps away, a reward is worth 35% — still significant!)
- **But not TOO much** (100 steps away is basically 0 — the agent doesn't plan infinitely far ahead)
- **Nice round numbers** for hand calculations in exams

In PRACTICE, researchers use γ = 0.99 or γ = 0.999 (more patient agents) because computers can handle the math. In EXAMS, γ = 0.9 is standard because the powers of 0.9 are easy to compute by hand.

---

### Now Let's Use V and γ Together — The Full Formula

**V(s) = sum of ALL future rewards, each multiplied by its discount factor:**

```
V(s) = R₀ + γ¹R₁ + γ²R₂ + γ³R₃ + ...

where:
  R₀ = reward at current state (step 0) — NOT discounted (γ⁰ = 1)
  R₁ = reward at next state (step 1) — discounted by γ
  R₂ = reward 2 steps ahead — discounted by γ²
  etc.
```

---

### 🧮 Computing V(s) — A Concrete Example (Step by Step!)

Let's actually COMPUTE V for a simple path, so you see exactly how the formula works:

```
Imagine a robot walking along a path:

State A ──→ State B ──→ State C ──→ State D (GOAL!)
Reward: -1    Reward: -1   Reward: -1   Reward: +10

The robot gets -1 for each step (hurry up!) and +10 at the goal.
γ = 0.9 (discount factor — chosen by us, not calculated!)
```

**What is V(A)?** "How much total discounted reward will I collect starting from A?"

```
V(A) = R(A) + γ × R(B) + γ² × R(C) + γ³ × R(D)
     = (-1) + 0.9 × (-1) + 0.9² × (-1) + 0.9³ × (+10)

Let's compute each term:
  Step 0 (at A):  R = -1    × γ⁰ = × 1      = -1.000    "I lose 1 right now"
  Step 1 (at B):  R = -1    × γ¹ = × 0.9    = -0.900    "I lose 1 next step (worth 0.9 now)"
  Step 2 (at C):  R = -1    × γ² = × 0.81   = -0.810    "I lose 1 in 2 steps (worth 0.81 now)"
  Step 3 (at D):  R = +10   × γ³ = × 0.729  = +7.290    "I gain 10 in 3 steps (worth 7.29 now)"

  How did we get 0.729?  → 0.9 × 0.9 × 0.9 = 0.729 ✅

V(A) = -1.000 + (-0.900) + (-0.810) + 7.290 = 4.580
```

> 🧮 **Checking the addition:**
> ```
> -1.000
> -0.900  → running total: -1.900
> -0.810  → running total: -2.710
> +7.290  → running total: -2.710 + 7.290 = +4.580 ✅
> ```

> 🍼 **What does V(A) = 4.58 mean?** "Starting from A and walking to the goal, you'll collect a total discounted reward of about 4.58. The goal reward of +10 is big, but it's 3 steps away so it's discounted to 7.29. The -1 penalties along the way reduce it further."

**Now compute V(B) (starting one step closer):**

```
V(B) = (-1) + 0.9 × (-1) + 0.9² × (+10)
     = -1 + (-0.9) + 8.1
     = 6.2
```

**V(C) (two steps closer):**

```
V(C) = (-1) + 0.9 × (+10) = -1 + 9 = 8.0
```

**V(D) (already at goal):**

```
V(D) = +10 (you're already there!)
```

**Summary — V values along the path:**
```
V(A) = 4.58    "Pretty far from goal, moderate value"
V(B) = 6.20    "Getting closer, higher value"
V(C) = 8.00    "Almost there! High value"
V(D) = 10.00   "Goal! Maximum value"

The closer to the goal → the higher the V value!
That's exactly what V should tell us — how GOOD each state is!
```

### The Discount Factor γ — In Depth!

### What Does γ Actually DO?

γ controls how much you care about FUTURE rewards vs IMMEDIATE rewards.

Think of γ as a **"patience factor"**:
- γ close to 0 → very IMpatient, only cares about NOW
- γ close to 1 → very patient, cares about the far future

### 🧮 Same Path, Different γ Values — Watch How V Changes!

```
Path: A(-1) → B(-1) → C(-1) → D(+10)
```

**γ = 0 (ZERO patience — only cares about RIGHT NOW):**
```
V(A) = -1 + 0×(-1) + 0×(-1) + 0×(10) = -1
V(B) = -1 + 0×(-1) + 0×(10) = -1
V(C) = -1 + 0×(10) = -1
V(D) = +10

With γ=0, V(A) = V(B) = V(C) = -1!
The agent only sees the immediate -1 step cost.
It doesn't "look ahead" to see the +10 goal at all!
Like a toddler who only sees the broccoli in front of them,
not the ice cream dessert afterward!
```

**γ = 0.5 (MODERATE patience):**
```
V(A) = -1 + 0.5×(-1) + 0.25×(-1) + 0.125×(10)
     = -1 - 0.5 - 0.25 + 1.25 = -0.5

V(B) = -1 + 0.5×(-1) + 0.25×(10) = -1 - 0.5 + 2.5 = 1.0

V(C) = -1 + 0.5×(10) = -1 + 5 = 4.0

V(D) = +10

The future reward of +10 is heavily discounted:
  At A (3 steps away): 10 × 0.5³ = 10 × 0.125 = only 1.25!
  At C (1 step away):  10 × 0.5¹ = 10 × 0.5   = 5.0
The agent sees the goal but doesn't value it much from far away.
```

**γ = 0.9 (HIGH patience — our standard example):**
```
V(A) = -1 + 0.9×(-1) + 0.81×(-1) + 0.729×(10) = 4.58
V(B) = -1 + 0.9×(-1) + 0.81×(10) = 6.2
V(C) = -1 + 0.9×(10) = 8.0
V(D) = +10

The future reward is barely discounted:
  At A (3 steps away): 10 × 0.9³ = 10 × 0.729 = 7.29 (still big!)
The agent strongly values the distant goal.
```

**γ = 1.0 (INFINITE patience — no discounting):**
```
V(A) = -1 + 1×(-1) + 1×(-1) + 1×(10) = -1 - 1 - 1 + 10 = 7.0
V(B) = -1 + (-1) + 10 = 8.0
V(C) = -1 + 10 = 9.0
V(D) = +10

No discount at all! Future rewards are worth EXACTLY the same as immediate ones.
Problem: if the path is INFINITE (no terminal state), V = -1 -1 -1 -1... = -∞!
That's why γ=1 is dangerous — the sum might not converge!
```

### 📊 Summary Table: V(A) for Different γ

| γ | V(A) | V(B) | V(C) | V(D) | Agent's Personality |
|---|---|---|---|---|---|
| **0** | -1.00 | -1.00 | -1.00 | 10 | "I only see what's RIGHT HERE" (blind to future) |
| **0.5** | -0.50 | 1.00 | 4.00 | 10 | "I see the future but it looks small" |
| **0.9** | 4.58 | 6.20 | 8.00 | 10 | "I value the future almost as much as now" |
| **1.0** | 7.00 | 8.00 | 9.00 | 10 | "Future = present. I'm infinitely patient" |

> 🍼 **Kid Version of γ**:
> - **γ = 0**: "Mom, I want candy NOW. I don't care about a birthday cake next week." 🍬
> - **γ = 0.5**: "I want candy now, but I'll also think a LITTLE about that birthday cake." 🍬🎂
> - **γ = 0.9**: "Birthday cake next week sounds almost as good as candy today! I can wait." 🎂
> - **γ = 1.0**: "I literally don't care if it's today or in 100 years. A reward is a reward." ♾️

### Why γ < 1 is Almost Always Used

1. **Math safety**: γ < 1 guarantees the infinite sum converges (stays finite)
2. **Real world**: Sooner rewards ARE more certain — who knows if you'll still be alive in 100 steps?
3. **Practical**: γ = 0.9 or γ = 0.99 are the most common choices in practice

### Action Value Function Q^π(s, a)

**Q^π(s, a)** = Expected total reward starting from state s, taking action a FIRST, then following policy π

```
Q^π(s, a) = E[R + γV^π(s') | s, a]
           = Σ_{s'} T(s, a, s') × [R(s, a, s') + γV^π(s')]
```

> 🍼 **ELI5**: "How good is it to DO this action in this state?" If going right leads toward the goal, Q(s, right) is high. If going right leads toward a pit, Q(s, right) is low.

### V vs Q

- **V(s)**: How good is this STATE? (regardless of what action you take next)
- **Q(s, a)**: How good is this STATE-ACTION pair?
- **Relationship**: V(s) = max_a Q(s, a) for the optimal policy

---

## 5. The Bellman Equation

### The Key Insight

The value of a state can be expressed in terms of its successor states' values:

```
V*(s) = max_a Σ_{s'} T(s, a, s') × [R(s, a, s') + γ × V*(s')]
```

> 🍼 **ELI5**: "The value of WHERE I AM = the best I can do NOW + (discounted) the value of WHERE I'LL BE"

### Breaking It Down

```
V*(s) = max   [  Σ    T(s,a,s')  ×  [ R(s,a,s')  +  γ V*(s') ] ]
         ↑        ↑        ↑              ↑              ↑
     best    for each  probability    immediate    discounted
     action  outcome   of outcome     reward      future value
```

### The Bellman Equation for Q-values

```
Q*(s, a) = Σ_{s'} T(s, a, s') × [R(s, a, s') + γ × max_{a'} Q*(s', a')]
```

### Optimal Policy from V* or Q*

```
π*(s) = argmax_a Σ_{s'} T(s, a, s') × [R(s, a, s') + γ × V*(s')]

or simply:

π*(s) = argmax_a Q*(s, a)
```

---

## 6. Value Iteration

### The Algorithm

Start with random V values, repeatedly apply the Bellman equation until convergence:

```
function VALUE_ITERATION(MDP, ε):
    initialize V(s) = 0 for all s
    
    repeat:
        δ = 0
        for each state s:
            v = V(s)
            V(s) = max_a Σ_{s'} T(s,a,s') × [R(s,a,s') + γ × V(s')]
            δ = max(δ, |v - V(s)|)
    until δ < ε                ← Converged! Values barely changed
    
    ← Extract optimal policy:
    for each state s:
        π(s) = argmax_a Σ_{s'} T(s,a,s') × [R(s,a,s') + γ × V(s')]
    
    return π
```

### Example Iteration (Grid World)

```
Iteration 0: All V = 0
┌──────┬──────┬──────┬──────┐
│  0   │  0   │  0   │ +1   │
├──────┼──────┼──────┼──────┤
│  0   │ ████ │  0   │ -1   │
├──────┼──────┼──────┼──────┤
│  0   │  0   │  0   │  0   │
└──────┴──────┴──────┴──────┘

Iteration 1: (γ=1, living reward=-0.04)
┌──────┬──────┬──────┬──────┐
│  0   │  0   │ 0.76 │ +1   │  ← (1,3) can reach goal with 80% prob
├──────┼──────┼──────┼──────┤
│  0   │ ████ │  0   │ -1   │
├──────┼──────┼──────┼──────┤
│  0   │  0   │  0   │  0   │
└──────┴──────┴──────┴──────┘

...values propagate outward over iterations...

Final (converged):
┌──────┬──────┬──────┬──────┐
│ 0.81 │ 0.87 │ 0.92 │ +1   │
├──────┼──────┼──────┼──────┤
│ 0.76 │ ████ │ 0.66 │ -1   │
├──────┼──────┼──────┼──────┤
│ 0.71 │ 0.66 │ 0.61 │ 0.39 │
└──────┴──────┴──────┴──────┘
```

### Properties

- **Guaranteed to converge** to the optimal values V*
- **Convergence rate**: Linear (each iteration reduces error by factor γ)
- **Time per iteration**: O(|S|² × |A|)

---

## 7. Policy Iteration

### Alternative Approach

Instead of iterating on values, iterate on POLICIES:

```
function POLICY_ITERATION(MDP):
    initialize π(s) = random action for each s
    
    repeat:
        ← Step 1: Policy EVALUATION — find V^π for current policy
        Solve: V^π(s) = Σ_{s'} T(s, π(s), s') × [R(s, π(s), s') + γV^π(s')]
        (This is a system of linear equations! Can solve directly)
        
        ← Step 2: Policy IMPROVEMENT — update policy greedily
        policy_stable = true
        for each state s:
            old_action = π(s)
            π(s) = argmax_a Σ_{s'} T(s,a,s') × [R(s,a,s') + γV^π(s')]
            if π(s) ≠ old_action: policy_stable = false
        
    until policy_stable            ← Policy didn't change!
    
    return π
```

### Value Iteration vs Policy Iteration

| Feature | Value Iteration | Policy Iteration |
|---|---|---|
| **Iterates on** | Values V(s) | Policy π(s) |
| **Per iteration** | One Bellman backup per state | Full policy evaluation + improvement |
| **Convergence** | Many iterations, each cheap | Few iterations, each expensive |
| **Typical** | Many fast iterations | 3-20 iterations (even for large MDPs!) |

---

## 8. Key Takeaways

1. **MDP** = States + Actions + Transitions + Rewards + Discount (S, A, T, R, γ)
2. **Markov Property**: Future depends only on current state, not history
3. **Policy π(s)** maps states to actions — the agent's strategy
4. **V(s)** = how good a state is; **Q(s,a)** = how good a state-action pair is
5. **Bellman Equation**: V*(s) = max_a [Σ T(s,a,s') × (R + γV*(s'))]
6. **Value Iteration**: Repeatedly apply Bellman equation → converges to V*
7. **Policy Iteration**: Alternate between evaluating and improving the policy
8. **Discount γ** balances immediate vs future rewards and ensures convergence

---

## 9. Exam Tips

### Must-Know

1. **Define MDP components** for a given problem
2. **Write the Bellman equation** and explain each term
3. **Run value iteration** for 2-3 iterations on a small grid
4. **Extract the optimal policy** from V* values
5. **Explain the discount factor** and its effect on behavior

### Common Mistakes

❌ Forgetting to multiply by transition probability T(s,a,s')
❌ Forgetting the discount factor γ
❌ Confusing V(s) with Q(s,a) — V is over states, Q is over state-action pairs
❌ Not considering stochastic transitions (agent might slip!)
❌ Setting γ = 1 without realizing it can cause non-convergence in infinite horizons

---

## 📖 References

- AIMA — Chapter 17 (Making Complex Decisions - https://aima.cs.berkeley.edu/contents.html)
- Sutton & Barto — Chapters 3-4

---

[⬅️ Prev: Causality](../18_Causality_Probabilistic_Reasoning/README.md) | [Back to Main](../README.md) | [Next: Q-Learning & Passive/Active RL ➡️](../20_RL_Q_Learning_Passive_Active/README.md)
