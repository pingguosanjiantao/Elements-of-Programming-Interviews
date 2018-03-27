def roteteArray(nums, k):
    if k < 0 or k >= len(nums):
        return None
    k -= 1
    inverseArray(nums, 0, k)
    inverseArray(nums, k + 1, len(nums) - 1)
    inverseArray(nums, 0, len(nums) - 1)
    return nums

def inverseArray(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1


print roteteArray([1, 2, 3, 4, 5, 6], 3)
