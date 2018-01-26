# optimal solution
def findDuplicateMissing(nums):
    missXORDup = 0
    length = len(nums)
    for i in range(length):
        missXORDup ^= (i ^ nums[i])
    diffBit = missXORDup & (~(missXORDup - 1))
    miss, dup = 0, 0
    for i in range(length):
        if (i & diffBit) != 0:
            miss ^= i
        else:
            dup ^= i
        if (nums[i] & diffBit) != 0:
            miss ^= nums[i]
        else:
            dup ^= nums[i]

    return [miss, dup]


print findDuplicateMissing([5, 3, 0, 3, 1, 2])
