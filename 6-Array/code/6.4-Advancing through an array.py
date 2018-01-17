# same with leetcode: forg jump
def canReachEnd(nums):
    canReachSoFar = 0
    for i in range(len(nums)):
        if i <= canReachSoFar:
            canReachSoFar = max(canReachSoFar, i + nums[i])
    return True if canReachSoFar >= len(nums) else False


print canReachEnd([3, 3, 1, 1, 2, 0, 1])
