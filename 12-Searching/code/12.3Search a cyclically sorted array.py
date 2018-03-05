def searchSmallest(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) / 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

def searching(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) / 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            if target >= nums[left]:
                right = mid
            else:
                left = mid + 1
        else:
            if target < nums[right - 1]:
                left = mid + 1
            else:
                right = mid
    return -1

print searching([2], 3)

print searchSmallest([3, 4, 5, 6, 1, 2])
