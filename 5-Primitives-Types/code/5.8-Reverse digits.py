def reverseDigital(x):
    if x < 0:
        return -reverseDigital(-x)
    ret = 0
    while x != 0:
        ret = ret * 10 + x % 10
        x /= 10
    return ret


print reverseDigital(-98)
