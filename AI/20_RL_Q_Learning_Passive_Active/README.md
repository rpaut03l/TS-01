# 🧠 Topic 20 — Q-Learning, Passive RL & Active RL

> **Difficulty**: 🔴 Hard | **Syllabus Section**: Reinforcement Learning 
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐⭐

---

## 🍼 Story (ELI5)

In the last topic, we knew EVERYTHING about the world (transition probabilities, rewards). That's like having the ANSWER KEY to a test — easy!

But in REAL reinforcement learning, the agent has to **learn by doing** — it doesn't know the transition probabilities or even the rewards ahead of time!

- **Passive RL** = "I have a fixed strategy (policy). Let me follow it many times and figure out how good each state is." (Like following a fixed recipe and seeing how the dish turns out)
- **Active RL** = "I get to CHOOSE what to do, and I learn the best strategy AS I go!" (Like experimenting in the kitchen to find the best recipe)
- **Q-Learning** = "I learn the value of every state-action pair WITHOUT even knowing the transition model!" (The MOST powerful and popular RL method!)

> 🍼 **ELI5**: 
> - **Passive RL** = A puppy that always follows the same path through the park. Over many walks, it learns which parts of the path have treats.
> - **Active RL** = A puppy that's FREE to explore the park. It discovers new paths and learns which routes lead to the most treats!
> - **Q-Learning** = The puppy learns "if I'm at the tree and go left, I get 5 treats" for every spot and direction.

---

## 📚 Table of Contents

