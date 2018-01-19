def strToint(s):
    if s is None or len(s) == 0:
        return None
    isNegative = True if s[0] == '-' else False
    if isNegative:
        s = s[1:]

    ret = 0
    for i in range(len(s)):
        digit = ord(s[i]) - ord('0')
        ret *= 10
        ret += digit

    if isNegative:
        ret = -ret
    return ret


def intToStr(num):
    isNegative = True if num < 0 else False
    if isNegative:
        num = -num
    ret = ''
    while num > 0:
        c = chr(ord('0') + num % 10)
        num /= 10
        ret = c + ret

    if isNegative:
        ret = '-' + ret
    return ret


print strToint("-59")
print intToStr(-123)
