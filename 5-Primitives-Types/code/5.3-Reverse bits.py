# brute-force
def reverseBits(x):
    i = 0
    while (x >> i) != 0:
        mask = (1 << i)
        if x & mask == 0:
            x |= mask
        else:
            x &= ~mask
        i += 1
    return x


# using a cache
def reverseBits_cache(x):
    precomputedReverse = [0b0, 0b0, 0b1, 0b0, 0b11, 0b10, 0b1, 0b0, 0b111, 0b110, 0b101, 0b100, 0b11, 0b10, 0b1, 0b0]
    wordSize = 4
    bitMask = 0xF
    ret = 0
    for i in range(32 / wordSize):
        ret |= precomputedReverse[((x >> i * wordSize) & bitMask)] << ((32 / wordSize - 1 - i) * wordSize)
    return ret

print bin(reverseBits_cache(0b1111000011110000))
