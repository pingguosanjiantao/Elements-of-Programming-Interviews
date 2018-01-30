def sumRootToLeaf(root):
    def doSumRootToLeaf(root, partialSum):
        if root is None:
            return 0
        partialSum = partialSum * 2 + root.val
        if root.left is None and root.right is None:
            return partialSum
        return doSumRootToLeaf(root.left, partialSum) + doSumRootToLeaf(root.right, partialSum)

    return doSumRootToLeaf(root, 0)
