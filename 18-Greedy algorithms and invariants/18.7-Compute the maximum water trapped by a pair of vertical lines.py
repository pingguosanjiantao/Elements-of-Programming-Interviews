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


print getMaxTrappedWater([1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1])
