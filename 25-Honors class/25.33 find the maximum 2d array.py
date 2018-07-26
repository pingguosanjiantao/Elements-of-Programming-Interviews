# coding:utf-8
# 1.寻找最大的正方形
def maxSquareSubmatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    maxHW = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                maxH = maxHW[i - 1][j][0] + 1 if i - 1 >= 0 else 1
                maxW = maxHW[i][j - 1][1] + 1 if j - 1 >= 0 else 1
                maxHW[i][j] = [maxH, maxW]
    maxSide = [[0 for _ in range(cols)] for _ in range(rows)]
    maxSquareArea = 0
    for i in range(rows):
        for j in range(cols):
            side = min(maxHW[i][j])
            if matrix[i][j] == 1:
                if i - 1 >= 0 and j - 1 >= 0:
                    side = min(maxSide[i - 1][j - 1] + 1, side)
                maxSide[i][j] = side
                maxSquareArea = max(maxSquareArea, side * side)
    return maxSquareArea

def maxSquareSubmatrix_2(matrix):
    if matrix == []:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    ans = 0  # 最长边
    for i in range(rows):
        for j in range(cols):
            dp[i][j] = int(matrix[i][j])
            if i > 0 and j > 0 and dp[i][j] > 0:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
            ans = max(ans, dp[i][j])
    return ans * ans

# 2.寻找最大长方形
def maxRectangleSubmatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    maxHW = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                maxH = maxHW[i - 1][j][0] + 1 if i - 1 >= 0 else 1
                maxW = maxHW[i][j - 1][1] + 1 if j - 1 >= 0 else 1
                maxHW[i][j] = [maxH, maxW]
    maxRectangleArea = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and maxHW[i][j][0] * maxHW[i][j][1] > maxRectangleArea:
                minW = float('inf')
                for k in range(maxHW[i][j][0]):
                    minW = min(minW, maxHW[i - k][j][1])
                    maxRectangleArea = max(maxRectangleArea, minW * (k + 1))
    return maxRectangleArea


# 2.寻找最大长方形_2
# copied from 18.8
def getLargestRectangle(nums):
    ret = 0
    stack = []  # store the idx of stepping up
    for i in range(len(nums) + 1):
        # update the idx of same value
        if len(stack) > 0 and i < len(nums) and nums[i] == nums[stack[-1]]:
            stack[-1] = i
        # maximum the rectangle
        while len(stack) > 0 and (i == len(nums) or nums[i] < nums[stack[-1]]):
            height = nums[stack.pop()]
            head = -1 if len(stack) == 0 else stack[-1]
            width = i - 1 - head
            ret = max(ret, height * width)
        stack += [i]
    return ret


def maxRectangleSubmatrix_2(matrix):
    rows, cols = len(matrix), len(matrix[0])
    matrixLine = [0] * cols
    maxRectangleArea = 0
    for i in range(rows):
        for j in range(cols):
            matrixLine[j] = matrixLine[j] + 1 if matrix[i][j] == 1 else 0
        maxRectangleArea = max(maxRectangleArea, getLargestRectangle(matrixLine[:]))
    return maxRectangleArea

# 寻找最大面积, 不规则
class UnionFind:
    def __init__(self, length):
        self.data = {}
        for i in range(length):
            self.data[i] = i
    def find(self, k):
        while self.data[k] != k:
            k = self.data[k]
        return k
    def union(self, a, b):
        aRoot, bRoot = self.find(a), self.find(b)
        if aRoot != bRoot:
            self.data[aRoot] = bRoot
def maxArea(matrix):
    rows, cols = len(matrix), len(matrix[0])
    uf = UnionFind(rows * cols)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                # union upper
                if i - 1 >= 0 and matrix[i - 1][j] == 1:
                    uf.union(i * cols + j, (i - 1) * cols + j)
                # union left
                if j - 1 >= 0 and matrix[i][j - 1] == 1:
                    uf.union(i * cols + j, i * cols + (j - 1))
    counter = {}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                root = uf.find(i * cols + j)
                counter[root] = counter.get(root, 0) + 1
    return max(counter.values())

matrix = [
    [1, 1, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
print maxSquareSubmatrix(matrix)
print maxSquareSubmatrix_2(matrix)
print maxRectangleSubmatrix(matrix)
print maxRectangleSubmatrix_2(matrix)
print maxArea(matrix)
