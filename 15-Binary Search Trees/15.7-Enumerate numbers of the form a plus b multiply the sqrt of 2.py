import math


class ABSqrt2:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = a + b * math.sqrt(2)


def generateFirstKABSqrt(k):
    ret = [ABSqrt2(0, 0)]
    i, j = 0, 0
    for _ in range(1, k):
        eleI, eleJ = ret[i], ret[j]
        eleIPlus1 = ABSqrt2(eleI.a + 1, eleI.b)
        eleJPlusSqrt2 = ABSqrt2(eleJ.a, eleJ.b + 1)
        ret += [eleIPlus1 if eleIPlus1.val < eleJPlusSqrt2.val else eleJPlusSqrt2]
        if eleIPlus1.val == ret[-1].val:
            i += 1
        if eleJPlusSqrt2.val == ret[-1].val:
            j += 1
    return ret


print generateFirstKABSqrt(3)
