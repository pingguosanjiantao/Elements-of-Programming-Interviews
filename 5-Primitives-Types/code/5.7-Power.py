def power_integer(x, y):
    ret = 1
    power = y
    while power != 0:
        if power & 1 != 0:
            ret *= x
        x *= x
        power >>= 1
    return ret


def power_float(x, y):
    ret = 1.0
    power = y
    if y < 0:
        power = -power
        x = 1.0 / x
    while power != 0:
        if power & 1 != 0:
            ret *= x
        x *= x
        power >>= 1
    return ret


print power_integer(2, 3)
print power_float(2, -2)
