def eleminateDuplicate(nums):
    idx, i = 1, 0
    nums.sort()
    while i < len(nums):
        if i > 0:
            if nums[i] != nums[i - 1]:
                nums[idx] = nums[i]
                idx += 1

        i += 1
    return nums[:idx]


print eleminateDuplicate([1, 1, 1, 2, 2, 3, 4, 4, 4])
