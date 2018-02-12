def flipColor(matrix, x, y):
    SHIFT = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    color = matrix[x][y]
    matrix[x][y] = not color
    for direct in SHIFT:
        nextX, nextY = x + direct[0], y + direct[1]
        if nextX in range(len(matrix)) and nextY in range(len(matrix[0])) and matrix[nextX][nextY] == color:
            flipColor(matrix, nextX, nextY)


matrix = [
    [False, True, False, True],
    [True, True, False, True],
    [False, False, False, True],
    [True, False, True, False],
    [False, True, False, True]
]
flipColor(matrix, 2, 1)
for m in matrix:
    print m
