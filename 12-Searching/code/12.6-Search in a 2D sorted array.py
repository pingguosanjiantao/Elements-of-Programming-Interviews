def matrixSearch(matrix, key):
    rows, cols = len(matrix), len(matrix[0])
    i, j = 0, cols - 1
    while i < rows and j >= 0:
        if matrix[i][j] == key:
            return True
        elif matrix[i][j] < key:
            i += 1
        else:
            j -= 1
    return False


data = [[-1, 2, 4],
        [1, 5, 9],
        [3, 6, 10]]
print matrixSearch(data, 6)
