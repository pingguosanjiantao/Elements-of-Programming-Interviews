def fillSurroundedRegions(matrix):
    if len(matrix) == 0:
        return
    visited = [[False] * len(matrix[0])] * len(matrix)
    for i in range(len(matrix)):
        if matrix[i][0] is True and not visited[i][0]:
            markVisited(matrix, i, 0, visited)
        if matrix[i][len(matrix) - 1] is True and not visited[i][len(matrix) - 1]:
            markVisited(matrix, i, len(matrix) - 1, visited)
    for j in range(len(matrix[0])):
        if matrix[0][j] is True and not visited[0][j]:
            markVisited(matrix, 0, j, visited)
        if matrix[len(matrix) - 1][j] is True and not visited[len(matrix) - 1][j]:
            markVisited(matrix, len(matrix) - 1, j, visited)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] is True and not visited[i][j]:
                matrix[i][j] = False


def markVisited(matirx, i, j, visited):
    SHIFT = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = [[i, j]]
    while len(queue) > 0:
        [x, y] = queue.pop(0)
        visited[x][y] = True
        for direct in SHIFT:
            nextX, nextY = x + direct[0], y + direct[1]
            if nextX in range(len(matrix)) and nextY in range(len(matrix[0])):
                if matrix[nextX][nextY] is True and not visited[nextX][nextY]:
                    queue += [[nextX, nextY]]


matrix = [
    [False, False, False, False],
    [True, False, True, False],
    [False, True, True, False],
    [False, False, False, False]
]
fillSurroundedRegions(matrix)
for m in matrix:
    print m
