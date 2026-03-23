# ╔══════════════════════════════════════════════════════════════════╗
# ║  🔀 MERGE SORT — Complete Code Tutorial (Colab Ready)            ║
# ╚══════════════════════════════════════════════════════════════════╝
#
# 🧒 THE STORY:
# You have a huge pile of LEGO bricks in random sizes.
# STEP 1: Split the pile in half. Split again. Until each pile has 1 brick.
# STEP 2: Merge pairs back — always pick the SMALLER brick first.
# One brick alone is already "sorted" — that's the base case!
#
# 🧠 MNEMONIC: "Split → Sort halves → Merge back"
# 🧠 MERGE trick: "Two sorted stacks? Always pick the smaller top card!"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 1: THE SIMPLE VERSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def merge_sort(arr):
    """
    Sort using Merge Sort (Divide and Conquer).
    
    HOW TO READ THIS CODE:
    
    Line: if len(arr) <= 1: return arr
    WHY:  A list with 0 or 1 items is already sorted! This STOPS the recursion.
          Without this, the function would call itself FOREVER and crash.
    
    Line: mid = len(arr) // 2
    WHY:  Find the middle index. // means "integer division" (no decimals).
          For 7 items: mid = 7 // 2 = 3. Left gets items 0,1,2. Right gets 3,4,5,6.
    
    Line: left = merge_sort(arr[:mid])
    WHY:  arr[:mid] = "give me everything from start to mid" (a slice).
          We RECURSIVELY sort the left half. Trust that merge_sort works on smaller inputs!
    
    Line: right = merge_sort(arr[mid:])
    WHY:  arr[mid:] = "give me everything from mid to end".
          Recursively sort the right half.
    
    Line: return merge(left, right)
    WHY:  Both halves are now sorted. Merge them into one sorted list.
    """
    if len(arr) <= 1:               # BASE CASE: 0 or 1 items = sorted!
        return arr
    
    mid = len(arr) // 2             # Find the middle
    left = merge_sort(arr[:mid])    # Sort left half (recursion!)
    right = merge_sort(arr[mid:])   # Sort right half (recursion!)
    return merge(left, right)       # Merge two sorted halves


def merge(left, right):
    """
    Merge two SORTED lists into one sorted list.
    
    THE TECHNIQUE: Two pointers! 
    - 'i' points to the current item in 'left'
    - 'j' points to the current item in 'right'
    - Compare left[i] vs right[j], pick the smaller one
    - Advance that pointer
    - When one list runs out, dump the rest of the other
    
    VISUAL:
    Left:  [2, 5, 8]    Right: [1, 4, 7]
            ↑ i=0               ↑ j=0
    
    Compare 2 vs 1 → pick 1 (from right, advance j)
    Compare 2 vs 4 → pick 2 (from left, advance i)
    Compare 5 vs 4 → pick 4 (from right, advance j)
    ...and so on
    """
    result = []                     # This will hold our merged result
    i = 0                           # Pointer into left list
    j = 0                           # Pointer into right list
    
    # While BOTH lists still have items:
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:     # Left's front is smaller (or equal)?
            result.append(left[i])  # Pick from left
            i += 1                  # Advance left pointer
        else:
            result.append(right[j]) # Pick from right
            j += 1                  # Advance right pointer
    
    # One list is empty now. Dump the rest of the other.
    # .extend() adds ALL remaining items at once.
    result.extend(left[i:])         # Any leftovers from left
    result.extend(right[j:])        # Any leftovers from right
    
    return result


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 2: VERBOSE VERSION — Watch the recursion unfold!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def merge_sort_verbose(arr, depth=0):
    """Same algorithm but shows every split and merge."""
    indent = "  " * depth
    print(f"{indent}merge_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}  → base case! return {arr}")
        return arr
    
    mid = len(arr) // 2
    print(f"{indent}  splitting at mid={mid}: {arr[:mid]} | {arr[mid:]}")
    
    left = merge_sort_verbose(arr[:mid], depth + 1)
    right = merge_sort_verbose(arr[mid:], depth + 1)
    
    result = merge(left, right)
    print(f"{indent}  merging {left} + {right} → {result}")
    return result


print("=" * 60)
print("  MERGE SORT — Basic Test")
print("=" * 60)
print(f"  Result: {merge_sort([38, 27, 43, 3, 9, 82, 10])}")

print("\n" + "=" * 60)
print("  MERGE SORT — Watch the Recursion!")
print("=" * 60)
merge_sort_verbose([5, 2, 4, 1])


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PART 3: MERGE STEP TRACED IN DETAIL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def merge_verbose(left, right):
    """Merge with every comparison shown."""
    result = []
    i = j = 0
    step = 1
    print(f"  Merging {left} and {right}:")
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            print(f"    Step {step}: {left[i]} ≤ {right[j]} → pick {left[i]} from LEFT")
            result.append(left[i]); i += 1
        else:
            print(f"    Step {step}: {left[i]} > {right[j]} → pick {right[j]} from RIGHT")
            result.append(right[j]); j += 1
        step += 1
    if left[i:]: print(f"    Append remaining from LEFT: {left[i:]}")
    if right[j:]: print(f"    Append remaining from RIGHT: {right[j:]}")
    result.extend(left[i:])
    result.extend(right[j:])
    print(f"    Result: {result}")
    return result

print("\n" + "=" * 60)
print("  MERGE STEP — Detailed Trace")
print("=" * 60)
merge_verbose([1, 3, 5, 7], [2, 4, 6, 8])


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CHEAT SHEET
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
print("""
╔══════════════════════════════════════════════════════╗
║  MERGE SORT CHEAT SHEET                              ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  def merge_sort(arr):                                ║
║      if len(arr) <= 1: return arr   # Base case      ║
║      mid = len(arr) // 2                             ║
║      left = merge_sort(arr[:mid])   # Sort left      ║
║      right = merge_sort(arr[mid:])  # Sort right     ║
║      return merge(left, right)      # Combine        ║
║                                                      ║
║  MNEMONIC: "Split → Sort halves → Merge back"        ║
║  MERGE TRICK: "Always pick the smaller top card"     ║
║                                                      ║
║  TIME:  ALWAYS O(n log n)  (best = avg = worst)      ║
║  SPACE: O(n)  (needs temp arrays for merging)        ║
║  STABLE: Yes (use ≤ not < in merge comparison)       ║
║                                                      ║
║  RECURRENCE: T(n) = 2T(n/2) + O(n)                   ║
║  WHY O(n log n)? log n levels × n work per level     ║
╚══════════════════════════════════════════════════════╝
""")
