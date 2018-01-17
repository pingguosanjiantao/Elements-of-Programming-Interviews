import random

# the same with 6.11
def onlineRandomSampling(k, nums):
    ret = nums[:k]
    # actually it will be writing as 'nums.hasNext()', here we simplify it
    cnt = k
    for i in range(k, len(nums)):
        cnt += 1
        idx = random.randint(0, cnt)
        if idx < k:
            ret[idx] = nums[i]

    return ret


print onlineRandomSampling(3, [1, 2, 3, 4, 5])
