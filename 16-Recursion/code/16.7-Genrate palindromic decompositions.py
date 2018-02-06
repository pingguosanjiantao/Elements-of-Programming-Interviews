def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left, right = left + 1, right - 1
    return True


def palindromePartition(s):
    def doPartition(s, begin, cur, ret):
        if begin == len(s):
            ret += [cur[:]]
            return
        for i in range(begin + 1, len(s) + 1):
            prefix = s[begin:i]
            if isPalindrome(prefix):
                cur += [prefix]
                doPartition(s, i, cur, ret)
                cur.pop()

    ret = []
    doPartition(s, 0, [], ret)
    return ret


print palindromePartition("02044")
