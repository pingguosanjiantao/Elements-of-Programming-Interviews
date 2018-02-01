def intersectTwoSortedArrays(a, b):
    ret = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j] and (i == 0 or a[i] != a[i - 1]):
            ret += [a[i]]
            i, j = i + 1, j + 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ret


print intersectTwoSortedArrays([2, 3, 3, 5, 5, 6, 7, 7, 8, 12], [5, 5, 6, 8, 8, 9, 10, 10])
