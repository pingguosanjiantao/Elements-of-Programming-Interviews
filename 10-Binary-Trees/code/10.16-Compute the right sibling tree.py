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
    dummy = TreeNode(-1)
    pre, cur = dummy, root
    while cur is not None:
        if cur.left is not None:
            pre.next = cur.left
            pre = pre.next
        if cur.right is not None:
            pre.next = cur.right
            pre = pre.next
        cur = cur.next
    constructRightSibling(dummy.next)
