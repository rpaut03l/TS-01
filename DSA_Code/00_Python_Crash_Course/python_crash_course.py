# ============================================================
# 🐍 PYTHON CRASH COURSE — Learn Python for DSA in 30 Minutes
# ============================================================
# If you've NEVER written Python before, start here!
# This file teaches you EVERYTHING you need to read and write
# DSA code. Run each section one by one.
#
# HOW TO RUN THIS:
# Option 1: Go to https://colab.research.google.com → New Notebook → paste code
# Option 2: Install Python → save as .py → run with: python filename.py
# Option 3: Use https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro  or https://www.online-python.com
# ============================================================

# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 1: PRINTING — Talking to the Screen             ║
# ╚══════════════════════════════════════════════════════════╝

# print() shows text on the screen. It's your first tool!
print("Hello, I'm learning Python!")    # This shows: Hello, I'm learning Python!
print(42)                                # This shows: 42
print("My age is", 25)                   # This shows: My age is 25

# MNEMONIC: print() = "SHOUT this to the screen!"


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 2: VARIABLES — Boxes That Hold Stuff            ║
# ╚══════════════════════════════════════════════════════════╝

# A variable is like a labeled box. You put something in it.
name = "Alice"       # A box called "name" holding the text "Alice"
age = 25             # A box called "age" holding the number 25
height = 5.6         # A box called "height" holding a decimal number
is_student = True    # A box called "is_student" holding True or False

print(name)          # Shows: Alice
print(age)           # Shows: 25

# You can change what's in the box:
age = 26             # Now the box "age" holds 26
print(age)           # Shows: 26

# MNEMONIC: variable = a STICKY NOTE on a box
# The name is the sticky note, the value is what's inside


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 3: DATA TYPES — What Kind of Stuff?             ║
# ╚══════════════════════════════════════════════════════════╝

# Python has a few basic types of data:
x = 10          # int     (whole number: 1, 2, 100, -5)
y = 3.14        # float   (decimal number: 1.5, 3.14, -0.001)
s = "hello"     # str     (text/string: "abc", "hello world")
b = True        # bool    (True or False — that's it!)
n = None        # None    (means "nothing" or "empty")

# Check the type:
print(type(x))  # <class 'int'>
print(type(s))  # <class 'str'>

# MNEMONIC: int = INTeger, float = FLOATing point, str = STRing of letters


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 4: MATH — Calculator Time!                      ║
# ╚══════════════════════════════════════════════════════════╝

a = 10
b = 3

