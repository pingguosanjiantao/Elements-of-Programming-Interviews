def findCombinations(score, samples):
    dp = [[0 for _ in range(score + 1)] for _ in range(len(samples))]
    for i in range(len(samples)):
        dp[i][0] = 1
        for j in range(1, score + 1):
            upComb = dp[i - 1][j] if i >= 1 else 0
            comb = dp[i][j - samples[i]] if j >= samples[i] else 0
            dp[i][j] = upComb + comb
    return dp[-1][-1]

print findCombinations(12, [2,3,7])