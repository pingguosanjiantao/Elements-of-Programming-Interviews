def closestlntSameBitCount(x):
    for i in range(32 - 1):
        mask_1 = x >> i
        mask_2 = x >> (i + 1)
        if mask_1 & 1 != mask_2 & 2:
            # swap
            bitMask = (1 << i) | (1 << (i + 1))
            x ^= bitMask
            return x
    return None
x = 0b11111111101
print bin(closestlntSameBitCount(x))



