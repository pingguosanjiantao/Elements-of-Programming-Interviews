# optimal solution
def maxWeightForThief(packages, weight):
    numPackages = len(packages)
    dp = [[0 for _ in range(weight + 1)] for _ in range(numPackages + 1)]
    for i in range(1, numPackages + 1):
        for j in range(1, weight + 1):
            dp[i][j] = dp[i - 1][j]
            k = j - packages[i - 1][0]
            if k >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + packages[i - 1][1])
    return dp[-1][-1]


# [weight, value]
print maxWeightForThief([[5, 60], [3, 50], [4, 70], [2, 30]], 5)
