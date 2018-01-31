def findSuccessor(root):
    if root.right is not None:
        root = root.right
        while root.left is not None:
            root = root.left
        return root
    while root.parent is not None and root.parent.right == root:
        root = root.parent
    return root.parent
