# optimal solution
def queen(A, cur=0):
    if cur == len(A):
        print A
        return
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur + 1)


queen([None] * 4)
