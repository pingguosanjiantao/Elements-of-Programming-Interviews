# optimal solution
def longestNondescSub(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[-1]


print longestNondescSub([0, 8, 4, 12, 2, 10, 6, 14, 1, 9])
