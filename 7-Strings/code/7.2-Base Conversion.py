def convertBase(s, base):
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

    retBased = constructFromBase(ret, base)
    if isNegative:
        retBased = '-' + retBased
    return retBased


# Assume that input integer is positive
def constructFromBase(num, base):
    ret = ''
    while num > 0:
        digit = num % base
        num /= base
        ret = str(digit) + ret
    return '0' if len(ret) == 0 else ret


print constructFromBase(6, 6)

print convertBase('-28', 6)
