# Bayesian Decision Theory - Practice Problems

> **🎯 Practice problems with expandable solutions for exam preparation**

---

## 📖 Table of Contents

1. [Basic Problems](#basic-problems)
2. [Intermediate Problems](#intermediate-problems)
3. [Advanced Problems](#advanced-problems)
4. [Medical Diagnosis Problems](#medical-diagnosis-problems)
5. [Real-World Applications](#real-world-applications)
6. [Exam-Style Problems](#exam-style-problems)
7. [Study Guide](#study-guide)

---

## How to Use This File

- ✅ Try each problem yourself first
- ✅ Write down your answer
- ✅ Click on **"Show Solution"** to check
- ✅ Mark problems you got wrong for review
- ✅ Aim to solve all problems correctly before exam

---

## Basic Problems

### Problem 1: Simple Email Classification

**Difficulty:** ⭐ Easy

**Problem:**

You're building a spam filter for your email.

**Given Information:**
- 40% of all emails are spam: `P(Spam) = 0.4`
- 60% of all emails are legitimate: `P(Legitimate) = 0.6`
- If an email is spam, 70% contain the word "Winner": `p(Winner | Spam) = 0.7`
- If an email is legitimate, 5% contain the word "Winner": `p(Winner | Legitimate) = 0.05`

**Question:**
An email arrives with the word "Winner" in it. What is the probability it's spam?

**What to find:** `P(Spam | Winner)`

---

<details>
<summary><b>Show Solution</b></summary>

### Solution to Problem 1

**Step 1: Calculate Evidence p(Winner)**

```
p(Winner) = p(Winner|Spam) × P(Spam) + p(Winner|Legitimate) × P(Legitimate)

          = 0.7 × 0.4 + 0.05 × 0.6
          
          = 0.28 + 0.03
          
          = 0.31
```

---

**Step 2: Calculate P(Spam | Winner)**

```
                  p(Winner|Spam) × P(Spam)
P(Spam|Winner) = ─────────────────────────
                       p(Winner)

                  0.7 × 0.4
               = ─────────
                    0.31

                  0.28
               = ──────
                  0.31

               = 0.903

               = 90.3%
```

---

**Step 3: Calculate P(Legitimate | Winner) [Optional Check]**

```
P(Legitimate|Winner) = 1 - P(Spam|Winner)
                     = 1 - 0.903
                     = 0.097
                     = 9.7%
```

✅ **Check:** 90.3% + 9.7% = 100% ✓

---

**Answer:**

The probability the email is spam given it contains "Winner" is **90.3%**.

**Decision:** Mark as SPAM 📧❌

---

**Visual Summary:**

```
BEFORE seeing "Winner" (Prior):
Spam:       40%  ████████
Legitimate: 60%  ████████████

AFTER seeing "Winner" (Posterior):
Spam:       90.3%  ██████████████████
Legitimate:  9.7%  ██

Confidence in SPAM increased dramatically!
```

</details>

---

### Problem 2: Weather Prediction

**Difficulty:** ⭐ Easy

**Problem:**

You're trying to predict if it will rain based on morning cloud cover.

**Given Information:**
- It rains 30% of days: `P(Rain) = 0.3`
- It doesn't rain 70% of days: `P(No Rain) = 0.7`
- When it rains, there are clouds in the morning 90% of the time: `p(Clouds | Rain) = 0.9`
- When it doesn't rain, there are clouds in the morning 20% of the time: `p(Clouds | No Rain) = 0.2`

**Question:**
You wake up and see clouds. What's the probability it will rain today?

**What to find:** `P(Rain | Clouds)`

---

<details>
<summary><b>Show Solution</b></summary>

### Solution to Problem 2

**Step 1: Calculate Evidence p(Clouds)**

```
p(Clouds) = p(Clouds|Rain) × P(Rain) + p(Clouds|No Rain) × P(No Rain)

          = 0.9 × 0.3 + 0.2 × 0.7
          
          = 0.27 + 0.14
          
          = 0.41
```

---

**Step 2: Calculate P(Rain | Clouds)**

```
                p(Clouds|Rain) × P(Rain)
P(Rain|Clouds) = ────────────────────────
                      p(Clouds)

                  0.9 × 0.3
               = ─────────
                    0.41

                  0.27
               = ──────
                  0.41

               = 0.659

               = 65.9%
```

---

**Answer:**

The probability it will rain given you see clouds is **65.9%**.

**Decision:** Probably will rain - bring an umbrella! ☔

---

**Interpretation:**

Your prior belief was 30% chance of rain. After seeing clouds, your belief updated to 65.9% chance of rain. The observation of clouds made you MORE confident it will rain.

</details>

---

### Problem 3: Coin Fairness Test

**Difficulty:** ⭐ Easy

**Problem:**

You have two coins in a bag:
- Coin A: Fair coin (50% heads, 50% tails)
- Coin B: Biased coin (80% heads, 20% tails)

You randomly pick one coin from the bag (each equally likely) and flip it.

**Given Information:**
- `P(Coin A) = 0.5`
- `P(Coin B) = 0.5`
- `p(Heads | Coin A) = 0.5`
- `p(Heads | Coin B) = 0.8`

**Question:**
You flip the coin and get HEADS. What's the probability you picked Coin B?

**What to find:** `P(Coin B | Heads)`

---

<details>
<summary><b>Show Solution</b></summary>

### Solution to Problem 3

**Step 1: Calculate Evidence p(Heads)**

```
p(Heads) = p(Heads|Coin A) × P(Coin A) + p(Heads|Coin B) × P(Coin B)

         = 0.5 × 0.5 + 0.8 × 0.5
         
         = 0.25 + 0.40
         
         = 0.65
```

---

**Step 2: Calculate P(Coin B | Heads)**

```
                  p(Heads|Coin B) × P(Coin B)
P(Coin B|Heads) = ───────────────────────────
                         p(Heads)

                    0.8 × 0.5
                = ───────────
                      0.65

                    0.40
                = ────────
                    0.65

                = 0.615

                = 61.5%
```

---

**Step 3: Calculate P(Coin A | Heads)**

```
P(Coin A|Heads) = 1 - P(Coin B|Heads)
                = 1 - 0.615
                = 0.385
                = 38.5%
```

---

**Answer:**

The probability you picked the biased coin (Coin B) is **61.5%**.

---

**Interpretation:**

Before the flip:
- Equal chance of either coin (50%-50%)

After seeing HEADS:
- More likely to be Coin B (61.5% vs 38.5%)
- Makes sense because Coin B produces heads more often!

</details>

---

## Intermediate Problems

### Problem 4: Disease Screening

**Difficulty:** ⭐⭐ Medium

**Problem:**

A hospital is screening patients for a rare disease.

**Given Information:**
- The disease affects 2% of the population: `P(Disease) = 0.02`
- The test has 98% sensitivity (true positive rate): `p(+ | Disease) = 0.98`
- The test has 95% specificity (true negative rate): `p(- | Healthy) = 0.95`

**Questions:**
1. What is the probability a patient has the disease given a positive test?
2. What is the probability a patient is healthy given a negative test?

**What to find:** 
- `P(Disease | +)`
- `P(Healthy | -)`

---

<details>
<summary><b>Show Solution</b></summary>

### Solution to Problem 4

**Part 1: P(Disease | Positive Test)**

**Step 1: Identify all probabilities**

```
P(Disease) = 0.02
P(Healthy) = 1 - 0.02 = 0.98

p(+ | Disease) = 0.98    [Sensitivity]
p(- | Disease) = 0.02

p(- | Healthy) = 0.95    [Specificity]
p(+ | Healthy) = 0.05    [False Positive Rate]
```

---

**Step 2: Calculate p(+)**

```
p(+) = p(+|Disease) × P(Disease) + p(+|Healthy) × P(Healthy)

     = 0.98 × 0.02 + 0.05 × 0.98
     
     = 0.0196 + 0.049
     
     = 0.0686
```

---

**Step 3: Calculate P(Disease | +)**

```
                p(+|Disease) × P(Disease)
P(Disease|+) = ─────────────────────────
                        p(+)

                 0.98 × 0.02
             = ─────────────
                   0.0686

                 0.0196
             = ────────
                 0.0686

             = 0.286

             = 28.6%
```

---

**Part 2: P(Healthy | Negative Test)**

**Step 1: Calculate p(-)**

```
p(-) = p(-|Disease) × P(Disease) + p(-|Healthy) × P(Healthy)

     = 0.02 × 0.02 + 0.95 × 0.98
     
     = 0.0004 + 0.931
     
     = 0.9314
```

---

**Step 2: Calculate P(Healthy | -)**

```
               p(-|Healthy) × P(Healthy)
P(Healthy|-) = ─────────────────────────
                        p(-)

                0.95 × 0.98
             = ─────────────
                  0.9314

                 0.931
             = ────────
                0.9314

             = 0.9996

             = 99.96%
```

---

**Answers:**

1. **P(Disease | Positive Test) = 28.6%**
   - Even with positive test, only 28.6% chance of disease
   - Why? Disease is rare (2%), so many false positives

2. **P(Healthy | Negative Test) = 99.96%**
   - Negative test is very reliable
   - If test is negative, almost certainly healthy

---

**Key Insight:**

This shows the **base rate fallacy**:
- Positive test doesn't mean you definitely have the disease
- The low prevalence (2%) means most positives are false alarms
- Negative test is much more reliable due to high specificity

</details>

---

## Study Guide

### Recommended Study Path

**Week 1: Basics**
- Problems 1-3 (Simple applications)
- Focus on: Understanding Bayes' formula

**Week 2: Applications**
- Problems 4-6 (Intermediate applications)
- Focus on: Medical tests, quality control

**Week 3: Review**
- Re-attempt all problems
- Focus on: Speed and accuracy

---

### Problem Difficulty Guide

**⭐ Easy (1-3):**
- 5-10 minutes each
- Direct application of Bayes' theorem
- Two classes only
- Good for building confidence

**⭐⭐ Medium (4-6):**
- 10-20 minutes each
- May involve multiple scenarios
- Requires careful calculation
- Good exam preparation

---

### Tips for Success

```
✅ Always write down what you're solving for
✅ Check that probabilities sum to 1
✅ Draw diagrams when confused
✅ Verify your answer makes intuitive sense
✅ Practice calculating without calculator first
✅ Then use calculator for final answer
```

---

## 📊 Quick Reference

**Most Important Formulas:**

```
1. Bayes' Theorem:
   P(ω|x) = [p(x|ω) × P(ω)] / p(x)

2. Evidence (2 classes):
   p(x) = p(x|ω₁)P(ω₁) + p(x|ω₂)P(ω₂)

3. Decision Rule:
   Choose ω* = argmax P(ωᵢ|x)

4. Verification:
   Σ P(ωᵢ|x) = 1
```

---

**Remember:**
- Base rate (prior) matters enormously!
- Don't confuse P(A|B) with P(B|A)
- Independence assumption makes calculations easier
- Always verify your answer makes intuitive sense

---

*Made with ❤️ for ML students*  
*Last updated: February 2026*

---
