class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# optimal solution
def reconstructPreorder(preorder):
    def doReconstructPreorder():
        if preorder[0] == 'null':
            preorder.pop(0)
            return None
        root = TreeNode(preorder.pop())
        left = doReconstructPreorder()
        right = doReconstructPreorder()
        root.left, root.right = left, right
        return root
    return doReconstructPreorder()