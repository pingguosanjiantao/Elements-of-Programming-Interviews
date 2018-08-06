def findFirstGreater(root, k):
    ret = None
    while root:
        if k < root.val:
            ret = root.val
            root = root.left
        else:
            root = root.right
    return ret