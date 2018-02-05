def nQueens(n):
    ret = []
    solveNQueens(n, 0, [], ret)
    return ret


def solveNQueens(n, row, colPlacement, ret):
    if row == n:
        ret += [colPlacement[:]]
    else:
        for col in range(n):
            colPlacement += [col]
            if isValid(colPlacement):
                solveNQueens(n, row + 1, colPlacement, ret)
            colPlacement.pop()


def isValid(colPlacement):
    rowID = len(colPlacement) - 1
    for i in range(rowID):
        diff = abs(colPlacement[i] - colPlacement[rowID])
        if diff == 0 or diff == rowID - i:
            return False
    return True


print nQueens(4)