1. [Passive vs Active RL](#1-passive-vs-active)
2. [Passive RL Methods](#2-passive-rl)
3. [Temporal Difference (TD) Learning](#3-td-learning)
4. [Active RL: Exploration vs Exploitation](#4-active-rl)
5. [Q-Learning](#5-q-learning)
6. [Key Takeaways](#6-key-takeaways)
7. [Exam Tips](#7-exam-tips)

---

## 1. Passive vs Active RL

### The Key Difference

| Feature | Passive RL | Active RL |
|---|---|---|
| **Policy** | FIXED (given) | LEARNED (agent chooses) |
| **Goal** | Learn V^π (how good is my fixed policy?) | Learn π* (what's the BEST policy?) |
| **Agent's freedom** | Must follow the given policy | Free to explore |
| **Like** | Evaluating a student's fixed study plan | Finding the BEST study plan |

### What the Agent Doesn't Know

In both cases, the agent typically does NOT know:
- T(s, a, s') — the transition model (how the world works)
- R(s) — the rewards (until it actually visits states)

It must learn these through **experience** (trial and error)!

---

## 2. Passive RL Methods

### 2.1 Direct Utility Estimation

**Idea**: Run the policy many times. For each state, average the total reward received from that state onwards.

```
function DIRECT_UTILITY_ESTIMATION(policy π):
    for many episodes:
        run policy π from start to terminal
        record the sequence: s₁, r₁, s₂, r₂, ..., sₙ, rₙ
        
        for each state sₜ in the sequence:
            utility_from_sₜ = rₜ + γrₜ₊₁ + γ²rₜ₊₂ + ...
            add utility_from_sₜ to samples[sₜ]
    
    for each state s:
        V(s) = average of samples[s]
```

**Pros**: Simple! Eventually converges to correct V^π.
**Cons**: SLOW! Wastes information by treating each state independently (ignores that V(s) is related to V(s')).

### 2.2 Adaptive Dynamic Programming (ADP)

**Idea**: Learn the transition model T and reward R from experience, then solve the MDP using value/policy iteration!

```
function ADP_PASSIVE(policy π):
    for many episodes:
        run policy π, observe transitions (s, a, s', r)
        
        ← Update model:
        count[s, a, s'] += 1
        T(s, a, s') = count[s, a, s'] / Σ_{s''} count[s, a, s'']
        R(s) = observed reward for state s
    
    ← Solve using policy evaluation:
    V^π = solve Bellman equations with learned T and R
```

**Pros**: Uses ALL available information (relationships between states). Converges faster.
**Cons**: Must store and maintain the full model. Expensive for large state spaces.

---

## 3. Temporal Difference (TD) Learning

### The Best of Both Worlds!

TD learning combines:
- **Direct estimation's simplicity** (no model needed!)
- **ADP's use of relationships** (learns from bootstrapping)

### The Key Idea

After a transition from s to s' with reward r:

```
V(s) ← V(s) + α × [r + γV(s') - V(s)]
        ↑              ↑            ↑
    learning         TD target   current
      rate          (updated      estimate
                     estimate)
```

> 🍼 **ELI5**: 
> - You THOUGHT state s was worth V(s)
> - Then you actually moved to s' and got reward r
> - The REAL value seems to be r + γV(s') (immediate reward + discounted future)
> - So you NUDGE your estimate a little toward this new information
> - α controls how much you nudge (big α = trust new info more)

### TD(0) Algorithm

```
function TD_LEARNING(policy π, α, γ):
    initialize V(s) = 0 for all s
    
    for each episode:
        s = start state
        while s is not terminal:
            a = π(s)                              ← Follow fixed policy
            take action a, observe reward r and next state s'
            V(s) ← V(s) + α × [r + γV(s') - V(s)]  ← TD update!
            s = s'
```

### Why TD Works

The **TD error** = r + γV(s') - V(s) is like a "surprise":
- If TD error > 0: "s was better than I thought!" → increase V(s)
- If TD error < 0: "s was worse than I thought!" → decrease V(s)
- If TD error = 0: "No surprise, my estimate was right" → no change

### Comparison

| Method | Needs Model? | Uses State Relationships? | Complexity |
|---|---|---|---|
| Direct Utility | ❌ No | ❌ No | Simple |
| ADP | Learns model | ✅ Yes | Expensive |
| **TD Learning** | ❌ No | ✅ Yes (bootstrapping) | **Best tradeoff!** |

---

## 4. Active RL: Exploration vs Exploitation

### The Fundamental Dilemma

The agent has to CHOOSE actions. Should it:
- **Exploit**: Do what it currently thinks is best? (Use current knowledge)
- **Explore**: Try something new to discover potentially better options? (Gain new knowledge)

> 🍼 **ELI5**: You know a good restaurant nearby. But there might be an AMAZING restaurant you haven't tried yet. Do you go to the safe choice (exploit) or try something new (explore)?

### Greedy Agent (Pure Exploitation)

Always take the action that currently seems best:
```
a = argmax_a Q(s, a)
```

**Problem**: Might never discover better actions! Gets stuck in local optima.

### ε-Greedy (Simple Exploration)

With probability (1-ε): take the best action (exploit)
With probability ε: take a RANDOM action (explore)

```
function EPSILON_GREEDY(s, Q, ε):
    if random() < ε:
        return random action          ← Explore!
    else:
        return argmax_a Q(s, a)        ← Exploit!
```

**Common**: Start with ε = 1.0 (all exploration), gradually decrease to ε ≈ 0.01 (mostly exploitation).

### Optimistic Initialization

Initialize Q-values HIGH (optimistically). This makes the agent think unexplored actions are great, naturally encouraging exploration!

```
Initialize: Q(s, a) = 100 for all s, a  (even though true values might be 1-10)

Agent tries action A → gets reward 5 → Q drops toward 5
Now other unexplored actions (still at 100) look better → agent explores them!
```

### Upper Confidence Bound (UCB)

Choose actions that balance exploitation with exploration uncertainty:

```
a = argmax_a [Q(s,a) + c × √(ln(N(s)) / N(s,a))]
              ↑ exploitation    ↑ exploration bonus (big for rarely-tried actions)
```

---

## 5. Q-Learning

### The Star Algorithm! ⭐

Q-Learning is **model-free, off-policy, active RL** that directly learns Q*(s, a) — the optimal Q-values!

### "Off-Policy" Meaning

The agent can explore using ANY strategy (like ε-greedy), but it's learning the OPTIMAL Q-values as if it were following the optimal policy. This is the magic of Q-learning!

### The Q-Learning Update Rule

After taking action a in state s, observing reward r and next state s':

```
Q(s, a) ← Q(s, a) + α × [r + γ × max_{a'} Q(s', a') - Q(s, a)]
                            ↑                ↑
                      immediate         best future value
                       reward          (assuming optimal play!)
```

Compare with TD:
- **TD**: V(s) ← V(s) + α[r + γV(s') - V(s)] — updates V based on next V
- **Q-Learning**: Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)] — updates Q based on BEST next Q

### The Q-Learning Algorithm

```
function Q_LEARNING(env, α, γ, ε, num_episodes):
    initialize Q(s, a) = 0 for all s, a
    
    for each episode:
        s = start state
        while s is not terminal:
            a = ε_greedy(s, Q, ε)              ← Choose action (exploration!)
            take action a, observe r, s'
            Q(s,a) ← Q(s,a) + α[r + γ max_{a'} Q(s',a') - Q(s,a)]  ← Q update!
            s = s'
    
    ← Extract optimal policy:
    for each state s:
        π*(s) = argmax_a Q(s, a)
    
    return π*
```

### Q-Learning Step-by-Step Example (FULL TRACE)

**Grid World** (2×2, γ=0.9, α=0.5):
```
┌───────┬───────┐
│ (0,0) │ (0,1) │ = +10 (Goal! Terminal state)
├───────┼───────┤
│ START │ (1,1) │
│ (1,0) │       │
└───────┴───────┘

Actions: Up, Down, Left, Right (if you hit a wall, you stay in place)
Living reward: -1 per step (encourages finding goal quickly!)
Goal reward: +10 at (0,1)
```

**Initialize ALL Q-values to 0:**

```
Q-Table (initially all zeros):
           Up    Down   Left   Right
(0,0)      0      0      0      0
(1,0)      0      0      0      0
(1,1)      0      0      0      0
(0,1)   terminal — no Q-values needed
```

**EPISODE 1:**

**Step 1**: s=(1,0), pick action=Right (ε-greedy chose randomly), arrive s'=(1,1), r=-1

```
Q((1,0), Right) ← Q((1,0), Right) + α × [r + γ × max_a' Q((1,1), a') - Q((1,0), Right)]
                ← 0 + 0.5 × [-1 + 0.9 × max(0, 0, 0, 0) - 0]
                ← 0 + 0.5 × [-1 + 0.9 × 0 - 0]
                ← 0 + 0.5 × [-1]
                ← -0.5

Updated Q-table:
           Up    Down   Left   Right
(1,0)      0      0      0     -0.5  ← updated!
```

**Step 2**: s=(1,1), pick action=Up, arrive s'=(0,1), r=+10 (GOAL!)

```
Q((1,1), Up) ← 0 + 0.5 × [10 + 0.9 × max Q((0,1), a') - 0]
             ← 0 + 0.5 × [10 + 0]     (terminal state, future value = 0)
             ← 0 + 0.5 × 10
             ← 5.0

Updated Q-table:
           Up    Down   Left   Right
(1,1)      5.0    0      0      0    ← updated!
```

Episode 1 ends (reached goal). **The agent learned that going Up from (1,1) is good!**

---

**EPISODE 2:**

**Step 1**: s=(1,0), pick action=Up, arrive s'=(0,0), r=-1

```
Q((1,0), Up) ← 0 + 0.5 × [-1 + 0.9 × max Q((0,0), a') - 0]
             ← 0 + 0.5 × [-1 + 0.9 × 0 - 0]   (all Q's at (0,0) are still 0)
             ← 0 + 0.5 × [-1]
             ← -0.5
```

**Step 2**: s=(0,0), pick action=Right, arrive s'=(0,1), r=+10 (GOAL!)

```
Q((0,0), Right) ← 0 + 0.5 × [10 + 0 - 0]
                ← 5.0
```

**After 2 episodes, Q-table:**
```
           Up     Down   Left   Right
(0,0)      0       0      0     5.0   ← knows Right leads to goal!
(1,0)     -0.5     0      0    -0.5
(1,1)      5.0     0      0      0    ← knows Up leads to goal!
```

---

**EPISODE 3:**

**Step 1**: s=(1,0), pick action=Right (ε-greedy), arrive s'=(1,1), r=-1

```
Q((1,0), Right) ← -0.5 + 0.5 × [-1 + 0.9 × max(5.0, 0, 0, 0) - (-0.5)]
                ← -0.5 + 0.5 × [-1 + 0.9 × 5.0 + 0.5]
                ← -0.5 + 0.5 × [-1 + 4.5 + 0.5]
                ← -0.5 + 0.5 × 4.0
                ← -0.5 + 2.0
                ← 1.5   ← Now POSITIVE! The agent learned (1,1) leads to reward!
```

**See what happened?** The reward from the goal PROPAGATED BACKWARDS through Q-values! First Q((1,1), Up) learned about the goal (Episode 1). Then Q((1,0), Right) learned that (1,1) is valuable (Episode 3). Over many episodes, knowledge flows backward from the goal to distant states!

> 🍼 **Kid Version**: The puppy found a treat at the end of a path. Next time, it remembers "that last step before the treat was good." The time after that, it remembers "the step BEFORE the last step was also good, because it leads to the good last step!" Eventually it learns the WHOLE path from the start to the treat!

**After many episodes, the Q-table converges to optimal values, and the policy becomes:**
```
(1,0): Right → (1,1)
(1,1): Up → (0,1) GOAL!
(0,0): Right → (0,1) GOAL!

Optimal path from (1,0): Right → Up → GOAL! ✅
```

### Properties of Q-Learning

| Property | Value |
|---|---|
| **Model-free** | ✅ No need to know T(s,a,s') or R! |
| **Off-policy** | ✅ Learns optimal Q* regardless of exploration strategy |
| **Converges** | ✅ Yes, with proper α schedule (α decreasing over time) |
| **Tabular** | Stores Q-value for every (s,a) pair — scales poorly for large spaces |

---

## 6. Key Takeaways

1. **Passive RL** = fixed policy, learn values. **Active RL** = learn the best policy.
2. **Direct Utility Estimation**: simple but slow (ignores state relationships)
3. **TD Learning**: model-free bootstrapping — the foundation of modern RL!
4. **TD Error** = r + γV(s') - V(s) — the "surprise" signal
5. **Exploration vs Exploitation**: Must balance trying new things with using what works
6. **ε-Greedy**: Simple exploration — random action with probability ε
7. **Q-Learning**: Model-free, off-policy, learns Q*(s,a) directly — **THE most important RL algorithm!**
8. **Q-update**: Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]

---

## 7. Exam Tips

### Must-Know

1. **Write the Q-learning update rule** and explain each component
2. **Trace Q-learning** for 3-4 steps on a small grid
3. **Compare passive vs active RL** methods
4. **Explain exploration vs exploitation** with examples
5. **Write the TD(0) update** and explain the TD error
6. **Compare Direct Utility, ADP, and TD Learning**

### Common Mistakes

❌ Using V(s') in Q-learning instead of max Q(s', a')
❌ Forgetting to multiply by learning rate α
❌ Confusing on-policy (SARSA) with off-policy (Q-learning)
❌ Not understanding why Q-learning is "off-policy" (it learns π* while following ε-greedy)
❌ Thinking Q-learning needs a model (it's model-free!)

### The Key Formula Card

```
TD:          V(s)   ← V(s)   + α[r + γV(s')            - V(s)]
Q-Learning:  Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)]
SARSA:       Q(s,a) ← Q(s,a) + α[r + γ Q(s',a')        - Q(s,a)]
                                           ↑ actual next action (on-policy)
```

---

## 📖 References

- AIMA — Chapter 22 (Reinforcement Learning)
- Sutton & Barto — Chapters 5-6

---

[⬅️ Prev: MDP & Policy](../19_RL_MDP_Policy/README.md) | [Back to Main](../README.md) | [Next: Policy Search ➡️](../21_RL_Policy_Search/README.md)
