# coding=utf-8
def computeLeastTickets(nums):
    if nums is None or len(nums) == 0:
        return 0
    ret = [1] * len(nums)
    for i in range(0, len(nums) - 1):
        if nums[i] < nums[i + 1]:
            ret[i + 1] = max(ret[i], ret[i + 1]) + 1
    for i in range(len(nums) - 1, 1):
        if nums[i - 1] > nums[i]:
            ret[i - 1] = max(ret[i - 1], ret[i]) + 1
    return ret


print computeLeastTickets([300, 400, 500, 200])
