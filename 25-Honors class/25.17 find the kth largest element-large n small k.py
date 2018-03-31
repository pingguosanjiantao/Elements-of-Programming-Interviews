# coding=utf-8
import random


# copied from 12.8
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


def findKthLargestWithUnknowLength(nums, k):
    queue = []
    for ele in nums:
        queue += [ele]
        if len(queue) == 2 * k - 1:
            findKth(queue, k)
            queue = queue[:k]
    findKth(queue, k)
    return queue[k - 1]


print findKthLargestWithUnknowLength([3, 2, 1, 8, 4, 9, 10, 32, 23], 8)
