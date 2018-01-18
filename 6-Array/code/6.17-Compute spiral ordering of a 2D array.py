def matrixInSpiralOrder(matrix):
    # representions of rightward, downward, leftward, upward
    SHIFT = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dir, x, y = 0, 0, 0
    length = len(matrix)
    ret = []
    for _ in range(length * length):
        ret += [matrix[x][y]]
        matrix[x][y] = False
        nextX, nextY = x + SHIFT[dir][0], y + SHIFT[dir][1]
        if nextX < 0 or nextX >= length or nextY < 0 or nextY >= length or matrix[nextX][nextY] is False:
            dir = (dir + 1) % 4
            nextX, nextY = x + SHIFT[dir][0], y + SHIFT[dir][1]
        x, y = nextX, nextY
    return ret


data = [[3, 4, 5, 6],
        [14, 15, 16, 7],
        [13, 18, 17, 8],
        [12, 11, 10, 9]]

print matrixInSpiralOrder(data)
