# optimal solution
def queen(A, curRow=0):
    if curRow == len(A):
        print A
    else:
        for col in range(len(A)):
            A[curRow], flag = col, True
            for row in range(curRow):
                # not equal and not diagonal, the diff in horizontal not equals to the diff in vertical
                if A[row] == col or abs(col - A[row]) == curRow - row:
                    flag = False
                    break
            if flag:
                queen(A, curRow + 1)


queen([None] * 4)
