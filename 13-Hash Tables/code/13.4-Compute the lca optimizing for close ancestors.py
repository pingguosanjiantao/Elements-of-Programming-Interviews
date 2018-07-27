class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


# on condition that node has the field of parent
def LCA(a, b):
    map = []
    while a or b:
        if a:
            if a in map:
                return a
            map += [a]
            a = a.parent
        if b:
            if b in map:
                return b
            map += [b]
            b = b.parent
    return None


a = TreeNode(1)
b = TreeNode(3)
root = TreeNode(2, a, b)
a.parent = root
b.parent = root

print LCA(a, b).val
