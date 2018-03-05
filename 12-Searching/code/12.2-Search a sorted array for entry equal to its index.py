def searchEntryEqualToItsIndex(nums):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) / 2
        diff = nums[mid] - mid
        if diff == 0:
            return mid
        elif diff > 0:
            right = mid
        else:
            left = mid + 1
    return -1


#  [-2, -1, 0, 0, 2, 2, 3]
print searchEntryEqualToItsIndex([-2, -1, 2, 2, 3])
