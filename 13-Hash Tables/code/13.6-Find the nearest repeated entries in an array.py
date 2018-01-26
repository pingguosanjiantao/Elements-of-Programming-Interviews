def findNearestRepetition(nums):
    lastestIndex = {}
    nearest = float("inf")
    for i in range(len(nums)):
        cur = nums[i]
        if lastestIndex.has_key(cur):
            nearest = min(nearest, i - lastestIndex(cur))
        lastestIndex[cur] = i
    return nearest

