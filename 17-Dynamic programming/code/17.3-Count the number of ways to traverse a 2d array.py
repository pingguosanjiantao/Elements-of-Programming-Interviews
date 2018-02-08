# optimal solution
def computeWays(m, n):
    if m == 0 or n == 0:
        return 1
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[-1][-1]


print computeWays(5, 5)
