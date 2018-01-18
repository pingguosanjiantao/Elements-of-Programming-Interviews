import random


# this method is copies from 6.11
def randomSampling(k, nums):
    for i in range(k):
        idx = i + random.randint(0, len(nums) - 1 - i)
        nums[idx], nums[i] = nums[i], nums[idx]
    return nums[:k]


def randomSubset(k, n):
    nums = [i for i in range(n)]
    return randomSampling(k, nums)


print randomSubset(3, 5)
