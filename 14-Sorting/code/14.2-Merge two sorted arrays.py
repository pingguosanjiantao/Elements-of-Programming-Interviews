def mergeTwoSortedArrays(a, aLength, b, bLength):
    i, j = aLength - 1, bLength - 1
    idx = aLength + bLength - 1
    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            a[idx] = a[i]
            i -= 1
        else:
            a[idx] = b[j]
            j -= 1
        idx -= 1
    while j >= 0:
        a[idx] = b[j]
        idx -= 1
        j -= 1
    return a


print mergeTwoSortedArrays([5, 13, 17, 0, 0, 0, 0], 3, [3, 7, 11, 19], 4)
