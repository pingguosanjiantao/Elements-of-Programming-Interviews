def gcd_minus(x, y):
    if x == y:
        return x
    if x < y:
        x, y = y, x
    return gcd_minus(x - y, y)


def gcd_divide(x, y):
    if x == y:
        return x
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd_divide(y, x % y)


def gcd(x, y):
    if x == y:
        return x
    elif x & 1 == 0 and y & 1 == 0:
        return gcd(x >> 1, y >> 1) << 1
    elif x & 1 == 0 and y & 1 != 0:
        return gcd(x >> 1, y)
    elif x & 1 != 0 and y & 1 == 0:
        return gcd(x, y >> 1)

    if x < y:
        x, y = y, x
    return gcd(x - y, y)


print gcd_minus(10, 4)
print gcd_divide(10, 4)
print gcd(10, 4)
