def findFirstMissingPositive(nums):
    if nums is None or len(nums) == 0:
        return None
    if len(nums) == 1:
        return 2 if nums[0] == 1 else 1
    for i in range(len(nums)):
        if nums[i] - 1 != i and nums[i] - 1 in range(len(nums)):
            idx = nums[i] - 1
            nums[idx], nums[i] = nums[i], nums[idx]
    for i in range(1, len(nums)):
        if nums[i] - 1 != i:
            return i + 1
    return len(nums) + 1


print findFirstMissingPositive([1, 3, 2, -1])
