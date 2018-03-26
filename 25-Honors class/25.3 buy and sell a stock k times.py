class Solution(object):
    def maxProfit(self, k, nums):
        length = len(nums)
        if length <= 0 or k < 1:
            return 0
        buy = [float('-inf') for _ in range(k + 1)]
        sell = [0 for _ in range(k + 1)]
        for i in range(length):
            for j in range(1, k + 1):
                buy[j] = max(sell[j - 1] - nums[i], buy[j])
                sell[j] = max(buy[j] + nums[i], sell[j])
        return max(max(buy), max(sell))

    def maxProfit_optimzed(self, k, nums):
        if k < 1:
            return 0
        if k > len(nums) / 2:
            maxNum = 0
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    maxNum += (nums[i + 1] - nums[i])
            return maxNum

        kSum = [float('-inf')] * (k * 2)
        for i in range(len(nums)):
            for j in range(min(i + 1, len(kSum))):
                diff = [-1, 1][j % 2] * nums[i] + (0 if j == 0 else kSum[j - 1])
                kSum[j] = max(diff, kSum[j])
        print kSum
        return kSum[-1]


k = 2
nums = [106, 373, 495, 477, 324]
print Solution().maxProfit(k, nums)
print Solution().maxProfit_optimzed(k, nums)
