EPSILON = 0.0001


def compare(a, b):
    diff = (a - b) / b
    if diff < - EPSILON:
        return -1
    elif diff > EPSILON:
        return 1
    else:
        return 0


def squareRoot(x):
    if x < 1.0:
        left, right = x, 1
    else:
        left, right = 1.0, x
    while compare(left, right) < 0:
        mid = (right + left) * 0.5
        midSquared = mid * mid
        diff = compare(midSquared, x)
        if diff == 0:
            return mid
        elif diff > 0:
            right = mid
        else:
            left = mid
    return left


print squareRoot(5)
