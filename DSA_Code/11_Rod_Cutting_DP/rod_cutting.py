# ╔══════════════════════════════════════════════════════════╗
# ║  🪵 ROD CUTTING — Dynamic Programming (Colab Ready)      ║
# ╚══════════════════════════════════════════════════════════╝
# STORY: Chocolate bar, different prices per size.
#        Try all cuts, REMEMBER best for smaller bars.
#        Build from small to big = bottom-up DP!
# MNEMONIC: "DP = Don't recompute, just look it uP!"

def rod_cutting(prices, n):
    """
    HOW TO READ THIS CODE:
    
    r[j] = best revenue for a rod of length j
    s[j] = best first cut for rod of length j
    
    for j in range(1, n+1):     → "Solve for length 1, then 2, then 3..."
        for i in range(1, j+1): → "Try cutting a piece of length i"
            revenue = prices[i] + r[j-i]  → "Price of piece i + best for remainder"
            if revenue > best: update!
    """
    r = [0] * (n + 1)    # r[j] = max revenue for length j
    s = [0] * (n + 1)    # s[j] = optimal first cut for length j
    
    print(f"  Prices: {prices[1:]}")
    print(f"  {'j':>3} | {'Tries (i: price[i]+r[j-i])':40} | {'Best':>5} | Cut")
    print(f"  {'─'*3}-+-{'─'*40}-+-{'─'*5}-+{'─'*5}")
    
    for j in range(1, n + 1):
        best = float('-inf')
        tries = []
        for i in range(1, j + 1):
            revenue = prices[i] + r[j - i]
            tries.append(f"i={i}: {prices[i]}+{r[j-i]}={revenue}")
            if revenue > best:
                best = revenue
                s[j] = i
        r[j] = best
        print(f"  {j:>3} | {', '.join(tries):40} | ${best:>4} | {s[j]}")
    
    # Reconstruct
    cuts = []
    remaining = n
    while remaining > 0:
        cuts.append(s[remaining])
        remaining -= s[remaining]
    
    return r[n], cuts

print("="*60)
print("  ROD CUTTING — Detailed Trace")
print("="*60)
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
for n in [4, 7, 10]:
    print(f"\n--- Rod of length {n} ---")
    rev, cuts = rod_cutting(prices, n)
    print(f"  Result: max revenue = ${rev}, cuts = {cuts}")
    print(f"  Verify: {' + '.join(f'${prices[c]}' for c in cuts)} = ${sum(prices[c] for c in cuts)}")

print("""
╔══════════════════════════════════════════════════╗
║  ROD CUTTING CHEAT SHEET                         ║
╠══════════════════════════════════════════════════╣
║  r[j] = max(p[i] + r[j-i]) for i=1..j            ║
║  Base: r[0] = 0                                  ║
║  Track s[j] for cut reconstruction               ║
║  TIME: O(n^2)  SPACE: O(n)                       ║
║  MNEMONIC: "Try all first cuts, reuse answers"   ║
╚══════════════════════════════════════════════════╝
""")
