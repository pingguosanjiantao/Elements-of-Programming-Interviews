def getPowerSet(nums):
    def doGetPowerSet(nums, begin, selected, ret):
        if begin == len(nums):
            ret += [selected[:]]
            return
        selected += [nums[begin]]
        doGetPowerSet(nums, begin + 1, selected, ret)
        selected.pop()
        doGetPowerSet(nums, begin + 1, selected, ret)

    ret = []
    doGetPowerSet(nums, 0, [], ret)
    return ret


# optimal solution using bit
def getSubset(nums):
    length = 2 ** len(nums)
    ret = []
    for i in range(length):
        cur = []
        for j in range(length):
            if (1 << j) & i != 0:
                cur += [nums[j]]
        ret += [cur]
    return ret


# print getPowerSet([0, 1, 2, 3])

print getSubset([0, 1, 2, 3])
