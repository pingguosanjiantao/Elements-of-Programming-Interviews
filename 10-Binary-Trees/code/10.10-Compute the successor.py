def findSuccessor(root):
    if root.right:
        root = root.right
        while root.left:
            root = root.left
        return root
    while root.parent and root.parent.right == root:
        root = root.parent
    return root.parent
