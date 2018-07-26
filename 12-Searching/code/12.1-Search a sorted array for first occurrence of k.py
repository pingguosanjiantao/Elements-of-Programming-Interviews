def searchFisrt(nums, key):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) / 2
        if nums[mid] == key:
            right -= 1
        elif nums[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left


nums = [-14, -14, -14, -14, -14, 4]
for n in nums:
    print searchFisrt(nums, n)
