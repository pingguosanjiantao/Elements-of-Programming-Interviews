# coding:utf-8
def findLongestSubarrayLessEqualK(nums, k):
    sums = [0] * len(nums)
    for i in range(len(nums)):
        sums[i] = sums[i - 1] + nums[i]

    minSumRight = sums[:]  # the minum from right to left
    for i in range(len(minSumRight) - 1)[::-1]:
        minSumRight[i] = min(minSumRight[i], minSumRight[i + 1])

    i, j = 0, 0
    ans = 0
    while i < len(nums) and j < len(nums):
        minCurrSum = minSumRight[j] - sums[i - 1] if i > 0 else minSumRight[j]
        if minCurrSum <= k:
            ans = max(ans, j - i + 1)
            j += 1
        else:  # maybe has a shorter result
            i += 1
    return ans


nums = [1, 3, 4, -1, 5, 2, 7, -5]
k = 16
print findLongestSubarrayLessEqualK(nums, k)
