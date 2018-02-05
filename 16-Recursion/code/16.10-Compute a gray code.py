def grayCode(n):
    if n == 0:
        return [0]
    grayCodePre = grayCode(n - 1)
    leadingBitOne = 1 << (n - 1)
    for i in range(len(grayCodePre) - 1, -1, -1):
        grayCodePre += [leadingBitOne | grayCodePre[i]]
    return grayCodePre
print grayCode(3)
