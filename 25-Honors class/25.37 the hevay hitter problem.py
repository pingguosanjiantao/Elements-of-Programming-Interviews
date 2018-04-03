# coding:utf-8
# find the item frequet more than k times
def searchFrequentItem(nums, k):
    hashMap = {}
    for ele in nums:
        hashMap[ele] = hashMap.get(ele, 0) + 1
        if len(hashMap) == k:
            for key, value in hashMap.items():
                if value == 1:
                    del hashMap[key]
                else:
                    hashMap[key] -= 1
    for key in hashMap.keys():
        hashMap[key] = 0
    for ele in nums:
        if ele in hashMap:
            hashMap[ele] += 1
    ret = []
    for key, value in hashMap.items():
        if value >= k:
            ret += [key]
    return ret


print searchFrequentItem([1, 2, 3, 4, 5, 6, 7, 8, 2, 1, 1, 2], 3)
