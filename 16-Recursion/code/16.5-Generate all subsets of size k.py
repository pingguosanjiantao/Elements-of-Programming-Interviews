def combination(n, k):
    def doCombination(nums, begin, cur, ret, k):
        if len(cur) == k:
            ret += [cur[:]]
        else:
            for i in range(begin, len(nums)):
                cur += [nums[i]]
                doCombination(nums, i + 1, cur, ret, k)
                cur.pop()

    ret = []
    doCombination([i for i in range(1, n + 1)], 0, [], ret, k)
    return ret


print combination(5, 2)
