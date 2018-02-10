# optimal solution
def miniPath(triangle):
    rows = len(triangle)
    if rows == 0:
        return 0
    dp = [float('inf') for _ in range(rows)]
    dp[0] = triangle[0][0]
    for i in range(1, rows):
        pre = dp[:i]
        for j in range(i + 1):
            if j == 0:
                dp[j] = pre[j] + triangle[i][j]
            elif j == i:
                dp[j] = pre[-1] + triangle[i][j]
            else:
                dp[j] = min(pre[j], pre[j - 1]) + triangle[i][j]
    return min(dp)


triangle = [
    [2],
    [4, 4],
    [8, 5, 6],
    [4, 2, 6, 2],
    [1, 5, 2, 3, 4]
]
print miniPath(triangle)
