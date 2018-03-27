def findBiggestNMinmusOneProduct_basic(A):
    preProduct = [1] * len(A)
    for i in range(len(A)):
        preProduct[i] = A[0] if i == 0 else preProduct[i - 1] * A[i]
    postProduct = 1
    maxProduct = 1
    for i in range(len(A) - 1, -1, -1):
        maxProduct = max(maxProduct, (1 if i == 0 else preProduct[i - 1]) * postProduct)
        postProduct *= A[i]
    return maxProduct


def findBiggestNMinmusOneProduct(A):
    negativeCnt = 0

    minNonnegativeIdx = -1
    maxNegativeIdx = -1
    minNegativeIdx = -1

    for i in range(len(A)):
        if A[i] < 0:
            negativeCnt += 1
            if (minNegativeIdx == -1 or A[minNegativeIdx] < A[i]):
                minNegativeIdx = i
            if maxNegativeIdx == -1 or A[maxNegativeIdx] > A[i]:
                maxNegativeIdx = i
        elif A[i] >= 0:
            if minNonnegativeIdx == -1 or A[i] < A[minNonnegativeIdx]:
                minNonnegativeIdx = i
    product = 1
    if (negativeCnt % 2) != 0:
        idxToSkip = minNegativeIdx
    else:
        idxToSkip = minNonnegativeIdx if minNonnegativeIdx != -1 else maxNegativeIdx
    for i in range(len(A)):
        if i != idxToSkip:
            product *= A[i]
    return product


print findBiggestNMinmusOneProduct_basic([3, 2, 5, 4])
print findBiggestNMinmusOneProduct([3, 2, 5, 4])
