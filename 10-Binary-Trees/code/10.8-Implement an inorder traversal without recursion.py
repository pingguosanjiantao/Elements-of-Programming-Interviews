# optimal solution
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorderTraversal(root):
    if root is None:
        return []
    stack = [root]
    ret = []
    while len(stack) > 0:
        cur = stack.pop()
        if cur.left is None and cur.right is None:
            ret += [cur.val]
        else:
            if cur.right is not None:
                stack += [cur.right]
            stack += [TreeNode(cur.val)]
            if cur.left is not None:
                stack += [cur.left]
    return ret
