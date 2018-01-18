# coding:utf-8

# In Chinese, it is called 杨辉三角
def generatePascalTriangle(n):
    ret = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or i == j:
                row += [1]
            else:
                row += [ret[-1][j - 1] + ret[-1][j]]
        ret += [row]
    return ret


print generatePascalTriangle(5)
