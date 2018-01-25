import random


def findKth(nums, k):
    length = len(nums)
    left, right = 0, length - 1
    while left <= right:
        pivotIdx = random.randint(left, right)
        newIdx = partitionAroundPivot(nums, left, right, pivotIdx)
        if newIdx == k - 1:
            return nums[newIdx]
        elif newIdx > k - 1:
            right = newIdx - 1
        else:
            left = newIdx + 1
    return None


def partitionAroundPivot(nums, left, right, idx):
    key = nums[idx]  # pivot point

    nums[idx], nums[right] = nums[right], nums[idx]
    cur = left
    for i in range(left, right):
        if nums[i] < key:
            nums[i], nums[cur] = nums[cur], nums[i]
            cur += 1
    nums[cur], nums[right] = nums[right], nums[cur]
    return cur


nums = [3, 2, 1, 5, 4]
print findKth(nums, 4)
