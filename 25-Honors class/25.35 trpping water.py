# coding:utf-8
def getTrappingWater(nums):
    if nums is None or len(nums) == 0:
        return 0
    maxValIdx = nums.index(max(nums))
    ret = 0
    leftMax = 0
    for i in range(maxValIdx):
        leftMax = max(leftMax, nums[i])
        ret += leftMax - nums[i]
    rightMax = 0
    for j in range(len(nums) - 1, maxValIdx, -1):
        rightMax = max(rightMax, nums[j])
        ret += rightMax - nums[j]
    return ret


print getTrappingWater([1, 2, 1, 3, 4, 5, 6, 1, 2, 0, 3])
