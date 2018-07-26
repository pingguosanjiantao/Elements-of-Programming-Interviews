class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# optimal solution
def isBalanced(root):
    def doIsBalanced(root):
        if root is None:
            return 0
        hl, hr = doIsBalanced(root.left), doIsBalanced(root.right)
        if hl < 0 or hr < 0 or abs(hl - hr) > 1:
            return -1
        return max(hl, hr) + 1

    return doIsBalanced(root) >= 0
