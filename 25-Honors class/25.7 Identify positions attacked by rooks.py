def setMatrixZeros(matrix):
    if matrix is None or len(matrix) == 0:
        return
    rows, cols = len(matrix), len(matrix[0])
    needSetFirstRow, needSetFirstCol = False, False
    for i in range(rows):
        if matrix[i][0] == 0:
            needSetFirstCol = True
            break
    for j in range(cols):
        if matrix[0][j] == 0:
            needSetFirstRow = True
            break
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0], matrix[0][j] = 0, 0
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    if needSetFirstRow:
        for j in range(cols):
            matrix[0][j] = 0
    if needSetFirstCol:
        for i in range(rows):
            matrix[i][0] = 0

matrix = [
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]

setMatrixZeros(matrix)

for ele in matrix:
    print ele