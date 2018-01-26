def getKmostFrequent(nums, k):
    counter = {}
    for ele in nums:
        counter[ele] = counter.get(ele, 0) + 1

    ret = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return [e[0] for e in ret[:k]]


print getKmostFrequent([1, 1, 1, 2, 2, 2, 2, 3, 3], 2)
