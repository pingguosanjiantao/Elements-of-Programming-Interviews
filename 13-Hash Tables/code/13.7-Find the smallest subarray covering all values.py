def findSmallestSubarrayCoverSet(words, keys):
    keywords = {}
    for ele in keys:
        keywords[ele] = keywords.get(ele, 0) + 1
    remainToCover = len(keys)
    ret = []
    left, right = 0, 0
    while right < len(words):
        key = words[right]
        keyCount = keywords.get(key, None)
        if keyCount is not None:
            keyCount -= 1
            keywords[key] = keyCount
            if keyCount >= 0:
                remainToCover -= 1
        while remainToCover == 0:  # update the [left, right], then put the leftest in keys in map
            if len(ret) == 0 or (right - left) < (ret[1] - ret[0]):
                ret = [left, right]
            key = words[left]
            keyCount = keywords.get(key, None)
            if keyCount is not None:
                keyCount += 1
                keywords[key] = keyCount
                if keyCount > 0:
                    remainToCover += 1
            left += 1
        right += 1
    return ret


words = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 'apple', 'dog', 'banana', 'apple', 'apple', 'cat', 'dog']
keys = ['banana', 'cat']
print findSmallestSubarrayCoverSet(words, keys)
