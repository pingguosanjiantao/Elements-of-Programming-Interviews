class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def binaryTreeDepthOrder(root):
    if root is None: return []
    ret = [[root.val]]
    queue = [root]
    while len(queue) > 0:
        cur = queue.pop(0)
        curLevel = []
        if cur.left is not None:
            curLevel += [cur.left.val]
        if cur.right is not None:
            curLevel += [cur.right.val]
        if len(curLevel) > 0:
            ret += [curLevel]
    return ret
