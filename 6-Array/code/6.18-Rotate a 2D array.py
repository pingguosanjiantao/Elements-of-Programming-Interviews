def rotateMatrix(matrix):
    length = len(matrix)
    size = length - 1
    for i in range(length / 2):
        for j in range(i, size - i):
            print i,j
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][size - i]
            matrix[j][size - i] = matrix[size - i][size - j]
            matrix[size - i][size - j] = matrix[size - j][i]
            matrix[size - j][i] = tmp
    return matrix


data = [[3,  4,  5,  6],
        [14, 15, 16, 7],
        [13, 18, 17, 8],
        [12, 11, 10, 9]]
print rotateMatrix(data)
