# coding=utf-8
# amazing problem
def findKthTwoSortedArrays(a, b, k):
    left, right = max(0, k - len(b)), min(len(a), k)
    while left < right:
        x = left + (right - left) / 2

        ax1 = float('-inf') if x <= 0 else a[x - 1]
        ax = float('inf') if x >= len(a) else a[x]
        bkx1 = float('-inf') if k - x <= 0 else b[k - x - 1]
        bkx = float('inf') if k - x >= len(b) else b[k - x]

        if ax < bkx1:
            left = x + 1
        elif ax1 > bkx:
            right = x - 1
        else:
            return max(ax1, bkx1)
    ab1 = float('-inf') if left <= 0 else a[left - 1]
    bkb1 = float('-inf') if k - left - 1 < 0 else b[k - left - 1]
    return max(ab1, bkb1)


print findKthTwoSortedArrays([1, 2, 4, 8], [4, 4, 5, 7], 4)
