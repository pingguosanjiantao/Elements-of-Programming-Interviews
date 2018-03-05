import random


def findKth(nums, k):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivotIdx = random.randint(left, right)
        newIdx = partitionByIdx(nums, left, right, pivotIdx)
        if newIdx == k - 1:
            return nums[newIdx]
        elif newIdx > k - 1:
            right = newIdx - 1
        else:
            left = newIdx + 1
    return None


# [left, right]
def partitionByIdx(nums, left, right, idx):
    key = nums[idx]  # pivot point

    nums[idx], nums[right] = nums[right], nums[idx]
    newIdx = partitionByKey(nums, left, right, key)
    nums[newIdx], nums[right] = nums[right], nums[newIdx]

    return newIdx


# [left, right)
def partitionByKey(nums, left, right, key):
    cur = left
    for i in range(left, right):
        if nums[i] < key:
            nums[i], nums[cur] = nums[cur], nums[i]
            cur += 1
    return cur


nums = [3, 2, 1, 8, 4]
print findKth(nums, 5)
