# the core is shuffle algorithm
import random


def randomSampling(k, nums):
    for i in range(k):
        idx = i + random.randint(0, len(nums) - i)
        nums[idx], nums[i] = nums[i], nums[idx]
    print nums[:k]


print randomSampling(3, [1, 2, 3, 4, 5])
