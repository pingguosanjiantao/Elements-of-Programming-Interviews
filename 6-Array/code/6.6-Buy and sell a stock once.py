def computeMaxProfit(nums):
    minPrice, maxProfit = float("inf"), 0
    for ele in nums:
        minPrice = min(minPrice, ele)
        maxProfit = max(maxProfit, ele - minPrice)
    return maxProfit


print computeMaxProfit([3, 2, 1, 0, 3, 2, 1])
