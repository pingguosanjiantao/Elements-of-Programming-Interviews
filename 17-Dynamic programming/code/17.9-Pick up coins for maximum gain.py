# optimal solution
# recursion version
def maxGain(coins):
    def doCompute(coins, a, b, dp):
        if a > b:
            return 0
        if dp[a][b] == 0:
            maxA = coins[a] + min(doCompute(coins, a + 2, b, dp), doCompute(coins, a + 1, b - 1, dp))
            maxB = coins[b] + min(doCompute(coins, a + 1, b - 1, dp), doCompute(coins, a, b - 2, dp))
            dp[a][b] = max(maxA, maxB)
        return dp[a][b]

    return doCompute(coins, 0, len(coins) - 1, [[0] * len(coins)] * len(coins))


coins = [5, 25, 10, 1]
print maxGain(coins)
