def hasPathSum(root, targetSum):
    def doHasPathSum(root, partialSum, targetSum):
        if root is None:
            return 0
        partialSum += root.val
        if root.left is None and root.right is None:
            return partialSum == targetSum
        return doHasPathSum(root.left, partialSum, targetSum) or doHasPathSum(root.right, partialSum, targetSum)

    return doHasPathSum(root, 0, targetSum)
