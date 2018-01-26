def findMinMax(nums):
    length = len(nums)
    if length <= 1:
        return [nums[0], nums[0]]
    if nums[0] < nums[1]:
        minVal, maxVal = nums[0], nums[1]
    else:
        minVal, maxVal = nums[1], nums[0]
    for i in range(2, length, 2):
        if i + 1 < length:
            minVal = min(minVal, min(nums[i], nums[i + 1]))
            maxVal = max(maxVal, max(nums[i], nums[i + 1]))
    if length % 2 != 0:
        minVal = min(minVal, nums[length - 1])
        maxVal = max(maxVal, nums[length - 1])
    return [minVal, maxVal]


print findMinMax([3, 2, 5, 1, 2, 4])
