def nextPermutation(s):
    length = len(s)

    def findAscendIdx():
        for i in range(length - 1, 0, -1):
            if s[i - 1] < s[i]:
                return i
        return 0

    def swapBiggerBackward(idx):
        for i in range(length - 1, idx, -1):
            if s[idx] < s[i]:
                s[idx], s[i] = s[i], s[idx]
                break

    def reverse(left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

    # body
    idx = findAscendIdx()
    if idx > 0:
        swapBiggerBackward(idx - 1)
    reverse(idx, len(s) - 1)
    return s


print nextPermutation([5, 4, 6, 8, 7])
