# using a cache
def reverseBits_cache(x):
    precomputedReverse = [0b0000,0b1000,0b0100,0b1100,
                          0b0010,0b1010,0b0110,0b1110,
                          0b0001,0b1001,0b0101,0b1101,
                          0b0011,0b1011,0b0111,0b1111]
    wordSize = 4
    bitMask = 0xF
    ret = 0
    for i in range(32 / wordSize):
        ret <<= wordSize
        ret |= precomputedReverse[((x >> i * wordSize) & bitMask)]
    return ret

print bin(reverseBits_cache(0b10010))