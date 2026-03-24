# 🎯 Topic 21 — Reinforcement Learning: Policy Search

> **Difficulty**: 🟡 Medium → 🔴 Hard | **Syllabus Section**: Reinforcement Learning
>
> **Slides**: SD-M | **Quiz Relevance**: ⭐⭐⭐⭐ 

---

## 🍼 The Big Story (ELI5)

### Two Ways to Train a Dog 🐕

**Way 1 — Value-Based (Q-Learning approach):**
You rate EVERY spot in the park and EVERY action: "Spot A + go left = 7 treats. Spot A + go right = 3 treats. Spot B + go left = 5 treats..." Then the dog always picks the highest-rated action. You learn the VALUE of everything first, then act based on values.

**Way 2 — Policy Search (Direct approach):**
You DON'T rate anything. Instead, the dog just TRIES stuff randomly. When it gets treats → "Do MORE of that!" When it gets nothing → "Do LESS of that!" Over time, the dog's behavior directly improves without ever computing values.

> 🍼 **Kid Version — The Simplest Possible Explanation**:
> 
> Imagine you're learning to shoot a basketball:
> - **Value-based** = First, calculate the EXACT angle, force, and position for every possible shot. Then execute the perfect shot. (Compute everything, then act.)
> - **Policy search** = Just throw the ball! Miss? Adjust a little. Miss again? Adjust more. Score! Remember what you did! (Try, learn from results, adjust.)
>
> Policy search is **learning by doing** — not learning by calculating.

---

## 📚 Table of Contents

