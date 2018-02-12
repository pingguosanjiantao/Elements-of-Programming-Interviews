def searchMaze(maze, s, t):
    def findPath(maze, s, t, path):
        if s == t:
            return True
        SHIFT = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for direct in SHIFT:
            next = [s[0] + direct[0], s[1] + direct[1]]
            if next[0] in range(len(maze)) and next[1] in range(len(maze[0])) and maze[next[0]][next[1]] is True:
                maze[next[0]][next[1]] = False
                path += [next]
                if findPath(maze, next, t, path):
                    return True
                path.pop()

    path = [s]
    maze[s[0]][s[1]] = False
    if not findPath(maze, s, t, path):
        path.pop()
    return path


maze = [
    [True, False, False, False],
    [True, True, True, True]
]
print searchMaze(maze, [0, 0], [1, 3])
