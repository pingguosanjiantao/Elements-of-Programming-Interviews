def divide(x, y):
    ret = 0
    while x >= y:
        cnt = -1  # cnt init to -1. As x >= y, it will be positive following
        divisor = y
        while x >= divisor:
            cnt += 1
            divisor <<= 1
        ret += 1 << cnt
        x -= y << cnt
    return ret


print divide(12, 4)
