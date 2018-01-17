# brute-force, just for positive integer arrays
def multiply_array_positive(x, y):
    ret = [0] * (len(x) + len(y))
    for i in range(len(x) - 1, -1, -1):
        for j in range(len(y) - 1, -1, -1):
            ret[i + j + 1] += x[i] * y[j]
            ret[i + j] += ret[i + j + 1] / 10
            ret[i + j + 1] = ret[i + j + 1] % 10
    for i in range(len(x) + len(y)):
        if ret[i] != 0:
            return ret[i:]
    return ret


# brute-force
def multiply_array(x, y):
    isNegative = True if (x[0] > 0) ^ (y[0] > 0) == 1 else False
    x[0], y[0] = abs(x[0]), abs(y[0])

    ret = [0] * (len(x) + len(y))
    for i in range(len(x) - 1, -1, -1):
        for j in range(len(y) - 1, -1, -1):
            ret[i + j + 1] += x[i] * y[j]
            ret[i + j] += ret[i + j + 1] / 10
            ret[i + j + 1] = ret[i + j + 1] % 10
    for i in range(len(x) + len(y)):
        if ret[i] != 0:
            ret = ret[i:]
            break

    if isNegative:
        ret[0] = - ret[0]

    return ret


print multiply_array_positive([1, 2], [9])
print multiply_array([-1, 2], [9])
