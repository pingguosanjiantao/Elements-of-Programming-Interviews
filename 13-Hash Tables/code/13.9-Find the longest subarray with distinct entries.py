def longestSubarrayWithDistinctEntries(nums):
    preOccurance = {}
    longestSubStartIdx, ret = 0, 0
    for i in range(len(nums)):
        if preOccurance.has_key(nums[i]):
            idx = preOccurance[nums[i]]
            if idx >= longestSubStartIdx:
                ret = max(ret, i - longestSubStartIdx)
                longestSubStartIdx = idx + 1
        preOccurance[nums[i]] = i
    ret = max(ret, len(nums) - longestSubStartIdx)
    return ret


print longestSubarrayWithDistinctEntries(['f', 's', 'f', 'e', 't', 'w', 'e', 'n', 'w', 'e'])