1. [Why Not Just Use Q-Learning for Everything?](#1-why-policy-search)
2. [What IS a "Parameterized Policy"?](#2-parameterized-policy)
3. [The Policy Gradient Idea — Made Simple](#3-policy-gradient)
4. [🧮 REINFORCE: The Algorithm (Fully Explained)](#4-reinforce)
5. [🧮 Complete REINFORCE Trace (Every Number!)](#5-trace)
6. [The Variance Problem & Baselines](#6-variance)
7. [Actor-Critic: Best of Both Worlds](#7-actor-critic)
8. [Value-Based vs Policy-Based Comparison](#8-comparison)
9. [Key Takeaways](#9-key-takeaways)
10. [Exam Tips](#10-exam-tips)

---

## 1. Why Not Just Use Q-Learning for Everything?

### Q-Learning's Three Big Problems

**Problem 1: Continuous Actions**

Q-Learning needs `max_a Q(s, a)` — find the action with the highest Q-value. But what if actions are CONTINUOUS?

```
Discrete actions (Q-Learning can handle):
  "Go left" or "Go right" or "Go up" or "Go down"
  → Just check Q(s, left), Q(s, right), Q(s, up), Q(s, down). Pick highest. Easy!

Continuous actions (Q-Learning BREAKS):
  "Apply force of 0.00 to 100.00 Newtons to the robot arm"
  → Check Q(s, 0.00), Q(s, 0.01), Q(s, 0.02), ..., Q(s, 100.00)?
  That's 10,000 checks! And what about Q(s, 37.4291)? INFINITE possibilities!
  Can't compute max over infinite values! 💀
```

**Policy search solution**: The policy directly OUTPUTS a continuous number!
```
π_θ(state) = 37.4 Newtons    ← Just outputs the action directly!
```

**Problem 2: Sometimes the Best Strategy is RANDOM**

In rock-paper-scissors, the best strategy is to play each option with probability 1/3 (random!). Q-Learning would say "always play rock" (or whatever had the highest Q), which is TERRIBLE — your opponent would always play paper!

Policy search can learn stochastic (random) policies: P(rock)=1/3, P(paper)=1/3, P(scissors)=1/3.

**Problem 3: Sometimes the Policy is Simpler Than the Value Function**

```
Example: A robot walking on a balance beam.

The optimal POLICY is simple: "lean slightly left if tilting right, lean slightly right if tilting left"
But the VALUE FUNCTION is incredibly complex: "the value of tilting 3.7° right with velocity 0.2°/sec at position 1.3m is..."

Why learn the complex thing when the simple thing is what you actually need?
```

---

## 2. What IS a "Parameterized Policy"?

### The Big Idea

Instead of a giant lookup table (Q-table), represent the policy as a **formula with adjustable knobs** called **parameters θ**.

> 🍼 **Kid Version**: Imagine a robot with 3 knobs on its back:
> - Knob 1 (θ₁): How much to turn left when it sees an obstacle on the right
> - Knob 2 (θ₂): How fast to go when the path is clear
> - Knob 3 (θ₃): How hard to brake when near a wall
>
> Policy search = try different knob settings, see which ones get the most reward, and adjust the knobs!

### Example 1: Linear Policy (Simplest)

```
Scenario: Robot decides how fast to drive based on road conditions.

Features of current state:
  f₁ = road curvature (how much the road bends)
  f₂ = current speed
  f₃ = distance to nearest car

Policy: speed = θ₁ × f₁ + θ₂ × f₂ + θ₃ × f₃

If θ = [−2.0, 0.5, 1.0]:
  speed = −2.0 × (curvature) + 0.5 × (current_speed) + 1.0 × (distance_to_car)
  
  Sharp curve (f₁=5) + going fast (f₂=60) + car close (f₃=2):
  speed = −2.0×5 + 0.5×60 + 1.0×2 = −10 + 30 + 2 = 22 (slow down!)
  
  Straight road (f₁=0) + going slow (f₂=20) + no cars (f₃=100):
  speed = −2.0×0 + 0.5×20 + 1.0×100 = 0 + 10 + 100 = 110 (speed up!)
```

### Example 2: Softmax Policy (For Choosing Between Discrete Options)

When you need to CHOOSE between discrete actions (left/right/up/down) but with PROBABILITIES:

```
P(action = Left | state) = e^(score_left) / (e^(score_left) + e^(score_right))

where score_left = θ_left · features
      score_right = θ_right · features
```

**🧮 Concrete Example:**

```
State features: [distance_to_wall = 3, angle_to_goal = 45°]
θ_left = [0.5, -0.1]   → score_left = 0.5×3 + (-0.1)×45 = 1.5 - 4.5 = -3.0
θ_right = [0.2, 0.3]   → score_right = 0.2×3 + 0.3×45 = 0.6 + 13.5 = 14.1

P(Left) = e^(-3.0) / (e^(-3.0) + e^(14.1))
        = 0.050 / (0.050 + 1,326,937)
        ≈ 0.0000 (almost zero!)

P(Right) = e^(14.1) / (e^(-3.0) + e^(14.1))
         ≈ 1.0000 (almost certain!)

The policy says: "Go RIGHT with near certainty!" because θ_right gives a much higher score.
```

### Example 3: Neural Network Policy (Modern Deep RL)

```
Input: game screen pixels (e.g., 84×84 image)
      ↓
  [Neural network with millions of parameters θ]
      ↓
Output: P(up) = 0.1, P(down) = 0.05, P(left) = 0.15, P(right) = 0.7

This is what AlphaGo, OpenAI Five, and ChatGPT's RLHF use!
```

---

## 3. The Policy Gradient Idea — Made Simple

### What We Want

Find the parameter values θ that make the agent collect the MOST total reward:

```
J(θ) = "Expected total reward when using policy π_θ"

We want to find θ* that MAXIMIZES J(θ).
```

### How: Gradient Ascent (Hill Climbing in Parameter Space!)

Remember hill climbing from Topic 4? Same idea but in the PARAMETER space!

```
θ_new = θ_old + α × ∇J(θ)
                     ↑
                 "gradient" = direction to move θ to INCREASE J

This is like hiking: look at which direction goes UPHILL, take a step that way.
Repeat until you reach a peak!
```

> 🍼 **Kid Version**: You have 3 knobs on the robot. You want to find the best setting.
> 1. Try the current knob settings → robot gets some reward
> 2. Wiggle each knob slightly → see if reward goes up or down
> 3. Turn each knob in the direction that made reward go UP
> 4. Repeat!

### The Core Principle (THE Most Important Thing!)

After running the policy and observing what happened:

```
FOR EACH action the agent took:
  
  Was the TOTAL REWARD after this action GOOD (positive)?
  → YES: Make this action MORE probable in this state!
         "That worked! Do more of it!"
  
  → NO: Make this action LESS probable in this state!
         "That was bad! Do less of it!"

THAT'S THE ENTIRE IDEA OF POLICY GRADIENT. 🎯
```

> 🍼 **The Dog Training Analogy (Again!):**
> - Dog sits → gets treat (+1) → dog learns to sit MORE often
> - Dog barks → gets scolded (-1) → dog learns to bark LESS often
> - The dog doesn't know WHY sitting is good. It just knows sitting leads to treats!

---

## 4. 🧮 REINFORCE: The Algorithm (Fully Explained)

REINFORCE is the simplest policy gradient algorithm. Let's break it down into plain English:

```
function REINFORCE(learning_rate α, discount γ, num_episodes):
    
    initialize θ randomly (start with random knob settings)
    
    for each episode:
        
        ──── PHASE 1: PLAY THE GAME ────
        Start a new game/episode
        At each step:
            Look at current state
            Use policy π_θ to RANDOMLY choose an action
            (higher probability actions are chosen more often)
            Take the action, observe reward and next state
        Keep playing until the game ends
        Record everything: (state₁, action₁, reward₁), (state₂, action₂, reward₂), ...
        
        ──── PHASE 2: COMPUTE RETURNS ────
        For each step t in the episode:
            G_t = reward_t + γ × reward_{t+1} + γ² × reward_{t+2} + ...
            "How much total (discounted) reward did I get FROM THIS POINT ONWARDS?"
        
        ──── PHASE 3: UPDATE THE POLICY ────
        For each step t:
            θ ← θ + α × G_t × ∇_θ log π_θ(state_t, action_t)
            
            Plain English:
            "Adjust θ so that action_t becomes more likely if G_t > 0,
             and less likely if G_t < 0"
```

### What Does "∇_θ log π_θ(s, a)" Mean? (Don't Panic!)

```
∇_θ log π_θ(s, a) = "The direction to adjust θ that makes action a MORE likely in state s"

Think of it as an ARROW pointing in parameter space:
  "If I move θ in THIS direction, the probability of choosing action a will increase"

The MAGNITUDE of G_t controls HOW MUCH we move:
  G_t = +100 → move A LOT in that direction (very good outcome!)
  G_t = +1   → move a little (slightly good)
  G_t = -50  → move in the OPPOSITE direction (bad outcome!)
```

---

## 5. 🧮 Complete REINFORCE Trace (Every Number!)

### Setup

```
Simple world: 2 states (A and B), 2 actions (Left and Right)
γ = 0.9, α = 0.1

Softmax policy with parameters:
  θ = {θ_A_Left, θ_A_Right, θ_B_Left, θ_B_Right}
  Initial θ = {0, 0, 0, 0}  (all equal → 50/50 random choice everywhere)

When all θ = 0:
  P(Left | A) = e^0 / (e^0 + e^0) = 1/2 = 0.5
  P(Right | A) = 0.5
  (same for state B)
```

### Episode 1: A Good Experience

**Phase 1: Play the game**
```
Step 1: In state A. Policy says 50/50. Randomly pick: RIGHT.
        → Get reward +2. Move to state B.

Step 2: In state B. Policy says 50/50. Randomly pick: LEFT.
        → Get reward +8. Game ends.
```

**Phase 2: Compute returns**
```
G₀ (from step 1 onwards) = reward₁ + γ × reward₂
                          = 2 + 0.9 × 8
                          = 2 + 7.2
                          = 9.2

G₁ (from step 2 onwards) = reward₂
                          = 8
```

**Phase 3: Update policy**
```
Step 1: We took RIGHT in state A, and G₀ = 9.2 (POSITIVE → good!)
  → Increase θ_A_Right so RIGHT becomes MORE likely in state A
  
  θ_A_Right ← 0 + 0.1 × 9.2 × (direction to increase P(Right|A))
  
  For softmax, ∇ log π(A, Right) = 1 - P(Right|A) = 1 - 0.5 = 0.5
  
  θ_A_Right ← 0 + 0.1 × 9.2 × 0.5 = 0 + 0.46 = 0.46

Step 2: We took LEFT in state B, and G₁ = 8 (POSITIVE → good!)
  → Increase θ_B_Left
  
  θ_B_Left ← 0 + 0.1 × 8 × 0.5 = 0.40
```

**After Episode 1:**
```
θ = {θ_A_Left=0, θ_A_Right=0.46, θ_B_Left=0.40, θ_B_Right=0}

New probabilities:
  P(Right | A) = e^0.46 / (e^0 + e^0.46) = 1.58 / (1 + 1.58) = 0.61  (was 0.50!)
  P(Left | B)  = e^0.40 / (e^0.40 + e^0) = 1.49 / (1.49 + 1) = 0.60  (was 0.50!)

The policy now PREFERS Right in A and Left in B — because those actions led to good rewards!
```

### Episode 2: A Bad Experience

**Phase 1: Play**
```
Step 1: In state A. P(Right)=0.61. Randomly pick: LEFT (unlucky 39% chance).
        → Get reward -3. Move to state B.

Step 2: In state B. P(Left)=0.60. Randomly pick: RIGHT (unlucky 40% chance).
        → Get reward -1. Game ends.
```

**Phase 2: Compute returns**
```
G₀ = -3 + 0.9 × (-1) = -3 - 0.9 = -3.9 (NEGATIVE! Bad episode!)
G₁ = -1 (NEGATIVE!)
```

**Phase 3: Update policy**
```
Step 1: Took LEFT in A, G₀ = -3.9 (NEGATIVE → bad!)
  → DECREASE θ_A_Left (make Left LESS likely in A)
  
  ∇ log π(A, Left) = 1 - P(Left|A) = 1 - 0.39 = 0.61
  θ_A_Left ← 0 + 0.1 × (-3.9) × 0.61 = 0 - 0.238 = -0.238

Step 2: Took RIGHT in B, G₁ = -1 (NEGATIVE → bad!)
  → DECREASE θ_B_Right
  
  θ_B_Right ← 0 + 0.1 × (-1) × 0.60 = -0.060
```

**After Episode 2:**
```
θ = {θ_A_Left=-0.238, θ_A_Right=0.46, θ_B_Left=0.40, θ_B_Right=-0.060}

New probabilities:
  P(Right | A) = e^0.46 / (e^-0.238 + e^0.46) = 1.58 / (0.79 + 1.58) = 0.67  (increased!)
  P(Left | B) = e^0.40 / (e^0.40 + e^-0.06) = 1.49 / (1.49 + 0.94) = 0.61  (increased!)
```

### What Happened Over 2 Episodes?

```
Episode 1: RIGHT in A → good (+9.2) → RIGHT became more likely ↑
Episode 2: LEFT in A → bad (-3.9)   → LEFT became less likely ↓ (= RIGHT more likely!)

Both episodes REINFORCED that RIGHT is better in state A!
P(Right|A): 0.50 → 0.61 → 0.67 (steadily increasing!)

After many more episodes, P(Right|A) → ~0.95+ and P(Left|B) → ~0.95+
The policy converges to the optimal strategy! 🎯
```

> 🍼 **Kid Version**: "Episode 1: I went right and got lots of candy! I'll go right more often. Episode 2: I went left and got yelled at! I'll go left LESS often. After many tries, I ALMOST ALWAYS go right because it's clearly better."

---

## 6. The Variance Problem & Baselines

### The Problem

REINFORCE updates are NOISY because returns vary wildly:

```
Episode 1: G₀ = +50  → "Go right was AMAZING!" → big positive update
Episode 2: G₀ = +48  → "Go right was AMAZING!" → big positive update  
Episode 3: G₀ = +2   → "Go right was meh" → tiny positive update
Episode 4: G₀ = +51  → "Go right was AMAZING!" → big positive update

All positive! But the updates have very different sizes.
The policy jumps around a lot → slow convergence.
```

### The Solution: Subtract a Baseline!

Instead of using G_t directly, use **G_t minus the AVERAGE return from that state**:

```
BEFORE (raw):      θ ← θ + α × G_t × ∇ log π
AFTER (baseline):  θ ← θ + α × (G_t - b) × ∇ log π

where b = average return = V(s) ≈ 37.75 (average of 50, 48, 2, 51)
```

Now the updates become:
```
Episode 1: G₀ - b = 50 - 37.75 = +12.25 → "Better than average" → positive update
Episode 2: G₀ - b = 48 - 37.75 = +10.25 → "Better than average" → positive update
Episode 3: G₀ - b = 2 - 37.75 = -35.75  → "WORSE than average!" → NEGATIVE update!
Episode 4: G₀ - b = 51 - 37.75 = +13.25 → "Better than average" → positive update

Now the updates are CENTERED around zero → much less noisy!
Episode 3 now correctly gets a NEGATIVE update (it was worse than usual).
```

> 🍼 **Kid Version**: Instead of asking "was this good?", ask "was this BETTER THAN USUAL?" If you usually get 8 treats and today you got 9, that's slightly good (+1). If you got 3, that's bad (-5). Much more useful than just "I got 3 treats" (is that good? depends on what's normal!).

---

## 7. Actor-Critic: Best of Both Worlds

### The Combination

```
ACTOR  = Policy π_θ(s, a)     → Decides WHAT to do (the "doing" part)
CRITIC = Value function V_w(s) → Evaluates HOW GOOD the state is (the "judging" part)

The ACTOR tries actions.
The CRITIC judges: "Was that better or worse than expected?"
The ACTOR adjusts based on the CRITIC's judgment.
```

```
Update rule:
  θ ← θ + α × (G_t - V_w(s_t)) × ∇ log π_θ(s_t, a_t)
                  ↑ CRITIC's baseline!

  "Make action more likely if return was BETTER than the critic expected,
   less likely if WORSE than expected."
```

> 🍼 **Kid Version**: The ACTOR is a student taking a test. The CRITIC is the teacher grading it. The student tries answers (actor), the teacher says "better than average!" or "worse than average!" (critic), and the student adjusts their study strategy accordingly.

---

## 8. Value-Based vs Policy-Based Comparison

| Feature | Value-Based (Q-Learning) | Policy-Based (REINFORCE) | Actor-Critic |
|---|---|---|---|
| **Learns** | Q(s,a) table → derives policy | Policy π_θ directly | Both! |
| **Actions** | Discrete ONLY | Discrete AND continuous! | Both! |
| **Policy type** | Deterministic | Can be stochastic | Both! |
| **Variance** | Low | HIGH | Medium (uses baseline) |
| **Sample efficiency** | Good | Poor (needs many episodes) | Good |
| **Convergence** | Can diverge | Local optimum | More stable |

### When to Use What

```
Discrete actions (Atari games)?     → Q-Learning or Actor-Critic
Continuous actions (robot control)? → Policy Gradient or Actor-Critic
Need stochastic policy (poker)?     → Policy Gradient
Want the best of everything?        → Actor-Critic ★
```

---

## 9. Key Takeaways

1. **Policy search** = find the best policy DIRECTLY (skip learning values!)
2. **Why?** Q-Learning can't handle continuous actions or stochastic policies
3. **Parameterized policy** π_θ(s,a) = formula with adjustable knobs θ
4. **REINFORCE**: Play → compute returns → make good actions more likely, bad actions less likely
5. **The core**: G_t > 0 → increase P(action). G_t < 0 → decrease P(action)
6. **Variance is the enemy** → subtract a baseline (average return)
7. **Actor-Critic** = policy (actor) + value function (critic) → best of both worlds
8. **Modern AI** (AlphaGo, ChatGPT RLHF, robot control) ALL use policy gradients!

---

## 10. Exam Tips

### Must-Know

1. **Explain why Q-Learning fails** for continuous actions (can't compute max over infinite actions)
2. **Describe the REINFORCE update** in plain English: "good outcomes → increase action probability"
3. **Know the update rule**: θ ← θ + α × G_t × ∇ log π_θ(s_t, a_t)
4. **Explain what the baseline does** (reduces variance without adding bias)
5. **Compare value-based vs policy-based** (at least 3 differences)

### Common Mistakes

❌ Thinking policy search always finds the GLOBAL optimum (it finds LOCAL optima — like hill climbing!)
❌ Forgetting REINFORCE needs COMPLETE episodes (you need the full return G_t)
❌ Confusing the policy gradient with the value function gradient (different things!)
❌ Not understanding that G_t > 0 → increase action probability (the CORE idea)

### The One-Line Summary

> "If the result was good, do more of what you did. If bad, do less." That's policy gradient.

---

## 📖 References

- AIMA — Chapter 22
- Sutton & Barto — Chapter 13 (Policy Gradient Methods)

---

[⬅️ Prev: Q-Learning](../20_RL_Q_Learning_Passive_Active/README.md) | [Back to Main](../README.md)

---

## 🏁 Congratulations! You've completed ALL 21 AI topics! 🎉

Go back to the [Main README](../README.md) to review the full structure and prepare for exams!

**The golden rule**: Understand it like you're 5, practice it like you're a researcher! Good luck! 🍀
