import random


# p is the probabilitesm like [0.2, 0.3, 0.4, 0.1]
def nonuniformRandomGenerator(nums, p):
    preSumOfP = [0] * (len(p) + 1)
    for i in range(len(p)):
        preSumOfP[i + 1] = preSumOfP[i] + p[i]
    uniform01 = random.random()

    # search zone differs from binary search node,
    # [a, b)
    def binarySearch(nums, left, right, target):
        if target == right:
            return right - 1
        while left < right:
            mid = (left + right) / 2
            if left + 1 == right:
                return left
            elif target < nums[mid]:
                right = mid
            else:
                left = mid
        return left

    idx = binarySearch(preSumOfP, 0, len(preSumOfP) - 1, uniform01)
    return nums[idx - 1]


counter = {}
for _ in range(1000):
    k = nonuniformRandomGenerator([0, 1, 2, 3], [0.1, 0.4, 0.3, 0.2])
    counter[k] = counter.get(k, 0) + 1
print counter
