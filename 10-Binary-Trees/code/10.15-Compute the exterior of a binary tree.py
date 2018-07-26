class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# a very amaznig problem, this is not a optimal solution
# leftTraversal is preorder, and rightTraversal is postorder
# rootTraversal is inorder
def exteriorBinaryTree(root):
    ret = []

    def isLeaf(root):
        return root.left is None and root.right is None

    def leftTraversal(root, isBoundary):
        ret = []
        if root is not None:
            if isBoundary or isLeaf(root):
                ret += [root.val]
            ret += leftTraversal(root.left, isBoundary)
            ret += leftTraversal(root.right, isBoundary and root.left is None)
        return ret

    def rightTraversal(root, isBoundary):
        ret = []
        if root is not None:
            ret += rightTraversal(root.left, isBoundary and root.right is None)
            ret += rightTraversal(root.right, isBoundary)
            if isBoundary or isLeaf(root):
                ret += [root.val]
        return ret

    if root is not None:
        ret += [root.val]
        ret += leftTraversal(root.left, True)
        ret += rightTraversal(root.right, True)
    return ret


root = TreeNode(5)
left = TreeNode(3)
right = TreeNode(7)
root.left = left
root.right = right
right.left = TreeNode(6)
right.right = TreeNode(8)

print exteriorBinaryTree(root)
