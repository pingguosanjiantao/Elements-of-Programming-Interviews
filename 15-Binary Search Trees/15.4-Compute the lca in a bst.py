def findLCA(root, a, b):
    while root.val < a.val or root.val > b.val:
        while root.val < a.val:
            root = root.right
        while root.val > root.val:
            root = root.left
    return root
