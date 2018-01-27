def longestContainedRange(nums):
    unprocessedEntries = nums[:]
    maxIntervalSize = 0
    while len(unprocessedEntries) > 0:
        a = unprocessedEntries.pop(0)
        lowerBound = a - 1
        while lowerBound in unprocessedEntries:
            unprocessedEntries.remove(lowerBound)
            lowerBound -= 1
        upperBound = a + 1
        while upperBound in unprocessedEntries:
            unprocessedEntries.remove(upperBound)
            upperBound += 1
        maxIntervalSize = max(maxIntervalSize, upperBound - lowerBound - 1)
    return maxIntervalSize


print longestContainedRange([3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8])
