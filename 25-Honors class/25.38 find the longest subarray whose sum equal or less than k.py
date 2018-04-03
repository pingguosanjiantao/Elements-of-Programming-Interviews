# coding:utf-8
def findLongestSubarrayLessEqualK(nums, k):
    prefixSum = []
    sums = 0
    for ele in nums:
        sums += ele
        prefixSum += [sums]
    if prefixSum[-1] <= k:
        return len(nums)
    minPrefixSum = prefixSum[:]
    for i in range(len(minPrefixSum) - 2, -1, -1):
        minPrefixSum[i] = min(minPrefixSum[i], minPrefixSum[i + 1])
    a, b = 0, 0
    maxLength = 0
    while a < len(nums) and b < len(nums):
        minCurrSum = minPrefixSum[b] - prefixSum[a - 1] if a > 0 else minPrefixSum[b]
        if minCurrSum <= k:
            curLength = b - a + 1
            maxLength = max(curLength, maxLength)
            b += 1
        else:
            a += 1
    return maxLength

print findLongestSubarrayLessEqualK([431, -15, 639, 342, -14, 565, -924, 635, 167, -70], 184)