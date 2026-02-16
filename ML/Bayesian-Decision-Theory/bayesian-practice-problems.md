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
7. [Bonus Challenge Problems](#bonus-challenge-problems)
8. [Study Guide](#study-guide)

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

**Answer:**

The probability the email is spam given it contains "Winner" is **90.3%**.

**Decision:** Mark as SPAM 📧❌

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

**Answer:**

The probability you picked the biased coin (Coin B) is **61.5%**.

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

**Answers:**

1. **P(Disease | Positive Test) = 28.6%**
   - Even with positive test, only 28.6% chance of disease
   - Why? Disease is rare (2%), so many false positives

2. **P(Healthy | Negative Test) = 99.96%**
   - Negative test is very reliable
   - If test is negative, almost certainly healthy

</details>

---

### Problem 5: Manufacturing Quality Control

**Difficulty:** ⭐⭐ Medium

**Problem:**

A factory has three machines (A, B, C) that produce widgets.

**Given Information:**
- Machine A produces 50% of all widgets: `P(Machine A) = 0.5`
- Machine B produces 30% of all widgets: `P(Machine B) = 0.3`
- Machine C produces 20% of all widgets: `P(Machine C) = 0.2`

Defect rates:
- Machine A: 1% defective: `p(Defective | A) = 0.01`
- Machine B: 2% defective: `p(Defective | B) = 0.02`
- Machine C: 5% defective: `p(Defective | C) = 0.05`

**Question:**
A widget is randomly selected and found to be defective. What's the probability it came from Machine C?

**What to find:** `P(Machine C | Defective)`

---

<details>
<summary><b>Show Solution</b></summary>

### Solution to Problem 5

**Step 1: Calculate p(Defective)**
```
p(Defective) = p(Defective|A) × P(A) + p(Defective|B) × P(B) + p(Defective|C) × P(C)

             = 0.01 × 0.5 + 0.02 × 0.3 + 0.05 × 0.2
             
             = 0.005 + 0.006 + 0.01
             
             = 0.021
             
             = 2.1%
```

---

**Step 2: Calculate P(Machine C | Defective)**
```
                     p(Defective|C) × P(C)
P(Machine C|Defective) = ─────────────────────────
                            p(Defective)

                           0.05 × 0.2
                       = ──────────────
                             0.021

                           0.01
                       = ────────
                          0.021

                       = 0.476

                       = 47.6%
```

---

**Answer:**

The probability a defective widget came from Machine C is **47.6%**.

</details>

---

## Advanced Problems

### Problem 6: Three-Class Problem

**Difficulty:** ⭐⭐⭐ Hard

**Problem:**

A fruit sorting machine classifies fruits into three types: Apples, Oranges, and Bananas.

**Given Information:**

Prior probabilities:
- `P(Apple) = 0.5`
- `P(Orange) = 0.3`
- `P(Banana) = 0.2`

The machine measures fruit weight (in grams). Based on historical data:

Likelihoods for weight = 150g:
- `p(150g | Apple) = 0.4`
- `p(150g | Orange) = 0.3`
- `p(150g | Banana) = 0.1`

**Question:**
A fruit weighing 150g is measured. Classify the fruit using Bayesian decision rule.

**What to find:** 
- `P(Apple | 150g)`
- `P(Orange | 150g)`
- `P(Banana | 150g)`
- Final classification

---

<details>
<summary><b>Show Solution</b></summary>

### Solution to Problem 6

**Step 1: Calculate Evidence p(150g)**
```
p(150g) = p(150g|Apple) × P(Apple) + p(150g|Orange) × P(Orange) + p(150g|Banana) × P(Banana)

        = 0.4 × 0.5 + 0.3 × 0.3 + 0.1 × 0.2
        
        = 0.20 + 0.09 + 0.02
        
        = 0.31
```

---

**Step 2: Calculate posteriors**
```
P(Apple|150g) = (0.4 × 0.5) / 0.31 = 0.20 / 0.31 = 0.645 = 64.5%

P(Orange|150g) = (0.3 × 0.3) / 0.31 = 0.09 / 0.31 = 0.290 = 29.0%

P(Banana|150g) = (0.1 × 0.2) / 0.31 = 0.02 / 0.31 = 0.065 = 6.5%
```

---

**Answer:**

**Classify as: APPLE 🍎**

Maximum posterior: 64.5%

</details>

---

## Medical Diagnosis Problems

### Problem 7: HIV Testing

**Difficulty:** ⭐⭐ Medium

**Problem:**

An HIV screening test is being evaluated.

**Given Information:**
- HIV prevalence in tested population: `P(HIV+) = 0.005` (0.5%)
- Test sensitivity: `p(Test+ | HIV+) = 0.999` (99.9%)
- Test specificity: `p(Test- | HIV-) = 0.995` (99.5%)

**Questions:**
1. If someone tests positive, what's the probability they actually have HIV?
2. If someone tests negative, what's the probability they're actually HIV-free?

**What to find:** 
- `P(HIV+ | Test+)`
- `P(HIV- | Test-)`

---

<details>
<summary><b>Show Solution</b></summary>

### Solution to Problem 7

**Part 1: P(HIV+ | Test+)**

**Step 1: Calculate p(Test+)**
```
p(Test+) = p(Test+ | HIV+) × P(HIV+) + p(Test+ | HIV-) × P(HIV-)

         = 0.999 × 0.005 + 0.005 × 0.995
         
         = 0.004995 + 0.004975
         
         = 0.00997
         
         ≈ 0.01 or 1%
```

---

**Step 2: Calculate P(HIV+ | Test+)**
```
                p(Test+ | HIV+) × P(HIV+)
P(HIV+ | Test+) = ───────────────────────────
                        p(Test+)

                   0.999 × 0.005
                = ──────────────
                      0.00997

                   0.004995
                = ───────────
                    0.00997

                = 0.501

                = 50.1%
```

---

**Answers:**

1. **P(HIV+ | Test+) = 50.1%**
   - Despite 99.9% sensitivity, only 50% of positive results are true positives!

2. **P(HIV- | Test-) ≈ 100%**
   - Negative test is extremely reliable

</details>

---

## Real-World Applications

### Problem 8: Credit Card Fraud Detection

**Difficulty:** ⭐⭐ Medium

**Problem:**

A bank is detecting fraudulent credit card transactions.

**Given Information:**
- 0.1% of transactions are fraudulent: `P(Fraud) = 0.001`
- The fraud detection algorithm flags suspicious transactions

Algorithm performance:
- `p(Flagged | Fraud) = 0.95` (catches 95% of fraud)
- `p(Flagged | Legitimate) = 0.02` (2% false positive rate)

**Question:**
If a transaction is flagged, what's the probability it's actually fraudulent?

**What to find:** 
- `P(Fraud | Flagged)`

---

<details>
<summary><b>Show Solution</b></summary>

### Solution to Problem 8

**Step 1: Calculate p(Flagged)**
```
p(Flagged) = p(Flagged | Fraud) × P(Fraud) + p(Flagged | Legit) × P(Legit)

           = 0.95 × 0.001 + 0.02 × 0.999
           
           = 0.00095 + 0.01998
           
           = 0.02093
```

---

**Step 2: Calculate P(Fraud | Flagged)**
```
                   p(Flagged | Fraud) × P(Fraud)
P(Fraud | Flagged) = ──────────────────────────────
                           p(Flagged)

                      0.95 × 0.001
                   = ─────────────
                        0.02093

                      0.00095
                   = ──────────
                       0.02093

                   = 0.0454

                   = 4.54%
```

---

**Answer:**

P(Fraud | Flagged) = **4.54%**

Only 4.54% of flagged transactions are actually fraud! This is the base rate problem in action.

</details>

---

## Exam-Style Problems

### Problem 9: University Admission System

**Difficulty:** ⭐⭐⭐ Hard

**Problem:**

A university admission system classifies applicants into three categories based on test scores.

**Categories:**
- High (H): Top tier candidates
- Medium (M): Average candidates  
- Low (L): Below average candidates

**Given Information:**

Prior probabilities (based on last year):
- `P(H) = 0.2`
- `P(M) = 0.5`
- `P(L) = 0.3`

An applicant gets a test score of 75 out of 100.

Historical data shows test score distributions:

| Score Range | P(score \| H) | P(score \| M) | P(score \| L) |
|------------|-------------|-------------|-------------|
| 70-79 | 0.3 | 0.4 | 0.2 |

**Questions:**
1. Calculate the posterior probability for each category
2. Which category should the applicant be classified into?

**What to find:** 
- `P(H | score=75)`, `P(M | score=75)`, `P(L | score=75)`
- Classification decision

---

<details>
<summary><b>Show Solution</b></summary>

### Solution to Problem 9

**Step 1: Calculate Evidence**
```
p(score=75) = 0.3 × 0.2 + 0.4 × 0.5 + 0.2 × 0.3
            
            = 0.06 + 0.20 + 0.06
            
            = 0.32
```

---

**Step 2: Calculate Posteriors**
```
P(H | 75) = (0.3 × 0.2) / 0.32 = 0.06 / 0.32 = 0.1875 = 18.75%

P(M | 75) = (0.4 × 0.5) / 0.32 = 0.20 / 0.32 = 0.625 = 62.5%

P(L | 75) = (0.2 × 0.3) / 0.32 = 0.06 / 0.32 = 0.1875 = 18.75%
```

✅ **Check:** 18.75% + 62.5% + 18.75% = 100% ✓

---

**Answer:**

**Classification: MEDIUM**

Maximum posterior: 62.5%

</details>

---

## Bonus Challenge Problems

### Problem 10: The Monty Hall Problem (Bayesian Perspective)

**Difficulty:** ⭐⭐⭐ Hard (Famous Paradox!)

**Problem:**

You're on a game show. There are 3 doors: behind one is a car, behind the others are goats.

**The Process:**
1. You pick Door 1
2. The host (who knows what's behind each door) opens Door 3, revealing a goat
3. The host asks: "Do you want to switch to Door 2?"

**Given:**
- Car is equally likely behind any door initially: `P(Car behind Door i) = 1/3` for i = 1, 2, 3
- Host will ALWAYS open a door with a goat (never the car)
- Host will ALWAYS offer you the switch

**Question:**
After the host opens Door 3 (showing a goat), what is:
1. P(Car behind Door 1 | Host opened Door 3)?
2. P(Car behind Door 2 | Host opened Door 3)?
3. Should you switch?

Use Bayes' Theorem to prove your answer!

---

<details>
<summary><b>Show Solution</b></summary>

### Solution to Problem 10

This is the famous **Monty Hall Problem** solved with Bayes' Theorem!

**Step 1: Calculate likelihoods P(H₃ | Cᵢ)**

**If car is behind Door 1 (C₁):**
- Host can open either Door 2 or Door 3
- By symmetry: `P(H₃ | C₁) = 1/2`

**If car is behind Door 2 (C₂):**
- Host MUST open Door 3 (can't reveal car)
- `P(H₃ | C₂) = 1`

**If car is behind Door 3 (C₃):**
- Host cannot open Door 3 (has the car!)
- `P(H₃ | C₃) = 0`

---

**Step 2: Calculate evidence P(H₃)**
```
P(H₃) = (1/2) × (1/3) + 1 × (1/3) + 0 × (1/3)
      
      = 1/6 + 1/3 + 0
      
      = 1/2
```

---

**Step 3: Calculate posteriors**
```
P(C₁ | H₃) = [(1/2) × (1/3)] / (1/2) = (1/6) / (1/2) = 1/3 = 33.3%

P(C₂ | H₃) = [1 × (1/3)] / (1/2) = (1/3) / (1/2) = 2/3 = 66.7%

P(C₃ | H₃) = [0 × (1/3)] / (1/2) = 0 = 0%
```

---

**Answers:**

1. **P(Car behind Door 1) = 1/3 = 33.3%**

2. **P(Car behind Door 2) = 2/3 = 66.7%**

3. **YES, YOU SHOULD SWITCH!**
   - Switching doubles your probability of winning!
   - Stay: 33.3% chance
   - Switch: 66.7% chance

**Always switch in Monty Hall!** 🚗

</details>

---

## Study Guide

### Recommended Study Path

**Week 1: Basics**
- Problems 1-3 (Simple applications)
- Focus on: Understanding Bayes' formula

**Week 2: Applications**
- Problems 4-5 (Intermediate applications)
- Focus on: Medical tests, quality control

**Week 3: Advanced**
- Problems 6-10 (Challenge problems)
- Focus on: Multi-class, complex scenarios

---

### Problem Difficulty Guide

**⭐ Easy (1-3):**
- 5-10 minutes each
- Direct application of Bayes' theorem
- Two classes only

**⭐⭐ Medium (4-5, 7-8):**
- 10-20 minutes each
- Multiple scenarios
- Good exam preparation

**⭐⭐⭐ Hard (6, 9-10):**
- 20-30 minutes each
- Multi-class or famous problems
- Deep understanding required

---

### Tips for Success
```
✅ Always write down what you're solving for
✅ Check that probabilities sum to 1
✅ Draw diagrams when confused
✅ Verify your answer makes intuitive sense
✅ Practice without calculator first
✅ Then verify with calculator
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
