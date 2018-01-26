def searchSmallest(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) / 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


print searchSmallest([3, 4, 5, 6, 1, 2])
