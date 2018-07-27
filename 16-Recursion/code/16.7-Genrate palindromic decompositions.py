def isPalindrome(s):
    return s == s[::-1]


def palindromePartition(s):
    def doPartition(s, begin):
        if begin == len(s):
            ret.append(path[:])
            return
        for i in range(begin + 1, len(s) + 1):
            prefix = s[begin:i]
            if isPalindrome(prefix):
                path.append(prefix)
                doPartition(s, i)
                path.pop()

    path = []
    ret = []
    doPartition(s, 0)
    return ret


print palindromePartition("02044")
