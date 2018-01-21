def encoding(s):
    ret = []
    cnt = 1
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            ret += [str(cnt), s[i - 1]]
            cnt = 1
        else:
            cnt += 1
    return ''.join(ret)


def decoding(s):
    cnt = 0
    ret = []
    for c in s:
        if c.isdigit():
            cnt = int(c)
        else:
            ret += [c] * cnt
    return ''.join(ret)


print encoding('ccccaaaaaabbbbb')
print decoding('4c6a5b')
