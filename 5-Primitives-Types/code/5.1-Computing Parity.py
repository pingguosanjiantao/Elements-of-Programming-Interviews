# brute-force algorithm
def computeParity_brute_force(x):
    ret = 0
    while x != 0:
        ret ^= (x & 1)
        x >>= 1
    return ret
# update by the numbers of 1s in x
def computeParity_numbers_of_1(x):
    ret = 0
    while x != 0:
        ret ^= 1
        x = x & (x - 1)
    return ret
# pre compute the fixed sub and merge the result
def computeParity_cache(x):
    preComputeParity = [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0]
    wordSize = 4
    mask = 0xF
    ret = 0
    for i in range(32/wordSize):
        ret ^= preComputeParity[(x >> (i * wordSize)) & mask]
    return ret
# shift with mask with the XORS
def computeParity_divide_and(x):
    x ^= (x >> 16)
    x ^= (x >> 8)
    x ^= (x >> 4)
    x ^= (x >> 2)
    x ^= (x >> 1)
    return x & 1

x = 1609
print computeParity_brute_force(x)
print computeParity_numbers_of_1(x)
print computeParity_cache(x)
print computeParity_divide_and(x)