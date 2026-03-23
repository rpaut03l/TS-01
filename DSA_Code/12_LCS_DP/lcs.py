# ╔══════════════════════════════════════════════════════════╗
# ║  🔗 LCS — Longest Common Subsequence (Colab Ready)       ║
# ╚══════════════════════════════════════════════════════════╝
# STORY: Two necklaces of beads. Find longest chain
#        that appears IN ORDER in BOTH (can skip beads).
# MNEMONIC: "Match? Diagonal+1. Miss? Max(Up, Left)"

def lcs(X, Y):
    """
    HOW TO READ THIS CODE:
    
    c[i][j] = LCS length of first i chars of X and first j chars of Y
    
    Three cases at each cell:
    1. X[i-1]==Y[j-1] → MATCH! → c[i][j] = c[i-1][j-1] + 1
       "Last chars are same → count it, check the rest"
    
    2. X[i-1]!=Y[j-1] → NO MATCH → c[i][j] = max(c[i-1][j], c[i][j-1])
       "Last chars different → skip one or the other, take the better"
    """
    m, n = len(X), len(Y)
    c = [[0]*(n+1) for _ in range(m+1)]
    
    # Fill the table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    
    # Print the table
    print(f"\n  DP Table:")
    print(f"      {'':>3}", end="")
    for ch in Y: print(f"{ch:>3}", end="")
    print()
    for i in range(m+1):
        label = " " if i==0 else X[i-1]
        print(f"  {label:>3}", end="")
        for j in range(n+1):
            print(f"{c[i][j]:>3}", end="")
        print()
    
    # Reconstruct
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            result.append(X[i-1])
            i -= 1; j -= 1
        elif c[i-1][j] >= c[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    lcs_str = ''.join(reversed(result))
    return c[m][n], lcs_str

print("="*50)
print("  LCS — Longest Common Subsequence")
print("="*50)
for X, Y in [("ABCBDAB","BDCABA"), ("ABCB","BDCAB"), ("AGGTAB","GXTXAYB")]:
    length, seq = lcs(X, Y)
    print(f"\n  X = '{X}', Y = '{Y}'")
    print(f"  LCS = '{seq}' (length {length})")

print("""
╔══════════════════════════════════════════════════╗
║  LCS CHEAT SHEET                                 ║
╠══════════════════════════════════════════════════╣
║  Match → c[i][j] = c[i-1][j-1] + 1 (diagonal)    ║
║  Miss  → c[i][j] = max(c[i-1][j], c[i][j-1])     ║
║  Base  → c[0][j] = c[i][0] = 0                   ║
║  TIME: O(m*n)  SPACE: O(m*n)                     ║
║  Reconstruct: trace back from c[m][n]            ║
╚══════════════════════════════════════════════════╝
""")
