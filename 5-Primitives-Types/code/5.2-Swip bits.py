# bit-fiddling idioms
def swipBits_bit_fiddling(x, i, j):
    # extract the i-th and j-th bits, and see if they differ
    if ((x >> i) & 1) != ((x >> j) & 1):
        bitMask = (1 << i) | (1 << j)
        x ^= bitMask
    return x


x = 0b11000
print bin(swipBits_bit_fiddling(x, 4, 3))
