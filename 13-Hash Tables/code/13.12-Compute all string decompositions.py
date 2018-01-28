from collections import Counter


# assume all strings in the keys array have same length
def findAllSubstrings(s, keys):
    keysCnt = Counter()
    for key in keys:
        keysCnt[key] += 1
    keySize = len(keys[0])
    step = keySize * len(keys)
    ret = []
    i = 0
    while i + step < len(s):
        curStrCnt = Counter()
        for j in range(keySize):
            curStr = s[i + j * keySize: i + (j + 1) * keySize]
            curCnt = keysCnt[curStr]  # get the keys cnt
            if curCnt == 0:
                break
            curStrCnt[curStr] += 1
            if curStrCnt[curStr] > curCnt:
                break
            ret += [s[i:i + step]]
            break
        i += 1
    return ret


print findAllSubstrings('amanaplanacanal', ['can', 'apl', 'ana'])
