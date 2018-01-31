class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# optimal solution
def binaryTreeFromPreorderInorder(preorder, inorder):
    if preorder is None or inorder is None or len(preorder) == 0 or len(inorder) == 0:
        return None
    root = TreeNode(preorder[0])
    idxInorder = inorder.index(preorder[0])
    idxPreorder = idxInorder + 1
    root.left = binaryTreeFromPreorderInorder(preorder[1:idxPreorder], inorder[:idxInorder])
    root.right = binaryTreeFromPreorderInorder(preorder[idxPreorder:], inorder[idxInorder + 1:])
    return root
