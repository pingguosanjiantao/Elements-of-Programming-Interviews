def getPowerSet(nums):
    def doGetPowerSet(nums, begin, selected, ret):
        if begin == len(nums):
            ret += [selected[:]]
        else:
            selected += [nums[begin]]
            doGetPowerSet(nums, begin + 1, selected, ret)
            selected.pop()
            doGetPowerSet(nums, begin + 1, selected, ret)

    ret = []
    doGetPowerSet(nums, 0, [], ret)
    return ret


print getPowerSet([0, 1, 2])
