# ╔══════════════════════════════════════════════════════════╗
# ║  📅 GREEDY ACTIVITY SELECTION — Colab Ready              ║
# ╚══════════════════════════════════════════════════════════╝
# STORY: One TV, many shows. Pick MOST shows without overlap.
#        Always pick show that ENDS soonest — leaves most room!
# MNEMONIC: "Greedy = Grab what Goes away first"

def activity_selection(activities):
    """
    HOW TO READ THIS CODE:
    
    sorted(..., key=lambda x: x[1])
        → Sort by the SECOND element (finish time). 
        → lambda x: x[1] means "for each tuple x, use x[1] as the sort key"
        → This is the CRUCIAL step! We sort by FINISH time, not start time.
    
    if start >= last_finish:
        → "Does this activity start at or after the last one finished?"
        → If YES → compatible! Pick it!
        → If NO → overlaps. Skip it.
    """
    # Sort by FINISH time (earliest finish first)
    sorted_acts = sorted(activities, key=lambda x: x[1])
    
    print(f"  Sorted by finish time:")
    for i, (s,f,name) in enumerate(sorted_acts):
        print(f"    {name}: [{s}, {f})")
    print()
    
    # Always pick the first (earliest-finishing) activity
    selected = [sorted_acts[0]]
    last_finish = sorted_acts[0][1]
    print(f"  SELECT {sorted_acts[0][2]} [{sorted_acts[0][0]},{sorted_acts[0][1]}). last_finish = {last_finish}")
    
    # Scan remaining activities
    for start, finish, name in sorted_acts[1:]:
        if start >= last_finish:    # Compatible?
            selected.append((start, finish, name))
            last_finish = finish
            print(f"  SELECT {name} [{start},{finish}). last_finish = {last_finish}")
        else:
            print(f"  skip   {name} [{start},{finish}) — overlaps! (starts {start} < {last_finish})")
    
    return selected

print("="*60)
print("  GREEDY ACTIVITY SELECTION — Step by Step")
print("="*60)
activities = [
    (1,4,"A"), (3,5,"B"), (0,6,"C"), (5,7,"D"),
    (3,9,"E"), (5,9,"F"), (6,10,"G"), (8,11,"H"),
    (8,12,"I"), (2,14,"J"), (12,16,"K"),
]
result = activity_selection(activities)
print(f"\n  Result: {len(result)} activities selected!")
for s,f,name in result:
    bar = "█" * (f - s)
    spaces = " " * s
    print(f"    {name}: {spaces}{bar} [{s},{f})")

print("""
╔══════════════════════════════════════════════════╗
║  GREEDY ACTIVITY SELECTION CHEAT SHEET           ║
╠══════════════════════════════════════════════════╣
║  1. Sort by FINISH time (NOT start time!)        ║
║  2. Pick first activity (earliest finish)        ║
║  3. Skip overlapping, pick next compatible       ║
║  TIME: O(n log n) for sort + O(n) scan           ║
║  PROVABLY OPTIMAL for unweighted version         ║
║  ❌ Fails for weighted! → use DP instead         ║
║  MNEMONIC: "Grab what Goes away first"           ║
╚══════════════════════════════════════════════════╝
""")
