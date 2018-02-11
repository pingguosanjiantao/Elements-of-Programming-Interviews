def hasTwoSum(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] + nums[right] == target:
            return True
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return False


def hasThreeSum(nums, target):
    for key in nums:
        if hasTwoSum(nums, target - key):
            return True
    return False


print hasThreeSum([2, 3, 5, 7, 11], 19)
