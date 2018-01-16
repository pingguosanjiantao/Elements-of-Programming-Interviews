import random


def uniformRandom(lower, upper):
    interval = upper - lower + 1
    ret = 0
    i = 0
    while (1 << i) < interval:
        ret = (ret << 1) | random.randint(0, 1)
        i += 1
    # if not satisfied,  do again
    if ret >= interval:
        return uniformRandom(lower, upper)
    return ret + lower


print uniformRandom(0, 5)
