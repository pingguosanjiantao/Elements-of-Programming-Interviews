def permute(s):
    ret = []

    def doPermute(left, right):
        if left == right:
            ret.append(s[:])
        else:
            for i in range(left, right + 1):
                s[left], s[i] = s[i], s[left]
                doPermute(left + 1, right)
                s[left], s[i] = s[i], s[left]

    doPermute(0, len(s) - 1)
    return ret


print permute(['a', 'b', 'c'])
