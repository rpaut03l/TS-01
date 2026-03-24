# 🔗 Topic 18 — Causality & Probabilistic Reasoning

> **Difficulty**: 🟡 Medium | **Syllabus Section**: Bayesian Networks & Uncertain Reasoning
>
> **Slides**: RB-M & SD-M | **Quiz Relevance**: ⭐⭐⭐⭐

---

## 🍼 The Big Story (ELI5)

### Ice Cream Doesn't Cause Drowning! 🍦🏊

You notice: when ice cream sales go UP, drowning deaths also go UP. Does ice cream CAUSE drowning?!

**NO!** Both happen because of HOT WEATHER:
- Hot weather → people buy more ice cream
- Hot weather → people swim more → more drowning

The hot weather is a **confounding variable** — it causes BOTH things but ice cream doesn't cause drowning!

> 🍼 **Kid Version**:
> - **Correlation** = "When A happens, B happens too" (ice cream ↑ and drowning ↑)
> - **Causation** = "A actually MAKES B happen" (pushing a ball → ball moves)
> - **Confounding** = "Secret thing C causes both A and B" (hot weather causes both!)
>
> Just because two things happen together doesn't mean one CAUSES the other!

---

## 📚 Table of Contents

1. [Correlation ≠ Causation](#1-correlation)
2. [Three Causal Structures](#2-three-structures)
3. [Simpson's Paradox (Fully Worked!)](#3-simpsons)
4. [The do-Operator (Intervention)](#4-do-operator)
5. [Pearl's Ladder of Causation](#5-ladder)
6. [Key Takeaways](#6-key-takeaways)
7. [Exam Tips](#7-exam-tips)

---

## 1. Correlation ≠ Causation

### Real Examples of False Causation

| Correlation | Confounding Variable | Real Explanation |
|---|---|---|
| Ice cream ↑ → Drowning ↑ | Hot weather | Both caused by heat |
| Shoe size ↑ → Reading ability ↑ | Age (children!) | Older kids have bigger feet AND read better |
| Firefighters at scene → More damage | Fire severity | Bigger fires bring more firefighters |
| Hospitals have high death rates | Sick people go to hospitals! | Selection bias |

---

## 2. Three Causal Structures

### Structure 1: Chain (Mediation)

```
A → B → C
"A causes B, B causes C"
Example: Smoking → Tar → Cancer
```

### Structure 2: Fork (Common Cause)

```
A ← B → C
"B causes both A and C"
Example: Hot weather ← Summer → More ice cream
```

### Structure 3: Collider (Common Effect)

```
A → B ← C
"Both A and C cause B"
Example: Talent → Fame ← Luck

WEIRD FACT: If you KNOW B (fame), then A and C become DEPENDENT!
"Among famous people, the less talented ones must be luckier."
This is called EXPLAINING AWAY or the "selection bias."
```

---

## 3. 🧮 Simpson's Paradox (Fully Worked!)

### The Story

A drug company tests a new medicine. Results:

```
Among MEN:
  Drug group:    81 recovered out of 87   (93% recovery)
  No-drug group: 234 recovered out of 270 (87% recovery)
  → Drug seems BETTER for men! ✅

Among WOMEN:
  Drug group:    192 recovered out of 263 (73% recovery)
  No-drug group: 55 recovered out of 80   (69% recovery)
  → Drug seems BETTER for women! ✅

OVERALL (combining everyone):
  Drug group:    81+192 = 273 out of 87+263 = 350 (78% recovery)
  No-drug group: 234+55 = 289 out of 270+80 = 350 (83% recovery)
  → Drug seems WORSE overall! ❌ 😱
```

### 🧮 Let's Verify the Math!

```
Men with drug:      81/87  = 93.1%  ← Drug better ✅
Men without drug:   234/270 = 86.7%

Women with drug:    192/263 = 73.0% ← Drug better ✅
Women without drug: 55/80  = 68.8%

Overall with drug:    (81+192)/(87+263) = 273/350 = 78.0% ← Drug WORSE?! ❌
Overall without drug: (234+55)/(270+80) = 289/350 = 82.6%
```

### Why Does This Happen?!

**The confounding variable is GENDER distribution:**
```
Drug group:    87 men + 263 women = 350 total (mostly WOMEN)
No-drug group: 270 men + 80 women = 350 total (mostly MEN)
```

Women have lower recovery rates overall. The drug group has MORE women, which drags down the overall average — even though the drug helps BOTH men AND women!

> 🍼 **Kid Version**: Imagine two schools take a test. In BOTH schools, girls score higher than boys. But School A has mostly girls (high scorers) and School B has mostly boys (lower scorers). Overall, School A scores higher — but NOT because of anything the school does. It's because of WHO goes there!

### The Lesson

**Always check for confounding variables!** The OVERALL trend can be OPPOSITE of the within-group trend when groups are unequally sized.

---

## 4. The do-Operator (Intervention)

### Seeing vs Doing

```
P(Y | X=x)     = "What's P(Y) among people who HAPPEN to have X=x?" 
                   (OBSERVATIONAL — just watching)

P(Y | do(X=x)) = "What's P(Y) if we FORCE X to be x?"
                   (INTERVENTIONAL — actively changing the world)
```

### Why They're Different

```
Example: Barometer reading (X) and Rain (Y)
  
  Observation: P(Rain | Barometer=low) = high
    "When the barometer reads low, it usually rains"
    
  Intervention: P(Rain | do(Barometer=low)) = unchanged!
    "If I PUSH the barometer needle to low, it doesn't cause rain!"
    
  The barometer PREDICTS rain (correlation) but doesn't CAUSE it!
```

### How do() Works in a Bayesian Network

When we do(X=x):
1. **CUT all arrows INTO X** (remove influence of X's parents)
2. **Set X=x** (force the value)
3. Leave everything else unchanged

```
BEFORE do():              AFTER do(X=x):
Z → X → Y                Z    X=x → Y        ← Arrows INTO X are CUT!
```

> 🍼 **Kid Version**: "Seeing a student study doesn't mean MAKING them study will help. Maybe the students who choose to study are already the smart ones (confounding). To test if studying HELPS, we force random students to study (intervention) and see what happens."

### The Adjustment Formula

```
P(Y | do(X=x)) = Σ_z P(Y | X=x, Z=z) × P(Z=z)

"Average the effect of X on Y across ALL values of confounders Z"
```

This REMOVES the confounding effect of Z!

---

## 5. Pearl's Ladder of Causation

| Level | Question | Type | Tool |
|---|---|---|---|
| **1. Seeing** | "What if I SEE X?" | Observation | P(Y\|X) |
| **2. Doing** | "What if I DO X?" | Intervention | P(Y\|do(X)) |
| **3. Imagining** | "What if I HAD done X?" | Counterfactual | P(Y_x\|X',Y') |

Each level is STRONGER than the previous. You can't answer Level 2 questions with Level 1 data alone (unless you know the causal structure)!

---

## 6. Key Takeaways

1. **Correlation ≠ Causation** — confounders can create fake relationships
2. **Simpson's Paradox** = group trends can REVERSE when combined (confounding!)
3. **do(X=x)** = intervention = CUT arrows into X, force X=x → different from just observing X=x
4. **Three structures**: Chain (A→B→C), Fork (A←B→C), Collider (A→B←C)
5. **Explaining away**: Observing a collider makes its causes dependent
6. **Pearl's Ladder**: Seeing < Doing < Imagining

---

## 7. Exam Tips

### Must-Know
1. **Explain Simpson's Paradox** with numbers
2. **Distinguish P(Y|X) from P(Y|do(X))** with an example
3. **Draw a modified graph** after applying do() (cut incoming arrows)
4. **Identify confounding variables** in a given scenario

### Common Mistakes
❌ Claiming correlation implies causation
❌ Confusing P(Y|X) with P(Y|do(X))
❌ Forgetting to CUT incoming arrows when applying do()

---

## 📖 References
- AIMA — Chapter 13-14
- Judea Pearl: "The Book of Why"

---

[⬅️ Prev: Bayesian Networks](../17_Bayesian_Network/README.md) | [Back to Main](../README.md) | [Next: RL — MDP ➡️](../19_RL_MDP_Policy/README.md)
