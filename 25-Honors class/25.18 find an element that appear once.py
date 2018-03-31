# coding=utf-8
# amazing
def findAllAppearsTripleButOneOnce(nums):
    counter = [0] * 32
    for x in nums:
        for i in range(32):
            if x & (1 << i) != 0:
                counter[i] += 1
    ret = 0
    for i in range(32):
        ret |= (counter[i] % 3) * (1 << i)
    return ret


print findAllAppearsTripleButOneOnce([2, 4, 2, 5, 2, 5, 5])
