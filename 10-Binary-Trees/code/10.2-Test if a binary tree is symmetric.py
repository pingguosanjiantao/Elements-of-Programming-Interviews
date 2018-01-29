def isSymetrix(root):
    def checkSymmetric(left, right):
        if left is None and right is None:
            return True
        if left is not None and right is not None:
            return left.val == right.val and checkSymmetric(left.left, right.right) and checkSymmetric(left.right, right.left)
        return False

    return root is None or checkSymmetric(root.left, root.right)
