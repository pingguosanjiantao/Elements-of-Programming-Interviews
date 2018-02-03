def findFirstGreater(root, k):
    ret = None
    while root is not None:
        if root.val > k:
            ret = root.val
            root = root.left
        else:
            root = root.right
    return ret