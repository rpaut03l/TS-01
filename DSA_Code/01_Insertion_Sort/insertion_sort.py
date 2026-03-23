# ╔══════════════════════════════════════════════════════════════════╗
# ║  🃏 INSERTION SORT — Complete Code Tutorial (Colab Ready)        ║
# ║  If you don't know Python, read 00_Python_Crash_Course first!    ║
# ╚══════════════════════════════════════════════════════════════════╝
#
# 🧒 THE STORY:
# You're holding playing cards. You pick up ONE new card at a time.
# You scan your hand from right to left, push bigger cards right,
# and drop the new card in its spot. That's insertion sort!
#
# 🧠 MNEMONIC: "Pick → Scan → Shift → Drop"
#
# To run in Google Colab:
#   1. Go to https://colab.research.google.com
#   2. New Notebook → paste this entire file into a cell
#   3. Press Shift+Enter to run!

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 1: THE SIMPLEST VERSION — Understand the logic first
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def insertion_sort_simple(arr):
    """
    Sort a list using Insertion Sort.
    
    WHAT EACH VARIABLE MEANS:
    - arr    = the list of numbers we want to sort (like our hand of cards)
    - j      = which card we're currently picking up (index in the list)
    - key    = the VALUE of that card (we save it before shifting)
    - i      = which card in our sorted hand we're comparing with
    
    WHAT EACH LINE DOES:
    - for j in range(1, len(arr)):  → "Pick up each card, starting from the 2nd"
    - key = arr[j]                  → "Hold this card so we don't lose it"  
    - i = j - 1                    → "Start comparing with the card to my left"
    - while i >= 0 and arr[i] > key → "While left card is bigger, keep going"
    - arr[i+1] = arr[i]           → "Push that bigger card one spot right"
    - i -= 1                       → "Look at the NEXT card to the left"
    - arr[i+1] = key              → "Drop our card in the empty spot"
    """
    
    # len(arr) gives us how many numbers are in the list
    # range(1, len(arr)) means: start at 1, go up to len(arr)-1
    # Why start at 1? Because the FIRST card (index 0) is already "sorted" by itself!
    
    for j in range(1, len(arr)):
        
        # STEP 1: PICK UP THE CARD
        # Save the current number. Why? Because we're about to shift things
        # and the spot where this number is will get OVERWRITTEN.
        key = arr[j]
        
        # STEP 2: START SCANNING LEFT
        # i starts at the position RIGHT BEFORE our card
        i = j - 1
        
        # STEP 3: SHIFT BIGGER CARDS RIGHT
        # Two conditions must BOTH be true to keep shifting:
        #   i >= 0         → we haven't gone past the start of the list
        #   arr[i] > key   → the card we're looking at is BIGGER than our card
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]    # Push the bigger card one spot to the right
            i = i - 1               # Move our "scanner" one spot to the left
        
        # STEP 4: DROP THE CARD
        # When the while loop ends, i points to a card SMALLER than key
        # (or i = -1, meaning our card is the smallest).
        # Either way, the right spot for our card is i+1.
        arr[i + 1] = key
    
    return arr


# Let's test it!
print("=" * 60)
print("  INSERTION SORT — Basic Test")
print("=" * 60)
test = [5, 2, 4, 6, 1, 3]
print(f"  Before: {test}")
result = insertion_sort_simple(test.copy())  # .copy() so we don't change the original
print(f"  After:  {result}")
print()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 2: VERBOSE VERSION — See every single step!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def insertion_sort_verbose(arr):
    """Same algorithm, but prints EVERY step so you can follow along."""
    arr = arr.copy()
    n = len(arr)
    total_comparisons = 0
    total_shifts = 0
    
    print(f"Starting array: {arr}")
    print(f"We have {n} elements. We'll make {n-1} passes.\n")
    
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        shifts_this_pass = 0
        comparisons_this_pass = 0
        
        print(f"━━━ Pass {j}: Picking up key = {key} ━━━")
        print(f"  Sorted part: {arr[:j]}  |  Picking: [{key}]  |  Unsorted: {arr[j+1:]}")
        
        while i >= 0 and arr[i] > key:
            comparisons_this_pass += 1
            print(f"  Compare: arr[{i}]={arr[i]} > {key}? YES → shift {arr[i]} right")
            arr[i + 1] = arr[i]
            shifts_this_pass += 1
            i -= 1
        
        if i >= 0:
            comparisons_this_pass += 1
            print(f"  Compare: arr[{i}]={arr[i]} > {key}? NO → STOP here!")
        else:
            print(f"  Reached the beginning → {key} goes to position 0!")
        
        arr[i + 1] = key
        total_comparisons += comparisons_this_pass
        total_shifts += shifts_this_pass
        
        print(f"  Insert {key} at index {i + 1}")
        print(f"  Result: {arr}")
        print(f"  ({comparisons_this_pass} comparisons, {shifts_this_pass} shifts)\n")
    
    print(f"✅ SORTED: {arr}")
    print(f"📊 Total: {total_comparisons} comparisons, {total_shifts} shifts")
    return arr


print("=" * 60)
print("  INSERTION SORT — Step-by-Step Trace")
print("=" * 60)
insertion_sort_verbose([5, 2, 4, 6, 1, 3])
print()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 3: VARIATIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Sort DESCENDING (biggest first)
def insertion_sort_desc(arr):
    """Just flip > to < in the comparison!"""
    arr = arr.copy()
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:    # ← Changed > to <
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr

print("=" * 60)
print("  VARIATIONS")
print("=" * 60)
print(f"  Ascending:  {insertion_sort_simple([5,2,4,6,1,3])}")
print(f"  Descending: {insertion_sort_desc([5,2,4,6,1,3])}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 4: COMPLEXITY ANALYSIS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print()
print("=" * 60)
print("  TIME COMPLEXITY DEMO")
print("=" * 60)

# Best case: already sorted → O(n)
best = list(range(1, 11))  # [1,2,3,...,10]
print(f"\n  Best case (sorted):  {best}")
insertion_sort_verbose(best)

# Worst case: reverse sorted → O(n²)
worst = list(range(10, 0, -1))  # [10,9,8,...,1]
print(f"\n  Worst case (reverse): {worst}")
insertion_sort_verbose(worst)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CHEAT SHEET
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print()
print("""
╔══════════════════════════════════════════════════════╗
║  INSERTION SORT CHEAT SHEET                          ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  CODE:                                               ║
║  for j in range(1, len(arr)):                        ║
║      key = arr[j]                                    ║
║      i = j - 1                                       ║
║      while i >= 0 and arr[i] > key:                  ║
║          arr[i+1] = arr[i]                           ║
║          i -= 1                                      ║
║      arr[i+1] = key                                  ║
║                                                      ║
║  MNEMONIC: "Pick → Scan → Shift → Drop"              ║
║                                                      ║
║  TIME:  Best O(n)  |  Avg O(n²)  |  Worst O(n²)      ║
║  SPACE: O(1)       |  STABLE: Yes  |  IN-PLACE: Yes  ║
║                                                      ║
║  USE WHEN: Small arrays (<30), nearly sorted data    ║
║  DON'T USE WHEN: Large random arrays                 ║
║                                                      ║
║  FUN FACT: shifts = inversions in the array          ║
╚══════════════════════════════════════════════════════╝
""")
