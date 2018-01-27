def findSmallestSequentiallyCoveringSubset(words, keys):
    length = len(keys)
    keyToIdxMap = {}
    for i in range(length):
        keyToIdxMap[keys[i]] = i

    preIdxsList = [-1] * length  # last occurance
    subDis, minDis = [float('inf')] * length, float("inf")

    ret = []
    for i in range(len(words)):
        if keyToIdxMap.has_key(words[i]):
            keyIdx = keyToIdxMap.get(words[i])
            preKeyIdx = keyIdx - 1
            if keyIdx == 0:
                subDis[0] = 1
            # when the pre key dis is inf, it means not occured yet. update one bye one
            elif subDis[preKeyIdx] != float('inf'):
                j = preIdxsList[preKeyIdx]
                subDis[keyIdx] = subDis[preKeyIdx] + (i - j)
            preIdxsList[keyIdx] = i
            if keyIdx == length - 1 and subDis[-1] < minDis:
                minDis = subDis[-1]
                ret = [i - minDis + 1, i]
    return ret


print findSmallestSequentiallyCoveringSubset(['apple', 'pair', 'banana', 'cat', 'apple', 'grape'], ['banana', 'apple'])