print(a + b)     # 13    Addition
print(a - b)     # 7     Subtraction
print(a * b)     # 30    Multiplication
print(a / b)     # 3.333 Division (always gives decimal)
print(a // b)    # 3     Floor division (cuts off decimal — whole number only!)
print(a % b)     # 1     Modulo (remainder: 10 ÷ 3 = 3 remainder 1)
print(a ** b)    # 1000  Power (10³ = 10 × 10 × 10 = 1000)

# SUPER IMPORTANT FOR DSA:
# //  = "integer division" (used in finding midpoints: mid = (left + right) // 2)
# %   = "remainder" (used for checking even/odd: n % 2 == 0 means even)
# **  = "power" (2**10 = 1024)

# Infinity — used in Dijkstra, DP, etc.
infinity = float('inf')      # Bigger than ANY number!
print(5 < infinity)          # True
print(infinity + 1)          # inf  (still infinity!)

# Negative infinity
neg_inf = float('-inf')      # Smaller than ANY number!


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 5: LISTS — A Row of Boxes                       ║
# ╚══════════════════════════════════════════════════════════╝

# A list is like a row of numbered boxes (starting from 0!)
# THIS IS THE MOST IMPORTANT DATA STRUCTURE IN PYTHON FOR DSA!

fruits = ["apple", "banana", "cherry"]
numbers = [5, 2, 4, 6, 1, 3]
empty = []

# Access by index (position). STARTS FROM 0, NOT 1!
print(fruits[0])    # apple   (first item = index 0)
print(fruits[1])    # banana  (second item = index 1)
print(fruits[2])    # cherry  (third item = index 2)
print(fruits[-1])   # cherry  (last item = index -1)

# Length
print(len(fruits))  # 3  (three items)

# Add to end
fruits.append("date")       # Now: ["apple", "banana", "cherry", "date"]

# Remove last
fruits.pop()                # Removes "date", now back to 3 items

# Change an item
fruits[1] = "blueberry"    # Now: ["apple", "blueberry", "cherry"]

# Slicing — get a PIECE of the list
arr = [10, 20, 30, 40, 50]
print(arr[1:3])     # [20, 30]     (index 1 up to BUT NOT including 3)
print(arr[:3])      # [10, 20, 30] (from start up to index 3)
print(arr[2:])      # [30, 40, 50] (from index 2 to end)
print(arr[:])       # [10, 20, 30, 40, 50]  (copy of entire list)

# MNEMONIC for indexing:
# Index:    0     1     2     3     4
# Value:   [10]  [20]  [30]  [40]  [50]
# Think of indices as LABELS on the boxes, starting from 0!

# List of lists (2D array — used in DP like LCS!)
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(grid[0][0])   # 1  (row 0, column 0)
print(grid[1][2])   # 6  (row 1, column 2)

# Create a list of zeros (common in DP!)
dp = [0] * 10       # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Create a 2D list of zeros (common in LCS!)
rows, cols = 3, 4
table = [[0] * cols for _ in range(rows)]
# [[0,0,0,0], [0,0,0,0], [0,0,0,0]]


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 6: IF/ELSE — Making Decisions                   ║
# ╚══════════════════════════════════════════════════════════╝

# "if" checks a condition. If True → do something. If False → skip or do something else.

age = 18

if age >= 18:
    print("You can vote!")       # This runs because 18 >= 18 is True
else:
    print("Too young to vote.")

# Multiple conditions:
score = 75

if score >= 90:
    print("Grade A")
elif score >= 80:       # "elif" = "else if"
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")
# Output: Grade C (because 75 >= 70)

# Comparisons:
# ==  means "equal to"       (5 == 5 is True)
# !=  means "not equal to"   (5 != 3 is True)
# >   means "greater than"
# <   means "less than"
# >=  means "greater or equal"
# <=  means "less or equal"

# Combine conditions:
# and  = both must be true     (True and True = True)
# or   = at least one true     (True or False = True)
# not  = flip it               (not True = False)

x = 5
if x > 0 and x < 10:
    print("x is between 0 and 10")  # This runs!

# MNEMONIC: if/elif/else = "IF this is true DO this, ELSE IF that DO that, OTHERWISE do this"


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 7: LOOPS — Repeating Things                     ║
# ╚══════════════════════════════════════════════════════════╝

# FOR LOOP — "do this for each item"
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Prints: apple, banana, cherry (one per line)

# FOR LOOP with range() — "do this N times"
for i in range(5):        # i goes: 0, 1, 2, 3, 4
    print(i)

for i in range(2, 7):     # i goes: 2, 3, 4, 5, 6
    print(i)

for i in range(1, 10, 2): # i goes: 1, 3, 5, 7, 9 (step by 2)
    print(i)

# THIS IS HOW INSERTION SORT WORKS:
# for j in range(1, len(arr)):   ← "for each card from 2nd to last"

# WHILE LOOP — "keep doing this while condition is true"
count = 0
while count < 5:
    print(count)        # Prints: 0, 1, 2, 3, 4
    count += 1          # count = count + 1

# THIS IS HOW INSERTION SORT'S INNER LOOP WORKS:
# while i >= 0 and arr[i] > key:  ← "keep shifting while bigger"

# BREAK — "stop the loop early"
for i in range(100):
    if i == 5:
        break           # Stops at i=5
    print(i)            # Prints: 0, 1, 2, 3, 4

# CONTINUE — "skip this iteration"
for i in range(5):
    if i == 2:
        continue        # Skips i=2
    print(i)            # Prints: 0, 1, 3, 4

# NESTED LOOPS — "a loop inside a loop" (used in O(n²) algorithms!)
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
# Prints all 9 combinations: (0,0), (0,1), (0,2), (1,0), ...


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 8: FUNCTIONS — Reusable Recipes                 ║
# ╚══════════════════════════════════════════════════════════╝

# A function is a named block of code you can call (use) anytime.
# Think of it as a RECIPE: you define it once, cook it whenever you want.

def greet(name):                # Define the function
    """This function says hello."""
    print(f"Hello, {name}!")

greet("Alice")     # Call it! → Hello, Alice!
greet("Bob")       # Call again! → Hello, Bob!

# Function that RETURNS a value:
def add(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return result       # "return" sends the answer back

answer = add(3, 5)      # answer = 8
print(answer)            # 8

# Function with default value:
def power(base, exp=2):
    return base ** exp

print(power(3))         # 9  (3² — used default exp=2)
print(power(3, 3))      # 27 (3³ — overrode default)

# RECURSIVE FUNCTION — A function that calls ITSELF!
# This is CRITICAL for Merge Sort, BST, DFS, etc.

def factorial(n):
    """Calculate n! = n × (n-1) × ... × 1"""
    if n <= 1:          # BASE CASE — when to STOP
        return 1
    return n * factorial(n - 1)   # RECURSIVE CASE — call yourself!

print(factorial(5))     # 120 (5 × 4 × 3 × 2 × 1)

# HOW RECURSION WORKS — Imagine a chain of helpers:
# factorial(5) asks factorial(4) → asks factorial(3) → asks factorial(2) → asks factorial(1)
# factorial(1) returns 1
# factorial(2) returns 2 × 1 = 2
# factorial(3) returns 3 × 2 = 6
# factorial(4) returns 4 × 6 = 24
# factorial(5) returns 5 × 24 = 120

# MNEMONIC: Every recursive function needs:
# 1. BASE CASE (when to stop) — without this, it runs FOREVER!
# 2. RECURSIVE CASE (calling itself with a SMALLER problem)


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 9: DICTIONARIES — Lookup Tables                 ║
# ╚══════════════════════════════════════════════════════════╝

# A dictionary maps KEYS to VALUES. Like a real dictionary:
# word → definition.  Used for adjacency lists in graphs!

phone_book = {
    "Alice": "555-0001",
    "Bob":   "555-0002",
    "Charlie": "555-0003"
}

print(phone_book["Alice"])       # 555-0001
phone_book["Dana"] = "555-0004"  # Add a new entry

# Check if key exists:
if "Bob" in phone_book:
    print("Found Bob!")

# Loop through:
for name, number in phone_book.items():
    print(f"{name}: {number}")

# Default value if key missing:
age = {}
age["Alice"] = 25
print(age.get("Bob", 0))    # 0 (Bob not found, return default 0)

# setdefault — add key with default if not exists:
graph = {}
graph.setdefault("A", []).append("B")   # graph = {"A": ["B"]}
graph.setdefault("A", []).append("C")   # graph = {"A": ["B", "C"]}

# THIS IS HOW WE BUILD ADJACENCY LISTS FOR GRAPHS!


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 10: SETS — Unique Collections                   ║
# ╚══════════════════════════════════════════════════════════╝

# A set holds UNIQUE items (no duplicates). Fast membership check!
# Used for "visited" sets in BFS/DFS!

visited = set()
visited.add("A")
visited.add("B")
visited.add("A")         # Duplicate — ignored!
print(visited)            # {'A', 'B'}

print("A" in visited)     # True  (O(1) — super fast!)
print("C" in visited)     # False


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 11: CLASSES — Building Your Own Data Structures ║
# ╚══════════════════════════════════════════════════════════╝

# A class is a BLUEPRINT for creating objects.
# We use classes to build nodes for trees, graphs, etc.

class Node:
    """A node in a Binary Search Tree."""
    def __init__(self, key):     # __init__ runs when you create a node
        self.key = key           # The value stored in this node
        self.left = None         # Left child (starts empty)
        self.right = None        # Right child (starts empty)

# Create nodes:
root = Node(10)
root.left = Node(5)
root.right = Node(15)

print(root.key)          # 10
print(root.left.key)     # 5
print(root.right.key)    # 15

# MNEMONIC: __init__ = "INITIAL setup" — runs when object is created
# self = "THIS particular object" (like "me" in English)
# self.key = "MY key value"


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 12: IMPORTANT PYTHON TOOLS FOR DSA              ║
# ╚══════════════════════════════════════════════════════════╝

# --- deque (double-ended queue) — USED FOR BFS! ---
from collections import deque

queue = deque()
queue.append("A")        # Add to right:  deque(['A'])
queue.append("B")        # Add to right:  deque(['A', 'B'])
first = queue.popleft()  # Remove from left: 'A'  (FIFO!)
print(first)             # A

# MNEMONIC: deque for BFS = "First In, First Out" like a real queue

# --- heapq (min-heap) — USED FOR DIJKSTRA! ---
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
smallest = heapq.heappop(heap)   # Always gives the SMALLEST!
print(smallest)                   # 1

# For Dijkstra: push (distance, vertex), always get the closest vertex
heapq.heappush(heap, (2, "A"))   # (distance=2, vertex="A")
heapq.heappush(heap, (1, "B"))
dist, vertex = heapq.heappop(heap)   # (1, "B") — closest first!

# --- sorted() — Sort anything! ---
arr = [5, 2, 4, 6, 1, 3]
sorted_arr = sorted(arr)              # [1, 2, 3, 4, 5, 6]  (new list)
arr.sort()                             # Sorts in-place (modifies arr)

# Sort by custom key (e.g., sort activities by finish time):
activities = [(1, 4), (3, 5), (0, 6), (5, 7)]
by_finish = sorted(activities, key=lambda x: x[1])
# [(1,4), (3,5), (0,6), (5,7)] → sorted by second element

# --- enumerate() — Loop with index ---
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")
# Index 0: apple
# Index 1: banana
# Index 2: cherry

# --- zip() — Loop over two lists together ---
names = ["Alice", "Bob"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# --- f-strings — Easy text formatting ---
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old.")
# My name is Alice and I'm 25 years old.


# ╔══════════════════════════════════════════════════════════╗
# ║  CHAPTER 13: COMMON PATTERNS IN DSA CODE                 ║
# ╚══════════════════════════════════════════════════════════╝

# PATTERN 1: "Find the best" — used in Rod Cutting, Dijkstra
best = float('-inf')      # Start with worst possible
for x in [3, 7, 1, 9, 4]:
    if x > best:
        best = x
print(f"Best = {best}")   # 9

# PATTERN 2: "Build a result list" — used in BFS paths
result = []
for i in range(5):
    result.append(i * 2)
print(result)              # [0, 2, 4, 6, 8]

# PATTERN 3: "Two pointers" — used in Merge
i, j = 0, 0
left = [1, 3, 5]
right = [2, 4, 6]
merged = []
while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        merged.append(left[i])
        i += 1
    else:
        merged.append(right[j])
        j += 1
merged.extend(left[i:])
merged.extend(right[j:])
print(merged)              # [1, 2, 3, 4, 5, 6]

# PATTERN 4: "DP table filling" — used in Rod Cutting, LCS
n = 5
dp = [0] * (n + 1)
for j in range(1, n + 1):
    dp[j] = dp[j-1] + j      # Example: cumulative sum
print(dp)                     # [0, 1, 3, 6, 10, 15]

# PATTERN 5: "Adjacency list graph" — used in BFS, DFS, Dijkstra
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
for neighbor in graph['A']:
    print(f"A connects to {neighbor}")


print("\n🎉 CONGRATULATIONS! You now know enough Python to read ALL the DSA code!")
print("Go ahead and open the algorithm files — you're ready!")
