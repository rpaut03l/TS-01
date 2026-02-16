# K-Nearest Neighbors (K-NN) Classification
## Complete Learning Guide with Practice Problems

---

## Table of Contents
- [🍎 Introduction - The Apple Store Analogy](#-introduction---the-apple-store-analogy)
- [📐 Understanding Distance](#-understanding-distance)
- [🔢 The Mathematics](#-the-mathematics)
  - [Understanding (x, y) Points](#step-1-understanding-x-y-points)
  - [Calculating Distance](#step-2-calculating-distance-pythagorean-theorem)
- [📝 Breaking Down the Notation](#-breaking-down-the-notation)
  - [Distance Notation](#what-does-this-mean)
  - [Sigma Notation](#what-does-this-mean-1)
- [🎯 Complete Distance Formula](#-complete-distance-formula---step-by-step)
- [🗳️ The Voting Formula](#️-the-voting-formula)
- [🎓 The Complete K-NN Algorithm](#-the-complete-k-nn-algorithm---super-simple)
- [📊 Visualizing Different K Values](#-visualizing-k1-vs-k3-vs-k5)
- [🔧 Feature Scaling](#-feature-scaling---why-it-matters)
- [🧮 Scaling Formulas](#-scaling-formula-explained)
  - [Min-Max Normalization](#min-max-normalization)
  - [Standardization (Z-score)](#standardization-z-score)
- [🎯 Choosing K](#-choosing-k---the-simple-rules)
- [🧪 Practice Problems](#-practice-problem---step-by-step)
- [✅ Summary](#-summary---the-big-picture)

---

## 🍎 Introduction - The Apple Store Analogy

Imagine you work at a fruit store and need to identify if a new fruit is an **apple** or an **orange**.

```
Your Memory (Training Data):
🍎 Red, Round, 3 inches     → APPLE
🍎 Red, Round, 2.5 inches   → APPLE
🍊 Orange, Round, 3 inches  → ORANGE
🍊 Orange, Round, 4 inches  → ORANGE
🍎 Red, Round, 2.8 inches   → APPLE

New Fruit: Red, Round, 2.7 inches → ??? 
```

**K-NN says:** "Look at the 3 most similar fruits you've seen before (K=3), and whatever most of them are, that's your answer!"

**Step 1:** Measure how similar the new fruit is to each fruit in memory  
**Step 2:** Pick the 3 closest matches  
**Step 3:** Count votes: 3 apples, 0 oranges  
**Step 4:** Answer: APPLE! 🍎

[Back to Top](#table-of-contents)

---

## 📐 Understanding Distance

### **What is "Distance"?**

Think of it like measuring how different two things are:

```
Person A: Height=5ft, Weight=120lbs
Person B: Height=6ft, Weight=180lbs

How different are they?
Height difference: 6-5 = 1 foot
Weight difference: 180-120 = 60 lbs

Total difference = somehow combine these two numbers
```

[Back to Top](#table-of-contents)

---

## 🔢 The Mathematics

### **Step 1: Understanding (x, y) Points**

```
Imagine a graph paper:

      y (height)
      ↑
    5 |     • Point A (3, 5)
    4 |   
    3 |  • Point B (2, 3)
    2 |
    1 |
    0 +---→ x (width)
      0 1 2 3 4 5
```

**Point A** has:
- x-coordinate (width) = 3
- y-coordinate (height) = 5

**Point B** has:
- x = 2
- y = 3

[Back to Top](#table-of-contents)

---

### **Step 2: Calculating Distance (Pythagorean Theorem)**

Remember the triangle formula from school? Same thing!

```
Point A (3, 5)
Point B (2, 3)

Step 1: Find horizontal difference
x-difference = 3 - 2 = 1

Step 2: Find vertical difference  
y-difference = 5 - 3 = 2

Step 3: Use Pythagorean theorem
      B•────┐
       │    │ 2 (height)
       │    │
       └────•A
         1
       (width)

Distance = √(1² + 2²)
        = √(1 + 4)
        = √5
        = 2.24
```

**In words:** The distance is approximately 2.24 units.

[Back to Top](#table-of-contents)

---

## 📝 Breaking Down the Notation

### **What does this mean?** 
$$||x^{(a)} - x^{(b)}||_2$$

Let me decode this scary-looking formula:

```
||  ||     → These bars mean "length" or "distance"
x^(a)      → Point A (the little (a) is just a label)
x^(b)      → Point B (the little (b) is just a label)
-          → Minus (subtract)
_2         → The subscript 2 means "Euclidean" (straight-line distance)
```

**Translation:** "The straight-line distance between point A and point B"

[Back to Top](#table-of-contents)

---

### **What does this mean?**
$$\sum_{j=1}^{d}$$

This is called **Sigma** - it means "add up"

```
Σ     → Greek letter Sigma = "Sum" = "Add up"
j=1   → Start with j=1 (first dimension)
d     → Go until d (last dimension)
```

**Example:**
If you have 3 dimensions (d=3):

```
Σ(j=1 to 3) means:
Do this for j=1, then j=2, then j=3, and ADD them all up

If calculating (xⱼ)²:
j=1: (x₁)² = first dimension squared
j=2: (x₂)² = second dimension squared  
j=3: (x₃)² = third dimension squared
Total = (x₁)² + (x₂)² + (x₃)²
```

[Back to Top](#table-of-contents)

---

## 🎯 Complete Distance Formula - Step by Step

$$||x^{(a)} - x^{(b)}||_2 = \sqrt{\sum_{j=1}^{d}(x_j^{(a)} - x_j^{(b)})^2}$$

### **Let's decode EVERY symbol:**

| Symbol | Meaning | Example |
|--------|---------|---------|
| $x^{(a)}$ | Point A (all coordinates) | (3, 5, 2) |
| $x^{(b)}$ | Point B (all coordinates) | (1, 4, 6) |
| $x_j^{(a)}$ | The j-th coordinate of point A | $x_1^{(a)}=3$, $x_2^{(a)}=5$ |
| $x_j^{(b)}$ | The j-th coordinate of point B | $x_1^{(b)}=1$, $x_2^{(b)}=4$ |
| $d$ | Total number of dimensions | 3 (we have 3 coordinates) |
| $\sum$ | Add everything up | + + + |
| $\sqrt{}$ | Square root | √ |

---

### **Full Example with Real Numbers:**

```
Point A: (3, 5, 2)   ← This is x^(a)
Point B: (1, 4, 6)   ← This is x^(b)
Dimensions: d = 3

Step 1: For j=1 (first coordinate)
(x₁^(a) - x₁^(b))² = (3 - 1)² = 2² = 4

Step 2: For j=2 (second coordinate)
(x₂^(a) - x₂^(b))² = (5 - 4)² = 1² = 1

Step 3: For j=3 (third coordinate)
(x₃^(a) - x₃^(b))² = (2 - 6)² = (-4)² = 16

Step 4: Sum them (Σ means add)
Sum = 4 + 1 + 16 = 21

Step 5: Square root (√)
Distance = √21 = 4.58
```

**Answer:** Points A and B are **4.58 units apart**

[Back to Top](#table-of-contents)

---

## 🗳️ The Voting Formula

$$y = \arg\max_{t^{(z)}} \sum_{r=1}^{k} \delta(t^{(z)}, t^{(r)})$$

This looks SCARY! Let's break it down:

### **Simple Translation:**
"Pick the class that gets the most votes from the K neighbors"

---

### **Symbol by Symbol:**

| Symbol | Meaning | Plain English |
|--------|---------|---------------|
| $y$ | The prediction | "Our answer" |
| $\arg\max$ | "Pick the one with maximum value" | "Choose the winner" |
| $t^{(z)}$ | A possible class (like "apple" or "orange") | "Option Z" |
| $\sum_{r=1}^{k}$ | Add up for all K neighbors | "Count all K votes" |
| $\delta$ | Delta function (1 if match, 0 if not) | "Does it match?" |
| $t^{(r)}$ | Class of the r-th neighbor | "What neighbor r voted for" |

---

### **What is δ (Delta)?**

Delta is a simple checker:

```python
δ(A, B) = 1 if A equals B
δ(A, B) = 0 if A doesn't equal B

Examples:
δ("apple", "apple")  = 1  ✓
δ("apple", "orange") = 0  ✗
δ("red", "red")      = 1  ✓
```

---

### **Complete Example:**

```
K = 5 (we look at 5 neighbors)

Neighbor 1: Apple  
Neighbor 2: Orange
Neighbor 3: Apple
Neighbor 4: Apple  
Neighbor 5: Orange

Question: How many votes for "Apple"?

For class "Apple":
r=1: δ(Apple, Apple)  = 1 ✓
r=2: δ(Apple, Orange) = 0 ✗
r=3: δ(Apple, Apple)  = 1 ✓
r=4: δ(Apple, Apple)  = 1 ✓
r=5: δ(Apple, Orange) = 0 ✗

Sum = 1 + 0 + 1 + 1 + 0 = 3 votes for Apple

For class "Orange":
r=1: δ(Orange, Apple)  = 0 ✗
r=2: δ(Orange, Orange) = 1 ✓
r=3: δ(Orange, Apple)  = 0 ✗
r=4: δ(Orange, Apple)  = 0 ✗
r=5: δ(Orange, Orange) = 1 ✓

Sum = 0 + 1 + 0 + 0 + 1 = 2 votes for Orange

argmax: Apple has 3, Orange has 2
Winner: APPLE! 🍎
```

[Back to Top](#table-of-contents)

---

## 🎓 The Complete K-NN Algorithm - Super Simple

```
INPUT: 
- Training data (fruits you've seen)
- New fruit to classify
- K (number of neighbors)

STEP 1: Measure distance from new fruit to EVERY fruit in memory
        Use: √[(difference₁)² + (difference₂)² + ...]

STEP 2: Sort all fruits by distance (closest first)

STEP 3: Pick the top K closest fruits

STEP 4: Count how many of each type
        Apples: 3
        Oranges: 1

STEP 5: Predict the class with most votes
        Answer: APPLE!
```

[Back to Top](#table-of-contents)

---

## 📊 Visualizing K=1 vs K=3 vs K=5

```
Training Data:
      🍎 🍎
    🍎  ?  🍊
      🍎 🍊 🍊

K=1 (look at 1 nearest):
Nearest to ? is 🍎 (distance = 0.5)
Prediction: APPLE

K=3 (look at 3 nearest):
3 nearest: 🍎, 🍎, 🍊
Votes: Apple=2, Orange=1
Prediction: APPLE

K=5 (look at 5 nearest):
5 nearest: 🍎, 🍎, 🍎, 🍊, 🍊
Votes: Apple=3, Orange=2
Prediction: APPLE
```

[Back to Top](#table-of-contents)

---

## 🔧 Feature Scaling - Why It Matters

### **The Problem:**

```
Fruit Features:
Weight: 50-200 grams
Color: 0-10 (red scale)

Fruit A: Weight=100g, Color=5
Fruit B: Weight=150g, Color=6
New:     Weight=110g, Color=5

Distance without scaling:
√[(110-100)² + (5-5)²] = √[100 + 0] = 10
√[(110-150)² + (5-6)²] = √[1600 + 1] = 40

Weight DOMINATES! Color barely matters!
```

### **The Solution: Make them equal**

```
Scale everything to 0-1:

Weight scaled = (weight - min) / (max - min)
              = (weight - 50) / (200 - 50)

Color scaled = (color - 0) / (10 - 0)

Now both features are 0-1 range!
```

[Back to Top](#table-of-contents)

---

## 🧮 Scaling Formula Explained

### **Min-Max Normalization:**

$$x_{scaled} = \frac{x - x_{min}}{x_{max} - x_{min}}$$

**In words:** "Squeeze everything between 0 and 1"

**Example:**
```
Weight values: [50, 100, 150, 200]
Min = 50, Max = 200

For weight = 100:
x_scaled = (100 - 50) / (200 - 50)
         = 50 / 150
         = 0.33

For weight = 200:
x_scaled = (200 - 50) / (200 - 50)
         = 150 / 150
         = 1.0

Result: [0, 0.33, 0.67, 1.0]
```

[Back to Top](#table-of-contents)

---

### **Standardization (Z-score):**

$$x_{scaled} = \frac{x - \mu}{\sigma}$$

Where:
- μ (mu) = average (mean)
- σ (sigma) = spread (standard deviation)

**In words:** "Center around 0, with most values between -1 and 1"

**Example:**
```
Heights: [150, 160, 170, 180]

μ (average) = (150+160+170+180)/4 = 165
σ (spread) = 11.2 (calculated using formula)

For height = 170:
x_scaled = (170 - 165) / 11.2
         = 5 / 11.2
         = 0.45

Result: [-1.34, -0.45, 0.45, 1.34]
```

[Back to Top](#table-of-contents)

---

## 🎯 Choosing K - The Simple Rules

### **Visual Guide:**

```
K=1:  Very sensitive          K=too large: Too smooth
      ┌─┐                              ┌───────┐
    ●│ │●                            ● │       │ ●
    ●└─┘●  ← Fits every noise          │       │
    ● ● ●                              │   ?   │
                                       │       │
                                     ● └───────┘ ●

K=3 to 7: JUST RIGHT! ✓
      ┌───┐
    ●│   │●
    ●│ ? │●
    ●└───┘●
```

### **Simple Rules:**

```
✓ If dataset < 100 samples    → Use K = 3-5
✓ If dataset 100-1000 samples → Use K = 5-10  
✓ If dataset > 1000 samples   → Use K = 10-20

✓ Always use ODD numbers (3, 5, 7...) to avoid ties
✓ Rule of thumb: K ≈ √(number of samples)

Example: 100 samples → K ≈ √100 = 10
```

[Back to Top](#table-of-contents)

---

## 🧪 Practice Problem - Step by Step

### **Problem:**

```
Training Data (2D points with classes):
Point 1: (1, 2) → Class A
Point 2: (2, 3) → Class A  
Point 3: (6, 5) → Class B
Point 4: (7, 7) → Class B
Point 5: (2, 2) → Class A

New Point: (3, 4) → ???
K = 3
```

---

### **Solution:**

**Step 1: Calculate distances**

```
Distance to Point 1:
√[(3-1)² + (4-2)²] = √[4 + 4] = √8 = 2.83

Distance to Point 2:
√[(3-2)² + (4-3)²] = √[1 + 1] = √2 = 1.41 ✓

Distance to Point 3:
√[(3-6)² + (4-5)²] = √[9 + 1] = √10 = 3.16

Distance to Point 4:
√[(3-7)² + (4-7)²] = √[16 + 9] = √25 = 5.00

Distance to Point 5:
√[(3-2)² + (4-2)²] = √[1 + 4] = √5 = 2.24 ✓
```

**Step 2: Sort by distance (smallest first)**

```
1. Point 2: 1.41 (Class A) ✓
2. Point 5: 2.24 (Class A) ✓
3. Point 1: 2.83 (Class A) ✓
4. Point 3: 3.16 (Class B)
5. Point 4: 5.00 (Class B)
```

**Step 3: Pick K=3 nearest**

```
Nearest 3:
Point 2 → Class A
Point 5 → Class A
Point 1 → Class A
```

**Step 4: Count votes**

```
Class A: 3 votes ✓
Class B: 0 votes

Winner: Class A!
```

**Answer: The new point (3, 4) is predicted to be Class A**

[Back to Top](#table-of-contents)

---

## ✅ Summary - The Big Picture

### **K-NN in 4 Steps:**

1. **Store** all training data (no learning!)
2. **Measure** distance to all stored points
3. **Pick** K closest points
4. **Vote** majority class wins

### **Key Formulas:**

```
Distance = √[sum of (difference)²]

Prediction = class with most votes among K neighbors

Scaling = (value - min) / (max - min)
```

### **Remember:**

- K-NN is **lazy** (doesn't learn, just memorizes)
- **Distance** = how similar two things are
- **K** = how many neighbors vote
- **Scaling** = make features equal importance

[Back to Top](#table-of-contents)


---
**Created for easy learning and quick reference!** ⭐
---
