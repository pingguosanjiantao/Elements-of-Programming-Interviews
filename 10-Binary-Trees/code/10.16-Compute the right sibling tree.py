class TreeNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.left = None
        self.right = None


# optimal solution
def constructRightSibling(root):
    if root is None:
        return
    pre = dummy = TreeNode(-1)
    while root:
        if root.left:
            pre.next = root.left
            pre = pre.next
        if root.right:
            pre.next = root.right
            pre = pre.next
        root = root.next
    constructRightSibling(dummy.next)
