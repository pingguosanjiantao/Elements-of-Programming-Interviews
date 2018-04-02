# coding=utf-8
def findMaxSubarrayInCircularArray(nums):
    return max(findMaxSubarray(nums), sum(nums) - findMinSubarray(nums))


def findMaxSubarray(nums):
    ret, pre = float('-inf'), 0
    for ele in nums:
        pre = max(ele, pre + ele)
        ret = max(ret, pre)
    return ret


def findMinSubarray(nums):
    ret, pre = float('inf'), 0
    for ele in nums:
        pre = min(ele, pre + ele)
        ret = min(ret, pre)
    return ret


print findMaxSubarrayInCircularArray([10, -4, 5, -4, 10])
