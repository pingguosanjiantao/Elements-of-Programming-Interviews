class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# optimal solution
def reconstructPreorder(preorder):
    idx, length = 0, len(preorder)
    def doReconstructPreorder():
        global idx
        if idx == length:
            return None
        root = TreeNode(preorder[idx])
        idx += 1
        left = doReconstructPreorder()
        right = doReconstructPreorder()
        root.left, root.right = left, right
        return root
    return doReconstructPreorder()