# optimal solution
def queen(A, cur=0):
    if cur == len(A):
        print A
    else:
        for col in range(len(A)):
            A[cur] = col
            if isValid(A, cur, col):
                queen(A, cur + 1)


def isValid(A, cur, col):
    for pre in range(cur):
        # not equal and not diagonal, the diff in horizontal not equals to the diff in vertical
        if A[pre] == col or abs(col - A[pre]) == cur - pre:
            return False
    return True


queen([None] * 4)
