def replaceAndRemove(size, s):
    # remove 'b's and count the number of 'a's
    writeIdx, aCnt = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[writeIdx] = s[i]
            writeIdx += 1
        if s[i] == 'a':
            aCnt += 1
    # compute the final size and move the element backward
    curIdx = writeIdx - 1
    writeIdx = writeIdx + aCnt - 1
    finalSize = writeIdx + 1
    while curIdx >= 0:
        if s[curIdx] == 'a':
            s[writeIdx] = 'd'
            writeIdx -= 1
            s[writeIdx] = 'd'
            writeIdx -= 1
        else:
            s[writeIdx] = s[curIdx]
            writeIdx -= 1
        curIdx -= 1

    return s[:finalSize]


s = ['a', 'c', 'd', 'b', 'b', 'c', 'a', '-', '-', '-']
print replaceAndRemove(7, s)
