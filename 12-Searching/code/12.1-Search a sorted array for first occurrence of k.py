def searchFisrt(nums, key):
    left, right = 0, len(nums)
    ret = None
    while left < right:
        mid = (left + right) / 2
        if nums[mid] == key:
            ret = mid
            right -= 1
        elif nums[mid] > key:
            right = mid
        else:
            left = mid + 1
    return ret

print searchFisrt([-14, -10, 2, 108, 108, 243, 285, 285, 401], 285)
