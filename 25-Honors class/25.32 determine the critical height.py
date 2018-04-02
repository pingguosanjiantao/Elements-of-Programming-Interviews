# coding=utf-8
def getHeight(c, d):
    dp = [[0] * (d + 1)] * (c + 1)
    for j in range(d + 1):
        dp[1][j] = j
    for i in range(c + 1):
        for j in range(d + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 + dp[i][j - 1]
    return dp[-1][-1]
