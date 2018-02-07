import math


def solveSudoku(matrix):
    return doSolveSudoku(0, 0, matrix)


def doSolveSudoku(i, j, matrix):
    if i == len(matrix):
        i, j = 0, j + 1
        if j == len(matrix[i]):
            return True
    if len(matrix[i][j]) != 0:
        return doSolveSudoku(i + 1, j, matrix)
    for val in range(1, len(matrix) + 1):
        if isValid(matrix, i, j, val):
            matrix[i][j] = val
            if doSolveSudoku(i + 1, j, matrix):
                return True
    matrix[i][j] = 0
    return False


def isValid(matrix, i, j, val):
    for row in range(len(matrix)):
        if row[j] == val:
            return False
    for col in range(len(matrix[0])):
        if matrix[i][col] == val:
            return False
    regionSize = math.sqrt(len(matrix))
    I, J = i / regionSize, j / regionSize
    for a in range(regionSize):
        for b in range(regionSize):
            if matrix[I * regionSize + a][J * regionSize + b] == val:
                return False
    return True
