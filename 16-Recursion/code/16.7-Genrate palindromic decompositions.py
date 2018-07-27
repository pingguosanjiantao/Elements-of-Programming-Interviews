def isPalindrome(s):
    return s == s[::-1]


def palindromePartition(s):
    def doPartition(s, begin, cur):
        if begin == len(s):
            ret.append(cur[:])
            return
        for i in range(begin + 1, len(s) + 1):
            prefix = s[begin:i]
            if isPalindrome(prefix):
                cur += [prefix]
                doPartition(s, i, cur)
                cur.pop()

    ret = []
    doPartition(s, 0, [])
    return ret


print palindromePartition("02044")
