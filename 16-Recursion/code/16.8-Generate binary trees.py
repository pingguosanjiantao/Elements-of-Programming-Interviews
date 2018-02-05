class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generateAllBinaryTrees(n):
    ret = []
    if n == 0:
        return [None]
    for leftNodes in range(n):
        rightNodes = n - 1 - leftNodes
        leftSubtrees = generateAllBinaryTrees(leftNodes)
        rightSubtrees = generateAllBinaryTrees(rightNodes)
        for left in leftSubtrees:
            for right in rightSubtrees:
                ret += [TreeNode(0, left, right)]
    return ret


print generateAllBinaryTrees(3)
