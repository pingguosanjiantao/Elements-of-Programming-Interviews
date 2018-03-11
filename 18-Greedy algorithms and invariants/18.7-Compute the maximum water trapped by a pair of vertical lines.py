def getMaxTrappedWater(nums):
    i, j = 0, len(nums) - 1
    ret = 0
    while i < j:
        ret = max(ret, (j - i) * min(nums[i], nums[j]))
        if nums[i] > nums[j]:
            j -= 1
        elif nums[i] < nums[j]:
            i += 1
        else:
            i, j = i + 1, j - 1
    return ret


# leetcode 42
def trap(nums):
    if nums is None or len(nums) <= 2:
        return 0

    ret = 0
    left, right = 0, len(nums) - 1
    maxLeft, maxRight = 0, 0
    while left < right:
        maxLeft, maxRight = max(maxLeft, nums[left]), max(maxRight, nums[right])
        if nums[left] < nums[right]:
            ret += maxLeft - nums[left]
            left += 1
        else:
            ret += maxRight - nums[right]
            right -= 1
    return ret


print getMaxTrappedWater([1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1])
print trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
