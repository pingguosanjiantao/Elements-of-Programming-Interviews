# coding:utf-8
def findLongestSubarrayLessEqualK(nums, k):
    length = len(nums)

    sums = [0] * length
    for i in range(length):
        sums[i] = sums[i - 1] + nums[i]

    minSumRight = sums[:]  # the minum from right to left
    for i in range(length - 1)[::-1]:
        minSumRight[i] = min(minSumRight[i], minSumRight[i + 1])

    sums += [0]

    i, j = -1, 0
    ans = 0
    while i < length and j < length:
        while j < len(nums) and minSumRight[j] - sums[i] <= k:
            ans = max(ans, j - i)
            j += 1
        i += 1
    return ans


nums = [1, 3, 4, -1, 5, 2, 7, -5]
k = 8
print findLongestSubarrayLessEqualK(nums, k)
