# optimal solution
def computeBinomialCoefficients(n, k):
    if k == 0 or n == k:
        return 1
    dp = [[0 for _ in range(k)] for _ in range(n)]
    for i in range(n):
        for j in range(min(k, i + 1)):
            if j == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
    return dp[-1][-1]


print computeBinomialCoefficients(5, 4)
