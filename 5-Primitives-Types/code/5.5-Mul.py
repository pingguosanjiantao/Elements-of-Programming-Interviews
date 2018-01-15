def add(x, y):
    ret = x ^ y
    carry = x & y
    while carry != 0:
        x, y = ret, carry << 1
        ret = x ^ y
        carry = x & y
    return ret

def multiply(x, y):
    ret = 0
    while x != 0:
        if x & 1 != 0:
            ret = add(ret, y)
        x >>= 1
        y <<= 1
    return ret

print multiply(31,3)