# first approach is using hashtable
# second space complexity is O(1)
def findPairSumK(nums, k):
    ret = findPairInPosNeg(nums, k)
    if ret is None:
        if k > 0:
            return findPairInPositive(nums, k)
        else:
            return findPairInNegative(nums, k)
    return ret


def findPairInPositive(nums, k):
    left, right = 0, len(nums) - 1
    while left < right and nums[left] > 0:
        left += 1
    while left < right and nums[right] > 0:
        right -= 1
    while left < right:
        if nums[left] + nums[right] == k:
            return [left, right]
        elif nums[left] + nums[right] > k:
            left += 1
            while left < right and nums[left] > 0:
                left += 1
        else:
            right -= 1
            while left < right and nums[right] > 0:
                right -= 1


def findPairInNegative(nums, k):
    left, right = 0, len(nums) - 1
    while left < right and nums[left] < 0:
        left += 1
    while left < right and nums[right] < 0:
        right -= 1
    while left < right:
        if nums[left] + nums[right] == k:
            return [left, right]
        elif nums[left] + nums[right] < k:
            left += 1
            while left < right and nums[left] < 0:
                left += 1
        else:
            right -= 1
            while left < right and nums[right] < 0:
                right -= 1


def findPairInPosNeg(nums, k):
    left, right = len(nums) - 1, len(nums) - 1
    while left >= 0 and nums[left] < 0:
        left -= 1
    while right >= 0 and nums[right] >= 0:
        right -= 1
    while left >= 0 and right >= 0:
        if nums[left] + nums[right] == k:
            return [left, right]
        elif nums[left] + nums[right] > k:
            left -= 1
            while left >= 0 and nums[left] < 0:
                left -= 1
        else:
            right -= 1
            while right >= 0 and nums[right] >= 0:
                right -= 1
    return None

print findPairSumK([-49, 75, 103, -147, 164, -197, -238, 314, 348, -422], 123)