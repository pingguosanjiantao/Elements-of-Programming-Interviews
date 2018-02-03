def isBST(root):
    def doIsBST(root, lower, upper):
        if root is None:
            return True
        elif root.val < lower or root.val > upper:
            return False
        else:
            return doIsBST(root.left, lower, root.val) and doIsBST(root.right, root.val, upper)

    return doIsBST(root, float('-inf'), float('inf'))
