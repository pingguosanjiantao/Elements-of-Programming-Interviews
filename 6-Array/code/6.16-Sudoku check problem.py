import math


def checkSudoku(matrix):
    def hasDulplicate(x, y, width, height, length):
        isPresent = [False] * (length + 1)
        for i in range(width):
            for j in range(height):
                idx = matrix[x + i][y + j]
                if idx is not None and isPresent[idx]:
                    return True
                isPresent[idx] = True
        return False

    length = len(matrix)
    # check rows
    for i in range(length):
        if hasDulplicate(i, 0, length, 0, length):
            return False
    # check cols
    for j in range(length):
        if hasDulplicate(0, j, 0, length, length):
            return False
    # check subtab
    numsOfSubtab = int(math.sqrt(length))
    for i in range(0, length, numsOfSubtab):
        for j in range(0, length, numsOfSubtab):
            if hasDulplicate(i, j, numsOfSubtab, numsOfSubtab, length):
                return False
    return True


data = [[2, 4, 3, 1],
        [1, 3, 4, 2],
        [4, 2, 1, 3],
        [3, 1, 2, 4]]
print checkSudoku(data)
