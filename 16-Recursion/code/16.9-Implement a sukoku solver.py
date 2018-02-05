import math


def solveSudoku(partialAssignment):
    return solvePartialSudoku(0, 0, partialAssignment)


def solvePartialSudoku(i, j, partialAssignment):
    if i == len(partialAssignment):
        i = 0
        j += 1
        if j == len(partialAssignment[i]):
            return True
    if len(partialAssignment[i][j]) != 0:
        return solvePartialSudoku(i + 1, j, partialAssignment)
    for val in range(1, len(partialAssignment) + 1):
        if validToAddVal(partialAssignment, i, j, val):
            partialAssignment[i][j] = val
            if solvePartialSudoku(i + 1, j, partialAssignment):
                return True
    partialAssignment[i][j] = 0
    return False


def validToAddVal(matrix, i, j, val):
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
