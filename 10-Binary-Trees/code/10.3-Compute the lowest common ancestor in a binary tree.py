# using dfs
def findLCA(root, a, b):
    def doFindLCA(root, a, b):
        if root is None:
            return [0, None]
        leftRet = doFindLCA(root.left, a, b)
        if leftRet[0] is 2:
            return leftRet
        rightRet = doFindLCA(root.right, a, b)
        if rightRet[0] is 2:
            return rightRet
        nums = leftRet[0] + rightRet[0]
        nums += 1 if root.val == a else 0
        nums += 1 if root.val == b else 0
        return nums, root if nums == 2 else None

    return findLCA(root, a, b)[1]
