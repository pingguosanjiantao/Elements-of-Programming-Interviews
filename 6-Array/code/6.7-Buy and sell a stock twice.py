def buyAndSellStockTwice(nums):
    firstProfit, secondProfit = [0] * len(nums), [0] * len(nums)
    minPrice, maxPrice = float("inf"), float("-inf")
    # toward
    maxProfit = 0
    for i in range(len(nums)):
        curPrice = nums[i]
        minPrice = min(minPrice, curPrice)
        maxProfit = max(maxProfit, curPrice - minPrice)
        firstProfit[i] = maxProfit
    # backward
    maxProfit = 0
    for i in range(len(nums) - 1, -1, -1):
        curPrice = nums[i]
        maxPrice = max(maxPrice, curPrice)
        maxProfit = max(maxProfit, maxPrice - curPrice)
        secondProfit[i] = maxProfit
    totalProfit = map(lambda (x, y): x + y, zip(firstProfit, secondProfit))
    return max(totalProfit)


print buyAndSellStockTwice([12, 11, 13, 9, 12, 8, 14, 13, 15])
