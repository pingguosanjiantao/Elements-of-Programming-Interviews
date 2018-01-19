def decode(s):
    ret = 0
    for c in s:
        ret = ret * 26 + ord(c) - ord('A') + 1
    return ret


def encode(num):
    ret = ''
    while num > 0:
        ret = chr((num - 1) % 26 + ord('A')) + ret
        num = (num - 1) / 26
    return ret


print decode('AA')
print encode(27)
