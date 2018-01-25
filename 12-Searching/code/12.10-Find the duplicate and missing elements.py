def findDuplicateMissing(nums):
    missXORDup = 0
    length = len(nums)
    for i in range(length):
        missXORDup ^= (i ^ nums[i])
    diffBit = missXORDup & (~(missXORDup - 1))
    missOrDup = 0
    for i in range(length):
        if (i & diffBit) != 0:
            missOrDup ^= i
        if (nums[i] & diffBit) != 0:
            missOrDup ^= nums[i]
    for ele in nums:
        if ele == missOrDup:
            return [missOrDup, missOrDup ^ missXORDup]
    return [missOrDup ^ missXORDup, missOrDup]


print findDuplicateMissing([5, 3, 0, 3, 1, 2])
