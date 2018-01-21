def lookAndSay(n):
    def nextNumber(s):
        ret = []
        i = 0
        while i < len(s):
            key, cnt = s[i], 0
            while i < len(s) and s[i] == key:
                i += 1
                cnt += 1
            ret += [str(cnt), key]
        return ''.join(ret)

    s = '1'
    for i in range(n):
        s = nextNumber(s)
    return s


print lookAndSay(5)
