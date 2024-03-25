import sys

def min_lift_cost(L):
    n = len(L)
    dp = [float('inf')] * n
    dp[0] = 0
    max_reachable = 0
    
    for i in range(n):
        max_reachable = max(max_reachable, i + L[i])
        
        for j in range(i + 1, min(max_reachable + 1, n)):
            dp[j] = min(dp[j], dp[i] + 1)
    
    return dp[-1]
    
L = []
for line in sys.stdin:
    line = line.strip().upper()
    
    if line == "END":
        break

    L.append(int(line))

result = min_lift_cost(L)
print(result)