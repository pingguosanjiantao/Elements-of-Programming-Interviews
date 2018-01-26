def squareRoot(k):
    left, right = 0, k
    while left <= right:
        mid = (left + right) / 2
        if mid * mid <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


print squareRoot(17)
