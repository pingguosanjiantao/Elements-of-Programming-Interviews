def computeLongestContiguousIncreasingSubarray(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        if i > 0:
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
    maxCnt = max(dp)
    maxEndIdx = dp.index(maxCnt)
    return nums[maxEndIdx - maxCnt + 1:maxEndIdx + 1]


print computeLongestContiguousIncreasingSubarray([2, 11, 3, 5, 13, 7, 19, 17, 23])
