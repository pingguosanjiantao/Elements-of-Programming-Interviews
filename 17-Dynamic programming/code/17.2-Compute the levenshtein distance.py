def computeEditDistance(a, b):
    if len(a) is 0:
        return len(b)
    if len(b) is 0:
        return len(a)

    rows, cols = len(a) + 1, len(b) + 1

    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        dp[i][0] = i
    for j in range(cols):
        dp[0][j] = j
    for i in range(1, rows):
        for j in range(1, cols):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1
    return dp[-1][-1]


print computeEditDistance('orchestra', 'carthorse')
