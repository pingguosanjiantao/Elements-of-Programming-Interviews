# optimal solution
def findDuplicateMissing(nums):
    missXORDup = 0
    length = len(nums)
    for i in range(length):
        missXORDup ^= (i ^ nums[i])
    diffBit = missXORDup & (~(missXORDup - 1))
    a, b = 0, 0
    for i in range(length):
        if (i & diffBit) != 0:
            a ^= i
        else:
            b ^= i
        if (nums[i] & diffBit) != 0:
            a ^= nums[i]
        else:
            b ^= nums[i]
    if a in nums:
        return [b, a]
    return [a, b]


print findDuplicateMissing([5, 3, 0, 3, 1, 2])
