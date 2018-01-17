def deleDulInArray(nums):
    if nums is None or len(nums) <= 1:
        return nums
    idx = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[idx] = nums[i]
            idx += 1
    return nums[:idx]


print deleDulInArray([1, 1, 2, 2, 3, 4, 4, 5])
